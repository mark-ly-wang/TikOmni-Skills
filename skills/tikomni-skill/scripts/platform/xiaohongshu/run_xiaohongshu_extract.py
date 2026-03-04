#!/usr/bin/env python3

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    _self = Path(__file__).resolve()
    for _parent in _self.parents:
        if (_parent / "scripts" / "core" / "bootstrap_env.py").is_file():
            sys.path.insert(0, str(_parent))
            break

"""Xiaohongshu extraction: APP -> WEB_V2 -> WEB, subtitle-first for video, image strategy B for photo notes."""

from scripts.core.bootstrap_env import bootstrap_for_direct_run

bootstrap_for_direct_run(__file__, __package__)

import argparse
import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from scripts.pipeline.asr.asr_pipeline import run_u2_asr_candidates_with_timeout_retry
from scripts.core.config_loader import config_get, load_tikomni_config, resolve_storage_paths
from scripts.core.extract_pipeline import build_api_trace, resolve_trace_error_context
from scripts.core.tikomni_common import (
    call_json_api,
    deep_find_all,
    deep_find_first,
    normalize_text,
    resolve_runtime,
    summarize_content,
    write_json_stdout,
)
from scripts.writers.write_benchmark_card import write_benchmark_card

APP_ENDPOINT = "/api/u1/v1/xiaohongshu/app/get_note_info"
WEB_V2_V2_ENDPOINT = "/api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2"
WEB_V2_V3_ENDPOINT = "/api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3"
WEB_ENDPOINT = "/api/u1/v1/xiaohongshu/web/get_note_info_v7"


def _safe_slug(value: Optional[str], fallback: str = "unknown") -> str:
    text = normalize_text(value)
    if not text:
        return fallback
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", text).strip("-").lower()
    return slug[:64] or fallback


def _traceable_identifier(source_input: Dict[str, Optional[str]], note_id: Optional[str]) -> str:
    if note_id:
        return _safe_slug(note_id)
    share = normalize_text(source_input.get("share_text"))
    if not share:
        return "missing_input"
    digest = hashlib.sha1(share.encode("utf-8")).hexdigest()[:10]
    return f"url-{digest}"


def _build_persist_payload(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    status: str,
    written_at: datetime,
) -> Dict[str, Any]:
    summary = {
        "summary": result.get("summary", ""),
        "insights": result.get("insights", []),
        "confidence": result.get("confidence"),
        "error_reason": result.get("error_reason"),
    }
    normalized = {
        "platform": "xiaohongshu",
        "content_kind": result.get("content_kind", "note"),
        "note_id": result.get("note_id") or note_id,
        "note_content_type": result.get("note_content_type"),
        "text_source": result.get("text_source"),
        "request_id": result.get("request_id"),
        "source": source_input,
    }
    return {
        "meta": {
            "written_at": written_at.isoformat(timespec="seconds"),
            "status": status,
            "platform": "xiaohongshu",
            "identifier": _traceable_identifier(source_input, note_id),
        },
        "summary": summary,
        "normalized": normalized,
        "raw": result,
    }


def _persist_output_artifact(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    if not persist_output:
        return {"enabled": False, "skipped": True, "reason": "disabled_by_flag"}

    try:
        paths = resolve_storage_paths(storage_config or {})
    except Exception as error:
        return {"enabled": True, "ok": False, "error": f"resolve_storage_paths_failed:{error}"}

    now = datetime.now()
    date_key = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    identifier = _traceable_identifier(source_input, note_id)
    has_error = bool(result.get("error_reason"))
    status = "error" if has_error else "success"

    if has_error:
        target_dir = Path(paths.get("errors_dir", "")) / date_key
    else:
        target_dir = Path(paths.get("runs_dir", "")) / str(paths.get("results_dir", "results")) / date_key

    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / f"{timestamp}-xiaohongshu-{identifier}.json"

    payload = _build_persist_payload(
        result=result,
        source_input=source_input,
        note_id=note_id,
        status=status,
        written_at=now,
    )
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "enabled": True,
        "ok": True,
        "status": status,
        "path": str(file_path),
    }


def _finalize_result(
    *,
    result: Dict[str, Any],
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
    persist_output: bool,
) -> Dict[str, Any]:
    result["output_persist"] = _persist_output_artifact(
        result=result,
        source_input=source_input,
        note_id=note_id,
        storage_config=storage_config,
        persist_output=persist_output,
    )
    return result


def _normalize_input(input_value: Optional[str], share_text: Optional[str], note_id: Optional[str]) -> Dict[str, Optional[str]]:
    normalized_share = normalize_text(share_text) or None
    normalized_note_id = normalize_text(note_id) or None

    if input_value and not normalized_share and not normalized_note_id:
        candidate = input_value.strip()
        if candidate.startswith("http://") or candidate.startswith("https://"):
            normalized_share = candidate
        else:
            normalized_note_id = candidate

    return {
        "share_text": normalized_share,
        "note_id": normalized_note_id,
    }


def _extract_note_id_from_share(share_text: Optional[str]) -> Optional[str]:
    if not share_text:
        return None
    text = share_text.strip()
    patterns = [
        r"/explore/([0-9a-zA-Z]+)",
        r"/discovery/item/([0-9a-zA-Z]+)",
        r"note_id=([0-9a-zA-Z]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def _resolve_note_id(payload: Any, source_input: Dict[str, Optional[str]]) -> Optional[str]:
    # Priority 1: explicit source input
    if source_input.get("note_id"):
        return source_input.get("note_id")

    # Priority 2: canonical keys from payload
    for key in ["note_id", "noteid", "item_id", "itemId"]:
        value = deep_find_first(payload, [key])
        text = normalize_text(value)
        if text and len(text) >= 16:
            return text

    # Priority 3: parse from canonical webpage URLs
    for key in ["webpage_url", "share_url", "url"]:
        values = deep_find_all(payload, [key])
        for value in values:
            text = normalize_text(value)
            hit = _extract_note_id_from_share(text)
            if hit:
                return hit

    # Priority 4: parse from source share text
    hit = _extract_note_id_from_share(source_input.get("share_text"))
    if hit:
        return hit

    return None


def _is_short_share_url(share_text: Optional[str]) -> bool:
    if not share_text:
        return False
    try:
        host = urllib.parse.urlparse(share_text).netloc.lower()
    except Exception:
        return False
    return "xhslink.com" in host


def _app_response_has_core_fields(response_data: Any) -> bool:
    subtitle_hit = bool(_extract_subtitle_inline_text(response_data)) or bool(_extract_subtitle_urls(response_data))
    video_hit = bool(_extract_video_candidates(response_data))
    # For APP-first strategy, if app only has weak image frames but no subtitle/video core,
    # continue probing WEB_V2 to improve media fidelity.
    return subtitle_hit or video_hit


def _fetch_note_info(*, base_url: str, token: str, timeout_ms: int, source_input: Dict[str, Optional[str]]) -> Dict[str, Any]:
    attempts: List[Dict[str, Any]] = []

    share_text = source_input.get("share_text")
    note_id = source_input.get("note_id") or _extract_note_id_from_share(share_text)

    def _call(path: str, params: Dict[str, Any], label: str) -> Dict[str, Any]:
        response = call_json_api(
            base_url=base_url,
            path=path,
            token=token,
            method="GET",
            timeout_ms=timeout_ms,
            params=params,
        )
        response["_endpoint"] = path
        response["_route_label"] = label
        attempts.append({"label": label, "endpoint": path, "response": response})
        return response

    app_params: Dict[str, Any] = {}
    if share_text:
        app_params["share_text"] = share_text
    if note_id:
        app_params["note_id"] = note_id

    app_response = _call(APP_ENDPOINT, app_params, "app")
    if app_response.get("ok"):
        app_response["_attempts"] = attempts
        return app_response

    is_short = _is_short_share_url(share_text)

    if is_short and share_text:
        v3_response = _call(WEB_V2_V3_ENDPOINT, {"short_url": share_text}, "web_v2_v3_short")
        if v3_response.get("ok"):
            v3_response["_attempts"] = attempts
            return v3_response

    if note_id:
        v2_response = _call(WEB_V2_V2_ENDPOINT, {"note_id": note_id}, "web_v2_v2_note_id")
        if v2_response.get("ok"):
            v2_response["_attempts"] = attempts
            return v2_response

    web_params: Dict[str, Any] = {}
    if share_text:
        web_params["share_text"] = share_text
    if note_id:
        web_params["note_id"] = note_id

    web_response = _call(WEB_ENDPOINT, web_params, "web_v7")
    web_response["_attempts"] = attempts
    return web_response


def _extract_subtitle_urls(payload: Any) -> List[str]:
    urls: List[str] = []
    for key in ["subtitle_url", "subtitleUrl", "srt_url", "srtUrl", "vtt_url", "vttUrl"]:
        for value in deep_find_all(payload, [key]):
            if isinstance(value, str):
                text = value.strip()
                if text.startswith("http://") or text.startswith("https://"):
                    urls.append(text)

    unique: List[str] = []
    seen = set()
    for url in urls:
        if url not in seen:
            unique.append(url)
            seen.add(url)
    return unique


def _extract_subtitle_inline_text(payload: Any) -> str:
    lines: List[str] = []
    subtitle_containers = deep_find_all(payload, ["subtitles", "subtitle_list", "subtitleList"])

    for container in subtitle_containers:
        if isinstance(container, list):
            for item in container:
                if isinstance(item, dict):
                    for key in ["text", "content", "sentence", "line"]:
                        val = item.get(key)
                        if isinstance(val, str) and normalize_text(val):
                            lines.append(normalize_text(val))
                elif isinstance(item, str) and normalize_text(item):
                    lines.append(normalize_text(item))
        elif isinstance(container, dict):
            for key in ["text", "content"]:
                val = container.get(key)
                if isinstance(val, str) and normalize_text(val):
                    lines.append(normalize_text(val))

    deduped = list(dict.fromkeys(lines))
    return "\n".join(deduped).strip()


def _subtitle_text_from_raw(raw: str) -> str:
    if not raw:
        return ""

    raw = raw.strip()
    if not raw:
        return ""

    if raw.startswith("{") or raw.startswith("["):
        try:
            data = json.loads(raw)
            texts: List[str] = []
            if isinstance(data, dict):
                for key in ["segments", "subtitles", "data", "result", "body"]:
                    val = data.get(key)
                    if isinstance(val, list):
                        for item in val:
                            if isinstance(item, dict):
                                t = item.get("text") or item.get("content") or item.get("sentence")
                                if isinstance(t, str) and normalize_text(t):
                                    texts.append(normalize_text(t))
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        t = item.get("text") or item.get("content") or item.get("sentence")
                        if isinstance(t, str) and normalize_text(t):
                            texts.append(normalize_text(t))
            return "\n".join(dict.fromkeys(texts)).strip()
        except Exception:
            pass

    lines = []
    for line in raw.splitlines():
        t = line.strip()
        if not t:
            continue
        if t.upper() == "WEBVTT":
            continue
        if re.match(r"^\d+$", t):
            continue
        if "-->" in t:
            continue
        if t.startswith("NOTE"):
            continue
        cleaned = normalize_text(t)
        if cleaned:
            lines.append(cleaned)

    return "\n".join(dict.fromkeys(lines)).strip()


def _fetch_subtitle_text(urls: List[str], timeout_ms: int) -> str:
    for url in urls:
        try:
            req = urllib.request.Request(url=url, method="GET")
            with urllib.request.urlopen(req, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                raw = response.read().decode("utf-8", errors="replace")
            text = _subtitle_text_from_raw(raw)
            if text:
                return text
        except Exception:
            continue
    return ""


def _url_likely_image(url: str) -> bool:
    lower = url.lower()
    image_tokens = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        "_jpg_",
        "_png_",
        "imageview2",
        "imagemogr2",
        "redimage",
        "frame/",
        "sns-img",
        "sns-webpic",
        "notes_pre_post",
    ]
    return any(token in lower for token in image_tokens)


def _url_likely_video(url: str) -> bool:
    lower = url.lower()
    video_tokens = [
        ".mp4",
        ".m3u8",
        ".m4a",
        ".mp3",
        "video",
        "play",
        "stream",
        "master",
        "sns-video",
        "redvideo",
        "vod",
        "/audio/",
    ]
    if _url_likely_image(url):
        return False
    return any(token in lower for token in video_tokens)


def _video_quality_hint(url: str) -> int:
    lower = url.lower()
    score = 9999

    query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    for key in ("w", "width", "ratio", "quality", "qn"):
        values = query.get(key)
        if not values:
            continue
        value = str(values[0]).lower()
        m = re.search(r"(\d{3,4})", value)
        if m:
            score = min(score, int(m.group(1)))

    for token, value in (("240p", 240), ("360p", 360), ("480p", 480), ("540p", 540), ("576p", 576), ("720p", 720), ("1080p", 1080), ("2k", 2000), ("4k", 4000)):
        if token in lower:
            score = min(score, value)

    return score


def _extract_video_candidates(payload: Any) -> List[str]:
    candidates: List[str] = []
    key_priority = [
        "master_url",
        "masterUrl",
        "video_url",
        "play_url",
        "origin_video_key",
        "origin_video_url",
        "video_play_url",
        "audio_url",
        "note_sound_info",
        "url",
    ]

    for key in key_priority:
        values = deep_find_all(payload, [key])
        for value in values:
            if isinstance(value, str):
                v = value.strip()
                if v.startswith("http://") or v.startswith("https://"):
                    candidates.append(v)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        v = item.strip()
                        if v.startswith("http://") or v.startswith("https://"):
                            candidates.append(v)
            elif isinstance(value, dict):
                nested = value.get("url") or value.get("play_url")
                if isinstance(nested, str):
                    v = nested.strip()
                    if v.startswith("http://") or v.startswith("https://"):
                        candidates.append(v)

    unique: List[str] = []
    seen = set()
    for url in candidates:
        if url not in seen:
            unique.append(url)
            seen.add(url)

    video_only = [u for u in unique if _url_likely_video(u)]
    if not video_only:
        return []

    scored = sorted(video_only, key=lambda u: (_video_quality_hint(u), video_only.index(u)))
    return scored


def _collect_urls(value: Any) -> List[str]:
    out: List[str] = []
    if isinstance(value, str):
        v = value.strip()
        if v.startswith("http://") or v.startswith("https://"):
            out.append(v)
    elif isinstance(value, list):
        for item in value:
            out.extend(_collect_urls(item))
    elif isinstance(value, dict):
        for key in ("url", "urlDefault", "url_default", "urlPre", "url_pre", "original"):
            if key in value:
                out.extend(_collect_urls(value.get(key)))
    return out


def _dedupe_image_urls(urls: List[str]) -> List[str]:
    unique: List[str] = []
    seen = set()
    for url in urls:
        if url in seen:
            continue
        seen.add(url)
        if _url_likely_image(url):
            unique.append(url)
    return unique


def _extract_image_candidates_with_strategy(payload: Any) -> Tuple[List[str], str]:
    # Priority 1: original image set
    originals = _dedupe_image_urls(deep_find_all(payload, ["original"]))
    if originals:
        return originals, "original"

    # Priority 2: WEB_V2 infoList with WB_DFT scene
    dft_urls: List[str] = []
    for key in ("imageList", "images_list"):
        image_lists = deep_find_all(payload, [key])
        for image_list in image_lists:
            if not isinstance(image_list, list):
                continue
            for item in image_list:
                if not isinstance(item, dict):
                    continue
                info_list = item.get("infoList") or item.get("info_list")
                if isinstance(info_list, list):
                    for info in info_list:
                        if not isinstance(info, dict):
                            continue
                        scene = str(info.get("imageScene") or info.get("image_scene") or "").upper()
                        if scene == "WB_DFT":
                            dft_urls.extend(_collect_urls(info.get("url")))
    dft_urls = _dedupe_image_urls(dft_urls)
    if dft_urls:
        return dft_urls, "wb_dft"

    # Priority 3: default representative image URLs
    default_urls: List[str] = []
    for key in ("urlDefault", "url_default", "urlPre", "url_pre"):
        default_urls.extend(_collect_urls(deep_find_all(payload, [key])))
    default_urls = _dedupe_image_urls(default_urls)
    if default_urls:
        return default_urls, "default"

    # Priority 4: generic fallback (single quality group intended)
    generic: List[str] = []
    for key in ("url", "url_list", "origin_image", "origin_image_url", "cover", "thumb", "image_url"):
        generic.extend(_collect_urls(deep_find_all(payload, [key])))
    generic = _dedupe_image_urls(generic)
    return generic, "fallback"


def _extract_image_candidates(payload: Any) -> List[str]:
    urls, _ = _extract_image_candidates_with_strategy(payload)
    return urls


def _extract_note_type_field(payload: Any) -> str:
    # WEB_V2 schema: note.type
    for note_obj in deep_find_all(payload, ["note"]):
        if isinstance(note_obj, dict):
            note_type = normalize_text(note_obj.get("type")).lower()
            if note_type:
                return note_type

    # APP schema: note_list[].type
    for key in ("note_list", "noteList"):
        for note_list in deep_find_all(payload, [key]):
            if not isinstance(note_list, list):
                continue
            for item in note_list:
                if not isinstance(item, dict):
                    continue
                note_type = normalize_text(item.get("type")).lower()
                if note_type:
                    return note_type

    # Strict fallback: only accept expected scalar values.
    for value in deep_find_all(payload, ["type"]):
        note_type = normalize_text(value).lower()
        if note_type in {"video", "normal", "image"}:
            return note_type

    return ""


def _detect_note_content_type(payload: Any, video_candidates: List[str], image_candidates: List[str]) -> str:
    note_type_value = _extract_note_type_field(payload)
    if note_type_value == "video":
        return "video"
    if note_type_value == "normal":
        return "image"
    if "video" in note_type_value:
        return "video"
    if "image" in note_type_value:
        return "image"

    note_sound_url = normalize_text(deep_find_first(payload, ["note_sound_info", "url"])).lower()
    has_note_audio = bool(note_sound_url and any(token in note_sound_url for token in [".m4a", ".mp3", "/audio/"]))

    has_video = bool(video_candidates) or has_note_audio
    has_image = bool(image_candidates)
    if has_video and has_image:
        return "mixed"
    if has_video:
        return "video"
    if has_image:
        return "image"
    return "unknown"


def _guess_ext_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    for ext in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
        if path.endswith(ext):
            return ext
    return ".jpg"


def _download_images(
    *,
    urls: List[str],
    timeout_ms: int,
    source_input: Dict[str, Optional[str]],
    note_id: Optional[str],
    storage_config: Optional[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not urls:
        return []

    try:
        paths = resolve_storage_paths(storage_config or {})
        base_dir = Path(paths.get("runs_dir", "")) / "assets" / datetime.now().strftime("%Y%m%d") / _traceable_identifier(source_input, note_id)
    except Exception:
        base_dir = Path("./tikomni-output/_runs/assets") / datetime.now().strftime("%Y%m%d") / _traceable_identifier(source_input, note_id)

    base_dir.mkdir(parents=True, exist_ok=True)
    results: List[Dict[str, Any]] = []

    for idx, url in enumerate(urls[:30], start=1):
        ext = _guess_ext_from_url(url)
        path = base_dir / f"image-{idx:02d}{ext}"
        try:
            req = urllib.request.Request(url=url, method="GET")
            with urllib.request.urlopen(req, timeout=max(timeout_ms / 1000.0, 1.0)) as response:
                content = response.read()
            path.write_bytes(content)
            results.append({"index": idx, "url": url, "path": str(path), "ok": True})
        except Exception as error:
            results.append({"index": idx, "url": url, "path": str(path), "ok": False, "error": str(error)})

    return results


def _build_result(
    *,
    source_input: Dict[str, Optional[str]],
    raw_content: str,
    confidence: str,
    error_reason: Optional[str],
    extract_trace: List[Dict[str, Any]],
    fallback_trace: List[Dict[str, Any]],
    request_id: Optional[str],
    text_source: str,
    note_id: Optional[str],
    subtitle_hit: bool,
    u2_task_id: Optional[str],
    u2_task_status: Optional[str],
    note_content_type: str,
    analysis_mode: str,
    selected_video_url: Optional[str],
    selected_video_candidates: List[str],
    selected_image_urls: List[str],
    downloaded_assets: List[Dict[str, Any]],
    missing_fields: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    summary_block = summarize_content(raw_content, source=f"xiaohongshu:{text_source}")
    insights = list(summary_block.get("insights", []))
    insights.extend([
        f"note_content_type={note_content_type}",
        f"analysis_mode={analysis_mode}",
        f"selected_image_count={len(selected_image_urls)}",
    ])
    return {
        "platform": "xiaohongshu",
        "content_kind": "note",
        "source": source_input,
        "note_id": note_id,
        "note_content_type": note_content_type,
        "analysis_mode": analysis_mode,
        "subtitle_hit": subtitle_hit,
        "text_source": text_source,
        "u2_task_id": u2_task_id,
        "u2_task_status": u2_task_status,
        "selected_video_url": selected_video_url,
        "selected_video_candidates": selected_video_candidates,
        "selected_image_urls": selected_image_urls,
        "downloaded_assets": downloaded_assets,
        "raw_content": raw_content,
        "summary": summary_block["summary"],
        "insights": insights,
        "confidence": confidence,
        "error_reason": error_reason,
        "missing_fields": missing_fields or [],
        "extract_trace": extract_trace,
        "fallback_trace": fallback_trace,
        "request_id": request_id,
    }


def run_xiaohongshu_extract(
    *,
    input_value: Optional[str],
    share_text: Optional[str],
    note_id: Optional[str],
    env_file: Optional[str],
    api_key_env: str,
    base_url: Optional[str],
    timeout_ms: Optional[int],
    poll_interval_sec: float,
    max_polls: int,
    u2_submit_max_retries: int,
    u2_submit_backoff_ms: int,
    u2_timeout_retry_enabled: bool,
    u2_timeout_retry_max_retries: int,
    force_u2_fallback: bool,
    write_card: bool,
    card_type: str,
    collect_material: bool,
    card_root: Optional[str],
    storage_config: Optional[Dict[str, Any]] = None,
    allow_process_env: bool = False,
    persist_output: bool = True,
) -> Dict[str, Any]:
    source_input = _normalize_input(input_value, share_text, note_id)
    if not source_input["share_text"] and not source_input["note_id"]:
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason="missing_share_text_or_note_id",
            extract_trace=[],
            fallback_trace=[],
            request_id=None,
            text_source="none",
            note_id=None,
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            note_content_type="unknown",
            analysis_mode="none",
            selected_video_url=None,
            selected_video_candidates=[],
            selected_image_urls=[],
            downloaded_assets=[],
            missing_fields=[{"field": "share_text_or_note_id", "reason": "missing_input"}],
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind="note",
                storage_config=storage_config,
            )
        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=None,
            storage_config=storage_config,
            persist_output=persist_output,
        )

    runtime = resolve_runtime(
        env_file=env_file,
        api_key_env=api_key_env,
        base_url=base_url,
        timeout_ms=timeout_ms,
        allow_process_env=allow_process_env,
    )

    trace: List[Dict[str, Any]] = []

    note_response = _fetch_note_info(
        base_url=runtime["base_url"],
        token=runtime["token"],
        timeout_ms=runtime["timeout_ms"],
        source_input=source_input,
    )

    attempts = note_response.get("_attempts") or []
    for index, attempt in enumerate(attempts, start=1):
        response = attempt.get("response") if isinstance(attempt, dict) else None
        endpoint = attempt.get("endpoint") if isinstance(attempt, dict) else None
        label = attempt.get("label") if isinstance(attempt, dict) else None
        if not isinstance(response, dict):
            continue
        step = "u1_get_note_info_effective" if index == len(attempts) else f"u1_get_note_info_attempt_{index}"
        trace.append(
            build_api_trace(
                step=step,
                endpoint=endpoint,
                response=response,
                extra={"route_label": label, "attempt": index},
            )
        )

    if not note_response.get("ok"):
        error_ctx = resolve_trace_error_context(
            responses=[note_response],
            extract_trace=trace,
            default_error_reason="u1_get_note_info_failed",
        )
        result = _build_result(
            source_input=source_input,
            raw_content="",
            confidence="low",
            error_reason=error_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=error_ctx.get("fallback_trace", []),
            request_id=error_ctx.get("request_id"),
            text_source="none",
            note_id=source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=None,
            u2_task_status="UNKNOWN",
            note_content_type="unknown",
            analysis_mode="none",
            selected_video_url=None,
            selected_video_candidates=[],
            selected_image_urls=[],
            downloaded_assets=[],
            missing_fields=[{"field": "u1_note_info", "reason": "all_routes_failed"}],
        )
        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind="note",
                storage_config=storage_config,
            )
        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=source_input.get("note_id"),
            storage_config=storage_config,
            persist_output=persist_output,
        )

    resolved_note_id = _resolve_note_id(note_response.get("data"), source_input)

    title = normalize_text(deep_find_first(note_response.get("data"), ["title"]))
    desc = normalize_text(deep_find_first(note_response.get("data"), ["desc", "content"]))
    caption_text = "\n".join([t for t in [title, desc] if t]).strip()

    subtitle_inline_text = "" if force_u2_fallback else _extract_subtitle_inline_text(note_response.get("data"))
    subtitle_urls = [] if force_u2_fallback else _extract_subtitle_urls(note_response.get("data"))
    subtitle_url_text = "" if force_u2_fallback else _fetch_subtitle_text(subtitle_urls, runtime["timeout_ms"])
    subtitle_text = subtitle_inline_text or subtitle_url_text

    video_candidates = _extract_video_candidates(note_response.get("data"))
    image_candidates, image_quality_strategy = _extract_image_candidates_with_strategy(note_response.get("data"))
    selected_video_url = video_candidates[0] if video_candidates else None
    type_field_value = _extract_note_type_field(note_response.get("data"))
    note_content_type = _detect_note_content_type(note_response.get("data"), video_candidates, image_candidates)

    trace.append(
        {
            "step": "media_probe",
            "type_field_value": type_field_value,
            "note_content_type": note_content_type,
            "video_candidate_count": len(video_candidates),
            "image_candidate_count": len(image_candidates),
            "image_quality_strategy": image_quality_strategy,
            "subtitle_hit": bool(subtitle_text),
            "subtitle_url_count": len(subtitle_urls),
            "force_u2_fallback": force_u2_fallback,
        }
    )

    missing_fields: List[Dict[str, str]] = []

    # Video-note path: aligned with douyin single-video pipeline (subtitle-first difference retained).
    if note_content_type in {"video", "mixed"}:
        if subtitle_text:
            success_ctx = resolve_trace_error_context(
                responses=[note_response],
                extract_trace=trace,
                explicit_error_reason=None,
                explicit_request_id=note_response.get("request_id"),
            )
            result = _build_result(
                source_input=source_input,
                raw_content=subtitle_text,
                confidence="high",
                error_reason=None,
                extract_trace=trace,
                fallback_trace=success_ctx.get("fallback_trace", []),
                request_id=success_ctx.get("request_id"),
                text_source="subtitle",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=True,
                u2_task_id=None,
                u2_task_status="SKIPPED",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=selected_video_url,
                selected_video_candidates=video_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    collect_material=collect_material,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        if not selected_video_url:
            missing_fields.append({"field": "selected_video_url", "reason": "video_note_but_no_video_url"})
            error_ctx = resolve_trace_error_context(
                responses=[note_response],
                extract_trace=trace,
                default_error_reason="subtitle_missing_and_no_video_url_for_u2",
            )
            result = _build_result(
                source_input=source_input,
                raw_content="",
                confidence="low",
                error_reason=error_ctx.get("error_reason"),
                extract_trace=trace,
                fallback_trace=error_ctx.get("fallback_trace", []),
                request_id=error_ctx.get("request_id"),
                text_source="none",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=False,
                u2_task_id=None,
                u2_task_status="UNKNOWN",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=None,
                selected_video_candidates=video_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    collect_material=collect_material,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        u2_bundle = run_u2_asr_candidates_with_timeout_retry(
            base_url=runtime["base_url"],
            token=runtime["token"],
            timeout_ms=runtime["timeout_ms"],
            candidates=video_candidates,
            submit_max_retries=u2_submit_max_retries,
            submit_backoff_ms=u2_submit_backoff_ms,
            poll_interval_sec=poll_interval_sec,
            max_polls=max_polls,
            timeout_retry_enabled=u2_timeout_retry_enabled,
            timeout_retry_max_retries=u2_timeout_retry_max_retries,
        )
        submit_bundle = u2_bundle.get("submit_bundle", {})
        submit_response = submit_bundle.get("submit_response", {})
        task_id = submit_bundle.get("task_id")
        poll_result = u2_bundle.get("poll_result", {})
        selected_video_url = u2_bundle.get("chosen_candidate") or selected_video_url

        trace.append(
            {
                "step": "u2_asr_timeout_retry",
                "endpoint": "/api/u2/v1/services/audio/asr/transcription + /api/u2/v1/tasks/{task_id}",
                "selected_video_url": selected_video_url,
                "selected_video_candidates": video_candidates,
                "candidate_attempts": u2_bundle.get("candidate_attempts", []),
                "submit_retries_config": {
                    "u2_submit_max_retries": max(0, int(u2_submit_max_retries)),
                    "u2_submit_backoff_ms": max(0, int(u2_submit_backoff_ms)),
                },
                "timeout_retry": u2_bundle.get("timeout_retry", {}),
                "rounds": u2_bundle.get("rounds", []),
                "final_task_id": poll_result.get("task_id") or task_id,
                "final_task_status": poll_result.get("task_status"),
                "final_error_reason": poll_result.get("error_reason"),
            }
        )

        if not poll_result.get("ok") and (
            not submit_response.get("ok") or not (poll_result.get("task_id") or task_id)
        ):
            error_ctx = resolve_trace_error_context(
                responses=[poll_result, submit_response, note_response],
                extract_trace=trace,
                default_error_reason="u2_submit_failed_or_missing_task_id",
                explicit_request_id=(
                    poll_result.get("request_id")
                    or submit_response.get("request_id")
                    or note_response.get("request_id")
                ),
            )
            fallback_text = caption_text
            if fallback_text:
                missing_fields.append({"field": "asr_transcript", "reason": f"u2_failed:{error_ctx.get('error_reason')}"})
            else:
                missing_fields.append({"field": "raw_content", "reason": "u2_failed_and_caption_missing"})
            result = _build_result(
                source_input=source_input,
                raw_content=fallback_text,
                confidence="medium" if fallback_text else "low",
                error_reason=None if fallback_text else error_ctx.get("error_reason"),
                extract_trace=trace,
                fallback_trace=error_ctx.get("fallback_trace", []),
                request_id=error_ctx.get("request_id"),
                text_source="caption_fallback" if fallback_text else "u2",
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                subtitle_hit=False,
                u2_task_id=poll_result.get("task_id") or task_id,
                u2_task_status=poll_result.get("task_status") or "UNKNOWN",
                note_content_type=note_content_type,
                analysis_mode="video_full",
                selected_video_url=selected_video_url,
                selected_video_candidates=video_candidates,
                selected_image_urls=image_candidates,
                downloaded_assets=[],
                missing_fields=missing_fields,
            )
            if write_card:
                result["card_write"] = write_benchmark_card(
                    payload=result,
                    platform="xiaohongshu",
                    card_type=card_type,
                    card_root=card_root,
                    collect_material=collect_material,
                    content_kind="single_video",
                    storage_config=storage_config,
                )
            return _finalize_result(
                result=result,
                source_input=source_input,
                note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
                storage_config=storage_config,
                persist_output=persist_output,
            )

        raw_content = poll_result.get("transcript_text", "") if poll_result.get("ok") else ""
        final_ctx = resolve_trace_error_context(
            responses=[poll_result, submit_response, note_response],
            extract_trace=trace,
            explicit_error_reason=poll_result.get("error_reason"),
            explicit_request_id=poll_result.get("request_id") or submit_response.get("request_id") or note_response.get("request_id"),
        )
        result = _build_result(
            source_input=source_input,
            raw_content=raw_content,
            confidence="high" if poll_result.get("ok") and raw_content else "low",
            error_reason=final_ctx.get("error_reason"),
            extract_trace=trace,
            fallback_trace=final_ctx.get("fallback_trace", []),
            request_id=final_ctx.get("request_id"),
            text_source="u2",
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            subtitle_hit=False,
            u2_task_id=poll_result.get("task_id") or task_id,
            u2_task_status=poll_result.get("task_status"),
            note_content_type=note_content_type,
            analysis_mode="video_full",
            selected_video_url=selected_video_url,
            selected_video_candidates=video_candidates,
            selected_image_urls=image_candidates,
            downloaded_assets=[],
            missing_fields=missing_fields,
        )

        if write_card:
            result["card_write"] = write_benchmark_card(
                payload=result,
                platform="xiaohongshu",
                card_type=card_type,
                card_root=card_root,
                collect_material=collect_material,
                content_kind="single_video",
                storage_config=storage_config,
            )

        return _finalize_result(
            result=result,
            source_input=source_input,
            note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
            storage_config=storage_config,
            persist_output=persist_output,
        )

    # Image-note path, strategy B: download images + light text analysis + write card.
    raw_content = caption_text

    downloaded_assets = _download_images(
        urls=image_candidates,
        timeout_ms=runtime["timeout_ms"],
        source_input=source_input,
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        storage_config=storage_config,
    )

    if not image_candidates:
        missing_fields.append({"field": "selected_image_urls", "reason": "image_note_but_no_image_url"})
    if not raw_content:
        missing_fields.append({"field": "raw_content", "reason": "title_and_desc_missing"})

    success_ctx = resolve_trace_error_context(
        responses=[note_response],
        extract_trace=trace,
        explicit_error_reason=None,
        explicit_request_id=note_response.get("request_id"),
    )

    result = _build_result(
        source_input=source_input,
        raw_content=raw_content,
        confidence="high" if raw_content else "medium",
        error_reason=None,
        extract_trace=trace,
        fallback_trace=success_ctx.get("fallback_trace", []),
        request_id=success_ctx.get("request_id"),
        text_source="caption",
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        subtitle_hit=False,
        u2_task_id=None,
        u2_task_status="SKIPPED",
        note_content_type="image" if note_content_type == "unknown" else note_content_type,
        analysis_mode="image_light_analysis",
        selected_video_url=None,
        selected_video_candidates=video_candidates,
        selected_image_urls=image_candidates,
        downloaded_assets=downloaded_assets,
        missing_fields=missing_fields,
    )

    if write_card:
        result["card_write"] = write_benchmark_card(
            payload=result,
            platform="xiaohongshu",
            card_type=card_type,
            card_root=card_root,
            collect_material=collect_material,
            content_kind="note",
            storage_config=storage_config,
        )

    return _finalize_result(
        result=result,
        source_input=source_input,
        note_id=str(resolved_note_id) if resolved_note_id else source_input.get("note_id"),
        storage_config=storage_config,
        persist_output=persist_output,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run xiaohongshu extraction chain")
    parser.add_argument("input", nargs="?", default=None, help="Share URL or note_id")
    parser.add_argument("--share-text", default=None, help="Xiaohongshu share URL/text")
    parser.add_argument("--note-id", default=None, help="Xiaohongshu note_id")
    parser.add_argument("--config", default=None, help="Runtime config YAML path")
    parser.add_argument("--env-file", default=None, help="Optional env file path")
    parser.add_argument("--allow-process-env", action="store_true", help="Allow process env to override .env/.env.local")
    parser.add_argument("--api-key-env", default=None, help="API key env variable name")
    parser.add_argument("--base-url", default=None, help="Tikomni base URL")
    parser.add_argument("--timeout-ms", type=int, default=None, help="Request timeout ms")
    parser.add_argument("--poll-interval-sec", type=float, default=None, help="U2 polling interval seconds")
    parser.add_argument("--max-polls", type=int, default=None, help="Max U2 polls")
    parser.add_argument(
        "--u2-submit-max-retries",
        type=int,
        default=None,
        help="Max retries for retriable U2 submit failures",
    )
    parser.add_argument(
        "--u2-submit-backoff-ms",
        type=int,
        default=None,
        help="Base backoff ms for retriable U2 submit failures (exponential)",
    )
    parser.add_argument(
        "--u2-timeout-retry-enabled",
        type=str,
        choices=["true", "false"],
        default=None,
        help="Enable conservative retry only when U2 polling times out",
    )
    parser.add_argument(
        "--u2-timeout-retry-max-retries",
        type=int,
        default=None,
        help="Conservative max retries for U2 timeout-only retry (0~3)",
    )
    parser.add_argument("--force-u2-fallback", action="store_true", help="Skip subtitle usage and force U2 fallback (test)")
    parser.add_argument("--write-card", dest="write_card", action="store_true", help="Write benchmark card to card root (default on)")
    parser.add_argument("--no-write-card", dest="write_card", action="store_false", help="Disable benchmark card writing")
    parser.set_defaults(write_card=True)
    parser.add_argument("--card-type", choices=["work", "author", "author_sample_work"], default="work", help="Primary card type")
    parser.add_argument("--collect-material", action="store_true", help="Write extra CMAT card")
    parser.add_argument("--card-root", default=None, help="Card root (absolute); falls back to TIKOMNI_CARD_ROOT when writing cards")
    parser.add_argument("--persist-output", dest="persist_output", action="store_true", help="Persist JSON artifact to TIKOMNI_OUTPUT_ROOT (default on)")
    parser.add_argument("--no-persist-output", dest="persist_output", action="store_false", help="Disable output artifact persistence")
    parser.set_defaults(persist_output=True)
    args = parser.parse_args()

    config, _ = load_tikomni_config(
        args.config,
        env_file=args.env_file,
        allow_process_env=args.allow_process_env,
    )

    resolved_env_file = args.env_file or config_get(config, "runtime.env_file", None)
    api_key_env = args.api_key_env or config_get(config, "runtime.auth_env_key", "TIKOMNI_API_KEY")
    base_url = args.base_url or config_get(config, "runtime.base_url", None)
    timeout_ms = args.timeout_ms if args.timeout_ms is not None else config_get(config, "runtime.timeout_ms", None)
    poll_interval_sec = (
        args.poll_interval_sec
        if args.poll_interval_sec is not None
        else config_get(config, "asr_strategy.poll_interval_sec", 3.0)
    )
    max_polls = args.max_polls if args.max_polls is not None else config_get(config, "asr_strategy.max_polls", 30)
    u2_submit_max_retries = (
        args.u2_submit_max_retries
        if args.u2_submit_max_retries is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.max_retries", 0)
    )
    u2_submit_backoff_ms = (
        args.u2_submit_backoff_ms
        if args.u2_submit_backoff_ms is not None
        else config_get(config, "asr_strategy.submit_retry.xiaohongshu_note.backoff_ms", 0)
    )
    u2_timeout_retry_enabled = (
        (str(args.u2_timeout_retry_enabled).lower() == "true")
        if args.u2_timeout_retry_enabled is not None
        else bool(config_get(config, "asr_strategy.u2_timeout_retry.enabled", True))
    )
    u2_timeout_retry_max_retries = (
        args.u2_timeout_retry_max_retries
        if args.u2_timeout_retry_max_retries is not None
        else config_get(config, "asr_strategy.u2_timeout_retry.max_retries", 3)
    )

    try:
        result = run_xiaohongshu_extract(
            input_value=args.input,
            share_text=args.share_text,
            note_id=args.note_id,
            env_file=resolved_env_file,
            api_key_env=api_key_env,
            base_url=base_url,
            timeout_ms=timeout_ms,
            poll_interval_sec=float(poll_interval_sec),
            max_polls=int(max_polls),
            u2_submit_max_retries=int(u2_submit_max_retries),
            u2_submit_backoff_ms=int(u2_submit_backoff_ms),
            u2_timeout_retry_enabled=bool(u2_timeout_retry_enabled),
            u2_timeout_retry_max_retries=int(u2_timeout_retry_max_retries),
            force_u2_fallback=args.force_u2_fallback,
            write_card=args.write_card,
            card_type=args.card_type,
            collect_material=args.collect_material,
            card_root=args.card_root,
            storage_config=config,
            allow_process_env=args.allow_process_env,
            persist_output=args.persist_output,
        )
    except ValueError as error:
        result = {
            "platform": "xiaohongshu",
            "content_kind": "note",
            "raw_content": "",
            "summary": "",
            "insights": ["source=xiaohongshu:runtime", "runtime_not_ready"],
            "confidence": "low",
            "error_reason": str(error),
            "missing_fields": [],
            "extract_trace": [],
            "fallback_trace": [],
            "request_id": None,
        }

    write_json_stdout(result)
    raise SystemExit(0 if not result.get("error_reason") else 1)


if __name__ == "__main__":
    main()
