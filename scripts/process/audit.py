#!/usr/bin/env python3
"""Deep data-quality audit for data/*.json.

Goes beyond validate.py (schema/id/link) to catch the *semantic* defects that
silently degrade the collection:

  1. dangling-refs     related.* pointing to non-existent ids
  2. self-refs         an entry referencing its own id
  3. taxonomy          subcategory outside the documented per-stage vocabulary
  4. eval-method       eval_method outside the documented vocabulary
  5. what-too-long     what > 80 chars (convention) / > 200 (schema hard cap)
  6. what-truncated    what looks cut off mid-sentence
  7. name-truncated    name looks cut off mid-word
  8. dup-url           same paper/repo/website URL on multiple entries
  9. dup-name          same normalized name on multiple entries
 10. type-link         type vs presence of paper/repo links is inconsistent
 11. bad-url           a link field that is not a well-formed http(s) URL

Exit code is 0 always (report-only); use --strict to exit 1 when any
*error-level* finding exists (dangling-refs, self-refs, dup-url, bad-url).

Usage:
    python scripts/process/audit.py [--json OUT] [--strict]
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from taxonomy import RELATED_KEYS, VALID_EVAL_METHODS, VALID_SUBCATEGORIES

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
SKIP = {"schema.json", "stats.json"}
MAX_SHOWN = 8  # findings printed per category before "... and N more"

# function words that signal a `what` was cut mid-sentence
DANGLING_TAIL = {
    "the", "a", "an", "and", "or", "of", "for", "to", "with", "in", "on",
    "at", "by", "from", "that", "which", "using", "via", "as", "is", "are",
    "this", "their", "its", "into", "across", "over", "under", "between",
}
URL_RE = re.compile(r"^https?://", re.I)


def load_all():
    """Return (entries, file_of_id) where entries is list of (entry, filename)."""
    entries = []
    for f in sorted(DATA.glob("*.json")):
        if f.name in SKIP:
            continue
        for item in json.loads(f.read_text()):
            entries.append((item, f.name))
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="write full findings as JSON to this path")
    ap.add_argument("--strict", action="store_true", help="exit 1 on error-level findings")
    args = ap.parse_args()

    entries = load_all()
    all_ids = {e["id"] for e, _ in entries}
    findings = defaultdict(list)

    # URL / name indexes for duplicate detection
    url_index = defaultdict(list)      # normalized url -> [id, ...]
    name_index = defaultdict(list)     # normalized name -> [id, ...]

    for e, fname in entries:
        eid = e["id"]

        # --- 1/2 dangling + self references ---
        related = e.get("related") or {}
        for key in RELATED_KEYS:
            for target in related.get(key, []) or []:
                if target == eid:
                    findings["self-refs"].append({"id": eid, "file": fname, "key": key})
                elif target not in all_ids:
                    findings["dangling-refs"].append(
                        {"id": eid, "file": fname, "key": key, "target": target}
                    )

        # --- 3 taxonomy ---
        stage = e.get("stage")
        sub = e.get("subcategory", "")
        valid = VALID_SUBCATEGORIES.get(stage, set())
        if valid and sub not in valid:
            findings["taxonomy"].append(
                {"id": eid, "file": fname, "stage": stage, "subcategory": sub}
            )

        # --- 4 eval-method ---
        em = e.get("eval_method")
        if em is not None and em not in VALID_EVAL_METHODS:
            findings["eval-method"].append({"id": eid, "file": fname, "eval_method": em})

        # --- 5 what length ---
        what = e.get("what", "") or ""
        if len(what) > 200:
            findings["what-over-200"].append({"id": eid, "file": fname, "len": len(what)})
        elif len(what) > 80:
            findings["what-over-80"].append({"id": eid, "file": fname, "len": len(what)})

        # --- 6 what truncated ---
        w = what.rstrip()
        if w:
            last = re.split(r"[\s]", w)[-1].strip(".,").lower()
            if w.endswith(("-", ",")) or (last in DANGLING_TAIL):
                findings["what-truncated"].append({"id": eid, "file": fname, "what": what})

        # --- 7 name truncated (structural cut only — avoids flagging real
        # titles that happen to end in a function word) ---
        name = (e.get("name", "") or "").rstrip()
        if name.endswith(("-", "—", "...", ":")):
            findings["name-truncated"].append({"id": eid, "file": fname, "name": name})

        # --- 8/9 duplicate indexes ---
        for key in ("paper", "repo", "website"):
            u = e.get(key)
            if u:
                url_index[u.rstrip("/").lower()].append(eid)
        if name:
            name_index[re.sub(r"[^a-z0-9]+", "", name.lower())].append(eid)

        # --- 10 type vs links: declared type should have its matching link
        # (type="paper" may use `website` for non-arXiv venues, so it is not flagged) ---
        t = e.get("type", "")
        has_paper = bool(e.get("paper"))
        has_repo = bool(e.get("repo"))
        if (t == "paper+repo" and not (has_paper and has_repo)) or (t == "repo" and not has_repo):
            findings["type-link"].append(
                {"id": eid, "file": fname, "type": t, "paper": has_paper, "repo": has_repo}
            )

        # --- 11 bad url ---
        for key in ("paper", "repo", "website", "leaderboard_url"):
            u = e.get(key)
            if u and not URL_RE.match(u):
                findings["bad-url"].append({"id": eid, "file": fname, "field": key, "url": u})

    for u, ids in url_index.items():
        if len(set(ids)) > 1:
            findings["dup-url"].append({"url": u, "ids": sorted(set(ids))})
    for n, ids in name_index.items():
        if len(set(ids)) > 1:
            findings["dup-name"].append({"ids": sorted(set(ids))})

    # ---- report ----
    ERROR_LEVEL = {"dangling-refs", "self-refs", "dup-url", "bad-url"}
    order = [
        "dangling-refs", "self-refs", "dup-url", "dup-name", "bad-url",
        "type-link", "taxonomy", "eval-method",
        "what-over-200", "what-over-80", "what-truncated", "name-truncated",
    ]
    print(f"=== Data Audit ({len(entries)} entries, {len(all_ids)} ids) ===\n")
    total = 0
    n_err = 0
    for key in order:
        items = findings.get(key, [])
        if not items:
            continue
        total += len(items)
        if key in ERROR_LEVEL:
            n_err += len(items)
        mark = "✗" if key in ERROR_LEVEL else "⚠"
        print(f"{mark} {key}: {len(items)}")
        for it in items[:MAX_SHOWN]:
            print(f"      {json.dumps(it, ensure_ascii=False)}")
        if len(items) > MAX_SHOWN:
            print(f"      ... and {len(items) - MAX_SHOWN} more")
        print()

    if total == 0:
        print("✓ No issues found.")
    else:
        print(f"--- {total} findings ({n_err} error-level) ---")

    if args.json:
        Path(args.json).write_text(json.dumps(findings, ensure_ascii=False, indent=2))
        print(f"\nFull findings → {args.json}")

    if args.strict and n_err:
        sys.exit(1)


if __name__ == "__main__":
    main()
