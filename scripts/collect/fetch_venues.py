#!/usr/bin/env python3
"""Fetch accepted paper lists from top AI/SE venues.

Scrapes OpenReview (ICLR, NeurIPS, ICML) and DBLP (ASE, ICSE, FSE)
for accepted papers, filters by SE-agent-evaluation relevance.

Usage:
    python fetch_venues.py [--year 2026]
"""
import json
import re
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

RELEVANCE_KEYWORDS = [
    "benchmark", "evaluation", "agent", "code", "software engineering",
    "swe-bench", "bug fix", "code review", "testing", "vulnerability",
    "sandbox", "harness", "leaderboard", "trajectory", "process",
    "context", "memory", "tool use", "programming", "repository",
    "pull request", "issue", "patch", "debug", "security",
    "arena", "competitive", "long-context", "degradation", "compression",
    "coding", "devops", "software", "reward model",
]

DBLP_VENUES = [
    ("ASE", "conf/kbse/kbse"),
    ("ICSE", "conf/icse/icse"),
    ("FSE", "conf/sigsoft/fse"),
    ("ISSTA", "conf/issta/issta"),
]

OPENREVIEW_VENUES = [
    ("ICLR", "ICLR.cc"),
    ("NeurIPS", "NeurIPS.cc"),
    ("ICML", "ICML.cc"),
]


def load_our_arxiv_ids():
    arxiv_re = re.compile(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})")
    ids = set()
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        for item in json.loads(f.read_text()):
            for key in ("paper", "repo", "website"):
                m = arxiv_re.search(item.get(key, ""))
                if m:
                    ids.add(m.group(1))
    return ids


def is_relevant(title):
    t = title.lower()
    return sum(1 for kw in RELEVANCE_KEYWORDS if kw in t) >= 2


def fetch_dblp(venue_key, year):
    url = f"https://dblp.org/search/publ/api?q=toc:db/{venue_key}{year}.bht:&format=json&h=1000"
    req = urllib.request.Request(url, headers={"User-Agent": "AwesomeSEAgentEval/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        hits = data.get("result", {}).get("hits", {}).get("hit", [])
        entries = []
        for hit in hits:
            info = hit.get("info", {})
            title = info.get("title", "").rstrip(".")
            if is_relevant(title):
                doi = info.get("doi", "")
                ee = info.get("ee", "")
                entries.append({
                    "title": title,
                    "link": ee or (f"https://doi.org/{doi}" if doi else ""),
                    "year": int(info.get("year", year)),
                    "venue": info.get("venue", ""),
                    "source": f"dblp:{venue_key}/{year}",
                    "summary": "",
                })
        return entries
    except Exception as e:
        print(f"    DBLP error: {e}")
        return []


def fetch_openreview(venue_prefix, year):
    url = f"https://api2.openreview.net/notes/search?query=*&source=forum&group={venue_prefix}/{year}/Conference&limit=500"
    req = urllib.request.Request(url, headers={"User-Agent": "AwesomeSEAgentEval/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        entries = []
        for note in data.get("notes", []):
            content = note.get("content", {})
            title = content.get("title", {})
            if isinstance(title, dict):
                title = title.get("value", "")
            if is_relevant(title):
                forum_id = note.get("forum", note.get("id", ""))
                entries.append({
                    "title": title,
                    "link": f"https://openreview.net/forum?id={forum_id}",
                    "year": year,
                    "venue": f"{venue_prefix}/{year}",
                    "source": f"openreview:{venue_prefix}/{year}",
                    "summary": "",
                })
        return entries
    except Exception as e:
        print(f"    OpenReview error: {e}")
        return []


def main():
    year = int(sys.argv[sys.argv.index("--year") + 1]) if "--year" in sys.argv else 2026
    our_ids = load_our_arxiv_ids()
    print(f"Our arXiv IDs: {len(our_ids)}")
    print(f"Scanning year: {year}")

    all_entries = []

    for name, key in DBLP_VENUES:
        print(f"\n[DBLP] {name} {year}...")
        entries = fetch_dblp(key, year)
        print(f"  Relevant: {len(entries)}")
        all_entries.extend(entries)
        time.sleep(2)

    for name, prefix in OPENREVIEW_VENUES:
        print(f"\n[OpenReview] {name} {year}...")
        entries = fetch_openreview(prefix, year)
        print(f"  Relevant: {len(entries)}")
        all_entries.extend(entries)
        time.sleep(2)

    deduped = {}
    for e in all_entries:
        key = e["title"].lower().strip()
        if key not in deduped:
            deduped[key] = e

    today = datetime.now().strftime("%Y%m%d")
    out_file = OUT_DIR / f"venues_{year}_{today}.jsonl"
    with open(out_file, "w") as f:
        for e in deduped.values():
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    print(f"\nTotal relevant (deduped): {len(deduped)}")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
