# Copy Extract Rules

## 1. Douyin

1. For copy/subtitle/transcript requests, always use U2.
2. `desc/title` can be used as context only, not as final transcript.

## 2. Xiaohongshu

1. Check subtitle fields first (`subtitle_url` / subtitles).
2. If subtitle is unavailable, use U2.

## 3. Batch Per-Item Copy Extraction

1. Enabled by default in homepage flow.
2. Eligibility: `video_model=video` and `13s < duration_ms <= 15min`.
3. Duration ceiling is configurable: `15min` (default) / `30min` / `60min`.
