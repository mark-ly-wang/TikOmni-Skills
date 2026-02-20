# tikomni-skill

`tikomni-skill` is a direct API skill for AI agents.  
It calls Tikomni public APIs (`u1` + `u2`) and writes process/results as Markdown artifacts.

🌐 中文版: [README.zh-CN.md](./README.zh-CN.md)

## ✨ About Tikomni Platform

1. Tikomni is a unified API platform for multi-platform social/content data access and AI-agent automation.
2. It supports 20+ platform domains through one API surface and one API key.
3. This skill helps agents route requests, run extraction flows, and persist outputs in `.md`.

Platform entry:

1. Homepage: [tikomni.com](https://tikomni.com)
2. Dashboard / Signup: [app.tikomni.com](https://app.tikomni.com)
3. API Base URL: [api.tikomni.com](https://api.tikomni.com)
4. API Docs: [docs.tikomni.com](https://docs.tikomni.com)

## 🚧 Coverage and Current Version

1. 20+ platform domains are covered, including Douyin, Xiaohongshu, TikTok, YouTube, X/Twitter, Threads, Instagram, Weibo, Bilibili, Kuaishou, Zhihu, Reddit, LinkedIn, Lemon8, Pipixia, Toutiao, Xigua, WeChat MP, and WeChat Channels.
2. Catalog coverage means endpoint routing is available; fixed workflow playbooks are released incrementally.

`v0.1.0-direct` (2026-02-20):

1. Workflowized (GA): Douyin homepage extraction.
2. Workflowized (GA): Xiaohongshu homepage extraction.
3. Catalog-routable (Beta): other supported platforms through intent-to-endpoint routing.
4. Output contract: always write `run/result/error` markdown artifacts.

## 🔑 Register and Get API Key

1. Open dashboard: [app.tikomni.com](https://app.tikomni.com)
2. Sign up and verify email.
3. Open API key / API token menu.
4. Create API key and save immediately.
5. Add key into local env:

```bash
TIKOMNI_API_KEY="<your_api_key>"
```

## ⚙️ Configuration (User Editable)

1. Env template: [`./env.example`](./env.example)
2. Local env file: workspace `.env` or `./.env.local`
3. Runtime config: [`./references/runtime-config.md`](./references/runtime-config.md)
4. Config guide: [`./references/configuration.md`](./references/configuration.md)
5. In execution, the skill reads runtime config first, then applies output/metadata/policy settings.

## 🤖 Natural-Language Customization

You can ask AI agents to install and customize this skill using natural language.

Example:

```text
Install tikomni-skill from <repo-url>/skills/tikomni-skill and run a smoke extraction.

Update ./references/runtime-config.md:
- output root to docs/my-project-output
- add tags: market=us, team=growth
```

## 📦 Installation

### Recommended: Agent-first from GitHub

1. Send repo URL to your AI agent.
2. Ask it to install from `skills/tikomni-skill`.
3. Ask it to run one smoke task.

### Codex / CodeX

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

Optional URL install:

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --url "https://github.com/<owner>/<repo>/tree/<ref>/skills/tikomni-skill"
```

### Claude Code

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

## 🚀 Quick Start

1. Set `TIKOMNI_API_KEY` in `.env`
2. Generate catalog:

```bash
node "./scripts/generate-api-catalog.mjs"
```

3. Open catalog index: [./references/api-catalog/index.md](./references/api-catalog/index.md)
4. Edit runtime profile: [./references/runtime-config.md](./references/runtime-config.md)

## 🤝 Contributing

1. PRs welcome for playbooks, normalization rules, markdown templates, and regression samples.
2. Issues welcome for feature proposals and extraction quality reports.
3. Keep EN/ZH docs semantically aligned.

## 📚 Core References

1. [SKILL.md](./SKILL.md)
2. [configuration.md](./references/configuration.md)
3. [runtime-config.md](./references/runtime-config.md)
4. [routing-rules.md](./references/routing-rules.md)
5. [normalize-rules.md](./references/normalize-rules.md)
6. [douyin-home-extract.md](./references/playbooks/douyin-home-extract.md)
7. [xiaohongshu-home-extract.md](./references/playbooks/xiaohongshu-home-extract.md)
8. [copy-extract-rules.md](./references/playbooks/copy-extract-rules.md)
9. [output-markdown.md](./references/output-markdown.md)
10. [customization-guide.md](./references/customization-guide.md)
