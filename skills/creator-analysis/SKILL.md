---
name: creator-analysis
description: 在用户要求分析一个创作者、博主、账号主页或作品集合时使用。使用本模块完成作者卡、全量作品事实卡、批量 ASR、分桶抽样、sampled works 批量解释和作者级聚合结论，并支持抖音、小红书及其他平台的创作者分析。
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

1. 读取 `references/contracts/creator-card-fields.md`，获取作者卡必保字段。
2. 读取 `references/contracts/work-card-fields.md`，为全量作品落事实卡。
3. 根据平台读取对应 guide：
   - 抖音：`references/platform-guides/douyin.md`
   - 小红书：`references/platform-guides/xiaohongshu.md`
   - 其他平台：`references/platform-guides/generic.md`
4. 视频作品按 `references/asr-orchestration.md` 进行批量 ASR 和 fallback。
5. 读取 `references/workflow.md`，完成分桶、抽样、sampled explanations、`author_analysis_v2`。
6. 输出作者卡、作品卡和聚合结论。

## 不要做

- 不要把 sampled explanations 原样铺到每个作品卡正文。
- 不要把平台原始过程字段直接暴露到最终卡片正文。
- 不要在 creator 路径里引入逐条作品 LLM 解释。

## References

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
