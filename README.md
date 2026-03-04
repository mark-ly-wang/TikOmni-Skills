# tikomni-skill

`tikomni-skill` is a direct API skill for AI agents.
It calls Tikomni public APIs (`u1` + `u2`) and writes run/result/error artifacts as Markdown.

🌐 中文版: [README.zh-CN.md](./README.zh-CN.md)

## Platform

1. Homepage: [tikomni.com](https://tikomni.com)
2. Dashboard / Signup: [app.tikomni.com](https://app.tikomni.com)
3. API Base URL: [api.tikomni.com](https://api.tikomni.com)
4. API Docs: [docs.tikomni.com](https://docs.tikomni.com)

## Coverage

- 20+ platform domains are catalog-covered.
- Fixed playbooks are currently GA for Douyin homepage and Xiaohongshu homepage extraction.
- Other domains are routed by catalog intent matching.

## Docs Navigation

- Chinese reference docs: [`docs/zh/references/`](./docs/zh/references/)
- Stage notes: [`docs/notes/`](./docs/notes/)

## Configuration

### 1) Copy env template first

```bash
cp ./skills/tikomni-skill/env.example ./.env
# or
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local
```

Then replace example values with real values.

### 2) Three key sources and priority

`TIKOMNI_API_KEY` is loaded from three sources with deterministic precedence:

1. process env (highest)
2. `skills/tikomni-skill/.env.local`
3. `<repo_root>/.env`

Priority rule: `process env > .env.local > .env`.

Path semantics:
- Default `.env` is always resolved as `<repo_root>/.env` (not CWD-dependent).
- If `--env-file` or `runtime.env_file` is relative, it is resolved from `<repo_root>`.

### 3) Path configuration

- Skill root: `<workspace_root>/skills/tikomni-skill`
- Runtime config template: `skills/tikomni-skill/references/config-templates/defaults.yaml`
- Runtime config docs:
  - EN: `skills/tikomni-skill/references/runtime-config.md`
  - ZH: `docs/zh/references/runtime-config.zh-CN.md`

### 4) Important env variables

- `TIKOMNI_API_KEY` (required)
- `TIKOMNI_BASE_URL` (optional, default `https://api.tikomni.com`)
- `TIKOMNI_TIMEOUT_MS` (optional, default `60000`)
- `TIKOMNI_CONFIG_FILE` (optional runtime config YAML path)

## Installation

### Agent-first from GitHub (recommended)

1. Ask your agent to install from `skills/tikomni-skill`.
2. Run one smoke extraction.

### Codex / CodeX

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

### Claude Code

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

## Quick Start

```bash
# 1) set key via one of the supported sources
export TIKOMNI_API_KEY="tk_example_123"

# 2) check readiness (prints source only, never prints secret)
python3 "./skills/tikomni-skill/scripts/check_tikomni_readiness.py"

# 3) generate API catalog
node "./skills/tikomni-skill/scripts/generate-api-catalog.mjs"

# 4) run extractor
python3 "./skills/tikomni-skill/scripts/run_tikomni_extract.py" "<url_or_id>"
```

## Core References

1. [skills/tikomni-skill/SKILL.md](./skills/tikomni-skill/SKILL.md)
2. [configuration.md](./skills/tikomni-skill/references/configuration.md)
3. [runtime-config.md](./skills/tikomni-skill/references/runtime-config.md)
4. [routing-rules.md](./skills/tikomni-skill/references/routing-rules.md)
5. [normalize-rules.md](./skills/tikomni-skill/references/normalize-rules.md)
6. [API catalog index](./skills/tikomni-skill/references/api-catalog/index.md)
