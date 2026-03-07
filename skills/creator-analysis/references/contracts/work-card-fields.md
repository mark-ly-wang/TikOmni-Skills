# Creator 作品卡字段字典

## 固定展示字段

- `platform`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `title`
- `caption_raw`
- `work_modality`
- `published_date`
- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `cover_image`
- `source_url`
- `share_url`
- `primary_text`

## 视频作品额外展示字段

- `asr_raw`
- `video_download_url`

## 关键规则

- 全量作品都保留事实卡。
- 最终作品卡不展示 `content_type`、`publish_time`、`create_time_sec`、`subtitle_raw`、`asr_source`、`asr_status`、`asr_error_reason`。
- 视频作品拿不到 `asr_raw` 时，保留事实卡，但标记 `analysis_eligibility=incomplete` 并排除出 creator 分析。
