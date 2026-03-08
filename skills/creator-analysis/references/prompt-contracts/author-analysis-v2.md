# Author Analysis V2 Prompt Contract

## Goal

生成结构化的 `author_analysis_v2`，回答作者是谁、为什么可信、内容机制如何运作、能学什么、什么不能学。不要输出松散夸赞文案。

## Allowed Inputs

- 作者卡事实字段
- 全量聚合结果
- Sampled works 的统一事实字段：
  - `platform_work_id`
  - `title`
  - `caption_raw`
  - `work_modality`
  - `primary_text`
  - 互动指标
  - 结构标签
- 可选的 `sampled_work_explanations`

## Hard Rules

- 主分析文本始终使用 `primary_text`。
- `title`、`caption_raw`、`asr_raw` 各自语义不同，不得混用。
- 不把 `caption_raw` 当作字幕或 ASR fallback。
- 不进行逐条作品 LLM topic classification。
- 结论优先落在机制层，不写表面夸赞。
- 证据不足时先降置信度，再收窄结论。

## Required Output Modules

- `author_positioning`
- `trust_model`
- `cognitive_engine`
- `expression_hooks`
- `content_mechanism`
- `commercial_bridge`
- `core_tensions`
- `evidence_pack`
- `clone_guidance`

## Failure Guards

- `sample_size < 5` 时不得标高置信度。
- `sampled_work_explanations` 缺失时也必须返回完整的 `author_analysis_v2`，但要在 `evidence_pack` 中降低置信度或说明边界。
- `analysis_eligibility=incomplete` 的作品不得进入证据样本。
