# Generic Creator Guide

## Goal

Map an unfamiliar platform into the unified creator-card and work-card contracts and then complete the creator analysis flow.

## Read Order

- Start with `references/api-capability-index.md` to lock onto the relevant platform tag.
- Read the matching `references/api-tags/<tag>.md` for route summaries, inputs, request bodies, and success-response summaries.
- Prioritize routes related to `user / author / creator / profile / home / channel / posts / notes / videos`.
- Add comment, media-download, subtitle, and extra-metric routes only when needed.

## Minimum Mapping Checklist

creator side:

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

work side:

- the required fields from the unified work-card field dictionary
- for video items: `video_download_url`

## Route Rules

- The creator-profile chain must cover both creator information and paginated work-list retrieval. Do not stop at a profile-only route.
- If the platform provides multiple profile routes or posts routes, prefer the variant with fuller fields and more stable pagination.
- The work-list route must reliably provide `platform_work_id` and the main published-time and engagement fields before sampling or aggregation can begin.
- If video items have no subtitles and no download path, mark ASR as infeasible at the route-selection stage.
- If batch U2 ASR is still incomplete after 120 seconds, follow `references/service-guides/asr-u2-u3-fallback.md` and use U3 fallback only for the unsuccessful subset.

## Current Runnable Implementation

- `skills/creator-analysis/scripts/author_home/`
- `skills/creator-analysis/scripts/core/`
