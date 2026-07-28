# ⑦ Rubrics for Agent Evaluation

Rubrics are measurement specifications: they define criteria, admissible evidence, decision rules, and aggregation. They are independent of the grader that executes them, so a rubric may be applied by code, a model, a human, or a hybrid pipeline.

> For research findings and design guidance, see [the Rubrics research report](../research/rubrics-agent-evaluation-2026-07-20.md).

## Classification

| Field | Question | Values |
|---|---|---|
| Role | How does the resource use rubrics? | benchmark application, construction method, grading method, meta-evaluation, practice guide |
| Scope | How reusable is the rubric? | general, domain-specific, task-specific |
| Target | What evidence is graded? | artifact, trajectory, both |
| Construction | Who creates the criteria? | expert-authored, model-generated, hybrid |
| Grading | Who applies the criteria? | deterministic, model-based, human, hybrid |
| Form | How are criteria structured? | analytic, checklist, hierarchical, holistic |
| Calibration | What reference validates grading? | human agreement, judge benchmark, execution agreement, not reported |

## Curated Resources

| Resource | Stage | Role | Scope | Target | Construction | Grading | Form | Calibration |
|---|---|---|---|---|---|---|---|---|
| [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://openai.com/index/paperbench/) | benchmark | benchmark-application | task-specific | artifact | expert-authored | hybrid | hierarchical | judge-benchmark |
| [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](https://github.com/alphadl/AdaRubrics) | methodology | construction-method | task-specific | trajectory | model-generated | model-based | analytic | human-agreement |
| [Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171) | methodology | construction-method | task-specific | artifact | model-generated | model-based | checklist | execution-agreement |
| [Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934) | methodology | grading-method | task-specific | both | expert-authored | model-based | hierarchical | human-agreement |
| [SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling](https://arxiv.org/abs/2604.14820) | methodology | grading-method | task-specific | trajectory | model-generated | model-based | analytic | not-reported |
| [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://github.com/THU-KEG/RuVerBench) | meta-analysis | meta-evaluation | task-specific | artifact | hybrid | model-based | checklist | human-agreement |
| [Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](https://arxiv.org/abs/2607.12835) | meta-analysis | meta-evaluation | task-specific | artifact | model-generated | model-based | checklist | judge-benchmark |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | meta-analysis | practice-guide | domain-specific | both | expert-authored | hybrid | analytic | human-agreement |

## Query the Data

```bash
jq '.[] | select(.rubric)' data/*.json
```

---

[← Back to README](../README.md)
