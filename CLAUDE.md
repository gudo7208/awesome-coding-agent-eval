# Awesome Coding Agent Eval

A curated collection of 900+ resources for evaluating AI coding agents.

## Data Architecture

Source of truth is `data/*.json` (5 files). README.md and docs/ are auto-generated — never edit them directly.

| File | Content | Count |
|---|---|---|
| data/benchmarks.json | Benchmarks & Datasets | 538 |
| data/methodology.json | Evaluation Methodology | 143 |
| data/toolchain.json | Toolchain (harness, sandbox) | 118 |
| data/leaderboards.json | Leaderboards | 23 |
| data/meta-analysis.json | Meta-Analysis & Pitfalls | 106 |

## Schema

Required fields: `id`, `name`, `stage`, `subcategory`, `what` (≤80 chars), `type`, `tags`

Key optional fields: `paper` (arXiv URL), `repo` (GitHub URL), `stars`, `languages`, `scale`, `eval_method` (execution-based/llm-judge/hybrid/human-eval), `venue`, `related` (cross-references), `recommended` (boolean)

## Commands

```bash
# Validate data
.venv/bin/python scripts/process/validate.py

# Regenerate README + docs from data
.venv/bin/python scripts/generate/generate_readme.py
.venv/bin/python scripts/generate/generate_docs.py
.venv/bin/python scripts/generate/generate_stats.py

# Run full collection pipeline (needs LLM_API_KEY env var)
.venv/bin/python scripts/collect/run_all.py --dry-run
```

## Conventions

- All entries go in `data/*.json`, not in README or docs
- `what` field must be ≤80 characters, English, format: "[Verb] [what] [for/on] [target]"
- `id` field: lowercase alphanumeric + hyphens only
- Every entry needs at least one link (`paper`, `repo`, or `website`)
- Run `validate.py` before committing
- LLM-dependent scripts read `LLM_API_KEY` and `LLM_BASE_URL` from environment

## Query Patterns

```bash
# Find recommended benchmarks
jq '[.[] | select(.recommended)] | length' data/benchmarks.json

# Search by subcategory
jq '.[] | select(.subcategory == "bug-fix") | {name, what, stars}' data/benchmarks.json

# Follow cross-references: benchmark → harness → leaderboard
jq '.[] | select(.id == "swe-bench") | .related' data/benchmarks.json

# Find by language
jq '.[] | select(.languages[]? == "python") | {name, what}' data/benchmarks.json
```

## What NOT to do

- Don't edit README.md or docs/*.md — they are generated
- Don't hardcode API keys — use environment variables
- Don't add entries without running validate.py
- Don't commit candidates/ or .checkpoint.json files
