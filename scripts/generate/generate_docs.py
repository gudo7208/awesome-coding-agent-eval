#!/usr/bin/env python3
"""Generate docs/1-6.md from data/*.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
DOCS = ROOT / "docs"

SUBCATEGORY_LABELS = {
    "bug-fix": "Bug Fix & Issue Resolution",
    "long-horizon": "Long-Horizon / Evolution",
    "end-to-end": "End-to-End / Multi-Task",
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

# Emoji tags for common tag values
TAG_EMOJIS = {
    "production": "🏭",
    "real-world": "🌍",
    "multilingual": "🌐",
    "multi-language": "🌐",
    "python": "🐍",
    "java": "☕",
    "javascript": "🟨",
    "typescript": "🔷",
    "go": "🐹",
    "rust": "🦀",
    "c++": "⚙️",
    "security": "🔒",
    "vulnerability": "🔒",
    "llm-judge": "🤖",
    "human-eval": "👤",
    "contamination-free": "✅",
    "leaderboard": "🏆",
    "survey": "📋",
    "long-horizon": "📅",
    "multi-agent": "🤝",
    "large-scale": "📦",
    "process-eval": "🔍",
}


def load_json(name):
    p = DATA / f"{name}.json"
    if not p.exists():
        return []
    return json.loads(p.read_text())


def get_link(item):
    return item.get("repo") or item.get("paper") or item.get("website") or ""


def get_emoji_tags(item):
    tags = item.get("tags", [])
    emojis = []
    for tag in tags:
        if tag in TAG_EMOJIS:
            emoji = TAG_EMOJIS[tag]
            if emoji not in emojis:
                emojis.append(emoji)
    return " ".join(emojis[:3])  # max 3 emojis


def resource_line(item):
    name = item["name"]
    link = get_link(item)
    if link:
        name = f"[{name}]({link})"
    what = item.get("what", "")
    stars = f" ⭐{item['stars']}" if item.get("stars") else ""
    emojis = get_emoji_tags(item)
    emoji_str = f" {emojis}" if emojis else ""
    return f"- {name}{stars} — {what}.{emoji_str}"


def alpha_group_label(name):
    c = name[0].upper() if name else "?"
    if "A" <= c <= "F":
        return "A–F"
    elif "G" <= c <= "L":
        return "G–L"
    elif "M" <= c <= "R":
        return "M–R"
    else:
        return "S–Z"


SUBCATEGORY_INTROS = {
    "bug-fix": "The most established evaluation category. SWE-bench family dominates. Start with SWE-bench Verified for a reliable baseline.",
    "end-to-end": "Evaluates agents on complete project development, not just isolated fixes. Growing rapidly as agents become more capable.",
    "long-horizon": "Tests multi-step, multi-file changes over extended interactions. Closer to real engineering work than single-issue benchmarks.",
    "large-codebase": "Evaluates navigation and modification in large-scale repos (>50K LOC). Tests real-world scalability.",
    "code-review": "Measures quality of review comments and suggestions. Emerging area with high practical value.",
    "testing": "Evaluates test generation, bug reproduction, and QA capabilities.",
    "security": "Benchmarks for vulnerability detection, secure code generation, and penetration testing.",
    "harness": "Frameworks that orchestrate benchmark execution. Pick one that supports your target benchmark.",
    "sandbox": "Isolated execution environments for running agent-generated code safely.",
    "llm-judge": "Using LLMs to score agent outputs. Faster than execution-based but less reliable. Calibrate carefully.",
    "process-eval": "Evaluates HOW the agent works (trajectory, reasoning), not just final output. Key for debugging agent behavior.",
    "limitation": "Critical reading before trusting any benchmark score. Understand what scores don't tell you.",
    "quality-study": "Empirical analyses of agent output quality at scale. Data-driven insights.",
    "blog": "Practitioner perspectives and lessons learned from real evaluation efforts.",
}


def render_section(sub, items):
    label = SUBCATEGORY_LABELS.get(sub, sub.replace("-", " ").title())
    lines = []
    lines.append(f'<a id="{sub}"></a>')
    lines.append(f"## {label}")
    lines.append("")
    if sub in SUBCATEGORY_INTROS:
        lines.append(f"*{SUBCATEGORY_INTROS[sub]}*")
        lines.append("")
    sorted_items = sorted(items, key=lambda x: x.get("name", "").upper())
    if len(sorted_items) > 30:
        # Group alphabetically
        groups = {}
        for item in sorted_items:
            g = alpha_group_label(item.get("name", ""))
            groups.setdefault(g, []).append(item)
        for g_label in ["A–F", "G–L", "M–R", "S–Z"]:
            if g_label not in groups:
                continue
            lines.append(f"### {g_label}")
            lines.append("")
            for item in groups[g_label]:
                lines.append(resource_line(item))
            lines.append("")
    else:
        for item in sorted_items:
            lines.append(resource_line(item))
        lines.append("")
    return lines


def build_toc(grouped, ordered_subs):
    lines = ["## Contents", ""]
    for sub in ordered_subs:
        if sub not in grouped:
            continue
        label = SUBCATEGORY_LABELS.get(sub, sub.replace("-", " ").title())
        count = len(grouped[sub])
        lines.append(f"- [{label} ({count})](#{sub})")
    lines.append("")
    return lines


def generate_page(items, title, intro, ordered_subs=None):
    grouped = {}
    for item in items:
        sub = item.get("subcategory", "other")
        grouped.setdefault(sub, []).append(item)

    if ordered_subs is None:
        ordered_subs = sorted(grouped.keys())

    lines = [f"# {title}", "", intro, ""]
    lines += build_toc(grouped, ordered_subs)

    for sub in ordered_subs:
        if sub not in grouped:
            continue
        lines += render_section(sub, grouped[sub])

    lines.append("---")
    lines.append("")
    lines.append("[← Back to README](../README.md)")
    lines.append("")
    return "\n".join(lines)


DIMENSIONS_EN = """\
# ① Evaluation Dimensions

Before evaluating an SE Agent, decide what to measure. This page maps the full capability space and shows where benchmarks exist vs. where the gaps are.

→ See [Landscape](landscape.md) for coverage visualization.

## Contents

- [Dimension Framework](#dimension-framework)
- [Dimension Details](#dimension-details)
- [Current Gaps](#current-gaps)

<a id="dimension-framework"></a>
## Dimension Framework

| Dimension | Description | Benchmarks | Coverage |
|---|---|---|---|
| Bug Localization & Fix | From issue to patch | [SWE-bench](2-benchmarks.md#bug-fix), [LiveCodeBench](2-benchmarks.md#bug-fix) | ████ 40 |
| End-to-End Development | Complete feature implementation | [OmniCode](2-benchmarks.md#end-to-end), [SWE-bench Pro](2-benchmarks.md#long-horizon) | █████ 60 |
| Code Review & PR Quality | Review comment quality, mergeability | [CR-Bench](2-benchmarks.md#code-review) | ██ 18 |
| Test Generation & QA | Writing tests, verifying correctness | [SWT-Bench](2-benchmarks.md#testing) | ██ 22 |
| Security & Vulnerability | Secure code, vulnerability detection | [CVE-Bench](2-benchmarks.md#security) | ███ 23 |
| Long-Horizon Evolution | Multi-step, cross-version development | [SWE-EVO](2-benchmarks.md#long-horizon) | █ 13 |
| Codebase Navigation | Understanding project structure | [CodeScaleBench](2-benchmarks.md#large-codebase) | █ 7 |
| Requirements Understanding | From vague requirements to tasks | — | ⚠️ Gap |
| Architecture Decisions | Choosing among design alternatives | — | ⚠️ Gap |
| Multi-Agent Collaboration | Coordinated multi-agent systems | [MARBLE](2-benchmarks.md#end-to-end) | ⚠️ 5 |

<a id="dimension-details"></a>
## Dimension Details

### Bug Localization & Fix
The most established category. SWE-bench family is the de facto standard. Start with **SWE-bench Verified** (500 human-verified issues) for a reliable baseline. For multi-language, use **Multi-SWE-bench**.
→ [All bug-fix benchmarks](2-benchmarks.md#bug-fix)

### End-to-End Development
Goes beyond isolated fixes — tests full feature implementation, project setup, and delivery. Growing rapidly. **OmniCode** covers multiple SE task types; **SWE-bench Pro** tests long-horizon multi-step work.
→ [All end-to-end benchmarks](2-benchmarks.md#end-to-end)

### Code Review & PR Quality
Measures quality of review comments and suggestions. High practical value but fewer benchmarks. **CodeFuse-CR-Bench** covers end-to-end review; **CodeCriticBench** focuses on critique quality.
→ [All code review benchmarks](2-benchmarks.md#code-review)

### Test Generation & QA
Evaluates test writing, bug reproduction, and verification. **SWT-Bench** is the primary benchmark. Closely related to bug-fix (agents that can write reproducing tests fix bugs better).
→ [All testing benchmarks](2-benchmarks.md#testing)

### Security & Vulnerability
Benchmarks for vulnerability detection, secure code generation, and penetration testing. **CVE-Bench** uses real CVEs; **CyberGym** tests at scale.
→ [All security benchmarks](2-benchmarks.md#security)

### Long-Horizon Evolution
Tests multi-step, multi-file changes over extended interactions. Closer to real engineering than single-issue benchmarks. **SWE-EVO** uses real software evolution scenarios.
→ [All long-horizon benchmarks](2-benchmarks.md#long-horizon)

### Engineering Efficiency
Token consumption, time cost, and Pareto optimality. Not a separate benchmark category — measured alongside other benchmarks. Check individual benchmark leaderboards for efficiency metrics.

<a id="current-gaps"></a>
## Current Gaps

These dimensions lack dedicated benchmarks — they represent the frontier of SE agent evaluation:

- **Requirements Understanding** — SWE-bench provides well-defined issues, skipping the hardest part: understanding what to build from vague requirements
- **Architecture Decisions** — No benchmark evaluates an agent's ability to choose among design alternatives, assess trade-offs, or make system-level decisions
- **Multi-Agent Collaboration** — Almost no benchmarks for multi-agent SE systems (MARBLE is the closest, but focuses on general collaboration, not SE-specific workflows)

These gaps are opportunities for new benchmark development.

---

[← Back to README](../README.md)
"""


def generate():
    DOCS.mkdir(exist_ok=True)

    (DOCS / "1-dimensions.md").write_text(DIMENSIONS_EN)
    print("Generated docs/1-dimensions.md")

    benchmarks = load_json("benchmarks")
    ordered_benchmarks = [
        "bug-fix", "end-to-end", "long-horizon", "large-codebase",
        "code-review", "testing", "security", "production",
        "code-generation", "feature-development", "multi-agent",
    ]
    text = generate_page(
        benchmarks,
        "② Benchmarks & Datasets",
        "SE Agent benchmarks organized by task type.",
        ordered_benchmarks,
    )
    (DOCS / "2-benchmarks.md").write_text(text)
    print(f"Generated docs/2-benchmarks.md ({len(benchmarks)} items)")

    methodology = load_json("methodology")
    ordered_methodology = [
        "llm-judge", "process-eval", "execution-based", "hybrid", "human-eval",
    ]
    text = generate_page(
        methodology,
        "③ Evaluation Methodology",
        "Different scoring approaches, each with trade-offs.",
        ordered_methodology,
    )
    (DOCS / "3-methodology.md").write_text(text)
    print(f"Generated docs/3-methodology.md ({len(methodology)} items)")

    toolchain = load_json("toolchain")
    ordered_toolchain = ["harness", "sandbox", "observability", "judge-tool"]
    text = generate_page(
        toolchain,
        "④ Evaluation Toolchain",
        "The tool stack you need to run an evaluation end-to-end.",
        ordered_toolchain,
    )
    (DOCS / "4-toolchain.md").write_text(text)
    print(f"Generated docs/4-toolchain.md ({len(toolchain)} items)")

    leaderboards = load_json("leaderboards")
    ordered_leaderboards = ["se-agent", "code-generation", "activity"]
    text = generate_page(
        leaderboards,
        "⑤ Leaderboards",
        "Aggregated rankings across benchmarks.",
        ordered_leaderboards,
    )
    (DOCS / "5-leaderboards.md").write_text(text)
    print(f"Generated docs/5-leaderboards.md ({len(leaderboards)} items)")

    meta = load_json("meta-analysis")
    ordered_meta = ["limitation", "quality-study", "survey", "blog"]
    text = generate_page(
        meta,
        "⑥ Meta-Analysis & Pitfalls",
        "Research on benchmark quality itself — know the traps before you trust the scores.",
        ordered_meta,
    )
    (DOCS / "6-meta-analysis.md").write_text(text)
    print(f"Generated docs/6-meta-analysis.md ({len(meta)} items)")


if __name__ == "__main__":
    generate()
