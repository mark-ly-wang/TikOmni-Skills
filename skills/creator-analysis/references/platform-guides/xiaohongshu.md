# Xiaohongshu Creator Guide

## Use This Guide For

- Use this guide first for Xiaohongshu creator, profile, and account tasks.
- The validated creator chain in this repository is profile input -> `user_id` / `xsec_token` resolution -> profile cascade -> post-list cascade.

## Preferred Route Comparator

- source priority: `app > web`
- version priority within the same source: `v2 > v1`
- desired order: `app v2 -> app -> web v2 -> web`

## Validated Route Chain

1. Resolve `user_id` / `xsec_token`: `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
2. Profile cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - Add web-v1 fallback only when the cascade still cannot satisfy creator fields.
3. Post-list cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_notes`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - Add web-v1 fallback only when the cascade still cannot supply stable note fields.

## Required Unified Fields

- creator side:
  - `platform_author_id`
  - `author_handle`
  - `nickname`
  - `ip_location`
  - `signature`
  - `avatar_url`
  - `fans_count`
  - `liked_count`
  - `collected_count`
  - `works_count`
  - `verified`
- work side:
  - `platform_work_id`
  - `title`
  - `caption_raw`
  - `published_date`
  - `digg_count`
  - `comment_count`
  - `collect_count`
  - `share_count`
  - `play_count`
  - `cover_image`
  - `share_url`
  - `source_url`
  - `video_download_url`

## Route Rules

- If `user_id` is already available, skip the resolution route. Treat `xsec_token` as supplemental rather than universally required.
- Apply the comparator above consistently to both profile and post-list cascades.
- Switch to fallback based on field completeness, not only on HTTP success.
- For video items, prefer native subtitles first; only move into batch ASR when native text is insufficient.
- If batch U2 ASR is still incomplete after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback only for the unsuccessful subset.
- If the profile-post chain still cannot provide stable fields, go back to `references/api-capability-index.md` and the matching `references/api-tags/*.md` for supplemental routes instead of sending half-complete data into creator analysis.

## First Stops In Code

- Route and pagination behavior: `skills/creator-analysis/scripts/author_home/collectors/homepage_collectors.py`
- Platform-field normalization: `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- Shared creator pipeline: `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
