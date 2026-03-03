#!/usr/bin/env python3
"""Low-quality-first video URL selector for Douyin single video flow."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse


def _dedupe_urls(values: List[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for value in values:
        if not isinstance(value, str):
            continue
        url = value.strip()
        if not (url.startswith("http://") or url.startswith("https://")):
            continue
        if url in seen:
            continue
        seen.add(url)
        ordered.append(url)
    return ordered


def _extract_urls_from_addr(addr: Any) -> List[str]:
    if not isinstance(addr, dict):
        return []
    urls = addr.get("url_list")
    if not isinstance(urls, list):
        return []
    return _dedupe_urls([str(item) for item in urls if isinstance(item, str)])


def _quality_hint_score(url: str) -> Optional[int]:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    # Highest confidence: explicit quality-like query params.
    for key in ("ratio", "resolution", "quality", "qn"):
        values = query.get(key)
        if not values:
            continue
        text = str(values[0]).lower()
        match = re.search(r"(\d{3,4})p", text)
        if match:
            return int(match.group(1))
        if text.isdigit():
            return int(text)

    lower_url = url.lower()
    for token, score in (
        ("240p", 240),
        ("360p", 360),
        ("480p", 480),
        ("540p", 540),
        ("576p", 576),
        ("720p", 720),
        ("1080p", 1080),
        ("2k", 2000),
        ("4k", 4000),
    ):
        if token in lower_url:
            return score

    # Fallback quality-style tags in path/query fragments.
    path_match = re.search(r"(\d{3,4})p", parsed.path.lower())
    if path_match:
        return int(path_match.group(1))

    return None


def _choose_lowest_from_download(download_urls: List[str]) -> Tuple[Optional[str], str]:
    if not download_urls:
        return None, "download_addr_missing"

    scored: List[Tuple[int, int, str]] = []
    for index, url in enumerate(download_urls):
        score = _quality_hint_score(url)
        if score is not None:
            scored.append((score, index, url))

    if scored:
        scored.sort(key=lambda row: (row[0], row[1]))
        winner = scored[0]
        return winner[2], f"download_addr_lowest_quality_hint(score={winner[0]})"

    # Explicit fallback rule (required): no quality hints => pick first download URL.
    return download_urls[0], "download_addr_first_url_fallback(no_quality_hint)"


def _parse_video_id(url: str) -> Optional[str]:
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        values = query.get("video_id")
        if values and values[0]:
            return values[0]
    except Exception:
        return None
    return None


def select_low_quality_video_url(video: Dict[str, Any]) -> Dict[str, Any]:
    """Select lowest-quality candidate with strict download_addr priority.

    Rules:
    1) Base candidate set from `video.download_addr.url_list`.
    2) If `video.bit_rate` exists, find the minimum `bit_rate` entry and try to map it
       back to download_addr by URL equality / shared `uri` / shared `video_id`.
    3) If mapping fails, choose the lowest-quality candidate from download_addr using:
       - smallest quality hint in URL (`ratio/quality/...`), else
       - first URL in download list.
    """

    download_addr = video.get("download_addr") if isinstance(video.get("download_addr"), dict) else {}
    download_urls = _extract_urls_from_addr(download_addr)
    download_uri = download_addr.get("uri") if isinstance(download_addr.get("uri"), str) else None

    bit_rate_list = video.get("bit_rate") if isinstance(video.get("bit_rate"), list) else []

    min_entry: Optional[Dict[str, Any]] = None
    min_rate: Optional[int] = None
    for index, entry in enumerate(bit_rate_list):
        if not isinstance(entry, dict):
            continue
        raw_rate = entry.get("bit_rate")
        try:
            rate = int(raw_rate)
        except Exception:
            continue
        if min_rate is None or rate < min_rate:
            min_rate = rate
            min_entry = {"index": index, "entry": entry}

    if min_entry and min_rate is not None:
        candidate_entry = min_entry["entry"]
        candidate_urls = _dedupe_urls(
            _extract_urls_from_addr(candidate_entry.get("download_addr"))
            + _extract_urls_from_addr(candidate_entry.get("play_addr"))
        )
        candidate_download_addr = candidate_entry.get("download_addr")
        candidate_play_addr = candidate_entry.get("play_addr")

        # mapping strategy A: direct URL equality
        if candidate_urls and download_urls:
            download_set = set(download_urls)
            for candidate_url in candidate_urls:
                if candidate_url in download_set:
                    return {
                        "video_down_url": candidate_url,
                        "selection_reason": f"bit_rate_min_mapped_url(bit_rate={min_rate})",
                        "selected_from": "bit_rate_mapped",
                        "min_bit_rate": min_rate,
                        "download_url_count": len(download_urls),
                        "bit_rate_count": len(bit_rate_list),
                    }

        # mapping strategy B: shared URI
        candidate_uri = None
        if isinstance(candidate_download_addr, dict) and isinstance(candidate_download_addr.get("uri"), str):
            candidate_uri = candidate_download_addr.get("uri")
        if not candidate_uri and isinstance(candidate_play_addr, dict) and isinstance(candidate_play_addr.get("uri"), str):
            candidate_uri = candidate_play_addr.get("uri")
        if candidate_uri and download_uri and candidate_uri == download_uri and download_urls:
            return {
                "video_down_url": download_urls[0],
                "selection_reason": f"bit_rate_min_mapped_uri(bit_rate={min_rate})",
                "selected_from": "bit_rate_mapped",
                "min_bit_rate": min_rate,
                "download_url_count": len(download_urls),
                "bit_rate_count": len(bit_rate_list),
            }

        # mapping strategy C: shared video_id in URL query
        candidate_video_ids = {v for v in (_parse_video_id(url) for url in candidate_urls) if v}
        if candidate_video_ids and download_urls:
            for url in download_urls:
                video_id = _parse_video_id(url)
                if video_id and video_id in candidate_video_ids:
                    return {
                        "video_down_url": url,
                        "selection_reason": f"bit_rate_min_mapped_video_id(bit_rate={min_rate})",
                        "selected_from": "bit_rate_mapped",
                        "min_bit_rate": min_rate,
                        "download_url_count": len(download_urls),
                        "bit_rate_count": len(bit_rate_list),
                    }

    selected_url, fallback_reason = _choose_lowest_from_download(download_urls)
    return {
        "video_down_url": selected_url,
        "selection_reason": fallback_reason,
        "selected_from": "download_addr",
        "min_bit_rate": min_rate,
        "download_url_count": len(download_urls),
        "bit_rate_count": len(bit_rate_list),
    }
