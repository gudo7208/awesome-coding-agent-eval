---
name: corpus-maintenance
description: Maintain the Awesome Coding Agent Eval data corpus — collect new arXiv papers not yet in the repo, audit and fix data-quality defects (dangling cross-references, duplicate entries, taxonomy drift, title-dump descriptions), and regenerate README/docs/llms.txt. Use for routine repo upkeep, e.g. when the user says "维护仓库 / 更新论文 / 补录论文 / 查数据漏洞 / 数据审计 / weekly update / daily maintenance / refresh the corpus".
---

# Corpus Maintenance

Routine upkeep for this repo's data corpus. Three independent phases —
**Collect**, **Audit & Fix**, **Regenerate** — run whichever the task needs.

## Ground rules

- **Source of truth is `data/*.json`** (benchmarks, methodology, toolchain, leaderboards, meta-analysis). `README.md`, `docs/*.md`, `llms.txt`, `llms-full.txt` are GENERATED — never hand-edit them; regenerate (Phase C).
- **Always finish with Phase C** (regenerate + validate + audit) after any data change.
- Use `.venv/bin/python` (never bare `python3`).
- The Bash sandbox blocks network. The arXiv fetch scripts need network → run them with `dangerouslyDisableSandbox: true` (or outside the sandbox).
- `candidates/` and `.checkpoint.json` are scratch — never commit them.

## Workflow checklist

Copy and track:

```
- [ ] A1. fetch recent arXiv candidates (network)
- [ ] A2. dedup candidates vs existing corpus (by arxiv id AND normalized name)
- [ ] A3. curate relevant ones into schema entries (strict relevance, good `what`)
- [ ] A4. append to the right data/*.json
- [ ] B1. run audit.py — triage findings
- [ ] B2. fix dangling-refs / duplicates / taxonomy via merge_duplicates.py
- [ ] B3. rewrite any title-dump `what` (what == name)
- [ ] C1. regenerate stats + docs + readme + llms.txt
- [ ] C2. validate.py and audit.py until clean
- [ ] C3. show results to the user before /ship
```

---

## Phase A — Collect new papers

```bash
# A1: fetch (network — disable sandbox). fetch_recent.py = cat:cs.SE/AI/CL/LG
# + relevance keywords + dedup vs existing arxiv ids. Output: candidates/arxiv_recent_<date>.jsonl
.venv/bin/python scripts/collect/fetch_recent.py
```

**A2 dedup**: load the candidate jsonl, drop any whose arxiv id (version-stripped) OR
normalized name already exists in `data/*.json`. The fetch already dedups by arxiv id;
the name check catches version/URL drift.

**A3 curate** — the relevance bar is strict: the paper must be about **evaluating AI
coding / software-engineering agents** (benchmark, methodology, toolchain, leaderboard,
or meta-analysis for such). Exclude general-agent (GUI/web/phone/memory/tool-use),
pure model releases, and non-code domains. See `reference.md` for the full criteria,
the controlled vocabulary, and the `what` format.

For a large candidate set, **fan out parallel `Agent` subagents (sonnet)**, each
curating a slice and writing a JSON file — Workflow can't read the filesystem and
large candidate sets don't fit in `args`. See `reference.md` → "Parallel curation pattern".

**A4 append**: build each entry with `id` = slug of name, `paper` = arxiv URL,
`added_date`/`last_verified` = today, `status` = "active". Append to the file matching
its `stage`. Re-check ids don't collide with existing ones.

---

## Phase B — Audit & fix defects

```bash
.venv/bin/python scripts/process/audit.py --json /tmp/audit.json
```

`audit.py` reports 12 defect classes. Triage:

| Finding | Action |
|---|---|
| `dangling-refs` | a `related` target id doesn't exist → fix the id (often a short alias of a real long id). Use `merge_duplicates.py` `rename_refs`. |
| `dup-url` / `dup-name` | same paper as two entries → merge. Pick the canonical (clean id + best `what`), redirect all inbound refs, delete the dup. Use `merge_duplicates.py` `merge`. |
| `taxonomy` | subcategory outside the controlled vocab for its stage → normalize to the nearest valid one. Use `merge_duplicates.py` `set_fields`. |
| `what-truncated` / `name-truncated` | cut mid-sentence → rewrite to a complete ≤80-char phrase. |
| `what-over-80` | exceeds the ≤80 convention → tighten. |
| `self-refs` / `eval-method` / `bad-url` | drop self-ref / use a valid eval_method / fix the URL. |

**Known-acceptable (do NOT "fix")**:
- `dup-url` among a project family that legitimately shares links (e.g. `swe-bench`,
  `swe-bench-verified`, `swe-bench-multimodal` share the repo; a benchmark and its
  leaderboard share a site).
- `type-link` (`paper+repo` with no paper link) — an enrichment gap, not a break.
  Leave it for a future paper-enrichment pass rather than downgrading the type.

The fix tool is data-driven (dry-run by default; `--apply` to write):

```bash
.venv/bin/python scripts/process/merge_duplicates.py --ops /tmp/ops.json          # dry-run
.venv/bin/python scripts/process/merge_duplicates.py --ops /tmp/ops.json --apply
```

`ops.json` schema and a worked example are in `reference.md` → "Fix ops format".

**B3 title-dump `what`** — entries where `what` == `name` are uninformative (the README
shows both, so they read as duplicated). Rewrite them into concise ≤80-char descriptions.
For a large batch, use the **parallel subagent pattern** (reference.md), instructing
agents to FAITHFULLY compress the title — never invent facts/numbers/benchmark names.

---

## Phase C — Regenerate & verify

```bash
.venv/bin/python scripts/generate/generate_stats.py
.venv/bin/python scripts/generate/generate_docs.py
.venv/bin/python scripts/generate/generate_readme.py
.venv/bin/python scripts/generate/generate_llms_txt.py
.venv/bin/python scripts/process/validate.py   # schema / ids / links — must pass
.venv/bin/python scripts/process/audit.py       # should show only known-acceptable findings
```

Loop B↔C until `validate.py` passes and `audit.py` shows only the known-acceptable
findings. Then show the user a summary (counts added/fixed, audit delta) and wait for
confirmation before `/ship` (per the repo's commit workflow).

---

See `reference.md` for: relevance criteria, controlled vocabulary, `what` format,
the fix-ops JSON format with an example, and the parallel-subagent curation pattern.
