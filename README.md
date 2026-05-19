<div align="center">
  <h1>Awesome Coding Agent Eval</h1>
  <p>A curated collection of 900+ resources for evaluating AI coding agents</p>

  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/resources-928-blue" alt="Resources">
  <img src="https://img.shields.io/badge/updated-weekly-green" alt="Updated weekly">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC--BY--4.0-lightgrey" alt="License"></a>
  <img src="https://img.shields.io/badge/links-checked-brightgreen" alt="Link Check">
</div>

## Why This List Exists

Most awesome lists end up bookmarked and forgotten. This one is different.

We built it as a **knowledge base for AI agents** — when your coding agent needs to research evaluation methods, pick a benchmark, or understand scoring trade-offs, it can query this repo's structured data directly ([llms-full.txt](llms-full.txt) for one-shot context, [AGENTS.md](AGENTS.md) for jq/Python recipes, or raw JSON in `data/`). Every entry is machine-readable first, human-readable second.

Of course, humans benefit too. The [Getting Started Guide](docs/getting-started.md) gets you oriented in 5 minutes, the Top 30 table below gives you the lay of the land, and the cross-references (`related` field) let you navigate from a benchmark to its harness, leaderboard, and known pitfalls in one click.

**Agent-first, human-friendly.**

> **Scope**: SE agent evaluation only — bug fixing, code review, testing, architecture, long-horizon development.
>
> **Not**: General LLM benchmarks, agent frameworks, or product reviews. See [Related Resources](#-related-resources) for those.

## Quick Start

| I want to... | Go to |
|---|---|
| Get started in 5 minutes | → [Getting Started Guide](docs/getting-started.md) |
| Understand what to evaluate | → [① Evaluation Dimensions](docs/1-dimensions.md) |
| Find the right benchmark (538) | → [② Benchmarks](#-top-30-benchmarks) |
| Understand scoring methods (143) | → [③ Methodology](#-evaluation-methodology) |
| Set up evaluation infrastructure (118) | → [④ Toolchain](#-evaluation-toolchain) |
| See agent rankings (23) | → [⑤ Leaderboards](#-leaderboards) |
| Learn about benchmark pitfalls (106) | → [⑥ Meta-Analysis](#-meta-analysis--pitfalls) |

## Table of Contents

- [Quick Start](#quick-start)
- [Top 30 Benchmarks](#-top-30-benchmarks)
- [② Benchmarks & Datasets](docs/2-benchmarks.md)
- [③ Evaluation Methodology](#-evaluation-methodology)
- [④ Evaluation Toolchain](#-evaluation-toolchain)
- [⑤ Leaderboards](#-leaderboards)
- [⑥ Meta-Analysis & Pitfalls](#-meta-analysis--pitfalls)
- [Related Resources](#-related-resources)
- [For AI Agents](#-for-ai-agents)
- [Contributing](#contributing)

## 🔥 Recently Added

- [AgencyBench](https://arxiv.org/abs/2601.11044) `ACL 2026` — Benchmark autonomous agents in 1M-token real-world contexts across 138 tasks
- [AutoExperiment: Evaluating Research Agents with Progressive Code Masking](https://arxiv.org/abs/2506.19724) `ICLR 2026` — Evaluate AI agents implementing ML experiments from papers via code masking
- [CR-Bench: Evaluating Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2603.11078) — Benchmark AI code review agents with fine-grained evaluation pipeline
- [ISO-Bench](https://arxiv.org/abs/2602.19594) — Benchmark coding agents on real-world LLM inference optimization tasks
- [MAPS: Multilingual Benchmark for Agent Performance and Security](https://arxiv.org/abs/2505.15935) — Evaluate agentic AI across 11 languages for performance and security
- [SWE Atlas: Measuring Coding Agents Across the Engineering Loop](https://scale.com/blog/swe-atlas-complete) — Benchmark suite for coding agents: QnA, test writing, and refactoring
- [SWE-PRBench: Benchmarking AI Code Review Quality Against PR Feedback](https://arxiv.org/abs/2603.26130) — Benchmark AI code review quality against 350 human-annotated pull requests
- [SWE-WebDevBench](https://arxiv.org/abs/2605.04637) — Evaluate vibe coding platforms as virtual software agencies across 68 metrics

---

## 📊 Top 30 Benchmarks

| Benchmark | What | Lang | Scale | Method | Year | ⭐ |
|---|---|---|---|---|---|---|
| [SWE-bench](https://github.com/swe-bench/SWE-bench) ✅ | 2294 real GitHub issues testing agent patch generation for Python bug fixes | python | 2294 | execution-based | 2023 | 4819 |
| [SWE-bench Multimodal](https://github.com/swe-bench/SWE-bench) ✅ | SWE-bench Multimodal | python | - | execution-based | 2023 | 4819 |
| [SWE-bench Verified](https://github.com/swe-bench/SWE-bench) ✅ | 500 human-verified subset of SWE-bench filtering ambiguous or erroneous issues | python | 500 | execution-based | 2023 | 4819 |
| [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) ✅ | LiveCodeBench | python, cpp, java | - | execution-based | 2024 | 854 |
| [bigcodebench](https://github.com/bigcode-project/bigcodebench) ✅ | Benchmarks LLMs on complex function calls, tool use, and instruction following | python | 1140 | execution-based | 2024 | 499 |
| [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) ✅ | terminal-bench-rl | python | - | execution-based | 2025 | 375 |
| [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) ✅ | Long-horizon SE task benchmark by Scale AI for multi-step complex engineering | python | - | execution-based | 2025 | 368 |
| [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) ✅ | multi-swe-bench | python | - | execution-based | 2025 | 333 |
| [joycode-agent](https://github.com/jd-opensource/joycode-agent) ✅ | Repository-level repair agent built and evaluated on SWE-Bench | python | 300 | execution-based | 2025 | 330 |
| [SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live) ✅ | SWE-bench-Live | python | - | execution-based | 2025 | 185 |
| [ai-coding-lang-bench](https://github.com/mame/ai-coding-lang-bench) ✅ | Benchmarks AI code generation across 13 programming languages | ruby | - | execution-based | 2026 | 151 |
| [devin-swebench-results](https://github.com/CognitionAI/devin-swebench-results) ✅ | Cognition's published Devin evaluation results and methodology on SWE-bench | python | 570 | execution-based | 2024 | 126 |
| [codefuse-evaluation](https://github.com/codefuse-ai/codefuse-evaluation) ✅ | codefuse-evaluation | python | - | execution-based | 2023 | 109 |
| [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) ✅ | Benchmarks LLMs on 1400+ real freelance software engineering tasks worth $1M+ | - | 1400 | execution-based | 2025 | 1441 |
| [skill](https://github.com/pinchbench/skill) ✅ | Benchmark by Kilo.ai for end-to-end evaluation of LLM coding agents on SE tasks | python | - | execution-based | 2026 | 1079 |
| [AICGSecEval](https://github.com/Tencent/AICGSecEval) ✅ | AICGSecEval | python | - | execution-based | 2025 | 965 |
| [appworld](https://github.com/StonyBrookNLP/appworld) ✅ | Evaluates agent tool-calling and planning across multi-app scenarios | python | - | execution-based | 2024 | 407 |
| [ML-Bench](https://github.com/gersteinlab/ML-Bench) ✅ | Evaluates LLM/agent ML task completion on 10K+ samples across 18 GitHub repos | python | 10000 | execution-based | 2023 | 316 |
| [HackSynth](https://github.com/aielte-research/HackSynth) ✅ | Evaluates LLM agents on autonomous penetration testing via CTF challenges | python | - | execution-based | 2024 | 303 |
| [sweet_rl](https://github.com/facebookresearch/sweet_rl) ✅ | Benchmarks multi-turn collaborative reasoning for LLM agent training | python | - | execution-based | 2025 | 266 |
| [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) ✅ | GitTaskBench | python | - | execution-based | 2025 | 252 |
| [MARBLE](https://github.com/ulab-uiuc/MARBLE) ✅ | MARBLE | python | - | execution-based | 2025 | 251 |
| [ai-agent-benchmark-compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) ✅ | Curated index of 50+ AI agent benchmarks across coding, tool-use, and reasoning | - | 50 | execution-based | 2025 | 134 |
| [SWT-Bench](https://github.com/logic-star-ai/SWT-Bench) ✅ | SWT-Bench | python | 1983 | execution-based | 2024 | 76 |
| [CodeScaleBench](https://sourcegraph.com/blog) ✅ | CodeScaleBench | python, go, typescript | - | execution-based | - | - |
| [OmniCode](https://arxiv.org/html/2602.02262v2) ✅ | OmniCode | python, javascript, java | - | execution-based | 2026 | - |
| [SWE-EVO](https://arxiv.org/html/2512.18470v2) ✅ | Benchmarks multi-step software evolution with 48 tasks across 7 OSS projects | python | 48 | execution-based | 2025 | - |
| [eval-dev-quality](https://github.com/symflower/eval-dev-quality) | Evaluates LLM code generation quality across multiple languages and tasks | go | - | execution-based | 2024 | 185 |
| [MMBench-GUI](https://github.com/open-compass/MMBench-GUI) | Hierarchical benchmark for GUI agents across desktop, mobile, and web platforms | python | - | execution-based | 2025 | 106 |
| [awesome-code-agents](https://github.com/EuniAI/awesome-code-agents) | Curated list of autonomous code agents, benchmarks, and research papers | python | - | execution-based | 2025 | 99 |

→ [See all 538 benchmarks](docs/2-benchmarks.md)

## 📖 Must-Read by Category

*If you read nothing else, start here — one recommended benchmark per task type.*

| Task | Benchmark | Why |
|---|---|---|
| Bug Fix & Issue Resolution | [SWE-bench](https://github.com/swe-bench/SWE-bench) | 2294 real GitHub issues testing agent patch generation for Python bug fixes |
| End-to-End / Multi-Task | [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) | Benchmarks LLMs on 1400+ real freelance software engineering tasks worth $1M+ |
| Security & Vulnerability | [AICGSecEval](https://github.com/Tencent/AICGSecEval) | AICGSecEval |
| Long-Horizon / Evolution | [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) | terminal-bench-rl |
| Testing & QA | [SWT-Bench](https://github.com/logic-star-ai/SWT-Bench) | SWT-Bench |

## 📐 Evaluation Methodology

<details>
<summary>③ Evaluation Methodology (143 resources)</summary>

### Agent Design

- 📝 [Rethinking SE Conventions for the Agentic Development Era](https://arxiv.org/abs/2604.07502) — Analyze how SE conventions should adapt for AI agent consumers.

### Benchmark Design

- 📝 [What Makes a Good Terminal-Agent Benchmark Task](https://arxiv.org/abs/2604.28093) — Guidelines for adversarial, difficult, and legible benchmark task design.

### Efficiency Analysis

- 📝 [Tokenomics: Quantifying Where Tokens Are Used in Agentic SE](https://arxiv.org/abs/2601.14470) — Analyze token consumption patterns across SDLC stages in multi-agent SE.

### Evaluation Framework

- 📝 [AEMA: Verifiable Evaluation Framework for Agentic LLM Systems](https://arxiv.org/abs/2601.11903) — Process-aware multi-agent evaluation framework for trustworthy LLM systems.
- 📝 [MASEval: Extending Multi-Agent Evaluation from Models to Systems](https://arxiv.org/abs/2603.08835) — Framework-agnostic evaluation treating entire multi-agent system as unit.

### Evaluation Theory

- 📝 [Agent Psychometrics: Task-Level Performance Prediction](https://arxiv.org/abs/2604.00594) — Predict task-level agent success using IRT with LLM-scaffold decomposition.

### Execution-based

- 📝 [A Systematic Approach for Assessing LLM Test Case Generation Capability](https://arxiv.org/html/2502.02866v1) — Systematic methodology for evaluating LLM-generated test cases.
- 📝 [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850v1) — Observability-driven automatic evolution of eval harnesses for coding agents.
- 📝 [Assessing Effectiveness of Test Suites: What Do We Know and What Should We Do?](https://www.semanticscholar.org/paper/e0fb57dcac9c62f87dec0331e655e2c6f3250b9b) — Assessing Effectiveness of Test Suites: What Do We Know and What Should We Do?.
- 📝 [Can Code Evaluation Metrics Detect Code Plagiarism?](https://arxiv.org/abs/2604.25778v1) — Can Code Evaluation Metrics Detect Code Plagiarism?.
- 📝 [COCO: Testing Code Generation Systems via Concretized Instructions](https://arxiv.org/abs/2308.13319) — Tests code generation via concretizing ambiguous natural-language instructions.
- 📝 [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification](https://arxiv.org/abs/2405.00253) — CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification.
- 📝 [CodeT: Code Generation with Generated Tests](https://arxiv.org/abs/2207.10397) — CodeT: Code Generation with Generated Tests.
- 📝 [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](https://openreview.net/forum?id=mrEK16Jy6h) — DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems.
- 📝 [Evaluating Large Language Models with Runtime Behavior of Program Execution](https://arxiv.org/abs/2403.16437) — Evaluates LLMs using runtime behavior and program execution traces.
- 📝 [Execution-Based Evaluation for Open-Domain Code Generation](https://arxiv.org/abs/2212.10481) — Execution-Based Evaluation for Open-Domain Code Generation.
- 📝 [How Many Code and Test Cases Are Enough? Evaluating Test Cases Generation from a Binary-Matrix Perspective](https://arxiv.org/abs/2510.08720) — Binary matrix framework evaluating LLM-generated test case quality and coverage.
- 📝 [How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks](https://arxiv.org/abs/2604.10508) — How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks.
- 📝 [InspectCoder: Dynamic Analysis-Driven Self Repair through Interactive LLM-Debugger Collaboration](https://www.semanticscholar.org/paper/5dc2d9d2be600942cb26293230899535ee35d70f) — Agentic self-repair via LLM-debugger dynamic analysis for code error diagnosis.
- 📝 [INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair](https://arxiv.org/abs/2311.09868) — INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair.
- 📝 [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://arxiv.org/abs/2310.02003) — L2MAC: Large Language Model Automatic Computer for Extensive Code Generation.
- 📝 [Measuring the performance of our models on real-world tasks (GDPval)](https://openai.com/index/gdpval/) — GDPval: framework evaluating model performance on real-world GDP-sector tasks.
- 📝 [Mutation-Guided Unit Test Generation with a Large Language Model](https://arxiv.org/html/2506.02954v6) — Uses mutation score instead of coverage to evaluate LLM-generated unit tests.
- 📝 [On the Reliability and Explainability of Language Models for Program Generation](https://arxiv.org/abs/2302.09587) — On the Reliability and Explainability of Language Models for Program Generation.
- 📝 [Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation](https://arxiv.org/abs/2412.14308) — RL from static quality metrics to generate high-quality, smell-free unit tests.
- 📝 [SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?](https://arxiv.org/abs/2604.25737v1) — SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?.
- 📝 [StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback](https://arxiv.org/abs/2402.01391) — StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback.
- 📝 [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449) — SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution.
- 📝 🐍 [SWE-ZERO to SWE-HERO](https://arxiv.org/abs/2604.01496) — Two-stage SFT recipe from execution-free to execution-based agent training.
- 📝 🐍 [Terminus-4B](https://arxiv.org/abs/2604.29102) — Small 4B model replacing frontier LLMs for agentic execution subtasks.

> See also: [LLM-as-Judge](#llm-judge), [Evaluation Harness](#harness)

### Human Evaluation

- 🔧 [vibe_hacking](https://github.com/tldrsec/vibe_hacking) — Secure code review evaluation of LLMs and vibe coding IDEs.
- 📝 [A Study on Developer Behaviors for Validating and Repairing LLM-Generated Code Using Eye Tracking and IDE Actions](https://arxiv.org/abs/2405.16081) — Eye tracking lab study on how developers validate and repair LLM-generated code.
- 📝 [Bridging HCI and AI Research for the Evaluation of Conversational SE Assistants](https://arxiv.org/abs/2502.07956) — HCI+AI framework for human-centered evaluation of conversational SE assistants.
- 📝 [ChatGPT in Action: Analyzing Its Use in Software Development](https://www.semanticscholar.org/paper/6f8f35aea416b2542d55a638ad20497f38181384) — Quantitative analysis of ChatGPT use in SE tasks using DevGPT dataset.
- 📝 [Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?](https://doi.org/10.1109/ICSE55347.2025.00060) — Study on DL-based automated code review quality vs human reviewers.
- 📝 [From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs](https://arxiv.org/abs/2604.14137) — From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs.
- 📝 [How can we assess human-agent interactions? Case studies in software agent design](https://arxiv.org/abs/2510.09801) — How can we assess human-agent interactions? Case studies in software agent design.
- 📝 [The RealHumanEval: Evaluating Large Language Models' Abilities to Support Programmers](https://arxiv.org/abs/2404.02806) — The RealHumanEval: Evaluating Large Language Models' Abilities to Support Programmers.
- 📝 [What makes a code review useful to OpenDev developers? An empirical investigation](https://arxiv.org/abs/2302.11686) — Empirical study of what makes code review comments useful to OSS developers.

### Hybrid

- 📝 [A methodical approach to agent evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation) — A methodical approach to agent evaluation.
- 📝 [Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap](https://arxiv.org/abs/2604.15075) — Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap.
- 📝 [Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and Evaluation](https://arxiv.org/abs/2510.24358) — Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and Evaluation.
- 📝 [Deep Assessment of Code Review Generation Approaches: Beyond Lexical Similarity](https://arxiv.org/abs/2501.05176) — Critiques lexical metrics like BLEU for code review and proposes better methods.
- 📝 [Evaluating AI Agents: A Practical Guide with Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-a-practical-guide-with-microsoft-foundry/4500224) — Evaluating AI Agents: A Practical Guide with Microsoft Foundry.
- 📝 [Evaluating AI Agents: More than just LLMs](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-more-than-just-llms/4460575) — Evaluating AI Agents: More than just LLMs.
- 📝 [Evaluation of LLM-Based Software Engineering Tools: Practices, Challenges, and Future Directions](https://arxiv.org/abs/2604.24621) — Systematic review of evaluation practices and challenges for LLM-based SE tools.
- 📝 [Multi-Agent Code Verification via Information Theory](https://arxiv.org/html/2511.16708) — Multi-Agent Code Verification via Information Theory.
- 📝 [Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning](https://arxiv.org/abs/2502.13820) — Evaluates synthetic verifiers on code and reasoning using scoring benchmarks.
- 📝 [Static Code Analysis in the AI Era: An In-depth Exploration of the Concept, Function, and Potential of Intelligent Code Analysis Agents](https://arxiv.org/abs/2310.08837) — ICAA combining AI models with static analysis tools for intelligent code review.

### LLM-as-Judge

- 📝 🐍 [Agent-Eval-Refine](https://github.com/Berkeley-NLP/Agent-Eval-Refine) — Uses LLM to evaluate agent trajectories and generate refinement feedback.
- 🔧 🔷 [AutoReviewer](https://github.com/gvasilei/AutoReviewer) — LLM-based automatic code review tool using language models.
- 📝 [code-agent-eval](https://github.com/amazon-science/code-agent-eval) — Evaluates agent-generated code patches using LLM critics without execution.
- 📝 [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — Surveys LLM-as-a-Judge scoring modes, biases, consistency, and applications.
- 📝 [Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934) — Uses agent judges for process-level evaluation of agentic system outputs.
- 📝 [AI-powered Code Review with LLMs: Early Results](https://arxiv.org/abs/2404.18496) — LLM-based AI agent for automated code review, detecting bugs and code smells.
- 📝 [An LLM-as-Judge Metric for Bridging the Gap with Human Evaluation in SE Tasks](https://arxiv.org/abs/2505.20854) — LLM-as-Judge metric bridging gap with human evaluation for SE tasks.
- 📝 [Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions](https://aclanthology.org/2025.acl-long.223/) — Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions.
- 📝 [AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration](https://arxiv.org/abs/2512.20159) — AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration.
- 📝 [Can GPT-4 Replicate Empirical Software Engineering Research?](https://arxiv.org/abs/2310.01727) — Evaluates GPT-4's ability to replicate empirical SE research studies.
- 📝 [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering](https://arxiv.org/abs/2502.06193) — Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering.
- 📝 [CODE-DITING: A Reasoning-Based Metric for Functional Alignment in Code Evaluation](https://arxiv.org/abs/2505.19502) — CODE-DITING: A Reasoning-Based Metric for Functional Alignment in Code Evaluation.
- 📝 [CodeJudge-Eval: Can Large Language Models be Good Judges in Code Understanding?](https://arxiv.org/abs/2408.10718) — Benchmark evaluating LLMs as judges of code correctness for code understanding.
- 📝 [CodeJudgeBench](https://arxiv.org/abs/2507.10535) — Benchmarks LLM-as-Judge reliability on code tasks, revealing bias and limits.
- 📝 [CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences](https://arxiv.org/abs/2403.09032) — LLM-as-a-Judge dataset for aligning code LLMs with user preferences.
- 📝 [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](https://arxiv.org/abs/2409.19715) — Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code.
- 📝 [Comparing Developer and LLM Biases in Code Evaluation](https://arxiv.org/abs/2603.24586) — Compares developer and LLM biases in code evaluation using TRACE framework.
- 📝 [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891) — Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers.
- 📝 [Correlating Automated and Human Evaluation of Code Documentation Generation Quality](https://www.semanticscholar.org/paper/3f673691509b430a3c57040928008b9949508987) — Correlates automated metrics vs human eval for code documentation generation.
- 📝 [CritiqueLLM: Towards an Informative Critique Generation Model for Evaluation of Large Language Model Generation](https://arxiv.org/abs/2311.18702) — CritiqueLLM: Towards an Informative Critique Generation Model for Evaluation of Large Language Model Generation.
- 📝 [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://arxiv.org/abs/2409.19801) — Reference-free metric scoring code review comments via code claims and smells.
- 📝 [DeepCRCEval: Revisiting the Evaluation of Code Review Comment Generation](https://arxiv.org/abs/2412.18291) — Proposes semantic-based framework for evaluating code review comment generation.
- 📝 [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://arxiv.org/abs/2504.15253) — Benchmarks LLM-as-Judge reliability for evaluating test-time compute scaling.
- 📝 [Foundational Automatic Evaluators: Scaling Multi-Task Generative Evaluator Training for Reasoning-Centric Domains](https://arxiv.org/abs/2510.17793) — Foundational Automatic Evaluators: Scaling Multi-Task Generative Evaluator Training for Reasoning-Centric Domains.
- 📝 [From Code to Courtroom: LLMs as the New Software Judges](https://arxiv.org/abs/2503.02246) — Survey of LLM-as-a-Judge paradigm for evaluating SE tasks like code generation.
- 📝 [How Trustworthy Are LLM-as-Judge Ratings for Interpretive Responses? Implications for Qualitative Research Workflows](https://arxiv.org/abs/2604.00008) — How Trustworthy Are LLM-as-Judge Ratings for Interpretive Responses? Implications for Qualitative Research Workflows.
- 📝 [Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning](https://arxiv.org/abs/2510.23038) — Trains LLM judges via tool-integrated reinforcement learning with code executor.
- 📝 [Issue-Oriented Agent-Based Framework for Automated Review Comment Generation](https://arxiv.org/abs/2511.00517) — Multi-agent framework for automated code review comment generation.
- 📝 [JudgeBench: A Benchmark for Evaluating LLM-based Judges](https://arxiv.org/abs/2410.12784) — Benchmark for evaluating reliability of LLM-based judges on challenging tasks.
- 📝 [JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://arxiv.org/abs/2310.17631) — Fine-tunes LLMs as scalable judges for evaluating open-ended LLM outputs.
- 📝 [Judging LLM-as-a-judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — Judging LLM-as-a-judge with MT-Bench and Chatbot Arena.
- 📝 [Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge](https://arxiv.org/abs/2406.07791) — Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge.
- 📝 [Leveraging Large Language Model for Automatic Patch Correctness Assessment](https://www.semanticscholar.org/paper/3c00979b598d834b92dbd0fd8e4399d594802de3) — Uses LLMs to assess correctness of auto-generated patches against overfitting.
- 📝 [LLM as a Judge](https://www.semanticscholar.org/paper/1c629669812cf4cdc354de1f6d36084a4b2adc8c) — LLM as a Judge.
- 📝 [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) — Trains LLM critic models to generate NL feedback helping catch bugs in LLM code.
- 📝 [LLM-as-a-Judge for Scalable Test Coverage Evaluation](https://arxiv.org/html/2512.01232) — LLM-as-a-Judge for Scalable Test Coverage Evaluation.
- 📝 [LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road Ahead](https://arxiv.org/abs/2510.24367) — Literature review of LLM-as-a-Judge paradigm for evaluating SE artifacts.
- 📝 [LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Roadmap](https://www.semanticscholar.org/paper/04745b236cf9ebdb06f33d14afa5e7541775af6c) — Survey on LLM-as-a-Judge in SE: potential, limitations, and future directions.
- 📝 [LLM-as-Judge for Co-Creation](https://arxiv.org/abs/2604.29600) — Reliability-aware evaluation framework for human-AI coding collaboration.
- 📝 [Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learning](https://www.semanticscholar.org/paper/d3c5ff93edbc9b37bcd3657acbebe276c650b18a) — RL-based training method to make LLM judge biases non-predictive for robustness.
- 📝 [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://arxiv.org/abs/2306.05087) — Trains dedicated judge model to auto-evaluate instruction-tuned LLM outputs.
- 📝 [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) — Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models.
- 📝 [Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery](https://arxiv.org/abs/2604.19049v1) — Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery.
- 📝 [ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding](https://arxiv.org/abs/2510.11498) — ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding.
- 📝 [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) — RM-R1: Reward Modeling as Reasoning.
- 📝 [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) — Iteratively improves LLM-as-Judge evaluators using only synthetic data.
- 📝 🐍 [Themis](https://arxiv.org/abs/2604.29500) — Robust multilingual code reward models for multi-criteria scoring.
- 📝 [Vibe Checker: Aligning Code Evaluation with Human Preference](https://arxiv.org/abs/2510.07315) — Vibe Checker: Aligning Code Evaluation with Human Preference.

> See also: [Process Evaluation](#process-eval), [Execution-based](#execution-based)

### Process Evaluation

- 📝 [A Benchmark Mutation Approach for Realistic Agent Evaluation](https://arxiv.org/abs/2510.08996) — Benchmark mutation approach generating realistic SE agent evaluation tasks.
- 📝 [A Computational Theory for Efficient Mini Agent Evaluation with Causal Guarantees](https://openreview.net/forum?id=dsjxCoa0CO) — Computational theory for efficient mini agent evaluation with causal guarantees.
- 📝 [A Framework for Continuous Evaluation of LLM Test Generation in Industry](https://arxiv.org/html/2504.18985v1) — Framework for continuous evaluation of LLM test generation in industry settings.
- 📝 [A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems](https://arxiv.org/html/2511.14136v1) — A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems.
- 📝 [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://arxiv.org/abs/2604.19572) — A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression.
- 📝 [ACON](https://arxiv.org/abs/2510.00615) — Compresses observations and interaction histories to reduce agent memory usage.
- 📝 [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation](https://arxiv.org/abs/2604.23581) — DAG-based step-level evaluation tracking error propagation in agentic workflows.
- 📝 [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/abs/2604.23581v1) — AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking.
- 📝 [Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity](https://arxiv.org/abs/2604.17609v1) — Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity.
- 📝 [AI agent evaluation: A practical framework for testing multi-step agents](https://www.braintrust.dev/articles/ai-agent-evaluation-framework) — AI agent evaluation: A practical framework for testing multi-step agents.
- 📝 [AlphaEval: Evaluating Agents in Production](https://arxiv.org/abs/2604.12162) — Framework for evaluating AI agents in production with implicit constraints.
- 📝 [Automatic Failure Attribution and Critical Step Prediction Method for Multi-Agent Systems Based on Causal Inference](https://arxiv.org/abs/2509.08682) — Attributes failures and predicts critical steps in multi-agent systems.
- 📝 [Beyond Accuracy: Evaluating Source Code Capabilities in Large Language Models for Software Engineering](https://www.semanticscholar.org/paper/208217bedf590ae49bcc0cb6f779271e644b8a01) — Beyond Accuracy: Evaluating Source Code Capabilities in Large Language Models for Software Engineering.
- 📝 [CodeCircuit: Toward Inferring LLM-Generated Code Correctness via Attribution Graphs](https://arxiv.org/abs/2602.07080) — Infers LLM-generated code correctness via attribution graphs without execution.
- 📝 [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/abs/2604.14877) — Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis.
- 📝 [Don't Let AI Agents YOLO Your Files: Shifting Information and Control to Filesystems for Agent Safety and Autonomy](https://arxiv.org/abs/2604.13536) — Don't Let AI Agents YOLO Your Files: Shifting Information and Control to Filesystems for Agent Safety and Autonomy.
- 📝 [Effective Strategies for Asynchronous Software Engineering Agents](https://arxiv.org/html/2603.21489v1) — Evaluates coordination strategies for asynchronous multi-agent SE workflows.
- 📝 [Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents](https://arxiv.org/abs/2604.26274) — Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents.
- 📝 [Evaluating Plan Compliance in Autonomous Programming Agents](https://arxiv.org/abs/2604.12147v2) — Evaluating Plan Compliance in Autonomous Programming Agents.
- 📝 [Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618) — Evaluating whether AI models would sabotage AI safety research.
- 📝 [Exploration and Exploitation Errors Are Measurable for Language Model Agents](https://arxiv.org/abs/2604.13151) — Exploration and Exploitation Errors Are Measurable for Language Model Agents.
- 📝 [Failure-Centered Runtime Evaluation for Deployed Trilingual Public-Space Agents](https://arxiv.org/abs/2604.23990) — Failure-centered runtime evaluation framework for deployed trilingual SE agents.
- 📝 [From Correctness to Collaboration: A Human-Centered Taxonomy of AI Agent Behaviors in Software Engineering](https://www.semanticscholar.org/paper/85198c5c58ceb3c8681ce3fbd19f52b9533164ec) — Taxonomy of AI agent behaviors from 91 developer rules beyond correctness.
- 📝 [From Reproduction to Replication: Evaluating Research Agents with Progressive Code Masking](https://arxiv.org/abs/2506.19724) — From Reproduction to Replication: Evaluating Research Agents with Progressive Code Masking.
- 📝 [Hodoscope: Unsupervised Monitoring for AI Misbehaviors](https://arxiv.org/abs/2604.11072) — Unsupervised monitoring framework for detecting unknown AI agent misbehaviors.
- 📝 [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/abs/2604.18874) — Formalizes adversarial tool environments as evaluation gap for agentic AI.
- 📝 [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750v1) — Analyzes and predicts token consumption patterns in agentic coding tasks.
- 📝 [How to Evaluate Coding Agents in Production](https://labs.adaline.ai/p/evaluate-coding-agents-production) — How to Evaluate Coding Agents in Production.
- 📝 [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787) — Scales inference compute via repeated sampling with coverage as power law.
- 📝 [Measuring the Unmeasurable: Markov Chain Reliability for LLM Agents](https://arxiv.org/abs/2604.24579) — Models agent traces as Markov chains for pass@k uncertainty quantification.
- 📝 [Plausible but Wrong: A case study on Agentic Failures in Astrophysical Workflows](https://arxiv.org/abs/2604.25345) — Case study on agentic AI failures in scientific workflows across 18 tasks.
- 📝 [Playing Psychic: Using Thought Trees to Predict Reasoning Models Accuracy on Coding Tasks](https://arxiv.org/abs/2604.16931) — Predicts reasoning model accuracy on coding tasks via thought tree structure.
- 📝 [Process-Level Trajectory Eval](https://arxiv.org/html/2510.25694v1) — Scores each agent step in trajectories rather than just final outcomes.
- 📝 [Process-Oriented Error Analysis](https://arxiv.org/abs/2503.12374) — Classifies and attributes process errors in software engineering agents.
- 📝 [Reasoning Through Execution (ORPS)](https://arxiv.org/abs/2412.15118) — Combines process and outcome supervision via execution for code gen.
- 📝 🐍 [RSCB-MC](https://arxiv.org/abs/2604.27283) — Risk-sensitive contextual bandits for agent memory retrieval decisions.
- 📝 [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529) — Test-time scaling framework via compact trajectory representations.
- 📝 [Self-Abstraction from Grounded Experience for Plan-Guided Policy Refinement](https://arxiv.org/abs/2511.05931) — Self-Abstraction from Grounded Experience for Plan-Guided Policy Refinement.
- 📝 [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9) — Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping.
- 📝 [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints](https://arxiv.org/abs/2509.09853) — SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints.
- 📝 [SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling](https://arxiv.org/abs/2604.14820) — SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling.
- 📝 [TDD Governance for Multi-Agent Code Generation via Prompt Engineering](https://arxiv.org/abs/2604.26615v1) — TDD governance framework for multi-agent code generation via prompt engineering.
- 📝 [Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework](https://arxiv.org/abs/2510.05365) — Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework.
- 📝 [The Complexity Trap](https://arxiv.org/abs/2508.21433) — Observation masking matches LLM summarization performance at half the cost.
- 📝 [The Kitchen Loop: User-Spec-Driven Development for a Self-Evolving Codebase](https://arxiv.org/abs/2603.25697) — The Kitchen Loop: User-Spec-Driven Development for a Self-Evolving Codebase.
- 📝 [Turning the Tide: Repository-based Code Reflection](https://arxiv.org/abs/2507.09866) — Proposes repository-based code reflection to improve SE agent reasoning.

> See also: [LLM-as-Judge](#llm-judge), [Hybrid](#hybrid)

</details>

## 🔧 Evaluation Toolchain

<details>
<summary>④ Evaluation Toolchain (118 resources)</summary>

### Benchmark Construction

- 📝 [REAP: Automatic Curation of Coding Agent Benchmarks from Production](https://arxiv.org/abs/2604.01527) — Automatically build coding agent benchmarks from production developer sessions.

### Efficiency

- 📝 [AgentDiet: Reducing Cost of LLM Agents with Trajectory Reduction](https://arxiv.org/abs/2509.23586) — Reduce agent trajectory tokens 40-60% by removing useless/redundant info.
- 📝 [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency](https://arxiv.org/abs/2603.29919) — Compress agent skill descriptions 48% and bodies 39% while improving quality.

### Evaluation Framework

- 📝 [MAESTRO: Multi-Agent Evaluation Suite for Testing, Reliability, and Observability](https://arxiv.org/abs/2601.00481) — Evaluation suite for multi-agent system testing and observability.

### Evaluation Harness

- 🔧 [OpenHands Eval Harness](https://github.com/All-Hands-AI/OpenHands) — Built-in eval framework for OpenHands supporting SWE-bench and more, 30x faster.
- 🔧 [OpenAI Evals](https://github.com/openai/evals) — OpenAI Evals.
- 🔧 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — General-purpose LLM evaluation framework supporting hundreds of benchmarks.
- 🔧 🐍 [harbor](https://github.com/harbor-framework/harbor) — Runs AI agent evals and RL environments with terminal-based benchmarking.
- 🔧 🐍 [intellagent](https://github.com/plurai-ai/intellagent) — intellagent.
- 🔧 🐍 [any-agent](https://github.com/mozilla-ai/any-agent) — Unified interface to build agents across frameworks with tracing and scoring.
- 🔧 [bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness) — Evaluates code generation models on HumanEval, MBPP, and other benchmarks.
- 🔧 [augment-swebench-agent](https://github.com/augmentcode/augment-swebench-agent) — Runs SWE-bench Verified evaluations with full pipeline for agent benchmarking.
- 🔧 🐍 [token-savior](https://github.com/Mibayy/token-savior) — token-savior.
- 🔧 🐍 [Test-Agent](https://github.com/codefuse-ai/Test-Agent) — LLM-powered software testing agent for industrial use cases.
- 🔧 [claw-eval](https://github.com/claw-eval/claw-eval) — claw-eval.
- 🔧 🐍 [upskill](https://github.com/huggingface/upskill) — Generates and evaluates coding skills of agents like Claude Code and Codex.
- 🔧 [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation) — awslabs/agent-evaluation.
- 🔧 🐍 [bananalyzer](https://github.com/reworkd/bananalyzer) — Evaluates web agents on standardized scraping and navigation test scenarios.
- 🔧 [SWE-bench Experiments](https://github.com/SWE-bench/experiments) — SWE-bench Experiments.
- 🔧 🔷 [ts-bench](https://github.com/laiso/ts-bench) — CLI benchmark tool for evaluating AI coding agents on TypeScript workloads.
- 🔧 🐹 [SanityHarness](https://github.com/lemon07r/SanityHarness) — SanityHarness.
- 🔧 🐍 [aira-dojo](https://github.com/facebookresearch/aira-dojo) — AI research agent development and evaluation framework by Facebook Research.
- 🔧 🐍 [collaborative-gym](https://github.com/SALT-NLP/collaborative-gym) — Framework for building and evaluating human-AI collaborative agents.
- 🔧 🐍 [evals](https://github.com/strands-agents/evals) — Evaluation framework for AI agents and LLM apps with automated agentic testing.
- 🔧 🟣 [AgentEval](https://github.com/AgentEvalHQ/AgentEval) — AgentEval.
- 🔧 🐍 [aider-swe-bench](https://github.com/Aider-AI/aider-swe-bench) — Harness for running and evaluating Aider on SWE-Bench benchmark.
- 🔧 🐍 [agent-quality-inspect](https://github.com/SAP/agent-quality-inspect) — agent-quality-inspect.
- 🔧 🐍 [CATArena](https://github.com/AGI-Eval-Official/CATArena) — Tournament platform for code agents via iterative competitive peer learning.
- 🔧 🐍 [sb-cli](https://github.com/SWE-bench/sb-cli) — Official SWE-bench CLI tool for running remote evaluation tasks.
- 🔧 [refact-bench](https://github.com/smallcloudai/refact-bench) — Benchmark harness evaluating AI coding assistants on SWE-Bench tasks via Docker.
- 🔧 🐍 [OD-SWE-bench](https://github.com/OpenDevin/OD-SWE-bench) — Enhanced SWE-bench fork with evaluation harness for OpenDevin agents.
- 🔧 ☕ [agent-bench](https://github.com/spring-ai-community/agent-bench) — Benchmarks Java AI agents in isolated sandboxes with Spring AI integration.
- 🔧 🐍 [evalmonkey](https://github.com/Corbell-AI/evalmonkey) — CLI eval harness for AI coding agents with benchmark and chaos fault injection.
- 🔧 🐍 [pr-arena](https://github.com/neulab/pr-arena) — Platform for pairwise PR generation and human comparison to rank coding agents.
- 🔧 🐍 [codex-long-running-harness](https://github.com/LongWeihan/codex-long-running-harness) — codex-long-running-harness.
- 🔧 🐍 [squeez](https://github.com/KRLabsOrg/squeez) — Compresses verbose tool outputs for coding agents via LoRA fine-tuning.
- 📝 [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071) — Architectural Design Decisions in AI Agent Harnesses.
- 📝 [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) — AWS blog on evaluating AI agents using Amazon Bedrock AgentCore Evaluations.
- 📝 [How to Build a Coding Agent Benchmark with Claude's Agent SDK](https://lirantal.com/blog/how-to-build-a-coding-agent-benchmark-with-claudes-agent-sdk) — Tutorial on building a coding agent benchmark harness with Claude Agent SDK.
- 📝 [OpenDevin: An Open Platform for AI Software Developers as Generalist Agents](https://www.semanticscholar.org/paper/be27ef5a9068d9e2be1ab97b7c3de7168c472972) — Open platform for building and evaluating AI software engineering agents.
- 📝 [smolagents](https://github.com/huggingface/smolagents) — Hugging Face lightweight framework for building and running LLM-powered agents.
- 📝 [SWE Agent](https://github.com/princeton-nlp/swe-agent) — SWE Agent.
- 📝 [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — Agent-computer interface framework for LM agents to resolve GitHub issues.
- 📝 [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](https://arxiv.org/abs/2412.10133) — LLM agent that auto-configures and executes test suites for arbitrary projects.

> See also: [Sandbox & Execution](#sandbox), [Execution-based](#execution-based)

### LLM Judge Tools

- 🔧 [Promptfoo](https://github.com/promptfoo/promptfoo) — Tests and evaluates LLM outputs with prompt comparison and auto-scoring.
- 🔧 🔷 [sage](https://github.com/usetig/sage) — LLM council that reviews and evaluates coding agent actions in real-time.
- 🔧 🐹 [diffdeck](https://github.com/KnockOutEZ/diffdeck) — diffdeck.
- 🔧 🦀 [augre](https://github.com/twitchax/augre) — LLM-powered local diff code review tool using CodeLlama or OpenAI.
- 🔧 🐍 [CodeFox-CLI](https://github.com/codefox-lab/CodeFox-CLI) — CLI tool for AI-powered code review of git diffs using local or cloud LLMs.
- 📝 [aiXamine: Simplified LLM Safety and Security](https://arxiv.org/abs/2504.14985) — Black-box LLM safety/security eval platform with 40+ tests across 8 dimensions.
- 📝 [Evaluate your AI agents with Vertex Gen AI evaluation service](https://cloud.google.com/blog/products/ai-machine-learning/introducing-agent-evaluation-in-vertex-ai-gen-ai-evaluation-service) — Google Vertex AI agent evaluation service with trajectory analysis.

### Observability

- 🔧 [Langfuse](https://github.com/langfuse/langfuse) — Open-source LLM observability platform with tracing, spans, and scoring.
- 🔧 🐍 [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) — Python SDK for AI agent observability, tracing, monitoring and evaluation.
- 🔧 🐍 [Observal](https://github.com/BlazeUp-AI/Observal) — Observal.
- 🔧 🐍 [agentevals](https://github.com/agentevals-dev/agentevals) — Evaluates AI agents via OpenTelemetry traces in a framework-agnostic way.
- 🔧 🐹 [agenttrace](https://github.com/luoyuctl/agenttrace) — Replays and audits coding-agent JSONL sessions locally.
- 🔧 [swe_bench_traces](https://github.com/codestoryai/swe_bench_traces) — Archives AI patch generation and evaluation traces on SWE-bench Lite.
- 🔧 [Braintrust](https://braintrust.dev) — Braintrust.
- 📝 [CodeTracer: Towards Traceable Agent States](https://arxiv.org/abs/2604.11641) — CodeTracer: Towards Traceable Agent States.
- 📝 [RepoAgent](https://github.com/OpenBMB/RepoAgent) — LLM-powered framework for automated repository documentation generation.
- 📝 [Systematic debugging for AI agents: Introducing the AgentRx framework](https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/) — AgentRx framework for systematic debugging of AI agent failure trajectories.

### Sandbox & Execution

- 🔧 [cua](https://github.com/trycua/cua) — Sandbox infra for computer-use agents with macOS/Linux/Windows VMs and SDK.
- 🔧 [E2B](https://github.com/e2b-dev/E2B) — Sandbox for secure AI agent code execution with Firecracker microVMs.
- 🔧 🐍 [OpenSandbox](https://github.com/alibaba/OpenSandbox) — OpenSandbox.
- 🔧 🦀 [microsandbox](https://github.com/superradcompany/microsandbox) — microsandbox.
- 🔧 🦀 [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) — Sandbox for secure AI agent code execution with instant concurrent containers.
- 🔧 🐍 [sandbox](https://github.com/agent-infra/sandbox) — sandbox.
- 🔧 [judge0](https://github.com/judge0/judge0) — Open-source sandboxed code execution system supporting 60+ languages.
- 🔧 🦀 [zeroboot](https://github.com/zerobootdev/zeroboot) — zeroboot.
- 🔧 🦀 [nono](https://github.com/always-further/nono) — Zero-config AI agent sandbox with capability-model-based multiplexed isolation.
- 🔧 🐹 [agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) — Kubernetes-based sandbox runtime for isolated stateful AI agent workloads.
- 🔧 🦀 [boxlite](https://github.com/boxlite-ai/boxlite) — Embeddable sandbox for AI agents with snapshots, state and hardware isolation.
- 🔧 🔷 [vibekit](https://github.com/superagent-ai/vibekit) — vibekit.
- 🔧 [agent-safehouse](https://github.com/eugene1g/agent-safehouse) — Sandbox for local AI agents with scoped read/write filesystem access.
- 🔧 🔷 [sandbox-agent](https://github.com/rivet-dev/sandbox-agent) — Run coding agents in sandboxed environments with HTTP control for evaluation.
- 🔧 🐍 [wuying-agentbay-sdk](https://github.com/agentbay-ai/wuying-agentbay-sdk) — Cloud sandbox environment SDK built for AI agents.
- 🔧 🔷 [gondolin](https://github.com/earendil-works/gondolin) — Experimental agent sandbox using Linux microVMs with TypeScript control plane.
- 🔧 🔷 [sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) — SDK for running sandboxed code environments on Cloudflare's edge network.
- 🔧 🦀 [vibe](https://github.com/lynaghk/vibe) — vibe.
- 🔧 🟨 [secure-exec](https://github.com/rivet-dev/secure-exec) — secure-exec.
- 🔧 🐍 [coderunner](https://github.com/instavm/coderunner) — Local isolated sandbox for AI agents to run code safely in containers.
- 🔧 🐹 [arrakis](https://github.com/abshkbh/arrakis) — arrakis.
- 🔧 🐹 [artifact-fs](https://github.com/cloudflare/artifact-fs) — FUSE filesystem driver for lazy-mounting large git repos in agent sandboxes.
- 🔧 🐍 [SWE-ReX](https://github.com/SWE-agent/SWE-ReX) — SWE-ReX.
- 🔧 🐍 [SmolVM](https://github.com/CelestoAI/SmolVM) — Lightweight open-source VM sandbox for AI agent code execution and browser use.
- 🔧 🦀 [pctx](https://github.com/portofcontext/pctx) — Execution layer running agentic tool calls in secure sandboxes for AI workflows.
- 🔧 [openhands-aci](https://github.com/All-Hands-AI/openhands-aci) — Defines standard interface layer for agent-computer interaction in OpenHands.
- 🔧 🐍 [SWE-bench-docker](https://github.com/aorwall/SWE-bench-docker) — Dockerized sandbox for running SWE-bench evaluations in isolated containers.
- 🔧 🐹 [the-agent-sandbox-taxonomy](https://github.com/kajogo777/the-agent-sandbox-taxonomy) — Taxonomy and scoring framework for AI agent sandboxes with 7 defense layers.
- 🔧 🐍 [ai-code-sandbox](https://github.com/typper-io/ai-code-sandbox) — Docker-based secure Python sandbox for isolated AI/LLM-generated code execution.
- 🔧 🐍 [agentbox](https://github.com/Michaelliv/agentbox) — Sandboxed code execution environment for AI agents.
- 🔧 🦀 [godbox](https://github.com/quantumsheep/godbox) — Secure sandboxing system for executing untrusted code in evaluation pipelines.
- 🔧 🐍 [MultiModal-Jupyter-Sandbox](https://github.com/ChenShawn/MultiModal-Jupyter-Sandbox) — MultiModal-Jupyter-Sandbox.
- 🔧 [awesome-agent-sandboxes](https://github.com/arjan/awesome-agent-sandboxes) — Curated list of code execution sandbox solutions for AI/LLM agents.
- 🔧 🐍 [Code-Runner-Sandbox](https://github.com/shouldnotappearcalm/Code-Runner-Sandbox) — Multi-language code execution sandbox (Python/Java/C/Go) for model evaluation.
- 🔧 🐍 [diy-sample-sandbox-cloud-run](https://github.com/GoogleCloudPlatform/diy-sample-sandbox-cloud-run) — Experimental on-demand code execution sandbox built on Google Cloud Run.
- 🔧 🐍 [sandboxed-jupyter-code-exec](https://github.com/anukriti-ranjan/sandboxed-jupyter-code-exec) — FastAPI sandboxed Python code execution environment using Jupyter kernels.
- 🔧 🐍 [exec-sandbox](https://github.com/dualeai/exec-sandbox) — exec-sandbox.
- 🔧 🐍 [python-sandbox](https://github.com/onyx-dot-app/python-sandbox) — Secure lightweight Python code execution sandbox for LLM/AI agents.
- 🔧 🐍 [skypilot-code-sandbox](https://github.com/alex000kim/skypilot-code-sandbox) — skypilot-code-sandbox.
- 🔧 🦀 [nix-sandbox-mcp](https://github.com/secbear/nix-sandbox-mcp) — Nix and bubblewrap sandboxed code execution via MCP for LLM agents.
- 🔧 🐍 [SWE-bench Harness](https://github.com/epoch-research/SWE-bench) — Containerized runtime environments for SWE-bench task evaluation via Docker.
- 🔧 🐍 [sandboxer](https://github.com/ammmir/sandboxer) — Forkable code execution sandbox server for LLMs and agents.
- 🔧 🐍 [moatless-testbeds](https://github.com/aorwall/moatless-testbeds) — moatless-testbeds.
- 🔧 🐍 [AgentKernelArena](https://github.com/AMD-AGI/AgentKernelArena) — Isolated sandbox for side-by-side benchmarking of SE agents on kernel tasks.
- 🔧 🐹 [boxed](https://github.com/akshayaggarwal99/boxed) — Sandboxed code execution engine for AI agents via Docker, Firecracker, and Wasm.
- 🔧 🦀 [mithril](https://github.com/radimsem/mithril) — Trustless MCP server with sandboxed execution tools for AI coding agents.
- 📝 [AgentRun](https://github.com/Jonathan-Adly/AgentRun) — Python library for running AI-generated code safely in Docker sandboxes.
- 📝 [AgentSim: A Platform for Verifiable Agent-Trace Simulation](https://arxiv.org/abs/2604.26653v1) — Platform for simulating and verifying agent traces for training/evaluation.
- 📝 [daVinci-Env: Open SWE Environment Synthesis at Scale](https://arxiv.org/abs/2603.13023) — Synthesizes executable SWE environments at scale for agent evaluation.
- 🔧 [Daytona](https://daytona.io) — Dev environment platform with persistent state and checkpoints for agent tasks.
- 📝 [MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering](https://arxiv.org/abs/2601.22859) — MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering.
- 🔧 [Modal](https://modal.com) — Modal.
- 📝 [PIPer: On-Device Environment Setup via Online Reinforcement Learning](https://arxiv.org/abs/2509.25455) — Online RL agent for automated on-device software project environment setup.
- 📝 [RAT: RunAnyThing via Fully Automated Environment Configuration](https://arxiv.org/abs/2604.23190) — RAT: RunAnyThing via Fully Automated Environment Configuration.
- 📝 [ScaleBox](https://arxiv.org/abs/2604.29700) — High-fidelity and scalable code verification sandbox for LLMs.
- 📝 [SWE-World: Building Software Engineering Agents in Docker-Free Environments](https://arxiv.org/abs/2602.03419) — SWE-World: Building Software Engineering Agents in Docker-Free Environments.

> See also: [Evaluation Harness](#harness), [Observability](#observability)

### Security & Vulnerability

- 📝 [VibeGuard: Security Gate Framework for AI-Generated Code](https://arxiv.org/abs/2604.01052) — Pre-publish security gate targeting 5 blind spots in AI-generated code.

> See also: [Testing & QA](#testing), [Bug Fix & Issue Resolution](#bug-fix)

</details>

## 🏆 Leaderboards

<details>
<summary>⑤ Leaderboards (23 resources)</summary>

### Activity

- 🔧 🐍 [claude-agent-leaderboard](https://github.com/kubony/claude-agent-leaderboard) — Leaderboard tracking agent/skill execution contributions in Claude Code.
- 🔧 [showdown](https://github.com/verseles/showdown) — Aggregates LLM rankings across multiple benchmarks with open community data.
- 📊 [Coding AI Leaderboard](https://www.star-history.com/coding-ai-leaderboard) — Tracks real-world activity of AI coding bots on GitHub (PRs, merge rates).
- 📝 [AgentPulse: A Continuous Multi-Signal Framework for Evaluating AI Agents in Deployment](https://arxiv.org/abs/2604.24038v1) — AgentPulse: A Continuous Multi-Signal Framework for Evaluating AI Agents in Deployment.
- 📝 [Agentic Much? Adoption of Coding Agents on GitHub](https://arxiv.org/abs/2601.18341) — Study of coding agent adoption patterns on GitHub in early 2025.

### Code Generation

- 🔧 [Julia-LLM-Leaderboard](https://github.com/svilupp/Julia-LLM-Leaderboard) — Leaderboard comparing AI models on Julia code generation with automated evals.
- 📝 [AI Coding Model Rankings & Benchmarks](https://onyx.app/best-llm-for-coding) — Ranks major LLMs across SE, code generation, and agentic coding benchmarks.
- 📝 [Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/) — Aider polyglot benchmark leaderboard comparing LLM coding across 6 languages.
- 📝 [Augment leads on CCEval: Benchmarking code completion for continuous improvement](https://www.augmentcode.com/blog/augment-leads-on-cceval-benchmarking-code-completion-for-continuous-improvement) — Augment leads on CCEval: Benchmarking code completion for continuous improvement.
- 📝 [Best AI Models for Coding - Arena Leaderboard](https://arena.ai/leaderboard/code) — Best AI Models for Coding - Arena Leaderboard.
- 📊 [BigCodeBench Leaderboard](https://huggingface.co/spaces/bigcode/bigcodebench-leaderboard) — Ranks LLMs on complex function-level code generation with diverse library calls.
- 📊 [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html) — EvalPlus Leaderboard.
- 📝 [LM Arena Coding Leaderboard: What Developers Need to Know](https://propelcode.ai/blog/lm-arena-coding-leaderboard-insights-for-developers) — Analysis of LM Arena coding leaderboard results and top model rankings.
- 📊 [LiveCodeBench Leaderboard](https://livecodebench.github.io/leaderboard.html) — LiveCodeBench Leaderboard.

### SE Agent

- 🔧 ☕ [Chronos](https://github.com/Kodezi/Chronos) — Debugging-first LM claiming SOTA on SWE-bench Lite with 80.33% resolve rate.
- 🔧 🐍 [multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) — Multi-agent coding system reaching #13 on TerminalBench leaderboard.
- 📝 [Auggie tops SWE-Bench Pro](https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro) — Auggie agent achieves top score of 51.80% on SWE-bench Pro leaderboard.
- 📝 [SWE-Bench Leaderboard March 2026](https://www.marc0.dev/en/leaderboard) — SWE-Bench Leaderboard March 2026.
- 📊 [SWE-bench Leaderboard](https://www.swebench.com) — Tracks SE agent resolve rates on 500 human-validated GitHub issues.
- 📝 [SWE-bench Verified (Epoch AI benchmark page)](https://epoch.ai/benchmarks/swe-bench-verified/) — Epoch AI leaderboard tracking agent performance on SWE-bench Verified.
- 📝 [Ultimate LLM Leaderboard for Agentic Coders](https://theaiforger.com/) — Aggregated LLM rankings for agentic coding across multiple benchmarks.
- 📝 [LLM Coding Leaderboard April 2026](https://www.datalearner.com/leaderboards/category/code) — Aggregated LLM coding leaderboard covering SWE-bench, LiveCodeBench and more.
- 📝 [Computer Agent Arena: Toward Human-Centric Evaluation and Analysis of Computer-Use Agents](https://openreview.net/forum?id=3x4SDbXbgl) — Human-centric evaluation platform and leaderboard for computer-use agents.

</details>

## 🔬 Meta-Analysis & Pitfalls

<details>
<summary>⑥ Meta-Analysis & Pitfalls (106 resources)</summary>

### Blogs & Practice Reports

- 📝 [2024 in Agents [LS Live! @ NeurIPS 2024]](https://www.latent.space/p/2024-agents) — Latent Space podcast: Graham Neubig on 8 key problems in building AI agents.
- 🌐 [8 Benchmarks Shaping AI Agents](https://tessl.io/blog/8-benchmarks-shaping-the-next-generation-of-ai-agents/) — Analyzes 8 key benchmarks shaping AI agent capabilities and trends.
- 📝 [8 benchmarks shaping the next generation of AI agents](https://ainativedev.io/news/8-benchmarks-shaping-the-next-generation-of-ai-agents) — Blog surveying 8 key benchmarks shaping next-gen AI agents including SWE-bench.
- 📝 [[State of Code Evals] After SWE-bench, Code Clash & SOTA Coding Benchmarks recap](https://www.latent.space/p/state-of-code-evals-after-swe-bench) — [State of Code Evals] After SWE-bench, Code Clash & SOTA Coding Benchmarks recap.
- 📝 [A review of OpenAI's o1 and how we evaluate coding agents](https://cognition.ai/blog/evaluating-coding-agents) — Cognition AI blog on coding agent evaluation methodology with o1 analysis.
- 📝 [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) — A Self-Improving Coding Agent.
- 📝 [a smarter way to evaluate coding AI (Toloka)](https://toloka.ai/blog/fixing-swe-bench-a-smarter-way-to-evaluate-coding-ai/) — Toloka blog proposing smarter evaluation fixes for SWE-bench limitations.
- 📝 [Agent Evaluation in 2026](https://orq.ai/blog/agent-evaluation) — Agent Evaluation in 2026.
- 📝 [Agent Evaluation Tools Compared: Why Generic Benchmarks Fail Production AI (2026)](https://latitude.so/blog/agent-evaluation-tools-comparison-product-specific-vs-generic-benchmarks) — Agent Evaluation Tools Compared: Why Generic Benchmarks Fail Production AI (2026).
- 📝 [Agent Factory Recap: A Deep Dive into Agent Evaluation, Practical Tooling, and Multi-Agent Systems](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-a-deep-dive-into-agent-evaluation-practical-tooling-and-multi-agent-systems) — Agent Factory Recap: A Deep Dive into Agent Evaluation, Practical Tooling, and Multi-Agent Systems.
- 📝 [Agentic coding evals — AI PM Wiki](https://genaipm.com/wiki/concepts/agentic-coding-evals) — AI PM Wiki overview of core concepts for evaluating agentic coding systems.
- 📝 [AI Benchmarks Are Broken and Nobody Wants to Admit It](https://fordelstudios.com/research/ai-benchmarks-are-broken-and-nobody-wants-to-admit-it) — Critique of AI benchmark vanity metrics vs real-world production performance.
- 📝 [AI coding benchmarks - failingfast.io](https://failingfast.io/ai-coding-guide/benchmarks/) — Overview of AI coding benchmarks including SWE-bench, Aider, and Arena Code.
- 📝 [AI evals are becoming the new compute bottleneck](https://huggingface.co/blog/evaleval/eval-costs-bottleneck) — HuggingFace blog on AI eval costs becoming the new compute bottleneck.
- 📝 [Benchmarking Multi-Agent AI: Insights & Practical Use](https://galileo.ai/blog/benchmarks-multi-agent-ai) — Blog overview of evaluation frameworks for multi-agent AI systems.
- 🌐 [CodeAnt: Multi-Step Workflow Evaluation Guide](https://www.codeant.ai/blogs/evaluate-llm-agentic-workflows) — CodeAnt: Multi-Step Workflow Evaluation Guide.
- 📝 [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Demystifying evals for AI agents.
- 📝 [Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work](https://cognition.ai/blog/devin-annual-performance-review-2025) — Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work.
- 📝 [Engineering in the Age of AI: 2026 Benchmark Report](https://www.cortex.io/post/ai-is-making-engineering-faster-but-not-better-state-of-ai-benchmark-2026) — Engineering in the Age of AI: 2026 Benchmark Report.
- 📝 [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) — Evaluating AI agents: Real-world lessons from building agentic systems at Amazon.
- 📝 [Every Major Eval Explained and Ranked](https://www.morphllm.com/ai-coding-benchmarks-2026) — Guide explaining and ranking major AI coding benchmarks with model scores.
- 📝 [From Vibe Checks to Continuous Evaluation: Engineering Reliable AI Agents](https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents) — Google Cloud blog on moving from vibe checks to continuous eval for AI agents.
- 🌐 [Galileo: Agent Evaluation Framework](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks) — Galileo: Agent Evaluation Framework.
- 📝 [How we built a high-quality AI code review agent](https://www.augmentcode.com/blog/how-we-built-high-quality-ai-code-review-agent) — How we built a high-quality AI code review agent.
- 🌐 [InfoQ: Evaluating AI Agents — Lessons Learned](https://www.infoq.com/articles/evaluating-ai-agents-lessons-learned/) — Shares practitioner lessons on AI agent evaluation metrics and common pitfalls.
- 🌐 [MiniMax: Production-Grade Benchmark Standard](https://www.minimax.io/news/production-grade-benchmark-for-coding-agents) — MiniMax proposes production-grade coding agent evaluation beyond toy benchmarks.
- 🌐 [Nilenso: What Benchmarks Actually Measure](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/) — Engineer reflection on what SWE benchmarks actually measure vs real SE skills.
- 🌐 [OpenAI: Harness Engineering for Codex](https://openai.com/index/harness-engineering/) — OpenAI shares Codex agent-first engineering practices on eval harness design.
- 📝 [Some critical issues with the SWE-bench dataset (HN discussion)](https://news.ycombinator.com/item?id=43130732) — HN discussion on critical issues with the SWE-bench dataset.
- 📝 [The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evaluation](https://substack.com/redirect/c460aa80-c741-441d-b041-8c96d766b047) — The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evaluation.
- 📝 [Towards a science of scaling agent systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) — Google Research blog on scaling laws and effectiveness of agent systems.
- 📝 [What Is the SWE-Rebench Benchmark? How Decontaminated Tests Expose Chinese Model Weaknesses](https://www.mindstudio.ai/blog/swe-rebench-benchmark-decontaminated-tests-model-inflation) — What Is the SWE-Rebench Benchmark? How Decontaminated Tests Expose Chinese Model Weaknesses.
- 📝 [Why 92% on Your Test Suite Means 40% User Satisfaction](https://tianpan.co/blog/2026-03-18-eval-to-production-gap) — Reveals gap between AI agent eval scores and real-world user satisfaction.
- 📝 [Why Your Agent Passes Every Benchmark and Still Fails in Production](https://tianpan.co/blog/2026-04-10-long-horizon-evaluation-gap-agent-benchmarks) — Why Your Agent Passes Every Benchmark and Still Fails in Production.
- 📝 [Your Agent Aced the Benchmark. Production Disagreed.](https://www.chanl.ai/blog/ai-agent-evaluation-benchmarks-predict-production) — Your Agent Aced the Benchmark. Production Disagreed..

### Efficiency

- 📝 [Turn-Control Strategies for Efficient Coding Agents](https://arxiv.org/abs/2510.16786) — Empirical study of turn-control strategies reducing agent cost 24-68%.

### Benchmark Limitations

- 📝 [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://arxiv.org/abs/2510.21614) — Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine.
- 📝 [Multilingual Prompt Localization for Agent-as-a-Judge: Language and Backbone Sensitivity in Requirement-Level Evaluation](https://arxiv.org/abs/2604.04532) — Multilingual Prompt Localization for Agent-as-a-Judge: Language and Backbone Sensitivity in Requirement-Level Evaluation.
- 📝 [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests) — OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed.
- 🌐 [SWE-bench Score vs Production Capability Gap](https://tianpan.co/blog/2026-04-09-agentic-coding-production-swebench-gap) — SWE-bench Score vs Production Capability Gap.
- 📝 [What skills does SWE-bench Verified evaluate?](https://epoch.ai/blog/what-skills-does-swe-bench-verified-evaluate) — What skills does SWE-bench Verified evaluate?.
- 📝 [Why LLM Benchmarks Fail Your AI Agent (The 0.95^10 Problem)](https://www.bestaifor.com/blog/the-agentic-ai-failure-stack-benchmarks-hallucinations-and-the-0-95-10-problem) — Why LLM Benchmarks Fail Your AI Agent (The 0.95^10 Problem).
- 📝 [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) — OpenAI drops SWE-bench Verified citing 59.4% test defects in failure cases.

### Multi-Agent

- 📝 [Agyn: Multi-Agent System for Team-Based Autonomous SE](https://arxiv.org/abs/2602.01465) — Multi-agent team system resolving 72.2% of SWE-bench 500 tasks.

### Agent Output Quality Studies

- 📝 [CROWDSELECT](https://github.com/listentm/CROWDSELECT) — CROWDSELECT.
- 📝 [AI Writes, We Analyze: The ChatGPT Python Code Saga](https://www.semanticscholar.org/paper/60a25d8a5d004b6369c84d73e89c04edcfabfa99) — Analyzes quality and security of 1756 ChatGPT-generated Python code snippets.
- 📝 [AI-Generated Smells](https://arxiv.org/abs/2604.28900) — Analysis of code and architecture smells in LLM/agent-driven development.
- 📝 [AIDev: Large-Scale Empirical Study of 930K Agentic PRs](https://arxiv.org/html/2602.09185) — AIDev: Large-Scale Empirical Study of 930K Agentic PRs.
- 📝 [Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/abs/2503.15223) — Analyzes correctness of SWE-bench passing patches beyond test-suite adequacy.
- 📝 [Assessing and Advancing Benchmarks for Evaluating Large Language Models in Software Engineering Tasks](https://arxiv.org/abs/2505.08903) — Assessing and Advancing Benchmarks for Evaluating Large Language Models in Software Engineering Tasks.
- 📝 [Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests](https://arxiv.org/abs/2601.20109) — Analyzes post-merge code quality issues in 1210 AI agent-generated bug-fix PRs.
- 📝 [Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering](https://arxiv.org/abs/2604.16790) — Audits LLM-as-a-judge reliability and biases in software engineering evaluation.
- 📝 [Can ChatGPT replace StackOverflow? A Study on Robustness and Reliability of Large Language Model Code Generation](https://arxiv.org/abs/2308.10335) — Study on robustness and reliability of LLM code generation vs Stack Overflow.
- 📝 [Code Review Agent Effectiveness Study](https://arxiv.org/html/2603.11078v1) — Empirical study on AI code review signal-to-noise ratio and developer adoption.
- 📝 [Demystifying Memorization in LLM-Based Program Repair via a General Hypothesis Testing Framework](https://www.semanticscholar.org/paper/160460f3954fd8a606a40bc666ac4968f7919eb5) — Tests whether LLM-based program repair reflects memorization or true reasoning.
- 📝 [Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents](https://arxiv.org/abs/2604.11088) — Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents.
- 📝 [Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions](https://arxiv.org/abs/2508.18771) — Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions.
- 📝 [Evaluating Agentic AI in the Wild](https://arxiv.org/abs/2604.29400) — Failure modes, drift patterns, and production evaluation framework.
- 📝 [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?.
- 📝 [Exploring and Evaluating Hallucinations in LLM-Powered Code Generation](https://arxiv.org/abs/2404.00971) — Study exploring and evaluating hallucinations in LLM code generation.
- 📝 [Exploring Autonomous Agents: A Closer Look at Why They Fail When Completing Tasks](https://arxiv.org/abs/2508.13143) — Analyzes failure modes of autonomous LLM agents across 34 programmable tasks.
- 📝 [How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests](https://arxiv.org/abs/2601.17581) — Analyzes 24K merged GitHub PRs comparing AI agent vs human code change patterns.
- 📝 [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750) — Analyzes token consumption patterns and cost prediction for AI coding agents.
- 📝 [How Well Does Agent Development Reflect Real-World Work?](https://arxiv.org/abs/2603.01203) — How Well Does Agent Development Reflect Real-World Work?.
- 📝 [Human-Agent versus Human Pull Requests: A Testing-Focused Characterization and Comparison](https://arxiv.org/abs/2601.21194) — Human-Agent versus Human Pull Requests: A Testing-Focused Characterization and Comparison.
- 📝 [Is Your Automated Software Engineer Trustworthy?](https://arxiv.org/abs/2506.17812) — Examines trustworthiness of coding agents and confidence calibration gaps.
- 🌐 [METR: SWE-bench Merge Rate Study](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/) — METR: SWE-bench Merge Rate Study.
- 📝 [Multi-Layered Memory Architectures for LLM Agents](https://arxiv.org/abs/2603.29194) — Multi-layer memory for persona consistency and fact stability in long dialogue.
- 📝 [Neurosymbolic Repo-level Code Localization](https://arxiv.org/abs/2604.16021) — Neurosymbolic Repo-level Code Localization.
- 📝 [ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents](https://arxiv.org/abs/2604.07789) — Quantifies oracle signal leakage impact on SWE agent benchmark performance.
- 📝 [Patch Patterns & Code Quality](https://arxiv.org/html/2410.12468) — Analyzes code quality of 4892 agent-generated patches for patterns and smells.
- 📝 [Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection](https://arxiv.org/abs/2602.05868) — Evaluates human feedback and static analyzers for securing LLM-generated code.
- 📝 [Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards](https://arxiv.org/abs/2601.08778) — Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards.
- 📝 [Promises, Perils, and (Timely) Heuristics for Mining Coding Agent Activity](https://arxiv.org/abs/2601.18345) — Promises, Perils, and (Timely) Heuristics for Mining Coding Agent Activity.
- 📝 [Proving Test Set Contamination in Black Box Language Models](https://arxiv.org/abs/2310.17623) — Proves test set contamination in black-box LLMs without training data access.
- 📝 [Quality Assessment of ChatGPT Generated Code and their Use by Developers](https://www.semanticscholar.org/paper/307e2a2285e78ef21e4e9f1cc47ef4e6ee653657) — Quality Assessment of ChatGPT Generated Code and their Use by Developers.
- 📝 [Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models](https://arxiv.org/abs/2403.04811) — Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models.
- 📝 [Research community dynamics behind popular AI benchmarks](https://www.semanticscholar.org/paper/6e84ff78ed2baf688803cec60ffc7240edc2d334) — Analyzes research community dynamics and evolution behind popular AI benchmarks.
- 📝 [Rethinking Benchmark and Contamination for Language Models with Rephrased Samples](https://arxiv.org/abs/2311.04850) — Rethinking Benchmark and Contamination for Language Models with Rephrased Samples.
- 📝 [Rethinking Repetition Problems of LLMs in Code Generation](https://arxiv.org/abs/2505.10402) — Studies repetition problems of LLMs in code generation tasks.
- 📝 [Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents](https://arxiv.org/abs/2602.07900) — Analyzes value of agent-generated tests for LLM-based repo-level issue solving.
- 📝 [Rocks Coding, Not Development--A Human-Centric, Experimental Evaluation of LLM-Supported SE Tasks](https://arxiv.org/abs/2402.05650) — Rocks Coding, Not Development--A Human-Centric, Experimental Evaluation of LLM-Supported SE Tasks.
- 📝 [Social Bias in LLM-Generated Code](https://arxiv.org/abs/2604.29900) — Benchmark and mitigation for social bias in LLM-generated code.
- 📝 [SWE-Bench+: Enhanced Coding Benchmark for LLMs](https://arxiv.org/abs/2410.06992) — SWE-Bench+: Enhanced Coding Benchmark for LLMs.
- 📝 [These Aren't the Reviews You're Looking For](https://arxiv.org/abs/2604.28800) — Study how humans review AI-generated pull requests.
- 📝 [Top Leaderboard Ranking = Top Coding Proficiency, Always? EvoEval: Evolving Coding Benchmarks via LLM](https://arxiv.org/abs/2403.19114) — Top Leaderboard Ranking = Top Coding Proficiency, Always? EvoEval: Evolving Coding Benchmarks via LLM.
- 📝 [Understanding Software Engineering Agents Through the Lens of Traceability: An Empirical Study](https://arxiv.org/abs/2506.08311) — Empirical study of SWE agent decision workflows via traceability lens.
- 📝 [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://arxiv.org/abs/2506.09289) — Exposes weak SWE-Bench tests and proposes UTBoost for stricter agent evaluation.
- 📝 [What Makes Software Bugs Escape Testing? Evidence from a Large-Scale Empirical Study](https://arxiv.org/abs/2604.26672v1) — What Makes Software Bugs Escape Testing? Evidence from a Large-Scale Empirical Study.
- 📝 [What's Wrong with Your Code Generated by Large Language Models? An Extensive Study](https://arxiv.org/abs/2407.06153) — What's Wrong with Your Code Generated by Large Language Models? An Extensive Study.
- 📝 [Why Are AI Agent Involved Pull Requests (Fix-Related) Remain Unmerged? An Empirical Study](https://arxiv.org/abs/2602.00164) — Empirical study on why AI agent fix-related pull requests remain unmerged.

### Surveys

- 📝 [74% of Production Agents Still Rely on Human Evaluation](https://www.chanl.ai/blog/production-eval-gap-survey) — 74% of Production Agents Still Rely on Human Evaluation.
- 📝 [A Survey of Code Review Benchmarks and Evaluation Practices in Pre-LLM and LLM Era](https://arxiv.org/abs/2602.13377) — A Survey of Code Review Benchmarks and Evaluation Practices in Pre-LLM and LLM Era.
- 📝 [A Survey on Large Language Model Benchmarks](https://arxiv.org/abs/2508.15361) — Survey covering benchmarks used to evaluate large language models.
- 📝 [Agent Benchmarks for Enterprise](https://simmering.dev/blog/agent-benchmarks/) — Agent Benchmarks for Enterprise.
- 📝 [Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering](https://arxiv.org/abs/2604.26275) — Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering.
- 📝 [AI-SQE: The 1st International Workshop on AI for Software Quality Evaluation](https://conf.researchr.org/home/icse-2026/ai-sqe-2026) — AI-SQE: The 1st International Workshop on AI for Software Quality Evaluation.
- 📝 [code LLM survey](https://arxiv.org/abs/2311.07989) — Survey of large language models for code understanding and generation.
- 📝 [Code Reasoning for Software Engineering Tasks: A Survey and A Call to Action](https://arxiv.org/abs/2506.13932) — Surveys LLM code reasoning techniques for SE tasks with gap analysis.
- 📝 [Mapping global dynamics of benchmark creation and saturation in artificial intelligence](https://arxiv.org/abs/2203.04592) — Mapping global dynamics of benchmark creation and saturation in artificial intelligence.
- 📝 [Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering](https://arxiv.org/abs/2604.01437) — Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering.
- 📝 [Software Development Life Cycle Perspective: A Survey of Benchmarks for Code Large Language Models and Agents](https://arxiv.org/abs/2505.05283) — Software Development Life Cycle Perspective: A Survey of Benchmarks for Code Large Language Models and Agents.
- 📝 [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) — Survey on Evaluation of LLM-based Agents.
- 🌐 [Symflower: LLM Agent Benchmarks Survey](https://symflower.com/en/company/blog/2025/benchmarks-llm-agents/) — Surveys SE agent benchmarks covering scope, limitations, and selection guidance.
- 📝 [The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding](https://www.semanticscholar.org/paper/435053aacc2d87f401787bd9a7e9d82575dd6deb) — The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding.
- 📝 [The Semi-Executable Stack: Agentic Software Engineering and the Expanding Scope of SE](https://arxiv.org/abs/2604.15468) — The Semi-Executable Stack: Agentic Software Engineering and the Expanding Scope of SE.

</details>

## 🔗 Related Resources

Complementary awesome lists (no duplication):

| Topic | Recommended |
|---|---|
| LLM Code Benchmarks | [tongye98/Awesome-Code-Benchmark](https://github.com/tongye98/Awesome-Code-Benchmark) |
| LLM for SE (papers) | [iSEngLab/AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) |
| Agent Tools & Frameworks | [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) |
| Agent Harness Engineering | [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) |
| AI Coding Tool Reviews | [murataslan1/ai-agent-benchmark](https://github.com/murataslan1/ai-agent-benchmark) |

## 🤖 For AI Agents

This repo is designed for both human and AI consumption.

| Access Method | File | Best For |
|---|---|---|
| Full content dump | [llms-full.txt](llms-full.txt) | RAG ingestion, one-shot context |
| Structured index | [llms.txt](llms.txt) | Discovering what's available |
| Query interface | [AGENTS.md](AGENTS.md) | jq/Python query recipes |
| Raw JSON | `data/*.json` | Programmatic filtering |
| Claude Code | [CLAUDE.md](CLAUDE.md) | Working in this repo |

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

Quick checklist:
1. Resource is related to SE Agent evaluation
2. Add to the appropriate `data/*.json` file
3. Fill required schema fields (id, name, stage, subcategory, what, type, tags)
4. Run `python scripts/process/validate.py` to verify

