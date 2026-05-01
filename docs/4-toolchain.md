# ④ Evaluation Toolchain

The tool stack you need to run an evaluation end-to-end.

## Contents

- [Evaluation Harness (40)](#harness)
- [Sandbox & Execution (55)](#sandbox)
- [Observability (9)](#observability)
- [LLM Judge Tools (7)](#judge-tool)

<a id="harness"></a>
## Evaluation Harness

*Frameworks that orchestrate benchmark execution. Pick one that supports your target benchmark.*

### A–F

- [agent-bench](https://github.com/spring-ai-community/agent-bench) ⭐26 — Benchmarks Java AI agents in isolated sandboxes with Spring AI integration. ☕
- [agent-quality-inspect](https://github.com/SAP/agent-quality-inspect) ⭐75 — SAP agentic AI evaluation toolkit with multi-framework benchmarking and LLM-as-j.
- [AgentEval](https://github.com/AgentEvalHQ/AgentEval) ⭐86 — Evaluates .NET AI agents with tool-call validation, RAG metrics, and model compa.
- [aider-swe-bench](https://github.com/Aider-AI/aider-swe-bench) ⭐81 — Harness for running and evaluating Aider on SWE-Bench benchmark.
- [aira-dojo](https://github.com/facebookresearch/aira-dojo) ⭐143 — AI research agent development and evaluation framework by Facebook Research.
- [any-agent](https://github.com/mozilla-ai/any-agent) ⭐1156 — Unified interface to build agents across frameworks with tracing and scoring.
- [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071) — Empirical study of architectural design decisions across 70 AI agent harness pro.
- [augment-swebench-agent](https://github.com/augmentcode/augment-swebench-agent) ⭐870 — Runs SWE-bench Verified evaluations with full pipeline for agent benchmarking.
- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation) ⭐359 — Tests generative AI agents with auto test generation and execution validation on.
- [bananalyzer](https://github.com/reworkd/bananalyzer) ⭐327 — Evaluates web agents on standardized scraping and navigation test scenarios.
- [bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness) ⭐1040 — Evaluates code generation models on HumanEval, MBPP, and other benchmarks.
- [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) — AWS blog on evaluating AI agents using Amazon Bedrock AgentCore Evaluations.
- [CATArena](https://github.com/AGI-Eval-Official/CATArena) ⭐64 — Tournament platform for code agents via iterative competitive peer learning.
- [claw-eval](https://github.com/claw-eval/claw-eval) ⭐508 — Agent evaluation harness with human-verified tasks for real-world behavior asses.
- [codex-long-running-harness](https://github.com/LongWeihan/codex-long-running-harness) ⭐15 — Long-running application harness for Codex using planner-generator-evaluator pat. 📅
- [collaborative-gym](https://github.com/SALT-NLP/collaborative-gym) ⭐128 — Framework for building and evaluating human-AI collaborative agents. 🤝
- [evalmonkey](https://github.com/Corbell-AI/evalmonkey) ⭐21 — CLI eval harness for AI coding agents with benchmark and chaos fault injection.
- [evals](https://github.com/strands-agents/evals) ⭐115 — Evaluation framework for AI agents and LLM apps with automated agentic testing. 🐍

### G–L

- [harbor](https://github.com/harbor-framework/harbor) ⭐1699 — Runs AI agent evals and RL environments with terminal-based benchmarking.
- [How to Build a Coding Agent Benchmark with Claude's Agent SDK](https://lirantal.com/blog/how-to-build-a-coding-agent-benchmark-with-claudes-agent-sdk) — Tutorial on building a coding agent benchmark harness with Claude Agent SDK.
- [intellagent](https://github.com/plurai-ai/intellagent) ⭐1182 — Diagnostic framework using synthetic interactions to test, score, and optimize a.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) ⭐12369 — General-purpose LLM evaluation framework supporting hundreds of benchmarks.

### M–R

- [OD-SWE-bench](https://github.com/OpenDevin/OD-SWE-bench) ⭐30 — Enhanced SWE-bench fork with evaluation harness for OpenDevin agents.
- [OpenAI Evals](https://github.com/openai/evals) ⭐18318 — Open-source framework for evaluating LLMs with benchmark registry and custom tas.
- [OpenDevin: An Open Platform for AI Software Developers as Generalist Agents](https://www.semanticscholar.org/paper/be27ef5a9068d9e2be1ab97b7c3de7168c472972) — Open platform for building and evaluating AI software engineering agents.
- [OpenHands Eval Harness](https://github.com/All-Hands-AI/OpenHands) ⭐72349 — Built-in eval framework for OpenHands supporting SWE-bench and more, 30x faster.
- [pr-arena](https://github.com/neulab/pr-arena) ⭐16 — Platform for pairwise PR generation and human comparison to rank coding agents.
- [refact-bench](https://github.com/smallcloudai/refact-bench) ⭐62 — Benchmark harness evaluating AI coding assistants on SWE-Bench tasks via Docker.

### S–Z

- [SanityHarness](https://github.com/lemon07r/SanityHarness) ⭐220 — Lightweight universal eval harness for coding agents with multi-language support. 🌐
- [sb-cli](https://github.com/SWE-bench/sb-cli) ⭐63 — Official SWE-bench CLI tool for running remote evaluation tasks.
- [smolagents](https://github.com/huggingface/smolagents) — Hugging Face lightweight framework for building and running LLM-powered agents. 🤝 🐍
- [squeez](https://github.com/KRLabsOrg/squeez) ⭐11 — Compresses verbose tool outputs for coding agents via LoRA fine-tuning.
- [SWE Agent](https://github.com/princeton-nlp/swe-agent) — Agent framework that turns LLMs into software engineering agents for fixing GitH.
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — Agent-computer interface framework for LM agents to resolve GitHub issues.
- [SWE-bench Experiments](https://github.com/SWE-bench/experiments) ⭐262 — Provides open-source predictions, logs, and trajectories for SWE-bench evaluatio.
- [Test-Agent](https://github.com/codefuse-ai/Test-Agent) ⭐688 — LLM-powered software testing agent for industrial use cases.
- [token-savior](https://github.com/Mibayy/token-savior) ⭐713 — MCP server enabling Claude to hit 100% on coding benchmark with token/time effic.
- [ts-bench](https://github.com/laiso/ts-bench) ⭐230 — CLI benchmark tool for evaluating AI coding agents on TypeScript workloads. 🔷
- [upskill](https://github.com/huggingface/upskill) ⭐503 — Generates and evaluates coding skills of agents like Claude Code and Codex.
- [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](https://arxiv.org/abs/2412.10133) — LLM agent that auto-configures and executes test suites for arbitrary projects.

<a id="sandbox"></a>
## Sandbox & Execution

*Isolated execution environments for running agent-generated code safely.*

### A–F

- [agent-safehouse](https://github.com/eugene1g/agent-safehouse) ⭐1662 — Sandbox for local AI agents with scoped read/write filesystem access.
- [agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) ⭐1973 — Kubernetes-based sandbox runtime for isolated stateful AI agent workloads.
- [agentbox](https://github.com/Michaelliv/agentbox) ⭐43 — Sandboxed code execution environment for AI agents.
- [AgentKernelArena](https://github.com/AMD-AGI/AgentKernelArena) ⭐13 — Isolated sandbox for side-by-side benchmarking of SE agents on kernel tasks. 🤝
- [AgentRun](https://github.com/Jonathan-Adly/AgentRun) — Python library for running AI-generated code safely in Docker sandboxes. 🐍
- [AgentSim: A Platform for Verifiable Agent-Trace Simulation](https://arxiv.org/abs/2604.26653v1) — Platform for simulating and verifying agent traces for training/evaluation.
- [ai-code-sandbox](https://github.com/typper-io/ai-code-sandbox) ⭐61 — Docker-based secure Python sandbox for isolated AI/LLM-generated code execution. 🐍
- [arrakis](https://github.com/abshkbh/arrakis) ⭐804 — Customizable self-hosted sandbox for AI agent code execution with backtracking a.
- [artifact-fs](https://github.com/cloudflare/artifact-fs) ⭐744 — FUSE filesystem driver for lazy-mounting large git repos in agent sandboxes.
- [awesome-agent-sandboxes](https://github.com/arjan/awesome-agent-sandboxes) ⭐23 — Curated list of code execution sandbox solutions for AI/LLM agents.
- [boxed](https://github.com/akshayaggarwal99/boxed) ⭐13 — Sandboxed code execution engine for AI agents via Docker, Firecracker, and Wasm.
- [boxlite](https://github.com/boxlite-ai/boxlite) ⭐1868 — Embeddable sandbox for AI agents with snapshots, state and hardware isolation.
- [Code-Runner-Sandbox](https://github.com/shouldnotappearcalm/Code-Runner-Sandbox) ⭐23 — Multi-language code execution sandbox (Python/Java/C/Go) for model evaluation. 🌐
- [coderunner](https://github.com/instavm/coderunner) ⭐820 — Local isolated sandbox for AI agents to run code safely in containers.
- [cua](https://github.com/trycua/cua) ⭐15010 — Sandbox infra for computer-use agents with macOS/Linux/Windows VMs and SDK.
- [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) ⭐4653 — Sandbox for secure AI agent code execution with instant concurrent containers. 🦀
- [daVinci-Env: Open SWE Environment Synthesis at Scale](https://arxiv.org/abs/2603.13023) — Synthesizes executable SWE environments at scale for agent evaluation.
- [Daytona](https://daytona.io) — Dev environment platform with persistent state and checkpoints for agent tasks. 📅
- [diy-sample-sandbox-cloud-run](https://github.com/GoogleCloudPlatform/diy-sample-sandbox-cloud-run) ⭐22 — Experimental on-demand code execution sandbox built on Google Cloud Run.
- [E2B](https://github.com/e2b-dev/E2B) ⭐11983 — Sandbox for secure AI agent code execution with Firecracker microVMs.
- [exec-sandbox](https://github.com/dualeai/exec-sandbox) ⭐21 — Lightweight secure code execution sandbox on QEMU microVM with 9-layer isolation.

### G–L

- [godbox](https://github.com/quantumsheep/godbox) ⭐28 — Secure sandboxing system for executing untrusted code in evaluation pipelines. 🔒
- [gondolin](https://github.com/earendil-works/gondolin) ⭐1025 — Experimental agent sandbox using Linux microVMs with TypeScript control plane. 🔷
- [judge0](https://github.com/judge0/judge0) ⭐4139 — Open-source sandboxed code execution system supporting 60+ languages. 🌐

### M–R

- [MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software En](https://arxiv.org/abs/2601.22859) — Constructs polyglot dev environments via multi-agent plan-execute-verify pipelin. 🤝
- [microsandbox](https://github.com/superradcompany/microsandbox) ⭐5877 — Secure lightweight sandbox for AI agent code execution with multi-language isola. 🔒
- [mithril](https://github.com/radimsem/mithril) ⭐11 — Trustless MCP server with sandboxed execution tools for AI coding agents.
- [moatless-testbeds](https://github.com/aorwall/moatless-testbeds) ⭐14 — Kubernetes-based isolated testbeds for applying patches and running SWE-Bench ev.
- [Modal](https://modal.com) — Serverless cloud platform for running AI agent workloads with GPU and container .
- [MultiModal-Jupyter-Sandbox](https://github.com/ChenShawn/MultiModal-Jupyter-Sandbox) ⭐24 — Jupyter-notebook-style sandbox for isolated code execution in AI agent workflows.
- [nix-sandbox-mcp](https://github.com/secbear/nix-sandbox-mcp) ⭐16 — Nix and bubblewrap sandboxed code execution via MCP for LLM agents.
- [nono](https://github.com/always-further/nono) ⭐2158 — Zero-config AI agent sandbox with capability-model-based multiplexed isolation.
- [openhands-aci](https://github.com/All-Hands-AI/openhands-aci) ⭐127 — Defines standard interface layer for agent-computer interaction in OpenHands.
- [OpenSandbox](https://github.com/alibaba/OpenSandbox) ⭐10354 — Alibaba open-source secure sandbox runtime for AI agents with Kubernetes support.
- [pctx](https://github.com/portofcontext/pctx) ⭐248 — Execution layer running agentic tool calls in secure sandboxes for AI workflows.
- [PIPer: On-Device Environment Setup via Online Reinforcement Learning](https://arxiv.org/abs/2509.25455) — Online RL agent for automated on-device software project environment setup.
- [python-sandbox](https://github.com/onyx-dot-app/python-sandbox) ⭐18 — Secure lightweight Python code execution sandbox for LLM/AI agents. 🐍
- [RAT: RunAnyThing via Fully Automated Environment Configuration](https://arxiv.org/abs/2604.23190) — Automates executable environment setup for any repo without manual configuration. 🌐

### S–Z

- [sandbox](https://github.com/agent-infra/sandbox) ⭐4474 — All-in-one Docker sandbox combining browser, shell, file, MCP and VSCode for AI .
- [sandbox-agent](https://github.com/rivet-dev/sandbox-agent) ⭐1336 — Run coding agents in sandboxed environments with HTTP control for evaluation.
- [sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) ⭐1000 — SDK for running sandboxed code environments on Cloudflare's edge network.
- [sandboxed-jupyter-code-exec](https://github.com/anukriti-ranjan/sandboxed-jupyter-code-exec) ⭐22 — FastAPI sandboxed Python code execution environment using Jupyter kernels.
- [sandboxer](https://github.com/ammmir/sandboxer) ⭐15 — Forkable code execution sandbox server for LLMs and agents.
- [secure-exec](https://github.com/rivet-dev/secure-exec) ⭐851 — Lightweight Node.js secure execution library using V8/WASM containerless sandbox.
- [skypilot-code-sandbox](https://github.com/alex000kim/skypilot-code-sandbox) ⭐17 — Self-hosted secure code execution sandbox for LLM agents via SkyPilot on cloud i.
- [SmolVM](https://github.com/CelestoAI/SmolVM) ⭐468 — Lightweight open-source VM sandbox for AI agent code execution and browser use.
- [SWE-bench Harness](https://github.com/epoch-research/SWE-bench) ⭐16 — Containerized runtime environments for SWE-bench task evaluation via Docker.
- [SWE-bench-docker](https://github.com/aorwall/SWE-bench-docker) ⭐105 — Dockerized sandbox for running SWE-bench evaluations in isolated containers.
- [SWE-ReX](https://github.com/SWE-agent/SWE-ReX) ⭐485 — Runtime environment for AI coding agents with local, Docker, and cloud execution.
- [SWE-World: Building Software Engineering Agents in Docker-Free Environments](https://arxiv.org/abs/2602.03419) — Docker-free sandbox for SWE agents using simulated OS environments at lower cost.
- [the-agent-sandbox-taxonomy](https://github.com/kajogo777/the-agent-sandbox-taxonomy) ⭐62 — Taxonomy and scoring framework for AI agent sandboxes with 7 defense layers.
- [vibe](https://github.com/lynaghk/vibe) ⭐883 — Lightweight Linux VM launcher on macOS providing isolated sandbox for LLM agents. 🦀
- [vibekit](https://github.com/superagent-ai/vibekit) ⭐1774 — Isolated sandbox execution for coding agents with data redaction and observabili. 🤝
- [wuying-agentbay-sdk](https://github.com/agentbay-ai/wuying-agentbay-sdk) ⭐1116 — Cloud sandbox environment SDK built for AI agents.
- [zeroboot](https://github.com/zerobootdev/zeroboot) ⭐2253 — Sub-millisecond VM sandbox via Firecracker/KVM copy-on-write fork for agent code.

<a id="observability"></a>
## Observability

- [agentevals](https://github.com/agentevals-dev/agentevals) ⭐118 — Evaluates AI agents via OpenTelemetry traces in a framework-agnostic way.
- [Braintrust](https://braintrust.dev) — Evaluates and monitors AI agents with experiment tracking and LLM-as-judge scori.
- [CodeTracer: Towards Traceable Agent States](https://arxiv.org/abs/2604.11641) — Traces agent state transitions and hidden error chains in multi-stage code workf.
- [Langfuse](https://github.com/langfuse/langfuse) ⭐26319 — Open-source LLM observability platform with tracing, spans, and scoring.
- [Observal](https://github.com/BlazeUp-AI/Observal) ⭐797 — Observability and eval framework for AI coding agents like Claude Code and Curso.
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16146 — Python SDK for AI agent observability, tracing, monitoring and evaluation. 🤝
- [RepoAgent](https://github.com/OpenBMB/RepoAgent) — LLM-powered framework for automated repository documentation generation.
- [swe_bench_traces](https://github.com/codestoryai/swe_bench_traces) ⭐10 — Archives AI patch generation and evaluation traces on SWE-bench Lite.
- [Systematic debugging for AI agents: Introducing the AgentRx framework](https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/) — AgentRx framework for systematic debugging of AI agent failure trajectories.

<a id="judge-tool"></a>
## LLM Judge Tools

- [aiXamine: Simplified LLM Safety and Security](https://arxiv.org/abs/2504.14985) — Black-box LLM safety/security eval platform with 40+ tests across 8 dimensions. 🔒
- [augre](https://github.com/twitchax/augre) ⭐41 — LLM-powered local diff code review tool using CodeLlama or OpenAI. 🤖
- [CodeFox-CLI](https://github.com/codefox-lab/CodeFox-CLI) ⭐39 — CLI tool for AI-powered code review of git diffs using local or cloud LLMs. 🤖
- [diffdeck](https://github.com/KnockOutEZ/diffdeck) ⭐47 — CLI tool generating smart diffs with security scans and AI-ready outputs for cod.
- [Evaluate your AI agents with Vertex Gen AI evaluation service](https://cloud.google.com/blog/products/ai-machine-learning/introducing-agent-evaluation-in-vertex-ai-gen-ai-evaluation-service) — Google Vertex AI agent evaluation service with trajectory analysis. 🤖
- [Promptfoo](https://github.com/promptfoo/promptfoo) ⭐20696 — Tests and evaluates LLM outputs with prompt comparison and auto-scoring.
- [sage](https://github.com/usetig/sage) ⭐93 — LLM council that reviews and evaluates coding agent actions in real-time. 🤖

---

[← Back to README](../README.md)
