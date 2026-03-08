---
name: single-work-analysis
description: 用于跨平台单作品抽取、转写、对标、拆解与结构化分析，适用于单个视频、单条图文、单篇文章、单个帖子、单条笔记等场景。当用户提到“对标”“拆解”“提取文案/标题/字幕/ASR”“分析作品/视频/图文/帖子/文章/笔记”“生成作品卡”或要求输出单条内容的结构化字段/结构化数据时触发；适用于抖音、小红书及其他平台的单条内容，不用于作者/账号主页分析。
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
2. 先读 `references/api-capability-index.md`，锁定当前平台 tag；再按需读 `references/api-tags/*.md`，确认单作品 detail / comment / media / subtitle 相关 route、认证方式与关键字段；如果需要精确字段说明、默认值、示例或完整响应结构，再读 `references/api-contracts/*.md`。
3. 读取 `references/contracts/work-card-fields.md`，确认必保字段与展示字段。
4. 根据平台读取对应 guide：
   - 抖音：`references/platform-guides/douyin.md`
   - 小红书：`references/platform-guides/xiaohongshu.md`
   - 其他平台：`references/platform-guides/generic.md`
5. 视频作品先读 `references/service-guides/asr-u2-u3-fallback.md`，再按 `references/asr-and-fallback.md` 获取 `subtitle_raw / asr_raw / asr_clean`。
6. 输出标准作品卡，再输出单作品级分析结果。

## 不要做

- 不要输出作者卡。
- 不要引入分桶、抽样、sampled explanations。
- 不要把平台原始过程字段直接暴露到最终作品卡正文。

## References

- API 能力索引：`references/api-capability-index.md`
- 按 tag 路由详情：`references/api-tags/`
- 按 tag 完整契约：`references/api-contracts/`
- U2/U3 ASR fallback：`references/service-guides/asr-u2-u3-fallback.md`
- 作品卡字段：`references/contracts/work-card-fields.md`
- 作品卡 schema：`references/schemas/work-card.schema.json`
- ASR 与失败路径：`references/asr-and-fallback.md`
- 其他平台指引：`references/platform-guides/generic.md`
- 抖音：`references/platform-guides/douyin.md`
- 小红书：`references/platform-guides/xiaohongshu.md`
