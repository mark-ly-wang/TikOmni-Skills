#!/usr/bin/env python3
"""Shared media URL classification helpers."""

from __future__ import annotations

from typing import Iterable, List


def _is_http_url(url: str) -> bool:
    lower = (url or "").lower()
    return lower.startswith("http://") or lower.startswith("https://")


def is_probable_image_url(url: str) -> bool:
    lower = (url or "").lower()
    if not _is_http_url(lower):
        return False
    image_tokens = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".gif",
        "imageview2",
        "imagemogr2",
        "redimage",
        "frame/",
        "sns-img",
        "sns-webpic",
        "notes_pre_post",
        "/image/",
        "/img/",
    ]
    return any(token in lower for token in image_tokens)


def is_probable_audio_url(url: str) -> bool:
    lower = (url or "").lower()
    if not _is_http_url(lower):
        return False
    audio_tokens = [
        ".m4a",
        ".mp3",
        ".aac",
        ".wav",
        ".flac",
        ".ogg",
        "/audio/",
        "sns-audio",
        "redaudio",
    ]
    return any(token in lower for token in audio_tokens)


def is_probable_video_url(url: str) -> bool:
    lower = (url or "").lower()
    if not _is_http_url(lower):
        return False
    if is_probable_image_url(lower) or is_probable_audio_url(lower):
        return False
    video_tokens = [
        ".mp4",
        ".m3u8",
        ".mov",
        ".flv",
        "/video/",
        "sns-video",
        "redvideo",
        "play",
        "stream",
        "master",
        "vod",
    ]
    return any(token in lower for token in video_tokens)


def filter_video_urls(urls: Iterable[str]) -> List[str]:
    unique: List[str] = []
    seen = set()
    for raw in urls:
        url = str(raw or "").strip()
        if not url or url in seen or not is_probable_video_url(url):
            continue
        unique.append(url)
        seen.add(url)
    return unique
