# Config Templates (Developer Notes)

This folder contains runtime config templates used by local scripts.

`defaults.yaml` is the default template for script maintainers and advanced routing customization.

## Default Template

- Path: `references/config-templates/defaults.yaml`
- Purpose: keep script defaults centralized without changing current behavior

## Loader Priority

`scripts/core/config_loader.py` resolves config in this order:

1. CLI `--config <path>`
2. Environment variable `TIKOMNI_CONFIG_FILE`
3. Built-in default: `references/config-templates/defaults.yaml`

## Current Script Support (Phase A/B)

- `scripts/cli/run_tikomni_extract.py` (unified entry)
- `scripts/registry/workflow_registry.py` (mapping layer consumed by unified entry)
- `scripts/platform/douyin/run_douyin_single_video.py`
- `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py`

## Default Runtime Behavior

- Fixed pipelines always write cards.
- Fixed pipelines always persist workflow JSON artifacts.
- Unified entry and fixed platform handlers do not expose per-run disable switches for card writing or output persistence.

Example:

```bash
python3 scripts/cli/run_tikomni_extract.py "<url>" \
  --config references/config-templates/defaults.yaml
```

If `--config` is not passed, behavior remains aligned with existing defaults (base URL, timeout, poll strategy, and retry policy).
