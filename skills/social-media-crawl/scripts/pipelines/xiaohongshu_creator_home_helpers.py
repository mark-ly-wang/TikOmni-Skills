#!/usr/bin/env python3
"""Xiaohongshu creator-home helper entrypoints."""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from scripts.pipelines.homepage_collectors import collect_xhs_author_home_raw
from scripts.pipelines.platform_adapters import adapt_xhs_author_home


def collect_and_adapt(
    *,
    input_value: str,
    base_url: str,
    token: str,
    timeout_ms: int,
    page_size: int,
    pages_max: int,
    max_items: int,
    progress: Any = None,
) -> Tuple[Dict[str, Any], Dict[str, Any], List[Dict[str, Any]], List[Dict[str, str]]]:
    raw = collect_xhs_author_home_raw(
        input_value=input_value,
        base_url=base_url,
        token=token,
        timeout_ms=timeout_ms,
        page_size=page_size,
        pages_max=pages_max,
        max_items=max_items,
        progress=progress,
    )
    profile, works, missing = adapt_xhs_author_home(raw)
    return raw, profile, works, missing

