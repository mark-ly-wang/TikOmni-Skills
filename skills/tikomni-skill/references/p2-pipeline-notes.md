# P2 Pipeline Refactor Notes

Phase 2 introduces shared runner pipeline helpers under `skills/tikomni-skill/scripts/`:

- `extract_pipeline.py`
  - `request_with_optional_fallback(...)`: shared primary/fallback API request pattern.
  - `build_api_trace(...)`: shared trace payload structure for API call steps.
  - `detect_platform_from_input(...)`: shared URL/text platform routing helper.
- `asr_pipeline.py`
  - `submit_u2_asr(...)`: shared U2 ASR submit call.
  - `submit_u2_asr_with_retry(...)`: shared submit retry/backoff flow.
  - `poll_u2_task_core(...)`: shared U2 poll loop.
  - `clean_transcript_text(...)`: shared transcript normalization hook.

Refactored runners:
- `run_douyin_extract.py`
- `run_xiaohongshu_extract.py`
- `run_tikomni_extract.py`
- `poll_u2_task.py` (now delegates to `asr_pipeline.poll_u2_task_core`)

Compatibility goal for this phase: keep CLI args and output semantics unchanged while reducing duplicated logic.
