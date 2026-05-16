# ② Benchmarks & Datasets

SE Agent benchmarks organized by task type.

## Contents

- [Bug Fix & Issue Resolution (69)](#bug-fix)
- [End-to-End / Multi-Task (109)](#end-to-end)
- [Long-Horizon / Evolution (35)](#long-horizon)
- [Large Codebase / Multi-Repo (22)](#large-codebase)
- [Code Review (27)](#code-review)
- [Testing & QA (40)](#testing)
- [Security & Vulnerability (49)](#security)
- [Production-Derived (13)](#production)
- [Code Generation (144)](#code-generation)
- [Feature Development (8)](#feature-development)
- [Multi-Agent (15)](#multi-agent)

<a id="bug-fix"></a>
## Bug Fix & Issue Resolution

*The most established evaluation category. SWE-bench family dominates. Start with SWE-bench Verified for a reliable baseline.*

### A–F

- [A Benchmark for Localizing Code and Non-Code Issues in Software Projects](https://arxiv.org/abs/2509.25242) — Benchmarks issue localization across code and non-code files on 1100 issues.
- [A Real-World Benchmark for Evaluating Fine-Grained Issue Solving Capabilities of Large Language Models](https://arxiv.org/abs/2411.18019) — A Real-World Benchmark for Evaluating Fine-Grained Issue Solving Capabilities of Large Language Models. 🌍
- [AEGIS: An Agent-based Framework for Bug Reproduction from Issue Descriptions](https://www.semanticscholar.org/paper/89dccc903cbeddb8c09df35c5c5da7aeaf0bcd6f) — Agent framework for automated bug reproduction from issue descriptions.
- [Agentic Bug Reproduction for Effective Automated Program Repair at Google](https://arxiv.org/abs/2502.01821) — Agentic Bug Reproduction for Effective Automated Program Repair at Google.
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489) — Agent-free LLM localize-repair-verify pipeline as baseline on SWE-bench.
- [Amazon introduces SWE-PolyBench, a multilingual benchmark for AI Coding Agents](https://aws.amazon.com/blogs/devops/amazon-introduces-swe-polybench-a-multi-lingual-benchmark-for-ai-coding-agents/) — SWE-PolyBench: multilingual benchmark for AI coding agents across languages. 🌐
- [An Analysis of the Automatic Bug Fixing Performance of ChatGPT](https://arxiv.org/abs/2301.08653) — Evaluates ChatGPT auto bug fixing on QuixBugs and Defects4J vs traditional APR.
- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](https://www.semanticscholar.org/paper/012a1885351785b62ab8273830197f1e759911ec) — Empirical study on fine-tuning LLMs of code for automated program repair.
- [An LLM-based Agent for Reliable Docker Environment Configuration](https://www.semanticscholar.org/paper/d569c3afc3b6b0e4f142107b893c3d365f58f081) — An LLM-based Agent for Reliable Docker Environment Configuration.
- [AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Tests](https://arxiv.org/abs/2507.17542) — AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Tests.
- [BackportBench: A Multilingual Benchmark for Automated Backporting of Patches](https://arxiv.org/abs/2512.01396) — Multilingual benchmark for automated patch backporting across software versions. 🌐
- [Bug-Report-Driven Fault Localization: Industrial Benchmarking and Lesson Learned at ABB Robotics](https://arxiv.org/abs/2604.25700v1) — Industrial benchmark for bug-report-driven fault localization at ABB Robotics.
- [BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills](https://arxiv.org/abs/2510.19898) — BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills.
- [BugsInPy: a database of existing bugs in Python programs to enable controlled testing and debugging studies](https://arxiv.org/abs/2401.15481) — BugsInPy: a database of existing bugs in Python programs to enable controlled testing and debugging studies. 🐍
- [CLEVER:A Curated Benchmark for Formally Verified](https://arxiv.org/abs/2505.13938) — Curated benchmark for formally verified bug fixes in software.
- [COAST: Enhancing the Code Debugging Ability of LLMs through Communicative Agent Based Data Synthesis](https://arxiv.org/abs/2408.05006) — Multi-agent data synthesis framework to enhance LLM code debugging ability. 🤝
- [CodeMonkeys: Scaling Test-Time Compute for Software Engineering](https://arxiv.org/abs/2501.14723) — CodeMonkeys: Scaling Test-Time Compute for Software Engineering.
- [CORE: Resolving Code Quality Issues using LLMs](https://www.semanticscholar.org/paper/4202a75d7b3c586ebd9451ed08f38cbf264cfd8e) — LLMs resolving static analysis code quality issues in developer workflows.
- [DebugBench: Evaluating Debugging Capability of Large Language Models](https://arxiv.org/abs/2401.04621) — Benchmark evaluating LLM debugging capability across multiple bug categories.
- [Defects4J: a database of existing faults to enable controlled testing studies for Java programs](https://www.semanticscholar.org/paper/37e2106bebd02f4ac9c410941fde7f358279e4a4) — Database of real Java faults enabling controlled testing/repair studies. ☕
- [Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair](https://arxiv.org/abs/2601.19066) — Co-generates bug reproduction tests with patches in agentic program repair.
- [Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis](https://arxiv.org/abs/2604.24212v1) — Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis.
- [Enhancing Program Repair with Specification Guidance and Intermediate Behavioral Signals](https://arxiv.org/abs/2604.11770) — LLM-based APR using intermediate behavioral signals beyond test-suite outcomes.
- [Evaluating and Improving Automated Repository-Level Rust Issue Resolution with LLM-based Agents](https://arxiv.org/abs/2602.22764) — Evaluates LLM agent issue resolution on 500 real repo-level Rust problems. 🦀

### G–L

- [GitBug-Actions: Building Reproducible Bug-Fix Benchmarks with GitHub Actions](https://arxiv.org/abs/2310.15642) — Reproducible bug-fix benchmark built from GitHub Actions CI pipelines.
- [GitBug-Java: A Reproducible Benchmark of Recent Java Bugs](https://arxiv.org/abs/2402.02961) — GitBug-Java: A Reproducible Benchmark of Recent Java Bugs. ☕
- [How Often Do Single-Statement Bugs Occur? The ManySStuBs4J Dataset](https://arxiv.org/abs/1905.13334) — Dataset of 153,652 Java single-statement bug-fix changes for program repair. ☕
- [HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks](https://arxiv.org/abs/2604.14709) — HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks.
- [InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Software Issue Resolution](https://arxiv.org/abs/2511.16004) — InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Software Issue Resolution. 🤝
- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) — Introducing SWE-bench Verified.
- [joycode-agent](https://github.com/jd-opensource/joycode-agent) ⭐330 — Repository-level repair agent built and evaluated on SWE-Bench.
- [Large Language Models of Code Fail at Completing Code with Potential Bugs](https://arxiv.org/abs/2306.03438) — Benchmark for code completion degradation when context contains potential bugs.
- [Lingma SWE-GPT: An Open Development-Process-Centric Language Model for Automated Software Improvement](https://arxiv.org/abs/2411.00622) — Dev-process-centric open LLM for automated software repair on SWE-bench.
- [LocAgent: Graph-Guided LLM Agents for Code Localization](https://arxiv.org/abs/2503.09089) — LocAgent: Graph-Guided LLM Agents for Code Localization.

### M–R

- [MLDebugging: Towards Benchmarking Code Debugging Across Multi-Library Scenarios](https://arxiv.org/abs/2506.13824) — Benchmark for code debugging across multi-library scenarios.
- [multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) ⭐333 — multi-swe-bench. 🌐
- [OmniGIRL](https://github.com/DeepSoftwareAnalytics/OmniGIRL) ⭐17 — OmniGIRL. 🌐
- [OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution](https://arxiv.org/abs/2505.04606) — Multilingual and multimodal benchmark for evaluating GitHub issue resolution. 🌐
- [Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?](https://arxiv.org/abs/2604.17338) — Evaluates whether models precisely debug or simply regenerate entire code.
- [QuixBugs: a multi-lingual program repair benchmark set based on the quixey challenge](https://www.semanticscholar.org/paper/7f1d443ab526240e2647e77e042434fc98249302) — QuixBugs: a multi-lingual program repair benchmark set based on the quixey challenge. 🌐
- [RepairBench: Leaderboard of Frontier Models for Program Repair](https://arxiv.org/abs/2409.18952) — RepairBench: Leaderboard of Frontier Models for Program Repair. 🏆
- [Reproducible Automated Program Repair Is Hard -- Experiences With the Defects4J Dataset](https://arxiv.org/abs/2604.26674v1) — Reproducibility challenges in APR evaluation using Defects4J benchmark dataset.
- [Rust-SWE-Bench](https://github.com/GhabiX/Rust-SWE-Bench) ⭐11 — Evaluates agent issue-resolution ability on real Rust project GitHub issues. 🦀

### S–Z

- [Skywork-SWE](https://arxiv.org/html/2506.19290v1) — Benchmark validating data scaling laws for SE agent bug-fix capability. 🐍
- [SpecRover: Code Intent Extraction via LLMs](https://arxiv.org/abs/2408.02232) — Infers code intent via LLMs for specification-driven automated program repair.
- [SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark](https://arxiv.org/abs/2603.00520) — SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark.
- [SWE-bench](https://github.com/swe-bench/SWE-bench) ⭐4819 — 2294 real GitHub issues testing agent patch generation for Python bug fixes. 🐍
- [SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks](https://arxiv.org/abs/2604.26278) — SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks.
- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419) — Continuously updated SWE-bench variant improving repo coverage and scalability.
- [SWE-bench Multimodal](https://github.com/swe-bench/SWE-bench) ⭐4819 — SWE-bench Multimodal.
- [SWE-bench Verified](https://github.com/swe-bench/SWE-bench) ⭐4819 — 500 human-verified subset of SWE-bench filtering ambiguous or erroneous issues. 🐍
- [SWE-Bench-Fork](https://github.com/SWE-Gym/SWE-Bench-Fork) ⭐13 — SWE-Gym fork of SWE-Bench for evaluating agents on real GitHub issue fixes.
- [SWE-bench-java: A GitHub Issue Resolving Benchmark for Java](https://arxiv.org/abs/2408.14354) — Extends SWE-bench to Java with real GitHub issue resolving tasks. ☕
- [swe-bench-lite-samples](https://github.com/ScalingIntelligence/swe-bench-lite-samples) ⭐14 — swe-bench-lite-samples.
- [SWE-Bench-plus-plus](https://github.com/TuringEnterprises/SWE-Bench-plus-plus) ⭐19 — SWE-Bench-plus-plus.
- [swe-bench.github.io](https://github.com/SWE-bench/swe-bench.github.io) ⭐12 — swe-bench.github.io. 🏆
- [SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling](https://arxiv.org/abs/2506.07636) — Provides 17K+ training instances and test cases for SWE agents with scaling.
- [SWE-Exp: Experience-Driven Software Issue Resolution](https://arxiv.org/abs/2507.23361) — SWE-Exp: Experience-Driven Software Issue Resolution.
- [SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution](https://arxiv.org/abs/2501.05040) — Trains open-source LLMs to resolve GitHub issues on SWE-bench tasks.
- [SWE-MERA](https://github.com/MERA-Evaluation/repotest) ⭐14 — Dynamic rolling SWE benchmark with fresh issues to prevent data contamination.
- [SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks](https://arxiv.org/abs/2507.11059) — SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks.
- [SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories](https://arxiv.org/abs/2509.08724) — Scales issue-resolving datasets by mirroring issues across repo environments.
- [SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents](https://arxiv.org/abs/2505.20411) — SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents.
- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798) — Scalable pipeline for synthesizing SWE training data with bug-fix benchmark.
- [SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs](https://arxiv.org/abs/2504.14757) — SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs.
- [SYSUSELab/FeedbackEval](https://github.com/SYSUSELab/FeedbackEval) — Benchmark for evaluating LLMs on feedback-driven code repair tasks.
- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139) — Training environment with 2,438 Python repo tasks and verifier for SE agents.
- [When Large Language Models Confront Repository-Level Automatic Program Repair: How Well They Done?](https://arxiv.org/abs/2403.00448) — Evaluates LLMs on repository-level automated program repair tasks.
- [[repo](https://github.com/NEUIR/DebugEval) — DebugEval: benchmark for evaluating LLM debugging capabilities.

<a id="end-to-end"></a>
## End-to-End / Multi-Task

*Evaluates agents on complete project development, not just isolated fixes. Growing rapidly as agents become more capable.*

### A–F

- [A Comprehensive Benchmark to Evaluate Agent Architectures in Enterprise](https://arxiv.org/html/2509.10769v1) — Benchmark evaluating agent architectures for enterprise multi-step workflows.
- [A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System](https://arxiv.org/abs/2510.09721) — A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System. 📋
- [ABC-Bench](https://github.com/OpenMOSS/ABC-Bench) ⭐29 — ABC-Bench.
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
- [Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development](https://arxiv.org/abs/2511.04064) — Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development.
- [benchmarks](https://github.com/0xpayne/gpt-migrate#-benchmarks) — GPT-Migrate benchmarks for automated codebase migration between frameworks.
- [Beyond pip install: Evaluating LLM Agents for the Automated Installation of Python Projects](https://arxiv.org/abs/2412.06294) — Beyond pip install: Evaluating LLM Agents for the Automated Installation of Python Projects. 🐍
- [Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents](https://arxiv.org/abs/2506.00172) — Scalable benchmark for evaluating system-level reasoning in LLM code agents.
- [CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments](https://arxiv.org/abs/2510.26852) — CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments.
- [ccbench](https://github.com/codecrafters-io/ccbench) ⭐29 — CodeCrafters benchmark tool for evaluating coding agents on SE tasks. 🦀
- [Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows](https://arxiv.org/abs/2604.20200) — Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows.
- [Claw-Eval-Live](https://arxiv.org/abs/2604.29300) — Live agent benchmark for evolving real-world workflows. 🌍
- [ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces](https://arxiv.org/abs/2604.05172) — ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces.
- [CocoaBench: Evaluating Unified Digital Agents in the Wild](https://arxiv.org/abs/2604.11201) — CocoaBench: Evaluating Unified Digital Agents in the Wild. 📅
- [CodeClash](https://github.com/CodeClash-ai/CodeClash) ⭐147 — Evaluates autonomous agent planning and execution on open-ended coding tasks.
- [CODEMENV: Benchmarking Large Language Models on Code Migration](https://arxiv.org/abs/2506.00894) — Benchmark for evaluating LLMs on code migration tasks across environments.
- [CoreCodeBench: A Configurable Multi-Scenario Repository-Level Benchmark](https://arxiv.org/abs/2507.05281) — Configurable multi-scenario repository-level benchmark for code agents.
- [Credit-Budgeted ICPC-Style Coding: When Agents Must Pay for Every Decision](https://arxiv.org/abs/2604.10182) — Evaluates coding agents on ICPC-style problems with credit-budgeted decisions.
- [Cursor debuts CursorBench-3 to evaluate coding agents](https://www.testingcatalog.com/cursor-debuts-cursorbench-3-to-evaluate-coding-agents/) — CursorBench-3: Cursor's benchmark evaluating coding agents on complex dev tasks.
- [DataSciBench: An LLM Agent Benchmark for Data Science](https://arxiv.org/abs/2502.13897) — Benchmark evaluating LLM agents on data science tasks end-to-end.
- [devin-swebench-results](https://github.com/CognitionAI/devin-swebench-results) ⭐126 — Cognition's published Devin evaluation results and methodology on SWE-bench.
- [DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle](https://arxiv.org/abs/2601.20882) — DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle. 📅
- [DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?](https://arxiv.org/abs/2409.07703) — Benchmark evaluating data science agents on realistic DS tasks.
- [EnConda-Bench](https://github.com/TencentYoutuResearch/EnConda-Bench) ⭐49 — EnConda-Bench.
- [EnvBench: A Benchmark for Automated Environment Setup](https://arxiv.org/abs/2503.14443) — Benchmarks LLM agents on automated dev environment setup across real repos.
- [eval-data](https://github.com/paradite/eval-data) ⭐17 — LLM evaluation prompts and datasets for real-world coding and writing tasks.
- [Evaluating Agents' Ability to Conduct Innovative AI Research](https://iclr.cc/virtual/2026/poster/10006754) — Benchmark of 20 tasks evaluating agents on innovative AI research capabilities.
- [Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios](https://arxiv.org/abs/2604.06742) — Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios.
- [EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration](https://arxiv.org/abs/2601.16489) — EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration. 🤝
- [Evolutionary Perspectives on the Evaluation of LLM-Based AI Agents: A Comprehensive Survey](https://arxiv.org/abs/2506.11102) — Surveys evolutionary perspectives on evaluating LLM chatbots vs AI agents. 📋
- [Exploring the Challenges and Opportunities of AI-assisted Codebase Generation](https://arxiv.org/abs/2508.07966) — Study of challenges and opportunities in AI-assisted full codebase generation. 📅
- [From What to How: Bridging User Requirements with Software Development Using Large Language Models](https://arxiv.org/abs/2602.13611) — Benchmarks LLMs on software design from user requirements to code generation.
- [Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External Solver](https://arxiv.org/abs/2604.25067) — Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline For Connect Four That Performs Comparably to an External.
- [Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization](https://arxiv.org/abs/2604.12290) — Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization.

### G–L

- [GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation](https://arxiv.org/abs/2604.24929) — GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation. 🌐
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) ⭐252 — GitTaskBench.
- [GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging](https://arxiv.org/abs/2508.18993) — Benchmark for code agents solving real-world tasks using code repositories.
- [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763) — GLM-5 model evaluated on agentic SE benchmarks like SWE-bench and DevBench.
- [HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?](https://arxiv.org/abs/2604.09408) — HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?.
- [How we compare model quality in Cursor (CursorBench)](https://cursor.com/blog/cursorbench) — CursorBench: multi-dimensional eval of AI coding agents in Cursor IDE.
- [Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819) — Hybrid-Gym: Training Coding Agents to Generalize Across Tasks.
- [IDE-Bench: Evaluating Large Language Models as IDE Agents on Real-World Software Engineering Tasks](https://arxiv.org/abs/2601.20886) — Evaluates LLMs as IDE agents on real-world software tasks with dockerized tests. 🌍
- [Immersion in the GitHub Universe: Scaling Coding Agents to Mastery](https://arxiv.org/abs/2602.09892) — Automated multi-agent workflow to generate large-scale SWE training/eval data. 🤝
- [insights](https://github.com/logic-star-ai/insights) ⭐49 — Tracks autonomous coding agents on real open-source projects with leaderboards. 🏆
- [InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](https://arxiv.org/abs/2306.14898) — Interactive coding benchmark modeling code tasks as RL with execution feedback.
- [june-2025-coding-agent-report](https://github.com/The-Focus-AI/june-2025-coding-agent-report) ⭐40 — Benchmarks 15 coding agents on real-world development tasks across IDEs.
- [leaderboard](https://github.com/pinchbench/leaderboard) ⭐35 — Leaderboard ranking LLM coding agents on end-to-end programming tasks. 🏆
- [Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs](https://arxiv.org/abs/2509.25873) — Minimal-scaffold agent to evaluate true agentic coding capabilities of LLMs.
- [LiveFMBench](https://arxiv.org/abs/2604.29800) — Evaluate agentic workflows in specification generation tasks.

### M–R

- [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/abs/2604.23897) — MarketBench: Evaluating AI Agents as Market Participants.
- [ML-Bench: Evaluating LLMs for Machine Learning Tasks on Repository-Level Code](https://ml-bench.github.io/) — ML-Bench: Evaluating LLMs for Machine Learning Tasks on Repository-Level Code.
- [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://openreview.net/forum?id=6s5uXNWGIh) — 75 Kaggle ML engineering tasks benchmark for evaluating ML agents.
- [MMBench-GUI](https://github.com/open-compass/MMBench-GUI) ⭐106 — Hierarchical benchmark for GUI agents across desktop, mobile, and web platforms.
- [Multi-Docker-Eval: A `Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering](https://arxiv.org/abs/2512.06915) — Benchmark for automated environment setup with 40 real repos across 9 languages. 🌐
- [Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving](https://arxiv.org/abs/2504.02605) — Multilingual issue-resolving benchmark across 7 languages with 1632 instances. 🌐
- [OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation](https://arxiv.org/abs/2604.10866) — OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation.
- [OmniCode](https://arxiv.org/html/2602.02262v2) — OmniCode.
- [OmniCode: A Benchmark for Evaluating Software Development Agents](https://openreview.net/forum?id=VP204Aa0gH) — OmniCode: A Benchmark for Evaluating Software Development Agents.
- [OpenCode Bench vs SWE-bench vs Terminal-Bench](https://www.morphllm.com/opencode-benchmarks) — Comparison of OpenCode Bench, SWE-bench, and Terminal-Bench benchmarks.
- [OpenGame: Open Agentic Coding for Games](https://arxiv.org/abs/2604.18394) — Benchmark for evaluating AI coding agents on full game development tasks.
- [OS-SPEAR: A Toolkit for the Safety, Performance,Efficiency, and Robustness Analysis of OS Agents](https://arxiv.org/abs/2604.24348) — OS-SPEAR: A Toolkit for the Safety, Performance,Efficiency, and Robustness Analysis of OS Agents.
- [OSS-Bench: Benchmark Generator for Coding LLMs](https://arxiv.org/abs/2505.12331) — Generates benchmarks for evaluating coding LLMs from open-source repositories.
- [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://openai.com/index/paperbench/) — Benchmark evaluating AI agents on replicating AI research papers from scratch.
- [Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents](https://arxiv.org/abs/2510.25694) — Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents. 🔍
- [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://arxiv.org/abs/2502.18525) — Programming with Pixels: Can Computer-Use Agents do Software Engineering?.
- [ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development](https://arxiv.org/html/2602.01655v1) — ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development.
- [reading-list](https://github.com/SWE-bench/reading-list) ⭐11 — SWE-bench curated reading list of papers on SE agent evaluation and benchmarks. 📋
- [RefactorBench](https://github.com/microsoft/RefactorBench) ⭐23 — Benchmarks agents on cross-file code refactoring tasks in real repositories.
- [RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale](https://arxiv.org/abs/2508.01550) — End-to-end pipeline generating, evaluating, and training SWE agents at scale.
- [RepoUnderstander](https://github.com/RepoUnderstander/RepoUnderstander) ⭐97 — RepoUnderstander.

### S–Z

- [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://openreview.net/forum?id=6z4YKr0GK6) — ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery.
- [Sea-benchmarks-public](https://github.com/Sea-Labs-ai/Sea-benchmarks-public) ⭐17 — Benchmarks AI coding agents across multiple software engineering tasks.
- [SERA: Soft-Verified Efficient Repository Agents](https://arxiv.org/abs/2601.20789) — SERA: Soft-Verified Efficient Repository Agents.
- [skill](https://github.com/pinchbench/skill) ⭐1079 — Benchmark by Kilo.ai for end-to-end evaluation of LLM coding agents on SE tasks.
- [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://arxiv.org/abs/2411.07763) — Benchmark evaluating LMs on real-world enterprise text-to-SQL workflows. 🌍
- [SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents](https://arxiv.org/abs/2602.09447) — Benchmarks LLM agents building production-grade software from specs in MoonBit.
- [SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context](https://arxiv.org/abs/2604.11716v1) — SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context.
- [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://arxiv.org/abs/2410.03859) — SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?.
- [SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live) ⭐185 — SWE-bench-Live. ✅
- [SWE-Compass](https://arxiv.org/html/2511.05459) — Unified benchmark integrating heterogeneous SE tasks for cross-task evaluation.
- [SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent](https://arxiv.org/abs/2604.26102) — SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent.
- [SWE-Effi](https://arxiv.org/abs/2509.09853) — Metrics balancing solution accuracy vs resource cost for SWE agent evaluation.
- [SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks](https://arxiv.org/abs/2603.00575) — SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks. 🌐 📅
- [SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?](https://arxiv.org/abs/2502.12115) — Benchmarks LLMs on 1400+ real Upwork freelance tasks worth $1M total. 🌍
- [SWE-PolyBench](https://github.com/amazon-science/SWE-PolyBench) ⭐83 — SWE-PolyBench. 🌐
- [SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents](https://arxiv.org/abs/2504.08703) — SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents. 🌐
- [SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering Tasks](https://arxiv.org/abs/2511.02352) — SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering Tasks.
- [SWE-Skills-Bench](https://github.com/GeniusHTX/SWE-Skills-Bench) ⭐33 — Benchmarks decomposed SE agent skills like fault localization and code editing.
- [SWE-Universe: Scale Real-World Verifiable Environments to Millions](https://arxiv.org/abs/2602.02361) — SWE-Universe: Scale Real-World Verifiable Environments to Millions.
- [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) ⭐1441 — Benchmarks LLMs on 1400+ real freelance software engineering tasks worth $1M+.
- [TDFlow: Agentic Workflows for Test Driven Development](https://arxiv.org/abs/2510.23761) — Test-driven multi-agent workflow for repo-level SE, evaluated on SWE-bench. 🤝
- [TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents](https://arxiv.org/abs/2602.07274) — TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents.
- [Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute](https://arxiv.org/abs/2503.23803) — TTC scaling for open-source SE agents evaluated on SWE-bench.
- [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/abs/2604.25727v1) — Skill-graph-based synthesis of terminal task instances for agent training/eval.
- [Towards Generating Functionally Correct Code Edits from Natural Language Issue Descriptions](https://arxiv.org/abs/2304.03816) — Evaluates LLM code edits from GitHub issues with hidden test verification.
- [Training Versatile Coding Agents in Synthetic Environments](https://arxiv.org/abs/2512.12216) — Training Versatile Coding Agents in Synthetic Environments.
- [TRAJECT-Bench](https://arxiv.org/abs/2510.04550) — Evaluates LLM tool use via full tool-selection trajectories, not just answers.
- [Unified Software Engineering agent as AI Software Engineer](https://arxiv.org/abs/2506.14683) — Defines AI SE agent concept and evaluates LLM agents as full software engineers.
- [WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224) — WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models.

<a id="long-horizon"></a>
## Long-Horizon / Evolution

*Tests multi-step, multi-file changes over extended interactions. Closer to real engineering work than single-issue benchmarks.*

### A–F

- [ALE-Bench: Towards Automating Long-Horizon Algorithm Engineering](https://sakana.ai/ale-bench/) — Benchmark for long-horizon algorithm engineering on hard optimization problems. 📅
- [AMA-Bench](https://github.com/AMA-Bench/AMA-Bench) ⭐36 — Benchmark for long-context retention and long-term memory in agent applications. 📅
- [An Interactive Benchmark for LLM Agents in Long-Context Software Engineering](https://arxiv.org/abs/2511.13998) — Interactive benchmark for LLM agents in long-context software engineering tasks.
- [Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios](https://arxiv.org/abs/2512.18470) — Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios. 📅
- [Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/html/2509.16941v1) — Can AI Agents Solve Long-Horizon Software Engineering Tasks?. 📅
- [Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](https://arxiv.org/abs/2604.24697) — Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft. 📅
- [ClawGym: A Scalable Framework for Building Effective Claw Agents](https://arxiv.org/abs/2604.26904v1) — ClawGym: A Scalable Framework for Building Effective Claw Agents.
- [ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents](https://arxiv.org/abs/2604.23781) — Living-world benchmark for multi-turn, multi-day, multimodal coworker agents. 📅
- [Conversations Beneath the Code](https://arxiv.org/abs/2604.28455) — Triadic data (spec, discussion, code) for long-horizon SE agents. 📅
- [EvoClaw: Evaluating AI Agents on Continuous Software Evolution](https://arxiv.org/abs/2603.13428) — EvoClaw: Evaluating AI Agents on Continuous Software Evolution. 📅
- [frontier-swe](https://github.com/Proximal-Labs/frontier-swe) ⭐93 — Benchmarks coding agents on long-horizon impl, perf engineering, and ML tasks. 📅

### G–L

- [goodai-ltm-benchmark](https://github.com/GoodAI/goodai-ltm-benchmark) ⭐86 — goodai-ltm-benchmark.
- [HARBOR: Automated Harness Optimization](https://arxiv.org/abs/2604.20938) — HARBOR: Automated Harness Optimization.
- [Hyper-multi-step: The Truth Behind Difficult Long-context Tasks](https://openreview.net/forum?id=LRPzo4jixx) — Hyper-multi-step: The Truth Behind Difficult Long-context Tasks.
- [LifelongAgentBench](https://github.com/caixd-220529/LifelongAgentBench) ⭐88 — Benchmark evaluating LLM agents as lifelong learners across tasks. 📅
- [LOCA-bench](https://arxiv.org/abs/2602.07962) — Evaluates agent performance degradation under dynamically growing context.
- [LoCoBench-Agent](https://github.com/SalesforceAIResearch/LoCoBench-Agent) ⭐19 — Long-context interactive benchmark for LLM agents on multi-turn code tasks.
- [LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces](https://arxiv.org/abs/2602.14337) — LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces. 📅
- [LongMemEval](https://arxiv.org/abs/2410.10813) — Benchmarks long-term memory recall in chat assistants across sessions.

### M–R

- [MemoryArena](https://arxiv.org/abs/2602.16313) — Evaluates agent memory across coupled multi-session tasks requiring recall.
- [METR's Autonomy Evaluation Resources](https://evaluations.metr.org/) — METR's Autonomy Evaluation Resources. 📅
- [MirrorCode: Evidence AI can already do some weeks-long coding tasks](https://epoch.ai/blog/mirrorcode-preliminary-results) — MirrorCode: Evidence AI can already do some weeks-long coding tasks. 📅
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation](https://arxiv.org/html/2512.12730v1) — Benchmark for generating complete Python libraries from NL requirements. 📅 🐍
- [NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents](https://arxiv.org/abs/2512.12730) — NL2Repo-Bench: Towards Long-Horizon Repository Generation Evaluation of Coding Agents. 📅
- [Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks](https://arxiv.org/abs/2604.24964) — Web agent benchmark for realistic long-horizon, multi-site browsing tasks. 📅

### S–Z

- [Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529v1) — Test-time compute scaling for long-horizon agentic coding tasks. 📅
- [SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents](https://arxiv.org/abs/2604.17308) — SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents.
- [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://arxiv.org/abs/2603.24755) — SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks. 📅
- [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://www.huggingface.co/papers/2603.24755) — SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks.
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) ⭐368 — Long-horizon SE task benchmark by Scale AI for multi-step complex engineering. 📅 🐍
- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/abs/2509.16941) — Benchmarks AI agents on 1865 long-horizon enterprise tasks from 41 repos. 📅
- [SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration](https://arxiv.org/abs/2603.03823) — SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration. 📅
- [SWE-EVO](https://arxiv.org/html/2512.18470v2) — Benchmarks multi-step software evolution with 48 tasks across 7 OSS projects. 📅 🐍
- [SwingArena](https://github.com/menik1126/Swing-Bench) — Competitive arena for long-context GitHub issue solving with Elo ranking. 🏆
- [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) ⭐375 — terminal-bench-rl. 📅

<a id="large-codebase"></a>
## Large Codebase / Multi-Repo

*Evaluates navigation and modification in large-scale repos (>50K LOC). Tests real-world scalability.*

- [Benchmarking Agentic Code Reasoning at the Repository Level](https://arxiv.org/html/2601.03731v1) — Benchmark for repository-level code reasoning in agentic LLMs.
- [CodeScaleBench](https://sourcegraph.com/blog) — CodeScaleBench.
- [CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning](https://arxiv.org/abs/2506.00750) — Benchmark and dataset for evaluating code semantic reasoning capabilities.
- [ContextBench](https://arxiv.org/abs/2602.05892) — Evaluates how coding agents retrieve and use code context for issue resolution.
- [Continuous Benchmark Generation for Evaluating Enterprise-scale LLM Agents](https://arxiv.org/html/2511.10049) — Continuous Benchmark Generation for Evaluating Enterprise-scale LLM Agents.
- [CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion](https://arxiv.org/abs/2310.11248) — Cross-file code completion benchmark across multiple languages. 🌐
- [DeepCodeBench: Real-World Codebase Understanding by Q&A Benchmarking](https://www.qodo.ai/blog/deepcodebench-real-world-codebase-understanding-by-qa-benchmarking/) — Q&A benchmark for real-world enterprise codebase understanding.
- [How to Understand Whole Software Repository?](https://www.semanticscholar.org/paper/19b825e139a54b543e7d8380ab0a1f9a7a29eaa2) — Benchmarks AI comprehension of whole software repositories via repo-level tasks.
- [HumanEvo: An Evolution-Aware Benchmark for More Realistic Evaluation of Repository-Level Code Generation](https://doi.org/10.1109/ICSE55347.2025.00228) — Evolution-aware benchmark for realistic repo-level code generation evaluation.
- [legacy-bench](https://github.com/Factory-AI/legacy-bench) ⭐13 — legacy-bench.
- [LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Software Engineering](https://arxiv.org/abs/2509.09614) — Benchmark for LLMs handling long-context complex software engineering tasks.
- [LongCodeBench: Evaluating Coding LLMs at 1M Context Windows](https://arxiv.org/abs/2505.07897) — LongCodeBench: Evaluating Coding LLMs at 1M Context Windows.
- [LONGCODEU: Benchmarking Long-Context Language Models on Long Code Understanding](https://arxiv.org/abs/2503.04359) — Benchmark for evaluating LLMs on long code understanding with long contexts.
- [Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits](https://arxiv.org/abs/2603.27745) — Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits.
- [R2E: Turning any Github Repository into a Programming Agent Environment](https://www.semanticscholar.org/paper/2860bfaa9fa1d249c24aaf0981ad61bdbcd9c544) — R2E: Turning any Github Repository into a Programming Agent Environment.
- [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://arxiv.org/abs/2306.03091) — Benchmark for repo-level multi-file code auto-completion in Python and Java.
- [Repository-level Code Translation Benchmark Targeting Rust](https://arxiv.org/abs/2411.13990) — Repository-level code translation benchmark targeting Rust. 🦀
- [Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation](https://arxiv.org/abs/2501.16050) — Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation.
- [SWE Context Bench](https://arxiv.org/abs/2602.08316) — Benchmarks context reuse across related coding tasks in programming agents.
- [SWE-QA: A Dataset and Benchmark for Complex Code Understanding](https://arxiv.org/abs/2604.24814) — 9,072 MCQs from 12 Python repos evaluating multi-hop code understanding. 🐍
- [Workspace-Bench](https://arxiv.org/abs/2604.28600) — Benchmark AI agents on workspace tasks with large-scale file dependencies. 📦
- [You make your evals, then your evals make you. Introducing AugmentQA](https://www.augmentcode.com/blog/you-make-your-evals-then-your-evals-make-you-introducing-augmentqa) — You make your evals, then your evals make you. Introducing AugmentQA.

<a id="code-review"></a>
## Code Review

*Measures quality of review comments and suggestions. Emerging area with high practical value.*

- [aacr-bench](https://github.com/alibaba/aacr-bench) ⭐150 — aacr-bench. 🌐
- [AACR-Bench: Evaluating Automatic Code Review with Holistic Repository-Level Context](https://arxiv.org/abs/2601.19494) — Benchmarks automatic code review using holistic repo-level context from PRs. 🌐
- [AUGER: automatically generating review comments with pre-training models](https://arxiv.org/abs/2208.08014) — Automated review comment generation using pre-training models.
- [Automatically Recommend Code Updates: Are We There Yet?](https://arxiv.org/abs/2209.07048) — Evaluates CodeLM-based code update recommendation on real-world tasks.
- [Automating code review activities by large-scale pre-training](https://arxiv.org/abs/2203.09095) — Pre-training model to automate code review activities in SE lifecycle.
- [Benchmarking and Studying the LLM-based Code Review](https://arxiv.org/abs/2509.01494) — Benchmarking and Studying the LLM-based Code Review.
- [Benchmarking LLMs for Fine-Grained Code Review with Enriched Context in Practice](https://arxiv.org/abs/2511.07017) — Benchmarks LLMs on fine-grained code review with enriched semantic context.
- [Code Review Agent Benchmark](https://arxiv.org/html/2603.23448v1) — Code Review Agent Benchmark. 🤖
- [CodeAgent: Autonomous Communicative Agents for Code Review](https://arxiv.org/abs/2402.02172) — Multi-agent LLM system for automated code review evaluation. 🤝
- [CodeCriticBench: A Holistic Code Critique Benchmark for Large Language Models](https://arxiv.org/abs/2502.16614) — Benchmarks LLM code critique on defect analysis, feedback, and review quality.
- [CodeFuse-CR-Bench](https://arxiv.org/abs/2509.14856) — Benchmarks end-to-end code review with comment generation and code revision.
- [CodeReviewer: Pre-Training for Automating Code Review Activities](https://www.semanticscholar.org/paper/b951c0691a0d2ca65202a1eed2ccedf6e305d035) — Pre-trained model and benchmark for automating code review activities.
- [CodeTaste: Can LLMs Generate Human-Level Code Refactorings?](https://arxiv.org/abs/2603.04177) — Benchmarks LLM ability to generate human-level code refactorings.
- [CommitSuite](https://arxiv.org/abs/2604.28700) — Comprehensive benchmark for commit classification and message generation.
- [CR-Bench: Evaluating Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2603.11078) — Benchmark AI code review agents with fine-grained evaluation pipeline. 🌍
- [EvaCRC: Evaluating Code Review Comments](https://www.semanticscholar.org/paper/b13d4d943bf997d33fcc340f7a943e16ff563d1f) — Evaluates code review comment quality with interpretable conceptual model.
- [Exploring the Capabilities of LLMs for Code-Change-Related Tasks](https://arxiv.org/abs/2407.02824) — Exploring the Capabilities of LLMs for Code-Change-Related Tasks.
- [Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical Study](https://arxiv.org/abs/2309.08221) — Empirical study of ChatGPT on automated code refinement and review tasks.
- [Generation-based Code Review Automation: How Far Are We?](https://arxiv.org/abs/2303.07221) — Generation-based Code Review Automation: How Far Are We?.
- [Harnessing Large Language Models for Curated Code Reviews](https://arxiv.org/abs/2502.03425) — Benchmark for LLM-generated curated code review comments with quality filtering.
- [PatchTrack: A Comprehensive Analysis of ChatGPT's Influence on Pull Request Outcomes](https://arxiv.org/abs/2505.07700) — PatchTrack: A Comprehensive Analysis of ChatGPT's Influence on Pull Request Outcomes.
- [RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian](https://arxiv.org/abs/2601.01129) — Evaluates LLM-based code review quality at scale in Atlassian production. 🏭
- [SWE-PRBench: Benchmarking AI Code Review Quality Against PR Feedback](https://arxiv.org/abs/2603.26130) — Benchmark AI code review quality against 350 human-annotated pull requests.
- [The Right Prompts for the Job: Repair Code-Review Defects with Large Language Model](https://arxiv.org/abs/2312.17485) — Benchmarks LLM prompt strategies for repairing code-review defects.
- [Towards Automating Code Review Activities](https://arxiv.org/abs/2101.02518) — Towards Automating Code Review Activities.
- [Understanding Dominant Themes in Reviewing Agentic AI-authored Code](https://arxiv.org/abs/2601.19287) — Analyzes 19,450 review comments on agent-authored PRs with 12-theme taxonomy.
- [We benchmarked 7 AI code review tools on large open-source projects](https://www.augmentcode.com/blog/we-benchmarked-7-ai-code-review-tools-on-real-world-prs-here-are-the-results) — We benchmarked 7 AI code review tools on large open-source projects.

<a id="testing"></a>
## Testing & QA

*Evaluates test generation, bug reproduction, and QA capabilities.*

### A–F

- [A Review of Large Language Models for Automated Test Case Generation](https://www.semanticscholar.org/paper/49c7ba3b6babda46a449850eb14be0ca04f3bc6d) — Review of LLM-based automated test case generation methods and effectiveness. 📋
- [ABTest: Behavior-Driven Testing for AI Coding Agents](https://arxiv.org/html/2604.03362v1) — ABTest: Behavior-Driven Testing for AI Coding Agents.
- [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](https://arxiv.org/abs/2302.06527) — Empirical evaluation of LLMs for automated unit test generation at scale.
- [AssertionBench: A Benchmark to Evaluate Large-Language Models for Assertion Generation](https://arxiv.org/abs/2406.18627) — AssertionBench: A Benchmark to Evaluate Large-Language Models for Assertion Generation.
- [Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Based Testing](https://arxiv.org/abs/2509.01616) — Generates issue-reproducing tests by combining LLMs with search-based testing.
- [Automated Unit Test Improvement using Large Language Models at Meta](https://arxiv.org/abs/2402.09171) — Automated Unit Test Improvement using Large Language Models at Meta.
- [Automating a Complete Software Test Process Using LLMs: An Automotive Case Study](https://doi.org/10.1109/ICSE55347.2025.00211) — LLM-automated software test process evaluation in automotive case study.
- [BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/abs/2604.24955) — Audits LLM agent benchmarks for spec flaws and overly strict evaluation. 🤖
- [Benchmarking LLMs for Unit Test Generation from Real-World Functions](https://arxiv.org/abs/2508.00408) — Benchmarking LLMs for Unit Test Generation from Real-World Functions.
- [Can LLMs Generate High-Quality Test Cases for Algorithm Problems? TestCase-Eval: A Systematic Evaluation of Fault Coverage and Exposure](https://arxiv.org/html/2506.12278v1) — Can LLMs Generate High-Quality Test Cases for Algorithm Problems? TestCase-Eval: A Systematic Evaluation of Fault Coverage and Exposure.
- [ChatUniTest: A Framework for LLM-Based Test Generation](https://arxiv.org/abs/2305.04764) — LLM-based automated unit test generation framework with adaptive strategies.
- [CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification](https://arxiv.org/abs/2502.08806) — CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification.
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268) — CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation.
- [Comprehend, Imitate, and then Update: Unleashing the Power of LLMs in Test Suite Evolution](https://www.semanticscholar.org/paper/914a407f6a53c0f48a2f152fd677d3ed524b3c66) — LLM-based approach for automated test suite evolution and obsolete test update.
- [Echo: Graph-Enhanced Retrieval and Execution Feedback for Issue Reproduction Test Generation](https://arxiv.org/abs/2603.07326) — Echo: Graph-Enhanced Retrieval and Execution Feedback for Issue Reproduction Test Generation.
- [Evaluating and Improving ChatGPT for Unit Test Generation](https://www.semanticscholar.org/paper/49c58278c069faaea0cdee4df9043015493bc854) — Evaluates and improves ChatGPT for unit test generation quality.

### G–L

- [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection](https://arxiv.org/abs/2508.06365) — Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection.
- [iCoRe: An Iterative Correlation-Aware Retriever for Bug Reproduction Test Generation](https://arxiv.org/abs/2604.19224) — iCoRe: An Iterative Correlation-Aware Retriever for Bug Reproduction Test Generation.
- [Investigating Test Overfitting on SWE-bench](https://arxiv.org/abs/2511.16858) — Investigating Test Overfitting on SWE-bench.
- [Issue2Test: Generating Reproducing Test Cases from Issue Reports](https://arxiv.org/abs/2503.16320) — Generates reproducing test cases from GitHub issue reports to validate fixes.
- [Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction](https://arxiv.org/abs/2209.11515) — LIBRO: LLM few-shot bug reproduction test generation from bug reports.

### M–R

- [MAGISTER: LLM-Based Test Generation with Role-Specialized Agents](https://www.semanticscholar.org/paper/874cbcf924bc4efc303582eae92e8ff438a3c1a8) — MAGISTER: LLM-Based Test Generation with Role-Specialized Agents. 🤝
- [MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact Study](https://arxiv.org/abs/2502.06556) — Benchmarks multi-file unit test generation across 3 languages and 20 projects. 🌐
- [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](https://doi.org/10.1109/ICSE55347.2025.00226) — LLM agent approach to repair non-idempotent-outcome tests.
- [No More Manual Tests? Evaluating and Improving ChatGPT for Unit Test Generation](https://arxiv.org/abs/2305.04207) — Evaluates ChatGPT for unit test generation quality and coverage.
- [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](https://arxiv.org/abs/2304.11686) — Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting.
- [Otter: Generating Tests from Issues to Validate SWE Patches](https://arxiv.org/abs/2502.05368) — Generates test cases from issue descriptions to validate SWE agent patches.
- [POSTCONDBENCH](https://arxiv.org/abs/2604.28400) — Benchmark correctness and completeness in formal postcondition inference.
- [RESTestBench: A Benchmark for Evaluating the Effectiveness of LLM-Generated REST API Test Cases from NL Requirements](https://arxiv.org/abs/2604.25862v1) — Benchmark for LLM-generated REST API test cases using mutation analysis.

### S–Z

- [Software Testing With Large Language Models: Survey, Landscape, and Vision](https://arxiv.org/abs/2307.07221) — Survey of LLMs applied to software testing tasks, landscape and vision. 📋
- [SWE-Tester: Training Open-Source LLMs for Issue Reproduction in Real-World Repositories](https://arxiv.org/abs/2601.13713) — Trains open-source LLMs to generate issue-reproducing tests from bug reports.
- [SWT-Bench](https://github.com/logic-star-ai/SWT-Bench) ⭐76 — SWT-Bench. 🐍
- [TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance](https://arxiv.org/abs/2601.18241) — TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance.
- [TestDecision: Sequential Test Suite Generation via Greedy Optimization and Reinforcement Learning](https://arxiv.org/abs/2604.01799) — TestDecision: Sequential Test Suite Generation via Greedy Optimization and Reinforcement Learning.
- [TESTEVAL: Benchmarking Large Language Models for Test Case Generation](https://arxiv.org/abs/2406.04531) — TESTEVAL: Benchmarking Large Language Models for Test Case Generation.
- [TestExplora: Benchmarking LLMs for Proactive Bug Discovery via Repository-Level Test Generation](https://arxiv.org/abs/2602.10471) — Benchmark for LLMs on proactive bug discovery via repo-level test generation.
- [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://arxiv.org/abs/2410.00752) — TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark. 🌍
- [Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage](https://arxiv.org/abs/2603.13724) — Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage.
- [UTBoost](https://github.com/CUHK-Shenzhen-SE/UTBoost) ⭐36 — Augments SWE-Bench with auto-generated unit tests to mitigate false positives.
- [When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution](https://arxiv.org/abs/2510.18270) — When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution.

<a id="security"></a>
## Security & Vulnerability

*Benchmarks for vulnerability detection, secure code generation, and penetration testing.*

### A–F

- [A User-Centered Security Evaluation of Copilot](https://arxiv.org/abs/2308.06587) — Evaluates security of GitHub Copilot-generated code via user-centered study. 🔒
- [A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code](https://arxiv.org/abs/2508.18106) — Repository-level benchmark evaluating security of AI-generated code. 🔒
- [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://openreview.net/forum?id=V4y0CpX4hK) — Formalizes and benchmarks attacks and defenses in LLM-based agents. 🔒
- [AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection](https://arxiv.org/abs/2601.19138) — Benchmarks agentic secure code review for pre-commit vulnerability detection. 🔒
- [AICGSecEval](https://github.com/Tencent/AICGSecEval) ⭐965 — AICGSecEval.
- [aicrypto-agent](https://github.com/wangyu-ovo/aicrypto-agent) ⭐30 — Benchmark evaluating LLM cryptography capabilities for AI SE agents. 🔒
- [Asleep at the Keyboard? Assessing the Security of GitHub Copilot’s Code Contributions](https://arxiv.org/abs/2108.09293) — Evaluates security vulnerabilities in GitHub Copilot's auto-generated code. 🔒
- [Assessing the Security of GitHub Copilot's Generated Code - A Targeted Replication Study](https://arxiv.org/abs/2311.11177) — Assessing the Security of GitHub Copilot's Generated Code - A Targeted Replication Study. 🔒
- [auto-pen-bench](https://github.com/lucagioacchini/auto-pen-bench) ⭐82 — Benchmarks generative agents on automated penetration testing scenarios. 🔒
- [AutoBaxBuilder: Bootstrapping Code Security Benchmarking](https://arxiv.org/abs/2512.21132) — Bootstraps code security benchmarks to evaluate LLM-generated code safety. 🔒
- [Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858) — Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX.
- [BinMetric: A Comprehensive Binary Analysis Benchmark for Large Language Models](https://arxiv.org/abs/2505.07360) — BinMetric: A Comprehensive Binary Analysis Benchmark for Large Language Models. 🔒
- [Constrained Decoding for Secure Code Generation](https://arxiv.org/abs/2405.00218) — Constrained Decoding for Secure Code Generation. 🔒
- [CS-Eval: A Comprehensive Large Language Model Benchmark for CyberSecurity](https://arxiv.org/abs/2411.16239) — Comprehensive bilingual LLM benchmark for cybersecurity tasks evaluation. 🔒
- [CVE-Bench](https://github.com/WhileBug/CVEBench) ⭐4 — Evaluates agents on understanding and fixing real CVE vulnerabilities. 🔒 🌐
- [CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](https://arxiv.org/abs/2503.17332) — Benchmarks AI agents on exploiting real-world CVE web vulnerabilities. 🔒 🌍
- [cybergym](https://github.com/sunblaze-ucb/cybergym) ⭐279 — Benchmarks AI agents on real-world vulnerability analysis at scale.
- [CyberGym: Evaluating AI Agents'Real-World Cybersecurity Capabilities at Scale](https://arxiv.org/abs/2506.02548) — CyberGym: Evaluating AI Agents'Real-World Cybersecurity Capabilities at Scale. 🔒 📦
- [CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models](https://arxiv.org/abs/2408.01605) — Benchmark suite evaluating cybersecurity risks and capabilities in LLMs. 🔒
- [Dynamic Cyber Ranges](https://arxiv.org/abs/2604.24184) — Dynamic Cyber Ranges.
- [Evaluating Large Language Models for Real-World Vulnerability Repair in C/C++ Code](https://www.semanticscholar.org/paper/db82597561835e151c417f7272455caa4d1a9d04) — Evaluating Large Language Models for Real-World Vulnerability Repair in C/C++ Code. 🔒

### G–L

- [HackSynth](https://github.com/aielte-research/HackSynth) ⭐303 — Evaluates LLM agents on autonomous penetration testing via CTF challenges.
- [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://arxiv.org/abs/2405.17238) — LLM-assisted static analysis approach for detecting security vulnerabilities. 🔒
- [Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks](https://arxiv.org/abs/2512.03262) — Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks. 🔒
- [JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/abs/2506.20170) — Benchmark for evaluating LLMs on JavaScript deobfuscation tasks. 🟨 🔒
- [Just another copy and paste? Comparing the security vulnerabilities of ChatGPT generated code and StackOverflow answers](https://arxiv.org/abs/2403.15600) — Just another copy and paste? Comparing the security vulnerabilities of ChatGPT generated code and StackOverflow answers. 🔒
- [Large Language Models for Code: Security Hardening and Adversarial Testing](https://arxiv.org/abs/2302.05319) — Large Language Models for Code: Security Hardening and Adversarial Testing. 🔒
- [LLM Security Guard for Code](https://arxiv.org/abs/2405.01103) — LLM Security Guard for Code. 🔒
- [LLMSecEval: A Dataset of Natural Language Prompts for Security Evaluations](https://arxiv.org/abs/2303.09384) — NL prompts based on CWE scenarios to evaluate security of LLM-generated code. 🔒
- [LogicEval: A Systematic Framework for Evaluating Automated Repair Techniques for Logical Vulnerabilities in Real-World Software](https://arxiv.org/abs/2604.12994) — LogicEval: A Systematic Framework for Evaluating Automated Repair Techniques for Logical Vulnerabilities in Real-World Software. 🔒

### M–R

- [MaliciousAgentSkillsBench](https://github.com/protectskills/MaliciousAgentSkillsBench) ⭐39 — Evaluates agent resilience against malicious skill injection scenarios. 🔒
- [MOCHA: Are Code Language Models Robust Against Multi-Turn Malicious Coding Prompts?](https://arxiv.org/abs/2507.19598) — Multi-turn adversarial coding prompt benchmark evaluating LLM robustness. 🔒
- [MOSAIC-Bench](https://arxiv.org/abs/2604.28901) — Measure compositional vulnerability induction in coding agents. 🔒
- [Multitask-Based Evaluation of Open-Source LLM on Software Vulnerability](https://arxiv.org/abs/2404.02056) — Multi-task evaluation of LLMs on software vulnerability using Big-Vul dataset. 🔒
- [OS-Sentinel](https://github.com/OS-Copilot/OS-Sentinel) ⭐47 — Benchmarks mobile GUI agent safety with hybrid validation for unsafe actions.
- [PentestGPT: An LLM-empowered Automatic Penetration Testing Tool](https://arxiv.org/abs/2308.06782) — Benchmarks LLM-driven automated penetration testing on real targets. 🔒
- [RealVuln: Benchmarking Rule-Based, General-Purpose LLM, and Security-Specialized Scanners on Real-World Code](https://arxiv.org/abs/2604.13764) — Benchmarks 15 vulnerability scanners on 26 Python repos with 796 annotations. 🐍
- [RedCode](https://github.com/AI-secure/RedCode) ⭐75 — Benchmark for risky code execution and generation by code agents. 🔒
- [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://arxiv.org/abs/2411.07781) — RedCode: Risky Code Execution and Generation Benchmark for Code Agents. 🔒
- [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](https://arxiv.org/abs/2409.15154) — Benchmark evaluating LLM resistance to generating malicious code. 🔒
- [Running in CIRCLE? A Simple Benchmark for LLM Code Interpreter Security](https://arxiv.org/abs/2507.19399) — Benchmark for evaluating security of LLM code interpreter environments. 🔒

### S–Z

- [SafeGenBench: A Benchmark Framework for Security Vulnerability Detection in LLM-Generated Code](https://arxiv.org/abs/2506.05692) — Benchmark for detecting security vulnerabilities in LLM-generated code. 🔒
- [scabench](https://github.com/scabench-org/scabench) ⭐110 — Benchmark for AI security audit agents on SCA and vulnerability detection tasks. 🔒
- [SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791) — Benchmark of LLM agents on real-world software security tasks. 🔒 🌍
- [SecBench: A Comprehensive Multi-Dimensional Benchmarking Dataset for LLMs in Cybersecurity](https://arxiv.org/abs/2412.20787) — Multi-dimensional benchmarking dataset for evaluating LLMs in cybersecurity. 🔒
- [SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios](https://arxiv.org/abs/2509.22097) — Benchmarks secure vibe-coding of AI agents on 105 C/C++ vulnerability tasks. 🔒
- [SecurityEval dataset: mining vulnerability examples to evaluate machine learning-based code generation techniques](https://www.semanticscholar.org/paper/71280dba5bda65c162f9deaffed7d3d20692ca0a) — Evaluates ML code generation security using real-world vulnerability samples. 🔒
- [Towards Agentic Investigation of Security Alerts](https://arxiv.org/abs/2604.25846) — Towards Agentic Investigation of Security Alerts. 🔒
- [VADER: A Human-Evaluated Benchmark for Vulnerability Assessment, Detection, Explanation, and Remediation](https://arxiv.org/abs/2505.19395) — VADER: A Human-Evaluated Benchmark for Vulnerability Assessment, Detection, Explanation, and Remediation. 🔒 👤

<a id="production"></a>
## Production-Derived

- [A Production-Derived Benchmark for Evaluating AI Coding Agents](https://arxiv.org/html/2604.01527v1) — A Production-Derived Benchmark for Evaluating AI Coding Agents. 🏭
- [AutoMat](https://arxiv.org/abs/2604.29200) — Evaluate coding agents on reproducing computational materials science.
- [Bots Don’t Mind Waiting, Do They? Comparing the Interaction With Automatically and Manually Created Pull Requests](https://arxiv.org/abs/2103.03591) — Compares acceptance and wait time of bot vs human pull requests in OSS projects.
- [CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs](https://arxiv.org/abs/2506.11059) — Multi-lingual benchmark for detecting AI-generated and paraphrased source code. 🌐
- [CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend](https://arxiv.org/abs/2604.23455) — CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend.
- [From Translation to Superset: Benchmark-Driven Evolution of a Production AI Agent from Rust to Python](https://arxiv.org/abs/2604.11518v1) — From Translation to Superset: Benchmark-Driven Evolution of a Production AI Agent from Rust to Python. 🏭 🦀 🐍
- [Hot Fixing in the Wild](https://arxiv.org/abs/2604.26892v1) — Hot Fixing in the Wild. 🏭
- [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384) — LinuxArena: A Control Setting for AI Agents in Live Production Software Environments. 🏭
- [Production-Derived Benchmark](https://arxiv.org/html/2604.01527v2) — Production-Derived Benchmark. 🏭 🌍
- [Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming](https://arxiv.org/abs/2210.14306) — Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming.
- [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779) — SWE-chat: Coding Agent Interactions From Real Users in the Wild. 🌍
- [SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads?](https://arxiv.org/abs/2511.06090) — SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads?.
- [SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?](https://arxiv.org/abs/2507.12415) — Benchmark for code performance optimization on real-world repos.

<a id="code-generation"></a>
## Code Generation

### A–F

- [A Closer Look at Different Difficulty Levels Code Generation Abilities of ChatGPT](https://www.semanticscholar.org/paper/f1847504a4895a3d31c31e7464e5b34d9eda8ef8) — Evaluates ChatGPT code generation across difficulty levels using benchmarks.
- [A Large-scale Class-level Benchmark Dataset for Code Generation with LLMs](https://arxiv.org/abs/2504.15564) — Large-scale class-level benchmark dataset for evaluating LLM code generation.
- [Agents4PLC: Automating Closed-loop PLC Code Generation and Verification in Industrial Control Systems using LLM-based Agents](https://arxiv.org/abs/2410.14209) — Agents4PLC: Automating Closed-loop PLC Code Generation and Verification in Industrial Control Systems using LLM-based Agents.
- [ai-coding-lang-bench](https://github.com/mame/ai-coding-lang-bench) ⭐151 — Benchmarks AI code generation across 13 programming languages. 🌐
- [An Empirical Evaluation of GitHub Copilot's Code Suggestions](https://www.semanticscholar.org/paper/cdfe9580f63070f311151444f9df32818cc858bf) — An Empirical Evaluation of GitHub Copilot's Code Suggestions.
- [ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation](https://arxiv.org/abs/2507.04952) — ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation.
- [Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation](https://arxiv.org/abs/2604.21505) — Assessing the Impact of Requirement Ambiguity on LLM-based Function-Level Code Generation.
- [AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators](https://arxiv.org/abs/2508.09101) — LLM-based automatic generation of code benchmarks for evaluating coding ability.
- [BaxBench: Can LLMs Generate Correct and Secure Backends?](https://arxiv.org/abs/2502.11844) — Evaluates LLM ability to generate correct and secure backend modules. 🔒
- [Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models](https://arxiv.org/abs/2407.11470) — Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models.
- [Beyond Output Correctness: Benchmarking and Evaluating Large Language Model Reasoning in Coding Tasks](https://arxiv.org/abs/2604.12379) — Benchmarks LLM reasoning quality across code generation and summarization tasks. 🔍
- [bigcodebench](https://github.com/bigcode-project/bigcodebench) ⭐499 — Benchmarks LLMs on complex function calls, tool use, and instruction following.
- [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://arxiv.org/abs/2406.15877) — Benchmarks code generation with diverse function calls and complex instructions.
- [CATCODER: Repository-Level Code Generation with Relevant Code and Type Context](https://arxiv.org/abs/2406.03283) — Evaluates repo-level code generation with integrated contextual information.
- [CETBench: A Novel Dataset constructed via Transformations over Programs for Benchmarking LLMs for Code-Equivalence Checking](https://arxiv.org/abs/2506.04019) — CETBench: A Novel Dataset constructed via Transformations over Programs for Benchmarking LLMs for Code-Equivalence Checking.
- [ClassEval-Pro: A Cross-Domain Benchmark for Class-Level Code Generation](https://arxiv.org/abs/2604.26923v1) — Cross-domain benchmark for class-level compositional code generation evaluation.
- [ClassEval: A Manually-Crafted Benchmark for Evaluating LLMs on Class-level Code Generation](https://arxiv.org/abs/2308.01861) — Class-level Python code generation benchmark with 100 tasks evaluating 11 LLMs. 🐍
- [Co-Located Tests, Better AI Code: How Test Syntax Structure Affects Foundation Model Code Generation](https://arxiv.org/abs/2604.19826) — Co-Located Tests, Better AI Code: How Test Syntax Structure Affects Foundation Model Code Generation.
- [CoCo-Bench: A Comprehensive Code Benchmark For Multi-task Large Language Model Evaluation](https://arxiv.org/abs/2504.20673) — Comprehensive multi-task code benchmark for evaluating LLMs across coding tasks.
- [CoCoNUT: Structural Code Understanding does not fall out of a tree](https://arxiv.org/abs/2501.16456) — Benchmarks LLM structural code understanding beyond surface-level generation.
- [Code-Vision: Evaluating Multimodal LLMs Logic Understanding and Code Generation Capabilities](https://arxiv.org/abs/2502.11829) — Benchmark evaluating multimodal LLMs on code generation from flowcharts.
- [Code2Bench: Scaling Source and Rigor for Dynamic Benchmark Construction](https://arxiv.org/abs/2508.07180) — Dynamic benchmark construction to evaluate LLMs on real-world code tasks. 🌍
- [CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges](https://arxiv.org/abs/2401.07339) — Repo-level code generation benchmark for tool-integrated agent systems.
- [CodeBenchGen: Creating Scalable Execution-based Code Generation Benchmarks](https://arxiv.org/abs/2404.00566) — Framework for automatically creating execution-based code generation benchmarks.
- [CodeFlowBench: A Multi-turn, Iterative Benchmark for Complex Code Generation](https://arxiv.org/abs/2504.21751) — Multi-turn iterative benchmark for evaluating complex code generation tasks.
- [codefuse-evaluation](https://github.com/codefuse-ai/codefuse-evaluation) ⭐109 — codefuse-evaluation.
- [CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Benchmarking on HumanEval-X](https://arxiv.org/abs/2303.17568) — HumanEval-X multilingual benchmark for code generation evaluation. 🌐
- [CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts](https://arxiv.org/abs/2505.05063) — CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts. 🌐
- [CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding &amp; Reasoning Capabilities of CodeLLMs](https://arxiv.org/abs/2410.01999) — Multi-task benchmark evaluating code understanding capabilities of code LLMs.
- [CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models](https://arxiv.org/abs/2302.00288) — CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models.
- [CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark for Evaluating LLMs on Code Understanding and Generation](https://arxiv.org/abs/2311.08588) — CodeScope: An Execution-based Multilingual Multitask Multidimensional Benchmark for Evaluating LLMs on Code Understanding and Generation. 🌐
- [CodeUpdateArena: Benchmarking Knowledge Editing on API Updates](https://arxiv.org/abs/2407.06249) — Benchmark for evaluating LLM code generation after API updates.
- [CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation](https://arxiv.org/abs/2102.04664) — CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation.
- [Collu-Bench: A Benchmark for Predicting Language Model Hallucinations in Code](https://arxiv.org/abs/2410.09997) — Benchmark for predicting language model hallucinations in generated code.
- [Competition-Level Code Generation with AlphaCode](https://arxiv.org/abs/2203.07814) — Competition-Level Code Generation with AlphaCode.
- [Competition-Level Problems are Effective LLM Evaluators](https://arxiv.org/abs/2312.02143) — Competition-Level Problems are Effective LLM Evaluators.
- [ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Code](https://arxiv.org/abs/2409.10280) — ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Code.
- [ConvCodeWorld: Benchmarking Conversational Code Generation in Reproducible Feedback Environments](https://openreview.net/forum?id=rpouyo09V0) — ConvCodeWorld: Benchmarking Conversational Code Generation in Reproducible Feedback Environments.
- [CrossCodeEval: Multilingual Repository-Level Code Completion Benchmark](https://crosscodeeval.github.io/) — CrossCodeEval: Multilingual Repository-Level Code Completion Benchmark. 🌐
- [CRUST-Bench: A Comprehensive Benchmark for C-to-safe-Rust Transpilation](https://arxiv.org/abs/2504.15254) — Benchmark for evaluating C-to-safe-Rust transpilation by AI agents. 🦀
- [CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution](https://arxiv.org/abs/2401.03065) — Benchmark testing LLM code reasoning, understanding, and execution capabilities.
- [da-code](https://github.com/yiyihum/da-code) ⭐95 — Benchmarks agent code generation on real-world data science tasks.
- [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](https://arxiv.org/abs/2410.07331) — Benchmark for evaluating LLM code generation in data science tasks.
- [Defective Task Descriptions in LLM-Based Code Generation: Detection and Analysis](https://arxiv.org/abs/2604.24703) — Defective Task Descriptions in LLM-Based Code Generation: Detection and Analysis.
- [Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Engineering](https://arxiv.org/abs/2403.03163) — Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Engineering.
- [DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation](https://arxiv.org/abs/2506.06251) — Benchmark for evaluating multimodal LLMs on front-end code generation tasks.
- [DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories](https://arxiv.org/abs/2405.19856) — DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories. 🌍
- [Drawing Pandas: A Benchmark for LLMs in Generating Plotting Code](https://arxiv.org/abs/2412.02764) — Benchmark for evaluating LLMs on generating data visualization plotting code.
- [DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation](https://arxiv.org/abs/2211.11501) — Benchmark of 1000 data science code generation problems from StackOverflow. 🐍
- [DS-Bench: A Realistic Benchmark for Data Science Code Generation](https://arxiv.org/abs/2505.15621) — Benchmark for evaluating code generation on realistic data science tasks.
- [DynaCode: A Dynamic Complexity-Aware Code Benchmark for Evaluating Large Language Models in Code Generation](https://arxiv.org/abs/2503.10452) — Dynamic complexity-aware benchmark for evaluating LLMs on code generation.
- [Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination](https://arxiv.org/abs/2503.04149) — Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination.
- [ECCO: Can We Improve Model-Generated Code Efficiency Without Sacrificing Functional Correctness?](https://arxiv.org/abs/2407.14044) — Benchmark evaluating LLM-generated code efficiency vs functional correctness.
- [EDIT-Bench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits](https://arxiv.org/abs/2511.04486) — Benchmarks LLM instructed code editing on 540 real-world edit tasks. 🌍
- [EffiBench-X: A Multi-Language Benchmark for Measuring Efficiency of LLM-Generated Code](https://arxiv.org/abs/2505.13004) — Multi-language benchmark measuring efficiency of LLM-generated code. 🌐
- [EffiBench: Benchmarking the Efficiency of Automatically Generated Code](https://arxiv.org/abs/2402.02037) — Benchmark evaluating efficiency of LLM-generated code beyond correctness.
- [ELABORATION: A Comprehensive Benchmark on Human-LLM Competitive Programming](https://arxiv.org/abs/2505.16667) — Benchmark comparing human and LLM performance on competitive programming tasks.
- [Escalating LLM-based Code Translation Benchmarking into the Class-level Era](https://arxiv.org/abs/2411.06145) — Escalating LLM-based Code Translation Benchmarking into the Class-level Era.
- [eval-dev-quality](https://github.com/symflower/eval-dev-quality) ⭐185 — Evaluates LLM code generation quality across multiple languages and tasks. 🌐
- [Evaluating Language Models for Efficient Code Generation](https://arxiv.org/abs/2408.06450) — Benchmark evaluating LLMs on generating efficient code beyond correctness.
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — Evaluates LLM code generation correctness via pass@k on HumanEval benchmark.
- [Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks](https://arxiv.org/abs/2403.04814) — Syntax-aware fill-in-the-middle benchmark for LLMs across multiple languages.
- [EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code Repositories](https://arxiv.org/abs/2404.00599) — Evolving code generation benchmark aligned with real-world code repositories. 🌍
- [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://arxiv.org/abs/2410.22821) — EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations.
- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) — Executable Code Actions Elicit Better LLM Agents.
- [Exploring Language Model's Code Generation Ability with Auxiliary Functions](https://arxiv.org/abs/2403.10575) — Benchmark evaluating LLM code generation with auxiliary/helper function usage.
- [FrontendBench: A Benchmark for Evaluating LLMs on Front-End Development via Automatic Evaluation](https://arxiv.org/abs/2506.13832) — Benchmark for evaluating LLMs on front-end development with auto evaluation.

### G–L

- [GitChameleon: Unmasking the Version-Switching Capabilities of Code Generation Models](https://arxiv.org/abs/2411.05830) — Benchmark testing LLM ability to generate code for specific library versions.
- [Github](https://github.com/openai/human-eval) — HumanEval: OpenAI benchmark for evaluating code generation from docstrings. 🐍
- [How Efficient is LLM-Generated Code? A Rigorous & High-Standard Benchmark](https://arxiv.org/abs/2406.06647) — Benchmark measuring efficiency of LLM-generated code with rigorous evaluation.
- [HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self-invoking Code Generation](https://arxiv.org/abs/2412.21199) — HumanEval Pro & MBPP Pro benchmarks for self-invoking code generation by LLMs.
- [HumanEval-V: Benchmarking High-Level Visual Reasoning with Complex Diagrams in Coding Tasks](https://arxiv.org/abs/2410.12381) — HumanEval-V: Benchmarking High-Level Visual Reasoning with Complex Diagrams in Coding Tasks.
- [HumanEvo: An Evolution-aware Benchmark for More Realistic Evaluation of Repository-level Code Generation](https://arxiv.org/abs/2406.06918) — HumanEvo: An Evolution-aware Benchmark for More Realistic Evaluation of Repository-level Code Generation.
- [ICPC-Eval: Probing the Frontiers of LLM Reasoning with Competitive Programming Contests](https://arxiv.org/abs/2506.04894) — Benchmark using ICPC competitive programming problems to evaluate LLM reasoning.
- [IFEvalCode: Controlled Code Generation](https://arxiv.org/abs/2507.05269) — IFEvalCode: Controlled Code Generation.
- [IndustryCode: A Benchmark for Industry Code Generation](https://arxiv.org/abs/2604.02729) — IndustryCode: A Benchmark for Industry Code Generation. 🌐
- [InfiBench: Evaluating the Question-Answering Capabilities of Code Large Language Models](https://arxiv.org/abs/2404.07940) — Benchmark evaluating question-answering capabilities of code LLMs.
- [Interaction2Code: Benchmarking MLLM-based Interactive Webpage Code Generation from Interactive Prototyping](https://arxiv.org/abs/2411.03292) — Benchmark for MLLM-based interactive webpage code generation from UI prototypes.
- [Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation](https://arxiv.org/abs/2305.01210) — Augments HumanEval/MBPP tests to rigorously evaluate LLM code correctness.
- [JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models](https://arxiv.org/abs/2406.12902) — Java OOP code generation benchmark evaluating LLMs at class/project granularity. ☕
- [L2CEval: Evaluating Language-to-Code Generation Capabilities of Large Language Models](https://arxiv.org/abs/2309.17446) — Benchmark evaluating language-to-code generation capabilities of LLMs.
- [LeetCodeDataset: A Temporal Dataset for Robust Evaluation and Efficient Training of Code LLMs](https://arxiv.org/abs/2504.14655) — Temporal LeetCode dataset for evaluating and training code LLMs.
- [LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://arxiv.org/abs/2412.04478) — Benchmark for generating code targeting specific library versions.
- [LiCoEval: Evaluating LLMs on License Compliance in Code Generation](https://arxiv.org/abs/2408.02487) — LiCoEval: Evaluating LLMs on License Compliance in Code Generation.
- [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) ⭐854 — LiveCodeBench.
- [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion](https://arxiv.org/abs/2406.09834) — Evaluates LLM code completion for deprecated API usage during library evolution.

### M–R

- [M2rc-Eval: Massively Multilingual Repository-level Code Completion Evaluation](https://arxiv.org/abs/2410.21157) — Multilingual repo-level code completion benchmark spanning many languages. 🌐
- [MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization](https://arxiv.org/abs/2402.11453) — Benchmark and method for evaluating LLM agents on scientific data visualization.
- [MCoNaLa: A Benchmark for Code Generation from Multiple Natural Languages](https://arxiv.org/abs/2203.08388) — Benchmark for code generation from multilingual natural language intents. 🌐
- [Measuring Coding Challenge Competence With APPS](https://arxiv.org/abs/2105.09938) — APPS benchmark for measuring code generation on coding challenges.
- [Measuring The Impact Of Programming Language Distribution](https://arxiv.org/abs/2302.01973) — Measuring The Impact Of Programming Language Distribution. 🌐
- [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://arxiv.org/abs/2402.07844) — Mercury: A Code Efficiency Benchmark for Code Large Language Models.
- [ML-Bench](https://github.com/gersteinlab/ML-Bench) ⭐316 — Evaluates LLM/agent ML task completion on 10K+ samples across 18 GitHub repos.
- [MMCode: Benchmarking Multimodal Large Language Models for Code Generation with Visually Rich Programming Problems](https://arxiv.org/abs/2404.09486) — Benchmark for code generation from visually rich problems using multimodal LLMs.
- [Multi-lingual Evaluation of Code Generation Models](https://arxiv.org/abs/2210.14868) — Multi-lingual Evaluation of Code Generation Models. 🌐
- [Multilingual Multimodal Software Developer for Code Generation](https://arxiv.org/abs/2507.08719) — Multilingual multimodal benchmark for evaluating code generation agents. 🌐
- [MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation](https://arxiv.org/abs/2208.08227) — MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation. 🌐
- [Natural Language to Code Generation in Interactive Data Science Notebooks](https://arxiv.org/abs/2212.09248) — ARCADE: 1078 NL-to-code benchmark for pandas tasks in Jupyter notebooks.
- [nl2code-dataset](https://github.com/aixcoder-plugin/nl2code-dataset) ⭐51 — Aix-bench: natural language to Java code synthesis evaluation benchmark dataset. ☕
- [No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT](https://arxiv.org/abs/2308.04838) — No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT. 🔒
- [NoFunEval: Funny How Code LMs Falter on Requirements Beyond Functional Correctness](https://arxiv.org/abs/2401.15963) — NoFunEval: Funny How Code LMs Falter on Requirements Beyond Functional Correctness. 🔒
- [OJBench: A Competition Level Code Benchmark For Large Language Models](https://arxiv.org/abs/2506.16395) — Competition-level code generation benchmark for LLMs from online judges.
- [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](https://arxiv.org/abs/2308.08961) — Taxonomy and benchmark for evaluating neural code translation models.
- [OOP: Object-Oriented Programming Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2401.06628) — Benchmark evaluating LLMs on object-oriented programming tasks.
- [PlayCoder: Making LLM-Generated GUI Code Playable](https://arxiv.org/abs/2604.19742) — PlayCoder: Making LLM-Generated GUI Code Playable.
- [Plot2Code: A Comprehensive Benchmark for Evaluating Multi-modal Large Language Models in Code Generation from Scientific Plots](https://arxiv.org/abs/2405.07990) — Benchmark evaluating MLLMs on generating executable code from scientific plots.
- [PPM: Automated Generation of Diverse Programming Problems for Benchmarking Code Generation Models](https://arxiv.org/abs/2401.15545) — PPM: Automated Generation of Diverse Programming Problems for Benchmarking Code Generation Models.
- [ProgramBench](https://arxiv.org/abs/2604.28500) — Evaluate if LLMs can rebuild programs from scratch.
- [Python Code Generation by Asking Clarification Questions](https://arxiv.org/abs/2212.09885) — Benchmark for Python code generation with clarification question asking. 🐍
- [QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies](https://arxiv.org/abs/2604.15151) — Evaluates LLM quantitative trading strategy code generation with backtesting.
- [React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend](https://arxiv.org/abs/2604.17187) — React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend.
- [ReCode: Robustness Evaluation of Code Generation Models](https://arxiv.org/abs/2212.10264) — Robustness evaluation benchmark for code generation models via perturbations.
- [ReCUBE: Evaluating Repository-Level Context Utilization in Code Generation](https://arxiv.org/abs/2603.25770) — Evaluates LLM cross-file context utilization in repo-level code generation.
- [Refining ChatGPT-Generated Code: Characterizing and Mitigating Code Quality Issues](https://arxiv.org/abs/2307.12596) — Characterizes and mitigates code quality issues in ChatGPT-generated code.
- [RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark](https://arxiv.org/html/2406.11927v2) — RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark.
- [ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code](https://arxiv.org/abs/2506.02314) — Benchmark for LLMs implementing novel ML research code from papers.
- [RTLLM: An Open-Source Benchmark for Design RTL Generation with Large Language Model](https://arxiv.org/abs/2308.05345) — Benchmark for RTL hardware design generation from natural language using LLMs.
- [RustEvo^2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://arxiv.org/abs/2503.16922) — Evolving benchmark for evaluating LLM Rust code generation under API changes. 🦀

### S–Z

- [Self-Edit: Fault-Aware Code Editor for Code Generation](https://arxiv.org/abs/2305.04087) — Generate-and-edit approach using execution feedback to improve LLM code quality.
- [Sketch2Code: Evaluating Vision-Language Models for Interactive Web Design Prototyping](https://arxiv.org/abs/2410.16232) — Benchmark evaluating VLMs on converting UI sketches to web code.
- [sniffbench](https://github.com/AnswerLayer/sniffbench) ⭐27 — Lightweight sniff-test benchmark for quick evaluation of coding agents.
- [STEPWISE-CODEX-Bench: Evaluating Complex Multi-Function Comprehension and Fine-Grained Execution Reasoning](https://arxiv.org/abs/2508.05193) — Benchmark for multi-function comprehension and fine-grained execution reasoning.
- [StudentEval: A Benchmark of Student-Written Prompts for Large Language Models of Code](https://arxiv.org/abs/2306.04556) — Benchmark of student-written prompts evaluating LLM code generation ability.
- [Success is in the Details: Evaluate and Enhance Details Sensitivity of Code](https://arxiv.org/abs/2505.14597) — Benchmark evaluating LLM sensitivity to code details for code generation.
- [svelte-bench](https://github.com/khromov/svelte-bench) ⭐168 — Benchmarks LLM code generation for Svelte 5 using HumanEval methodology.
- [SVGEditBench: A Benchmark Dataset for Quantitative Assessment of LLM's SVG Editing Capabilities](https://arxiv.org/abs/2404.13710) — Benchmark for evaluating LLM capabilities in editing SVG code.
- [Synthesizing Performance Constraints for Evaluating and Improving Code Efficiency](https://arxiv.org/abs/2505.23471) — Synthesizes performance constraints to evaluate and improve code efficiency.
- [TACO: Topics in Algorithmic COde generation dataset](https://arxiv.org/abs/2312.14852) — TACO: Topics in Algorithmic COde generation dataset.
- [The Path Not Taken: Duality in Reasoning about Program Execution](https://arxiv.org/abs/2604.20917) — The Path Not Taken: Duality in Reasoning about Program Execution.
- [Towards an understanding of large language models in software engineering tasks](https://arxiv.org/abs/2308.11396) — Towards an understanding of large language models in software engineering tasks. 📋
- [TRACY: Benchmarking Execution Efficiency of LLM-Based Code Translation](https://arxiv.org/abs/2508.11468) — Benchmark for evaluating execution efficiency of LLM-based code translation.
- [Unraveling the Potential of Large Language Models in Code Translation: How Far Are We?](https://arxiv.org/abs/2410.09812) — Unraveling the Potential of Large Language Models in Code Translation: How Far Are We?. 🌐
- [VerilogEval Evaluating Large Language Models for Verilog Code Generation](https://arxiv.org/abs/2309.07544) — VerilogEval Evaluating Large Language Models for Verilog Code Generation.
- [verina](https://github.com/sunblaze-ucb/verina) ⭐61 — Benchmark for verifiable code, specification, and proof generation evaluation.
- [VERINA: Benchmarking Verifiable Code Generation](https://arxiv.org/abs/2505.23135) — Benchmark for evaluating verifiable code generation with formal specifications.
- [VersiCode: Towards Version-controllable Code Generation](https://arxiv.org/abs/2406.07411) — Benchmark for generating code targeting specific library/API versions.
- [Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs](https://arxiv.org/abs/2406.20098) — Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs.
- [WebCode2M: A Real-World Dataset for Code Generation from Webpage Designs](https://arxiv.org/abs/2404.06369) — WebCode2M: A Real-World Dataset for Code Generation from Webpage Designs.
- [WebCode: Search Evals for Coding Agents](https://exa.ai/blog/webcode) — WebCode: benchmark evaluating coding agents on web search capabilities.
- [WebGen-Bench: Evaluating LLMs on Generating Interactive and Functional Websites from Scratch](https://arxiv.org/abs/2505.03733) — WebGen-Bench: Evaluating LLMs on Generating Interactive and Functional Websites from Scratch.
- [When Prompt Under-Specification Improves Code Correctness: An Exploratory Study of Prompt Wording and Structure Effects on LLM-Based Code Generation](https://arxiv.org/abs/2604.24712) — Study of prompt wording/structure effects on LLM code generation correctness.
- [wp-bench](https://github.com/WordPress/wp-bench) ⭐51 — wp-bench.
- [xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval](https://arxiv.org/abs/2303.03004) — xCodeEval: A Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval. 🌐
- [[data](https://github.com/ProsusAI/stack-eval) — Stack-Eval: benchmark for evaluating code generation from Stack Overflow data.

<a id="feature-development"></a>
## Feature Development

- [A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task](https://arxiv.org/html/2603.26337) — A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task.
- [Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and Evaluation](https://arxiv.org/html/2510.24358v1) — Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and Evaluation.
- [CodeAssistBench (Amazon Science)](https://www.amazon.science/code-and-datasets/codeassistbench) — CodeAssistBench (Amazon Science). 🤝
- [CodeAssistBench (CAB): Dataset &amp; Benchmarking for Multi-turn Chat-Based Code Assistance](https://arxiv.org/abs/2507.10646) — Multi-turn chat-based code assistance benchmark with real GitHub issues.
- [FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation for Feature Implementation](https://arxiv.org/abs/2503.06680) — Benchmark for repo-level feature implementation from 83 GitHub repos' PRs.
- [FeatureBench](https://github.com/LiberCoders/FeatureBench) ⭐58 — FeatureBench.
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://arxiv.org/abs/2602.10975) — Benchmarks agentic coding on complex multi-PR feature development tasks. 📅
- [NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Feature Addition](https://arxiv.org/abs/2507.18130) — NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Feature Addition.

<a id="multi-agent"></a>
## Multi-Agent

- [AgentArch](https://github.com/ServiceNow/AgentArch) ⭐11 — AgentArch.
- [CADMAS-CTX: Contextual Capability Calibration for Multi-Agent Delegation](https://arxiv.org/abs/2604.17950v1) — CADMAS-CTX: Contextual Capability Calibration for Multi-Agent Delegation. 🤝
- [CooperBench](https://github.com/cooperbench/CooperBench) ⭐11 — CooperBench. 🤝
- [GAMMAF: A Common Framework for Graph-Based Anomaly Monitoring Benchmarking in LLM Multi-Agent Systems](https://arxiv.org/abs/2604.24477) — GAMMAF: A Common Framework for Graph-Based Anomaly Monitoring Benchmarking in LLM Multi-Agent Systems. 🤝 🔒
- [LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review](https://arxiv.org/abs/2604.16321) — LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review. 🤝
- [MARBLE](https://github.com/ulab-uiuc/MARBLE) ⭐251 — MARBLE. 🤝
- [MASArena](https://github.com/LINs-lab/MASArena) ⭐38 — MASArena. 🤝
- [MultiAgentBench ACL 2025](https://aclanthology.org/2025.acl-long.421) — MultiAgentBench ACL 2025. 🤝
- [MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents](https://arxiv.org/html/2503.01935) — MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents. 🤝
- [open-multi-agent](https://github.com/JackChen-me/open-multi-agent) — Open benchmark framework for evaluating multi-agent systems. 🤝
- [Paper - ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) — Paper - ChatDev: Communicative Agents for Software Development. 🤝
- [Paper - MetaGPT: Meta Programming for Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) — Multi-agent framework encoding SOPs for collaborative software development. 🤝
- [SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution](https://arxiv.org/abs/2507.23348) — SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution. 🤝
- [sweet_rl](https://github.com/facebookresearch/sweet_rl) ⭐266 — Benchmarks multi-turn collaborative reasoning for LLM agent training.
- [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories](https://arxiv.org/abs/2604.07223) — TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories.

---

[← Back to README](../README.md)
