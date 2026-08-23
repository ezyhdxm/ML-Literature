# FeatLLM: Large Language Models for Few-shot Feature Engineering

- **Year:** 2024
- **Venue:** ICML 2024
- **Category:** Feature engineering
- **Priority:** B — 选择性阅读
- **Status:** Peer-reviewed
- **Survey score:** 79
- **Tags:** LLM, rules, few-shot, tabular
- **Paper / official page:** https://proceedings.mlr.press/v235/han24f.html

## Why it is in the reading list

论文最终预测器较简单，但“先生成规则、再交给 GBM”非常可迁移。适合冷启动、低样本新产品或新 issuer；不适合直接替代时序验证。

## Survey summary

### Problem

在标注样本很少时，如何把 LLM 的领域知识转成结构化规则与特征，而不在每个样本上调用 LLM。

### Method

LLM 生成类别级规则，规则匹配形成稀疏特征，再训练轻量预测器；推理阶段不需要逐行 LLM。

### Data / empirical evidence

在多类公开分类数据上与 TabLLM、STUNT 等 few-shot 方法比较，论文报告平均表现有明显提升。

### Assumption boundary

弱分布假设；依赖语义丰富的列名、标签定义和 LLM 能否提出可执行且无泄漏的规则。

### Million-row feasibility

规则生成成本与表大小弱相关，规则矩阵可稀疏化；全量百万行通常可行。

### Financial time-series fit

中。适合稀疏事件或新资产类别；成熟高频信号仍应以数据驱动搜索为主。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●○
- **S 可扩展:** ●●●●●
- **T 金融时序:** ●●○○○
- **E 证据质量:** ●●●●○

## My questions

<!-- Write questions below. Keep this heading so follow-up tooling can find it reliably. -->

- 

## My thoughts

<!-- Write your interpretation, objections, connections, or experiment ideas below. -->

- 

## Experiments / implementation ideas

- 

## Assistant follow-up

<!-- Future answers can be added here, or linked to a standalone report under reports/. -->

_No follow-up yet._
