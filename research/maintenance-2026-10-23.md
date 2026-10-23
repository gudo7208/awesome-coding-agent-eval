# Catalog maintenance — 2026-10-23

## Scope and sources

Focused public-source review of work indexed since the previous main-branch update
on 2026-09-07, through 2026-10-23. Searches covered coding-agent benchmarks,
specification-based validation, test generation, context retrieval, harness
engineering, repository-policy compliance, repeated-run reliability, and
performance-validation evidence. This is a curated increment, not an exhaustive
survey of the interval. Official arXiv records were opened to verify titles,
authors, scope, and reported evaluation units before inclusion.

## Added resources

| Resource | Primary source | Placement | Inclusion rationale |
|---|---|---|---|
| AgentSWE | [2610.13361](https://arxiv.org/abs/2610.13361) | Benchmark / End-to-end | 25 agent-software tasks; acceptance exercises frozen submissions on held-out requirements. |
| SpecGuardBench | [2610.16870](https://arxiv.org/abs/2610.16870) | Benchmark / Testing | 291 tasks evaluate whether executable harnesses accept permitted implementations and reject specification violations. Reference implementations are visible during construction. |
| VulContextBench | [2609.32601](https://arxiv.org/abs/2609.32601) | Benchmark / Security | 111 vulnerability-introducing commits evaluate retrieved and cited evidence rather than verdict accuracy alone. |
| TestSuiteBench | [2610.13065](https://arxiv.org/abs/2610.13065) | Benchmark / Testing | 165 applications evaluate specification-driven test suites using requirement-derived mutants. |
| Doc2Harness | [2610.20344](https://arxiv.org/abs/2610.20344) | Benchmark / Long-horizon | Frozen generated harnesses face scripted mock models and deterministic observable checks. The reported 328 test cases are not treated as 328 independent build tasks. |
| SWE-CC | [2610.06193](https://arxiv.org/abs/2610.06193) | Benchmark / Production | 500 contribution tasks audit repository-policy compliance in runtime behavior and final artifacts. |
| Identical Runs, Different Results | [2609.33812](https://arxiv.org/abs/2609.33812) | Meta-analysis / Quality study | Replication evidence on variance, compliance, cost, and temporal generalization; limited to one ML optimization task. |
| Performance-validation PR study | [2610.03969](https://arxiv.org/abs/2610.03969) | Meta-analysis / Quality study | Compares quantitative performance evidence in agent and human optimization contributions. |

Paper-only records do not imply that runnable code or downloadable benchmark
assets were independently verified. Repository links were attached only where
the official source identified them. No performance result was reproduced.

## Counts and validation

- Source records: 967 → 975; benchmarks 556 → 562; meta-analysis 119 → 121.
- Unchanged: methodology 148, toolchain 121, leaderboards 23.
- Deduplicated by unversioned arXiv identifier, normalized title, and record ID.
- Updated stale agent-guide counts from actual JSON data.
- Regenerated stats, README, docs, and both LLM-facing indexes with repository scripts.
- Schema, ID uniqueness, link presence, and new-description length checks pass.
- Deep audit before and after is identical: four intentional shared-URL groups
  (SWE-bench family and LiveCodeBench/leaderboard), plus 35 existing paper-link
  enrichment gaps. No new findings were introduced.

## Maintenance infrastructure observed

The paper-collection and weekly star-update workflows currently declare only
`workflow_dispatch`. They do not currently schedule collection or star refreshes.
The latest inspected Link Check completed successfully on 2026-10-21. No schedule,
credential setting, or automatic merge policy was changed in this content update.
The open external observability PRs were inspected for context; this update does
not close them or post contributor-facing comments.
