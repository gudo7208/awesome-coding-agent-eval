#!/usr/bin/env python3
"""Classify candidates: keyword pre-filter → LLM classify → output relevant entries.

Usage:
    python classify_candidates.py [input.jsonl] [--resume]

Features:
- Keyword pre-filter to reduce LLM calls
- Checkpoint every 10 items (resume with --resume)
- English what ≤80 chars
- Batch-friendly: processes any JSONL input
"""
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CANDIDATES = ROOT / "candidates"

BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8990/cc")
API_KEY = os.environ.get("LLM_API_KEY", "")
MODEL = "claude-sonnet-4-6"

KEYWORDS = [
    "benchmark", "evaluation", "swe-bench", "agent", "code review",
    "testing", "sandbox", "harness", "leaderboard", "software engineering",
    "trajectory", "process", "context", "memory", "degradation",
    "compression", "observation", "tool use", "multi-step", "long-horizon",
    "vulnerability", "security", "code generation", "pull request",
]

SYSTEM_PROMPT = """You are an expert in AI Software Engineering Agent evaluation.

Our awesome list is organized by evaluation workflow:
② Benchmarks & Datasets (stage: benchmark)
③ Evaluation Methodology (stage: methodology)
④ Evaluation Toolchain (stage: toolchain)
⑤ Leaderboards (stage: leaderboard)
⑥ Meta-Analysis & Pitfalls (stage: meta-analysis)

Valid subcategories:
- benchmark: bug-fix, end-to-end, long-horizon, large-codebase, code-review, testing, security, production, code-generation, multi-agent, feature-development
- methodology: llm-judge, process-eval, execution-based, hybrid, human-eval
- toolchain: harness, sandbox, observability, judge-tool
- leaderboard: se-agent, code-generation, activity
- meta-analysis: limitation, quality-study, blog, survey

Inclusion: Must relate to evaluating AI SE agents (benchmarks, scoring methods, harnesses, sandboxes, leaderboards, pitfall analyses).
Exclusion: Pure model releases, general LLM benchmarks unrelated to SE, product marketing, pure agent frameworks without evaluation.

Return ONLY JSON:
{"decision":"relevant"|"not-relevant","stage":"...","subcategory":"...","what":"≤80 char English description","type":"paper"|"repo"|"tool"|"blog"|"paper+repo","tags":["tag1","tag2","tag3"]}"""

CHECKPOINT_INTERVAL = 10


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


def keyword_match(title, summary):
    text = (title + " " + summary).lower()
    return sum(1 for kw in KEYWORDS if kw in text) >= 1


def call_llm(title, summary, link, source):
    user_msg = (
        f"Title: {title}\nAbstract: {summary[:600]}\nLink: {link}\nSource: {source}\n\n"
        "Classify this resource."
    )
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
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        return json.loads(text)


def main():
    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else CANDIDATES / "merged_new_20260430.jsonl"
    resume = "--resume" in sys.argv

    checkpoint_file = input_file.with_suffix(".checkpoint.json")
    output_relevant = input_file.with_suffix(".relevant.json")
    output_stats = input_file.with_suffix(".classify_stats.json")

    existing_urls = load_existing_urls()
    print(f"Existing URLs in DB: {len(existing_urls)}")

    candidates = []
    with open(input_file) as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))
    print(f"Total candidates: {len(candidates)}")

    to_classify = []
    skipped_existing = 0
    skipped_keyword = 0
    for c in candidates:
        url = (c.get("link") or c.get("url") or "").rstrip("/").lower()
        if url in existing_urls:
            skipped_existing += 1
            continue
        title = c.get("title") or c.get("name") or c.get("full_name", "")
        summary = c.get("summary") or c.get("description", "")
        if not keyword_match(title, summary):
            skipped_keyword += 1
            continue
        to_classify.append(c)

    print(f"Skipped (already in DB): {skipped_existing}")
    print(f"Skipped (keyword miss): {skipped_keyword}")
    print(f"To classify: {len(to_classify)}")

    processed = {}
    if resume and checkpoint_file.exists():
        processed = json.loads(checkpoint_file.read_text())
        print(f"Resuming from checkpoint: {len(processed)} already done")

    relevant = []
    not_relevant = 0
    errors = 0

    for i, c in enumerate(to_classify):
        title = c.get("title") or c.get("name") or c.get("full_name", "")
        link = c.get("link") or c.get("url", "")

        if link in processed:
            r = processed[link]
            if r.get("decision") == "relevant":
                relevant.append(r)
            else:
                not_relevant += 1
            continue

        summary = c.get("summary") or c.get("description", "")
        source = c.get("source", "unknown")

        print(f"  [{i+1}/{len(to_classify)}] {title[:60]}...", end=" ", flush=True)
        try:
            result = call_llm(title, summary, link, source)
            result["_link"] = link
            result["_title"] = title
            result["_source_data"] = c
            processed[link] = result

            if result.get("decision") == "relevant":
                relevant.append(result)
                print(f"-> relevant ({result.get('stage')}/{result.get('subcategory')})")
            else:
                not_relevant += 1
                print(f"-> {result.get('decision', 'unknown')}")
            time.sleep(0.3)
        except Exception as ex:
            errors += 1
            processed[link] = {"decision": "error", "error": str(ex)}
            print(f"-> ERROR: {ex}")
            time.sleep(2)

        if (i + 1) % CHECKPOINT_INTERVAL == 0:
            checkpoint_file.write_text(json.dumps(processed, ensure_ascii=False))

    checkpoint_file.write_text(json.dumps(processed, ensure_ascii=False))
    output_relevant.write_text(json.dumps(relevant, indent=2, ensure_ascii=False) + "\n")

    stats = {
        "total_candidates": len(candidates),
        "skipped_existing": skipped_existing,
        "skipped_keyword": skipped_keyword,
        "classified": len(to_classify),
        "relevant": len(relevant),
        "not_relevant": not_relevant,
        "errors": errors,
    }
    output_stats.write_text(json.dumps(stats, indent=2) + "\n")

    print(f"\n--- Summary ---")
    print(f"Relevant: {len(relevant)}")
    print(f"Not relevant: {not_relevant}")
    print(f"Errors: {errors}")
    print(f"Output: {output_relevant}")


if __name__ == "__main__":
    main()
