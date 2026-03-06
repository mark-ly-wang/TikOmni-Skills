# Capability Routing Matrix

Use this matrix to decide whether a request matches a fixed capability.
If none fits, enter universal fallback.

This file defines:
- capability name
- trigger intent
- route chain entry
- output expectation

This file does **not** define global endpoint priority or platform-specific endpoint versions.

| capability | status | trigger intents | route chain (entry script/playbook) | output expectation | notes |
|---|---|---|---|---|---|
| douyin.single_video | active | Douyin single video parsing, single-post structured extraction, field extraction from video URL | `scripts/cli/run_tikomni_extract.py` -> `scripts/registry/workflow_registry.py` -> `scripts/platform/douyin/run_douyin_single_video.py` | Single-video `raw + normalized + markdown` with `missing_fields`, `fallback_trace`, and `request_id` (when available) | fixed capability |
| xiaohongshu.single_note | active | Xiaohongshu single-note parsing, content and engagement extraction from note URL | `scripts/cli/run_tikomni_extract.py` -> `scripts/registry/workflow_registry.py` -> `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py` | Single-note `raw + normalized + markdown` with `missing_fields`, `fallback_trace`, and `request_id` (when available) | fixed capability |
| douyin.author_home | active | Douyin author homepage extraction + author analysis (componentized pipeline) | `scripts/cli/run_tikomni_extract.py --platform douyin --content-kind author_home` -> `scripts/registry/workflow_registry.py` -> `scripts/author_home/orchestrator/run_author_analysis.py` | Author profile + paginated works + prompt-first analysis + reused single-work cards | fixed capability |
| xiaohongshu.author_home | active | Xiaohongshu author homepage extraction + author analysis (componentized pipeline) | `scripts/cli/run_tikomni_extract.py --platform xiaohongshu --content-kind author_home` -> `scripts/registry/workflow_registry.py` -> `scripts/author_home/orchestrator/run_author_analysis.py` | Author profile + paginated works + prompt-first analysis + reused single-work cards | fixed capability |
| author.sample_writer | active | Utility: write normalized homepage works into standard cards | `scripts/writers/write_author_homepage_samples.py` | Reusable author sample output with traceable fields | utility-only |
| universal.intent_fallback | fallback | Any supported social-platform request that does not cleanly match a fixed capability but still fits TikOmni data extraction/analysis intent | `references/routing-rules.md` -> `references/api-catalog/index.md` -> `references/normalize-rules.md` -> `references/output-markdown.md` | Structured result/report with explicit `missing_fields` and `fallback_trace` | use when fixed capability does not fit |

## Hard rules
1. Match active fixed capabilities first.
2. Enter `universal.intent_fallback` only when no fixed capability cleanly fits.
3. Treat registry as handler lookup only, not as policy storage.
4. Do not infer TikOmni's total capability boundary from this matrix alone.
