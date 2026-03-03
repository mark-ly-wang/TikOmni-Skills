# P4 Storage Routing Notes

## What changed

Phase 4 introduces configurable storage routing for benchmark/material cards.

- New module: `scripts/storage_router.py`
- `write_benchmark_card.py` now resolves output routes via storage router instead of hardcoded path branches.
- Route decision can use both:
  1) `card_type`
  2) `content_kind` (mapped to card type by config)

## Config contract (defaults)

Configured in `references/config-templates/defaults.yaml` under `storage_routes`:

- `content_kind_card_type`
  - `single_video -> work`
  - `author_home -> author_sample_work`
  - `author_analysis -> author`
- `card_type_routes`
  - `work`, `author`, `author_sample_work`, `material`

If custom config omits these sections, built-in defaults are used to preserve behavior.

## Workflow wiring

- `run_douyin_extract.py` and `run_xiaohongshu_extract.py`
  - pass `storage_config=config`
  - pass `content_kind="single_video"` when writing cards
- `run_douyin_single_video.py`
  - now supports `--config`
  - passes `storage_config=config` and `--content-kind` (default `single_video`)
- `write_author_homepage_samples.py`
  - now supports `--config`
  - writes with `content_kind="author_home"`

## Compatibility

- Existing CLI flags and defaults remain valid.
- Existing output layout is unchanged by default config.
- New routing metadata is returned in `card_write.routing` for traceability.
