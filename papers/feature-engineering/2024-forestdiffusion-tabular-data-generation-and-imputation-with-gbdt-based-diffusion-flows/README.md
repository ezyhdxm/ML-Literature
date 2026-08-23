# ForestDiffusion: Tabular Data Generation and Imputation with GBDT-based Diffusion/Flows

- **Year:** 2024
- **Venue:** AISTATS 2024
- **Category:** Feature engineering
- **Priority:** A — 高优先
- **Status:** Peer-reviewed
- **Survey score:** 77
- **Tags:** GBDT, imputation, synthetic data, diffusion
- **Paper / official page:** https://proceedings.mlr.press/v238/jolicoeur-martineau24a.html
- **Code:** https://github.com/SamsungSAILMontreal/ForestDiffusion

## Why it is in the reading list

适合把 GBDT 能力扩展到 imputation 与场景生成，但不要把 synthetic rows 当作无风险增样；时间一致性与尾部依赖需另检验。

## Survey summary

### Problem

深度生成模型在混合型表格数据上训练不稳，且需要 GPU；能否用树模型学习扩散/流的向量场。

### Method

用 XGBoost 拟合 score 或 flow vector field，处理连续与离散列，支持生成、条件生成和缺失值填补。

### Data / empirical evidence

在 27 个数据集、9 类指标上与深度生成/填补基线比较，论文报告生成与 imputation 均具竞争力，CPU 训练可并行。

### Assumption boundary

不指定简单参数分布，但通过扩散路径与 score 估计引入建模选择。

### Million-row feasibility

树训练可扩展，但多时间步/多目标会放大成本；百万行需减少 diffusion steps、分块与并行。

### Financial time-series fit

中。可用于缺失 quote/size 的敏感性分析；对路径依赖和极端市场联合分布需非常谨慎。

### Rubric

- **A 弱假设:** ●●●●○
- **B 黑盒/GBM:** ●●●●●
- **S 可扩展:** ●●●○○
- **T 金融时序:** ●●●○○
- **E 证据质量:** ●●●●●

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
