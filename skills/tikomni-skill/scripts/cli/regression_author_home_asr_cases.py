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

import scripts.author_home.asr.home_asr as home_asr


_ORIG_U2_SINGLE = home_asr.run_u2_asr_candidates_with_timeout_retry
_ORIG_U2_BATCH = home_asr.run_u2_asr_batch_with_timeout_retry


def _fake_u2_runner(**kwargs):
    candidates = kwargs.get("candidates") or []
    selected = candidates[0] if candidates else ""
    if "success" in selected:
        return {
            "submit_bundle": {"submit_response": {"ok": True}, "task_id": "task-success"},
            "poll_result": {
                "ok": True,
                "task_status": "SUCCEEDED",
                "transcript_text": "这是模拟的 U2 转写文本，长度足够用于测试。",
                "error_reason": None,
            },
            "rounds": [{"round": 1}],
            "candidate_attempts": [{"candidate": selected, "ok": True}],
            "timeout_retry": {"enabled": True, "triggered": False},
            "chosen_candidate": selected,
        }

    return {
        "submit_bundle": {"submit_response": {"ok": False, "error_reason": "UPSTREAM_TIMEOUT"}, "task_id": None},
        "poll_result": {
            "ok": False,
            "task_status": "FAILED",
            "transcript_text": "",
            "error_reason": "u2_failed",
        },
        "rounds": [{"round": 1}],
        "candidate_attempts": [{"candidate": selected, "ok": False}],
        "timeout_retry": {"enabled": True, "triggered": True, "result": "retry_timeout_exhausted"},
        "chosen_candidate": selected,
    }


def _fake_u2_batch_runner(**kwargs):
    file_urls = kwargs.get("file_urls") or []
    if any("submitfail" in str(url) for url in file_urls):
        total = len(file_urls)
        progress = {
            "expected_total": total,
            "target_total": total,
            "metrics_total": 0,
            "metrics_succeeded": 0,
            "metrics_failed": 0,
            "metrics_completed": 0,
            "results_total": 0,
            "results_succeeded": 0,
            "results_failed": 0,
            "results_completed": 0,
            "complete": False,
            "completion_basis": "pending",
            "metrics": {},
        }
        return {
            "submit_bundle": {
                "submit_response": {"ok": False, "status_code": 503, "error_reason": "UPSTREAM_TIMEOUT"},
                "task_id": None,
                "retry_chain": [{"attempt": 1, "ok": False, "error_reason": "UPSTREAM_TIMEOUT"}],
                "final_submit_status": "failed_retries_exhausted",
                "file_urls": list(file_urls),
            },
            "poll_result": {
                "ok": False,
                "task_id": None,
                "task_status": "UNKNOWN",
                "request_id": "mock-batch-failed",
                "error_reason": "u2_submit_failed_or_missing_task_id",
                "raw_task": {},
                "task_metrics": {},
                "batch_results": {},
                "batch_progress": progress,
                "batch_complete": False,
                "trace": [],
            },
            "rounds": [{"round": 1}],
            "timeout_retry": {"enabled": True, "triggered": False, "result": "not_triggered"},
            "normalized_file_urls": list(file_urls),
            "mapped_results": {},
            "result_items": [],
            "task_metrics": {},
            "batch_progress": progress,
            "batch_complete": False,
        }

    mapped_results = {}
    success = 0
    failed = 0

    for url in file_urls:
        if "success" in str(url):
            success += 1
            mapped_results[url] = {
                "file_url": url,
                "task_status": "SUCCEEDED",
                "transcript_text": "这是模拟的批量 U2 转写文本，长度足够用于测试。",
                "error_reason": "",
                "ok": True,
            }
        else:
            failed += 1
            mapped_results[url] = {
                "file_url": url,
                "task_status": "FAILED",
                "transcript_text": "",
                "error_reason": "u2_failed",
                "ok": False,
            }

    total = len(file_urls)
    progress = {
        "expected_total": total,
        "target_total": total,
        "metrics_total": total,
        "metrics_succeeded": success,
        "metrics_failed": failed,
        "metrics_completed": success + failed,
        "results_total": len(mapped_results),
        "results_succeeded": success,
        "results_failed": failed,
        "results_completed": success + failed,
        "complete": True,
        "completion_basis": "task_metrics",
        "metrics": {"TOTAL": total, "SUCCEEDED": success, "FAILED": failed},
    }

    return {
        "submit_bundle": {
            "submit_response": {"ok": True, "status_code": 200},
            "task_id": "task-batch-success",
            "retry_chain": [{"attempt": 1, "ok": True}],
            "final_submit_status": "success",
            "file_urls": list(file_urls),
        },
        "poll_result": {
            "ok": failed == 0,
            "task_id": "task-batch-success",
            "task_status": "SUCCEEDED",
            "request_id": "mock-batch",
            "error_reason": None if failed == 0 else "u2_task_failed_partial",
            "raw_task": {},
            "task_metrics": {"TOTAL": total, "SUCCEEDED": success, "FAILED": failed},
            "batch_results": mapped_results,
            "batch_progress": progress,
            "batch_complete": True,
            "trace": [{"attempt": 1}],
        },
        "rounds": [{"round": 1}],
        "timeout_retry": {"enabled": True, "triggered": False, "result": "not_needed"},
        "normalized_file_urls": list(file_urls),
        "mapped_results": mapped_results,
        "result_items": list(mapped_results.values()),
        "task_metrics": {"TOTAL": total, "SUCCEEDED": success, "FAILED": failed},
        "batch_progress": progress,
        "batch_complete": True,
    }


def _check(label: str, condition: bool, detail: dict) -> dict:
    return {
        "name": label,
        "ok": bool(condition),
        "detail": detail,
    }


def main() -> None:
    home_asr.run_u2_asr_candidates_with_timeout_retry = _fake_u2_runner
    home_asr.run_u2_asr_batch_with_timeout_retry = _fake_u2_batch_runner
    try:
        douyin_bundle = home_asr.enrich_author_home_asr(
            platform="douyin",
            works=[
                {
                    "platform": "douyin",
                    "platform_work_id": "dy-ok",
                    "is_video": True,
                    "duration_ms": 20000,
                    "video_down_url": "https://video.success.mp4",
                    "raw_ref": {},
                },
                {
                    "platform": "douyin",
                    "platform_work_id": "dy-missing",
                    "is_video": True,
                    "duration_ms": 20000,
                    "video_down_url": "",
                    "raw_ref": {},
                },
                {
                    "platform": "douyin",
                    "platform_work_id": "dy-bad",
                    "is_video": True,
                    "duration_ms": 20000,
                    "video_down_url": "https://video.fail.mp4",
                    "raw_ref": {},
                },
                {
                    "platform": "douyin",
                    "platform_work_id": "dy-short",
                    "is_video": True,
                    "duration_ms": 12000,
                    "video_down_url": "https://video.short.mp4",
                    "raw_ref": {},
                },
            ],
            base_url="https://api.tikomni.com",
            token="mock",
            timeout_ms=1000,
            batch_size=2,
        )

        xhs_bundle = home_asr.enrich_author_home_asr(
            platform="xiaohongshu",
            works=[
                {
                    "platform": "xiaohongshu",
                    "platform_work_id": "xhs-subtitle",
                    "is_video": True,
                    "duration_ms": 24000,
                    "video_down_url": "https://video.fail.mp4",
                    "asr_raw": "这是可用字幕内容，字数明显超过二十个字符，能够直接用于分析。",
                    "raw_ref": {"subtitle_inline": ""},
                },
                {
                    "platform": "xiaohongshu",
                    "platform_work_id": "xhs-missing-subtitle",
                    "is_video": True,
                    "duration_ms": 24000,
                    "video_down_url": "https://video.success.mp4",
                    "asr_raw": "",
                    "raw_ref": {"subtitle_inline": "", "subtitle_urls": []},
                },
                {
                    "platform": "xiaohongshu",
                    "platform_work_id": "xhs-bad-subtitle",
                    "is_video": True,
                    "duration_ms": 24000,
                    "video_down_url": "",
                    "asr_raw": "00:00 --> 00:02",
                    "raw_ref": {"subtitle_inline": "00:00 --> 00:02", "subtitle_urls": []},
                },
                {
                    "platform": "xiaohongshu",
                    "platform_work_id": "xhs-not-video",
                    "is_video": False,
                    "duration_ms": 24000,
                    "video_down_url": "https://video.success.mp4",
                    "asr_raw": "",
                    "raw_ref": {"subtitle_inline": "", "subtitle_urls": []},
                },
            ],
            base_url="https://api.tikomni.com",
            token="mock",
            timeout_ms=1000,
            batch_size=2,
        )

        dy_map = {item.get("platform_work_id"): item for item in douyin_bundle.get("works", []) if isinstance(item, dict)}
        xhs_map = {item.get("platform_work_id"): item for item in xhs_bundle.get("works", []) if isinstance(item, dict)}

        dy_stats = douyin_bundle.get("stats") if isinstance(douyin_bundle.get("stats"), dict) else {}
        xhs_stats = xhs_bundle.get("stats") if isinstance(xhs_bundle.get("stats"), dict) else {}
        dy_submit_fail_bundle = home_asr.enrich_author_home_asr(
            platform="douyin",
            works=[
                {
                    "platform": "douyin",
                    "platform_work_id": "dy-submit-fail",
                    "is_video": True,
                    "duration_ms": 20000,
                    "video_down_url": "https://video.submitfail.mp4",
                    "raw_ref": {},
                }
            ],
            base_url="https://api.tikomni.com",
            token="mock",
            timeout_ms=1000,
            batch_size=2,
        )
        dy_submit_fail_stats = dy_submit_fail_bundle.get("stats") if isinstance(dy_submit_fail_bundle.get("stats"), dict) else {}

        checks = [
            _check("douyin_u2_success", dy_map.get("dy-ok", {}).get("asr_source") == "u2", dy_map.get("dy-ok", {})),
            _check(
                "douyin_missing_video",
                dy_map.get("dy-missing", {}).get("asr_error_reason") == "skip:video_down_url_missing",
                dy_map.get("dy-missing", {}),
            ),
            _check("douyin_bad_u2", dy_map.get("dy-bad", {}).get("asr_source") == "fallback_none", dy_map.get("dy-bad", {})),
            _check(
                "douyin_duration_short_gate",
                dy_map.get("dy-short", {}).get("asr_error_reason") == "skip:duration_too_short",
                dy_map.get("dy-short", {}),
            ),
            _check("xhs_subtitle_available", xhs_map.get("xhs-subtitle", {}).get("asr_source") == "xhs_subtitle", xhs_map.get("xhs-subtitle", {})),
            _check("xhs_subtitle_missing", xhs_map.get("xhs-missing-subtitle", {}).get("asr_source") == "u2", xhs_map.get("xhs-missing-subtitle", {})),
            _check(
                "xhs_subtitle_bad_gate",
                xhs_map.get("xhs-bad-subtitle", {}).get("asr_error_reason") == "skip:video_down_url_missing",
                xhs_map.get("xhs-bad-subtitle", {}),
            ),
            _check(
                "xhs_not_video_gate",
                xhs_map.get("xhs-not-video", {}).get("asr_error_reason") == "skip:not_video",
                xhs_map.get("xhs-not-video", {}),
            ),
            _check("douyin_batch_submitted", int(dy_stats.get("submitted_batches") or 0) >= 1, dy_stats),
            _check("douyin_batch_completed", int(dy_stats.get("completed_batches") or 0) >= 1, dy_stats),
            _check("douyin_batch_fallback", int(dy_stats.get("fallback_singles") or 0) >= 1, dy_stats),
            _check("xhs_batch_submitted", int(xhs_stats.get("submitted_batches") or 0) >= 1, xhs_stats),
            _check("submit_failure_not_counted_as_submitted", int(dy_submit_fail_stats.get("submitted_batches") or 0) == 0, dy_submit_fail_stats),
            _check("submit_failure_keeps_fallback_single", int(dy_submit_fail_stats.get("fallback_singles") or 0) == 1, dy_submit_fail_stats),
        ]

        output = {
            "ok": all(item.get("ok") for item in checks),
            "checks": checks,
            "stats": {
                "douyin": dy_stats,
                "xhs": xhs_stats,
                "douyin_submit_fail": dy_submit_fail_stats,
            },
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        raise SystemExit(0 if output["ok"] else 1)
    finally:
        home_asr.run_u2_asr_candidates_with_timeout_retry = _ORIG_U2_SINGLE
        home_asr.run_u2_asr_batch_with_timeout_retry = _ORIG_U2_BATCH


if __name__ == "__main__":
    main()
