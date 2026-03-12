#!/usr/bin/env python3
"""Shared input normalization and validation for social-media pipelines."""

from __future__ import annotations

import re
from typing import Dict, List, Optional
from urllib.parse import parse_qs, urlparse

from scripts.core.tikomni_common import normalize_text

_HTTP_URL_RE = re.compile(r"https?://[^\s<>'\"，。！？；：）】》]+", re.IGNORECASE)
_URL_TRAILING_PUNCTUATION = ".,!?;:)]}>'\"，。！？；：）】》、"
_XHS_NOTE_ID_RE = re.compile(r"^[0-9A-Za-z]{16,32}$")
_XHS_USER_ID_RE = re.compile(r"^[0-9A-Za-z]{8,32}$")
_DOUYIN_SEC_UID_RE = re.compile(r"^MS4wLjA[A-Za-z0-9_-]{8,}$")

_DOUYIN_HOST_TOKENS = ("douyin.com", "iesdouyin.com", "v.douyin.com")
_XHS_HOST_TOKENS = ("xiaohongshu.com", "xhslink.com")


def _dedupe_keep_order(items: List[str]) -> List[str]:
    unique: List[str] = []
    seen = set()
    for item in items:
        if item in seen:
            continue
        unique.append(item)
        seen.add(item)
    return unique


def _strip_url_punctuation(value: str) -> str:
    return value.rstrip(_URL_TRAILING_PUNCTUATION)


def extract_http_urls(text: Optional[str]) -> List[str]:
    raw = normalize_text(text)
    if not raw:
        return []
    matches = [_strip_url_punctuation(match.group(0)) for match in _HTTP_URL_RE.finditer(raw)]
    return _dedupe_keep_order([item for item in matches if item])


def _first_platform_url(text: Optional[str], host_tokens: tuple[str, ...]) -> Optional[str]:
    for url in extract_http_urls(text):
        host = urlparse(url).netloc.lower()
        if any(token in host for token in host_tokens):
            return url
    return None


def _text_contains_host(text: Optional[str], host_tokens: tuple[str, ...]) -> bool:
    lowered = normalize_text(text).lower()
    return any(token in lowered for token in host_tokens)


def looks_like_douyin_sec_uid(value: Optional[str]) -> bool:
    return bool(_DOUYIN_SEC_UID_RE.fullmatch(normalize_text(value)))


def looks_like_xhs_note_id(value: Optional[str]) -> bool:
    return bool(_XHS_NOTE_ID_RE.fullmatch(normalize_text(value)))


def looks_like_xhs_user_id(value: Optional[str]) -> bool:
    return bool(_XHS_USER_ID_RE.fullmatch(normalize_text(value)))


def extract_douyin_share_url(text: Optional[str]) -> Optional[str]:
    return _first_platform_url(text, _DOUYIN_HOST_TOKENS)


def extract_douyin_sec_uid(text: Optional[str]) -> Optional[str]:
    raw = normalize_text(text)
    if not raw:
        return None
    if looks_like_douyin_sec_uid(raw):
        return raw

    for url in extract_http_urls(raw):
        query = parse_qs(urlparse(url).query)
        for key in ("sec_uid", "sec_user_id"):
            candidate = normalize_text((query.get(key) or [""])[0])
            if looks_like_douyin_sec_uid(candidate):
                return candidate

    match = re.search(r"(?:sec_uid|sec_user_id)=([A-Za-z0-9._-]+)", raw)
    if match:
        candidate = normalize_text(match.group(1))
        if looks_like_douyin_sec_uid(candidate):
            return candidate
    return None


def extract_xhs_note_id(text: Optional[str]) -> Optional[str]:
    raw = normalize_text(text)
    if not raw:
        return None
    if looks_like_xhs_note_id(raw):
        return raw

    for pattern in (
        r"/explore/([0-9A-Za-z]+)",
        r"/discovery/item/([0-9A-Za-z]+)",
        r"note_id=([0-9A-Za-z]+)",
    ):
        match = re.search(pattern, raw)
        if not match:
            continue
        candidate = normalize_text(match.group(1))
        if looks_like_xhs_note_id(candidate):
            return candidate
    return None


def extract_xhs_user_id(text: Optional[str]) -> Optional[str]:
    raw = normalize_text(text)
    if not raw:
        return None
    if looks_like_xhs_user_id(raw):
        return raw

    for pattern in (
        r"/user/profile/([0-9A-Za-z]+)",
        r"(?:user_id|userid)=([0-9A-Za-z]+)",
    ):
        match = re.search(pattern, raw)
        if not match:
            continue
        candidate = normalize_text(match.group(1))
        if looks_like_xhs_user_id(candidate):
            return candidate
    return None


def extract_xhs_note_share_url(text: Optional[str]) -> Optional[str]:
    for url in extract_http_urls(text):
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        path = parsed.path.lower()
        query = parsed.query.lower()
        if "xhslink.com" in host:
            return url
        if "xiaohongshu.com" not in host:
            continue
        if "/explore/" in path or "/discovery/item/" in path or "note_id=" in query:
            return url
    return None


def extract_xhs_creator_share_url(text: Optional[str]) -> Optional[str]:
    for url in extract_http_urls(text):
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        path = parsed.path.lower()
        query = parsed.query.lower()
        if "xhslink.com" in host:
            return url
        if "xiaohongshu.com" not in host:
            continue
        if "/user/profile/" in path or "/user/" in path or "user_id=" in query or "userid=" in query:
            return url
    return None


def text_has_douyin_short_link(text: Optional[str]) -> bool:
    return _text_contains_host(text, ("v.douyin.com",))


def text_has_xhs_short_link(text: Optional[str]) -> bool:
    return _text_contains_host(text, ("xhslink.com",))


def normalize_douyin_work_input(input_value: Optional[str], share_url: Optional[str]) -> Dict[str, object]:
    explicit_share = normalize_text(share_url)
    raw_input = normalize_text(input_value)
    normalized_share = extract_douyin_share_url(explicit_share) or extract_douyin_share_url(raw_input)

    if normalized_share:
        return {
            "share_url": normalized_share,
            "error_reason": None,
            "missing_fields": [],
        }

    if raw_input:
        if text_has_douyin_short_link(raw_input):
            return {
                "share_url": None,
                "error_reason": "short_link_detected_but_unresolved",
                "missing_fields": [{"field": "share_url", "reason": "short_link_unresolved"}],
            }
        return {
            "share_url": None,
            "error_reason": "invalid_share_url",
            "missing_fields": [{"field": "share_url", "reason": "invalid_input"}],
        }

    return {
        "share_url": None,
        "error_reason": None,
        "missing_fields": [],
    }


def normalize_xhs_note_input(
    input_value: Optional[str],
    share_text: Optional[str],
    note_id: Optional[str],
) -> Dict[str, object]:
    explicit_note_id = normalize_text(note_id)
    if explicit_note_id and not looks_like_xhs_note_id(explicit_note_id):
        return {
            "share_text": None,
            "note_id": None,
            "error_reason": "invalid_note_id",
            "missing_fields": [{"field": "note_id", "reason": "invalid_format"}],
        }

    explicit_share = normalize_text(share_text)
    raw_input = normalize_text(input_value)

    normalized_note_id = explicit_note_id or extract_xhs_note_id(explicit_share) or extract_xhs_note_id(raw_input)
    normalized_share = extract_xhs_note_share_url(explicit_share) or extract_xhs_note_share_url(raw_input)

    if normalized_note_id or normalized_share:
        return {
            "share_text": normalized_share or None,
            "note_id": normalized_note_id or None,
            "error_reason": None,
            "missing_fields": [],
        }

    candidate = explicit_share or raw_input
    if candidate:
        if text_has_xhs_short_link(candidate):
            return {
                "share_text": None,
                "note_id": None,
                "error_reason": "short_link_detected_but_unresolved",
                "missing_fields": [{"field": "note_id", "reason": "short_link_unresolved"}],
            }
        return {
            "share_text": None,
            "note_id": None,
            "error_reason": "invalid_note_id",
            "missing_fields": [{"field": "note_id", "reason": "invalid_format"}],
        }

    return {
        "share_text": None,
        "note_id": None,
        "error_reason": None,
        "missing_fields": [],
    }


def normalize_douyin_creator_input(input_value: Optional[str]) -> Dict[str, object]:
    raw_input = normalize_text(input_value)
    normalized_input = extract_douyin_sec_uid(raw_input) or extract_douyin_share_url(raw_input) or raw_input or None

    if extract_douyin_sec_uid(raw_input) or extract_douyin_share_url(raw_input):
        return {
            "input_value": normalized_input,
            "error_reason": None,
            "missing_fields": [],
        }

    if raw_input:
        if text_has_douyin_short_link(raw_input):
            return {
                "input_value": None,
                "error_reason": "short_link_detected_but_unresolved",
                "missing_fields": [{"field": "platform_author_id", "reason": "short_link_unresolved"}],
            }
        return {
            "input_value": None,
            "error_reason": "invalid_creator_input",
            "missing_fields": [{"field": "platform_author_id", "reason": "invalid_format"}],
        }

    return {
        "input_value": None,
        "error_reason": None,
        "missing_fields": [],
    }


def normalize_xhs_creator_input(input_value: Optional[str]) -> Dict[str, object]:
    raw_input = normalize_text(input_value)
    normalized_input = extract_xhs_user_id(raw_input) or extract_xhs_creator_share_url(raw_input) or None

    if normalized_input:
        return {
            "input_value": normalized_input,
            "error_reason": None,
            "missing_fields": [],
        }

    if raw_input:
        if text_has_xhs_short_link(raw_input):
            return {
                "input_value": None,
                "error_reason": "short_link_detected_but_unresolved",
                "missing_fields": [{"field": "platform_author_id", "reason": "short_link_unresolved"}],
            }
        return {
            "input_value": None,
            "error_reason": "invalid_creator_input",
            "missing_fields": [{"field": "platform_author_id", "reason": "invalid_format"}],
        }

    return {
        "input_value": None,
        "error_reason": None,
        "missing_fields": [],
    }
