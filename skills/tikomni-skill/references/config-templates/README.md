# Config Templates (Developer Notes)

This folder contains executable runtime config templates used by local scripts.

## Default Template

- Path: `references/config-templates/defaults.yaml`
- Purpose: keep script defaults centralized without changing current behavior

## Loader Priority

`scripts/config_loader.py` resolves config in this order:

1. CLI `--config <path>`
2. Environment variable `TIKOMNI_CONFIG_FILE`
3. Built-in default: `references/config-templates/defaults.yaml`

## Current Script Support

- `scripts/run_tikomni_extract.py`
- `scripts/run_douyin_extract.py`
- `scripts/run_xiaohongshu_extract.py`

Example:

```bash
python3 skills/tikomni-skill/scripts/run_tikomni_extract.py "<url>" \
  --config skills/tikomni-skill/references/config-templates/defaults.yaml
```

If no `--config` is passed, behavior stays aligned with existing defaults (base URL, timeout, poll strategy, and douyin retry policy).
