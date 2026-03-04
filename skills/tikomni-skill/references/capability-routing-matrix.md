# Capability Routing Matrix

This matrix is the capability routing entry list for the TikOmni skill.
Match fixed capabilities first, then use universal fallback.

Scope:
- This document defines agent routing policy.
- Unified entry and registry handle mapping and dispatch only.

| capability | status | trigger intents | route chain (entry script/playbook) | output expectation | notes |
|---|---|---|---|---|---|
| douyin.single_video | active | Douyin single video parsing, single-post structured extraction, field extraction from video URL | `scripts/cli/run_tikomni_extract.py` -> `scripts/registry/workflow_registry.py` -> `scripts/platform/douyin/run_douyin_single_video.py` | Single-video `raw + normalized + markdown` with `missing_fields`, `fallback_trace`, and `request_id` (when available) | availability-first; `one_video app` primary, `one_video web` fallback |
| xiaohongshu.single_note | active | Xiaohongshu single-note parsing, content and engagement extraction from note URL | `scripts/cli/run_tikomni_extract.py` -> `scripts/registry/workflow_registry.py` -> `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py` | Single-note `raw + normalized + markdown` with `missing_fields`, `fallback_trace`, and `request_id` (when available) | default kind in registry is `note`; alias `single_video` supported |
| douyin.homepage_extract | active | Douyin author homepage extraction, homepage sampling, pre-analysis sampling | `references/playbooks/douyin-home-extract.md` | Homepage samples and traceable fields for downstream analysis/card writing | fixed playbook route; direct when matched |
| xiaohongshu.homepage_extract | active | Xiaohongshu author homepage extraction, homepage sampling, pre-analysis sampling | `references/playbooks/xiaohongshu-home-extract.md` | Homepage samples and traceable fields for downstream analysis/card writing | fixed playbook route; direct when matched |
| author.sample_writer | active | Write author homepage samples into standard cards, produce reusable sample docs | `scripts/writers/write_author_homepage_samples.py` | Reusable author sample output with traceable fields | supports sample accumulation and downstream content analysis |
| universal.intent_fallback | fallback | General research/extraction/analysis requests that miss fixed capabilities above | `references/routing-rules.md` -> `references/api-catalog/index.md` -> `references/normalize-rules.md` -> `references/output-markdown.md` | Structured result/report for user intent with explicit `missing_fields` and `fallback_trace` | trigger only after fixed capability miss |

## Routing Rules (Hard)
1. Perform capability matching by this matrix first (`active` priority).
2. Enter `universal.intent_fallback` only when fixed capabilities are not matched.
3. Registry is for handler mapping lookup only; do not use it as routing policy priority resolver.
4. Do not describe matrix/playbook policy as guaranteed script execution; execution facts must come from runtime results and trace.
