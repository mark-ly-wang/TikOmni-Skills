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

- `duration_ms`
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

- `author` is the display name, not an object.
- `duration_ms` uses milliseconds. Write `null` when the duration is unavailable or not applicable.
- Fact fields for the Markdown card go into frontmatter. Do not emit a separate `## Facts` section.
- The work-library directory writes only the Markdown card and no extra `.json` sidecar in the same directory.
- `primary_text` is the text that is best suited for reading and indexing in the current task.
- `asr_raw` and `subtitle_raw` are internal preserved text fields. Keep them in the normalized card data, but do not render them as standalone sections in the Markdown body.
- `play_count` may be `null`. Leave it empty when missing, and keep `0` only when the platform explicitly returns `0`.
- Preferred order for video works:
  - `subtitle_raw`
  - `asr_clean`
  - `caption_raw`
- Preferred order for text works:
  - `caption_raw`
- Do not add analytical fields.
