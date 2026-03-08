# Xiaohongshu Single Content Guide

## Read This First

- Use this guide first for Xiaohongshu single-item tasks.
- The validated route chain in this repository is `APP_V2 -> APP_V1 -> WEB_V2 -> WEB_V7`, with the detail route chosen by note type.

## Preferred Resources

- title: `title`
- caption: `desc` / `content`
- work ID: `note_id`
- author ID: platform author identifier
- author handle: readable account identifier
- for video notes, check platform-native subtitles before deciding whether ASR is needed

## Preferred Route Chain

1. Primary routes:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`
   - Typical input: `note_id` or `share_text`
   - Purpose: fetch the most complete note detail based on note type.
2. Fallback 1: `GET /api/u1/v1/xiaohongshu/app/get_note_info`
   - Typical input: `note_id` or `share_text`
3. Fallback 2:
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`
     - Required input: `note_id`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`
     - Required input: `short_url`
4. Fallback 3: `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`
   - Typical input: `note_id` or `share_text`
5. Video transcription:
   - `POST /api/u2/v1/services/audio/asr/transcription`
   - `POST /api/u2/v1/tasks/{task_id}`

## Unified Fields To Fill

- required fields: `platform`, `platform_work_id`, `platform_author_id`, `author_handle`, `title`, `caption_raw`, `work_modality`
- engagement metrics: `digg_count`, `comment_count`, `collect_count`, `share_count`, `play_count`
- source links: `source_url`, `share_url`, `cover_image`
- video-only fields: `video_download_url`, `asr_raw`

## Route Rules

- If the user provides only a short link, try parsing `note_id` from `share_text` first. Use the `short_url`-specific WEB_V2 route only when parsing fails.
- If `note_id` is already known, query by `note_id` directly instead of going through the share-link path.
- Prefer platform-native subtitles for video notes. Trigger U2 ASR only when subtitles are missing and a usable `video_download_url` exists.
- If U2 still has no result after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback.

## Current Runnable Implementation

- `skills/single-work-analysis/scripts/platform/xiaohongshu/`
