# TikOmni Skills

English | [中文](./README.zh-CN.md)

Give AI agents direct access to TikOmni's cross-platform content retrieval and structured data capabilities.

Works with `Codex`, `Claude Code`, and `OpenClaw`.  
Built for content retrieval, structured extraction, ASR text acquisition, structured JSON output, and fact-card persistence.

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com
- Releases: https://github.com/mark-ly-wang/TikOmni-Skills/releases

## Why This Repo Exists

`TikOmni-Skills` is the agent-facing delivery layer for TikOmni.

Its purpose is not to be a pile of platform scripts or just a few fixed templates. More importantly, it packages TikOmni's core capabilities into installable, composable skills so agents can directly:

- retrieve single content items, creator pages, and content collections
- retrieve comment threads, search results, rankings, livestreams, and product pages as concrete objects
- extract titles, captions, subtitles, transcripts, and structured fields
- generate normalized JSON outputs and fact cards
- pass results into archives, knowledge workflows, or downstream systems

If TikOmni is the cross-platform capability layer, this repository is the layer that makes those capabilities usable by agents.

## Supported Platforms

Current coverage includes mainstream platforms such as:

- Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo
- TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn
- WeChat Channels, WeChat Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, Pipixia

For the full catalog, see https://docs.tikomni.com

## What Structured Data You Can Get

Depending on platform and endpoint coverage, the skill can return:

- author or account metadata
- post or video basic information
- comments and replies
- search results, ranking results, livestream information, and commerce-related data
- engagement metrics such as likes, comments, collects, and shares when available
- subtitles, transcripts, and caption text when supported
- extractable media URLs and related assets when supported
- route and request trace metadata for reproducibility

## More Mature Fixed Pipelines

On top of those general capabilities, the repository currently freezes and validates four high-frequency pipelines:

- Douyin single work
- Douyin creator home
- Xiaohongshu single work
- Xiaohongshu creator home

These fixed pipelines are currently the most mature and easiest-to-reuse flows.  
They matter, but they do not define the full capability boundary of this repository.

## Public Skill

The npm package currently exposes:

| Skill | Role |
| --- | --- |
| `social-media-crawl` | Cross-platform structured crawling, fixed pipelines, fact-card persistence, and MCP-first generic retrieval |

## 30-Second Quick Start

### 1. Sign up and get an API key

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com

### 2. Install skills

Before installation, prepare:

- `Node.js >= 18`
- `Python 3`

Common setup commands:

macOS (Homebrew):

```bash
# If Homebrew is not installed yet:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install node
brew install python

node -v
npm -v
python3 --version
```

Linux (Ubuntu / Debian; also works in WSL):

```bash
sudo apt update
sudo apt install -y curl python3 python3-pip

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

nvm install --lts

node -v
npm -v
python3 --version
```

Windows (PowerShell):

```powershell
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Python.Python.3

node -v
npm -v
python --version
```

After that, install directly from npm.

First, list the currently available skills:

```bash
npx @tikomni/skills list
```

This package currently exposes `social-media-crawl`.

Install into Codex:

```bash
# Install the public skill
npx @tikomni/skills install codex all

# Equivalent explicit install
npx @tikomni/skills install codex social-media-crawl
```

Default target: `$CODEX_HOME/skills`, default `~/.codex/skills`

Install into Claude Code:

```bash
# Install the public skill
npx @tikomni/skills install claude-code all

# Equivalent explicit install
npx @tikomni/skills install claude-code social-media-crawl
```

Default target: `~/.claude/skills`

Install into OpenClaw:

```bash
# Install the public skill
npx @tikomni/skills install openclaw all

# Install into a custom directory
npx @tikomni/skills install openclaw social-media-crawl --dir "/custom/skills"
```

Default target: prefers `~/.openclaw/workspace/skills`, otherwise `~/.openclaw/skills`

Common flags:

- `--dir <path>`: override the target `skills` directory
- `--force`: overwrite an existing installed skill directory

If you do not want to use npm, you can also copy the target skill folder into the runtime's `skills` directory manually.

### 3. Configure environment variables

Recommended workflow:

- after CLI installation, the target `skills` root includes a shared [`env.example`](./env.example)
- copy `skills/env.example` to `skills/.env`
- add `.env.local` inside a specific skill only when that skill needs a local override

Minimum required config:

```bash
TIKOMNI_API_KEY="your_real_key"
TIKOMNI_OUTPUT_ROOT="/absolute/path/to/tikomni-output"
TIKOMNI_CARD_ROOT="/absolute/path/to/tikomni-cards"
```

For advanced variables, see [`env.example`](./env.example).

## You Can Also Ask Your Agent to Install It

Instead of running commands manually, you can ask your agent directly:

- "Install `social-media-crawl` into Codex."
- "Install `social-media-crawl` into the Claude Code skills directory."
- "Install `social-media-crawl` into OpenClaw and use `/custom/skills` as the target directory."

## How to Use It After Installation

Once configured, you can trigger tasks in natural language, for example:

- "Extract the structured fields and primary text from this Douyin video."
- "Fetch this Xiaohongshu note and write a fact card."
- "Collect works from this creator home and persist them into the author archive."
- "Use TikOmni MCP to fetch a comment thread and return normalized JSON."
- "Use TikOmni MCP to fetch search or ranking results and keep the output structured."

## Versioning and Releases

The current package version is declared in [`package.json`](./package.json).

For release and version details, see:

- [Releases](https://github.com/mark-ly-wang/TikOmni-Skills/releases)
- [`RELEASING.md`](./RELEASING.md)
- [`RELEASING.zh-CN.md`](./RELEASING.zh-CN.md)

## Security

- Never commit real API keys to Git
- Never expose sensitive config in logs, screenshots, or outputs
- Prefer `.env` and `.env.local` for local secret management

## Links

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API: https://api.tikomni.com
- Docs: https://docs.tikomni.com
- Issues: https://github.com/mark-ly-wang/TikOmni-Skills/issues
