# Douyin Creator Guide

## Use This Guide For

- Use this guide first for Douyin creator, profile, and account tasks.
- The validated creator chain in this repository is profile input -> `sec_user_id` resolution -> creator profile -> paginated post list.

## Validated Route Chain

1. Resolve `sec_user_id`: `GET /api/u1/v1/douyin/web/get_sec_user_id`
2. Fetch creator profile: `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
3. Fetch paginated post list: `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`

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

- If `sec_user_id` is already available, skip the resolution route.
- Default to the latest-post pagination path. Do not search random feed routes first.
- The post-list route must supply stable `aweme_id`, publish time, and engagement fields before creator analysis can continue.
- If batch U2 ASR is still incomplete after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback only for the unsuccessful subset.
- If the profile chain still cannot supply key creator fields, go back to `references/api-capability-index.md` and the matching `references/api-tags/*.md` to find supplemental routes instead of giving up on the creator card.

## First Stops In Code

- Route and pagination behavior: `skills/creator-analysis/scripts/author_home/collectors/homepage_collectors.py`
- Platform-field normalization: `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- Shared creator pipeline: `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
