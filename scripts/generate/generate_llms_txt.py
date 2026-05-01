#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt for LLM consumption.

llms.txt: Structured index with links to per-category markdown files.
llms-full.txt: All 900 entries inlined as one markdown document.

Following the llmstxt.org specification.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

STAGE_ORDER = [
    ("benchmarks", "Benchmarks & Datasets"),
    ("methodology", "Evaluation Methodology"),
    ("toolchain", "Evaluation Toolchain"),
    ("leaderboards", "Leaderboards"),
    ("meta-analysis", "Meta-Analysis & Pitfalls"),
]

SUBCATEGORY_LABELS = {
    "bug-fix": "Bug Fix & Issue Resolution",
    "end-to-end": "End-to-End / Multi-Task",
    "long-horizon": "Long-Horizon / Evolution",
    "large-codebase": "Large Codebase / Multi-Repo",
    "code-review": "Code Review",
    "testing": "Testing & QA",
    "security": "Security & Vulnerability",
    "production": "Production-Derived",
    "code-generation": "Code Generation",
    "feature-development": "Feature Development",
    "multi-agent": "Multi-Agent",
    "harness": "Evaluation Harness",
    "sandbox": "Sandbox & Execution",
    "observability": "Observability",
    "judge-tool": "LLM Judge Tools",
    "llm-judge": "LLM-as-Judge",
    "process-eval": "Process Evaluation",
    "execution-based": "Execution-based",
    "hybrid": "Hybrid",
    "human-eval": "Human Evaluation",
    "se-agent": "SE Agent",
    "activity": "Activity",
    "limitation": "Benchmark Limitations",
    "quality-study": "Agent Output Quality Studies",
    "blog": "Blogs & Practice Reports",
    "survey": "Surveys",
}


def load_data():
    all_data = {}
    for fname, label in STAGE_ORDER:
        fpath = DATA / f"{fname}.json"
        if fpath.exists():
            all_data[fname] = json.loads(fpath.read_text())
    return all_data


def entry_line(item):
    name = item["name"]
    link = item.get("repo") or item.get("paper") or item.get("website") or ""
    what = item.get("what", "")
    langs = ", ".join(item.get("languages", []))
    method = item.get("eval_method", "")
    stars = item.get("stars", "")
    rec = " [recommended]" if item.get("recommended") else ""

    parts = [what]
    if langs:
        parts.append(f"Lang: {langs}")
    if method:
        parts.append(f"Method: {method}")
    if stars:
        parts.append(f"Stars: {stars}")

    desc = ". ".join(parts)
    if link:
        return f"- [{name}]({link}){rec}: {desc}"
    return f"- {name}{rec}: {desc}"


def generate_llms_txt(all_data):
    stats = json.loads((DATA / "stats.json").read_text()) if (DATA / "stats.json").exists() else {}
    total = stats.get("total", sum(len(v) for v in all_data.values()))

    lines = [
        "# Awesome SE Agent Eval",
        "",
        f"> A curated collection of {total} resources for evaluating AI Software Engineering Agents. "
        "Covers benchmarks, scoring methods, toolchain, leaderboards, and pitfalls.",
        "",
        "This repository is organized by evaluation workflow: "
        "what to evaluate → benchmarks → scoring methods → toolchain → leaderboards → pitfalls. "
        "All data lives in data/*.json as structured JSON. "
        "Query with jq or parse programmatically.",
        "",
    ]

    for fname, label in STAGE_ORDER:
        items = all_data.get(fname, [])
        if not items:
            continue
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"- [Full {label} list](docs/{STAGE_ORDER.index((fname, label)) + 2}-{fname}.md): {len(items)} resources")
        lines.append("")

    lines.append("## Guides")
    lines.append("")
    lines.append("- [Getting Started](docs/getting-started.md): 5-minute guide to choosing and running your first evaluation")
    lines.append("- [Evaluation Dimensions](docs/1-dimensions.md): Framework for what to measure")
    lines.append("- [Coverage Landscape](docs/landscape.md): Visual map of benchmark coverage and gaps")
    lines.append("")

    lines.append("## For Agents")
    lines.append("")
    lines.append("- [AGENTS.md](AGENTS.md): Structured query interface with jq commands and Python snippets")
    lines.append("- [Data Schema](data/schema.json): JSON Schema for all entries")
    lines.append("- [Statistics](data/stats.json): Aggregate counts and top tags")
    lines.append("")

    lines.append("## Optional")
    lines.append("")
    lines.append("- [Contributing Guide](CONTRIBUTING.md): How to add new resources")
    lines.append("- [Changelog](CHANGELOG.md): Version history")
    lines.append("")

    return "\n".join(lines)


def generate_llms_full_txt(all_data):
    stats = json.loads((DATA / "stats.json").read_text()) if (DATA / "stats.json").exists() else {}
    total = stats.get("total", sum(len(v) for v in all_data.values()))

    lines = [
        "# Awesome SE Agent Eval — Full Content",
        "",
        f"> {total} curated resources for evaluating AI Software Engineering Agents.",
        "",
    ]

    for fname, label in STAGE_ORDER:
        items = all_data.get(fname, [])
        if not items:
            continue

        lines.append(f"## {label} ({len(items)})")
        lines.append("")

        by_sub = {}
        for item in items:
            sub = item.get("subcategory", "other")
            by_sub.setdefault(sub, []).append(item)

        for sub in sorted(by_sub.keys()):
            sub_items = by_sub[sub]
            sub_label = SUBCATEGORY_LABELS.get(sub, sub.replace("-", " ").title())
            lines.append(f"### {sub_label} ({len(sub_items)})")
            lines.append("")
            for item in sorted(sub_items, key=lambda x: -(x.get("stars") or 0)):
                lines.append(entry_line(item))
            lines.append("")

    return "\n".join(lines)


def main():
    all_data = load_data()

    llms_txt = generate_llms_txt(all_data)
    out1 = ROOT / "llms.txt"
    out1.write_text(llms_txt)
    print(f"Generated {out1} ({len(llms_txt.splitlines())} lines)")

    llms_full = generate_llms_full_txt(all_data)
    out2 = ROOT / "llms-full.txt"
    out2.write_text(llms_full)
    print(f"Generated {out2} ({len(llms_full.splitlines())} lines)")


if __name__ == "__main__":
    main()
