# TikOmni Skills ✨

English | [中文说明 (README.zh-CN.md)](./README.zh-CN.md)

A production-ready skill package for AI agents to fetch structured data from major social platforms through TikOmni APIs.

## 🚀 What this repository is

This repository provides the split TikOmni skill modules used by AI agents:
- `skills/meta-capability`
- `skills/single-work-analysis`
- `skills/creator-analysis`

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

(See the official docs catalog at https://docs.tikomni.com.)

## 🧩 What structured data you can get

Depending on platform and endpoint, the skill can return:
- author/account metadata
- post/video basic info
- engagement metrics (likes/comments/shares, etc. when available)
- subtitles/transcripts/copy text (when supported)
- routing and request trace metadata for reproducibility

## ✅ Currently available capabilities (human-facing)

> Practical feature scope you can use right now:

### 0) Skill modules currently in this repo
- `skills/meta-capability`: generic TikOmni exploration and execution guidance for agents
- `skills/single-work-analysis`: single-work analysis module for current Douyin / Xiaohongshu implementations
- `skills/creator-analysis`: creator-analysis module for current Douyin / Xiaohongshu implementations

### 1) Douyin / Xiaohongshu single-content analysis
- Single video/note extraction: title, author, publish time, engagement basics, etc.
- Text layer: subtitle/copy extraction when supported by upstream endpoints
- Output: normalized structured result + reusable work card

### 2) Douyin / Xiaohongshu author-home analysis
- Author-level collection and analysis from homepage content (latest-first pagination)
- Default behavior: full fetch with a cap of 200 items unless explicitly specified otherwise
- Output:
  - per-work card collection
  - author profile (nickname, platform id, IP location, fans/likes/collections, bio, avatar, work count, etc.)
  - business analysis + benchmark analysis

### 3) General capabilities
- Cross-platform normalization into a consistent schema
- Workflow-friendly outputs for strategy review, benchmarking, and knowledge capture
- Traceable metadata for troubleshooting and reproducibility

## 🔧 Install this skill

Use the integration method matching your agent runtime.

### CLI installer (`npx`)
After publishing this package to npm, you can install skills directly with:

```bash
npx @tikomni/skills list
npx @tikomni/skills install codex all
npx @tikomni/skills install claude-code creator-analysis
npx @tikomni/skills install openclaw meta-capability --dir "/custom/skills"
```

Default install targets:
- `codex` -> `$CODEX_HOME/skills` or `~/.codex/skills`
- `claude-code` -> `~/.claude/skills`
- `openclaw` -> prefers `~/.openclaw/workspace/skills`, otherwise `~/.openclaw/skills`

Optional flags:
- `--dir <path>`: override the target skills directory
- `--force`: overwrite an existing installed skill directory

Distribution note:
- `npx` installs from the npm registry package, not by cloning this GitHub repository at install time.
- GitHub is the source repo; npm is the distribution channel for end-user installation.

### OpenClaw
Place this repo (or one of the skill folders under `skills/`) in your OpenClaw workspace skills path, then let OpenClaw load the skill.

### Codex
Install/copy the target skill folder into your Codex skills directory.

### Claude Code
Install/copy the target skill folder into your Claude skills directory.

### Local development
Before the npm package is published, you can run the installer locally:

```bash
node bin/tikomni-skills.js list
node bin/tikomni-skills.js install codex meta-capability --dir "/tmp/tikomni-skills"
```

### Publishing
Release notes and publish steps live in [`RELEASING.md`](./RELEASING.md).

## ⚙️ Configure after installation (env-only)

TikOmni user configuration is **env-only**. You do not need to edit YAML.

Recommended workflow:
- copy the repo-root [`env.example`](./env.example) to `skills/.env`
- add `.env.local` inside a specific skill only when that skill needs a local override

Required:
```bash
TIKOMNI_API_KEY="your_real_key"
# required absolute path
TIKOMNI_OUTPUT_ROOT="/absolute/path/to/tikomni-output"
# required absolute path
TIKOMNI_CARD_ROOT="/absolute/path/to/tikomni-cards"
```

Optional advanced env vars:
```bash
# Runtime
TIKOMNI_TIMEOUT_MS="60000"

# Output subdirectories under TIKOMNI_OUTPUT_ROOT
# defaults: _runs / results / _errors
TIKOMNI_OUTPUT_RUNS_DIR="_runs"
TIKOMNI_OUTPUT_RESULTS_DIR="results"
TIKOMNI_OUTPUT_ERRORS_DIR="_errors"

# Naming
TIKOMNI_FILENAME_PATTERN_CARD="{prefix}-{author_slug}-{title_slug}{ext}"
TIKOMNI_FILENAME_PATTERN_JSON="{timestamp}-{platform}-{identifier}{ext}"

# Card route locale preset (default zh)
TIKOMNI_PATH_LOCALE="zh"   # zh | en

# Card prefixes
TIKOMNI_CARD_PREFIX_WORK="CBV"
TIKOMNI_CARD_PREFIX_AUTHOR="CBA"
TIKOMNI_CARD_PREFIX_AUTHOR_SAMPLE_WORK="CBV"

# Explicit routes (highest priority, separator: |)
TIKOMNI_CARD_ROUTE_WORK="content-system|benchmark|work-cards"
TIKOMNI_CARD_ROUTE_AUTHOR="content-system|benchmark|author-cards"
TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK="content-system|benchmark|author-sample-cards|{platform}-{author_slug}"
```

Route precedence:
1) `TIKOMNI_CARD_ROUTE_*` explicit env
2) `TIKOMNI_PATH_LOCALE` preset (`zh`/`en`, default `zh`)
3) built-in/default config

Recommended placement:
- `<skills_root>/.env` (shared config)
- `<skill_root>/.env.local` (local override)

For split modules, the same pattern applies:
- shared env at the skills root
- optional per-skill override in each skill folder's `.env.local`

## ▶️ How to use

Use the skill through natural-language requests in your AI agent, for example:
- “Extract Douyin homepage data for this URL.”
- “Get Xiaohongshu author posts and summarize key topics.”
- “Fetch video copy/subtitles and output structured markdown.”

## 🔐 Security

- Never commit real secrets (`.env`, `.env.local`, CI secrets)
- Never expose API keys in logs or output

## 📚 Core references

- Meta capability: [`skills/meta-capability/SKILL.md`](./skills/meta-capability/SKILL.md)
- Single work analysis: [`skills/single-work-analysis/SKILL.md`](./skills/single-work-analysis/SKILL.md)
- Creator analysis: [`skills/creator-analysis/SKILL.md`](./skills/creator-analysis/SKILL.md)
- API docs: https://docs.tikomni.com
