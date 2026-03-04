#!/usr/bin/env python3
"""Domain model skeleton for Tikomni extraction artifacts.

Phase 1 goal: define typed structures only, with zero behavior changes.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Literal, Optional, Tuple

SCHEMA_VERSION_V1 = "v1"
DEFAULT_SCHEMA_VERSION = SCHEMA_VERSION_V1
SUPPORTED_CONTENT_KINDS: Tuple[str, ...] = (
    "douyin_video",
    "xiaohongshu_note",
)

ContentKind = Literal["douyin_video", "xiaohongshu_note"]


@dataclass(frozen=True)
class NormalizedContent:
    """Normalized extraction output payload (language-agnostic skeleton)."""

    schema_version: str = DEFAULT_SCHEMA_VERSION
    content_kind: str = "douyin_video"
    platform: str = ""
    source_id: str = ""
    raw_content: str = ""
    summary: str = ""
    confidence: str = "low"
    request_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AsrArtifact:
    """ASR-related task/result metadata."""

    schema_version: str = DEFAULT_SCHEMA_VERSION
    content_kind: str = "douyin_video"
    task_id: Optional[str] = None
    task_status: str = "UNKNOWN"
    transcript_text: str = ""
    retry_count: int = 0
    poll_count: int = 0
    request_id: Optional[str] = None


@dataclass(frozen=True)
class AnalysisArtifact:
    """Post-ASR analysis/summarization artifact."""

    schema_version: str = DEFAULT_SCHEMA_VERSION
    content_kind: str = "douyin_video"
    summary: str = ""
    insights: Tuple[str, ...] = ()
    prompt_contract: Optional[str] = None
    request_id: Optional[str] = None


@dataclass(frozen=True)
class StorageTarget:
    """Output storage route metadata."""

    schema_version: str = DEFAULT_SCHEMA_VERSION
    content_kind: str = "douyin_video"
    route_key: str = "default"
    root_dir: str = "tikomni-output"
    runs_dir: str = "_runs"
    results_dir: str = "results"
    errors_dir: str = "_errors"
    filename_pattern: str = "{type}-{timestamp}-{job_id}.md"


def is_supported_content_kind(content_kind: str) -> bool:
    return content_kind in SUPPORTED_CONTENT_KINDS
