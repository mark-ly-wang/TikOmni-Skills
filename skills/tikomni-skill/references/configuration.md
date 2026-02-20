# Configuration Guide

This document defines where users configure this skill.

## 0. What does “local config” mean?

1. Local means the environment where your agent is running now.
2. If you run from CLI/CUI on your laptop, local means your laptop.
3. If you run from CI, local means that CI runner.

## 1. Configuration Sources

1. `.env` in the current workspace for secrets and runtime environment (most common).
2. `skills/tikomni-skill/references/runtime-config.md` for user-facing execution policy.
3. Optional: user can provide another config file path in prompt, and the agent should read that file first.
4. Env template file: `skills/tikomni-skill/env.example` (no real secret inside).

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
4. Feature toggles and extraction policy (batch behavior, transcript strategy).
5. Routing/fallback policy overrides (when user wants custom behavior).

## 6. Agent Execution Rule

1. Before calling any endpoint, read `runtime-config.md` (or user-specified config path).
2. Use runtime config values as first-class input to routing/extraction/output decisions.
3. If config is missing or incomplete, ask user to confirm fallback values before execution.
