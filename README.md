# TikOmni Skills

English | [中文说明 (README.zh-CN.md)](./README.zh-CN.md)

This repository hosts the TikOmni agent skill (`skills/tikomni-skill`) for direct HTTP calls to TikOmni public APIs (`u1` + `u2`) and structured markdown outputs.

## Platform

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API: https://api.tikomni.com
- API Docs: https://docs.tikomni.com

## Quick Start

```bash
# 1) Prepare config (choose one)
cp ./skills/tikomni-skill/env.example ./.env
# or
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local

# 2) Fill real TIKOMNI_API_KEY, then verify readiness
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# 3) (Optional) Generate API catalog
node ./skills/tikomni-skill/scripts/generate-api-catalog.mjs

# 4) Run extraction
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"
```

## Configuration (Important)

For users, configuration sources are **ONLY**:
1. `<repo_root>/.env`
2. `skills/tikomni-skill/.env.local`

Priority: `process env > .env.local > .env`

### Required env var

```bash
TIKOMNI_API_KEY="tk_xxx"
```

### Optional env vars

```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
TIKOMNI_CONFIG_FILE="skills/tikomni-skill/references/config-templates/defaults.yaml"
```

## Common Commands

```bash
# Readiness check
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# Generic extraction
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"

# Douyin homepage
python3 ./skills/tikomni-skill/scripts/run_douyin_extract.py "<douyin_url_or_id>"

# Xiaohongshu homepage
python3 ./skills/tikomni-skill/scripts/run_xiaohongshu_extract.py "<xhs_url_or_id>"
```

## Extension Notes

Extension points are under `skills/tikomni-skill/references/`:
- `routing-rules.md`
- `normalize-rules.md`
- `playbooks/`
- `config-templates/defaults.yaml`

## Security

- Never commit real secrets (`.env`, `.env.local`, CI secrets)
- Never print `TIKOMNI_API_KEY` in logs or markdown outputs
- In CI, disable command echo (`set +x`) before sourcing env files

## Core References

- [`skills/tikomni-skill/SKILL.md`](./skills/tikomni-skill/SKILL.md)
- [`skills/tikomni-skill/references/runtime-config.md`](./skills/tikomni-skill/references/runtime-config.md)
- [`skills/tikomni-skill/references/routing-rules.md`](./skills/tikomni-skill/references/routing-rules.md)
- [`skills/tikomni-skill/references/normalize-rules.md`](./skills/tikomni-skill/references/normalize-rules.md)
- [`skills/tikomni-skill/references/api-catalog/index.md`](./skills/tikomni-skill/references/api-catalog/index.md)
