# Large Language Models Engineer Too Many Simple Features for Tabular Data

- **Year:** 2024
- **Venue:** NeurIPS 2024 Table Representation Learning Workshop — Oral
- **Category:** Feature engineering
- **Priority:** A — 高优先
- **Status:** Workshop oral / preprint
- **Survey score:** 92
- **Tags:** LLM, negative result, AutoFE, benchmark
- **Paper / official page:** https://arxiv.org/abs/2410.17787

## Why it is in the reading list

这是避免被“LLM feature engineer”营销误导的必读负面结果。生产 harness 应显式提供 group/time operators，并让验证器而非 LLM 决定保留。

## Survey summary

### Problem

LLM 做特征工程时到底在生成什么，是否真的利用了复杂表结构。

### Method

系统比较多个 LLM 在多数据集上的特征建议，分析操作类型、复杂度、有效率与失败模式。

### Data / empirical evidence

覆盖 4 个 LLM 与 27 个数据集；发现模型偏爱加减乘除等简单操作，较少使用分组/聚合，且生成特征有时会伤害性能。

### Assumption boundary

经验研究，几乎无分布假设；结论依赖所测 LLM、prompt 与 operator library。

### Million-row feasibility

诊断结论本身可直接采用；LLM 搜索仍需样本化。

### Financial time-series fit

高。金融有大量必须显式表达的时间窗和横截面操作，通用 LLM 的“简单算术偏好”尤其危险。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●○
- **S 可扩展:** ●●●●●
- **T 金融时序:** ●●●●●
- **E 证据质量:** ●●●○○

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
