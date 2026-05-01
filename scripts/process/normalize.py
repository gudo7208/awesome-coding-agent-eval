#!/usr/bin/env python3
"""LLM post-processing: normalize subcategory, polish what, unify tags.

Reads all data/*.json, sends items with non-standard subcategory or
low-quality what to LLM for normalization, writes back in-place.
"""
import json
import os
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8990/cc")
API_KEY = os.environ.get("LLM_API_KEY", "")
MODEL = "claude-sonnet-4-6"

VALID_SUBCATEGORIES = {
    "benchmark": [
        "bug-fix", "end-to-end", "long-horizon", "large-codebase",
        "code-review", "testing", "security", "production", "code-generation",
        "multi-agent", "feature-development",
    ],
    "methodology": [
        "llm-judge", "process-eval", "execution-based", "hybrid", "human-eval",
    ],
    "toolchain": [
        "harness", "sandbox", "observability", "judge-tool",
    ],
    "leaderboard": [
        "se-agent", "code-generation", "activity",
    ],
    "meta-analysis": [
        "limitation", "quality-study", "blog", "survey",
    ],
}

SYSTEM_PROMPT = """You are a data normalization expert. For each resource:
1. subcategory: pick exactly ONE from the valid list
2. what: MUST be ≤80 characters English. Be extremely concise. Format: "[Verb] [what] [for/on] [target]". Examples:
   - "Evaluates agent bug-fix ability on 500 verified GitHub issues"
   - "Sandbox for secure AI agent code execution with Firecracker microVMs"
   - "Analyzes code quality of 4892 agent-generated patches"
3. tags: 3-5 lowercase hyphenated English tags
Return ONLY JSON: {"subcategory": "...", "what": "...", "tags": ["..."]}"""


def call_llm(user_msg):
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": 300,
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


def needs_normalization(item):
    stage = item.get("stage", "")
    sub = item.get("subcategory", "")
    valid = VALID_SUBCATEGORIES.get(stage, [])
    if sub not in valid:
        return True
    what = item.get("what", "")
    if not what or len(what) > 80:
        return True
    # All items need English what — check if current what contains CJK
    if any('一' <= c <= '鿿' for c in what):
        return True
    return False


def main():
    import sys
    target_files = sys.argv[1:] if len(sys.argv) > 1 else None
    total_fixed = 0
    total_items = 0

    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        if target_files and f.name not in target_files:
            continue
        data = json.loads(f.read_text())
        stage = data[0]["stage"] if data else ""
        valid_subs = VALID_SUBCATEGORIES.get(stage, [])
        to_fix = [(i, item) for i, item in enumerate(data) if needs_normalization(item)]
        total_items += len(data)

        if not to_fix:
            print(f"  {f.name}: {len(data)} items, 0 need fixing")
            continue

        print(f"  {f.name}: {len(data)} items, {len(to_fix)} need fixing")
        fixed = 0
        for idx, item in to_fix:
            user_msg = (
                f"Resource: {item['name']}\n"
                f"Stage: {item['stage']}\n"
                f"Current subcategory: {item.get('subcategory', '')}\n"
                f"Current what: {item.get('what', '')}\n"
                f"Current tags: {item.get('tags', [])}\n\n"
                f"Valid subcategories: {valid_subs}\n"
                f"Normalize this entry."
            )
            try:
                result = call_llm(user_msg)
                if result.get("subcategory") in valid_subs:
                    data[idx]["subcategory"] = result["subcategory"]
                if result.get("what"):
                    data[idx]["what"] = result["what"][:80]
                if result.get("tags"):
                    data[idx]["tags"] = result["tags"][:5]
                fixed += 1
            except Exception as ex:
                # 无法调 LLM 时用规则兜底
                sub = item.get("subcategory", "")
                best = None
                for v in valid_subs:
                    if v in sub.lower():
                        best = v
                        break
                if best:
                    data[idx]["subcategory"] = best
                    fixed += 1
                else:
                    data[idx]["subcategory"] = valid_subs[0] if valid_subs else "other"
                    fixed += 1
            time.sleep(0.5)

        f.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        total_fixed += fixed
        print(f"    Fixed {fixed}/{len(to_fix)}")

    print(f"\nTotal: {total_items} items, {total_fixed} fixed")


if __name__ == "__main__":
    main()
