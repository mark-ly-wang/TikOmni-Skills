---
name: tikomni-skill
description: Use this skill when users ask to analyze a video/post, analyze an author account, do benchmark research, or fetch structured data/copy/comments from supported social platforms. Prioritize intent completion and produce traceable outputs with explicit missing_fields for unavailable data.
---

# Tikomni Skill

## Mission
Complete user-facing content tasks across platforms: analyze a video/post, analyze an author, build benchmark cards, and fetch structured data/copy/comments with traceable outputs (`raw + normalized + markdown`). CLI defaults keep traceability on: write-card enabled, and Douyin single-video runner persists JSON artifacts to output root unless explicitly disabled.

## Script Layout (v2)
- Unified entry: `scripts/cli/run_tikomni_extract.py`
- Readiness check: `scripts/cli/check_tikomni_readiness.py`
- Douyin runner: `scripts/platform/douyin/run_douyin_single_video.py`
- Xiaohongshu runner: `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py`
- Writer entry: `scripts/writers/write_author_homepage_samples.py`

## Supported Platforms
Primary coverage includes: Douyin, Xiaohongshu, TikTok, Kuaishou, Bilibili, Weibo, Toutiao, Xigua, Zhihu, WeChat Channels, WeChat MP, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn, Lemon8, Pipixia.

Use API catalog as the canonical source for capability details and endpoint mapping: `references/api-catalog/index.md`.

## Execution Policy
1. **Matrix-first routing (hard rule):** Always match capability using `references/capability-routing-matrix.md` first.
2. **Fixed capability first (hard rule):** If request matches an active fixed capability in matrix, use that route chain/playbook directly.
3. **Fallback-only after miss (hard rule):** Only when no active fixed capability matches, use universal intent fallback route.
4. **Policy vs execution boundary (hard rule):** Playbooks/matrix define routing policy, not a claim that a specific script has executed successfully; execution truth must come from runtime trace/output.
5. **No fabrication (hard rule):** Never invent unavailable fields. Missing data must be reported via `missing_fields` with reason.
6. **Single-source rules:** Do not redefine API/output/routing rules in this file; use referenced docs as source of truth.

## Universal Workflow
1. Parse user intent and input constraints (platform, content type, quantity, output form).
2. Match `references/capability-routing-matrix.md` first.
3. If matrix has active fixed capability match, follow its route chain (entry script/playbook).
4. If no active fixed capability match, enter universal intent fallback (`routing-rules` + `api-catalog`).
5. Extract and normalize fields under `references/normalize-rules.md`.
6. Validate completeness and emit:
   - `missing_fields`: list of `{ field, reason }`
   - `fallback_trace`: route/fallback decisions
   - `request_id`: upstream trace id when available
7. Deliver markdown output per `references/output-markdown.md`.

## Quality Bar
- **Traceability:** Output must include source route/playbook and key decision trace.
- **Field integrity:** Structured fields align with normalization rules; no silent field dropping.
- **Missing-data discipline:** Any unavailable required field must be placed in `missing_fields`; do not infer or fabricate.
- **Actionability:** Final summary should be directly usable for user intent (extraction/reporting/analysis).

## References
### Core (active)
1. Capability routing matrix (first-class): `references/capability-routing-matrix.md`
2. Routing rules: `references/routing-rules.md`
3. Normalize rules: `references/normalize-rules.md`
4. Runtime config: `references/runtime-config.md`
5. API catalog entry: `references/api-catalog/index.md`
6. Douyin homepage playbook: `references/playbooks/douyin-home-extract.md`
7. Xiaohongshu homepage playbook: `references/playbooks/xiaohongshu-home-extract.md`
8. Copy extraction rules: `references/playbooks/copy-extract-rules.md`
9. Markdown output rules: `references/output-markdown.md`
10. Prompt contracts: `references/prompt-contracts/`

### Phase B planned references (placeholders; not created in Phase A)
1. Universal intent routing guide: `references/guides/universal-intent-routing.md`
2. Video analysis guide: `references/guides/video-analysis.md`
3. Article analysis guide: `references/guides/article-analysis.md`
4. Author home analysis guide: `references/guides/author-home-analysis.md`
5. Comment analysis guide: `references/guides/comment-analysis.md`
