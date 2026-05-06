#!/usr/bin/env python3
"""Merge classified relevant candidates into data/*.json.

Reads the .relevant.json output from classify_candidates.py,
converts each entry to schema format, deduplicates, and appends.

Usage:
    python merge_classified.py [relevant.json]
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CANDIDATES = ROOT / "candidates"

STAGE_FILE_MAP = {
    "benchmark": "benchmarks.json",
    "methodology": "methodology.json",
    "toolchain": "toolchain.json",
    "leaderboard": "leaderboards.json",
    "meta-analysis": "meta-analysis.json",
}

VALID_SUBCATEGORIES = {
    "benchmark": {
        "bug-fix", "end-to-end", "long-horizon", "large-codebase",
        "code-review", "testing", "security", "production", "code-generation",
        "multi-agent", "feature-development",
    },
    "methodology": {"llm-judge", "process-eval", "execution-based", "hybrid", "human-eval"},
    "toolchain": {"harness", "sandbox", "observability", "judge-tool"},
    "leaderboard": {"se-agent", "code-generation", "activity"},
    "meta-analysis": {"limitation", "quality-study", "blog", "survey"},
}


def make_id(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:120]


def to_schema_entry(item):
    stage = item.get("stage")
    if not stage or stage not in STAGE_FILE_MAP:
        return None

    subcategory = item.get("subcategory", "")
    valid = VALID_SUBCATEGORIES.get(stage, set())
    if subcategory not in valid:
        subcategory = sorted(valid)[0] if valid else "other"

    title = item.get("_title", "")
    link = item.get("_link", "")
    source_data = item.get("_source_data", {})

    entry_type = item.get("type", "paper")
    if entry_type not in ("paper", "repo", "tool", "blog", "paper+repo", "leaderboard", "dataset"):
        entry_type = "paper"

    what = item.get("what", "")[:200]
    if not what:
        what = title[:200]

    tags = item.get("tags", [])
    if not tags:
        tags = [subcategory]

    entry = {
        "id": make_id(title),
        "name": title,
        "stage": stage,
        "subcategory": subcategory,
        "what": what,
        "type": entry_type,
        "tags": tags[:5],
        "added_date": date.today().isoformat(),
        "last_verified": date.today().isoformat(),
        "status": "active",
    }

    if "arxiv.org" in link:
        entry["paper"] = link
    elif "github.com" in link:
        entry["repo"] = link
        stars = source_data.get("stars")
        if stars:
            entry["stars"] = stars
        lang = source_data.get("language")
        if lang:
            entry["languages"] = [lang.lower()]
    else:
        entry["website"] = link

    return entry


def main():
    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else CANDIDATES / "merged_new_20260430.relevant.json"

    if not input_file.exists():
        print(f"File not found: {input_file}")
        sys.exit(1)

    relevant = json.loads(input_file.read_text())
    print(f"Relevant candidates: {len(relevant)}")

    existing_ids = set()
    existing_urls = set()
    data_cache = {}
    for fname in STAGE_FILE_MAP.values():
        fpath = DATA / fname
        if fpath.exists():
            items = json.loads(fpath.read_text())
            data_cache[fname] = items
            for item in items:
                existing_ids.add(item["id"])
                for key in ("paper", "repo", "website"):
                    if item.get(key):
                        existing_urls.add(item[key].rstrip("/").lower())

    added = 0
    skipped_dup = 0
    skipped_invalid = 0
    by_file = {}

    for item in relevant:
        entry = to_schema_entry(item)
        if not entry:
            skipped_invalid += 1
            continue

        link = entry.get("paper") or entry.get("repo") or entry.get("website", "")
        if link.rstrip("/").lower() in existing_urls:
            skipped_dup += 1
            continue

        if entry["id"] in existing_ids:
            entry["id"] = entry["id"] + "-2"
            if entry["id"] in existing_ids:
                skipped_dup += 1
                continue

        fname = STAGE_FILE_MAP[entry["stage"]]
        if fname not in data_cache:
            data_cache[fname] = []
        data_cache[fname].append(entry)
        existing_ids.add(entry["id"])
        existing_urls.add(link.rstrip("/").lower())
        added += 1
        by_file[fname] = by_file.get(fname, 0) + 1

    for fname, items in data_cache.items():
        fpath = DATA / fname
        fpath.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n")

    print(f"\nAdded: {added}")
    print(f"Skipped (duplicate): {skipped_dup}")
    print(f"Skipped (invalid stage): {skipped_invalid}")
    print(f"By file: {by_file}")


if __name__ == "__main__":
    main()
