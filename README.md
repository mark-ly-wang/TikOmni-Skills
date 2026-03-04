# TikOmni Skills ✨

English | [中文说明 (README.zh-CN.md)](./README.zh-CN.md)

A production-ready skill package for AI agents to fetch structured data from major social platforms through TikOmni APIs.

## 🚀 What this repository is

This repository provides the `tikomni-skill` used by AI agents.

With this skill, agents can:
- collect cross-platform public content data
- normalize fields into consistent structured output
- generate markdown-ready extraction artifacts (for workflows and downstream analysis)

## 🌐 Official links

- Website: https://tikomni.com
- Sign up / Dashboard (get API key): https://app.tikomni.com
- API endpoint: https://api.tikomni.com
- API docs: https://docs.tikomni.com

## 📦 Supported platforms

Current catalog includes mainstream platforms such as:
- Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo
- TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn
- WeChat Channels, WeChat Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, Pipixia

(See full list in `skills/tikomni-skill/references/api-catalog/index.md`.)

## 🧩 What structured data you can get

Depending on platform and endpoint, the skill can return:
- author/account metadata
- post/video basic info
- engagement metrics (likes/comments/shares, etc. when available)
- subtitles/transcripts/copy text (when supported)
- routing and request trace metadata for reproducibility

## 🔧 Install this skill

Use the integration method matching your agent runtime.

### OpenClaw
Place this repo (or `skills/tikomni-skill`) in your OpenClaw workspace skills path, then let OpenClaw load the skill.

### Codex
Install/copy `skills/tikomni-skill` into your Codex skills directory.

### Claude Code
Install/copy `skills/tikomni-skill` into your Claude skills directory.

## ⚙️ Configure after installation (env-only)

TikOmni user configuration is **env-only**. You do not need to edit YAML.

Required:
```bash
TIKOMNI_API_KEY="your_real_key"
```

Optional advanced env vars (all have defaults):
```bash
# Runtime
TIKOMNI_TIMEOUT_MS="60000"

# Output directories
TIKOMNI_OUTPUT_ROOT="docs/skill-output"
TIKOMNI_OUTPUT_RUNS_DIR="_runs"
TIKOMNI_OUTPUT_RESULTS_DIR="results"
TIKOMNI_OUTPUT_ERRORS_DIR="_errors"

# Naming
TIKOMNI_FILENAME_PATTERN="{type}-{timestamp}-{job_id}.md"

# Card root (default: /mnt/openclaw/data/WIKI)
TIKOMNI_CARD_ROOT="/mnt/openclaw/data/WIKI"

# Card route locale preset (default zh)
TIKOMNI_PATH_LOCALE="zh"   # zh | en

# Explicit routes (highest priority, separator: |)
TIKOMNI_CARD_ROUTE_WORK="10-内容系统|15-对标研究|01-作品对标卡"
TIKOMNI_CARD_ROUTE_AUTHOR="10-内容系统|15-对标研究|03-作者对标卡"
TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK="10-内容系统|15-对标研究|02-作者样本集|{platform}-{author_slug}"
```

Route precedence:
1) `TIKOMNI_CARD_ROUTE_*` explicit env
2) `TIKOMNI_PATH_LOCALE` preset (`zh`/`en`, default `zh`)
3) built-in/default config

Recommended placement:
- `<repo_root>/.env` (project-level)
- `skills/tikomni-skill/.env.local` (local override)

## ▶️ How to use

Use the skill through natural-language requests in your AI agent, for example:
- “Extract Douyin homepage data for this URL.”
- “Get Xiaohongshu author posts and summarize key topics.”
- “Fetch video copy/subtitles and output structured markdown.”

## 🔐 Security

- Never commit real secrets (`.env`, `.env.local`, CI secrets)
- Never expose API keys in logs or output

## 📚 Core references

- Skill entry: [`skills/tikomni-skill/SKILL.md`](./skills/tikomni-skill/SKILL.md)
- API catalog: [`skills/tikomni-skill/references/api-catalog/index.md`](./skills/tikomni-skill/references/api-catalog/index.md)
