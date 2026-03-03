# Configuration Guide

This document defines where users configure this skill.

## 0. What does “local config” mean?

1. Local means the environment where your agent is running now.
2. If you run from CLI/CUI on your laptop, local means your laptop.
3. If you run from CI, local means that CI runner.

## 1. Configuration Sources

1. `.env` in the current workspace for secrets and runtime environment (most common).
2. `skills/tikomni-skill/references/runtime-config.md` for user-facing execution policy.
3. Env template file: `skills/tikomni-skill/env.example` (no real secret inside).
4. Script runtime template: `skills/tikomni-skill/references/config-templates/defaults.yaml` (internal default, maintainers/advanced users only).
5. Optional: user can provide another config file path in prompt, and the agent should read that file first.

## 2. Required `.env` Variables

```bash
TIKOMNI_API_KEY="<required>"
```

Optional:

```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
```

## 3. Recommended File Layout

1. `./.env`: your private local config.
2. `skills/tikomni-skill/env.example`: env template.
3. `skills/tikomni-skill/references/runtime-config.md`: runtime policy config.

## 4. CI Loading Without Leaking Logs

When loading env files in CI/scripts, disable command echo:

```bash
set +x
set -a
source "skills/tikomni-skill/.env.local"
set +a
```

Notes:

1. `set +x` prevents secret values from being echoed into logs.
2. `skills/tikomni-skill/.env.local` should never be committed.

## 5. Runtime Config Contract

`runtime-config.md` is the policy document for this skill. It should include these sections:

1. API runtime settings (base URL, auth env key, timeout).
2. Output folder strategy (root directory and sub-directory names).
3. Markdown metadata defaults (tags, title prefix, language).
4. Feature toggles and extraction policy (batch behavior, transcript strategy, and `asr_strategy.u2_timeout_retry` timeout-only retry switch with `max_retries` range `0~3`).
5. Routing/fallback policy overrides (when user wants custom behavior).
6. U2 submit does not use `idempotency-key` headers anymore.

## 6. Script Config Loader (Phase 1 Skeleton)

`skills/tikomni-skill/scripts/config_loader.py` path priority is fixed:

1. `--config <path>`
2. `TIKOMNI_CONFIG_FILE`
3. `skills/tikomni-skill/references/config-templates/defaults.yaml`

Risk-closure behavior:

1. PyYAML missing does **not** hard-fail script execution.
2. Built-in Python defaults are always available as fallback.
3. If config file read/parse fails, loader gracefully falls back to built-in defaults.

Supported CLI scripts:

1. `scripts/run_tikomni_extract.py`
2. `scripts/run_douyin_extract.py`
3. `scripts/run_xiaohongshu_extract.py`

## 7. Agent Execution Rule

1. Before calling any endpoint, read `runtime-config.md` (or user-specified config path).
2. Use runtime config values as first-class input to routing/extraction/output decisions.
3. If config is missing or incomplete, ask user to confirm fallback values before execution.
