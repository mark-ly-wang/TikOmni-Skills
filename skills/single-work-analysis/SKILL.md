---
name: single-work-analysis
description: Use this skill for single-item content retrieval, extraction, transcription, benchmarking, breakdown, and analysis. Trigger when the user asks to extract / fetch / transcribe / analyze / benchmark / break down, or 抓取 / 提取 / 转写 / 分析 / 对标 / 拆解 / 作品卡, and the target is a single video, post, article, note, image post, or other single content item rather than a creator, profile, or content collection.
---

# Single Work Analysis

## When To Use

- Use this skill when the target is one concrete content item rather than a creator, account, or profile page.
- Use this skill when the user wants a work card, subtitles or transcription, structured fields, or single-item analysis.
- Use this skill for a single video, post, article, note, image post, or another single content object.
- Use this skill when the user provides a link, share URL, page URL, platform ID, or another clear single-item entry point.

## What It Can Do

- Fetch and normalize facts for one content item.
- Extract titles, captions, subtitles, transcripts, media URLs, author identifiers, and engagement metrics when available.
- Produce a standard work card.
- Return single-item analysis grounded in retrieved facts.
- Return a reduced but still usable result when some fields are unavailable.

## Core Rules

- Keep the task scoped to one content item.
- Reuse the unified work-card field dictionary for final fact fields.
- Prefer the platform guide first. Only go back to API discovery references when the guide is insufficient.
- For video content, prefer platform-native subtitles before ASR.
- Use `asr_clean` as the primary text for video items and `caption_raw` as the primary text for text items.
- If usable `asr_raw` cannot be obtained for a video item, keep the fact card and return `incomplete` instead of fabricating analysis.

## Do Not

- Do not output creator cards.
- Do not introduce bucketing, sampling, sampled explanations, or `author_analysis_v2`.
- Do not expose platform process fields directly in the final work-card body.
- Do not expand a single-item task into creator-level analysis.

## Workflow

1. Identify the platform and `work_modality`, and confirm that the task is about one content item.
2. Read `references/contracts/work-card-fields.md` to confirm required fields and final display fields.
3. Read the platform guide first:
   - Douyin: `references/platform-guides/douyin.md`
   - Xiaohongshu: `references/platform-guides/xiaohongshu.md`
   - Other platforms: `references/platform-guides/generic.md`
4. For video content, read `references/service-guides/asr-u2-u3-fallback.md` and then `references/asr-and-fallback.md` to handle `subtitle_raw`, `asr_raw`, and `asr_clean`.
5. Read `references/api-capability-index.md`, `references/api-tags/`, and `references/api-contracts/` only when the platform guide does not provide enough route or field detail.
6. Return the standard work card first, then return the single-item analysis result.

## References

- API capability index: `references/api-capability-index.md`
- Tag-level route summaries: `references/api-tags/`
- Tag-level full contracts: `references/api-contracts/`
- U2/U3 ASR fallback: `references/service-guides/asr-u2-u3-fallback.md`
- Work-card fields: `references/contracts/work-card-fields.md`
- Work-card schema: `references/schemas/work-card.schema.json`
- ASR and failure handling: `references/asr-and-fallback.md`
- Generic platform guide: `references/platform-guides/generic.md`
- Douyin guide: `references/platform-guides/douyin.md`
- Xiaohongshu guide: `references/platform-guides/xiaohongshu.md`
