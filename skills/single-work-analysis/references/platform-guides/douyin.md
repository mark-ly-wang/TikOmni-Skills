# Douyin Single Content Guide

## Read This First

- Use this guide first for Douyin single-item tasks.
- The validated chain in this repository currently covers share URL -> single-video detail -> ASR when needed.

## Preferred Resources

- title: `title`
- caption: `desc`
- work ID: `aweme_id`
- author ID: stable author identifier
- author handle: `short_id` / `unique_id`
- video download URL: prefer the no-watermark download URL

## Preferred Route Chain

1. Primary route: `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`
   - Required input: `share_url`
   - Purpose: fetch single-item detail, basic author fields, engagement metrics, and media resources.
2. Fallback route: `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`
   - Required input: `share_url`
   - Purpose: fallback when the app route fails or returns insufficient fields.
3. Video transcription:
   - `POST /api/u2/v1/services/audio/asr/transcription`
   - polling: `POST /api/u2/v1/tasks/{task_id}`
   - key request-body field: `input.file_urls[]`
   - Purpose: produce `asr_raw` when the platform does not return usable subtitles.

## Unified Fields To Fill

- required fields: `platform`, `platform_work_id`, `platform_author_id`, `author_handle`, `title`, `caption_raw`, `work_modality`
- engagement metrics: `digg_count`, `comment_count`, `collect_count`, `share_count`, `play_count`
- source links: `source_url`, `share_url`, `cover_image`
- video-only fields: `video_download_url`, `asr_raw`

## Route Rules

- If the user provides only a share URL, use the primary route chain directly instead of searching for other detail routes first.
- Prefer platform-native subtitles for video items. Call U2 ASR only when usable `subtitle_raw` or `asr_raw` is missing.
- If U2 still has no result after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback.
- If the target is comments, search, rankings, or another non-single-item task, leave this guide and go back to `references/api-capability-index.md` for route discovery.

## Current Runnable Implementation

- `skills/single-work-analysis/scripts/platform/douyin/`
