---
name: single-work-analysis
description: 在用户要求分析一个具体作品时使用，适用于单个视频、单条图文、单篇文本、单个帖子等场景。使用本模块完成标题/文案/ASR 获取、标准作品卡生成、单作品结构化分析，以及陌生平台到统一作品卡字段的映射。
---

# Single Work Analysis

## 何时使用

- 用户要分析一个具体作品，而不是整个人/账号。
- 需要生成标准作品卡。
- 需要对视频做转写，或对文本作品做结构化抽取后分析。
- 平台不是抖音/小红书时，需要先把陌生平台映射到统一作品卡字段。

## 核心规则

- 作品事实字段直接复用统一作品卡字段字典。
- 视频作品的主文本来自 `asr_clean`；文本作品的主文本来自 `caption_raw`。
- 视频作品拿不到 `asr_raw` 时，保留事实卡并返回 `incomplete`，不要伪造分析结论。
- 不做作者级聚合、分桶、抽样、`author_analysis_v2`。

## 工作流程

1. 先识别 `work_modality`：`video` 或 `text`。
2. 读取 `references/contracts/work-card-fields.md`，确认必保字段与展示字段。
3. 根据平台读取对应 guide：
   - 抖音：`references/platform-guides/douyin.md`
   - 小红书：`references/platform-guides/xiaohongshu.md`
   - 其他平台：`references/platform-guides/generic.md`
4. 视频作品按 `references/asr-and-fallback.md` 获取 `subtitle_raw / asr_raw / asr_clean`。
5. 输出标准作品卡，再输出单作品级分析结果。

## 不要做

- 不要输出作者卡。
- 不要引入分桶、抽样、sampled explanations。
- 不要把平台原始过程字段直接暴露到最终作品卡正文。

## References

- 作品卡字段：`references/contracts/work-card-fields.md`
- 作品卡 schema：`references/schemas/work-card.schema.json`
- ASR 与失败路径：`references/asr-and-fallback.md`
- 其他平台指引：`references/platform-guides/generic.md`
- 抖音：`references/platform-guides/douyin.md`
- 小红书：`references/platform-guides/xiaohongshu.md`
