"""
Build cross-references (related field) for data/*.json entries.

Four-step strategy:
  Step 1: Rule-based (explicit clusters + ID prefix matching for known series)
  Step 2: Exact tag matching (toolchain/meta/leaderboard tags that exactly match benchmark IDs)
  Step 3: Subcategory-based variants (small subcategories only, max 20 members)
  Step 4: LLM-assisted (for high-star benchmarks still missing relations)
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import requests

DATA_DIR = Path(__file__).parent.parent.parent / "data"

LLM_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8990/cc") + "/v1/messages"
LLM_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = "claude-sonnet-4-6"


def load_file(fname: str) -> list[dict]:
    with open(DATA_DIR / fname) as f:
        data = json.load(f)
    return data if isinstance(data, list) else data.get("items", [])


def save_file(fname: str, items: list[dict]) -> None:
    path = DATA_DIR / fname
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
        f.write("\n")
    tmp.rename(path)


def empty_related() -> dict:
    return {"harness": [], "leaderboard": [], "meta_analysis": [], "variants": []}


def merge_related(base: dict | None, patch: dict) -> dict:
    result = empty_related()
    if base:
        for k in result:
            result[k] = list(base.get(k) or [])
    for k, vals in patch.items():
        for v in vals:
            if v not in result[k]:
                result[k].append(v)
    return result


def is_empty_related(r: dict | None) -> bool:
    if not r:
        return True
    return not any(r.get(k) for k in ("harness", "leaderboard", "meta_analysis", "variants"))


def add_rel(updates: dict, item_id: str, rel_type: str, targets: list[str], all_ids: set[str]) -> None:
    if item_id not in updates:
        updates[item_id] = empty_related()
    for t in targets:
        if t in all_ids and t != item_id and t not in updates[item_id][rel_type]:
            updates[item_id][rel_type].append(t)


# ---------------------------------------------------------------------------
# Step 1: Rule-based relations
# ---------------------------------------------------------------------------

# Explicit variant clusters: each group is mutually related as variants
VARIANT_CLUSTERS = [
    ["swe-bench", "swe-bench-verified", "swe-bench-pro", "swe-bench-multimodal"],
    ["humaneval", "humaneval-x", "humaneval-plus"],
    ["bigcodebench", "bigcodebench-benchmarking-code-generation-with-diverse-funct"],
    ["livecodebench", "livecodebench-leaderboard"],
]

# Explicit harness links: benchmark_id -> [harness_ids]
EXPLICIT_HARNESS: dict[str, list[str]] = {
    "swe-bench": ["swe-bench-harness", "openhands-eval-harness", "aider-swe-bench", "swe-bench-docker"],
    "swe-bench-verified": ["swe-bench-harness", "openhands-eval-harness", "aider-swe-bench"],
    "swe-bench-multimodal": ["swe-bench-harness"],
    "swe-bench-pro": ["swe-bench-harness"],
    "bigcodebench": ["bigcode-evaluation-harness"],
    "bigcodebench-benchmarking-code-generation-with-diverse-funct": ["bigcode-evaluation-harness"],
    "humaneval": ["bigcode-evaluation-harness"],
    "livecodebench": ["bigcode-evaluation-harness"],
}

# Explicit leaderboard links: benchmark_id -> [leaderboard_ids]
EXPLICIT_LEADERBOARD: dict[str, list[str]] = {
    "swe-bench": ["swe-bench-leaderboard", "swe-bench-leaderboard-march-2026", "showdown"],
    "swe-bench-verified": ["swe-bench-leaderboard", "swe-bench-verified-epoch-ai-benchmark-page"],
    "swe-bench-multimodal": ["swe-bench-leaderboard"],
    "swe-bench-pro": ["auggie-tops-swe-bench-pro"],
    "livecodebench": ["livecodebench-leaderboard", "2026-4"],
    "bigcodebench": ["bigcodebench-leaderboard"],
    "bigcodebench-benchmarking-code-generation-with-diverse-funct": ["bigcodebench-leaderboard"],
    "humaneval": ["evalplus-leaderboard"],
}

# Explicit meta_analysis links: benchmark_id -> [meta_analysis_ids]
EXPLICIT_META: dict[str, list[str]] = {
    "swe-bench": [
        "metr-merge-rate", "swe-bench-score-gap",
        "are-solved-issues-in-swe-bench-really-solved-corre",
        "ai-benchmarks-are-broken-and-nobody-wants-to-admit",
        "why-swe-bench-verified-no-longer-measures-frontier",
        "what-skills-does-swe-bench-verified-evaluate",
        "the-end-of-swe-bench-verified-mia-glaese-olivia-wa",
        "openai-abandons-swe-bench-verified-after-finding-5",
        "oracle-swe-quantifying-the-contribution-of-oracle-",
        "nilenso-what-benchmarks-measure",
        "swe-bench-enhanced-coding-benchmark-for-llms",
        "some-critical-issues-with-the-swe-bench-dataset-hn",
        "state-of-code-evals-after-swe-bench-code-clash-sot",
    ],
    "swe-bench-verified": [
        "metr-merge-rate", "swe-bench-score-gap",
        "why-swe-bench-verified-no-longer-measures-frontier",
        "what-skills-does-swe-bench-verified-evaluate",
        "the-end-of-swe-bench-verified-mia-glaese-olivia-wa",
    ],
    "swe-bench-pro": ["swe-bench-score-gap"],
}


def apply_rule_relations(all_ids: set[str], updates: dict[str, dict]) -> None:
    # Variant clusters
    for cluster in VARIANT_CLUSTERS:
        valid = [x for x in cluster if x in all_ids]
        for item_id in valid:
            others = [x for x in valid if x != item_id]
            add_rel(updates, item_id, "variants", others, all_ids)

    # Explicit harness
    for item_id, harnesses in EXPLICIT_HARNESS.items():
        add_rel(updates, item_id, "harness", harnesses, all_ids)

    # Explicit leaderboard
    for item_id, lbs in EXPLICIT_LEADERBOARD.items():
        add_rel(updates, item_id, "leaderboard", lbs, all_ids)

    # Explicit meta_analysis
    for item_id, metas in EXPLICIT_META.items():
        add_rel(updates, item_id, "meta_analysis", metas, all_ids)


# ---------------------------------------------------------------------------
# Step 2: Exact tag matching
# ---------------------------------------------------------------------------

# Tags that are too generic to use for matching
GENERIC_TAGS = {
    "benchmark", "evaluation", "code-generation", "llm", "python", "open-source",
    "multi-language", "harness", "sandbox", "security", "testing", "agent",
    "evaluation-framework", "code-execution", "docker", "safety", "monitoring",
    "repository", "llm-eval", "automation", "trajectory", "environment-setup",
    "agent-framework", "github-issues", "software-engineering", "code-understanding",
    "code-review", "multi-agent", "agent-evaluation", "long-horizon", "test-generation",
    "benchmark-analysis", "survey", "meta-analysis", "leaderboard", "ranking",
    "coding", "coding-agent", "llm-benchmark", "benchmark-survey", "benchmark-comparison",
    "code-completion", "competitive-programming", "contamination-free", "function-level",
    "library-use", "humaneval", "mbpp", "test-augmentation", "evalplus",
    "polyglot", "exercism", "llm-ranking", "agentic-coding", "benchmark-aggregation",
    "elo", "multi-step-reasoning", "tool-use", "activity", "github-bot", "pr-merge-rate",
    "production", "real-world", "enterprise", "reliability", "practitioner-survey",
    "adoption-barriers", "continuous-eval", "deployment", "multi-signal",
    "adoption", "github", "coding-agents", "julia", "claude-code", "activity-tracking",
    "agent-leaderboard", "computer-use", "human-eval", "open-data", "community-driven",
    "debugging", "multilingual", "terminal-bench", "aider-polyglot",
    "epoch-ai", "bug-fix", "agent-ranking", "patch-generation", "se-agent",
    "model-ranking", "benchmark-result", "lm-arena", "coding-leaderboard", "blog",
    "benchmarks", "leaderboard", "livecodebench",
}


def apply_exact_tag_relations(
    benchmarks: list[dict],
    toolchain: list[dict],
    meta_analysis: list[dict],
    leaderboards: list[dict],
    updates: dict[str, dict],
    all_ids: set[str],
) -> None:
    bench_ids = {b["id"] for b in benchmarks}

    # Build reverse index: benchmark_id -> list of toolchain/meta/leaderboard that reference it
    bench_to_harness: dict[str, list[str]] = {}
    bench_to_meta: dict[str, list[str]] = {}
    bench_to_lb: dict[str, list[str]] = {}

    for tc in toolchain:
        for tag in tc.get("tags", []):
            if tag in bench_ids and tag not in GENERIC_TAGS:
                bench_to_harness.setdefault(tag, []).append(tc["id"])

    for ma in meta_analysis:
        for tag in ma.get("tags", []):
            if tag in bench_ids and tag not in GENERIC_TAGS:
                bench_to_meta.setdefault(tag, []).append(ma["id"])

    for lb in leaderboards:
        for tag in lb.get("tags", []):
            if tag in bench_ids and tag not in GENERIC_TAGS:
                bench_to_lb.setdefault(tag, []).append(lb["id"])

    # Apply to benchmarks
    for bench in benchmarks:
        bid = bench["id"]
        if bid in bench_to_harness:
            add_rel(updates, bid, "harness", bench_to_harness[bid], all_ids)
        if bid in bench_to_meta:
            add_rel(updates, bid, "meta_analysis", bench_to_meta[bid], all_ids)
        if bid in bench_to_lb:
            add_rel(updates, bid, "leaderboard", bench_to_lb[bid], all_ids)

    # Benchmark-to-benchmark: if bench B's tags reference bench A's id,
    # B is likely a study/extension of A -> add B to A's meta_analysis
    # Only treat as variant if B's name/id contains A's name (explicit fork/extension)
    for bench in benchmarks:
        bid = bench["id"]
        bname_norm = bid.lower().replace("-", "")
        for tag in bench.get("tags", []):
            if tag in bench_ids and tag != bid and tag not in GENERIC_TAGS:
                tag_norm = tag.lower().replace("-", "")
                # If bid contains the referenced benchmark's id -> it's a variant/extension
                if tag_norm in bname_norm:
                    add_rel(updates, bid, "variants", [tag], all_ids)
                    add_rel(updates, tag, "variants", [bid], all_ids)
                else:
                    # Otherwise: bid is a study/method evaluated on tag benchmark
                    # Add bid to tag's meta_analysis (bid studies/extends tag)
                    add_rel(updates, tag, "meta_analysis", [bid], all_ids)


# ---------------------------------------------------------------------------
# Step 3: Subcategory-based variants (small subcategories only)
# ---------------------------------------------------------------------------

# Max subcategory size to auto-link as variants
SUBCAT_MAX_SIZE = 20


def apply_subcategory_relations(
    benchmarks: list[dict],
    updates: dict[str, dict],
    all_ids: set[str],
) -> None:
    from collections import defaultdict
    subcat_groups: dict[str, list[str]] = defaultdict(list)
    for b in benchmarks:
        sc = b.get("subcategory", "")
        if sc:
            subcat_groups[sc].append(b["id"])

    for sc, ids in subcat_groups.items():
        if len(ids) <= SUBCAT_MAX_SIZE:
            for bid in ids:
                others = [x for x in ids if x != bid]
                add_rel(updates, bid, "variants", others, all_ids)


# ---------------------------------------------------------------------------
# Step 4: LLM-assisted relations
# ---------------------------------------------------------------------------

def call_llm(prompt: str) -> str | None:
    try:
        resp = requests.post(
            LLM_URL,
            headers={
                "x-api-key": LLM_KEY,
                "content-type": "application/json",
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": LLM_MODEL,
                "max_tokens": 512,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["content"][0]["text"]
    except Exception as e:
        print(f"  LLM call failed: {e}", file=sys.stderr)
        return None


def parse_llm_ids(text: str, valid_ids: set[str]) -> dict:
    result = empty_related()
    current_key = None
    for line in text.splitlines():
        line = line.strip()
        low = line.lower()
        if low.startswith("harness:"):
            current_key = "harness"
            line = line[len("harness:"):].strip()
        elif low.startswith("leaderboard:"):
            current_key = "leaderboard"
            line = line[len("leaderboard:"):].strip()
        elif low.startswith("meta_analysis:") or low.startswith("meta-analysis:"):
            current_key = "meta_analysis"
            line = line.split(":", 1)[1].strip()
        elif low.startswith("variants:"):
            current_key = "variants"
            line = line[len("variants:"):].strip()
        if current_key and line:
            for part in re.split(r"[,\s]+", line):
                part = part.strip()
                if part in valid_ids:
                    if part not in result[current_key]:
                        result[current_key].append(part)
    return result


def apply_llm_relations(
    benchmarks: list[dict],
    toolchain: list[dict],
    meta_analysis: list[dict],
    leaderboards: list[dict],
    updates: dict[str, dict],
    all_ids: set[str],
    star_threshold: int = 50,
) -> None:
    tc_ids = [x["id"] for x in toolchain]
    ma_ids = [x["id"] for x in meta_analysis]
    lb_ids = [x["id"] for x in leaderboards]
    all_candidate_ids = set(tc_ids + ma_ids + lb_ids)

    candidates = [
        b for b in benchmarks
        if (b.get("stars") or 0) >= star_threshold
        and is_empty_related(updates.get(b["id"]))
    ]

    print(f"  LLM step: {len(candidates)} benchmarks with stars>={star_threshold} and no relations")

    for bench in candidates:
        bid = bench["id"]
        bname = bench.get("name", bid)
        bwhat = bench.get("what", "")

        prompt = f"""You are helping build a cross-reference index for a code benchmark catalog.

Benchmark: {bname}
ID: {bid}
Description: {bwhat}

From the lists below, identify which entries are related to this benchmark.
Only include entries that are CLEARLY related (same benchmark family, evaluation harness specifically for it, leaderboard tracking it, or meta-analysis studying it).
Be conservative — only include strong matches.

Toolchain IDs (harness/evaluation infrastructure):
{chr(10).join(tc_ids)}

Meta-analysis IDs:
{chr(10).join(ma_ids)}

Leaderboard IDs:
{chr(10).join(lb_ids)}

Reply in this exact format (omit sections with no matches):
harness: <id1>, <id2>
leaderboard: <id1>
meta_analysis: <id1>, <id2>
variants: (leave empty)

Only include IDs from the lists above. If nothing matches, reply: none"""

        print(f"  LLM: querying for {bid}...")
        text = call_llm(prompt)
        if not text or text.strip().lower() == "none":
            continue

        parsed = parse_llm_ids(text, all_candidate_ids)
        for k, vals in parsed.items():
            add_rel(updates, bid, k, vals, all_ids)

        time.sleep(0.3)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading data files...")
    benchmarks = load_file("benchmarks.json")
    leaderboards = load_file("leaderboards.json")
    meta_analysis = load_file("meta-analysis.json")
    toolchain = load_file("toolchain.json")

    all_ids: set[str] = set()
    for items in [benchmarks, leaderboards, meta_analysis, toolchain]:
        all_ids.update(x["id"] for x in items)

    updates: dict[str, dict] = {}

    # Step 1
    print("Step 1: Rule-based relations...")
    apply_rule_relations(all_ids, updates)
    step1_count = sum(1 for v in updates.values() if not is_empty_related(v))
    print(f"  {step1_count} entries updated by rules")

    # Step 2
    print("Step 2: Exact tag matching...")
    apply_exact_tag_relations(benchmarks, toolchain, meta_analysis, leaderboards, updates, all_ids)
    step2_count = sum(1 for v in updates.values() if not is_empty_related(v))
    print(f"  {step2_count} entries have relations after exact tag step")

    # Step 3
    print("Step 3: Subcategory-based variants...")
    apply_subcategory_relations(benchmarks, updates, all_ids)
    step3_count = sum(1 for v in updates.values() if not is_empty_related(v))
    print(f"  {step3_count} entries have relations after subcategory step")

    # Step 4
    print("Step 4: LLM-assisted relations...")
    apply_llm_relations(benchmarks, toolchain, meta_analysis, leaderboards, updates, all_ids)
    step4_count = sum(1 for v in updates.values() if not is_empty_related(v))
    print(f"  {step4_count} entries have relations after LLM step")

    # Write back to benchmarks.json
    print("Writing back to benchmarks.json...")
    changed = 0
    for item in benchmarks:
        bid = item["id"]
        patch = updates.get(bid)
        if patch and not is_empty_related(patch):
            new_related = merge_related(item.get("related"), patch)
            if new_related != item.get("related"):
                item["related"] = new_related
                changed += 1

    save_file("benchmarks.json", benchmarks)
    print(f"  {changed} benchmark entries updated")

    # Stats
    total = len(benchmarks)
    has_related = sum(1 for x in benchmarks if not is_empty_related(x.get("related")))
    coverage = has_related / total * 100 if total else 0
    print(f"\nFinal coverage: {has_related}/{total} = {coverage:.1f}%")

    if coverage < 70:
        print("WARNING: coverage < 70%, target not met", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
