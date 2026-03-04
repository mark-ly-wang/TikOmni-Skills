#!/usr/bin/env python3
"""Shared bootstrap utilities for direct script execution."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional


def _locate_repo_root(file_path: str) -> Optional[Path]:
    current = Path(file_path).resolve()
    for parent in current.parents:
        if (parent / "scripts").is_dir():
            return parent
    return None


def bootstrap_for_direct_run(file_path: str, package: Optional[str] = None) -> Optional[str]:
    """Inject repo root into sys.path when executed as a direct script path.

    Returns the injected repo-root string on success, otherwise ``None``.
    """

    if package not in {None, ""}:
        return None

    repo_root = _locate_repo_root(file_path)
    if repo_root is None:
        return None

    repo_root_str = str(repo_root)
    if repo_root_str not in sys.path:
        sys.path.insert(0, repo_root_str)
    return repo_root_str
