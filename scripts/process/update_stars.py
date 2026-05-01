#!/usr/bin/env python3
"""Update GitHub star counts for all repos in data/*.json."""
import json
import os
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

GITHUB_REPO_RE = re.compile(r"https://github\.com/([^/]+/[^/]+)")


def get_stars(full_name, token=None):
    import urllib.request
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{full_name}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
        return data["stargazers_count"]


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Warning: GITHUB_TOKEN not set, rate limit will be low")

    updated = 0
    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        changed = False
        for item in data:
            repo_url = item.get("repo", "")
            m = GITHUB_REPO_RE.match(repo_url)
            if not m:
                continue
            full_name = m.group(1)
            try:
                stars = get_stars(full_name, token)
                if stars != item.get("stars"):
                    print(f"  {item['id']}: {item.get('stars', '?')} → {stars}")
                    item["stars"] = stars
                    changed = True
                    updated += 1
                time.sleep(0.5)
            except Exception as ex:
                print(f"  {item['id']}: error - {ex}")

        if changed:
            f.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print(f"  Updated {f.name}")

    print(f"\nTotal updated: {updated}")


if __name__ == "__main__":
    main()
