#!/usr/bin/env python3
"""Expand seed papers via citation graph using Semantic Scholar API.

Strategy: from seed papers in data/*.json, fetch references (who they cite)
and citations (who cites them), then deduplicate against existing data.
"""
import json
import re
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

S2_API = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,abstract,year,externalIds,url,citationCount,referenceCount,publicationVenue"
RATE_LIMIT_SLEEP = 3.5  # S2 free tier: ~100 req/5min


def extract_arxiv_ids():
    """Extract arXiv IDs from all paper URLs in data/*.json."""
    arxiv_re = re.compile(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})")
    ids = {}
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        for item in json.loads(f.read_text()):
            for key in ("paper", "repo", "website"):
                url = item.get(key, "")
                m = arxiv_re.search(url)
                if m:
                    ids[m.group(1)] = item["id"]
                    break
    return ids


def s2_get(endpoint, params=None):
    url = f"{S2_API}/{endpoint}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("    Rate limited, sleeping 30s...")
            time.sleep(30)
            return s2_get(endpoint, params)
        raise


def get_paper_by_arxiv(arxiv_id):
    return s2_get(f"paper/ARXIV:{arxiv_id}", {"fields": S2_FIELDS})


def get_references(s2_paper_id, limit=100):
    data = s2_get(f"paper/{s2_paper_id}/references", {
        "fields": S2_FIELDS, "limit": str(limit)
    })
    return [r["citedPaper"] for r in data.get("data", []) if r.get("citedPaper", {}).get("title")]


def get_citations(s2_paper_id, limit=100):
    data = s2_get(f"paper/{s2_paper_id}/citations", {
        "fields": S2_FIELDS, "limit": str(limit)
    })
    papers = [c["citingPaper"] for c in data.get("data", []) if c.get("citingPaper", {}).get("title")]
    # Sort by citation count desc and cap at top 100 to handle high-citation seeds
    papers.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
    return papers[:100]


def paper_to_candidate(paper, source_id, direction):
    arxiv_id = (paper.get("externalIds") or {}).get("ArXiv", "")
    link = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else paper.get("url", "")
    return {
        "title": paper.get("title", ""),
        "summary": (paper.get("abstract") or "")[:500],
        "published": str(paper.get("year", "")),
        "arxiv_id": arxiv_id,
        "link": link,
        "s2_id": paper.get("paperId", ""),
        "citation_count": paper.get("citationCount", 0),
        "venue": (paper.get("publicationVenue") or {}).get("name", ""),
        "source": "citation-graph",
        "seed_paper": source_id,
        "direction": direction,
    }


def main():
    seed_arxiv_ids = extract_arxiv_ids()
    print(f"Found {len(seed_arxiv_ids)} seed papers with arXiv IDs")

    all_candidates = {}
    seed_s2_ids = {}

    # Phase 1: resolve seed papers to S2 IDs
    print("\n=== Phase 1: Resolving seed papers ===")
    for arxiv_id, local_id in seed_arxiv_ids.items():
        print(f"  {local_id} (arxiv:{arxiv_id})...", end=" ", flush=True)
        try:
            paper = get_paper_by_arxiv(arxiv_id)
            if paper and paper.get("paperId"):
                seed_s2_ids[local_id] = paper["paperId"]
                print(f"OK (citations: {paper.get('citationCount', '?')}, refs: {paper.get('referenceCount', '?')})")
            else:
                print("not found on S2")
        except Exception as ex:
            print(f"error: {ex}")
        time.sleep(RATE_LIMIT_SLEEP)

    print(f"\nResolved {len(seed_s2_ids)}/{len(seed_arxiv_ids)} seed papers")

    # Phase 2: fetch references
    print("\n=== Phase 2: Fetching references (who seeds cite) ===")
    for local_id, s2_id in seed_s2_ids.items():
        print(f"  {local_id} references...", end=" ", flush=True)
        try:
            refs = get_references(s2_id, limit=50)
            count = 0
            for paper in refs:
                pid = paper.get("paperId", "")
                if pid and pid not in all_candidates:
                    all_candidates[pid] = paper_to_candidate(paper, local_id, "reference")
                    count += 1
            print(f"{count} new")
        except Exception as ex:
            print(f"error: {ex}")
        time.sleep(RATE_LIMIT_SLEEP)

    # Phase 3: fetch citations
    print("\n=== Phase 3: Fetching citations (who cites seeds) ===")
    for local_id, s2_id in seed_s2_ids.items():
        print(f"  {local_id} citations...", end=" ", flush=True)
        try:
            cites = get_citations(s2_id, limit=100)
            count = 0
            for paper in cites:
                pid = paper.get("paperId", "")
                if pid and pid not in all_candidates:
                    all_candidates[pid] = paper_to_candidate(paper, local_id, "citation")
                    count += 1
            print(f"{count} new")
        except Exception as ex:
            print(f"error: {ex}")
        time.sleep(RATE_LIMIT_SLEEP)

    # Output
    out_file = OUT_DIR / f"citations_{datetime.now().strftime('%Y%m%d')}.jsonl"
    sorted_candidates = sorted(
        all_candidates.values(),
        key=lambda x: x.get("citation_count", 0),
        reverse=True,
    )
    with open(out_file, "w") as f:
        for c in sorted_candidates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"\n=== Summary ===")
    print(f"Seed papers resolved: {len(seed_s2_ids)}")
    print(f"Total unique candidates: {len(all_candidates)}")
    refs = sum(1 for c in all_candidates.values() if c["direction"] == "reference")
    cites = sum(1 for c in all_candidates.values() if c["direction"] == "citation")
    print(f"  From references: {refs}")
    print(f"  From citations: {cites}")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
