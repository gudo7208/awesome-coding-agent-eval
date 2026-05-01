# For AI Agents

This file helps AI agents efficiently query 900 SE agent evaluation resources. All data is structured JSON — no scraping needed.

## Quick Access

| Method | File | Best For |
|---|---|---|
| Full content dump | [llms-full.txt](llms-full.txt) | RAG ingestion, one-shot context loading |
| Structured index | [llms.txt](llms.txt) | Discovering what's available |
| Raw JSON | `data/*.json` | Precise filtering and programmatic access |
| Schema | [data/schema.json](data/schema.json) | Understanding field types |
| Statistics | [data/stats.json](data/stats.json) | Aggregate counts and trends |

## Data Layout

| File | Stage | Count |
|---|---|---|
| data/benchmarks.json | Benchmarks & Datasets | 530 |
| data/methodology.json | Evaluation Methodology | 133 |
| data/toolchain.json | Toolchain (harness, sandbox, observability) | 113 |
| data/leaderboards.json | Leaderboards | 24 |
| data/meta-analysis.json | Meta-Analysis & Pitfalls | 100 |

## Schema

Required: `id`, `name`, `stage`, `subcategory`, `what`, `type`, `tags`

Key optional fields:
- `paper` — arXiv or publication URL
- `repo` — GitHub repository URL
- `stars` — GitHub star count
- `languages` — programming languages (lowercase array)
- `scale` — number of test cases/issues
- `eval_method` — one of: execution-based, llm-judge, hybrid, human-eval
- `venue` — conference/journal (e.g. "ICLR 2026")
- `recommended` — boolean, editorially curated top picks
- `related` — cross-references: `{harness: [], leaderboard: [], meta_analysis: [], variants: []}`

### Subcategory Values
- benchmark: bug-fix, end-to-end, long-horizon, large-codebase, code-review, testing, security, production, code-generation, multi-agent, feature-development
- methodology: llm-judge, process-eval, execution-based, hybrid, human-eval
- toolchain: harness, sandbox, observability, judge-tool
- leaderboard: se-agent, code-generation, activity
- meta-analysis: limitation, quality-study, blog, survey

## Query Recipes

### jq (shell)

```bash
# Recommended benchmarks
jq '[.[] | select(.recommended)] | sort_by(-.stars) | .[:10] | .[] | {name, what, stars}' data/benchmarks.json

# Benchmarks by subcategory
jq '[.[] | select(.subcategory == "security")] | length' data/benchmarks.json

# Multi-language benchmarks
jq '.[] | select(.languages | length > 1) | {name, languages, what}' data/benchmarks.json

# Benchmarks with leaderboards
jq '.[] | select(.related.leaderboard | length > 0) | {name, leaderboard: .related.leaderboard}' data/benchmarks.json

# Recently added (last 30 days)
jq '.[] | select(.added_date >= "2026-04-01") | {name, what, subcategory}' data/benchmarks.json

# Full evaluation stack for a benchmark
jq '.[] | select(.id == "swe-bench") | {name, eval_method, scale, related}' data/benchmarks.json

# Cross-stage: find harness for a benchmark
HARNESS=$(jq -r '.[] | select(.id == "swe-bench") | .related.harness[]' data/benchmarks.json)
echo "$HARNESS" | while read id; do jq --arg id "$id" '.[] | select(.id == $id) | {name, what, repo}' data/toolchain.json; done
```

### Python

```python
import json
from pathlib import Path

data_dir = Path("data")

def load(name):
    return json.loads((data_dir / f"{name}.json").read_text())

benchmarks = load("benchmarks")
toolchain = load("toolchain")

# Top 10 recommended by stars
recommended = sorted(
    [b for b in benchmarks if b.get("recommended")],
    key=lambda x: -(x.get("stars") or 0)
)[:10]

# Find all resources for a specific benchmark
def get_eval_stack(benchmark_id):
    bench = next((b for b in benchmarks if b["id"] == benchmark_id), None)
    if not bench:
        return None
    rel = bench.get("related", {})
    return {
        "benchmark": bench,
        "harnesses": [t for t in toolchain if t["id"] in rel.get("harness", [])],
        "leaderboards": [l for l in load("leaderboards") if l["id"] in rel.get("leaderboard", [])],
        "pitfalls": [m for m in load("meta-analysis") if m["id"] in rel.get("meta_analysis", [])],
    }

stack = get_eval_stack("swe-bench")
```

## Common Agent Tasks

### "Help me choose a benchmark for my use case"
1. Read `data/stats.json` for overview
2. Filter `data/benchmarks.json` by `subcategory` matching the use case
3. Sort by `recommended` first, then `stars`
4. For top picks, check `related.meta_analysis` for known pitfalls

### "Set up an evaluation environment"
1. Pick benchmark from `data/benchmarks.json`
2. Follow `related.harness` IDs → look up in `data/toolchain.json`
3. Follow `related.leaderboard` IDs → look up in `data/leaderboards.json`

### "What scoring method should I use?"
1. Read `data/methodology.json`, filter by `subcategory`
2. `execution-based` = deterministic, needs test suite
3. `llm-judge` = flexible, needs calibration
4. `hybrid` = combines both

### "What are the known problems with benchmark X?"
1. Find benchmark in `data/benchmarks.json`
2. Read `related.meta_analysis` array
3. Look up each ID in `data/meta-analysis.json`

## Data Freshness
- Updated weekly via GitHub Actions
- Star counts refreshed weekly
- Dead links checked weekly (lychee)
- New papers discovered via 6 collection sources: arXiv, recency sweep, GitHub, citation chain, competitor diff, venue proceedings
