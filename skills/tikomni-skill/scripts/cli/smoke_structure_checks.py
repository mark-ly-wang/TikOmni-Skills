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

    return {"ok": all_ok, "checks": checks}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run structural smoke checks for TikOmni script entrypoints")
    parser.parse_args()

    result = run_checks()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result.get("ok") else 1)


if __name__ == "__main__":
    main()
