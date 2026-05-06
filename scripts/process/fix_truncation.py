#!/usr/bin/env python3
"""Fix truncated name, id, and what fields across all data files.

Three-phase approach:
1. Restore full names from arXiv/GitHub APIs
2. Rebuild ids from full names, update all related references
3. Regenerate truncated what fields via LLM

Usage:
    python fix_truncation.py [--phase 1|2|3|all] [--dry-run]
"""
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CHECKPOINT_FILE = ROOT / "scripts/process/.fix_truncation_checkpoint.json"

DATA_FILES = [
    "benchmarks.json", "methodology.json", "toolchain.json",
    "meta-analysis.json", "leaderboards.json",
]

LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8990/cc")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = "claude-sonnet-4-6"


def load_all_data():
    data = {}
    for fname in DATA_FILES:
        fpath = DATA / fname
        if fpath.exists():
            data[fname] = json.loads(fpath.read_text())
    return data


def save_all_data(data):
    for fname, items in data.items():
        fpath = DATA / fname
        tmp = fpath.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n")
        tmp.rename(fpath)


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        return json.loads(CHECKPOINT_FILE.read_text())
    return {"phase1_done": [], "phase2_done": False, "phase3_done": []}


def save_checkpoint(cp):
    CHECKPOINT_FILE.write_text(json.dumps(cp, indent=2))


# --- Phase 1: Restore full names from arXiv API ---

def extract_arxiv_id(url):
    """Extract arXiv ID from various URL formats."""
    if not url:
        return None
    patterns = [
        r"arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)",
        r"arxiv\.org/html/(\d{4}\.\d{4,5}(?:v\d+)?)",
        r"arxiv\.org/pdf/(\d{4}\.\d{4,5}(?:v\d+)?)",
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def fetch_arxiv_title(arxiv_id):
    """Fetch full title from arXiv API."""
    base_id = re.sub(r"v\d+$", "", arxiv_id)
    url = f"http://export.arxiv.org/api/query?id_list={base_id}"
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml = resp.read().decode()
        titles = re.findall(r"<title[^>]*>(.*?)</title>", xml, re.DOTALL)
        # First title is the query metadata, second is the paper title
        for title in titles:
            title = title.strip().replace("\n", " ")
            title = re.sub(r"\s+", " ", title)
            if title and "arXiv" not in title and "Error" not in title:
                return title
    except Exception as e:
        print(f"    arXiv API error for {arxiv_id}: {e}")
    return None


def fetch_github_name(repo_url):
    """Fetch repo full name/description from GitHub API."""
    m = re.match(r"https?://github\.com/([^/]+/[^/]+)", repo_url)
    if not m:
        return None
    repo_path = m.group(1).rstrip("/")
    api_url = f"https://api.github.com/repos/{repo_path}"
    token = os.environ.get("GITHUB_TOKEN", "")
    req = urllib.request.Request(api_url)
    if token:
        req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        return data.get("full_name") or data.get("name")
    except Exception as e:
        print(f"    GitHub API error for {repo_path}: {e}")
    return None


def is_name_truncated(name):
    return len(name) == 80


def phase1_restore_names(data, checkpoint, dry_run=False):
    """Restore truncated names from arXiv/GitHub APIs."""
    print("\n=== Phase 1: Restore full names ===")
    done_ids = set(checkpoint.get("phase1_done", []))
    restored = 0
    failed = []
    batch_count = 0

    for fname, items in data.items():
        for item in items:
            if not is_name_truncated(item["name"]):
                continue
            if item["id"] in done_ids:
                continue

            arxiv_id = extract_arxiv_id(item.get("paper", ""))
            if arxiv_id:
                time.sleep(3.5)
                title = fetch_arxiv_title(arxiv_id)
                if title:
                    if not dry_run:
                        item["name"] = title
                    print(f"  ✓ [{fname}] {item['id'][:40]}... → {title[:60]}...")
                    restored += 1
                else:
                    failed.append((fname, item["id"], "arXiv fetch failed"))
            elif item.get("repo") and "github.com" in item["repo"]:
                time.sleep(1)
                name = fetch_github_name(item["repo"])
                if name:
                    if not dry_run:
                        item["name"] = name
                    print(f"  ✓ [{fname}] {item['id'][:40]}... → {name}")
                    restored += 1
                else:
                    failed.append((fname, item["id"], "GitHub fetch failed"))
            else:
                failed.append((fname, item["id"], "no arXiv/GitHub URL"))

            done_ids.add(item["id"])
            batch_count += 1
            if batch_count % 20 == 0:
                checkpoint["phase1_done"] = list(done_ids)
                save_checkpoint(checkpoint)
                if not dry_run:
                    save_all_data(data)
                print(f"  [checkpoint] {restored} restored, {len(failed)} failed")

    checkpoint["phase1_done"] = list(done_ids)
    save_checkpoint(checkpoint)
    if not dry_run:
        save_all_data(data)

    print(f"\n  Phase 1 complete: {restored} restored, {len(failed)} failed")
    if failed:
        print(f"  Failed entries ({len(failed)}):")
        for fname, eid, reason in failed[:20]:
            print(f"    {fname}: {eid[:50]} — {reason}")
    return failed


# --- Phase 2: Rebuild ids and update related references ---

def make_id(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:120]


def phase2_rebuild_ids(data, dry_run=False):
    """Rebuild ids from full names and update all related references."""
    print("\n=== Phase 2: Rebuild ids and update related references ===")

    id_map = {}  # old_id → new_id
    all_ids = set()

    # First pass: compute new ids and build mapping
    for fname, items in data.items():
        for item in items:
            old_id = item["id"]
            new_id = make_id(item["name"])
            if new_id != old_id:
                # Handle collisions
                candidate = new_id
                suffix = 2
                while candidate in all_ids and candidate != old_id:
                    candidate = f"{new_id[:117]}-{suffix}"
                    suffix += 1
                new_id = candidate
                id_map[old_id] = new_id
            all_ids.add(new_id)

    print(f"  IDs to update: {len(id_map)}")

    if dry_run:
        for old, new in list(id_map.items())[:10]:
            print(f"    {old[:50]} → {new[:50]}")
        return id_map

    # Second pass: update ids
    for fname, items in data.items():
        for item in items:
            if item["id"] in id_map:
                item["id"] = id_map[item["id"]]

    # Third pass: update all related references
    refs_updated = 0
    for fname, items in data.items():
        for item in items:
            related = item.get("related")
            if not related:
                continue
            for key in list(related.keys()):
                new_list = []
                for ref_id in related[key]:
                    if ref_id in id_map:
                        new_list.append(id_map[ref_id])
                        refs_updated += 1
                    else:
                        new_list.append(ref_id)
                related[key] = new_list

    save_all_data(data)
    print(f"  IDs updated: {len(id_map)}, related refs updated: {refs_updated}")
    return id_map


# --- Phase 3: Regenerate truncated what fields via LLM ---

def is_what_truncated(what):
    return len(what) == 80


def call_llm(prompt):
    """Call LLM API to regenerate what field."""
    payload = {
        "model": LLM_MODEL,
        "max_tokens": 200,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{LLM_BASE_URL}/v1/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LLM_API_KEY}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode())
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"    LLM error: {e}")
        return None


def regenerate_what(name, old_what):
    """Use LLM to generate a complete what description."""
    prompt = f"""Given this paper/tool title and its truncated description, write a complete one-sentence description (≤150 chars, English).

Title: {name}
Truncated description: {old_what}

Rules:
- Must be a COMPLETE sentence (no trailing fragments)
- Start with a verb (Evaluate, Benchmark, Measure, etc.) or noun phrase
- ≤150 characters
- English only
- No quotes in output, just the description text"""

    result = call_llm(prompt)
    if result:
        result = result.strip('"').strip("'").strip()
        if len(result) <= 200 and len(result) > 20:
            return result
    return None


def fix_what_from_name(name, old_what):
    """Fix truncated what without LLM - use name as basis."""
    if len(name) <= 150:
        return name
    # Truncate to last complete word within 150 chars
    truncated = name[:150]
    last_space = truncated.rfind(" ")
    if last_space > 80:
        return truncated[:last_space]
    return truncated


def phase3_fix_what(data, checkpoint, dry_run=False):
    """Regenerate truncated what fields."""
    print("\n=== Phase 3: Fix truncated what fields ===")
    done_ids = set(checkpoint.get("phase3_done", []))
    fixed = 0
    failed = 0
    batch_count = 0
    use_llm = bool(LLM_API_KEY)
    if not use_llm:
        print("  (No LLM_API_KEY set, using name-based fallback)")

    for fname, items in data.items():
        for item in items:
            if not is_what_truncated(item.get("what", "")):
                continue
            if item["id"] in done_ids:
                continue

            new_what = None
            if use_llm:
                time.sleep(0.5)
                new_what = regenerate_what(item["name"], item["what"])

            if not new_what:
                new_what = fix_what_from_name(item["name"], item["what"])

            if new_what:
                if not dry_run:
                    item["what"] = new_what
                fixed += 1
            else:
                failed += 1

            done_ids.add(item["id"])
            batch_count += 1
            if batch_count % 50 == 0:
                checkpoint["phase3_done"] = list(done_ids)
                save_checkpoint(checkpoint)
                if not dry_run:
                    save_all_data(data)
                print(f"  [checkpoint] {fixed} fixed, {failed} failed")

    checkpoint["phase3_done"] = list(done_ids)
    save_checkpoint(checkpoint)
    if not dry_run:
        save_all_data(data)

    print(f"\n  Phase 3 complete: {fixed} fixed, {failed} failed")


# --- Main ---

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix truncated fields in data files")
    parser.add_argument("--phase", choices=["1", "2", "3", "all"], default="all")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = load_all_data()
    checkpoint = load_checkpoint()

    if args.phase in ("1", "all"):
        phase1_restore_names(data, checkpoint, dry_run=args.dry_run)

    if args.phase in ("2", "all"):
        phase2_rebuild_ids(data, dry_run=args.dry_run)

    if args.phase in ("3", "all"):
        phase3_fix_what(data, checkpoint, dry_run=args.dry_run)

    # Summary
    print("\n=== Final Summary ===")
    for fname in DATA_FILES:
        items = data.get(fname, [])
        name_trunc = sum(1 for i in items if len(i["name"]) == 80)
        what_trunc = sum(1 for i in items if len(i.get("what", "")) == 80)
        id_60 = sum(1 for i in items if len(i["id"]) == 60)
        print(f"  {fname}: name@80={name_trunc}, what@80={what_trunc}, id@60={id_60}")


if __name__ == "__main__":
    main()