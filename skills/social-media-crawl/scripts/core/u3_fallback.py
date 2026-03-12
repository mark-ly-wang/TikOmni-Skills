#!/usr/bin/env python3
"""U3 public URL fallback helpers."""

from __future__ import annotations

import mimetypes
import os
import socket
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.core.tikomni_common import (
    DEFAULT_USER_AGENT,
    call_json_api,
    normalize_text,
    resolve_timeout_retry_policy,
)

DEFAULT_U3_PROVIDER = "oss"
DEFAULT_CONTENT_TYPE = "video/mp4"
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
TIMEOUT_LIKE_HTTP_STATUS_CODES = {408, 429, 502, 503, 504}


def _safe_name_from_url(source_url: str) -> str:
    parsed = urllib.parse.urlparse(source_url)
    name = Path(parsed.path).name.strip()
    return name or "media.bin"


def _guess_content_type(file_name: str, header_value: Optional[str]) -> str:
    header_text = normalize_text(header_value)
    if header_text:
        return header_text.split(";", 1)[0].strip() or DEFAULT_CONTENT_TYPE
    guessed, _ = mimetypes.guess_type(file_name)
    return guessed or DEFAULT_CONTENT_TYPE


def download_media_to_tempfile(
    *,
    source_url: str,
    timeout_ms: int,
) -> Dict[str, Any]:
    parsed = urllib.parse.urlparse(source_url)
    host = parsed.netloc.lower()
    headers = {
        "User-Agent": os.getenv("TIKOMNI_HTTP_USER_AGENT", DEFAULT_USER_AGENT),
        "Accept": "*/*",
    }
    if "xhscdn.com" in host:
        headers.update(
            {
                "Referer": "https://www.xiaohongshu.com/",
                "Origin": "https://www.xiaohongshu.com",
                "Range": "bytes=0-",
            }
        )
    request = urllib.request.Request(
        source_url,
        headers=headers,
        method="GET",
    )

    temp_path = ""
    file_size = 0
    request_id = None
    try:
        with urllib.request.urlopen(request, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
            final_url = response.geturl() or source_url
            content_type = response.headers.get("Content-Type")
            file_name = _safe_name_from_url(final_url)
            suffix = Path(file_name).suffix or ".bin"
            with tempfile.NamedTemporaryFile(prefix="tikomni-u3-", suffix=suffix, delete=False) as handle:
                temp_path = handle.name
                while True:
                    chunk = response.read(DOWNLOAD_CHUNK_SIZE)
                    if not chunk:
                        break
                    handle.write(chunk)
                    file_size += len(chunk)

            return {
                "ok": file_size > 0,
                "file_path": temp_path,
                "size_bytes": file_size,
                "file_name": file_name,
                "content_type": _guess_content_type(file_name, content_type),
                "final_url": final_url,
                "request_id": request_id,
                "error_reason": None if file_size > 0 else "u3_download_empty",
            }
    except urllib.error.HTTPError as error:
        return {
            "ok": False,
            "file_path": temp_path,
            "size_bytes": file_size,
            "file_name": _safe_name_from_url(source_url),
            "content_type": DEFAULT_CONTENT_TYPE,
            "final_url": source_url,
            "request_id": request_id,
            "error_reason": f"u3_download_http_{error.code}",
        }
    except Exception as error:
        return {
            "ok": False,
            "file_path": temp_path,
            "size_bytes": file_size,
            "file_name": _safe_name_from_url(source_url),
            "content_type": DEFAULT_CONTENT_TYPE,
            "final_url": source_url,
            "request_id": request_id,
            "error_reason": f"u3_download_failed:{normalize_text(error)}",
        }


def create_u3_upload(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    file_name: str,
    content_type: str,
    size_bytes: int,
    provider: str = DEFAULT_U3_PROVIDER,
) -> Dict[str, Any]:
    return call_json_api(
        base_url=base_url,
        path="/api/u3/v1/uploads",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={
            "provider": provider,
            "file_name": file_name,
            "content_type": content_type,
            "size_bytes": int(size_bytes),
        },
    )


def _is_timeout_like_upload_error(status_code: Optional[int], error_reason: Optional[str]) -> bool:
    if isinstance(status_code, (int, float)) and int(status_code) in TIMEOUT_LIKE_HTTP_STATUS_CODES:
        return True

    reason = str(error_reason or "").strip().lower()
    if not reason:
        return False
    return any(token in reason for token in ("timeout", "timed out", "deadline exceeded"))


def upload_file_to_presigned_url(
    *,
    upload_url: str,
    upload_headers: Optional[Dict[str, Any]],
    upload_method: str,
    file_path: str,
    content_type: str,
    timeout_ms: int,
) -> Dict[str, Any]:
    try:
        with open(file_path, "rb") as handle:
            data = handle.read()
    except Exception as error:
        return {
            "ok": False,
            "status_code": None,
            "error_reason": f"u3_upload_failed:{normalize_text(error)}",
            "retry_attempt": 0,
            "timeout_retry_max": 0,
            "timeout_retry_exhausted": False,
            "retry_chain": [],
        }

    headers = {
        "Content-Type": content_type or DEFAULT_CONTENT_TYPE,
        "User-Agent": os.getenv("TIKOMNI_HTTP_USER_AGENT", DEFAULT_USER_AGENT),
    }
    if isinstance(upload_headers, dict):
        for key, value in upload_headers.items():
            header_key = str(key).strip()
            if not header_key:
                continue
            headers[header_key] = str(value)

    retry_policy = resolve_timeout_retry_policy()
    timeout_retry_max = int(retry_policy.get("max_retries", 0) or 0)
    retry_backoff_ms = int(retry_policy.get("backoff_ms", 0) or 0)
    max_attempts = 1 + timeout_retry_max
    retry_chain: List[Dict[str, Any]] = []
    last_result: Dict[str, Any] = {
        "ok": False,
        "status_code": None,
        "error_reason": "u3_upload_failed:unknown",
    }

    for attempt in range(1, max_attempts + 1):
        if attempt > 1 and retry_backoff_ms > 0:
            sleep_ms = retry_backoff_ms * (2 ** (attempt - 2))
            time.sleep(sleep_ms / 1000.0)

        try:
            request = urllib.request.Request(
                upload_url,
                data=data,
                headers=headers,
                method=(upload_method or "PUT").upper(),
            )
            with urllib.request.urlopen(request, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                status_code = response.getcode()
                result: Dict[str, Any] = {
                    "ok": 200 <= int(status_code) < 300,
                    "status_code": status_code,
                    "error_reason": None if 200 <= int(status_code) < 300 else f"u3_upload_http_{status_code}",
                }
        except urllib.error.HTTPError as error:
            result = {
                "ok": False,
                "status_code": error.code,
                "error_reason": f"u3_upload_http_{error.code}",
            }
        except urllib.error.URLError as error:
            reason_obj = getattr(error, "reason", error)
            reason_text = normalize_text(reason_obj)
            result = {
                "ok": False,
                "status_code": None,
                "error_reason": f"u3_upload_failed:{reason_text or 'network_error'}",
                "_timeout_like": isinstance(reason_obj, socket.timeout)
                or _is_timeout_like_upload_error(status_code=None, error_reason=reason_text),
            }
        except (TimeoutError, socket.timeout) as error:
            result = {
                "ok": False,
                "status_code": None,
                "error_reason": f"u3_upload_failed:{normalize_text(error) or 'timeout'}",
                "_timeout_like": True,
            }
        except Exception as error:
            reason_text = normalize_text(error)
            result = {
                "ok": False,
                "status_code": None,
                "error_reason": f"u3_upload_failed:{reason_text or 'unknown'}",
                "_timeout_like": _is_timeout_like_upload_error(status_code=None, error_reason=reason_text),
            }

        if result.get("ok"):
            result["retry_attempt"] = max(0, attempt - 1)
            result["timeout_retry_max"] = timeout_retry_max
            result["timeout_retry_exhausted"] = False
            result["retry_chain"] = retry_chain
            return result

        timeout_like = bool(
            result.pop(
                "_timeout_like",
                _is_timeout_like_upload_error(
                    status_code=result.get("status_code"),
                    error_reason=result.get("error_reason"),
                ),
            )
        )
        retry_chain.append(
            {
                "attempt": attempt,
                "status_code": result.get("status_code"),
                "error_reason": result.get("error_reason"),
                "timeout_like": timeout_like,
            }
        )
        last_result = dict(result)

        if timeout_like and attempt < max_attempts:
            continue

        last_result["retry_attempt"] = max(0, attempt - 1)
        last_result["timeout_retry_max"] = timeout_retry_max
        last_result["timeout_retry_exhausted"] = bool(timeout_like and attempt >= max_attempts)
        last_result["retry_chain"] = retry_chain
        return last_result

    last_result["retry_attempt"] = timeout_retry_max
    last_result["timeout_retry_max"] = timeout_retry_max
    last_result["timeout_retry_exhausted"] = True
    last_result["retry_chain"] = retry_chain
    return last_result


def complete_u3_upload(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    upload_id: str,
) -> Dict[str, Any]:
    return call_json_api(
        base_url=base_url,
        path=f"/api/u3/v1/uploads/{upload_id}/complete",
        token=token,
        method="POST",
        timeout_ms=timeout_ms,
        body={},
    )


def cleanup_temp_file(file_path: Optional[str]) -> None:
    if not file_path:
        return
    try:
        Path(file_path).unlink(missing_ok=True)
    except Exception:
        pass


def run_u3_public_url_fallback(
    *,
    base_url: str,
    token: str,
    timeout_ms: int,
    source_url: str,
    provider: str = DEFAULT_U3_PROVIDER,
) -> Dict[str, Any]:
    download_bundle = download_media_to_tempfile(source_url=source_url, timeout_ms=timeout_ms)
    trace = [
        {
            "step": "u3_download_source",
            "ok": bool(download_bundle.get("ok")),
            "error_reason": download_bundle.get("error_reason"),
            "size_bytes": download_bundle.get("size_bytes"),
            "content_type": download_bundle.get("content_type"),
            "file_name": download_bundle.get("file_name"),
        }
    ]
    if not download_bundle.get("ok"):
        cleanup_temp_file(download_bundle.get("file_path"))
        return {
            "ok": False,
            "error_reason": download_bundle.get("error_reason") or "u3_download_failed",
            "public_url": "",
            "trace": trace,
            "request_id": download_bundle.get("request_id"),
        }

    create_response = create_u3_upload(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        provider=provider,
        file_name=str(download_bundle.get("file_name") or "media.bin"),
        content_type=str(download_bundle.get("content_type") or DEFAULT_CONTENT_TYPE),
        size_bytes=int(download_bundle.get("size_bytes") or 0),
    )
    create_body = create_response.get("data") if isinstance(create_response.get("data"), dict) else {}
    create_payload = create_body.get("data") if isinstance(create_body.get("data"), dict) else {}
    upload_id = normalize_text(create_payload.get("upload_id"))
    upload_url = normalize_text(create_payload.get("upload_url"))
    upload_method = normalize_text(create_payload.get("upload_method")) or "PUT"
    upload_headers = create_payload.get("upload_headers") if isinstance(create_payload.get("upload_headers"), dict) else {}
    trace.append(
        {
            "step": "u3_create_upload",
            "ok": bool(create_response.get("ok") and upload_id and upload_url),
            "request_id": create_response.get("request_id"),
            "status_code": create_response.get("status_code"),
            "error_reason": create_response.get("error_reason"),
            "upload_id": upload_id,
            "provider": create_payload.get("provider"),
            "upload_method": upload_method,
        }
    )
    if not create_response.get("ok") or not upload_id or not upload_url:
        cleanup_temp_file(download_bundle.get("file_path"))
        return {
            "ok": False,
            "error_reason": create_response.get("error_reason") or "u3_create_upload_failed",
            "public_url": "",
            "trace": trace,
            "request_id": create_response.get("request_id"),
        }

    upload_response = upload_file_to_presigned_url(
        upload_url=upload_url,
        upload_headers=upload_headers,
        upload_method=upload_method,
        file_path=str(download_bundle.get("file_path") or ""),
        content_type=str(download_bundle.get("content_type") or DEFAULT_CONTENT_TYPE),
        timeout_ms=timeout_ms,
    )
    trace.append(
        {
            "step": "u3_upload_object",
            "ok": bool(upload_response.get("ok")),
            "status_code": upload_response.get("status_code"),
            "error_reason": upload_response.get("error_reason"),
            "retry_attempt": upload_response.get("retry_attempt", 0),
            "retry_count": len(upload_response.get("retry_chain") or []),
            "timeout_retry_max": upload_response.get("timeout_retry_max", 0),
            "timeout_retry_exhausted": bool(upload_response.get("timeout_retry_exhausted")),
            "retry_chain": upload_response.get("retry_chain") or [],
        }
    )
    if not upload_response.get("ok"):
        cleanup_temp_file(download_bundle.get("file_path"))
        return {
            "ok": False,
            "error_reason": upload_response.get("error_reason") or "u3_upload_failed",
            "public_url": "",
            "trace": trace,
            "request_id": create_response.get("request_id"),
        }

    complete_response = complete_u3_upload(
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        upload_id=upload_id,
    )
    complete_body = complete_response.get("data") if isinstance(complete_response.get("data"), dict) else {}
    complete_payload = complete_body.get("data") if isinstance(complete_body.get("data"), dict) else {}
    public_url = normalize_text(complete_payload.get("file_url"))
    trace.append(
        {
            "step": "u3_complete_upload",
            "ok": bool(complete_response.get("ok") and public_url),
            "request_id": complete_response.get("request_id"),
            "status_code": complete_response.get("status_code"),
            "error_reason": complete_response.get("error_reason"),
            "upload_id": upload_id,
            "public_url_present": bool(public_url),
        }
    )
    cleanup_temp_file(download_bundle.get("file_path"))
    return {
        "ok": bool(complete_response.get("ok") and public_url),
        "error_reason": None if complete_response.get("ok") and public_url else (complete_response.get("error_reason") or "u3_complete_failed"),
        "public_url": public_url,
        "upload_id": upload_id,
        "provider": complete_payload.get("provider") or provider,
        "request_id": complete_response.get("request_id") or create_response.get("request_id"),
        "trace": trace,
    }
