# Corpus Maintenance — Reference

- [Relevance criteria](#relevance-criteria)
- [Controlled vocabulary](#controlled-vocabulary)
- [The `what` field](#the-what-field)
- [Entry schema](#entry-schema)
- [Fix ops format](#fix-ops-format)
- [Parallel curation / rewrite pattern](#parallel-curation--rewrite-pattern)

---

## Relevance criteria

This corpus is specifically about **evaluating AI coding / software-engineering agents**.

**INCLUDE** only if the resource is one of:
- a benchmark/dataset for code tasks (code generation, bug-fix, code review, testing /
  unit-test generation, repo-level / large-codebase, security / vulnerability of code,
  CI, program repair, spec / verification, web/UI-from-spec coding) → `stage: benchmark`
- an evaluation **methodology** for code agents (LLM-as-judge, process / trajectory
  evaluation, execution-based, hybrid, human-eval) → `stage: methodology`
- a **toolchain** for running/evaluating code agents (harness, sandbox, observability,
  judge tooling) → `stage: toolchain`
- a **leaderboard** for code agents → `stage: leaderboard`
- a **meta-analysis** / pitfall study / survey about code-agent evaluation → `stage: meta-analysis`

**EXCLUDE** (be ruthless):
- pure model releases or training methods (RL, distillation, prompt-opt) with no
  code-specific evaluation contribution
- general-agent benchmarks NOT about code: GUI / web / phone / mobile / game / social /
  medical / finance / memory / tool-use agents — unless clearly coding/SE-specific
- pure ML / CV / NLP / robotics / physics / bio / hardware papers
- agent frameworks without an evaluation contribution

When in doubt, exclude. A curated list wins on precision, not volume.

---

## Controlled vocabulary

`subcategory` MUST come from the list for its `stage` (audit.py flags violations as
`taxonomy`). Do not invent new subcategories — normalize to the nearest fit; the precise
nuance lives in `tags`.

| stage | valid subcategories |
|---|---|
| benchmark | bug-fix, end-to-end, long-horizon, large-codebase, code-review, testing, security, production, code-generation, multi-agent, feature-development |
| methodology | llm-judge, process-eval, execution-based, hybrid, human-eval |
| toolchain | harness, sandbox, observability, judge-tool |
| leaderboard | se-agent, code-generation, activity |
| meta-analysis | limitation, quality-study, blog, survey |

`eval_method` (optional, on benchmark/methodology): `execution-based`, `llm-judge`,
`hybrid`, `human-eval`.

This table is the single source of truth; it is mirrored in
`scripts/process/classify_candidates.py`, `merge_classified.py`, and `audit.py`.
If you ever extend it, update all four.

---

## The `what` field

A concise, scannable description — the most-read field after `name`.

- **≤ 80 characters**, English, one phrase.
- Format: `[Verb] [what] for/on [target]`. Lead with a verb: Evaluate / Benchmark /
  Measure / Assess / Study / Analyze / Survey / Detect / Generate / Rank / Provide /
  Diagnose.
- **Never** the title verbatim (audit + readability rely on this). Never repeat the
  artifact's own name.
- Be faithful: compress what the title/abstract states; do not invent numbers,
  datasets, or capabilities.

Examples:

| name | what |
|---|---|
| SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Resolve real-world GitHub issues to test agent patch generation |
| AssertionBench: A Benchmark to Evaluate LLMs for Assertion Generation | Evaluate LLMs on hardware assertion generation |
| A Survey of Code Review Benchmarks... | Survey code review benchmarks across pre-LLM and LLM eras |

---

## Entry schema

Required: `id`, `name`, `stage`, `subcategory`, `what`, `type`, `tags`.
Every entry needs ≥1 link (`paper` / `repo` / `website`).

- `id`: lowercase `[a-z0-9-]+`, slug of the name (≤80 chars). Prefer the short artifact
  name when one exists (e.g. `swe-bench`). Must be globally unique across all files.
- `type`: paper, repo, tool, blog, paper+repo, dataset, leaderboard. Use `paper+repo`
  only when BOTH a paper and a repo link are present.
- `tags`: 3–5 lowercase hyphenated tags.
- `related`: `{harness, leaderboard, meta_analysis, variants}` — arrays of other ids.
- bookkeeping: `added_date`, `last_verified` (ISO date), `status` (active/deprecated/archived),
  `recommended` (bool — only for landmark resources).

Full JSON Schema: `data/schema.json`. Validate with `scripts/process/validate.py`.

---

## Fix ops format

`merge_duplicates.py` is driven by an ops JSON. Dry-run by default; `--apply` writes.

```json
{
  "merge":       {"<dup_id>": "<canonical_id>"},
  "rename_refs": {"<old_ref>": "<new_ref>"},
  "set_fields":  {"<id>": {"subcategory": "long-horizon"}}
}
```

- **merge**: deletes `dup_id`; the canonical inherits the union of `related` lists, any
  scalar fields it lacked, and the dup's `what` if the canonical's was a title-dump.
  Every reference to `dup_id` corpus-wide is redirected to `canonical_id`.
  Pick the canonical = cleanest id (no `-2` suffix) + best curation.
- **rename_refs**: redirect a reference id without deleting any entry (for a mistyped /
  aliased `related` target).
- **set_fields**: overwrite fields on an entry in place (e.g. taxonomy normalization,
  fixing a wrong `paper` link).

After every op it cleans all `related` lists (dedup, drop self-refs, drop dangling).

Worked example (real run, 2026-05): merge 10 duplicate pairs, fix a dangling alias,
normalize 7 drifted subcategories →

```json
{
  "merge": {
    "swe-effi-re-evaluating-...-resource-constraints": "swe-effi",
    "benchmarking-llms-for-fine-grained-code-review-...": "contextcrbench"
  },
  "rename_refs": { "projdevbench": "projdevbench-benchmarking-ai-coding-agents-on-end-to-end-project-development" },
  "set_fields": { "swe-ci": {"subcategory": "long-horizon"} }
}
```

Verify with `audit.py` before and after; expect `entries removed = len(merge)` and
zero new dangling-refs.

---

## Parallel curation / rewrite pattern

For LLM-heavy batch work (curating many candidates, rewriting many `what` fields), the
`Workflow` tool is awkward: its scripts have no filesystem access and large datasets
don't fit in `args`. Instead fan out **`Agent` subagents (model: sonnet)** that read
batch files directly:

1. Split the work list into N batch files (`/tmp/batch_<i>.json`), ~30–40 items each.
2. Launch N `Agent` calls in ONE message (parallel). Each agent:
   - reads its `/tmp/batch_<i>.json`,
   - applies the rule (curate with the relevance criteria + controlled vocab, OR rewrite
     `what` faithfully),
   - **writes** its result to `/tmp/out_<i>.json` (don't return large data in the reply),
   - replies with just a count.
3. Collect `/tmp/out_*.json`, verify full coverage, sanity-check (lengths, no title-dumps,
   no invented names), then apply to `data/*.json` with a small Python script.

Always re-run `validate.py` + `audit.py` afterward (Phase C). Keep relevance strict and
forbid agents from inventing benchmark names — verify any short name actually appears in
the paper's title/abstract.
