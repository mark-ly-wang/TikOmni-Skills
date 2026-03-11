# Work Fact Card Fields

## Required Fields

- `platform`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `author`
- `title`
- `caption_raw`
- `work_modality`
- `published_date`
- `cover_image`
- `source_url`
- `share_url`
- `primary_text`
- `primary_text_source`
- `request_id`
- `completeness`
- `missing_fields`
- `error_reason`
- `extract_trace`

## Optional Fields

- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `video_download_url`
- `asr_raw`
- `asr_clean`
- `subtitle_raw`

## Field Rules

- `author` 是展示名，不是对象。
- Markdown 卡片的事实字段进入 frontmatter，不再输出 `## Facts` 章节。
- `primary_text` 为当前任务最适合阅读和索引的主文本。
- `play_count` 允许为 `null`；缺失时卡片展示为空，只有平台明确返回 `0` 时才保留 `0`。
- 视频优先顺序：
  - `subtitle_raw`
  - `asr_clean`
  - `caption_raw`
- 文本作品优先顺序：
  - `caption_raw`
- 不允许出现分析字段。
