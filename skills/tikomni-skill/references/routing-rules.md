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

## 3. Fixed Routing for Homepage Extraction (Registry-backed, componentized)

1. Douyin author-home route chain:
   - `scripts/cli/run_tikomni_extract.py --platform douyin --content-kind author_home`
   - `scripts/registry/workflow_registry.py` (resolve: `douyin/author_home`)
   - `scripts/author_home/orchestrator/run_author_analysis.py`
   - collector endpoints: `handler_user_profile` + `fetch_user_post_videos`
2. Xiaohongshu author-home route chain:
   - `scripts/cli/run_tikomni_extract.py --platform xiaohongshu --content-kind author_home`
   - `scripts/registry/workflow_registry.py` (resolve: `xiaohongshu/author_home`)
   - `scripts/author_home/orchestrator/run_author_analysis.py`
   - collector endpoints: `fetch_user_info_app` + `fetch_home_notes_app` (with app fallback)
3. Legacy homepage playbooks are decommissioned (migration notes only, no execution path).

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

1. Homepage default sort is latest (Douyin `sort_type=0`; Xiaohongshu fixed latest feed).
2. Default extraction bounds: `page_size=20`, `pages_max=50`, total `max_items=200` (hard cap across platforms).
3. Pagination strategy is cursor loop (`max_cursor` / `cursor`) with dedupe + checkpoint.
4. If user provides quantity constraints, apply safe cap and never exceed 200.

## 6. Fallback Rule

1. When fixed capabilities in matrix are not matched, enter universal fallback flow.
2. Fallback flow must emit complete `fallback_trace` and `missing_fields`.
