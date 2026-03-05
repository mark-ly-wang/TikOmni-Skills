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


_ORIG_U2 = home_asr.run_u2_asr_candidates_with_timeout_retry


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


def _check(label: str, condition: bool, detail: dict) -> dict:
    return {
        "name": label,
        "ok": bool(condition),
        "detail": detail,
    }


def main() -> None:
    home_asr.run_u2_asr_candidates_with_timeout_retry = _fake_u2_runner
    try:
        douyin_bundle = home_asr.enrich_author_home_asr(
            platform="douyin",
            works=[
                {"platform_work_id": "dy-ok", "video_down_url": "https://video.success.mp4", "raw_ref": {}},
                {"platform_work_id": "dy-missing", "video_down_url": "", "raw_ref": {}},
                {"platform_work_id": "dy-bad", "video_down_url": "https://video.fail.mp4", "raw_ref": {}},
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
                    "platform_work_id": "xhs-subtitle",
                    "video_down_url": "https://video.fail.mp4",
                    "asr_raw": "这是可用字幕内容，字数明显超过二十个字符，能够直接用于分析。",
                    "raw_ref": {"subtitle_inline": ""},
                },
                {
                    "platform_work_id": "xhs-missing-subtitle",
                    "video_down_url": "https://video.success.mp4",
                    "asr_raw": "",
                    "raw_ref": {"subtitle_inline": "", "subtitle_urls": []},
                },
                {
                    "platform_work_id": "xhs-bad-subtitle",
                    "video_down_url": "",
                    "asr_raw": "00:00 --> 00:02",
                    "raw_ref": {"subtitle_inline": "00:00 --> 00:02", "subtitle_urls": []},
                },
            ],
            base_url="https://api.tikomni.com",
            token="mock",
            timeout_ms=1000,
            batch_size=2,
        )

        dy_map = {item.get("platform_work_id"): item for item in douyin_bundle.get("works", []) if isinstance(item, dict)}
        xhs_map = {item.get("platform_work_id"): item for item in xhs_bundle.get("works", []) if isinstance(item, dict)}

        checks = [
            _check("douyin_u2_success", dy_map.get("dy-ok", {}).get("asr_source") == "u2", dy_map.get("dy-ok", {})),
            _check("douyin_missing_video", dy_map.get("dy-missing", {}).get("asr_source") == "fallback_none", dy_map.get("dy-missing", {})),
            _check("douyin_bad_u2", dy_map.get("dy-bad", {}).get("asr_source") == "fallback_none", dy_map.get("dy-bad", {})),
            _check("xhs_subtitle_available", xhs_map.get("xhs-subtitle", {}).get("asr_source") == "xhs_subtitle", xhs_map.get("xhs-subtitle", {})),
            _check("xhs_subtitle_missing", xhs_map.get("xhs-missing-subtitle", {}).get("asr_source") == "u2", xhs_map.get("xhs-missing-subtitle", {})),
            _check("xhs_subtitle_bad", xhs_map.get("xhs-bad-subtitle", {}).get("asr_source") == "fallback_none", xhs_map.get("xhs-bad-subtitle", {})),
        ]

        output = {
            "ok": all(item.get("ok") for item in checks),
            "checks": checks,
            "stats": {
                "douyin": douyin_bundle.get("stats"),
                "xhs": xhs_bundle.get("stats"),
            },
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        raise SystemExit(0 if output["ok"] else 1)
    finally:
        home_asr.run_u2_asr_candidates_with_timeout_retry = _ORIG_U2


if __name__ == "__main__":
    main()
