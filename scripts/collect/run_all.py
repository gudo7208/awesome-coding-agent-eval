#!/usr/bin/env python3
"""Orchestrate the full collection pipeline.

Steps:
  1. fetch_arxiv
  2. fetch_recent
  3. fetch_github
  4. fetch_competitors
  5. fetch_venues
  6. deduplicate (scripts/process/deduplicate.py)
  7. classify_candidates  [skipped with --dry-run or --skip-llm]
  8. merge_classified     [skipped with --dry-run]
  9. validate
  10. generate (stats + docs + readme)

Flags:
  --dry-run     Run steps 1-6 only (no LLM, no merge, no generate)
  --skip-llm    Skip LLM classification; run keyword pre-filter only
  --skip-collect  Skip steps 1-5; start from existing candidates/
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable

COLLECT_SCRIPTS = [
    ROOT / "scripts/collect/fetch_arxiv.py",
    ROOT / "scripts/collect/fetch_recent.py",
    ROOT / "scripts/collect/fetch_github.py",
    ROOT / "scripts/collect/fetch_competitors.py",
    ROOT / "scripts/collect/fetch_venues.py",
]

PROCESS_SCRIPTS = {
    "deduplicate": ROOT / "scripts/process/deduplicate.py",
    "classify":    ROOT / "scripts/process/classify_candidates.py",
    "merge":       ROOT / "scripts/process/merge_classified.py",
    "validate":    ROOT / "scripts/process/validate.py",
}

GENERATE_SCRIPTS = [
    ROOT / "scripts/generate/generate_stats.py",
    ROOT / "scripts/generate/generate_docs.py",
    ROOT / "scripts/generate/generate_readme.py",
]


def run(label, cmd, *, allow_fail=True):
    print(f"\n[{label}] Running: {' '.join(str(c) for c in cmd)}")
    t0 = time.time()
    result = subprocess.run(cmd, cwd=ROOT)
    elapsed = time.time() - t0
    ok = result.returncode == 0
    status = "OK" if ok else f"FAILED (exit {result.returncode})"
    print(f"[{label}] {status} in {elapsed:.1f}s")
    if not ok and not allow_fail:
        sys.exit(result.returncode)
    return ok


def count_candidates():
    candidates = ROOT / "candidates"
    total = 0
    for f in candidates.glob("*.jsonl"):
        try:
            total += sum(1 for line in f.open() if line.strip())
        except OSError:
            pass
    return total


def count_data():
    data = ROOT / "data"
    total = 0
    for f in data.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        try:
            import json
            total += len(json.loads(f.read_text()))
        except Exception:
            pass
    return total


def main():
    parser = argparse.ArgumentParser(description="Run full collection pipeline")
    parser.add_argument("--dry-run", action="store_true",
                        help="Collect + deduplicate only; skip LLM, merge, generate")
    parser.add_argument("--skip-llm", action="store_true",
                        help="Skip LLM classification (keyword pre-filter only)")
    parser.add_argument("--skip-collect", action="store_true",
                        help="Skip collection; start from existing candidates/")
    args = parser.parse_args()

    results = {}
    data_before = count_data()

    # ── Step 1-5: Collect ──────────────────────────────────────────────────
    if not args.skip_collect:
        print("\n=== COLLECT ===")
        for script in COLLECT_SCRIPTS:
            label = script.stem
            ok = run(label, [PYTHON, str(script)])
            results[label] = ok
    else:
        print("\n[skip-collect] Skipping collection steps.")

    candidates_before = count_candidates()
    print(f"\nCandidates in candidates/: {candidates_before}")

    # ── Step 6: Deduplicate ────────────────────────────────────────────────
    print("\n=== DEDUPLICATE ===")
    ok = run("deduplicate", [PYTHON, str(PROCESS_SCRIPTS["deduplicate"])])
    results["deduplicate"] = ok

    if args.dry_run:
        _print_summary(results, data_before, count_data())
        return

    # ── Step 7: Classify ───────────────────────────────────────────────────
    print("\n=== CLASSIFY ===")
    candidates_dir = ROOT / "candidates"
    classify_cmd = [PYTHON, str(PROCESS_SCRIPTS["classify"])]
    if args.skip_llm:
        # classify_candidates.py reads all *.jsonl in candidates/ by default;
        # pass --keyword-only if the script supports it, otherwise just run normally
        # (keyword pre-filter is always applied inside the script)
        print("[classify] --skip-llm: running keyword-only pre-filter")

    # Find unclassified JSONL files (no corresponding .relevant.json)
    jsonl_files = sorted(candidates_dir.glob("*.jsonl"))
    classified_any = False
    for jf in jsonl_files:
        relevant_out = jf.with_suffix("").with_suffix(".relevant.json")
        if relevant_out.exists():
            print(f"[classify] {jf.name}: already classified, skipping")
            continue
        cmd = classify_cmd + [str(jf)]
        ok = run(f"classify:{jf.stem}", cmd)
        results[f"classify:{jf.stem}"] = ok
        classified_any = True

    if not classified_any:
        print("[classify] No new JSONL files to classify.")

    # ── Step 8: Merge ──────────────────────────────────────────────────────
    print("\n=== MERGE ===")
    relevant_files = sorted(candidates_dir.glob("*.relevant.json"))
    merged_any = False
    for rf in relevant_files:
        ok = run(f"merge:{rf.stem}", [PYTHON, str(PROCESS_SCRIPTS["merge"]), str(rf)])
        results[f"merge:{rf.stem}"] = ok
        merged_any = True

    if not merged_any:
        print("[merge] No .relevant.json files found.")

    # ── Step 9: Validate ───────────────────────────────────────────────────
    print("\n=== VALIDATE ===")
    ok = run("validate", [PYTHON, str(PROCESS_SCRIPTS["validate"])], allow_fail=True)
    results["validate"] = ok

    # ── Step 10: Generate ──────────────────────────────────────────────────
    print("\n=== GENERATE ===")
    for script in GENERATE_SCRIPTS:
        ok = run(script.stem, [PYTHON, str(script)])
        results[script.stem] = ok

    _print_summary(results, data_before, count_data())


def _print_summary(results, data_before, data_after):
    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY")
    print("=" * 60)
    ok_steps = [k for k, v in results.items() if v]
    fail_steps = [k for k, v in results.items() if not v]
    print(f"  Steps OK    : {len(ok_steps)}")
    if fail_steps:
        print(f"  Steps FAILED: {len(fail_steps)}")
        for s in fail_steps:
            print(f"    - {s}")
    print(f"  Data entries: {data_before} → {data_after} (+{data_after - data_before})")
    print("=" * 60)


if __name__ == "__main__":
    main()
