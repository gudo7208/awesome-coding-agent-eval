# Changelog

## Unreleased (2026-09-07)

### Weekly Evaluation Refresh

- Added SWE-Gate's released execution benchmark for review-constraint compliance
- Added trajectory-aware subset evaluation and commit-first judge reliability research
- Added CATJudge's runnable code-driven web-app testing toolchain
- Added three studies of late requirements, benchmark task demands, and coding-harness architecture
- Deferred unreleased benchmark assets and excluded general-agent work without a direct software-engineering evaluation target
- Regenerated derived documentation and statistics for 967 total resources

### Corpus Refresh and Maintenance

- Fast-forwarded the local baseline to the 947-resource remote corpus while preserving the in-progress rubric work
- Added nine verified resources from recent papers and open community contributions: four benchmarks, one methodology, two observability tools, and two meta-analysis resources
- Fixed daily collection deduplication so versioned arXiv URLs match unversioned corpus entries
- Disabled the failing daily collection and weekly star schedules while retaining manual workflow dispatch
- Regenerated all derived outputs for 960 total resources and refreshed the agent-facing counts and recent-date query
- Investigated the scheduled workflows: daily collection is blocked by a missing `LLM_API_KEY`, while weekly star branches are pushed but PR creation is disabled for GitHub Actions

### Rubrics Research and Cross-Stage Index

- Added a Chinese research report on rubric design, generation, calibration, reliability, and use in coding-agent evaluation
- Added four SE-agent-relevant resources: Agentic Rubrics, AdaRubric, RuVerBench, and the experiment-reproduction rubric meta-evaluation
- Added optional structured `rubric` metadata and a generated cross-stage Rubrics view
- Added rubric role and target statistics plus agent-facing query recipes
- Regenerated README, docs, statistics, and both LLM indexes; collection and validation workflows now include the LLM exports

## v1.0.0 (2026-05-01)

### Production-Ready Release
- 900 curated resources across 5 categories
- Evaluation workflow: Benchmarks (530) → Methodology (133) → Toolchain (113) → Leaderboards (24) → Meta-Analysis (100)
- Top 30 table with eval_method, scale, languages, year columns — zero empty cells on method/year
- 98% related field coverage (cross-references between benchmarks, harnesses, leaderboards, meta-analyses)
- 27 recommended benchmarks with ✅ markers
- 6 collection sources: arXiv keywords, recency sweep, GitHub search, citation chain, competitor diff, venue proceedings
- Collection orchestrator (run_all.py) with --dry-run and --skip-llm modes
- Dead-link CI workflow (lychee)
- README visual polish: badges, Recently Added section, Must-Read by Category, See Also cross-references
- Schema extended with venue and leaderboard_url fields
- All API keys moved to environment variables

## v0.1.0 (2026-04-29)

### Initial Release
- 428 curated resources across 5 categories
- Evaluation workflow: Benchmarks (228) → Methodology (58) → Toolchain (82) → Leaderboards (6) → Meta-Analysis (54)
- Structured JSON data with schema validation
- Auto-generated README and docs from data
- GitHub Actions for weekly collection and validation
- Agent-friendly query interface (AGENTS.md)
