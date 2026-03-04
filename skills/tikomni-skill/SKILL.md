---
name: tikomni-skill
description: Use this skill when users ask to analyze a video/post, analyze an author account, do benchmark research, or fetch structured data/copy/comments from supported social platforms. Prioritize intent completion and produce traceable outputs with explicit missing_fields for unavailable data.
---

# Tikomni Skill

## Mission
Complete user-facing content tasks across platforms: analyze a video/post, analyze an author, build benchmark cards, and fetch structured data/copy/comments with traceable outputs (`raw + normalized + markdown`).

## Supported Platforms
Primary coverage includes: Douyin, Xiaohongshu, TikTok, Kuaishou, Bilibili, Weibo, Toutiao, Xigua, Zhihu, WeChat Channels, WeChat MP, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn, Lemon8, Pipixia.

Use API catalog as the canonical source for capability details and endpoint mapping: `references/api-catalog/index.md`.

## Execution Policy
1. **Pipeline-first (hard rule):** If the request matches explicit fixed playbooks, execute playbook flow only.
   - Douyin homepage extraction → `references/playbooks/douyin-home-extract.md`
   - Xiaohongshu homepage extraction → `references/playbooks/xiaohongshu-home-extract.md`
2. **Intent fallback (hard rule):** If no fixed playbook matches, route by intent using `references/api-catalog/index.md` and routing rules.
3. **No fabrication (hard rule):** Never invent unavailable fields. Missing data must be reported via `missing_fields` with reason.
4. **Single-source rules:** Do not redefine API/output/routing rules in this file; use referenced docs as source of truth.

## Universal Workflow
1. Parse user intent and input constraints (platform, content type, quantity, output form).
2. Decide route: fixed playbook or intent fallback.
3. Select endpoint priority using runtime config policy (`app > web_v2 > web` when unspecified).
   - Douyin single-video is **availability-first** (`one_video app` primary, `one_video web` fallback).
   - High-quality Douyin chain is deprecated and must not be treated as an active primary route.
4. Extract and normalize fields under `references/normalize-rules.md`.
5. Validate completeness and emit:
   - `missing_fields`: list of `{ field, reason }`
   - `fallback_trace`: route/fallback decisions
   - `request_id`: upstream trace id when available
6. Deliver markdown output per `references/output-markdown.md`.

## Quality Bar
- **Traceability:** Output must include source route/playbook and key decision trace.
- **Field integrity:** Structured fields align with normalization rules; no silent field dropping.
- **Missing-data discipline:** Any unavailable required field must be placed in `missing_fields`; do not infer or fabricate.
- **Actionability:** Final summary should be directly usable for user intent (extraction/reporting/analysis).

## References
### Core (active)
1. Routing rules: `references/routing-rules.md`
2. Normalize rules: `references/normalize-rules.md`
3. Runtime config: `references/runtime-config.md`
4. API catalog entry: `references/api-catalog/index.md`
5. Douyin homepage playbook: `references/playbooks/douyin-home-extract.md`
6. Xiaohongshu homepage playbook: `references/playbooks/xiaohongshu-home-extract.md`
7. Copy extraction rules: `references/playbooks/copy-extract-rules.md`
8. Markdown output rules: `references/output-markdown.md`
9. Prompt contracts: `references/prompt-contracts/`

### Phase B planned references (placeholders; not created in Phase A)
1. Universal intent routing guide: `references/guides/universal-intent-routing.md`
2. Video analysis guide: `references/guides/video-analysis.md`
3. Article analysis guide: `references/guides/article-analysis.md`
4. Author home analysis guide: `references/guides/author-home-analysis.md`
5. Comment analysis guide: `references/guides/comment-analysis.md`
