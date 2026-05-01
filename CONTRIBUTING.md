# Contributing to AwesomeCodeBench

Thank you for helping grow this curated list of AI SE Agent evaluation resources.

## Inclusion Criteria

A resource is eligible if it meets **all** of the following:

- Directly related to evaluating AI Software Engineering (SE) Agents
- Has at least one accessible link (paper, repo, website, or leaderboard URL)
- Has a clearly defined evaluation target (e.g., code generation, bug fixing, PR review) or evaluation method

## Exclusion Criteria

Do not submit resources that are:

- Pure code models without an evaluation framework or benchmark
- General-purpose LLM benchmarks not specific to SE tasks (e.g., MMLU, HellaSwag)
- Product marketing pages or press releases without technical content
- Agent frameworks or scaffolding with no associated evaluation methodology or results

## How to Add a Resource

### Step 1 — Identify the stage

Determine which stage your resource belongs to:

| Stage | Description |
|---|---|
| `benchmark` | Datasets and task suites used to evaluate SE agents |
| `methodology` | Evaluation methods, metrics, and scoring approaches |
| `toolchain` | Infrastructure for running evaluations (sandboxes, harnesses, judges) |
| `leaderboard` | Live or published rankings of SE agent performance |
| `meta-analysis` | Surveys, studies, and analyses about SE agent evaluation |

### Step 2 — Add to the correct `data/*.json` file

Edit the JSON file corresponding to the stage (e.g., `data/benchmarks.json`).

### Step 3 — Fill in all required fields

```json
{
  "id": "unique-kebab-case-id",
  "name": "Resource Name",
  "stage": "benchmark",
  "subcategory": "code-generation",
  "what": "Evaluates agent ability to generate correct code from natural language specs",
  "type": "paper",
  "tags": ["code-generation", "python"],
  "url": "https://example.com/paper"
}
```

**Required fields:**

| Field | Constraint |
|---|---|
| `id` | Unique, kebab-case, no spaces |
| `name` | Human-readable resource name |
| `stage` | One of the five stages above |
| `subcategory` | Must be from the valid list below |
| `what` | ≤80 characters, English, format: `[Verb] [what] [for/on] [target]` |
| `type` | One of: `paper`, `repo`, `website`, `leaderboard`, `blog` |
| `tags` | Array of lowercase strings |

**`what` field format:**

> `[Verb] [what] [for/on] [target]`

Examples:
- `Evaluates agent ability to resolve GitHub issues end-to-end`
- `Measures code review quality on real-world pull requests`
- `Provides sandbox execution environment for SE agent benchmarks`

### Step 4 — Valid subcategory values

**benchmark:**
`code-generation`, `code-review`, `end-to-end`, `feature-development`, `large-codebase`, `long-horizon`, `multi-agent`, `production`, `security`, `testing`

**methodology:**
`execution-based`, `human-eval`, `hybrid`, `llm-judge`, `process-eval`

**toolchain:**
`harness`, `judge-tool`, `observability`, `sandbox`

**leaderboard:**
`activity`, `code-generation`, `se-agent`

**meta-analysis:**
`blog`, `limitation`, `quality-study`, `survey`

### Step 5 — Validate

```bash
python scripts/process/validate.py
```

All checks must pass before submitting.

### Step 6 — Regenerate docs

```bash
python scripts/generate/generate_readme.py
```

> **Do not manually edit `README.md` or any file under `docs/`.** These are auto-generated from the JSON data. Manual edits will be overwritten.

### Step 7 — Open a pull request

Use the PR template and confirm all checklist items before submitting.
