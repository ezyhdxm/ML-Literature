# CAAFE: Context-Aware Automated Feature Engineering with LLMs

- **Year:** 2023
- **Venue:** NeurIPS 2023
- **Category:** Feature engineering
- **Priority:** A — 高优先
- **Status:** Peer-reviewed
- **Survey score:** 82
- **Tags:** LLM, AutoFE, semantic features, few-shot
- **Paper / official page:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c2df4c35cdbee764ebb9e9d0acd5197-Abstract-Conference.html
- **Code:** https://github.com/automl/CAAFE

## Why it is in the reading list

LLM 最适合作为候选生成器，而不是最终裁判。必须把允许的 API、历史窗口、group key 与可用时点写进 harness，并自动拒绝 target leakage。

## Survey summary

### Problem

传统 AutoFE 只看数值关系，无法利用列名、领域语义与数据集描述。

### Method

让 LLM 迭代提出可执行 Python 特征，并用验证反馈筛选；特征同时带自然语言解释。

### Data / empirical evidence

在 14 个数据集上与强 tabular baselines 比较，11 个数据集得到改善；论文报告平均 ROC-AUC 从 0.798 提升到 0.822。

### Assumption boundary

对 (X,Y) 几乎无模型假设，但依赖列语义、LLM 先验与验证集可信度；结果有随机性。

### Million-row feasibility

LLM 调用本身与行数无关，真正成本来自多轮训练；百万行应在时间分层小样本上打分。

### Financial time-series fit

中高。对有清晰业务语义的 RFQ、交易、报价字段有价值；对匿名化字段或强时变关系价值下降。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●○
- **S 可扩展:** ●●●●○
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
