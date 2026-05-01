#!/usr/bin/env python3
"""Enrich benchmarks.json with eval_method, scale, languages, venue via LLM."""

import argparse
import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent.parent / "data" / "benchmarks.json"
CHECKPOINT_FILE = Path(__file__).parent / ".enrich_checkpoint.json"

LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8990/cc")
LLM_URL = f"{LLM_BASE_URL}/v1/messages"
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_HEADERS = {
    "x-api-key": LLM_API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}
MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = """You extract structured metadata from academic paper information.
Given a paper title and abstract, extract:
- eval_method: exactly one of "execution-based", "llm-judge", "hybrid", "human-eval". If unclear, use "execution-based" for benchmarks with test suites, "llm-judge" for those using LLM scoring.
- scale: integer number of test cases/issues/problems. Extract the most prominent number. If unclear, return null.
- languages: array of programming languages mentioned. Use lowercase. If unclear, return [].
- venue: conference/journal if mentioned (e.g. "ICLR 2026", "NeurIPS 2025"). If unclear, return null.

Return ONLY JSON: {"eval_method":"...","scale":null|int,"languages":[],"venue":null|"..."}"""

EVAL_METHOD_WHITELIST = {"execution-based", "llm-judge", "hybrid", "human-eval"}


def call_llm(name: str, what: str, paper_url: str) -> dict | None:
    user_msg = f"Title: {name}\nAbstract: {what}\nPaper: {paper_url}"
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 256,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_msg}],
    }).encode()

    req = urllib.request.Request(LLM_URL, data=payload, headers=LLM_HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read())
        text = body["content"][0]["text"].strip()
        # Strip markdown code fences if present
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text)
    except (urllib.error.URLError, json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"  LLM error for {name}: {e}")
        return None


def validate_result(result: dict) -> dict:
    """Validate and sanitize LLM output."""
    out = {}
    em = result.get("eval_method")
    if em in EVAL_METHOD_WHITELIST:
        out["eval_method"] = em

    sc = result.get("scale")
    if isinstance(sc, int) and sc > 0:
        out["scale"] = sc
    elif isinstance(sc, float) and sc > 0:
        out["scale"] = int(sc)

    langs = result.get("languages")
    if isinstance(langs, list):
        cleaned = [str(l).lower().strip() for l in langs if l]
        if cleaned:
            out["languages"] = cleaned

    venue = result.get("venue")
    if isinstance(venue, str) and venue.strip():
        out["venue"] = venue.strip()

    return out


def load_checkpoint() -> dict:
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE) as f:
            return json.load(f)
    return {}


def save_checkpoint(checkpoint: dict):
    tmp = CHECKPOINT_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(checkpoint, f)
    tmp.rename(CHECKPOINT_FILE)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=200)
    args = parser.parse_args()

    with open(DATA_FILE) as f:
        data = json.load(f)

    # Sort by stars descending, build id->index map
    sorted_data = sorted(data, key=lambda x: x.get("stars", 0), reverse=True)
    top_n = sorted_data[: args.top]

    # Identify candidates: missing any of eval_method, scale, languages
    candidates = [
        b for b in top_n
        if not b.get("eval_method") or b.get("scale") is None or not b.get("languages")
    ]
    print(f"Top {args.top}: {len(candidates)} entries need enrichment")

    checkpoint = load_checkpoint()
    id_to_idx = {b["id"]: i for i, b in enumerate(data)}

    updated = 0
    for i, bench in enumerate(candidates):
        bid = bench["id"]
        if bid in checkpoint:
            print(f"[{i+1}/{len(candidates)}] {bench['name']} — skipped (checkpoint)")
            # Apply checkpoint result to data
            result = checkpoint[bid]
            idx = id_to_idx[bid]
            for field, val in result.items():
                if not data[idx].get(field):
                    data[idx][field] = val
            continue

        print(f"[{i+1}/{len(candidates)}] {bench['name']} ...", end=" ", flush=True)
        raw = call_llm(
            bench["name"],
            bench.get("what", ""),
            bench.get("paper", bench.get("repo", "")),
        )
        if raw is None:
            print("FAILED")
            time.sleep(1)
            continue

        validated = validate_result(raw)
        print(f"-> {validated}")

        idx = id_to_idx[bid]
        for field, val in validated.items():
            if not data[idx].get(field):
                data[idx][field] = val

        checkpoint[bid] = validated
        updated += 1

        if updated % 10 == 0:
            save_checkpoint(checkpoint)
            # Atomic write of main data file
            tmp = DATA_FILE.with_suffix(".tmp")
            with open(tmp, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            tmp.rename(DATA_FILE)
            print(f"  [checkpoint saved at {updated} updates]")

        time.sleep(0.3)

    # Final save
    save_checkpoint(checkpoint)
    tmp = DATA_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    tmp.rename(DATA_FILE)

    print(f"\nDone. {updated} entries enriched.")


if __name__ == "__main__":
    main()
