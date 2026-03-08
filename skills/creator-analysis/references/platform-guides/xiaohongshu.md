# Xiaohongshu Creator Guide

## Read This First

- Use this guide first for Xiaohongshu creator, profile, and account tasks.
- The validated chain in this repository is profile input -> `user_id` / `xsec_token` resolution -> profile cascade -> post-list cascade.

## Preferred Creator Resources

- nickname
- handle
- IP location
- avatar
- fan count, liked count, work count

## Preferred Work Resources

- work ID: `note_id`
- title / caption: `title` / `desc` / `content`
- for video items, check native subtitles first
- engagement metrics: digg, comment, collect, share, play

## Preferred Route Chain

1. Profile identifier resolution: `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
   - OpenAPI-required input: `share_link`
   - The current implementation also sends `share_url` and `url` redundantly.
2. Profile cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_info`
   - Typical input: `user_id`, with `share_text` / `xsec_token` as needed
3. Post-list cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_notes`
   - Typical input: `user_id`, `cursor`

## Unified Fields To Fill

- creator card: `platform_author_id`, `author_handle`, `nickname`, `ip_location`, `signature`, `avatar_url`, `fans_count`, `liked_count`, `collected_count`, `works_count`, `verified`
- work cards: `platform_work_id`, `title`, `caption_raw`, `published_date`, `digg_count`, `comment_count`, `collect_count`, `share_count`, `play_count`, `video_download_url`

## Route Rules

- If `user_id` is already available, skip the resolution route. Treat `xsec_token` as supplemental rather than universally required.
- Try both the profile cascade and the posts cascade in order, and switch to fallback based on field completeness.
- If batch U2 ASR is still incomplete after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback only for the unsuccessful subset.
- If the profile-post chain still cannot provide stable fields, go back to `references/api-capability-index.md` and the matching `references/api-tags/*.md` for supplemental routes instead of sending half-complete data into creator analysis.

## Current Runnable Implementation

- `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
