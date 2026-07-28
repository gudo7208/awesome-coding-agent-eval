---
title: Agent 评测中的 Rubrics：方法、工程实践与可靠性调研
date: 2026-07-20
scope: AI software engineering agents
status: completed
---

# Agent 评测中的 Rubrics：方法、工程实践与可靠性调研

## 执行摘要

Rubric 不是“让 LLM 打个分”的提示词，而是一份测量规格：它把成功标准拆成可判定 criteria，说明允许使用的证据、满足条件、权重或门禁，以及如何聚合。Rubric 与 grader 正交；同一份 rubric 可以由程序、模型、人类或混合流程执行。

对 coding agent，推荐的默认架构是：

1. 用执行测试、状态检查和安全检查作为 correctness hard gates；
2. 用原子化 rubric 补足需求完整性、设计质量、合理替代实现、过程约束和可解释 partial credit；
3. 每个 criterion 独立判断并要求证据，允许 `Unknown`；
4. 用专家标注集校准 judge，并在 criterion 层报告可靠性；
5. 将 rubric、judge prompt、模型、聚合规则和版本一起冻结，持续抽检漂移。

当前证据不支持“自动生成 rubric 可以直接替代专家标准”或“高总分相关性足以证明 judge 可靠”。自动生成 rubric 会出现覆盖不足、过度细分、高分偏置和领域适配弱；长输出的 rubric verification 即使由前沿模型完成仍存在显著噪声。

## 1. 范围与研究问题

本报告聚焦能直接服务于 AI 软件工程 agent 评测的 Rubrics，包括 coding agent、研究复现 agent 以及可迁移到 SE agent 的通用 agent-eval 方法。教育评分、泛文本质量评价和纯产品营销材料仅作为方法背景，不作为仓库主收录对象。

研究问题：

- Rubric 与 grader、metric、test oracle 的边界是什么？
- Agent 场景中的 rubric 应如何分类？
- 静态、任务自适应和 repository-grounded rubric 各自解决什么问题？
- 自动构建和 LLM judge 的可靠性如何验证？
- Coding agent 应怎样把 rubric 与执行门禁组合？

## 2. 操作性定义

一份可执行 rubric 至少包含四部分：

| 组成 | 回答的问题 | 反例 |
|---|---|---|
| Criterion | 评什么单一事实或质量维度？ | “正确、完整、风格好”混在一项 |
| Evidence scope | 可以看哪些文件、日志、测试或轨迹？ | judge 自行猜测隐藏要求 |
| Decision rule / anchor | 怎样算满足、部分满足或失败？ | 只有“优秀/一般/较差”无锚点 |
| Aggregation | 权重、层级、hard gate 如何形成结论？ | 严重安全失败被平均分冲淡 |

相关概念边界：

- Rubric：规定测量对象与判定规则。
- Grader / judge：执行规则的人、模型或程序。
- Metric：输出的统计量，如 pass rate、加权分、F1、kappa。
- Oracle：可作为正确性依据的权威证据，如隐藏测试、数据库终态或专家 gold label。
- Pairwise / pointwise：judge protocol，不是 rubric 本身的类型。

## 3. 分类框架

### 3.1 结构与尺度

- Holistic：一次给整体分，成本低但诊断性差。
- Analytic：按多个维度分别评分，适合质量诊断。
- Checklist：原子二元 criteria，通常更易校准和审计。
- Hierarchical：criteria 形成树并逐层聚合，适合长任务 partial credit。
- Binary：满足/不满足，默认优先。
- Anchored ordinal：只有确需表达程度差异时使用，并为每档提供行为锚点。
- Nominal：输出错误类型或类别，适合 failure taxonomy。

### 3.2 作用域与构建方式

- General：跨任务复用，如通用沟通质量。
- Domain-specific：面向 coding、research 或 support 等领域。
- Task-specific：由具体 issue、PRD、论文或环境实例生成。
- Expert-authored：领域专家直接定义。
- Model-generated：模型从任务、参考答案或环境上下文生成。
- Hybrid：模型生成后由专家审核，或专家 rubric 经模型扩展。

### 3.3 评测目标与证据

- Artifact / outcome：最终 patch、代码库、报告、数据库终态。
- Trajectory / process：工具调用、步骤、成本、安全行为和中间决策。
- Both：结果和过程共同受约束。
- Evidence basis：可进一步区分 reference-free、reference-grounded、source-grounded、repository-grounded 和 execution-grounded。

### 3.4 聚合与用途

- 等权或风险加权；
- 层级加权传播；
- hard gate 后再计算 partial-credit；
- rubric 作为评测标准、process reward、test-time verifier 或训练 preference signal。

## 4. 关键研究脉络

### 4.1 从整体 judge 到原子 criteria

[G-Eval（EMNLP 2023）](https://aclanthology.org/2023.emnlp-main.153/)用 criteria、推理步骤和结构化表单提高与人类判断的一致性，但也暴露模型对 LLM 生成文本的偏好。后续 [LLM-Rubric（ACL 2024）](https://aclanthology.org/2024.acl-long.745/)不直接相信 judge 原始分，而是汇总多个 rubric 问题的分布，再学习到人类评分的校准映射。

[LMUnit](https://arxiv.org/abs/2412.13091)把评测要求表达为自然语言 unit tests；[CheckEval（EMNLP 2025）](https://aclanthology.org/2025.emnlp-main.796/)进一步用二元 checklist 替代宽泛 Likert 判断。共同趋势是从“整体感觉分”走向可独立核验的自然语言断言。

这些工作主要是通用 LLM evaluation，因此不全部进入 SE-only 数据集，但构成 rubric 设计的直接方法基础。

### 4.2 Agent 评测中的任务级 Rubrics

[PaperBench](https://arxiv.org/abs/2504.01848)把 20 个研究复现任务拆成 8,316 个可评分 leaf requirements。Rubric 由论文作者共同审核，提交在独立环境中重跑，leaf 判定后按层级权重向上聚合；同时单独建立 JudgeEval，而不是假定自动 judge 天然可信。

[Agent-as-a-Judge（ICML 2025）](https://proceedings.mlr.press/v267/zhuge25a.html)在 55 个真实代码生成任务上使用 365 条人工层级要求，让 agent judge 检查结果与过程，并与人类基线比较。这说明 agentic judge 的价值来自更完整的证据获取能力，而不只是换一个更大的模型。

[Anthropic 的 agent eval 实践指南](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)将 grader 分成 code-based、model-based 和 human 三类。对 coding agent，它建议以单测和状态验证为主，再用清晰 rubric 补充代码质量或交互行为；模型 grader 必须与专家校准，并通过阅读轨迹判断失败是否公平。

### 4.3 静态、任务自适应与上下文 Grounding

固定通用 rubric 成本低，但会遗漏当前任务真正重要的维度。[AdaRubric](https://arxiv.org/abs/2603.21362)从任务描述动态生成维度，逐步评估 trajectory，并报告了与人类评分的相关性和一致性；其 SWE-bench 结果属于从主实验域向 coding 的 zero-shot transfer，应避免过度外推。

[Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171)更进一步：rubric agent 先探索 repository，再生成 File Change、Spec Alignment、Integrity、Runtime 等 codebase-specific checklist，之后用另一个模型对 patch 进行 execution-free 评分。在 SWE-bench Verified 的 Best@16 选择中，它较最强对照至少提升 3.5 个百分点；去掉 repository access 会降低效果。

这个结果证明 repository grounding 能改善 criteria 的具体性和可判定性，但不证明 rubric 可以替代最终测试。论文的最终 resolved 判断仍依赖 ground-truth tests，execution-free rubric 更适合作为候选排序、dense feedback 和 tests 难覆盖质量的补充信号。

[SWE-TRACE](https://arxiv.org/abs/2604.14820)则把 rubric 用在 trajectory：辅助 Rubric-Agent 为中间步骤提供 dense process reward，并将同一信号用于 test-time pruning。它代表 rubric 从“评最终作品”扩展到训练和推理过程控制。

## 5. 可靠性与已知失效模式

### 5.1 自动生成 Rubric 不是 Gold Standard

[RubricBench](https://arxiv.org/abs/2603.01562)使用 1,147 个困难 pairwise 样本和专家原子 rubrics，发现当前模型自动生成标准与人类标准仍有明显差距。[Can LLMs Write Reliable Rubrics?](https://arxiv.org/abs/2607.12835)在实验复现任务中同时做 intrinsic 和 downstream meta-evaluation，发现增强上下文后可以接近人类基线，但自动 rubric 仍常出现过度细分、高分偏置和领域适配弱。

因此 rubric generation pipeline 至少要检查：

- Coverage：需求是否被完整覆盖；
- Atomicity：每项是否只判一件事；
- Applicability：criterion 是否适用于当前任务；
- Redundancy：重复项是否放大某类要求；
- Label consistency：criterion 是否真的区分正确与错误样本；
- Adversarial robustness：格式、长度、措辞和无关证据能否影响结论。

### 5.2 Judge 需要 Criterion-level Meta-evaluation

[RuVerBench](https://arxiv.org/abs/2606.29920)包含 deep research 和 agentic coding 的 2,458 条 criterion-level 人类标注。结果显示，前沿 judge 仍有噪声；prompt 变化会显著影响较弱模型，batching 存在准确率与成本权衡，majority vote 有效但边际收益递减。

只报告总分 Pearson/Spearman 会掩盖局部失败。最低可靠性证据应包括：

- criterion-level precision、recall、F1 和混淆矩阵；
- 与专家及专家之间的一致性，如 Cohen's kappa 或 Krippendorff's alpha；
- test-retest、seed、judge model 和 prompt sensitivity；
- `Unknown` / abstain 比例与错误覆盖关系；
- 长度、顺序、自模型偏好和 grader-hacking 的反事实 probe；
- 每项成本、批处理方式与投票策略。

### 5.3 常见设计错误

- Criterion 混入多个可独立失败的要求；
- Rubric 只从任务标题生成，未读取 repo、规格或参考材料；
- 把工具调用路径写死，惩罚能达到正确终态的替代方案；
- 用质量均分覆盖安全、数据破坏或功能失败；
- Judge 看到模型身份、冗长 reasoning 或无关格式线索；
- 修改 judge prompt 后直接在同一校准集报告提升；
- 把 execution-free verifier 当成最终 correctness oracle。

## 6. Coding Agent 的可信 Rubric 最小协议

### 6.1 构建

1. 输入必须包含 task/spec、允许证据和环境契约；存在 reference implementation 时用于证明任务可解，而不是强制实现相似度。
2. 一个 criterion 只描述一个可观察事实；正向要求、禁止项和 critical failure 分开。
3. 默认使用二元 criterion；需要程度判断时使用带行为锚点的 ordinal scale。
4. 权重按风险和业务后果确定，不按“容易测量”确定。
5. 对代码任务，criteria 应引用文件、符号、测试、日志或状态证据，但不锁死无必要的实现细节。

### 6.2 执行

1. 先运行编译、测试、静态检查、安全和终态 hard gates。
2. 再对需求完整性、设计质量、可维护性和受约束过程计算 partial-credit。
3. 每个维度独立 judge，输出 `decision + confidence + evidence`；证据不足返回 `Unknown`。
4. 高风险 criterion 不参与均分抵消，直接触发 fail 或人工复核。
5. 不向 judge 暴露候选模型身份；pairwise 做 answer-order swap，ordinal 做 option-order permutation。

### 6.3 校准与运维

1. 建立包含正例、负例、边界例、对抗例和合理替代实现的专家标注集。
2. 划分 prompt-development 与 held-out validation，避免 judge prompt 对校准集过拟合。
3. 冻结 rubric、judge prompt、judge model、temperature、batching、投票和聚合版本。
4. 定期抽样复审 trajectory 和 evidence；当 task distribution 或模型家族变化时重新校准。
5. Rubric 变更应记录被替换 criterion、原因及历史分数是否可比。

## 7. 选型建议

| 场景 | 推荐 Rubric | 主 Oracle / Grader | 备注 |
|---|---|---|---|
| Bug fix / patch | task-specific repository-grounded checklist | hidden tests + model judge | tests 判功能；rubric 补 spec、integrity、质量 |
| 长程 coding trajectory | analytic process rubric | outcome gate + step judge | 只约束确有价值的安全/效率过程 |
| 研究复现 | hierarchical weighted rubric | clean execution + judge + expert audit | 适合 partial credit；judge 单独做 meta-eval |
| 生产回归 | stable binary criteria | deterministic checks first | 目标接近 100%，持续监控漂移 |
| 能力探索 | difficult task-specific criteria | hybrid grading | 保留区分度，避免过早饱和 |

明确推荐：对本仓库用户的 SE agent eval，采用“执行 hard gates + repository-grounded atomic rubric + criterion-level calibrated judge”的混合路线。不要选“一个通用 LLM 一次给 1–10 总分”作为正式验收。

## 8. 本次仓库更新原则

Rubrics 是横跨 benchmark、methodology 和 meta-analysis 的测量层，不新增第六个 stage。仓库以可选 `rubric` 对象表达：

- `role`：benchmark application / construction method / grading method / meta-evaluation / practice guide；
- `scope`：general / domain-specific / task-specific；
- `target`：artifact / trajectory / both；
- `construction`：expert-authored / model-generated / hybrid；
- `grading`：deterministic / model-based / human / hybrid；
- `form`：analytic / checklist / hierarchical / holistic；
- `calibration`：human agreement / judge benchmark / execution agreement / not reported。

专题页由结构化数据自动生成：[Rubrics for Agent Evaluation](../docs/7-rubrics.md)。

本轮只新增或结构化标注直接满足 SE-agent 范围的高价值资源。HealthBench、FACTS Grounding、通用 instruction-following RubricBench、通用 LLM-Rubric 等保留在报告作为方法证据，不因“使用 rubric”就扩张成泛 LLM 目录。

## 9. 来源与筛选方法

检索时间：2026-07-20。来源优先级为论文正式页面/论文原文、官方机构工程文档和官方代码仓库；二手博客仅用于发现，不作为关键结论的唯一依据。条目进入结构化仓库前按标题、URL 和现有 tags 三层去重，并要求与 SE agent evaluation 有直接关系。

主要一手来源：

- [PaperBench paper](https://arxiv.org/abs/2504.01848)
- [Agent-as-a-Judge, ICML 2025](https://proceedings.mlr.press/v267/zhuge25a.html)
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171)
- [AdaRubric](https://arxiv.org/abs/2603.21362)
- [SWE-TRACE](https://arxiv.org/abs/2604.14820)
- [RuVerBench](https://arxiv.org/abs/2606.29920)
- [Can LLMs Write Reliable Rubrics?](https://arxiv.org/abs/2607.12835)
- [G-Eval, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.153/)
- [LLM-Rubric, ACL 2024](https://aclanthology.org/2024.acl-long.745/)
- [CheckEval, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.796/)
