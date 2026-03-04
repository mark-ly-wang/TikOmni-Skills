# Routing Rules

## 0. Runtime Structure (Phase A/B)

1. Unified entry: `scripts/cli/run_tikomni_extract.py`.
2. Registry mapping layer: `scripts/registry/workflow_registry.py`.
3. Platform handlers: `scripts/platform/*/`.
4. Shared logic: `scripts/core/` and `scripts/pipeline/`.

## 1. Policy Priority (Hard)

1. Capability priority is defined by `references/capability-routing-matrix.md`.
2. `run_tikomni_extract` parses input, resolves workflow, and executes handler.
3. Registry resolves `(platform, content_kind) -> handler` only.
4. Do not move routing policy priority into registry.

## 2. Global Endpoint Priority

1. For the same platform and intent, prefer `app > web_v2 > web`.
2. If core fields are missing, treat as failure even when HTTP is 2xx.
3. Default fallback chain limit is 3.

## 3. Fixed Routing for Homepage Extraction

1. Douyin homepage extraction route:
   - `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
2. Xiaohongshu homepage extraction route:
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`

## 4. Fixed Routing for Single Content (Registry-backed)

1. Douyin single-video route chain:
   - `scripts/cli/run_tikomni_extract.py`
   - `scripts/registry/workflow_registry.py` (resolve: `douyin/single_video`)
   - `scripts/platform/douyin/run_douyin_single_video.py`
2. Xiaohongshu single-note route chain:
   - `scripts/cli/run_tikomni_extract.py`
   - `scripts/registry/workflow_registry.py` (resolve: `xiaohongshu/note`, alias: `single_video`)
   - `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py`

## 5. Default Parameters

1. Douyin homepage default sort is latest: `sort_type=0`.
2. Default extraction bounds: `limit=20`, `pages_max=50`.
3. If user provides quantity constraints, pass through with safe caps.

## 6. Fallback Rule

1. When fixed capabilities in matrix are not matched, enter universal fallback flow.
2. Fallback flow must emit complete `fallback_trace` and `missing_fields`.
