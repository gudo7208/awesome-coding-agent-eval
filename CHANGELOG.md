# Changelog

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
