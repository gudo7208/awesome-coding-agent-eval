#!/usr/bin/env python3
"""Fetch new GitHub repos related to SE agent evaluation."""
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

QUERIES = [
    "SWE-bench",
    "code agent benchmark",
    "coding agent evaluation",
    "software engineering benchmark",
    "code evaluation harness",
    "LLM code review",
    "agent sandbox",
    "code execution sandbox",
    "AI coding benchmark",
    "agent evaluation framework",
    "code quality benchmark",
    "programming benchmark agent",
    "software testing agent",
    "automated code review",
    "code agent leaderboard",
    "AI developer benchmark",
    "software engineering agent benchmark",
    "code agent evaluation",
    "coding agent benchmark evaluation",
    "LLM code review benchmark",
    # --- 新增：上下文与记忆 ---
    "agent context benchmark",
    "agent memory benchmark",
    "context engineering LLM",
    # --- 新增：轨迹与过程 ---
    "trajectory evaluation",
    "process reward model code",
    # --- 新增：效率与退化 ---
    "agent token efficiency",
    "coding agent degradation",
    # --- 新增：审查与质量 ---
    "pull request review benchmark",
    "code review agent",
]

MIN_STARS = 10


def search_github(query, token=None):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.github.com/search/repositories?q={encoded_query}&sort=stars&order=desc&per_page=50"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Warning: GITHUB_TOKEN not set, rate limit will be low")

    all_repos = {}
    for query in QUERIES:
        print(f"Searching: {query}")
        retries = 0
        while retries < 3:
            try:
                result = search_github(query, token)
                for repo in result.get("items", []):
                    if repo["stargazers_count"] >= MIN_STARS:
                        all_repos[repo["full_name"]] = {
                            "name": repo["name"],
                            "full_name": repo["full_name"],
                            "description": (repo.get("description") or "")[:200],
                            "url": repo["html_url"],
                            "stars": repo["stargazers_count"],
                            "language": repo.get("language"),
                            "topics": repo.get("topics", []),
                            "created_at": repo["created_at"][:10],
                            "updated_at": repo["updated_at"][:10],
                            "source": "github",
                        }
                print(f"  Found {len(result.get('items', []))} repos ({len([r for r in result.get('items', []) if r['stargazers_count'] >= MIN_STARS])} with ≥{MIN_STARS} stars)")
                break
            except Exception as ex:
                err_str = str(ex)
                if "403" in err_str or "rate limit" in err_str.lower():
                    print(f"  Rate limit hit, sleeping 60s...")
                    time.sleep(60)
                    retries += 1
                else:
                    print(f"  Error: {ex}")
                    break
        time.sleep(7)  # ~8-9 req/min to stay under 10/min limit

    today = datetime.now().strftime("%Y%m%d")
    out_file = OUT_DIR / f"github_full_{today}.jsonl"
    with open(out_file, "w") as f:
        for repo in sorted(all_repos.values(), key=lambda x: x["stars"], reverse=True):
            f.write(json.dumps(repo, ensure_ascii=False) + "\n")

    print(f"\nTotal unique repos (≥{MIN_STARS} stars): {len(all_repos)}")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
