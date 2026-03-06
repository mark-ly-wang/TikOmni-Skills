#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

import json
from typing import Any, Dict

import scripts.pipeline.asr.asr_pipeline as asr_pipeline


_ORIG_CALL_JSON_API = asr_pipeline.call_json_api
_ORIG_FETCH_TRANSCRIPTION = asr_pipeline.fetch_transcription_text_by_url


def _fake_call_json_api(*, path: str, body: Dict[str, Any] | None = None, **kwargs: Any) -> Dict[str, Any]:
    state = _fake_call_json_api.state

    if path == "/api/u2/v1/services/audio/asr/transcription":
        return {
            "ok": True,
            "status_code": 200,
            "request_id": "mock-submit",
            "error_reason": None,
            "data": {"task_id": "task-batch-001"},
        }

    if path == "/api/u2/v1/tasks/task-batch-001":
        state["poll_count"] += 1
        if state["poll_count"] == 1:
            return {
                "ok": True,
                "status_code": 200,
                "request_id": "mock-poll-1",
                "error_reason": None,
                "data": {
                    "task_id": "task-batch-001",
                    "status": "RUNNING",
                    "platform_task_status": "PARTIAL_SUCCEEDED",
                    "input_count": 3,
                    "succeeded_count": 2,
                    "failed_count": 0,
                    "pending_count": 1,
                    "task_metrics": {"TOTAL": 3, "SUCCEEDED": 2, "FAILED": 0},
                    "results": [
                        {"item_index": 0, "status": "SUCCEEDED", "transcription_url": "https://transcript.success-1.json"},
                        {"item_index": 1, "status": "SUCCEEDED", "transcription_url": "https://transcript.success-2.json"},
                    ],
                },
            }

        return {
            "ok": True,
            "status_code": 200,
            "request_id": "mock-poll-2",
            "error_reason": None,
            "data": {
                "task_id": "task-batch-001",
                "status": "SUCCEEDED",
                "platform_task_status": "PARTIAL_SUCCEEDED",
                "input_count": 3,
                "succeeded_count": 2,
                "failed_count": 1,
                "pending_count": 0,
                "task_metrics": {"TOTAL": 3, "SUCCEEDED": 2, "FAILED": 1},
                "results": [
                    {"item_index": 0, "status": "SUCCEEDED", "transcription_url": "https://transcript.success-1.json"},
                    {"item_index": 1, "status": "SUCCEEDED", "transcription_url": "https://transcript.success-2.json"},
                    {"item_index": 2, "status": "FAILED", "error_reason": "decode_error"},
                ],
            },
        }

    return {
        "ok": False,
        "status_code": 404,
        "request_id": "mock-unknown",
        "error_reason": f"unexpected_path:{path}",
        "data": {},
    }


_fake_call_json_api.state = {"poll_count": 0}


def _fake_fetch_transcription_text_by_url(*, transcription_url: str, timeout_ms: int) -> Dict[str, Any]:
    if "success-1" in transcription_url:
        return {
            "ok": True,
            "transcription_url": transcription_url,
            "error_reason": "",
            "transcript_text": "第一条成功文本",
        }
    if "success-2" in transcription_url:
        return {
            "ok": True,
            "transcription_url": transcription_url,
            "error_reason": "",
            "transcript_text": "第二条成功文本",
        }
    return {
        "ok": False,
        "transcription_url": transcription_url,
        "error_reason": "transcription_payload_empty",
        "transcript_text": "",
    }


def _check(name: str, condition: bool, detail: Dict[str, Any]) -> Dict[str, Any]:
    return {"name": name, "ok": bool(condition), "detail": detail}


def main() -> None:
    asr_pipeline.call_json_api = _fake_call_json_api
    asr_pipeline.fetch_transcription_text_by_url = _fake_fetch_transcription_text_by_url
    try:
        bundle = asr_pipeline.run_u2_asr_batch_with_timeout_retry(
            base_url="https://api.tikomni.com",
            token="mock-token",
            timeout_ms=1000,
            file_urls=[
                "https://media.success-1.mp4",
                "https://media.success-2.mp4",
                "https://media.failed-1.mp4",
            ],
            submit_max_retries=0,
            submit_backoff_ms=0,
            poll_interval_sec=0.01,
            max_polls=4,
            timeout_retry_enabled=False,
            timeout_retry_max_retries=0,
        )

        poll_result = bundle.get("poll_result") if isinstance(bundle.get("poll_result"), dict) else {}
        trace = poll_result.get("trace") if isinstance(poll_result.get("trace"), list) else []
        task_metrics = bundle.get("task_metrics") if isinstance(bundle.get("task_metrics"), dict) else {}
        batch_progress = bundle.get("batch_progress") if isinstance(bundle.get("batch_progress"), dict) else {}

        checks = [
            _check("poll_waits_for_complete_metrics", len(trace) == 2, {"trace_len": len(trace)}),
            _check("batch_complete_true", bool(bundle.get("batch_complete")), {"batch_complete": bundle.get("batch_complete")}),
            _check("batch_progress_complete", bool(batch_progress.get("complete")), batch_progress),
            _check("platform_pending_zero_on_complete", int(batch_progress.get("provider_pending") or 0) == 0, batch_progress),
            _check("task_metrics_total_gt_1", int(task_metrics.get("TOTAL") or 0) > 1, task_metrics),
            _check("results_mapped_all_urls", len(bundle.get("mapped_results") or {}) == 3, {"mapped_count": len(bundle.get("mapped_results") or {})}),
            _check(
                "transcription_url_hydrated_to_text",
                len([item for item in (bundle.get("result_items") or []) if item.get("task_status") == "SUCCEEDED" and item.get("transcript_text")]) == 2,
                {"result_items": bundle.get("result_items") or []},
            ),
        ]

        output = {
            "ok": all(item.get("ok") for item in checks),
            "checks": checks,
            "poll_attempts": _fake_call_json_api.state.get("poll_count"),
            "task_metrics": task_metrics,
            "batch_progress": batch_progress,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        raise SystemExit(0 if output["ok"] else 1)
    finally:
        asr_pipeline.call_json_api = _ORIG_CALL_JSON_API
        asr_pipeline.fetch_transcription_text_by_url = _ORIG_FETCH_TRANSCRIPTION


if __name__ == "__main__":
    main()
