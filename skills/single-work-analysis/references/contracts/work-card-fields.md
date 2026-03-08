# Work Card Fields

## Final Display Fields

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

## Video-Only Additional Fields

- `asr_raw`
- `video_download_url`

## Key Semantics

- `caption_raw` is the author-written description, caption, or body text. It is not subtitles and it is not raw ASR.
- `primary_text` is the main display text and the main analysis text:
  - video: `primary_text = asr_clean`
  - text: `primary_text = caption_raw`
- `video_download_url` is a required field for video items and should default to the no-watermark download URL when available.
- `subtitle_raw` is a collection-layer source field and should not appear in the final work-card body.

## Missing-Value Rules

- Missing numeric fields should be rendered as `N/A` in the display layer.
- Preserve `0` when the platform explicitly returns `0`.
- Generate `published_date` in the display timezone, with `Asia/Shanghai` as the default.
