#!/usr/bin/env python3
"""Fetch new papers from arXiv related to SE agent evaluation."""
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "candidates"
OUT_DIR.mkdir(exist_ok=True)

QUERIES = [
    # SE Agent
    "software engineering agent benchmark",
    "coding agent evaluation",
    "code agent benchmark",
    "AI developer agent",
    # Benchmark
    "code benchmark evaluation",
    "SWE-bench software engineering",
    "programming benchmark LLM",
    # 评估方法
    "LLM judge code evaluation",
    "code quality evaluation automated",
    "agent evaluation framework",
    # 工具与执行
    "code sandbox execution evaluation",
    "agent harness software testing",
    # 过程评估
    "trajectory evaluation agent",
    "process evaluation coding agent",
    "agent debugging evaluation",
    # 安全
    "code security benchmark vulnerability",
    "vulnerability detection benchmark LLM",
    # 多步骤
    "multi-step coding agent",
    "long-horizon software engineering",
    "software evolution agent",
    # --- 新增：上下文与记忆 ---
    "agent context retrieval benchmark",
    "context engineering LLM agent",
    "context utilization coding agent",
    "agent memory evaluation benchmark",
    "long-term memory agent benchmark",
    "multi-session agent memory",
    # --- 新增：轨迹与过程监督 ---
    "trajectory analysis coding agent",
    "process supervision code generation",
    "process reward model code",
    "step-level evaluation agent",
    # --- 新增：退化与效率 ---
    "agent degradation long context",
    "context window compression agent",
    "observation masking agent efficiency",
    "token efficiency coding agent",
    # --- 新增：代码审查与质量 ---
    "automated code review LLM benchmark",
    "pull request quality evaluation",
]

ARXIV_API = "http://export.arxiv.org/api/query"
MAX_RESULTS = 50


def search_arxiv(query, max_results=MAX_RESULTS):
    params = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode()


def parse_entries(xml_text):
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")[:300]
        published = entry.find("atom:published", ns).text[:10]
        arxiv_id = entry.find("atom:id", ns).text.split("/abs/")[-1]
        link = f"https://arxiv.org/abs/{arxiv_id}"
        categories = [c.get("term") for c in entry.findall("atom:category", ns)]
        entries.append({
            "title": title,
            "summary": summary,
            "published": published,
            "arxiv_id": arxiv_id,
            "link": link,
            "categories": categories,
            "source": "arxiv",
        })
    return entries


def main():
    all_entries = {}
    for query in QUERIES:
        print(f"Searching: {query}")
        try:
            xml = search_arxiv(query)
            entries = parse_entries(xml)
            for e in entries:
                all_entries[e["arxiv_id"]] = e
            print(f"  Found {len(entries)} results")
        except Exception as ex:
            print(f"  Error: {ex}")
        time.sleep(3)

    today = datetime.now().strftime("%Y%m%d")
    out_file = OUT_DIR / f"arxiv_full_{today}.jsonl"
    with open(out_file, "w") as f:
        for entry in sorted(all_entries.values(), key=lambda x: x["published"], reverse=True):
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"\nTotal unique: {len(all_entries)}")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
