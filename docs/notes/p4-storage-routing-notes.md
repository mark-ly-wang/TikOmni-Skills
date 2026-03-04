# P4 Storage Routing Notes

## What changed

Phase 4 introduces configurable storage routing for benchmark/material cards.

- New module: `scripts/storage_router.py`
- `write_benchmark_card.py` now resolves output routes via storage router instead of hardcoded path branches.
- Route decision can use both:
  1) `content_kind` mapping (default priority)
  2) `card_type` manual input (advanced override with `--force-card-type`)

## Config contract (defaults)

Configured in `references/config-templates/defaults.yaml` under `storage_routes`:

- `content_kind_card_type`
  - `single_video -> work`
  - `author_home -> author_sample_work`
  - `author_analysis -> author`
- `card_type_routes`
  - `work`, `author`, `author_sample_work`, `material`

If custom config omits these sections, built-in defaults are used to preserve behavior.

## Routing priority (risk-closure)

- Default behavior: prefer `content_kind` mapping when provided and mapped.
- Fallback behavior: if no `content_kind` mapping is available, use normalized `card_type`.
- Advanced override: use `--force-card-type` only when you intentionally need manual `card_type` to win.

## Workflow wiring

- `run_douyin_extract.py` and `run_xiaohongshu_extract.py`
  - pass `storage_config=config`
  - pass `content_kind="single_video"` when writing cards
- `run_douyin_single_video.py`
  - supports `--config`
  - passes `storage_config=config` and `--content-kind` (default `single_video`)
- `write_author_homepage_samples.py`
  - supports `--config`
  - writes with `content_kind="author_home"`
- `write_benchmark_card.py`
  - supports `--force-card-type` for explicit manual override

## Config-friendly guidance

- `defaults.yaml` is an internal/default template for scripts and maintainers.
- End users should primarily configure `.env` + `references/runtime-config.md` guidance.
- Avoid asking non-developer users to hand-edit YAML unless they explicitly request advanced routing customization.

## Compatibility

- Existing CLI flags remain valid.
- Existing output layout is unchanged under default mappings.
- New routing metadata includes `force_card_type` and route parts for traceability.
