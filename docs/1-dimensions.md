# ① Evaluation Dimensions

Before evaluating an SE Agent, decide what to measure. This page maps the full capability space and shows where benchmarks exist vs. where the gaps are.

→ See [Landscape](landscape.md) for coverage visualization.

## Contents

- [Dimension Framework](#dimension-framework)
- [Dimension Details](#dimension-details)
- [Current Gaps](#current-gaps)

<a id="dimension-framework"></a>
## Dimension Framework

| Dimension | Description | Benchmarks | Coverage |
|---|---|---|---|
| Bug Localization & Fix | From issue to patch | [SWE-bench](2-benchmarks.md#bug-fix), [LiveCodeBench](2-benchmarks.md#bug-fix) | ████ 40 |
| End-to-End Development | Complete feature implementation | [OmniCode](2-benchmarks.md#end-to-end), [SWE-bench Pro](2-benchmarks.md#long-horizon) | █████ 60 |
| Code Review & PR Quality | Review comment quality, mergeability | [CR-Bench](2-benchmarks.md#code-review) | ██ 18 |
| Test Generation & QA | Writing tests, verifying correctness | [SWT-Bench](2-benchmarks.md#testing) | ██ 22 |
| Security & Vulnerability | Secure code, vulnerability detection | [CVE-Bench](2-benchmarks.md#security) | ███ 23 |
| Long-Horizon Evolution | Multi-step, cross-version development | [SWE-EVO](2-benchmarks.md#long-horizon) | █ 13 |
| Codebase Navigation | Understanding project structure | [CodeScaleBench](2-benchmarks.md#large-codebase) | █ 7 |
| Requirements Understanding | From vague requirements to tasks | — | ⚠️ Gap |
| Architecture Decisions | Choosing among design alternatives | — | ⚠️ Gap |
| Multi-Agent Collaboration | Coordinated multi-agent systems | [MARBLE](2-benchmarks.md#end-to-end) | ⚠️ 5 |

<a id="dimension-details"></a>
## Dimension Details

### Bug Localization & Fix
The most established category. SWE-bench family is the de facto standard. Start with **SWE-bench Verified** (500 human-verified issues) for a reliable baseline. For multi-language, use **Multi-SWE-bench**.
→ [All bug-fix benchmarks](2-benchmarks.md#bug-fix)

### End-to-End Development
Goes beyond isolated fixes — tests full feature implementation, project setup, and delivery. Growing rapidly. **OmniCode** covers multiple SE task types; **SWE-bench Pro** tests long-horizon multi-step work.
→ [All end-to-end benchmarks](2-benchmarks.md#end-to-end)

### Code Review & PR Quality
Measures quality of review comments and suggestions. High practical value but fewer benchmarks. **CodeFuse-CR-Bench** covers end-to-end review; **CodeCriticBench** focuses on critique quality.
→ [All code review benchmarks](2-benchmarks.md#code-review)

### Test Generation & QA
Evaluates test writing, bug reproduction, and verification. **SWT-Bench** is the primary benchmark. Closely related to bug-fix (agents that can write reproducing tests fix bugs better).
→ [All testing benchmarks](2-benchmarks.md#testing)

### Security & Vulnerability
Benchmarks for vulnerability detection, secure code generation, and penetration testing. **CVE-Bench** uses real CVEs; **CyberGym** tests at scale.
→ [All security benchmarks](2-benchmarks.md#security)

### Long-Horizon Evolution
Tests multi-step, multi-file changes over extended interactions. Closer to real engineering than single-issue benchmarks. **SWE-EVO** uses real software evolution scenarios.
→ [All long-horizon benchmarks](2-benchmarks.md#long-horizon)

### Engineering Efficiency
Token consumption, time cost, and Pareto optimality. Not a separate benchmark category — measured alongside other benchmarks. Check individual benchmark leaderboards for efficiency metrics.

<a id="current-gaps"></a>
## Current Gaps

These dimensions lack dedicated benchmarks — they represent the frontier of SE agent evaluation:

- **Requirements Understanding** — SWE-bench provides well-defined issues, skipping the hardest part: understanding what to build from vague requirements
- **Architecture Decisions** — No benchmark evaluates an agent's ability to choose among design alternatives, assess trade-offs, or make system-level decisions
- **Multi-Agent Collaboration** — Almost no benchmarks for multi-agent SE systems (MARBLE is the closest, but focuses on general collaboration, not SE-specific workflows)

These gaps are opportunities for new benchmark development.

---

[← Back to README](../README.md)
