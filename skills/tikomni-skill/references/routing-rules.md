# Routing Rules

## 1. Global Endpoint Priority

1. For the same platform and intent, prefer `app > web_v2 > web`.
2. If core fields are missing, treat it as a failure even when HTTP is 2xx.
3. Default fallback chain limit is 3.

## 2. Fixed Routing for Homepage Extraction

1. Douyin homepage extraction must use:
   - `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
2. Xiaohongshu homepage extraction must use:
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`

## 3. Default Parameters

1. Douyin homepage default sort is latest: `sort_type=0`.
2. Default extraction bounds: `limit=20`, `pages_max=50`.
3. If users provide quantity constraints, pass them through with safe caps.

## 4. Single Post and Other Tasks

1. Single post extraction is not a fixed playbook.
2. Single post extraction can use free routing from `api-catalog`, but must log routing and fallback traces.
