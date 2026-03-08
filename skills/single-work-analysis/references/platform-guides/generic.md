# Generic Single-Content Guide

## Goal

Map an unfamiliar platform's single content item into the unified work-card field dictionary and then complete the single-item analysis.

## Read Order

- Start with `references/api-capability-index.md` to find the relevant platform tag.
- Read the matching `references/api-tags/<tag>.md` for route summaries, inputs, request bodies, and success-response summaries.
- Prioritize routes related to `detail / post / note / video / article / comment / download / subtitle`.
- Decide whether extra comment, subtitle, media-download, or author-supplement routes are needed.

## Minimum Mapping Checklist

- `work_modality`
- `title`
- `caption_raw`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `source_url`
- `share_url`
- for video items: `video_download_url`
- engagement metrics: digg, comment, collect, share, play

## Route Rules

- The detail route must reliably provide `platform_work_id`, main text, author identity, and at least one of media URL or cover image.
- If the detail route does not return subtitles for a video item, keep searching for a subtitle route or a usable download URL before entering ASR.
- If the platform offers App / Web / V2 / V3 variants at the same time, prefer the version with fuller fields and more stable behavior, and keep a recorded fallback.
- Do not skip required-field validation just because one route returns some usable data.
- If U2 still has no result after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback.

## Additional Video Requirements

- If platform subtitles exist, map them to `subtitle_raw` first and then normalize into `asr_raw`.
- If subtitles do not exist, ensure `video_download_url` first and then call ASR.

## Current Runnable Implementation

- `skills/single-work-analysis/scripts/platform/`
- `skills/single-work-analysis/scripts/core/`
