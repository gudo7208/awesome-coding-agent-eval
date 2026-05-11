# ④ Evaluation Toolchain

The tool stack you need to run an evaluation end-to-end.

## Contents

- [Evaluation Harness (40)](#harness)
- [Sandbox & Execution (56)](#sandbox)
- [Observability (9)](#observability)
- [LLM Judge Tools (7)](#judge-tool)

<a id="harness"></a>
## Evaluation Harness

*Frameworks that orchestrate benchmark execution. Pick one that supports your target benchmark.*

### A–F

- [agent-bench](https://github.com/spring-ai-community/agent-bench) ⭐26 — Benchmarks Java AI agents in isolated sandboxes with Spring AI integration. ☕
- [agent-quality-inspect](https://github.com/SAP/agent-quality-inspect) ⭐75 — agent-quality-inspect.
- [AgentEval](https://github.com/AgentEvalHQ/AgentEval) ⭐89 — AgentEval.
- [aider-swe-bench](https://github.com/Aider-AI/aider-swe-bench) ⭐81 — Harness for running and evaluating Aider on SWE-Bench benchmark.
- [aira-dojo](https://github.com/facebookresearch/aira-dojo) ⭐144 — AI research agent development and evaluation framework by Facebook Research.
- [any-agent](https://github.com/mozilla-ai/any-agent) ⭐1162 — Unified interface to build agents across frameworks with tracing and scoring.
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071) — Architectural Design Decisions in AI Agent Harnesses.
- [augment-swebench-agent](https://github.com/augmentcode/augment-swebench-agent) ⭐872 — Runs SWE-bench Verified evaluations with full pipeline for agent benchmarking.
- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation) ⭐360 — awslabs/agent-evaluation.
- [bananalyzer](https://github.com/reworkd/bananalyzer) ⭐328 — Evaluates web agents on standardized scraping and navigation test scenarios.
- [bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness) ⭐1042 — Evaluates code generation models on HumanEval, MBPP, and other benchmarks.
- [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) — AWS blog on evaluating AI agents using Amazon Bedrock AgentCore Evaluations.
- [CATArena](https://github.com/AGI-Eval-Official/CATArena) ⭐65 — Tournament platform for code agents via iterative competitive peer learning.
- [claw-eval](https://github.com/claw-eval/claw-eval) ⭐537 — claw-eval.
- [codex-long-running-harness](https://github.com/LongWeihan/codex-long-running-harness) ⭐16 — codex-long-running-harness. 📅
- [collaborative-gym](https://github.com/SALT-NLP/collaborative-gym) ⭐130 — Framework for building and evaluating human-AI collaborative agents. 🤝
- [evalmonkey](https://github.com/Corbell-AI/evalmonkey) ⭐24 — CLI eval harness for AI coding agents with benchmark and chaos fault injection.
- [evals](https://github.com/strands-agents/evals) ⭐121 — Evaluation framework for AI agents and LLM apps with automated agentic testing. 🐍

### G–L

- [harbor](https://github.com/harbor-framework/harbor) ⭐1870 — Runs AI agent evals and RL environments with terminal-based benchmarking.
- [How to Build a Coding Agent Benchmark with Claude's Agent SDK](https://lirantal.com/blog/how-to-build-a-coding-agent-benchmark-with-claudes-agent-sdk) — Tutorial on building a coding agent benchmark harness with Claude Agent SDK.
- [intellagent](https://github.com/plurai-ai/intellagent) ⭐1211 — intellagent.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) ⭐12496 — General-purpose LLM evaluation framework supporting hundreds of benchmarks.

### M–R

- [OD-SWE-bench](https://github.com/OpenDevin/OD-SWE-bench) ⭐30 — Enhanced SWE-bench fork with evaluation harness for OpenDevin agents.
- [OpenAI Evals](https://github.com/openai/evals) ⭐18431 — OpenAI Evals.
- [OpenDevin: An Open Platform for AI Software Developers as Generalist Agents](https://www.semanticscholar.org/paper/be27ef5a9068d9e2be1ab97b7c3de7168c472972) — Open platform for building and evaluating AI software engineering agents.
- [OpenHands Eval Harness](https://github.com/All-Hands-AI/OpenHands) ⭐73111 — Built-in eval framework for OpenHands supporting SWE-bench and more, 30x faster.
- [pr-arena](https://github.com/neulab/pr-arena) ⭐16 — Platform for pairwise PR generation and human comparison to rank coding agents.
- [refact-bench](https://github.com/smallcloudai/refact-bench) ⭐63 — Benchmark harness evaluating AI coding assistants on SWE-Bench tasks via Docker.

### S–Z

- [SanityHarness](https://github.com/lemon07r/SanityHarness) ⭐222 — SanityHarness. 🌐
- [sb-cli](https://github.com/SWE-bench/sb-cli) ⭐66 — Official SWE-bench CLI tool for running remote evaluation tasks.
- [smolagents](https://github.com/huggingface/smolagents) ⭐27212 — Hugging Face lightweight framework for building and running LLM-powered agents. 🤝 🐍
- [squeez](https://github.com/KRLabsOrg/squeez) ⭐17 — Compresses verbose tool outputs for coding agents via LoRA fine-tuning.
- [SWE Agent](https://github.com/princeton-nlp/swe-agent) ⭐19185 — SWE Agent.
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — Agent-computer interface framework for LM agents to resolve GitHub issues.
- [SWE-bench Experiments](https://github.com/SWE-bench/experiments) ⭐263 — SWE-bench Experiments.
- [Test-Agent](https://github.com/codefuse-ai/Test-Agent) ⭐691 — LLM-powered software testing agent for industrial use cases.
- [token-savior](https://github.com/Mibayy/token-savior) ⭐834 — token-savior.
- [ts-bench](https://github.com/laiso/ts-bench) ⭐233 — CLI benchmark tool for evaluating AI coding agents on TypeScript workloads. 🔷
- [upskill](https://github.com/huggingface/upskill) ⭐526 — Generates and evaluates coding skills of agents like Claude Code and Codex.
- [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](https://arxiv.org/abs/2412.10133) — LLM agent that auto-configures and executes test suites for arbitrary projects.

<a id="sandbox"></a>
## Sandbox & Execution

*Isolated execution environments for running agent-generated code safely.*

### A–F

- [agent-safehouse](https://github.com/eugene1g/agent-safehouse) ⭐1740 — Sandbox for local AI agents with scoped read/write filesystem access.
- [agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) ⭐2114 — Kubernetes-based sandbox runtime for isolated stateful AI agent workloads.
- [agentbox](https://github.com/Michaelliv/agentbox) ⭐44 — Sandboxed code execution environment for AI agents.
- [AgentKernelArena](https://github.com/AMD-AGI/AgentKernelArena) ⭐15 — Isolated sandbox for side-by-side benchmarking of SE agents on kernel tasks. 🤝
- [AgentRun](https://github.com/Jonathan-Adly/AgentRun) ⭐372 — Python library for running AI-generated code safely in Docker sandboxes. 🐍
- [AgentSim: A Platform for Verifiable Agent-Trace Simulation](https://arxiv.org/abs/2604.26653v1) — Platform for simulating and verifying agent traces for training/evaluation.
- [ai-code-sandbox](https://github.com/typper-io/ai-code-sandbox) ⭐61 — Docker-based secure Python sandbox for isolated AI/LLM-generated code execution. 🐍
- [arrakis](https://github.com/abshkbh/arrakis) ⭐809 — arrakis.
- [artifact-fs](https://github.com/cloudflare/artifact-fs) ⭐787 — FUSE filesystem driver for lazy-mounting large git repos in agent sandboxes.
- [awesome-agent-sandboxes](https://github.com/arjan/awesome-agent-sandboxes) ⭐23 — Curated list of code execution sandbox solutions for AI/LLM agents.
- [boxed](https://github.com/akshayaggarwal99/boxed) ⭐13 — Sandboxed code execution engine for AI agents via Docker, Firecracker, and Wasm.
- [boxlite](https://github.com/boxlite-ai/boxlite) ⭐2042 — Embeddable sandbox for AI agents with snapshots, state and hardware isolation.
- [Code-Runner-Sandbox](https://github.com/shouldnotappearcalm/Code-Runner-Sandbox) ⭐23 — Multi-language code execution sandbox (Python/Java/C/Go) for model evaluation. 🌐
- [coderunner](https://github.com/instavm/coderunner) ⭐824 — Local isolated sandbox for AI agents to run code safely in containers.
- [cua](https://github.com/trycua/cua) ⭐15885 — Sandbox infra for computer-use agents with macOS/Linux/Windows VMs and SDK.
- [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) ⭐5257 — Sandbox for secure AI agent code execution with instant concurrent containers. 🦀
- [daVinci-Env: Open SWE Environment Synthesis at Scale](https://arxiv.org/abs/2603.13023) — Synthesizes executable SWE environments at scale for agent evaluation.
- [Daytona](https://daytona.io) — Dev environment platform with persistent state and checkpoints for agent tasks. 📅
- [diy-sample-sandbox-cloud-run](https://github.com/GoogleCloudPlatform/diy-sample-sandbox-cloud-run) ⭐23 — Experimental on-demand code execution sandbox built on Google Cloud Run.
- [E2B](https://github.com/e2b-dev/E2B) ⭐12134 — Sandbox for secure AI agent code execution with Firecracker microVMs.
- [exec-sandbox](https://github.com/dualeai/exec-sandbox) ⭐24 — exec-sandbox.

### G–L

- [godbox](https://github.com/quantumsheep/godbox) ⭐28 — Secure sandboxing system for executing untrusted code in evaluation pipelines. 🔒
- [gondolin](https://github.com/earendil-works/gondolin) ⭐1149 — Experimental agent sandbox using Linux microVMs with TypeScript control plane. 🔷
- [judge0](https://github.com/judge0/judge0) ⭐4159 — Open-source sandboxed code execution system supporting 60+ languages. 🌐

### M–R

- [MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering](https://arxiv.org/abs/2601.22859) — MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering. 🤝
- [microsandbox](https://github.com/superradcompany/microsandbox) ⭐6019 — microsandbox. 🔒
- [mithril](https://github.com/radimsem/mithril) ⭐13 — Trustless MCP server with sandboxed execution tools for AI coding agents.
- [moatless-testbeds](https://github.com/aorwall/moatless-testbeds) ⭐14 — moatless-testbeds.
- [Modal](https://modal.com) — Modal.
- [MultiModal-Jupyter-Sandbox](https://github.com/ChenShawn/MultiModal-Jupyter-Sandbox) ⭐24 — MultiModal-Jupyter-Sandbox.
- [nix-sandbox-mcp](https://github.com/secbear/nix-sandbox-mcp) ⭐16 — Nix and bubblewrap sandboxed code execution via MCP for LLM agents.
- [nono](https://github.com/always-further/nono) ⭐2342 — Zero-config AI agent sandbox with capability-model-based multiplexed isolation.
- [openhands-aci](https://github.com/All-Hands-AI/openhands-aci) ⭐127 — Defines standard interface layer for agent-computer interaction in OpenHands.
- [OpenSandbox](https://github.com/alibaba/OpenSandbox) ⭐10544 — OpenSandbox.
- [pctx](https://github.com/portofcontext/pctx) ⭐251 — Execution layer running agentic tool calls in secure sandboxes for AI workflows.
- [PIPer: On-Device Environment Setup via Online Reinforcement Learning](https://arxiv.org/abs/2509.25455) — Online RL agent for automated on-device software project environment setup.
- [python-sandbox](https://github.com/onyx-dot-app/python-sandbox) ⭐23 — Secure lightweight Python code execution sandbox for LLM/AI agents. 🐍
- [RAT: RunAnyThing via Fully Automated Environment Configuration](https://arxiv.org/abs/2604.23190) — RAT: RunAnyThing via Fully Automated Environment Configuration. 🌐

### S–Z

- [sandbox](https://github.com/agent-infra/sandbox) ⭐4613 — sandbox.
- [sandbox-agent](https://github.com/rivet-dev/sandbox-agent) ⭐1361 — Run coding agents in sandboxed environments with HTTP control for evaluation.
- [sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) ⭐1017 — SDK for running sandboxed code environments on Cloudflare's edge network.
- [sandboxed-jupyter-code-exec](https://github.com/anukriti-ranjan/sandboxed-jupyter-code-exec) ⭐22 — FastAPI sandboxed Python code execution environment using Jupyter kernels.
- [sandboxer](https://github.com/ammmir/sandboxer) ⭐15 — Forkable code execution sandbox server for LLMs and agents.
- [ScaleBox](https://arxiv.org/abs/2604.29700) — High-fidelity and scalable code verification sandbox for LLMs.
- [secure-exec](https://github.com/rivet-dev/secure-exec) ⭐863 — secure-exec.
- [skypilot-code-sandbox](https://github.com/alex000kim/skypilot-code-sandbox) ⭐17 — skypilot-code-sandbox.
- [SmolVM](https://github.com/CelestoAI/SmolVM) ⭐534 — Lightweight open-source VM sandbox for AI agent code execution and browser use.
- [SWE-bench Harness](https://github.com/epoch-research/SWE-bench) ⭐16 — Containerized runtime environments for SWE-bench task evaluation via Docker.
- [SWE-bench-docker](https://github.com/aorwall/SWE-bench-docker) ⭐105 — Dockerized sandbox for running SWE-bench evaluations in isolated containers.
- [SWE-ReX](https://github.com/SWE-agent/SWE-ReX) ⭐497 — SWE-ReX.
- [SWE-World: Building Software Engineering Agents in Docker-Free Environments](https://arxiv.org/abs/2602.03419) — SWE-World: Building Software Engineering Agents in Docker-Free Environments.
- [the-agent-sandbox-taxonomy](https://github.com/kajogo777/the-agent-sandbox-taxonomy) ⭐66 — Taxonomy and scoring framework for AI agent sandboxes with 7 defense layers.
- [vibe](https://github.com/lynaghk/vibe) ⭐898 — vibe. 🦀
- [vibekit](https://github.com/superagent-ai/vibekit) ⭐1784 — vibekit. 🤝
- [wuying-agentbay-sdk](https://github.com/agentbay-ai/wuying-agentbay-sdk) ⭐1117 — Cloud sandbox environment SDK built for AI agents.
- [zeroboot](https://github.com/zerobootdev/zeroboot) ⭐2312 — zeroboot.

<a id="observability"></a>
## Observability

- [agentevals](https://github.com/agentevals-dev/agentevals) ⭐125 — Evaluates AI agents via OpenTelemetry traces in a framework-agnostic way.
- [Braintrust](https://braintrust.dev) — Braintrust.
- [CodeTracer: Towards Traceable Agent States](https://arxiv.org/abs/2604.11641) — CodeTracer: Towards Traceable Agent States.
- [Langfuse](https://github.com/langfuse/langfuse) ⭐26948 — Open-source LLM observability platform with tracing, spans, and scoring.
- [Observal](https://github.com/BlazeUp-AI/Observal) ⭐1048 — Observal.
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16154 — Python SDK for AI agent observability, tracing, monitoring and evaluation. 🤝
- [RepoAgent](https://github.com/OpenBMB/RepoAgent) ⭐960 — LLM-powered framework for automated repository documentation generation.
- [swe_bench_traces](https://github.com/codestoryai/swe_bench_traces) ⭐10 — Archives AI patch generation and evaluation traces on SWE-bench Lite.
- [Systematic debugging for AI agents: Introducing the AgentRx framework](https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/) — AgentRx framework for systematic debugging of AI agent failure trajectories.

<a id="judge-tool"></a>
## LLM Judge Tools

- [aiXamine: Simplified LLM Safety and Security](https://arxiv.org/abs/2504.14985) — Black-box LLM safety/security eval platform with 40+ tests across 8 dimensions. 🔒
- [augre](https://github.com/twitchax/augre) ⭐41 — LLM-powered local diff code review tool using CodeLlama or OpenAI. 🤖
- [CodeFox-CLI](https://github.com/codefox-lab/CodeFox-CLI) ⭐40 — CLI tool for AI-powered code review of git diffs using local or cloud LLMs. 🤖
- [diffdeck](https://github.com/KnockOutEZ/diffdeck) ⭐47 — diffdeck.
- [Evaluate your AI agents with Vertex Gen AI evaluation service](https://cloud.google.com/blog/products/ai-machine-learning/introducing-agent-evaluation-in-vertex-ai-gen-ai-evaluation-service) — Google Vertex AI agent evaluation service with trajectory analysis. 🤖
- [Promptfoo](https://github.com/promptfoo/promptfoo) ⭐21115 — Tests and evaluates LLM outputs with prompt comparison and auto-scoring.
- [sage](https://github.com/usetig/sage) ⭐93 — LLM council that reviews and evaluates coding agent actions in real-time. 🤖

---

[← Back to README](../README.md)
