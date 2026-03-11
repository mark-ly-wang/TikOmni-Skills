#!/usr/bin/env python3
"""Normalize Douyin item type into a stable video gate decision."""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple


VIDEO_MODEL_VIDEO_TOKENS = {
    "video",
    "long_video",
    "mix_video",
    "playlet_video",
}

VIDEO_MODEL_NON_VIDEO_TOKENS = {
    "image",
    "images",
    "photo",
    "atlas",
    "text",
    "live_photo",
    "slideshow",
}

ITEM_TYPE_VIDEO_TOKENS = {
    "video",
    "long_video",
}

ITEM_TYPE_NON_VIDEO_TOKENS = {
    "image",
    "images",
    "photo",
    "atlas",
    "text",
}

# Known common values; unknown values will fall back to structural inspection.
AWEME_TYPE_VIDEO_VALUES = {
    0,
    4,
    51,
    55,
    58,
    61,
    109,
}

AWEME_TYPE_NON_VIDEO_VALUES = {
    2,
    68,
    150,
    151,
    152,
    153,
}


def _to_bool(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        if value in (0, 1):
            return bool(value)
        return None
    if isinstance(value, str):
        token = value.strip().lower()
        if token in {"1", "true", "yes", "y"}:
            return True
        if token in {"0", "false", "no", "n"}:
            return False
    return None


def _to_int(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("-"):
            sign = -1
            text = text[1:]
        else:
            sign = 1
        if text.isdigit():
            return sign * int(text)
    return None


def _pick_field(item: Dict[str, Any], key: str) -> Any:
    if key in item:
        return item.get(key)
    video = item.get("video")
    if isinstance(video, dict) and key in video:
        return video.get(key)
    return None


def _match_token(value: Any, allow: set[str], deny: set[str]) -> Optional[Tuple[bool, str]]:
    if not isinstance(value, str):
        return None
    token = value.strip().lower()
    if not token:
        return None

    # Some responses return serialized JSON in `video_model`; ignore those blobs.
    if token.startswith("{") or token.startswith("["):
        return None

    if token in allow:
        return True, token
    if token in deny:
        return False, token

    # tolerant contains-match for compact variants like "video_model_video"
    if len(token) <= 64:
        for candidate in allow:
            if candidate and candidate in token:
                return True, token
        for candidate in deny:
            if candidate and candidate in token:
                return False, token

    return None


def _has_video_structure(item: Dict[str, Any]) -> bool:
    video = item.get("video")
    if not isinstance(video, dict):
        return False

    if isinstance(video.get("download_addr"), dict):
        addr = video.get("download_addr")
        if isinstance(addr.get("url_list"), list) and len(addr.get("url_list")) > 0:
            return True
    if isinstance(video.get("play_addr"), dict):
        addr = video.get("play_addr")
        if isinstance(addr.get("url_list"), list) and len(addr.get("url_list")) > 0:
            return True
    if isinstance(video.get("bit_rate"), list) and len(video.get("bit_rate")) > 0:
        return True
    if isinstance(video.get("duration"), (int, float)) and float(video.get("duration")) > 0:
        return True

    return False


def normalize_douyin_video_type(item: Dict[str, Any]) -> Dict[str, Any]:
    """Return normalized `is_video` + reason from mixed Douyin schemas.

    Compatible fields include:
    - is_video
    - video_model (item-level and video.video_model)
    - item_type
    - aweme_type
    - structural fallback via item.video.*
    """

    explicit_is_video = _to_bool(_pick_field(item, "is_video"))
    if explicit_is_video is not None:
        return {
            "is_video": explicit_is_video,
            "video_type_reason": f"is_video={explicit_is_video}",
            "matched_field": "is_video",
        }

    video_model_value = _pick_field(item, "video_model")
    video_model_match = _match_token(video_model_value, VIDEO_MODEL_VIDEO_TOKENS, VIDEO_MODEL_NON_VIDEO_TOKENS)
    if video_model_match is not None:
        is_video, token = video_model_match
        return {
            "is_video": is_video,
            "video_type_reason": f"video_model={token}",
            "matched_field": "video_model",
        }

    item_type_value = _pick_field(item, "item_type")
    item_type_match = _match_token(item_type_value, ITEM_TYPE_VIDEO_TOKENS, ITEM_TYPE_NON_VIDEO_TOKENS)
    if item_type_match is not None:
        is_video, token = item_type_match
        return {
            "is_video": is_video,
            "video_type_reason": f"item_type={token}",
            "matched_field": "item_type",
        }

    aweme_type_value = _to_int(_pick_field(item, "aweme_type"))
    if aweme_type_value is not None:
        if aweme_type_value in AWEME_TYPE_VIDEO_VALUES:
            return {
                "is_video": True,
                "video_type_reason": f"aweme_type={aweme_type_value}:video",
                "matched_field": "aweme_type",
            }
        if aweme_type_value in AWEME_TYPE_NON_VIDEO_VALUES:
            return {
                "is_video": False,
                "video_type_reason": f"aweme_type={aweme_type_value}:non_video",
                "matched_field": "aweme_type",
            }

    if _has_video_structure(item):
        return {
            "is_video": True,
            "video_type_reason": "video_struct_present",
            "matched_field": "video_struct",
        }

    image_infos = item.get("image_infos")
    if isinstance(image_infos, list) and len(image_infos) > 0:
        return {
            "is_video": False,
            "video_type_reason": "image_infos_present",
            "matched_field": "image_infos",
        }

    return {
        "is_video": False,
        "video_type_reason": "unknown_non_video_default",
        "matched_field": "default",
    }
