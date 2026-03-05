# TikOmni Skill (Dev Layer)

## Recent Pipeline Guarantees

### 1) Global API Governance
- Global rate limit: `QPS=5` (default, `TIKOMNI_GLOBAL_QPS` override)
- Timeout retry: `3` retries per API call (`TIKOMNI_TIMEOUT_RETRY_MAX`)
- Retry backoff: exponential (`TIKOMNI_TIMEOUT_RETRY_BACKOFF_MS`)
- Unified trace fields:
  - `rate_limit_wait_ms`
  - `retry_attempt`
  - `fallback_trigger_reason`

### 2) Author Home ASR Rules
- Douyin homepage works: always try U2 ASR
- Xiaohongshu homepage works:
  1. Prefer API subtitle
  2. Subtitle invalid (`empty/too_short<20/garbled/timeline_only/noise`) => fallback U2
  3. If both unavailable => `asr_source=fallback_none`
- Output enum: `asr_source in {xhs_subtitle,u2,fallback_none}`

### 3) Author Benchmark Card
- Author card rendering is decoupled from work card rendering
- Author analysis is Prompt-First via `references/prompt-contracts/author-analysis.md`
- Minimal schema required fields:
  - `business_score`
  - `benchmark_gap_score`
  - `style_radar`
  - `core_contradictions`
  - `recommendations`

### 4) Stability
- Author-home ASR supports:
  - checkpoint resume (`checkpoint.completed_work_ids`)
  - idempotent dedupe by `platform_work_id`
  - U2 batch submit (`file_urls`) with configurable size (default 50, hard max 100)
  - batch submit/poll mapping by `file_url`, with single-item fallback for unmapped/failed results
  - batch-level trace events (`submitted/completed/mapped/unmapped/fallback`)

## Entry
Use `scripts/cli/run_tikomni_extract.py` with `--content-kind author_home` for homepage flows.
