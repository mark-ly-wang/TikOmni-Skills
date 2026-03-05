#!/usr/bin/env python3
"""Lightweight structural smoke checks for TikOmni scripts."""

from __future__ import annotations

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run_help(command: List[str]) -> Dict[str, Any]:
    proc = subprocess.run(command, capture_output=True, text=True)
    stdout = (proc.stdout or "")
    stderr = (proc.stderr or "")
    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout_head": "\n".join(stdout.splitlines()[:4]),
        "stderr_head": "\n".join(stderr.splitlines()[:4]),
    }


def _check_import(module_name: str) -> Dict[str, Any]:
    try:
        importlib.import_module(module_name)
        return {"ok": True}
    except Exception as error:  # pragma: no cover - smoke diagnostics only
        return {"ok": False, "error": f"{type(error).__name__}: {error}"}


def _check_card_frontmatter_generic_keys() -> Dict[str, Any]:
    try:
        from scripts.writers.write_benchmark_card import _extract_required_fields, _render_markdown

        payload = {
            "title": "测试标题",
            "author": {"nickname": "测试作者"},
            "share_url": "https://example.com/share",
            "xhs_user_id": "xhs_uid_123",
            "xhs_sec_token": "xhs_sec_123",
            "douyin_sec_uid": "dy_sec_123",
            "douyin_aweme_author_id": "dy_author_123",
        }
        fields = _extract_required_fields(payload, platform="xiaohongshu")
        markdown = _render_markdown(
            card_id="smoke-card",
            card_type="work",
            fields=fields,
            generated_at="2026-03-05T00:00:00",
        )

        frontmatter = ""
        parts = markdown.split("---")
        if len(parts) >= 3:
            frontmatter = parts[1]

        hidden_keys = [
            "xhs_user_id",
            "xhs_sec_token",
            "douyin_sec_uid",
            "douyin_aweme_author_id",
        ]
        leaked_keys = [key for key in hidden_keys if f"\n{key}:" in f"\n{frontmatter}"]
        payload_keys_kept = [key for key in hidden_keys if bool(fields.get(key))]

        ok = (not leaked_keys) and (len(payload_keys_kept) == len(hidden_keys))
        return {
            "ok": ok,
            "leaked_frontmatter_keys": leaked_keys,
            "required_fields_keys_kept": payload_keys_kept,
        }
    except Exception as error:
        return {"ok": False, "error": f"{type(error).__name__}: {error}"}


def _check_xhs_create_time_sec_parsing() -> Dict[str, Any]:
    try:
        from scripts.platform.xiaohongshu.run_xiaohongshu_extract import _extract_xhs_metadata

        cases = [
            ({"create_time_sec": 1700000000}, 1700000000, "root_sec"),
            ({"create_time": 1700000000123}, 1700000000, "root_ms"),
            ({"note": {"time": "1700000001"}}, 1700000001, "note_time_str"),
            ({"note_list": [{"publish_time": 1700000000456}]}, 1700000000, "note_list_publish_ms"),
        ]

        case_results: List[Dict[str, Any]] = []
        all_ok = True
        for payload, expected, label in cases:
            metadata = _extract_xhs_metadata(
                payload=payload,
                source_input={"share_text": None, "note_id": None},
                selected_video_url=None,
                selected_image_urls=[],
            )
            actual = metadata.get("create_time_sec")
            ok = actual == expected
            all_ok = all_ok and ok
            case_results.append({"label": label, "expected": expected, "actual": actual, "ok": ok})

        return {"ok": all_ok, "cases": case_results}
    except Exception as error:
        return {"ok": False, "error": f"{type(error).__name__}: {error}"}


def _check_publish_time_text_render() -> Dict[str, Any]:
    try:
        from scripts.writers.write_benchmark_card import _extract_required_fields

        fields = _extract_required_fields(
            {
                "title": "publish_time test",
                "create_time_sec": 1700000000,
                "publish_time": 1700000000,
            },
            platform="douyin",
        )
        text = str(fields.get("publish_time_text") or "")
        source = str(fields.get("publish_time_source") or "")
        ok = bool(text and text != "未知" and source)
        return {"ok": ok, "publish_time_text": text, "publish_time_source": source}
    except Exception as error:
        return {"ok": False, "error": f"{type(error).__name__}: {error}"}


def run_checks() -> Dict[str, Any]:
    root = _repo_root()
    py = sys.executable

    cli_targets = [
        {
            "name": "cli/run_tikomni_extract.py",
            "module": "scripts.cli.run_tikomni_extract",
            "path": root / "scripts" / "cli" / "run_tikomni_extract.py",
        },
        {
            "name": "platform/douyin/run_douyin_single_video.py",
            "module": "scripts.platform.douyin.run_douyin_single_video",
            "path": root / "scripts" / "platform" / "douyin" / "run_douyin_single_video.py",
        },
        {
            "name": "platform/xiaohongshu/run_xiaohongshu_extract.py",
            "module": "scripts.platform.xiaohongshu.run_xiaohongshu_extract",
            "path": root / "scripts" / "platform" / "xiaohongshu" / "run_xiaohongshu_extract.py",
        },
        {
            "name": "author_home/orchestrator/run_author_analysis.py",
            "module": "scripts.author_home.orchestrator.run_author_analysis",
            "path": root / "scripts" / "author_home" / "orchestrator" / "run_author_analysis.py",
        },
        {
            "name": "pipeline/asr/poll_u2_task.py",
            "module": "scripts.pipeline.asr.poll_u2_task",
            "path": root / "scripts" / "pipeline" / "asr" / "poll_u2_task.py",
        },
    ]

    checks: Dict[str, Any] = {}
    all_ok = True

    for target in cli_targets:
        import_result = _check_import(target["module"])
        module_help = _run_help([py, "-m", target["module"], "--help"])
        direct_help = _run_help([py, str(target["path"]), "--help"])
        target_ok = bool(import_result.get("ok") and module_help.get("ok") and direct_help.get("ok"))
        all_ok = all_ok and target_ok
        checks[target["name"]] = {
            "ok": target_ok,
            "import": import_result,
            "module_help": module_help,
            "direct_help": direct_help,
        }

    registry_import = _check_import("scripts.registry.workflow_registry")
    resolve_ok = False
    resolve_detail: Dict[str, Any] = {}
    if registry_import.get("ok"):
        from scripts.registry.workflow_registry import DEFAULT_WORKFLOW_REGISTRY

        douyin_handler, douyin_kind = DEFAULT_WORKFLOW_REGISTRY.resolve("douyin", "auto")
        xhs_handler, xhs_kind = DEFAULT_WORKFLOW_REGISTRY.resolve("xiaohongshu", "auto")
        douyin_home_handler, douyin_home_kind = DEFAULT_WORKFLOW_REGISTRY.resolve("douyin", "author_home")
        xhs_home_handler, xhs_home_kind = DEFAULT_WORKFLOW_REGISTRY.resolve("xiaohongshu", "author_home")
        resolve_ok = bool(
            douyin_handler and douyin_kind == "single_video" and xhs_handler and xhs_kind and douyin_home_handler and xhs_home_handler
        )
        resolve_detail = {
            "douyin_kind": douyin_kind,
            "xiaohongshu_kind": xhs_kind,
            "douyin_handler": bool(douyin_handler),
            "xiaohongshu_handler": bool(xhs_handler),
            "douyin_home_kind": douyin_home_kind,
            "xhs_home_kind": xhs_home_kind,
            "douyin_home_handler": bool(douyin_home_handler),
            "xhs_home_handler": bool(xhs_home_handler),
        }

    registry_ok = bool(registry_import.get("ok") and resolve_ok)
    all_ok = all_ok and registry_ok
    checks["registry/workflow_registry.py"] = {
        "ok": registry_ok,
        "import": registry_import,
        "resolve": {"ok": resolve_ok, **resolve_detail},
    }

    schema_import = _check_import("scripts.author_home.schema")
    semantic_ok = False
    semantic_detail: Dict[str, Any] = {}
    if schema_import.get("ok"):
        from scripts.author_home.schema import validate_author_profile, validate_work_item, validate_works_collection

        profile_errors = validate_author_profile(
            {
                "platform": "douyin",
                "platform_author_id": "",
                "nickname": "",
                "ip_location": "",
                "fans_count": 0,
                "liked_count": 0,
                "collected_count": 0,
                "signature": "",
                "avatar_url": "",
                "works_count": 0,
                "verified": False,
                "snapshot_at": "2026-03-05T00:00:00",
            }
        )
        work_errors = validate_work_item(
            {
                "platform": "douyin",
                "platform_work_id": "",
                "platform_author_id": "",
                "title": "",
                "desc": "",
                "publish_time": "",
                "content_type": "video",
                "duration_ms": 0,
                "tags": [],
                "metrics": {},
                "cover_image": "",
                "source_url": "",
                "share_url": "",
                "raw_ref": {},
            }
        )
        collection_errors = validate_works_collection([])

        has_profile_empty = any(
            isinstance(item, dict) and item.get("field") == "platform_author_id" and item.get("reason") == "empty_value" for item in profile_errors
        )
        has_work_empty = any(
            isinstance(item, dict) and item.get("field") == "platform_work_id" and item.get("reason") == "empty_value" for item in work_errors
        )
        has_empty_collection = any(
            isinstance(item, dict) and item.get("field") == "works" and item.get("reason") == "empty_collection" for item in collection_errors
        )
        semantic_ok = bool(has_profile_empty and has_work_empty and has_empty_collection)
        semantic_detail = {
            "profile_empty_value": has_profile_empty,
            "work_empty_value": has_work_empty,
            "works_empty_collection": has_empty_collection,
        }

    checks["author_home/schema.py"] = {
        "ok": bool(schema_import.get("ok") and semantic_ok),
        "import": schema_import,
        "semantic_validation": {"ok": semantic_ok, **semantic_detail},
    }
    all_ok = all_ok and bool(schema_import.get("ok") and semantic_ok)

    card_frontmatter_check = _check_card_frontmatter_generic_keys()
    checks["writers/write_benchmark_card.py::frontmatter_generic_keys"] = card_frontmatter_check
    all_ok = all_ok and bool(card_frontmatter_check.get("ok"))

    xhs_time_check = _check_xhs_create_time_sec_parsing()
    checks["platform/xiaohongshu/run_xiaohongshu_extract.py::create_time_sec"] = xhs_time_check
    all_ok = all_ok and bool(xhs_time_check.get("ok"))

    publish_time_render_check = _check_publish_time_text_render()
    checks["writers/write_benchmark_card.py::publish_time_text"] = publish_time_render_check
    all_ok = all_ok and bool(publish_time_render_check.get("ok"))

    return {"ok": all_ok, "checks": checks}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run structural smoke checks for TikOmni script entrypoints")
    parser.parse_args()

    result = run_checks()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
