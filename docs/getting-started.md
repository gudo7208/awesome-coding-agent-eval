# Getting Started: Evaluate Your SE Agent in 5 Minutes

New to SE agent evaluation? This guide walks you from zero to a running evaluation.

---

## Step 1: Choose What to Evaluate

Before picking a benchmark, decide which capability you care about.

→ [① Evaluation Dimensions](1-dimensions.md) — full framework

Quick decision tree:

```
What does your agent do?
├── Fix bugs from GitHub issues?       → SWE-bench family
├── Review code / generate PR comments? → CR-Bench, Code Review Agent Benchmark
├── Write tests?                        → SWT-Bench, TestBench
├── End-to-end feature development?     → OmniCode, SWE-bench Pro
├── Work across multiple languages?     → Multi-SWE-bench
└── Long multi-step tasks?              → SWE-bench Pro, SWE-EVO
```

**Known gaps** (no good benchmark yet): requirements understanding, architecture decisions, multi-agent collaboration.

---

## Step 2: Pick a Benchmark

Top 5 recommended starting points:

| Benchmark | Why use it |
|---|---|
| [SWE-bench Verified](https://github.com/swe-bench/SWE-bench) | Gold standard — 500 human-validated Python issues, widely cited |
| [Multi-SWE-bench](https://github.com/multi-swe-bench/multi-swe-bench) | Same rigor as SWE-bench but covers Java, TypeScript, Go, Rust, C++ |
| [LiveCodeBench](https://livecodebench.github.io/leaderboard.html) | Contamination-free — continuously updated with fresh problems |
| [SWE-bench Pro](https://www.swebench.com) | Long-horizon tasks — harder, closer to real engineering work |
| [SWT-Bench](https://github.com/swe-bench/SWE-bench) | Testing focus — evaluates whether the agent writes good tests |

→ [② All 228 Benchmarks](2-benchmarks.md)

---

## Step 3: Set Up Your Toolchain

**Minimal setup** (get running in under an hour):

```bash
# 1. Clone SWE-bench
git clone https://github.com/swe-bench/SWE-bench
cd SWE-bench && pip install -e .

# 2. Run your agent against the benchmark
python run_evaluation.py \
  --predictions_path your_agent_predictions.jsonl \
  --swe_bench_tasks SWE-bench_Verified \
  --log_dir ./logs

# 3. Score
python get_results.py --predictions_path your_agent_predictions.jsonl
```

**Recommended for isolation**: [E2B](https://github.com/e2b-dev/E2B) — Firecracker microVM sandboxes, minimal setup, works with any agent.

**For production-scale runs**: [SWE-ReX](https://github.com/SWE-agent/SWE-ReX) supports local, Docker, and cloud execution from the same interface.

→ [④ Full Toolchain Guide](4-toolchain.md)

---

## Step 4: Choose a Scoring Method

| Method | When to use | Reliability |
|---|---|---|
| Execution-based | Default — run tests, check pass/fail | Highest |
| LLM-as-Judge | When execution isn't possible (e.g., code review quality) | Medium — watch for position bias |
| Process evaluation | When you want to understand HOW the agent works, not just outcomes | Emerging |
| Hybrid | Combine execution + LLM judge for richer signal | Best of both |

For most use cases, start with execution-based. It's the most reproducible and hardest to game.

→ [③ Methodology Deep Dive](3-methodology.md)

---

## Step 5: Run and Interpret Results

**Where to see leaderboards**:
- [SWE-bench Leaderboard](https://www.swebench.com) — SE agent resolve rates
- [LiveCodeBench Leaderboard](https://livecodebench.github.io/leaderboard.html) — contamination-free code generation
- [BigCodeBench Leaderboard](https://huggingface.co/spaces/bigcode/bigcodebench-leaderboard) — function-level generation

**Known pitfalls to watch for**:

- **Score inflation**: ~50% of SWE-bench passing PRs would not be merged in real projects ([METR study](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)). A high resolve rate does not mean production-ready code.
- **Test suite weakness**: SWE-bench tests are often too weak to catch subtle bugs. [UTBoost](https://arxiv.org/abs/2506.09289) found many "passing" patches are actually incorrect.
- **Data contamination**: Models trained on GitHub data may have seen benchmark issues. Use LiveCodeBench or SWE-MERA for contamination-resistant evaluation.
- **Oracle leakage**: Some benchmarks inadvertently leak information about the correct fix. Check [ORACLE-SWE](https://arxiv.org/abs/2604.07789) before trusting scores.
- **Single-language bias**: SWE-bench is Python-only. If your agent targets other languages, validate on Multi-SWE-bench.

→ [⑥ Meta-Analysis & Pitfalls](6-meta-analysis.md) — read this before publishing results

---

## What's Next?

- **Explore the full benchmark list** → [② Benchmarks & Datasets](2-benchmarks.md)
- **Set up weekly monitoring** — use [GitHub Actions](https://docs.github.com/en/actions) with `sb-cli` to run evaluations on each agent release
- **Read meta-analyses before publishing** → [⑥ Meta-Analysis](6-meta-analysis.md) — understand what your score actually means
- **Understand process, not just outcomes** → [③ Process Evaluation](3-methodology.md#process-eval) — trajectory-level analysis reveals failure modes that outcome metrics miss

---

[← Back to README](../README.md)
