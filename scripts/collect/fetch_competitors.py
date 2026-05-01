#!/usr/bin/env python3
"""Diff our collection against competitor awesome lists.

Fetches README from competitor repos, extracts arXiv/GitHub links,
and outputs papers/repos we're missing.

Usage:
    python fetch_competitors.py
"""
import json
import re
import time
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

COMPETITORS = [
    {
        "name": "tongye98/Awesome-Code-Benchmark",
        "url": "https://raw.githubusercontent.com/tongye98/Awesome-Code-Benchmark/main/README.md",
    },
    {
        "name": "iSEngLab/AwesomeLLM4SE",
        "url": "https://raw.githubusercontent.com/iSEngLab/AwesomeLLM4SE/main/README.md",
    },
    {
        "name": "saltudelft/ml4se",
        "url": "https://raw.githubusercontent.com/saltudelft/ml4se/main/README.md",
    },
]

ARXIV_RE = re.compile(r"https?://arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})")
GITHUB_RE = re.compile(r"https?://github\.com/([\w.-]+/[\w.-]+)")


def load_our_ids():
    arxiv_ids = set()
    github_repos = set()
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        for item in json.loads(f.read_text()):
            for key in ("paper", "repo", "website"):
                url = item.get(key, "")
                m = ARXIV_RE.search(url)
                if m:
                    arxiv_ids.add(m.group(1))
                m = GITHUB_RE.search(url)
                if m:
                    github_repos.add(m.group(1).lower())
    return arxiv_ids, github_repos


def fetch_readme(url):
    req = urllib.request.Request(url, headers={"User-Agent": "AwesomeSEAgentEval/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode()


def main():
    our_arxiv, our_github = load_our_ids()
    print(f"Our collection: {len(our_arxiv)} arXiv, {len(our_github)} GitHub repos")

    all_missing = []

    for comp in COMPETITORS:
        print(f"\n--- {comp['name']} ---")
        try:
            readme = fetch_readme(comp["url"])
        except Exception as e:
            print(f"  Failed to fetch: {e}")
            continue

        their_arxiv = set(ARXIV_RE.findall(readme))
        their_github = set(m.lower() for m in GITHUB_RE.findall(readme))

        missing_arxiv = their_arxiv - our_arxiv
        missing_github = their_github - our_github

        print(f"  Their arXiv: {len(their_arxiv)}, missing: {len(missing_arxiv)}")
        print(f"  Their GitHub: {len(their_github)}, missing: {len(missing_github)}")

        for aid in missing_arxiv:
            all_missing.append({
                "arxiv_id": aid,
                "link": f"https://arxiv.org/abs/{aid}",
                "source": f"competitor:{comp['name']}",
                "title": "",
                "summary": "",
            })
        for repo in missing_github:
            all_missing.append({
                "full_name": repo,
                "link": f"https://github.com/{repo}",
                "source": f"competitor:{comp['name']}",
                "title": repo.split("/")[-1],
                "summary": "",
            })
        time.sleep(1)

    deduped = {}
    for item in all_missing:
        key = item.get("arxiv_id") or item.get("full_name", "")
        if key not in deduped:
            deduped[key] = item

    today = datetime.now().strftime("%Y%m%d")
    out_file = OUT_DIR / f"competitor_diff_{today}.jsonl"
    with open(out_file, "w") as f:
        for item in deduped.values():
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"\nTotal missing (deduped): {len(deduped)}")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
