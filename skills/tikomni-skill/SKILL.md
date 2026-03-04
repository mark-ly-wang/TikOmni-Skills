---
name: tikomni-skill
description: Use this skill when users ask to analyze a video/post, analyze an author account, do benchmark research, or fetch structured data/copy/comments from supported social platforms. Prioritize intent completion and produce traceable outputs with explicit missing_fields for unavailable data.
---

# Tikomni Skill

## Mission
Complete user-facing content tasks across platforms: analyze a video/post, analyze an author, build benchmark cards, and fetch structured data/copy/comments with traceable outputs (`raw + normalized + markdown`).

Default behavior:
- `--write-card` is enabled by default (disable with `--no-write-card`).
- Unified entry JSON persistence is enabled by default for all registered workflows (disable globally with `--no-persist-output`).

## Script Layout (Phase A/B aligned)
- Unified CLI entry: `scripts/cli/run_tikomni_extract.py`
- Workflow registry (mapping): `scripts/registry/workflow_registry.py`
- Platform handlers: `scripts/platform/douyin/run_douyin_single_video.py`, `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py`
- Shared core: `scripts/core/`
- Shared pipeline: `scripts/pipeline/asr/`
- Writers: `scripts/writers/`
- Readiness check: `scripts/cli/check_tikomni_readiness.py`

## Routing Boundary (Hard)
1. Use unified entry + registry mapping: `run_tikomni_extract` parses inputs and resolves handlers through registry.
2. Registry scope is mapping only: `(platform, content_kind) -> handler`.
3. Routing policy source of truth: `references/capability-routing-matrix.md` + `references/routing-rules.md`.

## Execution Policy
1. **Matrix-first routing (hard rule):** Always match capability using `references/capability-routing-matrix.md` first.
2. **Fixed capability first (hard rule):** If request matches an active fixed capability in matrix, use that route chain/playbook directly.
3. **Fallback-only after miss (hard rule):** Only when no active fixed capability matches, use universal intent fallback route.
4. **Policy vs execution boundary (hard rule):** Playbooks/matrix define routing policy, not execution success; execution truth comes from runtime trace/output.
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
- **Traceability:** Output includes source route/playbook and key decision trace.
- **Field integrity:** Structured fields align with normalization rules; no silent field dropping.
- **Missing-data discipline:** Any unavailable required field must be placed in `missing_fields`; do not infer or fabricate.
- **Actionability:** Final summary is directly usable for user intent (extraction/reporting/analysis).

## References
1. Capability routing matrix (first-class): `references/capability-routing-matrix.md`
2. Routing rules: `references/routing-rules.md`
3. Runtime config: `references/runtime-config.md`
4. Normalize rules: `references/normalize-rules.md`
5. API catalog entry: `references/api-catalog/index.md`
6. Douyin homepage playbook: `references/playbooks/douyin-home-extract.md`
7. Xiaohongshu homepage playbook: `references/playbooks/xiaohongshu-home-extract.md`
8. Copy extraction rules: `references/playbooks/copy-extract-rules.md`
9. Markdown output rules: `references/output-markdown.md`
10. Prompt contracts: `references/prompt-contracts/`
