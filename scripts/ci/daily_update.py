#!/usr/bin/env python3
"""Daily auto-collection for GitHub Actions.

Collects recent arXiv papers, classifies via LLM, merges into data/*.json,
validates, and regenerates outputs. Designed to run unattended in CI.

Environment variables:
    LLM_API_KEY     - API key (required unless --dry-run)
    LLM_BASE_URL    - API endpoint (default: https://api.anthropic.com)
    LLM_PROVIDER    - "anthropic" (default) or "openai"
    LLM_MODEL       - Model name (default: claude-haiku-4-5-20251001)
    DAYS_BACK       - How many days to look back (default: 3)

Usage:
    python scripts/ci/daily_update.py            # full run
    python scripts/ci/daily_update.py --dry-run  # collect only, no LLM
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

# --- Configuration ---
API_KEY = os.environ.get("LLM_API_KEY", "")
BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.anthropic.com")
PROVIDER = os.environ.get("LLM_PROVIDER", "anthropic")
MODEL = os.environ.get("LLM_MODEL", "claude-haiku-4-5-20251001")
DAYS_BACK = int(os.environ.get("DAYS_BACK", "3"))
DRY_RUN = "--dry-run" in sys.argv

ARXIV_API = "http://export.arxiv.org/api/query"

# --- PLACEHOLDER_QUERIES ---

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

SYSTEM_PROMPT = """You are an expert in AI Software Engineering Agent evaluation.

Our awesome list covers SE agent evaluation resources organized by workflow:
- benchmark: bug-fix, end-to-end, long-horizon, large-codebase, code-review, testing, security, production, code-generation, multi-agent, feature-development
- methodology: llm-judge, process-eval, execution-based, hybrid, human-eval
- toolchain: harness, sandbox, observability, judge-tool
- leaderboard: se-agent, code-generation, activity
- meta-analysis: limitation, quality-study, blog, survey

Inclusion: Must relate to evaluating AI SE agents (benchmarks, scoring methods, harnesses, sandboxes, leaderboards, pitfall analyses).
Exclusion: Pure model releases, general LLM benchmarks unrelated to SE, product marketing, pure agent frameworks without evaluation.

Return ONLY valid JSON:
{"decision":"relevant"|"not-relevant","stage":"benchmark"|"methodology"|"toolchain"|"leaderboard"|"meta-analysis","subcategory":"...","what":"≤80 char English description starting with verb","type":"paper"|"repo"|"tool"|"blog"|"paper+repo","tags":["tag1","tag2","tag3"]}"""

STAGE_FILE_MAP = {
    "benchmark": "benchmarks.json",
    "methodology": "methodology.json",
    "toolchain": "toolchain.json",
    "leaderboard": "leaderboards.json",
    "meta-analysis": "meta-analysis.json",
}


# --- Step 1: Collect from arXiv ---

def collect_arxiv(days_back):
    """Query arXiv for recent papers matching topic queries."""
    print(f"\n=== Step 1: Collect (last {days_back} days) ===")
    candidates = []
    seen_ids = set()

    for i, query in enumerate(TOPIC_QUERIES):
        print(f"  [{i+1}/{len(TOPIC_QUERIES)}] {query[:60]}...")
        xml_text = _arxiv_query(query, max_results=50)
        if not xml_text:
            continue
        entries = _parse_arxiv(xml_text, days_back)
        for e in entries:
            if e["arxiv_id"] not in seen_ids:
                seen_ids.add(e["arxiv_id"])
                candidates.append(e)
        time.sleep(3)

    print(f"  Raw candidates: {len(candidates)}")
    return candidates


def _arxiv_query(query, max_results=50):
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "AwesomeCodingAgentEval/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            time.sleep(10 * (attempt + 1))
    return None


def _parse_arxiv(xml_text, days_back):
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    cutoff = datetime.now() - timedelta(days=days_back)
    entries = []

    for entry in root.findall("atom:entry", ns):
        published = entry.find("atom:published", ns)
        if published is None:
            continue
        pub_date = datetime.fromisoformat(published.text.replace("Z", "+00:00")).replace(tzinfo=None)
        if pub_date < cutoff:
            continue

        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")[:500]
        link = ""
        for lnk in entry.findall("atom:link", ns):
            if lnk.get("type") == "text/html":
                link = lnk.get("href", "")
                break
        if not link:
            id_el = entry.find("atom:id", ns)
            link = id_el.text if id_el is not None else ""

        arxiv_id = link.split("/abs/")[-1] if "/abs/" in link else link.split("/")[-1]

        entries.append({
            "title": title,
            "summary": summary,
            "link": link,
            "arxiv_id": arxiv_id,
            "published": published.text[:10],
        })
    return entries


# --- Step 2: Deduplicate against existing data ---

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


def deduplicate(candidates, existing_urls):
    print(f"\n=== Step 2: Deduplicate ===")
    new = []
    for c in candidates:
        url = c["link"].rstrip("/").lower()
        if url not in existing_urls:
            new.append(c)
    print(f"  After dedup: {len(new)} (removed {len(candidates) - len(new)} existing)")
    return new


# --- Step 3: Keyword pre-filter ---

def keyword_filter(candidates):
    print(f"\n=== Step 3: Keyword filter ===")
    passed = []
    for c in candidates:
        text = (c["title"] + " " + c["summary"]).lower()
        hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw in text)
        if hits >= 2:
            passed.append(c)
    print(f"  After keyword filter: {len(passed)} (removed {len(candidates) - len(passed)})")
    return passed


# --- Step 4: LLM Classification ---

def classify_batch(candidates):
    print(f"\n=== Step 4: LLM Classification ({len(candidates)} candidates) ===")
    if not API_KEY:
        print("  ERROR: LLM_API_KEY not set, cannot classify")
        sys.exit(1)

    relevant = []
    errors = 0
    for i, c in enumerate(candidates):
        try:
            result = _call_llm(c["title"], c["summary"], c["link"])
            if result and result.get("decision") == "relevant":
                result["_link"] = c["link"]
                result["_title"] = c["title"]
                relevant.append(result)
                print(f"  [{i+1}/{len(candidates)}] ✓ {c['title'][:50]}...")
            else:
                print(f"  [{i+1}/{len(candidates)}] ✗ skip")
        except Exception as e:
            errors += 1
            print(f"  [{i+1}/{len(candidates)}] ERROR: {e}")
        time.sleep(0.5)

    print(f"  Relevant: {len(relevant)}, Errors: {errors}")
    return relevant


def _call_llm(title, summary, link):
    user_msg = f"Title: {title}\nAbstract: {summary[:600]}\nLink: {link}\n\nClassify this resource."

    if PROVIDER == "openai":
        return _call_openai(user_msg)
    return _call_anthropic(user_msg)


def _call_anthropic(user_msg):
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 400,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_msg}],
    }).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode())
        text = result["content"][0]["text"].strip()
        return _parse_json_response(text)


def _call_openai(user_msg):
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 400,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
    }).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    req = urllib.request.Request(f"{BASE_URL}/v1/chat/completions", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode())
        text = result["choices"][0]["message"]["content"].strip()
        return _parse_json_response(text)


def _parse_json_response(text):
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


# --- Step 5: Merge into data files ---

def merge_entries(classified):
    print(f"\n=== Step 5: Merge ({len(classified)} entries) ===")
    today = datetime.now().strftime("%Y-%m-%d")
    added = []

    data_cache = {}
    for stage, fname in STAGE_FILE_MAP.items():
        fpath = DATA / fname
        data_cache[stage] = json.loads(fpath.read_text())

    existing_ids = set()
    for items in data_cache.values():
        for item in items:
            existing_ids.add(item["id"])

    for c in classified:
        stage = c.get("stage", "")
        if stage not in STAGE_FILE_MAP:
            continue

        entry_id = _slugify(c.get("_title", ""))
        if entry_id in existing_ids:
            entry_id = entry_id + "-2"
        if entry_id in existing_ids:
            continue

        entry = {
            "id": entry_id,
            "name": c.get("_title", "")[:100],
            "stage": stage,
            "subcategory": c.get("subcategory", ""),
            "what": c.get("what", "")[:80],
            "type": c.get("type", "paper"),
            "tags": c.get("tags", []),
            "paper": c.get("_link", ""),
            "added_date": today,
        }

        data_cache[stage].append(entry)
        existing_ids.add(entry_id)
        added.append(entry)

    for stage, fname in STAGE_FILE_MAP.items():
        fpath = DATA / fname
        fpath.write_text(json.dumps(data_cache[stage], indent=2, ensure_ascii=False) + "\n")

    print(f"  Added: {len(added)} entries")
    return added


def _slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80]


# --- Step 6: Validate ---

def validate():
    print(f"\n=== Step 6: Validate ===")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/process/validate.py")],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  VALIDATION FAILED:\n{result.stdout}\n{result.stderr}")
        return False
    print("  ✓ All checks passed")
    return True


# --- Step 7: Regenerate outputs ---

def regenerate():
    print(f"\n=== Step 7: Regenerate ===")
    scripts = [
        "scripts/generate/generate_stats.py",
        "scripts/generate/generate_readme.py",
        "scripts/generate/generate_llms_txt.py",
        "scripts/generate/generate_docs.py",
    ]
    for script in scripts:
        result = subprocess.run(
            [sys.executable, str(ROOT / script)],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ERROR in {script}: {result.stderr}")
            return False
        for line in result.stdout.strip().split("\n"):
            if line:
                print(f"  {line}")
    return True


# --- Step 8: Summary ---

def write_summary(added):
    print(f"\n=== Summary ===")
    print(f"New entries: {len(added)}")

    if not added:
        print("No new entries found today.")
        return

    lines = [f"## Daily Collection {datetime.now().strftime('%Y-%m-%d')}\n"]
    lines.append(f"**{len(added)} new entries added**\n")
    lines.append("| Name | Stage | Subcategory |")
    lines.append("|---|---|---|")
    for e in added:
        lines.append(f"| [{e['name'][:50]}]({e.get('paper','')}) | {e['stage']} | {e['subcategory']} |")

    summary_path = ROOT / "ci_summary.md"
    summary_path.write_text("\n".join(lines) + "\n")
    print(f"  Summary written to {summary_path}")

    for line in lines:
        print(line)


# --- Main ---

def main():
    print(f"=== Daily Update {'(DRY RUN)' if DRY_RUN else ''} ===")
    print(f"  Provider: {PROVIDER}, Model: {MODEL}")
    print(f"  Base URL: {BASE_URL}")
    print(f"  Days back: {DAYS_BACK}")
    print(f"  API key: {'set' if API_KEY else 'NOT SET'}")

    # Step 1: Collect
    candidates = collect_arxiv(DAYS_BACK)
    if not candidates:
        print("\nNo candidates found. Done.")
        return

    # Step 2: Deduplicate
    existing_urls = load_existing_urls()
    candidates = deduplicate(candidates, existing_urls)
    if not candidates:
        print("\nAll candidates already in DB. Done.")
        return

    # Step 3: Keyword filter
    candidates = keyword_filter(candidates)
    if not candidates:
        print("\nNo candidates passed keyword filter. Done.")
        return

    # Dry run stops here
    if DRY_RUN:
        print(f"\n=== DRY RUN: {len(candidates)} candidates would be sent to LLM ===")
        for c in candidates[:20]:
            print(f"  - {c['title'][:70]}")
        return

    # Step 4: Classify
    classified = classify_batch(candidates)
    if not classified:
        print("\nNo relevant entries found. Done.")
        return

    # Step 5: Merge
    added = merge_entries(classified)
    if not added:
        print("\nNo new entries to add. Done.")
        return

    # Step 6: Validate
    if not validate():
        print("\nValidation failed! Reverting changes.")
        subprocess.run(["git", "checkout", "--", "data/"], cwd=ROOT)
        sys.exit(1)

    # Step 7: Regenerate
    if not regenerate():
        print("\nRegeneration failed!")
        sys.exit(1)

    # Step 8: Summary
    write_summary(added)


if __name__ == "__main__":
    main()
