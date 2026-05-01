#!/usr/bin/env python3
"""Deduplicate candidates against existing data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CANDIDATES = ROOT / "candidates"


def load_existing_urls():
    urls = set()
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        for item in json.loads(f.read_text()):
            for key in ("paper", "repo", "website"):
                if item.get(key):
                    urls.add(item[key].rstrip("/").lower())
    return urls


def main():
    existing = load_existing_urls()
    print(f"Existing URLs: {len(existing)}")

    for f in sorted(CANDIDATES.glob("*.jsonl")):
        total = 0
        new = 0
        dupes = 0
        with open(f) as fh:
            for line in fh:
                total += 1
                entry = json.loads(line)
                url = (entry.get("link") or entry.get("url") or "").rstrip("/").lower()
                if url in existing:
                    dupes += 1
                else:
                    new += 1
        print(f"  {f.name}: {total} total, {new} new, {dupes} duplicates")


if __name__ == "__main__":
    main()
