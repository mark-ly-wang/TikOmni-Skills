---
name: creator-analysis
description: 用于跨平台创作者、博主、达人、UP 主、账号主页与作品集合分析。当用户提到“账号分析”“创作者分析”“博主分析”“主页分析”“账号对标”“账号拆解”“分析某个账号/博主/达人/UP 主”“作者卡”“主页作品汇总”或要求输出账号主页的结构化数据、全量作品事实卡、抽样解释、聚合结论时触发；适用于抖音、小红书及其他平台的账号主页或作品集合，不用于单个作品分析。
---

# Creator Analysis

## 何时使用

- 用户要分析一个创作者/博主/账号，而不是单个作品。
- 需要输出作者卡、全量作品卡、抽样解释和作者级结论。
- 需要对主页下多个视频优先走批量 ASR。
- 平台不是抖音/小红书时，需要先把陌生平台映射到统一作品卡和作者卡字段。

## 核心规则

- 全量作品保留事实卡，但不做逐条 LLM deep analysis。
- 视频作品优先走批量 ASR，单次最多 100 条链接。
- sampled works 的解释字段只能来自一次批量 LLM 分析。
- `author_analysis_v2` 是正式的作者级主分析对象。

## 工作流程

1. 先读 `references/api-capability-catalog.md`，确认当前平台有哪些主页、作者、作品列表、评论和媒体相关 route，以及 route 的入参字段。
2. 读取 `references/contracts/creator-card-fields.md`，获取作者卡必保字段。
3. 读取 `references/contracts/work-card-fields.md`，为全量作品落事实卡。
4. 根据平台读取对应 guide：
   - 抖音：`references/platform-guides/douyin.md`
   - 小红书：`references/platform-guides/xiaohongshu.md`
   - 其他平台：`references/platform-guides/generic.md`
5. 视频作品按 `references/asr-orchestration.md` 进行批量 ASR 和 fallback。
6. 读取 `references/workflow.md`，完成分桶、抽样、sampled explanations、`author_analysis_v2`。
7. 输出作者卡、作品卡和聚合结论。

## 不要做

- 不要把 sampled explanations 原样铺到每个作品卡正文。
- 不要把平台原始过程字段直接暴露到最终卡片正文。
- 不要在 creator 路径里引入逐条作品 LLM 解释。

## References

- API 能力总表：`references/api-capability-catalog.md`
- 作者卡字段：`references/contracts/creator-card-fields.md`
- 作品卡字段：`references/contracts/work-card-fields.md`
- ASR 编排：`references/asr-orchestration.md`
- Creator 工作流：`references/workflow.md`
- 作者级 prompt：`references/prompt-contracts/author-analysis-v2.md`
- Sampled explanations prompt：`references/prompt-contracts/sampled-work-batch-explanations.md`
- 作者级 schema：`references/schemas/author-analysis-v2.schema.json`
- Sampled explanations schema：`references/schemas/sampled-work-batch-explanations.schema.json`
- 其他平台指引：`references/platform-guides/generic.md`
- 抖音：`references/platform-guides/douyin.md`
- 小红书：`references/platform-guides/xiaohongshu.md`
