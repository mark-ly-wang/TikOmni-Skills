#!/usr/bin/env python3
"""Host adapters for single-work structured analysis."""

from __future__ import annotations

import json
import os
import re
import signal
import shutil
import subprocess
import tempfile
import time
from typing import Any, Dict, List, Optional, Tuple

from scripts.core.progress_report import ProgressReporter


SUPPORTED_PROVIDERS = {"auto", "openclaw", "claude_code", "codex", "local"}
DEFAULT_PROVIDER_ORDER = ["openclaw", "claude_code", "codex"]


def normalize_provider(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_")
    return text if text in SUPPORTED_PROVIDERS else "auto"


def resolve_preferred_provider(config: Optional[Dict[str, Any]] = None) -> str:
    env_value = os.getenv("TIKOMNI_ANALYSIS_PROVIDER", "").strip()
    configured = ""
    if isinstance(config, dict):
        configured = str(config.get("provider") or "").strip()
    return normalize_provider(configured or env_value or "auto")


def resolve_analysis_timeout(config: Optional[Dict[str, Any]] = None, default: int = 30) -> int:
    env_value = os.getenv("TIKOMNI_ANALYSIS_TIMEOUT_SEC", "").strip()
    raw_value = env_value
    if isinstance(config, dict) and str(config.get("timeout_sec") or "").strip():
        raw_value = str(config.get("timeout_sec")).strip()
    try:
        parsed = int(raw_value or default)
    except Exception:
        parsed = default
    return max(5, min(parsed, 90))


def is_provider_available(provider: str) -> bool:
    normalized = normalize_provider(provider)
    if normalized == "openclaw":
        return bool(shutil.which("openclaw"))
    if normalized == "claude_code":
        return bool(shutil.which("claude"))
    if normalized == "codex":
        return bool(shutil.which("codex"))
    if normalized == "local":
        return True
    return False


def choose_provider(preferred: str) -> Tuple[str, List[str]]:
    normalized = normalize_provider(preferred)
    if normalized == "local":
        return "local", []
    if normalized != "auto":
        return normalized, [normalized]

    available = [provider for provider in DEFAULT_PROVIDER_ORDER if is_provider_available(provider)]
    if available:
        return available[0], available
    return "local", []


def _extract_json_object(text: str) -> Dict[str, Any]:
    candidate = str(text or "").strip()
    if not candidate:
        return {}

    fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", candidate, flags=re.S)
    if fenced:
        candidate = fenced.group(1).strip()

    try:
        parsed = json.loads(candidate)
        return parsed if isinstance(parsed, dict) else {}
    except Exception:
        pass

    start = candidate.find("{")
    end = candidate.rfind("}")
    if start >= 0 and end > start:
        try:
            parsed = json.loads(candidate[start : end + 1])
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}


def _extract_openclaw_text(stdout: str) -> str:
    payload = _extract_json_object(stdout)
    texts: List[str] = []
    result = payload.get("result")
    payloads = result.get("payloads", []) if isinstance(result, dict) else []
    for item in payloads:
        if not isinstance(item, dict):
            continue
        text = str(item.get("text") or "").strip()
        if text:
            texts.append(text)
    return "\n".join(texts).strip()


def _run_command(
    *,
    cmd: List[str],
    provider: str,
    operation: str,
    timeout_sec: int,
    progress: Optional[ProgressReporter],
    output_file: Optional[str] = None,
) -> Dict[str, Any]:
    started_at = time.perf_counter()
    if progress is not None:
        progress.subprocess_event(
            stage="analysis.host",
            provider=provider,
            operation=operation,
            event="started",
        )

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            start_new_session=True,
        )
    except Exception as error:
        duration_ms = int((time.perf_counter() - started_at) * 1000)
        if progress is not None:
            progress.subprocess_event(
                stage="analysis.host",
                provider=provider,
                operation=operation,
                event="failed",
                duration_ms=duration_ms,
                summary={"error_reason": f"spawn_failed:{error}"},
            )
        return {
            "ok": False,
            "provider": provider,
            "duration_ms": duration_ms,
            "exit_code": None,
            "stdout": "",
            "stderr": "",
            "error_reason": f"spawn_failed:{error}",
        }

    heartbeat_sec = 5.0
    stdout = ""
    stderr = ""
    exit_code: Optional[int] = None
    error_reason = ""

    while True:
        elapsed = time.perf_counter() - started_at
        remaining = float(timeout_sec) - elapsed
        if remaining <= 0:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except Exception:
                try:
                    process.kill()
                except Exception:
                    pass
            stdout, stderr = process.communicate()
            exit_code = process.returncode
            error_reason = "analysis_timeout"
            break
        try:
            stdout, stderr = process.communicate(timeout=min(heartbeat_sec, remaining))
            exit_code = process.returncode
            break
        except subprocess.TimeoutExpired:
            if progress is not None:
                progress.heartbeat(
                    stage="analysis.host",
                    message="analysis subprocess still running",
                    data={
                        "provider": provider,
                        "operation": operation,
                        "elapsed_ms": int((time.perf_counter() - started_at) * 1000),
                    },
                )

    duration_ms = int((time.perf_counter() - started_at) * 1000)
    if not error_reason and int(exit_code or 0) != 0:
        error_reason = f"subprocess_exit_{exit_code}"

    if output_file and os.path.isfile(output_file):
        try:
            stdout = open(output_file, "r", encoding="utf-8").read()
        except Exception:
            pass

    if progress is not None:
        progress.subprocess_event(
            stage="analysis.host",
            provider=provider,
            operation=operation,
            event="done" if not error_reason else "failed",
            duration_ms=duration_ms,
            exit_code=exit_code,
            summary={
                "error_reason": error_reason or None,
                "stdout_len": len(stdout or ""),
                "stderr_len": len(stderr or ""),
            },
        )

    return {
        "ok": not bool(error_reason),
        "provider": provider,
        "duration_ms": duration_ms,
        "exit_code": exit_code,
        "stdout": stdout,
        "stderr": stderr,
        "error_reason": error_reason or None,
    }


def _build_message(prompt_text: str, payload: Dict[str, Any]) -> str:
    return (
        "请严格执行下面的提示词契约，输出唯一 JSON 对象，不要输出 markdown 代码块，不要输出解释。\n\n"
        "=== 提示词契约 ===\n"
        f"{prompt_text}\n\n"
        "=== 输入数据(JSON) ===\n"
        f"{json.dumps(payload, ensure_ascii=False)}"
    )


def _run_openclaw(
    *,
    prompt_text: str,
    payload: Dict[str, Any],
    timeout_sec: int,
    progress: Optional[ProgressReporter],
) -> Dict[str, Any]:
    result = _run_command(
        cmd=[
            "openclaw",
            "agent",
            "--agent",
            "main",
            "--message",
            _build_message(prompt_text, payload),
            "--json",
        ],
        provider="openclaw",
        operation="structured_analysis",
        timeout_sec=timeout_sec,
        progress=progress,
    )
    result["raw_text"] = _extract_openclaw_text(result.get("stdout", ""))
    return result


def _run_codex(
    *,
    prompt_text: str,
    payload: Dict[str, Any],
    timeout_sec: int,
    progress: Optional[ProgressReporter],
) -> Dict[str, Any]:
    output_file = tempfile.NamedTemporaryFile(prefix="single-work-analysis-", suffix=".txt", delete=False)
    output_path = output_file.name
    output_file.close()
    try:
        result = _run_command(
            cmd=[
                "codex",
                "exec",
                "--skip-git-repo-check",
                "-o",
                output_path,
                _build_message(prompt_text, payload),
            ],
            provider="codex",
            operation="structured_analysis",
            timeout_sec=timeout_sec,
            progress=progress,
            output_file=output_path,
        )
        result["raw_text"] = str(result.get("stdout") or "").strip()
        return result
    finally:
        try:
            os.unlink(output_path)
        except Exception:
            pass


def _run_claude_code(
    *,
    prompt_text: str,
    payload: Dict[str, Any],
    timeout_sec: int,
    progress: Optional[ProgressReporter],
) -> Dict[str, Any]:
    result = _run_command(
        cmd=["claude", "-p", _build_message(prompt_text, payload)],
        provider="claude_code",
        operation="structured_analysis",
        timeout_sec=timeout_sec,
        progress=progress,
    )
    result["raw_text"] = str(result.get("stdout") or "").strip()
    return result


def run_structured_analysis(
    *,
    prompt_text: str,
    payload: Dict[str, Any],
    provider: str,
    timeout_sec: int,
    progress: Optional[ProgressReporter] = None,
) -> Dict[str, Any]:
    preferred = normalize_provider(provider)
    chosen_provider, attempted_providers = choose_provider(preferred)
    if chosen_provider == "local":
        return {
            "ok": False,
            "provider": "local",
            "duration_ms": 0,
            "attempted_providers": attempted_providers,
            "error_reason": "analysis_provider_unavailable",
            "structured": {},
        }

    if not is_provider_available(chosen_provider):
        return {
            "ok": False,
            "provider": chosen_provider,
            "duration_ms": 0,
            "attempted_providers": attempted_providers or [chosen_provider],
            "error_reason": "analysis_provider_unavailable",
            "structured": {},
        }

    if chosen_provider == "openclaw":
        result = _run_openclaw(
            prompt_text=prompt_text,
            payload=payload,
            timeout_sec=timeout_sec,
            progress=progress,
        )
    elif chosen_provider == "codex":
        result = _run_codex(
            prompt_text=prompt_text,
            payload=payload,
            timeout_sec=timeout_sec,
            progress=progress,
        )
    else:
        result = _run_claude_code(
            prompt_text=prompt_text,
            payload=payload,
            timeout_sec=timeout_sec,
            progress=progress,
        )

    raw_text = str(result.get("raw_text") or "")
    structured = _extract_json_object(raw_text)
    return {
        "ok": bool(result.get("ok")) and bool(structured),
        "provider": chosen_provider,
        "duration_ms": int(result.get("duration_ms") or 0),
        "attempted_providers": attempted_providers or [chosen_provider],
        "error_reason": result.get("error_reason") or (None if structured else "analysis_parse_failed"),
        "structured": structured if isinstance(structured, dict) else {},
    }
