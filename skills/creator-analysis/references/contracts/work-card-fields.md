# Creator Work Card Fields

## Fixed Display Fields

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

## Key Rules

- Keep fact cards for all retrieved works.
- The final work card should not expose `content_type`, `publish_time`, `create_time_sec`, `subtitle_raw`, `asr_source`, `asr_status`, or `asr_error_reason`.
- If a video item cannot obtain `asr_raw`, keep the fact card but mark `analysis_eligibility=incomplete` and exclude that item from creator analysis.
