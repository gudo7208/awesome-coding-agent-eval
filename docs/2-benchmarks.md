# ② Benchmarks & Datasets

SE Agent benchmarks organized by task type.

## Contents

- [Bug Fix & Issue Resolution (69)](#bug-fix)
- [End-to-End / Multi-Task (107)](#end-to-end)
- [Long-Horizon / Evolution (34)](#long-horizon)
- [Large Codebase / Multi-Repo (21)](#large-codebase)
- [Code Review (24)](#code-review)
- [Testing & QA (39)](#testing)
- [Security & Vulnerability (48)](#security)
- [Production-Derived (12)](#production)
- [Code Generation (143)](#code-generation)
- [Feature Development (8)](#feature-development)
- [Multi-Agent (15)](#multi-agent)

<a id="bug-fix"></a>
## Bug Fix & Issue Resolution

*The most established evaluation category. SWE-bench family dominates. Start with SWE-bench Verified for a reliable baseline.*

### A–F

- [A Benchmark for Localizing Code and Non-Code Issues in Software Projects](https://arxiv.org/abs/2509.25242) — Benchmarks issue localization across code and non-code files on 1100 issues.
- [A Real-World Benchmark for Evaluating Fine-Grained Issue Solving Capabilities of](https://arxiv.org/abs/2411.18019) — Evaluates fine-grained issue solving via QA, fault localization, and code editin. 🌍
- [AEGIS: An Agent-based Framework for Bug Reproduction from Issue Descriptions](https://www.semanticscholar.org/paper/89dccc903cbeddb8c09df35c5c5da7aeaf0bcd6f) — Agent framework for automated bug reproduction from issue descriptions.
- [Agentic Bug Reproduction for Effective Automated Program Repair at Google](https://arxiv.org/abs/2502.01821) — Evaluates agents generating bug reproduction tests for automated repair at Googl.
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489) — Agent-free LLM localize-repair-verify pipeline as baseline on SWE-bench.
- [Amazon introduces SWE-PolyBench, a multilingual benchmark for AI Coding Agents](https://aws.amazon.com/blogs/devops/amazon-introduces-swe-polybench-a-multi-lingual-benchmark-for-ai-coding-agents/) — SWE-PolyBench: multilingual benchmark for AI coding agents across languages. 🌐
- [An Analysis of the Automatic Bug Fixing Performance of ChatGPT](https://arxiv.org/abs/2301.08653) — Evaluates ChatGPT auto bug fixing on QuixBugs and Defects4J vs traditional APR.
- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](https://www.semanticscholar.org/paper/012a1885351785b62ab8273830197f1e759911ec) — Empirical study on fine-tuning LLMs of code for automated program repair.
- [An LLM-based Agent for Reliable Docker Environment Configuration](https://www.semanticscholar.org/paper/d569c3afc3b6b0e4f142107b893c3d365f58f081) — LLM agent for configuring Docker environments to support SE agent evaluation tas.
- [AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Tests](https://arxiv.org/abs/2507.17542) — Technique for auto-generating bug reproducible tests via LLM assertion inversion.
- [BackportBench: A Multilingual Benchmark for Automated Backporting of Patches](https://arxiv.org/abs/2512.01396) — Multilingual benchmark for automated patch backporting across software versions. 🌐
- [Bug-Report-Driven Fault Localization: Industrial Benchmarking and Lesson Learned at ABB Robotics](https://arxiv.org/abs/2604.25700v1) — Industrial benchmark for bug-report-driven fault localization at ABB Robotics.
- [BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills](https://arxiv.org/abs/2510.19898) — Generates synthetic complex bugs via SWE agents for training and evaluating bug-.
- [BugsInPy: a database of existing bugs in Python programs to enable controlled testing and debugging studies](https://arxiv.org/abs/2401.15481) — Curated database of real Python bugs for controlled testing and debugging studie. 🐍
- [CLEVER:A Curated Benchmark for Formally Verified](https://arxiv.org/abs/2505.13938) — Curated benchmark for formally verified bug fixes in software.
- [COAST: Enhancing the Code Debugging Ability of LLMs through Communicative Agent ](https://arxiv.org/abs/2408.05006) — Multi-agent data synthesis framework to enhance LLM code debugging ability. 🤝
- [CodeMonkeys: Scaling Test-Time Compute for Software Engineering](https://arxiv.org/abs/2501.14723) — Scales test-time compute on SWE-bench via iterative test generation and selectio.
- [CORE: Resolving Code Quality Issues using LLMs](https://www.semanticscholar.org/paper/4202a75d7b3c586ebd9451ed08f38cbf264cfd8e) — LLMs resolving static analysis code quality issues in developer workflows.
- [DebugBench: Evaluating Debugging Capability of Large Language Models](https://arxiv.org/abs/2401.04621) — Benchmark evaluating LLM debugging capability across multiple bug categories.
- [Defects4J: a database of existing faults to enable controlled testing studies for Java programs](https://www.semanticscholar.org/paper/37e2106bebd02f4ac9c410941fde7f358279e4a4) — Database of real Java faults enabling controlled testing/repair studies. ☕
- [Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair](https://arxiv.org/abs/2601.19066) — Co-generates bug reproduction tests with patches in agentic program repair.
- [Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis](https://arxiv.org/abs/2604.24212v1) — Dynamic analysis tooling for autonomous debugging agents in automated program re.
- [Enhancing Program Repair with Specification Guidance and Intermediate Behavioral Signals](https://arxiv.org/abs/2604.11770) — LLM-based APR using intermediate behavioral signals beyond test-suite outcomes.
- [Evaluating and Improving Automated Repository-Level Rust Issue Resolution with L](https://arxiv.org/abs/2602.22764) — Evaluates LLM agent issue resolution on 500 real repo-level Rust problems. 🦀
- [FeedbackEval A Benchmark for Evaluating Large Language Models in Feedback-Driven](https://github.com/SYSUSELab/FeedbackEval) — Benchmark for evaluating LLMs on feedback-driven code repair tasks.

### G–L

- [GitBug-Actions: Building Reproducible Bug-Fix Benchmarks with GitHub Actions](https://arxiv.org/abs/2310.15642) — Reproducible bug-fix benchmark built from GitHub Actions CI pipelines.
- [GitBug-Java: A Reproducible Benchmark of Recent Java Bugs](https://arxiv.org/abs/2402.02961) — Reproducible benchmark of recent real-world Java bugs for evaluating bug-fix too. ☕
- [How Often Do Single-Statement Bugs Occur? The ManySStuBs4J Dataset](https://arxiv.org/abs/1905.13334) — Dataset of 153,652 Java single-statement bug-fix changes for program repair. ☕
- [HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks](https://arxiv.org/abs/2604.14709) — Benchmarks LLM agents on hardware bug repair with 417 real PRs from 6 HDL projec.
- [InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Soft](https://arxiv.org/abs/2511.16004) — Adversarial multi-agent framework iteratively refining tests and patches for rep. 🤝
- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) — OpenAI releases SWE-bench Verified, human-reviewed subset improving benchmark re.
- [joycode-agent](https://github.com/jd-opensource/joycode-agent) ⭐330 — Repository-level repair agent built and evaluated on SWE-Bench.
- [Large Language Models of Code Fail at Completing Code with Potential Bugs](https://arxiv.org/abs/2306.03438) — Benchmark for code completion degradation when context contains potential bugs.
- [Lingma SWE-GPT: An Open Development-Process-Centric Language Model for Automated](https://arxiv.org/abs/2411.00622) — Dev-process-centric open LLM for automated software repair on SWE-bench.
- [LocAgent: Graph-Guided LLM Agents for Code Localization](https://arxiv.org/abs/2503.09089) — Graph-guided LLM agent framework for code localization evaluated on bug-fix task.

### M–R

- [MLDebugging: Towards Benchmarking Code Debugging Across Multi-Library Scenarios](https://arxiv.org/abs/2506.13824) — Benchmark for code debugging across multi-library scenarios.
- [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) ⭐333 — Evaluates agents on real GitHub issues across Java, TypeScript, Go, Rust, and C+. 🌐
- [OmniGIRL](https://github.com/DeepSoftwareAnalytics/OmniGIRL) ⭐17 — Multilingual multimodal GitHub issue resolution benchmark across Python/JS/TS/Go. 🌐
- [OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution](https://arxiv.org/abs/2505.04606) — Multilingual and multimodal benchmark for evaluating GitHub issue resolution. 🌐
- [Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?](https://arxiv.org/abs/2604.17338) — Evaluates whether models precisely debug or simply regenerate entire code.
- [QuixBugs: a multi-lingual program repair benchmark set based on the quixey challenge](https://www.semanticscholar.org/paper/7f1d443ab526240e2647e77e042434fc98249302) — Multi-lingual program repair benchmark for evaluating automated bug-fixing agent. 🌐
- [RepairBench: Leaderboard of Frontier Models for Program Repair](https://arxiv.org/abs/2409.18952) — Leaderboard benchmarking frontier models on program repair with execution valida. 🏆
- [Reproducible Automated Program Repair Is Hard -- Experiences With the Defects4J Dataset](https://arxiv.org/abs/2604.26674v1) — Reproducibility challenges in APR evaluation using Defects4J benchmark dataset.
- [Rust-SWE-Bench](https://github.com/GhabiX/Rust-SWE-Bench) ⭐11 — Evaluates agent issue-resolution ability on real Rust project GitHub issues. 🦀

### S–Z

- [Skywork-SWE](https://arxiv.org/html/2506.19290v1) — Benchmark validating data scaling laws for SE agent bug-fix capability. 🐍
- [SpecRover: Code Intent Extraction via LLMs](https://arxiv.org/abs/2408.02232) — Infers code intent via LLMs for specification-driven automated program repair.
- [SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark](https://arxiv.org/abs/2603.00520) — Adversarial framework exposing inflated SWE-Bench scores via test suite strength.
- [SWE-bench](https://github.com/swe-bench/SWE-bench) ⭐4819 — 2294 real GitHub issues testing agent patch generation for Python bug fixes. 🐍
- [SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks](https://arxiv.org/abs/2604.26278) — SWE-Bench-style bug-fix benchmark for 5G core network software using Docker+test.
- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419) — Continuously updated SWE-bench variant improving repo coverage and scalability.
- [SWE-bench Multimodal](https://github.com/swe-bench/SWE-bench) ⭐4819 — Extends SWE-bench with visual software engineering tasks like UI bugs and screen.
- [SWE-bench Verified](https://github.com/swe-bench/SWE-bench) ⭐4819 — 500 human-verified subset of SWE-bench filtering ambiguous or erroneous issues. 🐍
- [SWE-Bench-Fork](https://github.com/SWE-Gym/SWE-Bench-Fork) ⭐13 — SWE-Gym fork of SWE-Bench for evaluating agents on real GitHub issue fixes.
- [SWE-bench-java: A GitHub Issue Resolving Benchmark for Java](https://arxiv.org/abs/2408.14354) — Extends SWE-bench to Java with real GitHub issue resolving tasks. ☕
- [swe-bench-lite-samples](https://github.com/ScalingIntelligence/swe-bench-lite-samples) ⭐14 — Samples and analyzes SWE-bench Lite dataset characteristics and task distributio.
- [SWE-Bench-plus-plus](https://github.com/TuringEnterprises/SWE-Bench-plus-plus) ⭐19 — Enhanced SWE-Bench with improved tests and reduced data leakage for bug-fix eval.
- [swe-bench.github.io](https://github.com/SWE-bench/swe-bench.github.io) ⭐12 — SWE-bench official leaderboard ranking AI agents on real GitHub issue resolution. 🏆
- [SWE-Dev: Building Software Engineering Agents with Training and Inference Scalin](https://arxiv.org/abs/2506.07636) — Provides 17K+ training instances and test cases for SWE agents with scaling.
- [SWE-Exp: Experience-Driven Software Issue Resolution](https://arxiv.org/abs/2507.23361) — Benchmarks experience-driven issue resolution using historical fix patterns on S.
- [SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Re](https://arxiv.org/abs/2501.05040) — Trains open-source LLMs to resolve GitHub issues on SWE-bench tasks.
- [SWE-MERA](https://github.com/MERA-Evaluation/repotest) ⭐14 — Dynamic rolling SWE benchmark with fresh issues to prevent data contamination.
- [SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on ](https://arxiv.org/abs/2507.11059) — Dynamic benchmark for evaluating LLMs on software engineering tasks, addressing .
- [SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories](https://arxiv.org/abs/2509.08724) — Scales issue-resolving datasets by mirroring issues across repo environments.
- [SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evalua](https://arxiv.org/abs/2505.20411) — Automated pipeline for continuous task collection and decontaminated SWE agent e.
- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798) — Scalable pipeline for synthesizing SWE training data with bug-fix benchmark.
- [SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models ](https://arxiv.org/abs/2504.14757) — Synthesizes verifiable repo-level bug-fix datasets to improve LLM repair ability.
- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139) — Training environment with 2,438 Python repo tasks and verifier for SE agents.
- [When Large Language Models Confront Repository-Level Automatic Program Repair: H](https://arxiv.org/abs/2403.00448) — Evaluates LLMs on repository-level automated program repair tasks.
- [[repo](https://github.com/NEUIR/DebugEval) — DebugEval: benchmark for evaluating LLM debugging capabilities.

<a id="end-to-end"></a>
## End-to-End / Multi-Task

*Evaluates agents on complete project development, not just isolated fixes. Growing rapidly as agents become more capable.*

### A–F

- [A Comprehensive Benchmark to Evaluate Agent Architectures in Enterprise](https://arxiv.org/html/2509.10769v1) — Benchmark evaluating agent architectures for enterprise multi-step workflows.
- [A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LL](https://arxiv.org/abs/2510.09721) — Comprehensive survey on benchmarks and solutions for LLM-driven SE agent systems. 📋
- [ABC-Bench](https://github.com/OpenMOSS/ABC-Bench) ⭐29 — Evaluates code agents on real-repo backend dev: exploration, editing, config, an.
- [AdamBench](https://github.com/tabupl/AdamBench) ⭐25 — Agentic coding benchmark for local LLMs on daily software engineering tasks.
- [Agentic Software Issue Resolution with Large Language Models: A Survey](https://arxiv.org/abs/2512.22256) — Surveys LLM-based agents for automated software issue resolution. 📋
- [AgentProcessBench](https://arxiv.org/abs/2603.14465) — 1,000 trajectories with 8,509 human labels for step-level tool-use quality.
- [AgentRewardBench](https://arxiv.org/abs/2504.08942) — 1,302-trajectory benchmark for assessing LLM judges of web agent trajectories. 🤖
- [ai-agent-benchmark](https://github.com/murataslan1/ai-agent-benchmark) ⭐24 — Leaderboard comparing 80+ AI coding agents on SWE-Bench with pricing info. 🏆
- [ai-agent-benchmark-compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) ⭐134 — Curated index of 50+ AI agent benchmarks across coding, tool-use, and reasoning.
- [Apex2-Terminal-Bench-Agent](https://github.com/heartyguy/Apex2-Terminal-Bench-Agent) ⭐66 — Benchmarks terminal-based coding agents with leaderboard and ablation results. 🏆
- [appworld](https://github.com/StonyBrookNLP/appworld) ⭐407 — Evaluates agent tool-calling and planning across multi-app scenarios.
- [Automated Benchmark Generation for Repository-Level Coding Tasks](https://arxiv.org/abs/2503.07701) — Automated pipeline for generating repo-level coding agent benchmarks at scale.
- [awesome-code-agents](https://github.com/EuniAI/awesome-code-agents) ⭐99 — Curated list of autonomous code agents, benchmarks, and research papers. 📋
- [BC-Bench](https://github.com/microsoft/BC-Bench) ⭐26 — Evaluates AI agents on Microsoft Business Central AL codebase tasks.
- [Benchmarking and Studying the LLM-based Agent System in End-to-End Software Deve](https://arxiv.org/abs/2511.04064) — Systematic benchmark studying LLM-based agent systems in end-to-end software dev.
- [benchmarks](https://github.com/0xpayne/gpt-migrate#-benchmarks) — GPT-Migrate benchmarks for automated codebase migration between frameworks.
- [Beyond pip Install: Evaluating LLM Agents for the Automated Installation of Pyth](https://arxiv.org/abs/2412.06294) — Evaluates LLM agents on automated Python project installation beyond pip install. 🐍
- [Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents](https://arxiv.org/abs/2506.00172) — Scalable benchmark for evaluating system-level reasoning in LLM code agents.
- [CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tour](https://arxiv.org/abs/2510.26852) — Tournament-style benchmark evaluating code agents' iterative optimization and ev.
- [ccbench](https://github.com/codecrafters-io/ccbench) ⭐29 — CodeCrafters benchmark tool for evaluating coding agents on SE tasks. 🦀
- [Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Ag](https://arxiv.org/abs/2604.20200) — Studies score exploitation by coding agents under user pressure on public benchm.
- [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/abs/2604.05172) — Benchmark evaluating LLM agents on productivity tasks in simulated multi-service.
- [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201) — Benchmarks unified digital agents on long-horizon cross-capability tasks spannin. 📅
- [CodeClash](https://github.com/CodeClash-ai/CodeClash) ⭐147 — Evaluates autonomous agent planning and execution on open-ended coding tasks.
- [CODEMENV: Benchmarking Large Language Models on Code Migration](https://arxiv.org/abs/2506.00894) — Benchmark for evaluating LLMs on code migration tasks across environments.
- [CoreCodeBench: A Configurable Multi-Scenario Repository-Level Benchmark](https://arxiv.org/abs/2507.05281) — Configurable multi-scenario repository-level benchmark for code agents.
- [Credit-Budgeted ICPC-Style Coding: When Agents Must Pay for Every Decision](https://arxiv.org/abs/2604.10182) — Evaluates coding agents on ICPC-style problems with credit-budgeted decisions.
- [Cursor debuts CursorBench-3 to evaluate coding agents](https://www.testingcatalog.com/cursor-debuts-cursorbench-3-to-evaluate-coding-agents/) — CursorBench-3: Cursor's benchmark evaluating coding agents on complex dev tasks.
- [DataSciBench: An LLM Agent Benchmark for Data Science](https://arxiv.org/abs/2502.13897) — Benchmark evaluating LLM agents on data science tasks end-to-end.
- [devin-swebench-results](https://github.com/CognitionAI/devin-swebench-results) ⭐126 — Cognition's published Devin evaluation results and methodology on SWE-bench.
- [DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle](https://arxiv.org/abs/2601.20882) — Benchmarks AI agents across full DevOps cycle: development, deployment, and oper. 📅
- [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703) — Benchmark evaluating data science agents on realistic DS tasks.
- [EnConda-Bench](https://github.com/TencentYoutuResearch/EnConda-Bench) ⭐49 — Benchmarks SE agents on environment configuration with process-level trajectory .
- [EnvBench: A Benchmark for Automated Environment Setup](https://arxiv.org/abs/2503.14443) — Benchmarks LLM agents on automated dev environment setup across real repos.
- [eval-data](https://github.com/paradite/eval-data) ⭐17 — LLM evaluation prompts and datasets for real-world coding and writing tasks.
- [Evaluating Agents' Ability to Conduct Innovative AI Research](https://iclr.cc/virtual/2026/poster/10006754) — Benchmark of 20 tasks evaluating agents on innovative AI research capabilities.
- [Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios](https://arxiv.org/abs/2604.06742) — Benchmarks LLM agents on zero-to-one CLI tool generation with execution-based ev.
- [EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration](https://arxiv.org/abs/2601.16489) — Multi-agent system for autonomous environment configuration in SE task evaluatio. 🤝
- [Evolutionary Perspectives on the Evaluation of LLM-Based AI Agents: A Comprehens](https://arxiv.org/abs/2506.11102) — Surveys evolutionary perspectives on evaluating LLM chatbots vs AI agents. 📋
- [Exploring the Challenges and Opportunities of AI-assisted Codebase Generation](https://arxiv.org/abs/2508.07966) — Study of challenges and opportunities in AI-assisted full codebase generation. 📅
- [From What to How: Bridging User Requirements with Software Development Using Lar](https://arxiv.org/abs/2602.13611) — Benchmarks LLMs on software design from user requirements to code generation.
- [Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver](https://arxiv.org/abs/2604.25067) — Benchmark measuring AI agents' ability to implement ML research pipelines end-to.
- [Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks ](https://arxiv.org/abs/2604.12290) — Benchmarks self-evolving agents on iterative real-world engineering optimization.

### G–L

- [GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation](https://arxiv.org/abs/2604.24929) — Multilingual adaptation workflow for agent benchmarks with cultural/functional a. 🌐
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) ⭐252 — Evaluates repo-level agent workflows from understanding to delivery with cost-aw.
- [GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code ](https://arxiv.org/abs/2508.18993) — Benchmark for code agents solving real-world tasks using code repositories.
- [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763) — GLM-5 model evaluated on agentic SE benchmarks like SWE-bench and DevBench.
- [HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?](https://arxiv.org/abs/2604.09408) — Benchmarks whether coding agents know when to act autonomously vs ask humans for.
- [How we compare model quality in Cursor (CursorBench)](https://cursor.com/blog/cursorbench) — CursorBench: multi-dimensional eval of AI coding agents in Cursor IDE.
- [Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819) — Multi-task benchmark evaluating coding agent generalization across exploration, .
- [IDE-Bench: Evaluating Large Language Models as IDE Agents on Real-World Software](https://arxiv.org/abs/2601.20886) — Evaluates LLMs as IDE agents on real-world software tasks with dockerized tests. 🌍
- [Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://arxiv.org/abs/2602.09892) — Automated multi-agent workflow to generate large-scale SWE training/eval data. 🤝
- [insights](https://github.com/logic-star-ai/insights) ⭐49 — Tracks autonomous coding agents on real open-source projects with leaderboards. 🏆
- [InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feed](https://arxiv.org/abs/2306.14898) — Interactive coding benchmark modeling code tasks as RL with execution feedback.
- [june-2025-coding-agent-report](https://github.com/The-Focus-AI/june-2025-coding-agent-report) ⭐40 — Benchmarks 15 coding agents on real-world development tasks across IDEs.
- [leaderboard](https://github.com/pinchbench/leaderboard) ⭐35 — Leaderboard ranking LLM coding agents on end-to-end programming tasks. 🏆
- [Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs](https://arxiv.org/abs/2509.25873) — Minimal-scaffold agent to evaluate true agentic coding capabilities of LLMs.

### M–R

- [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/abs/2604.23897) — Benchmark assessing AI agents' self-assessment of task cost/ability on SWE-bench.
- [ML-Bench: Evaluating LLMs for Machine Learning Tasks on Repository-Level Code](https://ml-bench.github.io/) — Benchmark evaluating LLMs on repository-level ML tasks with end-to-end execution.
- [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://openreview.net/forum?id=6s5uXNWGIh) — 75 Kaggle ML engineering tasks benchmark for evaluating ML agents.
- [MMBench-GUI](https://github.com/open-compass/MMBench-GUI) ⭐106 — Hierarchical benchmark for GUI agents across desktop, mobile, and web platforms.
- [Multi-Docker-Eval: A 'Shovel of the Gold Rush' Benchmark on Automatic Environmen](https://arxiv.org/abs/2512.06915) — Benchmark for automated environment setup with 40 real repos across 9 languages. 🌐
- [Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving](https://arxiv.org/abs/2504.02605) — Multilingual issue-resolving benchmark across 7 languages with 1632 instances. 🌐
- [OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation](https://arxiv.org/abs/2604.10866) — Benchmark of 100 professional task scenarios across 65 domains via language envi.
- [OmniCode](https://arxiv.org/html/2602.02262v2) — Multi-task SE benchmark covering code generation, refactoring, docs, and bug fix.
- [OmniCode: A Benchmark for Evaluating Software Development Agents](https://openreview.net/forum?id=VP204Aa0gH) — Benchmark evaluating SE agents across bug fix, test gen, style fix, and code rev.
- [OpenCode Bench vs SWE-bench vs Terminal-Bench](https://www.morphllm.com/opencode-benchmarks) — Comparison of OpenCode Bench, SWE-bench, and Terminal-Bench benchmarks.
- [OpenGame: Open Agentic Coding for Games](https://arxiv.org/abs/2604.18394) — Benchmark for evaluating AI coding agents on full game development tasks.
- [OS-SPEAR: A Toolkit for the Safety, Performance,Efficiency, and Robustness Analysis of OS Agents](https://arxiv.org/abs/2604.24348) — Toolkit for safety, performance, efficiency, robustness evaluation of OS GUI age.
- [OSS-Bench: Benchmark Generator for Coding LLMs](https://arxiv.org/abs/2505.12331) — Generates benchmarks for evaluating coding LLMs from open-source repositories.
- [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://openai.com/index/paperbench/) — Benchmark evaluating AI agents on replicating AI research papers from scratch.
- [Process-Level Trajectory Evaluation for Environment Configuration in Software En](https://arxiv.org/abs/2510.25694) — Enconda-bench: process-level trajectory evaluation for SE agent environment conf. 🔍
- [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://arxiv.org/abs/2502.18525) — Benchmark for computer-use agents completing SE tasks by visually operating IDEs.
- [ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development](https://arxiv.org/html/2602.01655v1) — Benchmark for evaluating AI agents on full multi-file project generation from sp.
- [reading-list](https://github.com/SWE-bench/reading-list) ⭐11 — SWE-bench curated reading list of papers on SE agent evaluation and benchmarks. 📋
- [RefactorBench](https://github.com/microsoft/RefactorBench) ⭐23 — Benchmarks agents on cross-file code refactoring tasks in real repositories.
- [RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale](https://arxiv.org/abs/2508.01550) — End-to-end pipeline generating, evaluating, and training SWE agents at scale.
- [RepoUnderstander](https://github.com/RepoUnderstander/RepoUnderstander) ⭐97 — Benchmarks repo-level code understanding via structure and dependency analysis o.

### S–Z

- [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven](https://openreview.net/forum?id=6z4YKr0GK6) — Benchmark for rigorously assessing language agents on data-driven scientific dis.
- [Sea-benchmarks-public](https://github.com/Sea-Labs-ai/Sea-benchmarks-public) ⭐17 — Benchmarks AI coding agents across multiple software engineering tasks.
- [SERA: Soft-Verified Efficient Repository Agents](https://arxiv.org/abs/2601.20789) — SERA: efficient training of repo-specialized coding agents evaluated on SWE-benc.
- [skill](https://github.com/pinchbench/skill) ⭐1079 — Benchmark by Kilo.ai for end-to-end evaluation of LLM coding agents on SE tasks.
- [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Work](https://arxiv.org/abs/2411.07763) — Benchmark evaluating LMs on real-world enterprise text-to-SQL workflows. 🌍
- [SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in](https://arxiv.org/abs/2602.09447) — Benchmarks LLM agents building production-grade software from specs in MoonBit.
- [SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context](https://arxiv.org/abs/2604.11716v1) — Framework for managing dynamic reasoning context in SWE agents, evaluated on SWE.
- [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://arxiv.org/abs/2410.03859) — Evaluates agents on visual software issues extending SWE-bench to multimodal dom.
- [SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live) ⭐185 — Continuously updated contamination-free benchmark of real GitHub issues for SE a. ✅
- [SWE-Compass](https://arxiv.org/html/2511.05459) — Unified benchmark integrating heterogeneous SE tasks for cross-task evaluation.
- [SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent](https://arxiv.org/abs/2604.26102) — SWE-Edit: decoupled code editing interface for SWE agents, evaluated on SWE-benc.
- [SWE-Effi](https://arxiv.org/abs/2509.09853) — Metrics balancing solution accuracy vs resource cost for SWE agent evaluation.
- [SWE-Hub: A Unified Production System for Scalable, Executable Software Engineeri](https://arxiv.org/abs/2603.00575) — Unified system for cross-language env reproduction and scalable bug synthesis ev. 🌐 📅
- [SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software](https://arxiv.org/abs/2502.12115) — Benchmarks LLMs on 1400+ real Upwork freelance tasks worth $1M total. 🌍
- [SWE-PolyBench](https://github.com/amazon-science/SWE-PolyBench) ⭐83 — Multilingual repo-level coding agent benchmark extending SWE-bench beyond Python. 🌐
- [SWE-PolyBench: A multi-language benchmark for repository level evaluation of cod](https://arxiv.org/abs/2504.08703) — Evaluates coding agents on 2110 repo-level tasks across Java, JS, TS, and Python. 🌐
- [SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering Tasks](https://arxiv.org/abs/2511.02352) — Reproducible C# benchmark with 150 instances across 17 repos for agent evaluatio.
- [SWE-Skills-Bench](https://github.com/GeniusHTX/SWE-Skills-Bench) ⭐33 — Benchmarks decomposed SE agent skills like fault localization and code editing.
- [SWE-Universe: Scale Real-World Verifiable Environments to Millions](https://arxiv.org/abs/2602.02361) — Generates millions of verifiable SWE environments from GitHub PRs with anti-hack.
- [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) ⭐1441 — Benchmarks LLMs on 1400+ real freelance software engineering tasks worth $1M+.
- [TDFlow: Agentic Workflows for Test Driven Development](https://arxiv.org/abs/2510.23761) — Test-driven multi-agent workflow for repo-level SE, evaluated on SWE-bench. 🤝
- [TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents](https://arxiv.org/abs/2602.07274) — High-fidelity terminal agent environment and trajectory synthesis for training/e.
- [Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute](https://arxiv.org/abs/2503.23803) — TTC scaling for open-source SE agents evaluated on SWE-bench.
- [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/abs/2604.25727v1) — Skill-graph-based synthesis of terminal task instances for agent training/eval.
- [Towards Generating Functionally Correct Code Edits from Natural Language Issue D](https://arxiv.org/abs/2304.03816) — Evaluates LLM code edits from GitHub issues with hidden test verification.
- [Training Versatile Coding Agents in Synthetic Environments](https://arxiv.org/abs/2512.12216) — Synthetic environment generation for training versatile SE agents beyond issue r.
- [TRAJECT-Bench](https://arxiv.org/abs/2510.04550) — Evaluates LLM tool use via full tool-selection trajectories, not just answers.
- [Unified Software Engineering agent as AI Software Engineer](https://arxiv.org/abs/2506.14683) — Defines AI SE agent concept and evaluates LLM agents as full software engineers.
- [WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224) — Evaluates multimodal web coding with visual fidelity and interaction quality met.

<a id="long-horizon"></a>
## Long-Horizon / Evolution

*Tests multi-step, multi-file changes over extended interactions. Closer to real engineering work than single-issue benchmarks.*

### A–F

- [ALE-Bench: Towards Automating Long-Horizon Algorithm Engineering](https://sakana.ai/ale-bench/) — Benchmark for long-horizon algorithm engineering on hard optimization problems. 📅
- [AMA-Bench](https://github.com/AMA-Bench/AMA-Bench) ⭐36 — Benchmark for long-context retention and long-term memory in agent applications. 📅
- [An Interactive Benchmark for LLM Agents in Long-Context Software Engineering](https://arxiv.org/abs/2511.13998) — Interactive benchmark for LLM agents in long-context software engineering tasks.
- [Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios](https://arxiv.org/abs/2512.18470) — SWE-EVO: benchmark with 48 tasks for agents across multi-version software evolut. 📅
- [Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/html/2509.16941v1) — Benchmark of long-horizon SE tasks requiring hours-to-days effort and multi-file. 📅
- [Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](https://arxiv.org/abs/2604.24697) — Minecraft-based benchmark for evaluating causal discovery-to-application loop in. 📅
- [ClawGym: A Scalable Framework for Building Effective Claw Agents](https://arxiv.org/abs/2604.26904v1) — Scalable framework for building and evaluating claw-style SE agents with verifia.
- [ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworke](https://arxiv.org/abs/2604.23781) — Living-world benchmark for multi-turn, multi-day, multimodal coworker agents. 📅
- [EvoClaw: Evaluating AI Agents on Continuous Software Evolution](https://arxiv.org/abs/2603.13428) — Evaluates AI agents on continuous software evolution via milestone DAGs from com. 📅
- [frontier-swe](https://github.com/Proximal-Labs/frontier-swe) ⭐93 — Benchmarks coding agents on long-horizon impl, perf engineering, and ML tasks. 📅

### G–L

- [goodai-ltm-benchmark](https://github.com/GoodAI/goodai-ltm-benchmark) ⭐86 — Benchmark library for long-term memory and continual learning in LLM-based agent.
- [HARBOR: Automated Harness Optimization](https://arxiv.org/abs/2604.20938) — Optimizes benchmark harnesses for long-horizon LM agents via automated config se.
- [Hyper-multi-step: The Truth Behind Difficult Long-context Tasks](https://openreview.net/forum?id=LRPzo4jixx) — Analyzes difficulty of long-context tasks via multi-step reasoning in SE agent e.
- [LifelongAgentBench](https://github.com/caixd-220529/LifelongAgentBench) ⭐88 — Benchmark evaluating LLM agents as lifelong learners across tasks. 📅
- [LOCA-bench](https://arxiv.org/abs/2602.07962) — Evaluates agent performance degradation under dynamically growing context.
- [LoCoBench-Agent](https://github.com/SalesforceAIResearch/LoCoBench-Agent) ⭐19 — Long-context interactive benchmark for LLM agents on multi-turn code tasks.
- [LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Progra](https://arxiv.org/abs/2602.14337) — Benchmarks long-horizon CLI-based programming agents with fine-grained evaluatio. 📅
- [LongMemEval](https://arxiv.org/abs/2410.10813) — Benchmarks long-term memory recall in chat assistants across sessions.

### M–R

- [MemoryArena](https://arxiv.org/abs/2602.16313) — Evaluates agent memory across coupled multi-session tasks requiring recall.
- [METR's Autonomy Evaluation Resources](https://evaluations.metr.org/) — METR autonomy evaluation resources for long-horizon SE, ML, and cybersecurity ta. 📅
- [MirrorCode: Evidence AI can already do some weeks-long coding tasks](https://epoch.ai/blog/mirrorcode-preliminary-results) — MirrorCode benchmark: AI agents replicate 16k-line bioinformatics toolkit autono. 📅
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation](https://arxiv.org/html/2512.12730v1) — Benchmark for generating complete Python libraries from NL requirements. 📅 🐍
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding A](https://arxiv.org/abs/2512.12730) — Evaluates coding agents on full repository generation from natural language spec. 📅
- [Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks](https://arxiv.org/abs/2604.24964) — Web agent benchmark for realistic long-horizon, multi-site browsing tasks. 📅

### S–Z

- [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529v1) — Test-time compute scaling for long-horizon agentic coding tasks. 📅
- [SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents](https://arxiv.org/abs/2604.17308) — Benchmark for lifelong skill discovery, repair, and library maintenance in agent.
- [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterativ](https://arxiv.org/abs/2603.24755) — Benchmarks coding agent degradation over iterative tasks with 20 problems and 93. 📅
- [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://www.huggingface.co/papers/2603.24755) — Benchmarks code quality degradation in AI agents over iterative development task.
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) ⭐368 — Long-horizon SE task benchmark by Scale AI for multi-step complex engineering. 📅 🐍
- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/abs/2509.16941) — Benchmarks AI agents on 1865 long-horizon enterprise tasks from 41 repos. 📅
- [SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous In](https://arxiv.org/abs/2603.03823) — CI-cycle benchmark evaluating agents on codebase maintenance under requirement c. 📅
- [SWE-EVO](https://arxiv.org/html/2512.18470v2) — Benchmarks multi-step software evolution with 48 tasks across 7 OSS projects. 📅 🐍
- [SwingArena](https://github.com/menik1126/Swing-Bench) — Competitive arena for long-context GitHub issue solving with Elo ranking. 🏆
- [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) ⭐375 — GRPO training code for long-horizon terminal/coding tasks, top TerminalBench age. 📅

<a id="large-codebase"></a>
## Large Codebase / Multi-Repo

*Evaluates navigation and modification in large-scale repos (>50K LOC). Tests real-world scalability.*

- [Benchmarking Agentic Code Reasoning at the Repository Level](https://arxiv.org/html/2601.03731v1) — Benchmark for repository-level code reasoning in agentic LLMs.
- [CodeScaleBench](https://sourcegraph.com/blog) — Benchmarks agent navigation, comprehension, and modification in large multi-repo.
- [CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning](https://arxiv.org/abs/2506.00750) — Benchmark and dataset for evaluating code semantic reasoning capabilities.
- [ContextBench](https://arxiv.org/abs/2602.05892) — Evaluates how coding agents retrieve and use code context for issue resolution.
- [Continuous Benchmark Generation for Evaluating Enterprise-scale LLM Agents](https://arxiv.org/html/2511.10049) — Continuous benchmark generation process for evaluating enterprise-scale LLM agen.
- [CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completi](https://arxiv.org/abs/2310.11248) — Cross-file code completion benchmark across multiple languages. 🌐
- [DeepCodeBench: Real-World Codebase Understanding by Q&A Benchmarking](https://www.qodo.ai/blog/deepcodebench-real-world-codebase-understanding-by-qa-benchmarking/) — Q&A benchmark for real-world enterprise codebase understanding.
- [How to Understand Whole Software Repository?](https://www.semanticscholar.org/paper/19b825e139a54b543e7d8380ab0a1f9a7a29eaa2) — Benchmarks AI comprehension of whole software repositories via repo-level tasks.
- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Repository-Level Code Generation](https://doi.org/10.1109/ICSE55347.2025.00228) — Evolution-aware benchmark for realistic repo-level code generation evaluation.
- [legacy-bench](https://github.com/Factory-AI/legacy-bench) ⭐13 — Benchmarks AI agents on legacy software maintenance, comprehension, and migratio.
- [LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Softwar](https://arxiv.org/abs/2509.09614) — Benchmark for LLMs handling long-context complex software engineering tasks.
- [LongCodeBench: Evaluating Coding LLMs at 1M Context Windows](https://arxiv.org/abs/2505.07897) — Benchmark evaluating coding LLMs with 1M token context windows on long code task.
- [LONGCODEU: Benchmarking Long-Context Language Models on Long Code Understanding](https://arxiv.org/abs/2503.04359) — Benchmark for evaluating LLMs on long code understanding with long contexts.
- [Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository E](https://arxiv.org/abs/2603.27745) — Benchmarks AI agent maintainability in repo-level edits via probe-oracle framewo.
- [R2E: Turning any Github Repository into a Programming Agent Environment](https://www.semanticscholar.org/paper/2860bfaa9fa1d249c24aaf0981ad61bdbcd9c544) — Converts any GitHub repo into executable agent evaluation environment with tests.
- [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://arxiv.org/abs/2306.03091) — Benchmark for repo-level multi-file code auto-completion in Python and Java.
- [Repository-level Code Translation Benchmark Targeting Rust](https://arxiv.org/abs/2411.13990) — Repository-level code translation benchmark targeting Rust. 🦀
- [Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Transl](https://arxiv.org/abs/2501.16050) — Benchmark framework for evaluating code repository translation with fine-grained.
- [SWE Context Bench](https://arxiv.org/abs/2602.08316) — Benchmarks context reuse across related coding tasks in programming agents.
- [SWE-QA: A Dataset and Benchmark for Complex Code Understanding](https://arxiv.org/abs/2604.24814) — 9,072 MCQs from 12 Python repos evaluating multi-hop code understanding. 🐍
- [You make your evals, then your evals make you. Introducing AugmentQA](https://www.augmentcode.com/blog/you-make-your-evals-then-your-evals-make-you-introducing-augmentqa) — AugmentQA: internal benchmark for information retrieval quality in large codebas.

<a id="code-review"></a>
## Code Review

*Measures quality of review comments and suggestions. Emerging area with high practical value.*

- [aacr-bench](https://github.com/alibaba/aacr-bench) ⭐150 — Benchmarks automated code review across multi-language repositories with expert-. 🌐
- [AACR-Bench: Evaluating Automatic Code Review with Holistic Repository-Level Cont](https://arxiv.org/abs/2601.19494) — Benchmarks automatic code review using holistic repo-level context from PRs. 🌐
- [AUGER: automatically generating review comments with pre-training models](https://arxiv.org/abs/2208.08014) — Automated review comment generation using pre-training models.
- [Automatically Recommend Code Updates: Are We There Yet?](https://arxiv.org/abs/2209.07048) — Evaluates CodeLM-based code update recommendation on real-world tasks.
- [Automating code review activities by large-scale pre-training](https://arxiv.org/abs/2203.09095) — Pre-training model to automate code review activities in SE lifecycle.
- [Benchmarking and Studying the LLM-based Code Review](https://arxiv.org/abs/2509.01494) — Benchmarks LLM code review on 1000 human-verified GitHub PRs with project contex.
- [Benchmarking LLMs for Fine-Grained Code Review with Enriched Context in Practice](https://arxiv.org/abs/2511.07017) — Benchmarks LLMs on fine-grained code review with enriched semantic context.
- [Code Review Agent Benchmark](https://arxiv.org/html/2603.23448v1) — Evaluates code review agents on quality, accuracy, and actionability of comments. 🤖
- [CodeAgent: Autonomous Communicative Agents for Code Review](https://arxiv.org/abs/2402.02172) — Multi-agent LLM system for automated code review evaluation. 🤝
- [CodeCriticBench: A Holistic Code Critique Benchmark for Large Language Models](https://arxiv.org/abs/2502.16614) — Benchmarks LLM code critique on defect analysis, feedback, and review quality.
- [CodeFuse-CR-Bench](https://arxiv.org/abs/2509.14856) — Benchmarks end-to-end code review with comment generation and code revision.
- [CodeReviewer: Pre-Training for Automating Code Review Activities](https://www.semanticscholar.org/paper/b951c0691a0d2ca65202a1eed2ccedf6e305d035) — Pre-trained model and benchmark for automating code review activities.
- [CodeTaste: Can LLMs Generate Human-Level Code Refactorings?](https://arxiv.org/abs/2603.04177) — Benchmarks LLM ability to generate human-level code refactorings.
- [EvaCRC: Evaluating Code Review Comments](https://www.semanticscholar.org/paper/b13d4d943bf997d33fcc340f7a943e16ff563d1f) — Evaluates code review comment quality with interpretable conceptual model.
- [Exploring the Capabilities of LLMs for Code-Change-Related Tasks](https://arxiv.org/abs/2407.02824) — Benchmarks LLMs on code-change tasks including review and commit message generat.
- [Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical St](https://arxiv.org/abs/2309.08221) — Empirical study of ChatGPT on automated code refinement and review tasks.
- [Generation-based Code Review Automation: How Far Are We?](https://arxiv.org/abs/2303.07221) — Analyzes flawed metrics and dataset issues in generation-based code review autom.
- [Harnessing Large Language Models for Curated Code Reviews](https://arxiv.org/abs/2502.03425) — Benchmark for LLM-generated curated code review comments with quality filtering.
- [PatchTrack: A Comprehensive Analysis of ChatGPT's Influence on Pull Request Outc](https://arxiv.org/abs/2505.07700) — Analyzes ChatGPT's impact on 338 GitHub pull request review and integration outc.
- [RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review ](https://arxiv.org/abs/2601.01129) — Evaluates LLM-based code review quality at scale in Atlassian production. 🏭
- [The Right Prompts for the Job: Repair Code-Review Defects with Large Language Mo](https://arxiv.org/abs/2312.17485) — Benchmarks LLM prompt strategies for repairing code-review defects.
- [Towards Automating Code Review Activities](https://arxiv.org/abs/2101.02518) — Benchmarks automated code review with comment generation and revision recommenda.
- [Understanding Dominant Themes in Reviewing Agentic AI-authored Code](https://arxiv.org/abs/2601.19287) — Analyzes 19,450 review comments on agent-authored PRs with 12-theme taxonomy.
- [We benchmarked 7 AI code review tools on large open-source projects](https://www.augmentcode.com/blog/we-benchmarked-7-ai-code-review-tools-on-real-world-prs-here-are-the-results) — Benchmark of 7 AI code review tools on real-world PRs measuring precision and re.

<a id="testing"></a>
## Testing & QA

*Evaluates test generation, bug reproduction, and QA capabilities.*

### A–F

- [A Review of Large Language Models for Automated Test Case Generation](https://www.semanticscholar.org/paper/49c7ba3b6babda46a449850eb14be0ca04f3bc6d) — Review of LLM-based automated test case generation methods and effectiveness. 📋
- [ABTest: Behavior-Driven Testing for AI Coding Agents](https://arxiv.org/html/2604.03362v1) — Behavior-driven fuzzing framework generating repo-grounded tests for AI coding a.
- [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](https://arxiv.org/abs/2302.06527) — Empirical evaluation of LLMs for automated unit test generation at scale.
- [AssertionBench: A Benchmark to Evaluate Large-Language Models for Assertion Gene](https://arxiv.org/abs/2406.18627) — Benchmark evaluating LLMs on generating assertions for hardware/software verific.
- [Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Bas](https://arxiv.org/abs/2509.01616) — Generates issue-reproducing tests by combining LLMs with search-based testing.
- [Automated Unit Test Improvement using Large Language Models at Meta](https://arxiv.org/abs/2402.09171) — Industrial evaluation of TestGen-LLM for automated unit test improvement at Meta.
- [Automating a Complete Software Test Process Using LLMs: An Automotive Case Study](https://doi.org/10.1109/ICSE55347.2025.00211) — LLM-automated software test process evaluation in automotive case study.
- [BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmark](https://arxiv.org/abs/2604.24955) — Audits LLM agent benchmarks for spec flaws and overly strict evaluation. 🤖
- [Benchmarking LLMs for Unit Test Generation from Real-World Functions](https://arxiv.org/abs/2508.00408) — Benchmarks LLM unit test generation from real-world functions with contamination.
- [ChatUniTest: A Framework for LLM-Based Test Generation](https://arxiv.org/abs/2305.04764) — LLM-based automated unit test generation framework with adaptive strategies.
- [CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verifi](https://arxiv.org/abs/2502.08806) — Benchmarks test case generation for coverage and verification across 845 program.
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generat](https://arxiv.org/abs/2604.12268) — Benchmarks LLM ability to generate executable behavioral specs with pre/postcond.
- [Comprehend, Imitate, and then Update: Unleashing the Power of LLMs in Test Suite Evolution](https://www.semanticscholar.org/paper/914a407f6a53c0f48a2f152fd677d3ed524b3c66) — LLM-based approach for automated test suite evolution and obsolete test update.
- [Echo: Graph-Enhanced Retrieval and Execution Feedback for Issue Reproduction Tes](https://arxiv.org/abs/2603.07326) — Generates issue reproduction tests via graph-enhanced retrieval and execution fe.
- [Evaluating and Improving ChatGPT for Unit Test Generation](https://www.semanticscholar.org/paper/49c58278c069faaea0cdee4df9043015493bc854) — Evaluates and improves ChatGPT for unit test generation quality.

### G–L

- [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and](https://arxiv.org/abs/2508.06365) — Generates SWE-Bench reproduction tests via heterogeneous prompting and execution.
- [iCoRe: An Iterative Correlation-Aware Retriever for Bug Reproduction Test Generation](https://arxiv.org/abs/2604.19224) — Iterative retrieval method for generating bug reproduction tests from issue desc.
- [Investigating Test Overfitting on SWE-bench](https://arxiv.org/abs/2511.16858) — Studies test overfitting on SWE-bench where agents pass tests but miss scenarios.
- [Issue2Test: Generating Reproducing Test Cases from Issue Reports](https://arxiv.org/abs/2503.16320) — Generates reproducing test cases from GitHub issue reports to validate fixes.
- [Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Repr](https://arxiv.org/abs/2209.11515) — LIBRO: LLM few-shot bug reproduction test generation from bug reports.

### M–R

- [MAGISTER: LLM-Based Test Generation with Role-Specialized Agents](https://www.semanticscholar.org/paper/874cbcf924bc4efc303582eae92e8ff438a3c1a8) — Multi-agent LLM system with role-specialized agents for automated unit test gene. 🤝
- [MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact ](https://arxiv.org/abs/2502.06556) — Benchmarks multi-file unit test generation across 3 languages and 20 projects. 🌐
- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](https://doi.org/10.1109/ICSE55347.2025.00226) — LLM agent approach to repair non-idempotent-outcome tests.
- [No More Manual Tests? Evaluating and Improving ChatGPT for Unit Test Generation](https://arxiv.org/abs/2305.04207) — Evaluates ChatGPT for unit test generation quality and coverage.
- [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](https://arxiv.org/abs/2304.11686) — Differential prompting to guide ChatGPT in generating failure-inducing test case.
- [Otter: Generating Tests from Issues to Validate SWE Patches](https://arxiv.org/abs/2502.05368) — Generates test cases from issue descriptions to validate SWE agent patches.
- [RESTestBench: A Benchmark for Evaluating the Effectiveness of LLM-Generated REST](https://arxiv.org/abs/2604.25862v1) — Benchmark for LLM-generated REST API test cases using mutation analysis.

### S–Z

- [Software Testing With Large Language Models: Survey, Landscape, and Vision](https://arxiv.org/abs/2307.07221) — Survey of LLMs applied to software testing tasks, landscape and vision. 📋
- [SWE-Tester: Training Open-Source LLMs for Issue Reproduction in Real-World Repos](https://arxiv.org/abs/2601.13713) — Trains open-source LLMs to generate issue-reproducing tests from bug reports.
- [SWT-Bench](https://github.com/logic-star-ai/SWT-Bench) ⭐76 — Benchmark for generating valid test cases for real bug fixes, built on SWE-bench. 🐍
- [TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance](https://arxiv.org/abs/2601.18241) — Benchmark evaluating LLMs on unit test maintenance: creation, repair, and update.
- [TestCase-Eval: Can LLMs Generate High-Quality Test Cases for Algorithm Problems?](https://arxiv.org/html/2506.12278v1) — Benchmark evaluating fault coverage of LLM-generated test cases for algorithm pr.
- [TestDecision: Sequential Test Suite Generation via Greedy Optimization and Reinforcement Learning](https://arxiv.org/abs/2604.01799) — Sequential test suite generation using greedy optimization and RL with open-sour.
- [TESTEVAL: Benchmarking Large Language Models for Test Case Generation](https://arxiv.org/abs/2406.04531) — Benchmark comparing LLMs on test case generation across correctness and coverage.
- [TestExplora: Benchmarking LLMs for Proactive Bug Discovery via Repository-Level Test Generation](https://arxiv.org/abs/2602.10471) — Benchmark for LLMs on proactive bug discovery via repo-level test generation.
- [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://arxiv.org/abs/2410.00752) — Benchmarks unit test generation and test completion on real-world open-source pr. 🌍
- [Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality](https://arxiv.org/abs/2603.13724) — Analyzes AI agent test generation frequency, quality, and coverage vs human-writ.
- [UTBoost](https://github.com/CUHK-Shenzhen-SE/UTBoost) ⭐36 — Augments SWE-Bench with auto-generated unit tests to mitigate false positives.
- [When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resol](https://arxiv.org/abs/2510.18270) — Evaluates impact of regression tests on SWE issue resolution and test generation.

<a id="security"></a>
## Security & Vulnerability

*Benchmarks for vulnerability detection, secure code generation, and penetration testing.*

### A–F

- [A User-Centered Security Evaluation of Copilot](https://arxiv.org/abs/2308.06587) — Evaluates security of GitHub Copilot-generated code via user-centered study. 🔒
- [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](https://arxiv.org/abs/2508.18106) — Repository-level benchmark evaluating security of AI-generated code. 🔒
- [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://openreview.net/forum?id=V4y0CpX4hK) — Formalizes and benchmarks attacks and defenses in LLM-based agents. 🔒
- [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilitie](https://arxiv.org/abs/2601.19138) — Benchmarks agentic secure code review for pre-commit vulnerability detection. 🔒
- [AICGSecEval](https://github.com/Tencent/AICGSecEval) ⭐965 — Repo-level benchmark for detecting security vulnerabilities in AI-generated code.
- [aicrypto-agent](https://github.com/wangyu-ovo/aicrypto-agent) ⭐30 — Benchmark evaluating LLM cryptography capabilities for AI SE agents. 🔒
- [Asleep at the Keyboard? Assessing the Security of GitHub Copilot’s Code Contributions](https://arxiv.org/abs/2108.09293) — Evaluates security vulnerabilities in GitHub Copilot's auto-generated code. 🔒
- [Assessing the Security of GitHub Copilot's Generated Code - A Targeted Replication Study](https://arxiv.org/abs/2311.11177) — Replication study assessing security vulnerabilities in GitHub Copilot generated. 🔒
- [auto-pen-bench](https://github.com/lucagioacchini/auto-pen-bench) ⭐82 — Benchmarks generative agents on automated penetration testing scenarios. 🔒
- [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) — Bootstraps code security benchmarks to evaluate LLM-generated code safety. 🔒
- [Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858) — Trajectory-level safety evaluation benchmarks for agent systems in Claw and Code.
- [BinMetric: A Comprehensive Binary Analysis Benchmark for Large Language Models](https://arxiv.org/abs/2505.07360) — Comprehensive benchmark evaluating LLMs on binary analysis tasks for software se. 🔒
- [Constrained Decoding for Secure Code Generation](https://arxiv.org/abs/2405.00218) — Benchmark measuring correctness+security of LLM-generated code with constrained . 🔒
- [CS-Eval: A Comprehensive Large Language Model Benchmark for CyberSecurity](https://arxiv.org/abs/2411.16239) — Comprehensive bilingual LLM benchmark for cybersecurity tasks evaluation. 🔒
- [CVE-Bench](https://github.com/WhileBug/CVEBench) ⭐4 — Evaluates agents on understanding and fixing real CVE vulnerabilities. 🔒 🌐
- [CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Applicat](https://arxiv.org/abs/2503.17332) — Benchmarks AI agents on exploiting real-world CVE web vulnerabilities. 🔒 🌍
- [cybergym](https://github.com/sunblaze-ucb/cybergym) ⭐279 — Benchmarks AI agents on real-world vulnerability analysis at scale.
- [CyberGym: Evaluating AI Agents'Real-World Cybersecurity Capabilities at Scale](https://arxiv.org/abs/2506.02548) — Benchmarks cybersecurity agents on 1,507 real vulnerabilities across 188 project. 🔒 📦
- [CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities](https://arxiv.org/abs/2408.01605) — Benchmark suite evaluating cybersecurity risks and capabilities in LLMs. 🔒
- [Dynamic Cyber Ranges](https://arxiv.org/abs/2604.24184) — Dynamic Cyber Ranges for evaluating LLM-driven APT agents beyond static CTF benc.
- [Evaluating Large Language Models for Real-World Vulnerability Repair in C/C++ Co](https://www.semanticscholar.org/paper/db82597561835e151c417f7272455caa4d1a9d04) — Dataset of 223 real C/C++ memory corruption vulns to evaluate LLM repair ability. 🔒

### G–L

- [HackSynth](https://github.com/aielte-research/HackSynth) ⭐303 — Evaluates LLM agents on autonomous penetration testing via CTF challenges.
- [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://arxiv.org/abs/2405.17238) — LLM-assisted static analysis approach for detecting security vulnerabilities. 🔒
- [Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-](https://arxiv.org/abs/2512.03262) — Benchmarks vulnerability risk in agent-generated code across 200 real-world vibe. 🔒
- [JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/abs/2506.20170) — Benchmark for evaluating LLMs on JavaScript deobfuscation tasks. 🟨 🔒
- [Just another copy and paste? Comparing the security vulnerabilities of ChatGPT generated code and StackOverflow answers](https://arxiv.org/abs/2403.15600) — Compares security vulnerabilities in ChatGPT-generated code vs StackOverflow ans. 🔒
- [Large Language Models for Code: Security Hardening and Adversarial Testing](https://arxiv.org/abs/2302.05319) — Security hardening and adversarial testing evaluation of LLMs generating secure . 🔒
- [LLM Security Guard for Code](https://arxiv.org/abs/2405.01103) — Benchmarks LLM-generated code security using static analyzers and vulnerability . 🔒
- [LLMSecEval: A Dataset of Natural Language Prompts for Security Evaluations](https://arxiv.org/abs/2303.09384) — NL prompts based on CWE scenarios to evaluate security of LLM-generated code. 🔒
- [LogicEval: A Systematic Framework for Evaluating Automated Repair Techniques for](https://arxiv.org/abs/2604.12994) — Evaluates automated repair techniques on real-world software logic vulnerabiliti. 🔒

### M–R

- [MaliciousAgentSkillsBench](https://github.com/protectskills/MaliciousAgentSkillsBench) ⭐39 — Evaluates agent resilience against malicious skill injection scenarios. 🔒
- [MOCHA: Are Code Language Models Robust Against Multi-Turn Malicious Coding Prompts?](https://arxiv.org/abs/2507.19598) — Multi-turn adversarial coding prompt benchmark evaluating LLM robustness. 🔒
- [Multitask-Based Evaluation of Open-Source LLM on Software Vulnerability](https://arxiv.org/abs/2404.02056) — Multi-task evaluation of LLMs on software vulnerability using Big-Vul dataset. 🔒
- [OS-Sentinel](https://github.com/OS-Copilot/OS-Sentinel) ⭐47 — Benchmarks mobile GUI agent safety with hybrid validation for unsafe actions.
- [PentestGPT: An LLM-empowered Automatic Penetration Testing Tool](https://arxiv.org/abs/2308.06782) — Benchmarks LLM-driven automated penetration testing on real targets. 🔒
- [RealVuln: Benchmarking Rule-Based, General-Purpose LLM, and Security-Specialized](https://arxiv.org/abs/2604.13764) — Benchmarks 15 vulnerability scanners on 26 Python repos with 796 annotations. 🐍
- [RedCode](https://github.com/AI-secure/RedCode) ⭐75 — Benchmark for risky code execution and generation by code agents. 🔒
- [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781) — Benchmark for evaluating safety risks in code execution and generation by code a. 🔒
- [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](https://arxiv.org/abs/2409.15154) — Benchmark evaluating LLM resistance to generating malicious code. 🔒
- [Running in CIRCLE? A Simple Benchmark for LLM Code Interpreter Security](https://arxiv.org/abs/2507.19399) — Benchmark for evaluating security of LLM code interpreter environments. 🔒

### S–Z

- [SafeGenBench: A Benchmark Framework for Security Vulnerability Detection in LLM-](https://arxiv.org/abs/2506.05692) — Benchmark for detecting security vulnerabilities in LLM-generated code. 🔒
- [scabench](https://github.com/scabench-org/scabench) ⭐110 — Benchmark for AI security audit agents on SCA and vulnerability detection tasks. 🔒
- [SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security ](https://arxiv.org/abs/2506.11791) — Benchmark of LLM agents on real-world software security tasks. 🔒 🌍
- [SecBench: A Comprehensive Multi-Dimensional Benchmarking Dataset for LLMs in Cyb](https://arxiv.org/abs/2412.20787) — Multi-dimensional benchmarking dataset for evaluating LLMs in cybersecurity. 🔒
- [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing](https://arxiv.org/abs/2509.22097) — Benchmarks secure vibe-coding of AI agents on 105 C/C++ vulnerability tasks. 🔒
- [SecurityEval dataset: mining vulnerability examples to evaluate machine learning](https://www.semanticscholar.org/paper/71280dba5bda65c162f9deaffed7d3d20692ca0a) — Evaluates ML code generation security using real-world vulnerability samples. 🔒
- [Towards Agentic Investigation of Security Alerts](https://arxiv.org/abs/2604.25846) — Agentic LLM workflow for automated security alert investigation over log sources. 🔒
- [VADER: A Human-Evaluated Benchmark for Vulnerability Assessment, Detection, Expl](https://arxiv.org/abs/2505.19395) — Human-evaluated benchmark for vulnerability assessment, detection, explanation, . 🔒 👤

<a id="production"></a>
## Production-Derived

- [A Production-Derived Benchmark for Evaluating AI Coding Agents](https://arxiv.org/html/2604.01527v1) — Production-derived benchmark for evaluating AI coding agents in industrial setti. 🏭
- [Bots Don’t Mind Waiting, Do They? Comparing the Interaction With Automatically and Manually Created Pull Requests](https://arxiv.org/abs/2103.03591) — Compares acceptance and wait time of bot vs human pull requests in OSS projects.
- [CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs](https://arxiv.org/abs/2506.11059) — Multi-lingual benchmark for detecting AI-generated and paraphrased source code. 🌐
- [CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend](https://arxiv.org/abs/2604.23455) — Benchmark for LLM-agent cross-modal failure diagnosis combining browser and back.
- [From Translation to Superset: Benchmark-Driven Evolution of a Production AI Agent from Rust to Python](https://arxiv.org/abs/2604.11518v1) — Benchmark-driven LLM-assisted Rust-to-Python translation evaluation on 648K LOC . 🏭 🦀 🐍
- [Hot Fixing in the Wild](https://arxiv.org/abs/2604.26892v1) — Large-scale study of hot fixes in 61k GitHub repos in the era of AI coding agent. 🏭
- [LinuxArena: A Control Setting for AI Agents in Live Production Software Environm](https://arxiv.org/abs/2604.15384) — Benchmarks AI agent control in 20 live Linux environments with 1671 tasks and 18. 🏭
- [Production-Derived Benchmark](https://arxiv.org/html/2604.01527v2) — Benchmarks agent engineering capability on tasks derived from real production en. 🏭 🌍
- [Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Progr](https://arxiv.org/abs/2210.14306) — Models programmer interaction behaviors and cognitive costs with AI coding assis.
- [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779) — Real-world coding agent conversation dataset with 6K sessions and 355K tool call. 🌍
- [SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Work](https://arxiv.org/abs/2511.06090) — Benchmarks LLM code optimization on 498 tasks across 9 data-science/ML/HPC repos.
- [SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositori](https://arxiv.org/abs/2507.12415) — Benchmark for code performance optimization on real-world repos.

<a id="code-generation"></a>
## Code Generation

### A–F

- [A Closer Look at Different Difficulty Levels Code Generation Abilities of ChatGPT](https://www.semanticscholar.org/paper/f1847504a4895a3d31c31e7464e5b34d9eda8ef8) — Evaluates ChatGPT code generation across difficulty levels using benchmarks.
- [A Large-scale Class-level Benchmark Dataset for Code Generation with LLMs](https://arxiv.org/abs/2504.15564) — Large-scale class-level benchmark dataset for evaluating LLM code generation.
- [Agents4PLC: Automating Closed-loop PLC Code Generation and Verification in Indus](https://arxiv.org/abs/2410.14209) — Benchmark for LLM-based agents generating and verifying PLC code in industrial c.
- [ai-coding-lang-bench](https://github.com/mame/ai-coding-lang-bench) ⭐151 — Benchmarks AI code generation across 13 programming languages. 🌐
- [An Empirical Evaluation of GitHub Copilot's Code Suggestions](https://www.semanticscholar.org/paper/cdfe9580f63070f311151444f9df32818cc858bf) — Empirical study evaluating correctness and understandability of GitHub Copilot c.
- [ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evalu](https://arxiv.org/abs/2507.04952) — Benchmark for evaluating LLM code generation of visual and interactive artifacts.
- [Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation](https://arxiv.org/abs/2604.21505) — Benchmark studying how requirement ambiguity affects LLM function-level code gen.
- [AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators](https://arxiv.org/abs/2508.09101) — LLM-based automatic generation of code benchmarks for evaluating coding ability.
- [BaxBench: Can LLMs Generate Correct and Secure Backends?](https://arxiv.org/abs/2502.11844) — Evaluates LLM ability to generate correct and secure backend modules. 🔒
- [Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Lan](https://arxiv.org/abs/2407.11470) — Benchmark evaluating code generation across multiple quality dimensions beyond c.
- [Beyond Output Correctness: Benchmarking and Evaluating Large Language Model Reas](https://arxiv.org/abs/2604.12379) — Benchmarks LLM reasoning quality across code generation and summarization tasks. 🔍
- [bigcodebench](https://github.com/bigcode-project/bigcodebench) ⭐499 — Benchmarks LLMs on complex function calls, tool use, and instruction following.
- [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Compl](https://arxiv.org/abs/2406.15877) — Benchmarks code generation with diverse function calls and complex instructions.
- [CETBench: A Novel Dataset constructed via Transformations over Programs for Benchmarking LLMs for Code-Equivalence Checking](https://arxiv.org/abs/2506.04019) — Dataset benchmarking LLMs on code-equivalence checking via program transformatio.
- [ClassEval-Pro: A Cross-Domain Benchmark for Class-Level Code Generation](https://arxiv.org/abs/2604.26923v1) — Cross-domain benchmark for class-level compositional code generation evaluation.
- [ClassEval: A Manually-Crafted Benchmark for Evaluating LLMs on Class-level Code Generation](https://arxiv.org/abs/2308.01861) — Class-level Python code generation benchmark with 100 tasks evaluating 11 LLMs. 🐍
- [Co-Located Tests, Better AI Code: How Test Syntax Structure Affects Foundation Model Code Generation](https://arxiv.org/abs/2604.19826) — Empirical study on how test co-location syntax affects AI code generation qualit.
- [CoCo-Bench: A Comprehensive Code Benchmark For Multi-task Large Language Model E](https://arxiv.org/abs/2504.20673) — Comprehensive multi-task code benchmark for evaluating LLMs across coding tasks.
- [CoCoNUT: Structural Code Understanding does not fall out of a tree](https://arxiv.org/abs/2501.16456) — Benchmarks LLM structural code understanding beyond surface-level generation.
- [Code-Vision: Evaluating Multimodal LLMs Logic Understanding and Code Generation Capabilities](https://arxiv.org/abs/2502.11829) — Benchmark evaluating multimodal LLMs on code generation from flowcharts.
- [CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real](https://arxiv.org/abs/2401.07339) — Repo-level code generation benchmark for tool-integrated agent systems.
- [CodeBenchGen: Creating Scalable Execution-based Code Generation Benchmarks](https://arxiv.org/abs/2404.00566) — Framework for automatically creating execution-based code generation benchmarks.
- [CodeFlowBench: A Multi-turn, Iterative Benchmark for Complex Code Generation](https://arxiv.org/abs/2504.21751) — Multi-turn iterative benchmark for evaluating complex code generation tasks.
- [codefuse-evaluation](https://github.com/codefuse-ai/codefuse-evaluation) ⭐109 — Benchmarks code LLMs on generation, translation, commenting, and repo-level comp.
- [CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Benchmarking on HumanEval-X](https://arxiv.org/abs/2303.17568) — HumanEval-X multilingual benchmark for code generation evaluation. 🌐
- [CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixe](https://arxiv.org/abs/2505.05063) — Benchmark evaluating LLMs on code generation from code-mixed (multilingual) prom. 🌐
- [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities o](https://arxiv.org/abs/2410.01999) — Multi-task benchmark evaluating code understanding capabilities of code LLMs.
- [CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained ](https://arxiv.org/abs/2302.00288) — Benchmark for pragmatic code generation evaluating generative pre-trained models.
- [CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark ](https://arxiv.org/abs/2311.08588) — Execution-based multilingual multitask benchmark for LLM code understanding and . 🌐
- [CodeUpdateArena: Benchmarking Knowledge Editing on API Updates](https://arxiv.org/abs/2407.06249) — Benchmark for evaluating LLM code generation after API updates.
- [CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation](https://arxiv.org/abs/2102.04664) — Multi-task benchmark with 10 SE tasks across 14 datasets for code understanding/.
- [Collu-Bench: A Benchmark for Predicting Language Model Hallucinations in Code](https://arxiv.org/abs/2410.09997) — Benchmark for predicting language model hallucinations in generated code.
- [Competition-Level Code Generation with AlphaCode](https://arxiv.org/abs/2203.07814) — AlphaCode: large-scale code generation evaluated on competitive programming task.
- [Competition-Level Problems are Effective LLM Evaluators](https://arxiv.org/abs/2312.02143) — Evaluates LLM reasoning via recent Codeforces competition problems to avoid data.
- [ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Co](https://arxiv.org/abs/2409.10280) — Benchmarks code models on complex generation, completion, summarization, and API.
- [ConvCodeWorld: Benchmarking Conversational Code Generation in Reproducible Feedback Environments](https://openreview.net/forum?id=rpouyo09V0) — Benchmark for conversational code generation with reproducible feedback environm.
- [CrossCodeEval: Multilingual Repository-Level Code Completion Benchmark](https://crosscodeeval.github.io/) — Multilingual repo-level code completion benchmark with cross-file dependency eva. 🌐
- [CRUST-Bench: A Comprehensive Benchmark for C-to-safe-Rust Transpilation](https://arxiv.org/abs/2504.15254) — Benchmark for evaluating C-to-safe-Rust transpilation by AI agents. 🦀
- [CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution](https://arxiv.org/abs/2401.03065) — Benchmark testing LLM code reasoning, understanding, and execution capabilities.
- [da-code](https://github.com/yiyihum/da-code) ⭐95 — Benchmarks agent code generation on real-world data science tasks.
- [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](https://arxiv.org/abs/2410.07331) — Benchmark for evaluating LLM code generation in data science tasks.
- [Defective Task Descriptions in LLM-Based Code Generation: Detection and Analysis](https://arxiv.org/abs/2604.24703) — Analyzes defective task descriptions in LLM code generation and builds a defect .
- [Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Eng](https://arxiv.org/abs/2403.03163) — Benchmark for multimodal code generation converting UI designs to front-end code.
- [DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation](https://arxiv.org/abs/2506.06251) — Benchmark for evaluating multimodal LLMs on front-end code generation tasks.
- [DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-World ](https://arxiv.org/abs/2405.19856) — Manually-annotated code generation benchmark aligned with real-world repositorie. 🌍
- [Drawing Pandas: A Benchmark for LLMs in Generating Plotting Code](https://arxiv.org/abs/2412.02764) — Benchmark for evaluating LLMs on generating data visualization plotting code.
- [DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501) — Benchmark of 1000 data science code generation problems from StackOverflow. 🐍
- [DS-Bench: A Realistic Benchmark for Data Science Code Generation](https://arxiv.org/abs/2505.15621) — Benchmark for evaluating code generation on realistic data science tasks.
- [DyCodeEval: Dynamic Benchmarking of Reasoning Capabilities in Code Large Languag](https://arxiv.org/abs/2503.04149) — Dynamic benchmark addressing data contamination in code LLM reasoning evaluation.
- [DynaCode: A Dynamic Complexity-Aware Code Benchmark for Evaluating Large Languag](https://arxiv.org/abs/2503.10452) — Dynamic complexity-aware benchmark for evaluating LLMs on code generation.
- [Dynamic Benchmark Construction for Evaluating Large Language Models on Real-Worl](https://arxiv.org/abs/2508.07180) — Dynamic benchmark construction to evaluate LLMs on real-world code tasks. 🌍
- [ECCO: Can We Improve Model-Generated Code Efficiency Without Sacrificing Functional Correctness?](https://arxiv.org/abs/2407.14044) — Benchmark evaluating LLM-generated code efficiency vs functional correctness.
- [EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits](https://arxiv.org/abs/2511.04486) — Benchmarks LLM instructed code editing on 540 real-world edit tasks. 🌍
- [EFFIBENCH-X:A Multi-Language Benchmark fo rMeasuring Effciency ofLLM.Generated C](https://arxiv.org/abs/2505.13004) — Multi-language benchmark measuring efficiency of LLM-generated code. 🌐
- [EffiBench: Benchmarking the Efficiency of Automatically Generated Code](https://arxiv.org/abs/2402.02037) — Benchmark evaluating efficiency of LLM-generated code beyond correctness.
- [ELABORATION: A Comprehensive Benchmark on Human-LLM Competitive Programming](https://arxiv.org/abs/2505.16667) — Benchmark comparing human and LLM performance on competitive programming tasks.
- [Enhancing Repository-Level Code Generation with Integrated Contextual Informatio](https://arxiv.org/abs/2406.03283) — Evaluates repo-level code generation with integrated contextual information.
- [Escalating LLM-based Code Translation Benchmarking into the Class-level Era](https://arxiv.org/abs/2411.06145) — Class-level code translation benchmark escalating evaluation beyond function-lev.
- [eval-dev-quality](https://github.com/symflower/eval-dev-quality) ⭐185 — Evaluates LLM code generation quality across multiple languages and tasks. 🌐
- [Evaluating Language Models for Efficient Code Generation](https://arxiv.org/abs/2408.06450) — Benchmark evaluating LLMs on generating efficient code beyond correctness.
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — Evaluates LLM code generation correctness via pass@k on HumanEval benchmark.
- [Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks](https://arxiv.org/abs/2403.04814) — Syntax-aware fill-in-the-middle benchmark for LLMs across multiple languages.
- [EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code](https://arxiv.org/abs/2404.00599) — Evolving code generation benchmark aligned with real-world code repositories. 🌍
- [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluat](https://arxiv.org/abs/2410.22821) — Evolving code generation benchmark mitigating data leakage with domain-specific .
- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) — Proposes executable Python code actions for LLM agents with evaluation benchmark.
- [Exploring Language Model's Code Generation Ability with Auxiliary Functions](https://arxiv.org/abs/2403.10575) — Benchmark evaluating LLM code generation with auxiliary/helper function usage.
- [FrontendBench: A Benchmark for Evaluating LLMs on Front-End Development via Auto](https://arxiv.org/abs/2506.13832) — Benchmark for evaluating LLMs on front-end development with auto evaluation.

### G–L

- [GitChameleon: Unmasking the Version-Switching Capabilities of Code Generation Mo](https://arxiv.org/abs/2411.05830) — Benchmark testing LLM ability to generate code for specific library versions.
- [Github](https://github.com/openai/human-eval) — HumanEval: OpenAI benchmark for evaluating code generation from docstrings. 🐍
- [How Efficient is LLM-Generated Code? A Rigorous & High-Standard Benchmark](https://arxiv.org/abs/2406.06647) — Benchmark measuring efficiency of LLM-generated code with rigorous evaluation.
- [HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self-invoking Co](https://arxiv.org/abs/2412.21199) — HumanEval Pro & MBPP Pro benchmarks for self-invoking code generation by LLMs.
- [HumanEval-V: Benchmarking High-Level Visual Reasoning with Complex Diagrams in C](https://arxiv.org/abs/2410.12381) — Benchmark for code generation from complex visual diagrams requiring high-level .
- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Reposito](https://arxiv.org/abs/2406.06918) — Evolution-aware benchmark for realistic repo-level code generation over project .
- [ICPC-Eval: Probing the Frontiers of LLM Reasoning with Competitive Programming C](https://arxiv.org/abs/2506.04894) — Benchmark using ICPC competitive programming problems to evaluate LLM reasoning.
- [IFEvalCode: Controlled Code Generation](https://arxiv.org/abs/2507.05269) — Benchmark for evaluating LLM code generation under controlled instruction constr.
- [IndustryCode: A Benchmark for Industry Code Generation](https://arxiv.org/abs/2604.02729) — Benchmarks multi-domain multi-language code generation for finance, automation, . 🌐
- [InfiBench: Evaluating the Question-Answering Capabilities of Code Large Language](https://arxiv.org/abs/2404.07940) — Benchmark evaluating question-answering capabilities of code LLMs.
- [Interaction2Code: Benchmarking MLLM-based Interactive Webpage Code Generation from Interactive Prototyping](https://arxiv.org/abs/2411.03292) — Benchmark for MLLM-based interactive webpage code generation from UI prototypes.
- [Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large L](https://arxiv.org/abs/2305.01210) — Augments HumanEval/MBPP tests to rigorously evaluate LLM code correctness.
- [JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models](https://arxiv.org/abs/2406.12902) — Java OOP code generation benchmark evaluating LLMs at class/project granularity. ☕
- [L2CEval: Evaluating Language-to-Code Generation Capabilities of Large Language M](https://arxiv.org/abs/2309.17446) — Benchmark evaluating language-to-code generation capabilities of LLMs.
- [LeetCodeDataset: A Temporal Dataset for Robust Evaluation and Efficient Training](https://arxiv.org/abs/2504.14655) — Temporal LeetCode dataset for evaluating and training code LLMs.
- [LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://arxiv.org/abs/2412.04478) — Benchmark for generating code targeting specific library versions.
- [LiCoEval: Evaluating LLMs on License Compliance in Code Generation](https://arxiv.org/abs/2408.02487) — Benchmark evaluating LLM compliance with open-source license terms during code g.
- [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) ⭐854 — Continuously updated competitive programming benchmark to prevent data contamina.
- [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code C](https://arxiv.org/abs/2406.09834) — Evaluates LLM code completion for deprecated API usage during library evolution.

### M–R

- [M2rc-Eval: Massively Multilingual Repository-level Code Completion Evaluation](https://arxiv.org/abs/2410.21157) — Multilingual repo-level code completion benchmark spanning many languages. 🌐
- [MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visual](https://arxiv.org/abs/2402.11453) — Benchmark and method for evaluating LLM agents on scientific data visualization.
- [MCoNaLa: A Benchmark for Code Generation from Multiple Natural Languages](https://arxiv.org/abs/2203.08388) — Benchmark for code generation from multilingual natural language intents. 🌐
- [Measuring Coding Challenge Competence With APPS](https://arxiv.org/abs/2105.09938) — APPS benchmark for measuring code generation on coding challenges.
- [Measuring The Impact Of Programming Language Distribution](https://arxiv.org/abs/2302.01973) — BabelCode framework for execution-based code eval across multiple programming la. 🌐
- [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://arxiv.org/abs/2402.07844) — Benchmark evaluating code efficiency of LLM-generated solutions beyond correctne.
- [ML-Bench](https://github.com/gersteinlab/ML-Bench) ⭐316 — Evaluates LLM/agent ML task completion on 10K+ samples across 18 GitHub repos.
- [MMCode: Benchmarking Multimodal Large Language Models for Code Generation with V](https://arxiv.org/abs/2404.09486) — Benchmark for code generation from visually rich problems using multimodal LLMs.
- [Multi-lingual Evaluation of Code Generation Models](https://arxiv.org/abs/2210.14868) — Multi-lingual code generation benchmarks (MBXP, Multilingual HumanEval, MathQA-X. 🌐
- [Multilingual Multimodal Software Developer for Code Generation](https://arxiv.org/abs/2507.08719) — Multilingual multimodal benchmark for evaluating code generation agents. 🌐
- [MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation](https://arxiv.org/abs/2208.08227) — Multi-language code generation benchmark translating unit-test-driven tasks to 1. 🌐
- [Natural Language to Code Generation in Interactive Data Science Notebooks](https://arxiv.org/abs/2212.09248) — ARCADE: 1078 NL-to-code benchmark for pandas tasks in Jupyter notebooks.
- [nl2code-dataset](https://github.com/aixcoder-plugin/nl2code-dataset) ⭐51 — Aix-bench: natural language to Java code synthesis evaluation benchmark dataset. ☕
- [No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by Ch](https://arxiv.org/abs/2308.04838) — Assesses ChatGPT code generation quality across correctness, complexity, and sec. 🔒
- [NoFunEval: Funny How Code LMs Falter on Requirements Beyond Functional Correctne](https://arxiv.org/abs/2401.15963) — Benchmarks code LMs on non-functional requirements: efficiency, security, mainta. 🔒
- [OJBench: A Competition Level Code Benchmark For Large Language Models](https://arxiv.org/abs/2506.16395) — Competition-level code generation benchmark for LLMs from online judges.
- [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](https://arxiv.org/abs/2308.08961) — Taxonomy and benchmark for evaluating neural code translation models.
- [OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2401.06628) — Benchmark evaluating LLMs on object-oriented programming tasks.
- [PlayCoder: Making LLM-Generated GUI Code Playable](https://arxiv.org/abs/2604.19742) — Benchmarks LLM-generated GUI apps on event-driven interaction and state correctn.
- [Plot2Code: A Comprehensive Benchmark for Evaluating Multi-modal Large Language Models in Code Generation from Scientific Plots](https://arxiv.org/abs/2405.07990) — Benchmark evaluating MLLMs on generating executable code from scientific plots.
- [PPM: Automated Generation of Diverse Programming Problems for Benchmarking Code ](https://arxiv.org/abs/2401.15545) — Automated generation of diverse programming problems for benchmarking code gen m.
- [Python Code Generation by Asking Clarification Questions](https://arxiv.org/abs/2212.09885) — Benchmark for Python code generation with clarification question asking. 🐍
- [QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models](https://arxiv.org/abs/2604.15151) — Evaluates LLM quantitative trading strategy code generation with backtesting.
- [React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native](https://arxiv.org/abs/2604.17187) — Evaluates 5 open-weights coding models on React Native app generation on GH200 h.
- [ReCode: Robustness Evaluation of Code Generation Models](https://arxiv.org/abs/2212.10264) — Robustness evaluation benchmark for code generation models via perturbations.
- [ReCUBE: Evaluating Repository-Level Context Utilization in Code Generation](https://arxiv.org/abs/2603.25770) — Evaluates LLM cross-file context utilization in repo-level code generation.
- [Refining ChatGPT-Generated Code: Characterizing and Mitigating Code Quality Issues](https://arxiv.org/abs/2307.12596) — Characterizes and mitigates code quality issues in ChatGPT-generated code.
- [RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark](https://arxiv.org/html/2406.11927v2) — Repo-level executable benchmark for code generation with automated test-based ev.
- [ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Rese](https://arxiv.org/abs/2506.02314) — Benchmark for LLMs implementing novel ML research code from papers.
- [RTLLM: An Open-Source Benchmark for Design RTL Generation with Large Language Model](https://arxiv.org/abs/2308.05345) — Benchmark for RTL hardware design generation from natural language using LLMs.
- [RustEvo2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generat](https://arxiv.org/abs/2503.16922) — Evolving benchmark for evaluating LLM Rust code generation under API changes. 🦀

### S–Z

- [Self-Edit: Fault-Aware Code Editor for Code Generation](https://arxiv.org/abs/2305.04087) — Generate-and-edit approach using execution feedback to improve LLM code quality.
- [Sketch2Code: Evaluating Vision-Language Models for Interactive Web Design Protot](https://arxiv.org/abs/2410.16232) — Benchmark evaluating VLMs on converting UI sketches to web code.
- [sniffbench](https://github.com/AnswerLayer/sniffbench) ⭐27 — Lightweight sniff-test benchmark for quick evaluation of coding agents.
- [STEPWISE-CODEX-Bench: Evaluating Complex Multi-Function Comprehension and Fine-G](https://arxiv.org/abs/2508.05193) — Benchmark for multi-function comprehension and fine-grained execution reasoning.
- [StudentEval: A Benchmark of Student-Written Prompts for Large Language Models of](https://arxiv.org/abs/2306.04556) — Benchmark of student-written prompts evaluating LLM code generation ability.
- [Success is in the Details: Evaluate and Enhance Details Sensitivity of Code](https://arxiv.org/abs/2505.14597) — Benchmark evaluating LLM sensitivity to code details for code generation.
- [svelte-bench](https://github.com/khromov/svelte-bench) ⭐168 — Benchmarks LLM code generation for Svelte 5 using HumanEval methodology.
- [SVGEditBench: A Benchmark Dataset for Quantitative Assessment of LLM's SVG Editi](https://arxiv.org/abs/2404.13710) — Benchmark for evaluating LLM capabilities in editing SVG code.
- [Synthesizing Performance Constraints for Evaluating and Improving Code Efficienc](https://arxiv.org/abs/2505.23471) — Synthesizes performance constraints to evaluate and improve code efficiency.
- [TACO: Topics in Algorithmic COde generation dataset](https://arxiv.org/abs/2312.14852) — Large-scale algorithmic code generation dataset with 25k+ competition-level prob.
- [The Path Not Taken: Duality in Reasoning about Program Execution](https://arxiv.org/abs/2604.20917) — Dual reasoning benchmark: predict outputs AND generate inputs for program execut.
- [Towards an understanding of large language models in software engineering tasks](https://arxiv.org/abs/2308.11396) — Surveys LLM evaluation across SE tasks, identifying benchmark gaps and research . 📋
- [TRACY: Benchmarking Execution Efficiency of LLM-Based Code Translation](https://arxiv.org/abs/2508.11468) — Benchmark for evaluating execution efficiency of LLM-based code translation.
- [Unraveling the Potential of Large Language Models in Code Translation: How Far Are We?](https://arxiv.org/abs/2410.09812) — Large-scale empirical study of LLMs on code translation across programming langu. 🌐
- [VerilogEval Evaluating Large Language Models for Verilog Code Generation](https://arxiv.org/abs/2309.07544) — Benchmark evaluating LLMs on Verilog hardware description language code generati.
- [verina](https://github.com/sunblaze-ucb/verina) ⭐61 — Benchmark for verifiable code, specification, and proof generation evaluation.
- [VERINA: Benchmarking Verifiable Code Generation](https://arxiv.org/abs/2505.23135) — Benchmark for evaluating verifiable code generation with formal specifications.
- [VersiCode: Towards Version-controllable Code Generation](https://arxiv.org/abs/2406.07411) — Benchmark for generating code targeting specific library/API versions.
- [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://arxiv.org/abs/2406.20098) — Benchmark and dataset for evaluating MLLMs on webpage screenshot to HTML code ge.
- [WebCode2M: A Real-World Dataset for Code Generation from Webpage Designs](https://arxiv.org/abs/2404.06369) — Large-scale real-world dataset for evaluating webpage code generation from desig.
- [WebCode: Search Evals for Coding Agents](https://exa.ai/blog/webcode) — WebCode: benchmark evaluating coding agents on web search capabilities.
- [WebGen-Bench: Evaluating LLMs on Generating Interactive and Functional Websites ](https://arxiv.org/abs/2505.03733) — Benchmark evaluating LLMs on generating interactive and functional websites from.
- [When Prompt Under-Specification Improves Code Correctness: An Exploratory Study of Prompt Wording and Structure Effects on LLM-Based Code Generation](https://arxiv.org/abs/2604.24712) — Study of prompt wording/structure effects on LLM code generation correctness.
- [wp-bench](https://github.com/WordPress/wp-bench) ⭐51 — WordPress-specific benchmark evaluating LLMs on WP APIs, plugins, and security c.
- [XCodeEval: An Execution-based Large Scale Multilingual Multitask Benchmark for C](https://arxiv.org/abs/2303.03004) — Execution-based multilingual multitask benchmark for code generation and underst. 🌐
- [[data](https://github.com/ProsusAI/stack-eval) — Stack-Eval: benchmark for evaluating code generation from Stack Overflow data.

<a id="feature-development"></a>
## Feature Development

- [A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reason](https://arxiv.org/html/2603.26337) — Benchmark for repo-level code agents on feature addition with intermediate reaso.
- [CodeAssistBench (Amazon Science)](https://www.amazon.science/code-and-datasets/codeassistbench) — Benchmark evaluating AI coding assistants via multi-agent workflows and Docker v. 🤝
- [CodeAssistBench (CAB): Dataset & Benchmarking for Multi-turn Chat-Based Code Ass](https://arxiv.org/abs/2507.10646) — Multi-turn chat-based code assistance benchmark with real GitHub issues.
- [FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation for Featu](https://arxiv.org/abs/2503.06680) — Benchmark for repo-level feature implementation from 83 GitHub repos' PRs.
- [FeatureBench](https://github.com/LiberCoders/FeatureBench) ⭐58 — Evaluates AI coding agents on complex feature development tasks in real-world re.
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://arxiv.org/abs/2602.10975) — Benchmarks agentic coding on complex multi-PR feature development tasks. 📅
- [NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Feature Additio](https://arxiv.org/abs/2507.18130) — Evaluates LLM-driven feature addition in no-code platforms using real project do.
- [PRDBench: Automatically Benchmarking LLM Code Agents through Agent-driven Annota](https://arxiv.org/html/2510.24358v1) — Benchmark of 50 real-world Python projects with PRD requirements for code agents.

<a id="multi-agent"></a>
## Multi-Agent

- [AgentArch](https://github.com/ServiceNow/AgentArch) ⭐11 — Benchmarks agent architectures like ReAct and Plan-and-Solve on enterprise tasks.
- [CADMAS-CTX: Contextual Capability Calibration for Multi-Agent Delegation](https://arxiv.org/abs/2604.17950v1) — Contextual capability calibration benchmark for multi-agent delegation in SE tas. 🤝
- [CooperBench](https://github.com/cooperbench/CooperBench) ⭐11 — Benchmarks multi-agent collaboration on SE tasks with conflict detection and res. 🤝
- [GAMMAF: A Common Framework for Graph-Based Anomaly Monitoring Benchmarking in LLM Multi-Agent Systems](https://arxiv.org/abs/2604.24477) — Standardized framework for benchmarking graph-based anomaly detection in LLM mul. 🤝 🔒
- [LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review](https://arxiv.org/abs/2604.16321) — MLR synthesizing evaluation evidence for LLM-based multi-agent code generation s. 🤝
- [MARBLE](https://github.com/ulab-uiuc/MARBLE) ⭐251 — Benchmarks LLM multi-agent collaboration and competition across diverse scenario. 🤝
- [MASArena](https://github.com/LINs-lab/MASArena) ⭐38 — Benchmarks single and multi-agent systems on task performance, accuracy, and eff. 🤝
- [MultiAgentBench ACL 2025](https://aclanthology.org/2025.acl-long.421) — Benchmark evaluating LLM agent collaboration and competition with milestone KPIs. 🤝
- [MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents](https://arxiv.org/html/2503.01935) — Benchmark evaluating LLM multi-agent collaboration and competition across scenar. 🤝
- [open-multi-agent](https://github.com/JackChen-me/open-multi-agent) — Open benchmark framework for evaluating multi-agent systems. 🤝
- [Paper - ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) — Multi-agent framework where LLM agents collaborate on end-to-end software develo. 🤝
- [Paper - MetaGPT: Meta Programming for Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — Multi-agent framework encoding SOPs for collaborative software development. 🤝
- [SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution](https://arxiv.org/abs/2507.23348) — Multi-agent debate framework for software issue resolution evaluated on SWE-benc. 🤝
- [sweet_rl](https://github.com/facebookresearch/sweet_rl) ⭐266 — Benchmarks multi-turn collaborative reasoning for LLM agent training.
- [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories](https://arxiv.org/abs/2604.07223) — Benchmark assessing LLM guardrail safety on multi-step tool-calling trajectories.

---

[← Back to README](../README.md)
