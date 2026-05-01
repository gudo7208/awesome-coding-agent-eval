#!/usr/bin/env python3
"""Generate README.md from data/*.json."""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = ROOT / "README.md"

STAGE_DOCS = {
    "benchmarks": ("② Benchmarks & Datasets", "docs/2-benchmarks.md"),
    "methodology": ("③ Evaluation Methodology", "docs/3-methodology.md"),
    "toolchain": ("④ Evaluation Toolchain", "docs/4-toolchain.md"),
    "leaderboards": ("⑤ Leaderboards", "docs/5-leaderboards.md"),
    "meta-analysis": ("⑥ Meta-Analysis & Pitfalls", "docs/6-meta-analysis.md"),
}

RELATED = [
    ("LLM Code Benchmarks", "tongye98/Awesome-Code-Benchmark", "https://github.com/tongye98/Awesome-Code-Benchmark"),
    ("LLM for SE (papers)", "iSEngLab/AwesomeLLM4SE", "https://github.com/iSEngLab/AwesomeLLM4SE"),
    ("Agent Tools & Frameworks", "kyrolabs/awesome-agents", "https://github.com/kyrolabs/awesome-agents"),
    ("Agent Harness Engineering", "Picrew/awesome-agent-harness", "https://github.com/Picrew/awesome-agent-harness"),
    ("AI Coding Tool Reviews", "murataslan1/ai-agent-benchmark", "https://github.com/murataslan1/ai-agent-benchmark"),
]

# emoji tags for item types
TYPE_EMOJI = {
    "paper": "📝",
    "paper+repo": "📝",
    "repo": "🔧",
    "tool": "🔧",
    "leaderboard": "📊",
    "website": "🌐",
    "blog": "🌐",
    "survey": "📝",
}

LANG_EMOJI = {
    "python": "🐍",
    "java": "☕",
    "javascript": "🟨",
    "typescript": "🔷",
    "go": "🐹",
    "rust": "🦀",
    "c++": "⚙️",
    "cpp": "⚙️",
    "ruby": "💎",
    "c#": "🟣",
}

SUBCATEGORY_SEE_ALSO = {
    "bug-fix": ["end-to-end", "testing"],
    "end-to-end": ["bug-fix", "long-horizon"],
    "long-horizon": ["end-to-end", "large-codebase"],
    "large-codebase": ["long-horizon", "end-to-end"],
    "code-review": ["testing", "llm-judge"],
    "testing": ["bug-fix", "code-review"],
    "security": ["testing", "bug-fix"],
    "llm-judge": ["process-eval", "execution-based"],
    "process-eval": ["llm-judge", "hybrid"],
    "execution-based": ["llm-judge", "harness"],
    "harness": ["sandbox", "execution-based"],
    "sandbox": ["harness", "observability"],
}


def load_all():
    items = {}
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        items[f.stem] = json.loads(f.read_text())
    return items


def item_link(item):
    url = item.get("repo") or item.get("website") or item.get("paper") or ""
    name = item["name"]
    return f"[{name}]({url})" if url else name


def item_emoji(item):
    emojis = []
    t = item.get("type", "")
    if e := TYPE_EMOJI.get(t):
        emojis.append(e)
    for lang in item.get("languages", []):
        if e := LANG_EMOJI.get(lang):
            emojis.append(e)
            break
    return " ".join(emojis)


def _extract_year(item):
    import re
    if item.get("venue"):
        m = re.search(r"20\d{2}", item["venue"])
        if m:
            return m.group()
    for key in ("paper", "repo", "website"):
        url = item.get(key, "")
        m = re.search(r"arxiv\.org/(?:abs|html|pdf)/(\d{2})\d{2}\.", url)
        if m:
            prefix = int(m.group(1))
            return str(2000 + prefix) if prefix < 50 else str(1900 + prefix)
    return "-"


def top30_benchmark_table(benchmarks):
    def sort_key(b):
        is_rec = 1 if b.get("recommended") else 0
        has_lb = 1 if b.get("related", {}).get("leaderboard") else 0
        stars = b.get("stars") or 0
        return (-is_rec, -has_lb, -stars, b.get("name", "").lower())

    sorted_b = sorted(benchmarks, key=sort_key)
    top30 = sorted_b[:30]

    rows = []
    rows.append("| Benchmark | What | Lang | Scale | Method | Year | ⭐ |")
    rows.append("|---|---|---|---|---|---|---|")
    for b in top30:
        name = item_link(b)
        rec = " ✅" if b.get("recommended") else ""
        what = (b.get("what") or "")[:70]
        langs = ", ".join(b.get("languages", [])) or "-"
        scale = str(b["scale"]) if b.get("scale") else "-"
        method = b.get("eval_method") or "-"
        year = _extract_year(b)
        stars = str(b["stars"]) if b.get("stars") else "-"
        rows.append(f"| {name}{rec} | {what} | {langs} | {scale} | {method} | {year} | {stars} |")
    return rows


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


def section_details(stage, label, items):
    """Render a <details> section for a stage, grouped by subcategory."""
    n = len(items)
    lines = []
    lines.append("<details>")
    lines.append(f"<summary>{label} ({n} resources)</summary>")
    lines.append("")

    by_sub = defaultdict(list)
    for item in items:
        by_sub[item.get("subcategory", "other")].append(item)

    for sub, sub_items in sorted(by_sub.items()):
        heading = SUBCATEGORY_LABELS.get(sub, sub.replace('-', ' ').title())
        lines.append(f"### {heading}")
        lines.append("")
        for item in sorted(sub_items, key=lambda x: -(x.get("stars") or 0)):
            link = item_link(item)
            desc = (item.get("what") or "")[:80]
            emojis = item_emoji(item)
            prefix = f"{emojis} " if emojis else ""
            venue = f" `{item['venue']}`" if item.get("venue") else ""
            lines.append(f"- {prefix}{link}{venue} — {desc}.")
        lines.append("")
        see_also = SUBCATEGORY_SEE_ALSO.get(sub, [])
        if see_also:
            refs = ", ".join(
                f"[{SUBCATEGORY_LABELS.get(s, s)}](#{s})" for s in see_also
                if s in SUBCATEGORY_LABELS
            )
            lines.append(f"> See also: {refs}")
            lines.append("")

    lines.append("</details>")
    return lines


def generate():
    all_data = load_all()
    benchmarks = all_data.get("benchmarks", [])
    counts = {k: len(v) for k, v in all_data.items()}
    total = sum(counts.values())

    lines = []

    # 1. Header
    lines += [
        '<div align="center">',
        "  <h1>Awesome SE Agent Eval</h1>",
        "  <p>A curated collection of resources for evaluating AI Software Engineering Agents</p>",
        "",
        '  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>',
        f'  <img src="https://img.shields.io/badge/resources-{total}-blue" alt="Resources">',
        '  <img src="https://img.shields.io/badge/updated-weekly-green" alt="Updated weekly">',
        '  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC--BY--4.0-lightgrey" alt="License"></a>',
        '  <img src="https://img.shields.io/badge/links-checked-brightgreen" alt="Link Check">',
        "</div>",
        "",
    ]

    # 2. 3-sentence positioning
    lines += [
        '> **What**: Benchmarks, tools, methodologies, and insights for evaluating AI agents on real-world software engineering tasks.',
        ">",
        "> **Scope**: SE agent evaluation only — bug fixing, code review, testing, architecture, long-horizon development.",
        ">",
        "> **Not**: General LLM benchmarks, agent frameworks, or product reviews. See [Related Resources](#-related-resources) for those.",
        "",
    ]

    # 3. Quick Start navigation table
    lines += [
        "## Quick Start",
        "",
        "| I want to... | Go to |",
        "|---|---|",
        "| Get started in 5 minutes | → [Getting Started Guide](docs/getting-started.md) |",
        "| Understand what to evaluate | → [① Evaluation Dimensions](docs/1-dimensions.md) |",
        f"| Find the right benchmark ({counts.get('benchmarks', 0)}) | → [② Benchmarks](#-top-30-benchmarks) |",
        f"| Understand scoring methods ({counts.get('methodology', 0)}) | → [③ Methodology](#-evaluation-methodology) |",
        f"| Set up evaluation infrastructure ({counts.get('toolchain', 0)}) | → [④ Toolchain](#-evaluation-toolchain) |",
        f"| See agent rankings ({counts.get('leaderboards', 0)}) | → [⑤ Leaderboards](#-leaderboards) |",
        f"| Learn about benchmark pitfalls ({counts.get('meta-analysis', 0)}) | → [⑥ Meta-Analysis](#-meta-analysis--pitfalls) |",
        "",
    ]

    # 4. Table of Contents
    lines += [
        "## Table of Contents",
        "",
        "- [Quick Start](#quick-start)",
        "- [Top 30 Benchmarks](#-top-30-benchmarks)",
        "- [② Benchmarks & Datasets](docs/2-benchmarks.md)",
        "- [③ Evaluation Methodology](#-evaluation-methodology)",
        "- [④ Evaluation Toolchain](#-evaluation-toolchain)",
        "- [⑤ Leaderboards](#-leaderboards)",
        "- [⑥ Meta-Analysis & Pitfalls](#-meta-analysis--pitfalls)",
        "- [Related Resources](#-related-resources)",
        "- [For AI Agents](#-for-ai-agents)",
        "- [Contributing](#contributing)",
        "",
    ]

    # 5. Trending / Recently Added
    recent = sorted(
        [b for b in benchmarks if b.get("added_date")],
        key=lambda x: x["added_date"],
        reverse=True,
    )[:8]
    if recent:
        lines += [
            "## 🔥 Recently Added",
            "",
        ]
        for b in recent:
            link = item_link(b)
            what = (b.get("what") or "")[:70]
            venue = f" `{b['venue']}`" if b.get("venue") else ""
            lines.append(f"- {link}{venue} — {what}")
        lines += ["", "---", ""]

    # 6. Top 30 Benchmarks table
    lines += [
        "## 📊 Top 30 Benchmarks",
        "",
    ]
    lines += top30_benchmark_table(benchmarks)
    lines += [
        "",
        f"→ [See all {len(benchmarks)} benchmarks](docs/2-benchmarks.md)",
        "",
    ]

    # 7. Must-Read picks
    must_reads = [b for b in benchmarks if b.get("recommended")]
    must_reads_by_sub = defaultdict(list)
    for b in must_reads:
        must_reads_by_sub[b.get("subcategory", "other")].append(b)
    pick_subs = ["bug-fix", "end-to-end", "security", "long-horizon", "code-review", "testing"]
    picks = []
    for sub in pick_subs:
        candidates = must_reads_by_sub.get(sub, [])
        if candidates:
            picks.append((sub, sorted(candidates, key=lambda x: -(x.get("stars") or 0))[0]))
    if picks:
        lines += [
            "## 📖 Must-Read by Category",
            "",
            "*If you read nothing else, start here — one recommended benchmark per task type.*",
            "",
            "| Task | Benchmark | Why |",
            "|---|---|---|",
        ]
        for sub, b in picks:
            label = SUBCATEGORY_LABELS.get(sub, sub)
            link = item_link(b)
            what = (b.get("what") or "")[:60]
            lines.append(f"| {label} | {link} | {what} |")
        lines += [""]

    # 6. Collapsible sections for each stage (② ~ ⑥)
    stage_order = ["methodology", "toolchain", "leaderboards", "meta-analysis"]
    stage_headings = {
        "methodology": "## 📐 Evaluation Methodology",
        "toolchain": "## 🔧 Evaluation Toolchain",
        "leaderboards": "## 🏆 Leaderboards",
        "meta-analysis": "## 🔬 Meta-Analysis & Pitfalls",
    }

    for stage in stage_order:
        label_full = STAGE_DOCS[stage][0]
        items = all_data.get(stage, [])
        lines.append(stage_headings[stage])
        lines.append("")
        lines += section_details(stage, label_full, items)
        lines.append("")

    # 7. Related Resources
    lines += [
        "## 🔗 Related Resources",
        "",
        "Complementary awesome lists (no duplication):",
        "",
        "| Topic | Recommended |",
        "|---|---|",
    ]
    for desc, name, url in RELATED:
        lines.append(f"| {desc} | [{name}]({url}) |")
    lines.append("")

    # 8. For AI Agents
    lines += [
        "## 🤖 For AI Agents",
        "",
        "→ [AGENTS.md](AGENTS.md) — Structured query interface for AI agents",
        "",
        "All data lives in `data/` as JSON. Query with `jq` or parse programmatically.",
        "",
    ]

    # 9. Contributing
    lines += [
        "## Contributing",
        "",
        "PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.",
        "",
        "Quick checklist:",
        "1. Resource is related to SE Agent evaluation",
        "2. Add to the appropriate `data/*.json` file",
        "3. Fill required schema fields (id, name, stage, subcategory, what, type, tags)",
        "4. Run `python scripts/process/validate.py` to verify",
        "",
    ]

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Generated {OUT} ({len(lines)} lines)")


if __name__ == "__main__":
    generate()
