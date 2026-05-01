#!/usr/bin/env python3
"""Sweep recent arXiv papers (last N months) in SE-agent-relevant categories.

Complements fetch_arxiv.py (keyword-based) and fetch_citations.py (graph-based)
by catching new papers that haven't been cited yet and may use novel terminology.

Strategy: query by category + date range, then filter by relevance keywords.
"""
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

ARXIV_API = "http://export.arxiv.org/api/query"

TOPIC_QUERIES = [
    "cat:cs.SE AND (agent OR benchmark OR evaluation)",
    "cat:cs.AI AND (coding agent benchmark OR software engineering agent)",
    "cat:cs.CL AND (code generation benchmark OR code agent evaluation)",
    "cat:cs.LG AND (software engineering agent OR coding benchmark)",
    "(agent context retrieval OR context engineering) AND (code OR software)",
    "(agent memory benchmark OR long-term memory agent)",
    "(trajectory evaluation OR process supervision) AND (code OR agent)",
    "(agent degradation OR context compression) AND (coding OR software)",
    "(code review benchmark OR pull request evaluation) AND LLM",
    "(observation masking OR token efficiency) AND agent",
]

RELEVANCE_KEYWORDS = [
    "benchmark", "evaluation", "agent", "coding", "software engineering",
    "code generation", "code review", "bug fix", "vulnerability",
    "swe-bench", "leaderboard", "harness", "sandbox",
    "trajectory", "process evaluation", "llm judge",
    "context", "memory", "degradation", "compression",
    "tool use", "multi-step", "long-horizon",
    "code quality", "test generation", "pull request",
]

MONTHS_BACK = 6
MAX_PER_QUERY = 100
MAX_RETRIES = 3


def search_arxiv_query(query, max_results=MAX_PER_QUERY):
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "AwesomeSEAgentEval/1.0"})
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            wait = 10 * (attempt + 1)
            print(f"    Retry {attempt+1}/{MAX_RETRIES} after {wait}s: {e}")
            time.sleep(wait)
    return None


def parse_entries(xml_text):
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        summary_el = entry.find("atom:summary", ns)
        if title_el is None or summary_el is None:
            continue
        title = title_el.text.strip().replace("\n", " ")
        summary = summary_el.text.strip().replace("\n", " ")
        published = entry.find("atom:published", ns).text[:10]
        raw_id = entry.find("atom:id", ns).text.split("/abs/")[-1]
        arxiv_id = raw_id.split("v")[0]
        categories = [c.get("term") for c in entry.findall("atom:category", ns)]
        entries.append({
            "title": title,
            "summary": summary[:500],
            "published": published,
            "arxiv_id": arxiv_id,
            "link": f"https://arxiv.org/abs/{arxiv_id}",
            "categories": categories,
            "source": "arxiv-recent",
        })
    return entries


def is_relevant(entry):
    text = (entry["title"] + " " + entry["summary"]).lower()
    hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw in text)
    return hits >= 2


def main():
    print(f"Running {len(TOPIC_QUERIES)} topic queries")

    all_entries = {}
    for i, query in enumerate(TOPIC_QUERIES, 1):
        print(f"\n[{i}/{len(TOPIC_QUERIES)}] {query[:60]}...")
        xml = search_arxiv_query(query)
        if xml is None:
            print("  Skipped (all retries failed)")
            continue
        entries = parse_entries(xml)
        relevant = [e for e in entries if is_relevant(e)]
        for e in relevant:
            all_entries[e["arxiv_id"]] = e
        print(f"  Fetched {len(entries)}, relevant: {len(relevant)}")
        time.sleep(5)

    existing_ids = set()
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        for item in json.loads(f.read_text()):
            for key in ("paper", "repo", "website"):
                url = item.get(key, "")
                if "arxiv.org" in url:
                    aid = url.split("/")[-1].split("v")[0]
                    existing_ids.add(aid)

    new_entries = {k: v for k, v in all_entries.items() if k not in existing_ids}
    print(f"\nTotal relevant: {len(all_entries)}")
    print(f"Already in DB: {len(all_entries) - len(new_entries)}")
    print(f"New candidates: {len(new_entries)}")

    today = datetime.now().strftime("%Y%m%d")
    out_file = OUT_DIR / f"arxiv_recent_{today}.jsonl"
    with open(out_file, "w") as f:
        for entry in sorted(new_entries.values(), key=lambda x: x["published"], reverse=True):
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
