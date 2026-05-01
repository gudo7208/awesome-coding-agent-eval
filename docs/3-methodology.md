# ③ Evaluation Methodology

Different scoring approaches, each with trade-offs.

## Contents

- [LLM-as-Judge (46)](#llm-judge)
- [Process Evaluation (45)](#process-eval)
- [Execution-based (23)](#execution-based)
- [Hybrid (10)](#hybrid)
- [Human Evaluation (9)](#human-eval)

<a id="llm-judge"></a>
## LLM-as-Judge

*Using LLMs to score agent outputs. Faster than execution-based but less reliable. Calibrate carefully.*

### A–F

- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — Surveys LLM-as-a-Judge scoring modes, biases, consistency, and applications. 🤖 📋
- [Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934) — Uses agent judges for process-level evaluation of agentic system outputs. 🤖 🔍
- [Agent-Eval-Refine](https://github.com/Berkeley-NLP/Agent-Eval-Refine) ⭐149 — Uses LLM to evaluate agent trajectories and generate refinement feedback.
- [AI-powered Code Review with LLMs: Early Results](https://arxiv.org/abs/2404.18496) — LLM-based AI agent for automated code review, detecting bugs and code smells. 🤖
- [An LLM-as-Judge Metric for Bridging the Gap with Human Evaluation in SE Tasks](https://arxiv.org/abs/2505.20854) — LLM-as-Judge metric bridging gap with human evaluation for SE tasks. 🤖
- [Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Dis](https://aclanthology.org/2025.acl-long.223/) — Auto-Arena: automated LLM evaluation via agent peer battles and committee discus. 🤖 🤝
- [AutoReviewer](https://github.com/gvasilei/AutoReviewer) ⭐48 — LLM-based automatic code review tool using language models. 🤖
- [AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Mult](https://arxiv.org/abs/2512.20159) — Benchmarks LLM-as-a-Judge for code via rule-based perturbation and multi-source . 🤖
- [Can GPT-4 Replicate Empirical Software Engineering Research?](https://arxiv.org/abs/2310.01727) — Evaluates GPT-4's ability to replicate empirical SE research studies. 🤖
- [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Softw](https://arxiv.org/abs/2502.06193) — Empirical study on LLM-as-judge replacing human evaluators in software engineeri. 🤖
- [code-agent-eval](https://github.com/amazon-science/code-agent-eval) ⭐10 — Evaluates agent-generated code patches using LLM critics without execution. 🤖
- [CODE-DITING: A Reasoning-Based Metric for Functional Alignment in Code Evaluatio](https://arxiv.org/abs/2505.19502) — LLM reasoning-based metric for evaluating functional alignment of generated code. 🤖
- [CodeJudge-Eval: Can Large Language Models be Good Judges in Code Understanding?](https://arxiv.org/abs/2408.10718) — Benchmark evaluating LLMs as judges of code correctness for code understanding. 🤖
- [CodeJudgeBench](https://arxiv.org/abs/2507.10535) — Benchmarks LLM-as-Judge reliability on code tasks, revealing bias and limits. 🤖
- [CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models ](https://arxiv.org/abs/2403.09032) — LLM-as-a-Judge dataset for aligning code LLMs with user preferences. 🤖
- [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedbac](https://arxiv.org/abs/2409.19715) — Environment for training and evaluating LLM-generated feedback on erroneous code.
- [Comparing Developer and LLM Biases in Code Evaluation](https://arxiv.org/abs/2603.24586) — Compares developer and LLM biases in code evaluation using TRACE framework. 🤖
- [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891) — Studies interventions that hide emergent misalignment via contextual triggers in.
- [Correlating Automated and Human Evaluation of Code Documentation Generation Quality](https://www.semanticscholar.org/paper/3f673691509b430a3c57040928008b9949508987) — Correlates automated metrics vs human eval for code documentation generation. 👤
- [CritiqueLLM: Towards an Informative Critique Generation Model for Evaluation of ](https://arxiv.org/abs/2311.18702) — Trains LLMs to generate informative critiques for pointwise and pairwise evaluat. 🤖
- [CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims a](https://arxiv.org/abs/2409.19801) — Reference-free metric scoring code review comments via code claims and smells.
- [DeepCRCEval: Revisiting the Evaluation of Code Review Comment Generation](https://arxiv.org/abs/2412.18291) — Proposes semantic-based framework for evaluating code review comment generation. 🤖
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Ti](https://arxiv.org/abs/2504.15253) — Benchmarks LLM-as-Judge reliability for evaluating test-time compute scaling. 🤖
- [Foundational Automatic Evaluators: Scaling Multi-Task Generative Evaluator Train](https://arxiv.org/abs/2510.17793) — Trains multi-task generative evaluator on 2.5M samples for pairwise and stepwise. 🤖
- [From Code to Courtroom: LLMs as the New Software Judges](https://arxiv.org/abs/2503.02246) — Survey of LLM-as-a-Judge paradigm for evaluating SE tasks like code generation. 🤖 📋

### G–L

- [How Trustworthy Are LLM-as-Judge Ratings for Interpretive Responses? Implications for Qualitative Research Workflows](https://arxiv.org/abs/2604.00008) — Study examining LLM-as-judge alignment with human judgments for interpretive res. 🤖 👤
- [Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement ](https://arxiv.org/abs/2510.23038) — Trains LLM judges via tool-integrated reinforcement learning with code executor. 🤖
- [Issue-Oriented Agent-Based Framework for Automated Review Comment Generation](https://arxiv.org/abs/2511.00517) — Multi-agent framework for automated code review comment generation. 🤝 🤖
- [JudgeBench: A Benchmark for Evaluating LLM-based Judges](https://arxiv.org/abs/2410.12784) — Benchmark for evaluating reliability of LLM-based judges on challenging tasks. 🤖
- [JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://arxiv.org/abs/2310.17631) — Fine-tunes LLMs as scalable judges for evaluating open-ended LLM outputs. 🤖
- [Judging LLM-as-a-judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — Studies LLM-as-a-judge biases and proposes MT-Bench and Chatbot Arena frameworks. 🤖
- [Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge](https://arxiv.org/abs/2406.07791) — Studies position bias in LLM-as-a-Judge with stability, consistency, and fairnes. 🤖
- [Leveraging Large Language Model for Automatic Patch Correctness Assessment](https://www.semanticscholar.org/paper/3c00979b598d834b92dbd0fd8e4399d594802de3) — Uses LLMs to assess correctness of auto-generated patches against overfitting. 🤖
- [LLM as a Judge](https://www.semanticscholar.org/paper/1c629669812cf4cdc354de1f6d36084a4b2adc8c) — Studies LLM-as-judge for automated evaluation, analyzing human alignment and bia. 🤖
- [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) — Trains LLM critic models to generate NL feedback helping catch bugs in LLM code. 🤖
- [LLM-as-a-Judge for Scalable Test Coverage Evaluation](https://arxiv.org/html/2512.01232) — LLM-as-judge approach for scalable test coverage evaluation across model configs. 🤖
- [LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road](https://www.semanticscholar.org/paper/04745b236cf9ebdb06f33d14afa5e7541775af6c) — Survey on LLM-as-a-Judge in SE: potential, limitations, and future directions. 🤖 📋
- [LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road Ahead](https://arxiv.org/abs/2510.24367) — Literature review of LLM-as-a-Judge paradigm for evaluating SE artifacts. 🤖 📋

### M–R

- [Making Bias Non-Predictive: Training Robust LLM Judges via Reinforcement Learnin](https://www.semanticscholar.org/paper/d3c5ff93edbc9b37bcd3657acbebe276c650b18a) — RL-based training method to make LLM judge biases non-predictive for robustness. 🤖
- [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimizati](https://arxiv.org/abs/2306.05087) — Trains dedicated judge model to auto-evaluate instruction-tuned LLM outputs. 🤖
- [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Lang](https://arxiv.org/abs/2405.01535) — Open-source LLM judge for evaluating LM outputs via direct scoring and pairwise . 🤖
- [Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery](https://arxiv.org/abs/2604.19049v1) — Adversarial multi-agent review pipeline to improve precision in LLM defect disco. 🤝
- [ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding](https://arxiv.org/abs/2510.11498) — RL framework using multimodal LLM as visual critic for front-end code evaluation. 🤖
- [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) — Integrates chain-of-thought reasoning into reward models for interpretable LLM j. 🤖

### S–Z

- [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) — Iteratively improves LLM-as-Judge evaluators using only synthetic data. 🤖
- [Vibe Checker: Aligning Code Evaluation with Human Preference](https://arxiv.org/abs/2510.07315) — Aligns LLM-as-judge code evaluation with human preference on readability and sty. 🤖

<a id="process-eval"></a>
## Process Evaluation

*Evaluates HOW the agent works (trajectory, reasoning), not just final output. Key for debugging agent behavior.*

### A–F

- [A Benchmark Mutation Approach for Realistic Agent Evaluation](https://arxiv.org/abs/2510.08996) — Benchmark mutation approach generating realistic SE agent evaluation tasks.
- [A Computational Theory for Efficient Mini Agent Evaluation with Causal Guarantees](https://openreview.net/forum?id=dsjxCoa0CO) — Computational theory for efficient mini agent evaluation with causal guarantees.
- [A Framework for Continuous Evaluation of LLM Test Generation in Industry](https://arxiv.org/html/2504.18985v1) — Framework for continuous evaluation of LLM test generation in industry settings.
- [A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems](https://arxiv.org/html/2511.14136v1) — Multi-dimensional framework evaluating enterprise AI agents on cost, reliability.
- [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://arxiv.org/abs/2604.19572) — Self-evolving observation compression framework for long-horizon terminal agents. 📅
- [ACON](https://arxiv.org/abs/2510.00615) — Compresses observations and interaction histories to reduce agent memory usage. 📅
- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error](https://arxiv.org/abs/2604.23581) — DAG-based step-level evaluation tracking error propagation in agentic workflows. 🔍 🤖
- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/abs/2604.23581v1) — DAG-structured step-level evaluation for agentic workflows with error propagatio.
- [Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity](https://arxiv.org/abs/2604.17609v1) — Evaluates whether LLM agents exploit unexpected environmental discoveries in SE .
- [AI agent evaluation: A practical framework for testing multi-step agents](https://www.braintrust.dev/articles/ai-agent-evaluation-framework) — Braintrust practical framework for evaluating multi-step agents across reasoning.
- [AlphaEval: Evaluating Agents in Production](https://arxiv.org/abs/2604.12162) — Framework for evaluating AI agents in production with implicit constraints. 🔍 🌍
- [Automatic Failure Attribution and Critical Step Prediction Method for Multi-Agen](https://arxiv.org/abs/2509.08682) — Attributes failures and predicts critical steps in multi-agent systems. 🤝
- [Beyond Accuracy: Evaluating Source Code Capabilities in Large Language Models fo](https://www.semanticscholar.org/paper/208217bedf590ae49bcc0cb6f779271e644b8a01) — Evaluates LLM source code capabilities beyond accuracy using interpretability me.
- [CodeCircuit: Toward Inferring LLM-Generated Code Correctness via Attribution Gra](https://arxiv.org/abs/2602.07080) — Infers LLM-generated code correctness via attribution graphs without execution. 🔍
- [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/abs/2604.14877) — PASS@(k,T) metric jointly measuring sampling and interaction depth for RL agents. 🔍
- [Don't Let AI Agents YOLO Your Files: Shifting Information and Control to Filesystems for Agent Safety and Autonomy](https://arxiv.org/abs/2604.13536) — Systematic study of AI agent filesystem misuse across 290 reports, 13 frameworks.
- [Effective Strategies for Asynchronous Software Engineering Agents](https://arxiv.org/html/2603.21489v1) — Evaluates coordination strategies for asynchronous multi-agent SE workflows. 🤝
- [Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents](https://arxiv.org/abs/2604.26274) — Behavioral firewall using pDFA to detect anomalous tool-call sequences in AI age.
- [Evaluating Plan Compliance in Autonomous Programming Agents](https://arxiv.org/abs/2604.12147v2) — Evaluates plan compliance in autonomous programming agents using reason-act-obse.
- [Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618) — Evaluates frontier models' propensity to sabotage AI safety research when deploy.
- [Exploration and Exploitation Errors Are Measurable for Language Model Agents](https://arxiv.org/abs/2604.13151) — Quantifies exploration and exploitation errors of LM agents in controlled enviro. 🔍
- [Failure-Centered Runtime Evaluation for Deployed Trilingual Public-Space Agents](https://arxiv.org/abs/2604.23990) — Failure-centered runtime evaluation framework for deployed trilingual SE agents.
- [From Correctness to Collaboration: A Human-Centered Taxonomy of AI Agent Behavio](https://www.semanticscholar.org/paper/85198c5c58ceb3c8681ce3fbd19f52b9533164ec) — Taxonomy of AI agent behaviors from 91 developer rules beyond correctness.
- [From Reproduction to Replication: Evaluating Research Agents with Progressive Co](https://arxiv.org/abs/2506.19724) — Progressive code masking framework to evaluate research agents from reproduction.

### G–L

- [Hodoscope: Unsupervised Monitoring for AI Misbehaviors](https://arxiv.org/abs/2604.11072) — Unsupervised monitoring framework for detecting unknown AI agent misbehaviors. 🔍
- [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/abs/2604.18874) — Formalizes adversarial tool environments as evaluation gap for agentic AI.
- [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750v1) — Analyzes and predicts token consumption patterns in agentic coding tasks.
- [How to Evaluate Coding Agents in Production](https://labs.adaline.ai/p/evaluate-coding-agents-production) — Four metrics for evaluating coding agents in real production engineering environ. 🏭
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787) — Scales inference compute via repeated sampling with coverage as power law.

### M–R

- [Measuring the Unmeasurable: Markov Chain Reliability for LLM Agents](https://arxiv.org/abs/2604.24579) — Models agent traces as Markov chains for pass@k uncertainty quantification. 🔍
- [Plausible but Wrong: A case study on Agentic Failures in Astrophysical Workflows](https://arxiv.org/abs/2604.25345) — Case study on agentic AI failures in scientific workflows across 18 tasks.
- [Playing Psychic: Using Thought Trees to Predict Reasoning Models Accuracy on Cod](https://arxiv.org/abs/2604.16931) — Predicts reasoning model accuracy on coding tasks via thought tree structure. 🔍
- [Process-Level Trajectory Eval](https://arxiv.org/html/2510.25694v1) — Scores each agent step in trajectories rather than just final outcomes. 🔍
- [Process-Oriented Error Analysis](https://arxiv.org/abs/2503.12374) — Classifies and attributes process errors in software engineering agents. 🔍
- [Reasoning Through Execution (ORPS)](https://arxiv.org/abs/2412.15118) — Combines process and outcome supervision via execution for code gen.

### S–Z

- [Self-Abstraction from Grounded Experience for Plan-Guided Policy Refinement](https://arxiv.org/abs/2511.05931) — Self-improving LLM agent via experience abstraction and plan-guided policy refin.
- [Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping](https://openreview.net/forum?id=LZZENDlZt9) — Process evaluation with intrinsic signals and adaptive reward shaping for SE age. 🔍 🤖
- [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Co](https://arxiv.org/abs/2509.09853) — Evaluates AI coding agent effectiveness under resource constraints like cost and. 🔍
- [SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Mode](https://arxiv.org/abs/2604.14820) — Rubric-based process reward model with test-time scaling for long-horizon SWE ag. 📅
- [TDD Governance for Multi-Agent Code Generation via Prompt Engineering](https://arxiv.org/abs/2604.26615v1) — TDD governance framework for multi-agent code generation via prompt engineering. 🤝
- [TDD Governance for Multi-Agent Code Generation via Prompt Engineering](https://arxiv.org/abs/2604.26615) — TDD governance framework enforcing Red-Green-Refactor as prompt-level constraint. 🤝
- [Test Case Generation from Bug Reports via Large Language Models: A Cognitive Lay](https://arxiv.org/abs/2510.05365) — Evaluates LLM test generation from bug reports using Bloom's taxonomy cognitive . 🔍
- [The Complexity Trap](https://arxiv.org/abs/2508.21433) — Observation masking matches LLM summarization performance at half the cost.
- [The Kitchen Loop: User-Spec-Driven Development for a Self-Evolving Codebase](https://arxiv.org/abs/2603.25697) — Kitchen Loop: spec-driven autonomous eval with synthetic users and unbeatable te.
- [Turning the Tide: Repository-based Code Reflection](https://arxiv.org/abs/2507.09866) — Proposes repository-based code reflection to improve SE agent reasoning.

<a id="execution-based"></a>
## Execution-based

- [A Systematic Approach for Assessing LLM Test Case Generation Capability](https://arxiv.org/html/2502.02866v1) — Systematic methodology for evaluating LLM-generated test cases.
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-](https://arxiv.org/abs/2604.25850v1) — Observability-driven automatic evolution of eval harnesses for coding agents.
- [Assessing Effectiveness of Test Suites: What Do We Know and What Should We Do?](https://www.semanticscholar.org/paper/e0fb57dcac9c62f87dec0331e655e2c6f3250b9b) — Survey comparing test suite effectiveness metrics with standardized evaluation f.
- [Can Code Evaluation Metrics Detect Code Plagiarism?](https://arxiv.org/abs/2604.25778v1) — Study on whether code evaluation metrics can reliably detect source code plagiar.
- [Can Code Evaluation Metrics Detect Code Plagiarism?](https://arxiv.org/abs/2604.25778) — Empirical study on whether code evaluation metrics can detect source code plagia.
- [COCO: Testing Code Generation Systems via Concretized Instructions](https://arxiv.org/abs/2308.13319) — Tests code generation via concretizing ambiguous natural-language instructions.
- [CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verifica](https://arxiv.org/abs/2405.00253) — Taxonomy and benchmark for detecting code hallucinations in LLMs via execution v.
- [CodeT: Code Generation with Generated Tests](https://arxiv.org/abs/2207.10397) — Uses generated tests to score and select code solutions via dual execution agree.
- [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](https://openreview.net/forum?id=mrEK16Jy6h) — Intervention-driven auto debugging evaluation framework for LLM multi-agent syst. 🤝
- [Evaluating Large Language Models with Runtime Behavior of Program Execution](https://arxiv.org/abs/2403.16437) — Evaluates LLMs using runtime behavior and program execution traces.
- [Execution-Based Evaluation for Open-Domain Code Generation](https://arxiv.org/abs/2212.10481) — Proposes execution-based evaluation methods for open-domain code generation task.
- [How Many Code and Test Cases Are Enough? Evaluating Test Cases Generation from a](https://arxiv.org/abs/2510.08720) — Binary matrix framework evaluating LLM-generated test case quality and coverage.
- [How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks](https://arxiv.org/abs/2604.10508) — Iterative self-repair evaluation across model scales and benchmarks with executi.
- [InspectCoder: Dynamic Analysis-Driven Self Repair through Interactive LLM-Debugger Collaboration](https://www.semanticscholar.org/paper/5dc2d9d2be600942cb26293230899535ee35d70f) — Agentic self-repair via LLM-debugger dynamic analysis for code error diagnosis.
- [INTERVENOR: Prompt the Coding Ability of Large Language Models with the Interact](https://arxiv.org/abs/2311.09868) — Interactive chain-of-repair methodology to improve LLM code generation via itera.
- [Measuring the performance of our models on real-world tasks (GDPval)](https://openai.com/index/gdpval/) — GDPval: framework evaluating model performance on real-world GDP-sector tasks.
- [Mutation-Guided Unit Test Generation with a Large Language Model](https://arxiv.org/html/2506.02954v6) — Uses mutation score instead of coverage to evaluate LLM-generated unit tests.
- [On the Reliability and Explainability of Language Models for Program Generation](https://arxiv.org/abs/2302.09587) — Studies reliability and explainability of LMs for code generation, repair, trans.
- [Paper - L2MAC: Large Language Model Automatic Computer for Extensive Code Genera](https://arxiv.org/abs/2310.02003) — LLM-based multi-step code generation framework with automatic task decomposition.
- [Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation](https://arxiv.org/abs/2412.14308) — RL from static quality metrics to generate high-quality, smell-free unit tests.
- [SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of In](https://arxiv.org/abs/2604.25737v1) — Multi-agent decomposition framework for reliable instructed code editing on Edit. 🤝
- [StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Fee](https://arxiv.org/abs/2402.01391) — RL from compiler feedback to improve LLM code generation via stepwise optimizati.
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449) — RL-based training for SWE tasks using rule-based similarity rewards on real repo.

<a id="hybrid"></a>
## Hybrid

- [A methodical approach to agent evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation) — Google Cloud blog on systematic agent evaluation covering reasoning, tool use, a.
- [Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consist](https://arxiv.org/abs/2604.15075) — Optimizes cost-benefit trade-off of SE agents via predictive early stopping and .
- [Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and E](https://arxiv.org/abs/2510.24358) — Agent-driven annotation and evaluation framework reducing benchmark labeling cos.
- [Deep Assessment of Code Review Generation Approaches: Beyond Lexical Similarity](https://arxiv.org/abs/2501.05176) — Critiques lexical metrics like BLEU for code review and proposes better methods.
- [Evaluating AI Agents: A Practical Guide with Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-a-practical-guide-with-microsoft-foundry/4500224) — Practical guide to defining quality criteria and continuous evaluation of AI age.
- [Evaluating AI Agents: More than just LLMs](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-more-than-just-llms/4460575) — Microsoft blog on evaluating AI agents beyond single LLM responses covering acti.
- [Evaluation of LLM-Based Software Engineering Tools: Practices, Challenges, and F](https://arxiv.org/abs/2604.24621) — Systematic review of evaluation practices and challenges for LLM-based SE tools. 📋
- [Multi-Agent Code Verification via Information Theory](https://arxiv.org/html/2511.16708) — Multi-agent code verification system using information theory to detect flawed p. 🤝 🔒
- [Scoring Verifiers: Evaluating Synthetic Verification in Code and Reasoning](https://arxiv.org/abs/2502.13820) — Evaluates synthetic verifiers on code and reasoning using scoring benchmarks.
- [Static Code Analysis in the AI Era: An In-depth Exploration of the Concept, Function, and Potential of Intelligent Code Analysis Agents](https://arxiv.org/abs/2310.08837) — ICAA combining AI models with static analysis tools for intelligent code review.

<a id="human-eval"></a>
## Human Evaluation

- [A Study on Developer Behaviors for Validating and Repairing LLM-Generated Code Using Eye Tracking and IDE Actions](https://arxiv.org/abs/2405.16081) — Eye tracking lab study on how developers validate and repair LLM-generated code. 👤
- [Bridging HCI and AI Research for the Evaluation of Conversational SE Assistants](https://arxiv.org/abs/2502.07956) — HCI+AI framework for human-centered evaluation of conversational SE assistants.
- [ChatGPT in Action: Analyzing Its Use in Software Development](https://www.semanticscholar.org/paper/6f8f35aea416b2542d55a638ad20497f38181384) — Quantitative analysis of ChatGPT use in SE tasks using DevGPT dataset.
- [Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?](https://doi.org/10.1109/ICSE55347.2025.00060) — Study on DL-based automated code review quality vs human reviewers. 👤
- [From Feelings to Metrics: Understanding and Formalizing How Users Vibe-Test LLMs](https://arxiv.org/abs/2604.14137) — Formalizes informal user vibe-testing of LLMs into systematic evaluation methodo. 👤
- [How can we assess human-agent interactions? Case studies in software agent desig](https://arxiv.org/abs/2510.09801) — Framework for assessing human-agent interaction quality in software agent design.
- [The RealHumanEval: Evaluating Large Language Models' Abilities to Support Progra](https://arxiv.org/abs/2404.02806) — Web-based framework evaluating LLM coding support via real programmer task compl.
- [vibe_hacking](https://github.com/tldrsec/vibe_hacking) ⭐41 — Secure code review evaluation of LLMs and vibe coding IDEs. 🔒 🤖
- [What makes a code review useful to OpenDev developers? An empirical investigation](https://arxiv.org/abs/2302.11686) — Empirical study of what makes code review comments useful to OSS developers. 👤

---

[← Back to README](../README.md)
