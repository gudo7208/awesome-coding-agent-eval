# For AI Agents

This file helps AI agents (Claude Code, Cursor, Copilot, etc.) efficiently query this repository's evaluation resources.

## Data Layout

| File | Stage | Content | Count |
|---|---|---|---|
| data/benchmarks.json | ② | Benchmarks & Datasets | 530 |
| data/methodology.json | ③ | Evaluation Methodology | 133 |
| data/toolchain.json | ④ | Toolchain (harness, sandbox, observability) | 113 |
| data/leaderboards.json | ⑤ | Leaderboards | 24 |
| data/meta-analysis.json | ⑥ | Meta-Analysis & Pitfalls | 100 |
| data/stats.json | - | Statistics summary | - |
| data/schema.json | - | JSON Schema definition | - |

## Schema Quick Reference

Required: id, name, stage, subcategory, what, type, tags
Optional: paper, repo, website, stars, languages, scale, eval_method, venue, leaderboard_url, granularity, limitations, related, recommended

### Subcategory Values
- benchmark: bug-fix, end-to-end, long-horizon, large-codebase, code-review, testing, security, production, code-generation, multi-agent, feature-development
- methodology: llm-judge, process-eval, execution-based, hybrid, human-eval
- toolchain: harness, sandbox, observability, judge-tool
- leaderboard: se-agent, code-generation, activity
- meta-analysis: limitation, quality-study, blog, survey

## Common Query Scenarios

### 1. "Recommend a bug-fix benchmark"
```bash
jq '.[] | select(.subcategory == "bug-fix") | {name, what, stars, repo}' data/benchmarks.json
```

### 2. "Find multi-language benchmarks"
```bash
jq '.[] | select(.languages | length > 1) | {name, what, languages}' data/benchmarks.json
```

### 3. "What are the pitfalls of SWE-bench?"
```bash
jq '.[] | select(.related.meta_analysis != null) | select(.id | startswith("swe-bench")) | {name, related}' data/benchmarks.json
# Then look up the meta_analysis IDs:
jq '.[] | select(.id == "metr-merge-rate") | {name, what}' data/meta-analysis.json
```

### 4. "I need to set up an evaluation environment"
```bash
jq '.[] | select(.subcategory == "harness" or .subcategory == "sandbox") | {name, what, stars, repo}' data/toolchain.json
```

### 5. "What's new in the last month?"
```bash
jq '.[] | select(.added_date >= "2026-04-01") | {name, what, stage}' data/benchmarks.json
```

### 6. "Which benchmarks have leaderboards?"
```bash
jq '.[] | select(.related.leaderboard != null and (.related.leaderboard | length > 0)) | {name, leaderboard: .related.leaderboard}' data/benchmarks.json
```

### 7. "Compare execution-based vs LLM-judge methods"
```bash
jq '.[] | select(.subcategory == "execution-based" or .subcategory == "llm-judge") | {name, what, subcategory}' data/methodology.json
```

### 8. "Find code review evaluation resources"
```bash
jq '.[] | select(.subcategory == "code-review") | {name, what}' data/benchmarks.json
jq '.[] | select(.tags | any(. == "code-review")) | {name, what}' data/meta-analysis.json
```

### 9. "Get the complete evaluation kit for SWE-bench"
```bash
# Benchmark + harness + leaderboard + pitfalls in one query chain
BENCH=$(jq '.[] | select(.id == "swe-bench-verified")' data/benchmarks.json)
HARNESS_IDS=$(echo $BENCH | jq -r '.related.harness[]')
LEADER_IDS=$(echo $BENCH | jq -r '.related.leaderboard[]')
META_IDS=$(echo $BENCH | jq -r '.related.meta_analysis[]')
```

### 10. "Overview statistics"
```bash
jq '{total, by_stage, top_tags: [.top_tags[:5][] | "\(.tag) (\(.count))"]}' data/stats.json
```

## Combination Queries (using related field)

### From benchmark to full evaluation stack
Given a benchmark ID, find everything needed to run and interpret it:
1. The benchmark itself: `jq '.[] | select(.id == "ID")' data/benchmarks.json`
2. Its harness: `jq '.[] | select(.id == ("HARNESS_IDS"))' data/toolchain.json`
3. Its leaderboard: `jq '.[] | select(.id == ("LB_IDS"))' data/leaderboards.json`
4. Known pitfalls: `jq '.[] | select(.id == ("META_IDS"))' data/meta-analysis.json`

### From need to recommendation
"I want to evaluate X" → filter benchmarks by subcategory → check related.harness → check related.meta_analysis

## Data Freshness
- Updated weekly via GitHub Actions
- Star counts refreshed monthly
- Dead links checked weekly
