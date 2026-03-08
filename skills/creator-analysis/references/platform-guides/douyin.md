# Douyin Creator Guide

## Read This First

- Use this guide first for Douyin creator, profile, and account tasks.
- The validated chain in this repository is profile input -> `sec_user_id` resolution -> creator profile -> paginated post list.

## Preferred Creator Resources

- nickname: `nickname`
- handle: `short_id` / `unique_id`
- IP location
- avatar
- fan count, liked count, work count

## Preferred Work Resources

- work ID: `aweme_id`
- title / caption: `title` / `desc`
- video download URL: prefer the no-watermark path
- engagement metrics: digg, comment, collect, share, play

## Preferred Route Chain

1. Profile identifier resolution: `GET /api/u1/v1/douyin/web/get_sec_user_id`
   - OpenAPI-required input: `url`
   - The current implementation also sends `share_url` redundantly.
2. Creator profile: `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - Required input: `sec_user_id`
3. Paginated post list: `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
   - Required input: `sec_user_id`
   - Common pagination parameters: `max_cursor`, `count`, `sort_type`

## Unified Fields To Fill

- creator card: `platform_author_id`, `author_handle`, `nickname`, `ip_location`, `signature`, `avatar_url`, `fans_count`, `liked_count`, `works_count`, `verified`
- work cards: `platform_work_id`, `title`, `caption_raw`, `published_date`, `digg_count`, `comment_count`, `collect_count`, `share_count`, `play_count`, `video_download_url`

## Route Rules

- If `sec_user_id` is already available, skip the resolution route.
- Default to the latest-post pagination path. Do not search random feed routes first.
- If batch U2 ASR is still incomplete after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback only for the unsuccessful subset.
- If the profile chain still cannot supply key creator fields, go back to `references/api-capability-index.md` and the matching `references/api-tags/*.md` to find supplemental routes instead of giving up on the creator card.

## Current Runnable Implementation

- `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
