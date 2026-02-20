# tikomni-skill

`tikomni-skill` is a direct API skill for AI agents. It calls Tikomni public APIs (`u1` + `u2`) at `https://api.tikomni.com` and writes process/results as Markdown artifacts.

Chinese version: `README.zh-CN.md`.

## About Tikomni Platform

1. Tikomni is a unified API platform for multi-platform social/content data access and AI-agent automation.
2. It supports 20+ platform domains through one API surface and one API key.
3. This skill helps agents route requests, run extraction flows, and persist outputs in `.md`.

Platform entry points:

1. Homepage: `https://tikomni.com`
2. Dashboard / signup: `https://app.tikomni.com`
3. API base URL: `https://api.tikomni.com`
4. API docs: `https://docs.tikomni.com`

## Coverage and Implemented Version

1. 20+ platform domains are available in `references/api-catalog`, including Douyin, Xiaohongshu, TikTok, YouTube, X/Twitter, Threads, Instagram, Weibo, Bilibili, Kuaishou, Zhihu, Reddit, LinkedIn, Lemon8, Pipixia, Toutiao, Xigua, WeChat MP, and WeChat Channels.
2. Catalog coverage means endpoint routing is available; fixed workflow playbooks are released incrementally.

`v0.1.0-direct` (2026-02-20):

1. Workflowized (GA): Douyin homepage extraction.
2. Workflowized (GA): Xiaohongshu homepage extraction.
3. Catalog-routable (Beta): other supported platforms through intent-to-endpoint routing.
4. Output contract: always write `run/result/error` markdown artifacts.
5. Execution model: agent-orchestrated direct HTTP calls (no standalone runtime package yet).

## Register and Get API Key

1. Open dashboard: `https://app.tikomni.com`
2. Sign up and verify your email.
3. Enter user dashboard and open the API key / API token menu.
4. Create an API key and save it immediately.
5. Add it to your local `.env`:

```bash
TIKOMNI_API_KEY="<your_api_key>"
```

## Configuration (User-Editable)

This skill is configurable. User-facing policies should be configured in reference docs, not hardcoded in prompts.

1. Env template: `skills/tikomni-skill/env.example` (copy first, then fill real key).
2. Environment variables: workspace `.env` or `skills/tikomni-skill/.env.local` (common in CI).
3. Runtime profile document: edit `skills/tikomni-skill/references/runtime-config.md`.
4. Configuration schema and instructions: `skills/tikomni-skill/references/configuration.md`.
5. Note: local CLI/CUI runs use your machine env as local config; CI runs use runner env as local config.
6. During execution, the skill first reads the runtime config document and applies user policies for output folders, markdown metadata, and extraction behavior.

## Natural-Language Skill Creation and Customization

1. Users can describe requirements in natural language and ask AI agents to install this skill directly from GitHub.
2. Users can describe custom platform functions in natural language, such as new endpoint routing, field normalization, fallback policy, and markdown schema.
3. Teams can maintain private forks for organization-specific workflows and contribute reusable capabilities back via PR.

Example prompts:

```text
Install tikomni-skill from <repo-url>/skills/tikomni-skill and run a smoke extraction.

Update runtime config at skills/tikomni-skill/references/runtime-config.md:
- output root to docs/my-project-output
- add tags: market=us, team=growth
- keep markdown artifact naming with job_id suffix.

Create a custom playbook for Bilibili author-home extraction and wire it to the catalog routing.
```

## Installation

### Recommended: Agent-first from GitHub

1. Send the repository URL to your AI agent.
2. Ask the agent to install from `skills/tikomni-skill`.
3. Ask the agent to run a smoke task.

### Codex / CodeX

1. Install from GitHub using Codex skill installer:

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

2. Optional URL-based install:

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --url "https://github.com/<owner>/<repo>/tree/<ref>/skills/tikomni-skill"
```

### Claude Code (local skills folder)

1. Copy the skill folder into Claude Code skills directory:

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

2. Start a new Claude Code session and ask it to use `tikomni-skill`.

### OpenClaw and Other Agent Tools

1. Preferred: provide the GitHub repository and ask the agent to auto-install `skills/tikomni-skill`.
2. Manual fallback: copy this folder into the tool's local skills directory and invoke by skill name `tikomni-skill`.

## Quick Start

1. Set `TIKOMNI_API_KEY` in `.env`.
2. Generate API catalog:

```bash
node "skills/tikomni-skill/scripts/generate-api-catalog.mjs"
```

3. Open catalog index:

```text
skills/tikomni-skill/references/api-catalog/index.md
```

4. Configure runtime profile:

```text
skills/tikomni-skill/references/runtime-config.md
```

## Contributing

1. PRs are welcome for new platform playbooks, field normalization rules, markdown templates, and regression samples.
2. Please open issues for feature proposals, routing policy changes, or extraction quality reports.
3. Keep EN/ZH docs semantically aligned when updating rules.

## Core References

1. `skills/tikomni-skill/SKILL.md`
2. `skills/tikomni-skill/references/configuration.md`
3. `skills/tikomni-skill/references/runtime-config.md`
4. `skills/tikomni-skill/references/routing-rules.md`
5. `skills/tikomni-skill/references/normalize-rules.md`
6. `skills/tikomni-skill/references/playbooks/douyin-home-extract.md`
7. `skills/tikomni-skill/references/playbooks/xiaohongshu-home-extract.md`
8. `skills/tikomni-skill/references/playbooks/copy-extract-rules.md`
9. `skills/tikomni-skill/references/output-markdown.md`
10. `skills/tikomni-skill/references/customization-guide.md`
