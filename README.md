# TikOmni Skills

English | [中文](./README.zh-CN.md)

Give AI agents direct access to TikOmni's cross-platform content retrieval and structured analysis capabilities.

Works with `Codex`, `Claude Code`, and `OpenClaw`.  
Built for content extraction, single-work analysis, creator analysis, search results, comment threads, rankings, livestreams, and structured outputs.

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com
- Releases: https://github.com/mark-ly-wang/TikOmni-Skills/releases

## Why This Repo Exists

`TikOmni-Skills` is the agent-facing delivery layer for TikOmni skills.

Its purpose is not to be a pile of platform scripts or a few fixed templates. More importantly, it packages TikOmni's core capabilities into installable, composable skills so agents can directly:

- retrieve single content items, creator pages, and content collections
- retrieve comment threads, search results, rankings, livestreams, and product pages as concrete platform objects
- extract titles, captions, subtitles, transcripts, and structured fields
- generate normalized JSON outputs and Markdown cards
- continue with analysis, summaries, and downstream knowledge workflows

If TikOmni is the cross-platform capability layer, this repository is the layer that makes those capabilities usable by agents.

## Supported Platforms

Current coverage includes mainstream platforms such as:

- Douyin, Xiaohongshu, Kuaishou, Bilibili, Weibo
- TikTok, YouTube, Instagram, Threads, Twitter/X, Reddit, LinkedIn
- WeChat Channels, WeChat Official Accounts, Toutiao, Xigua, Zhihu, Lemon8, Pipixia

For the full catalog, see https://docs.tikomni.com

## What Structured Data You Can Get

Depending on the platform and endpoint, the skills can return:

- author or account metadata
- post or video basic information
- comments and replies
- search results, ranking results, livestream information, and commerce-related data
- engagement metrics such as likes, comments, and shares when available
- subtitles, transcripts, or caption text when supported
- extractable media URLs and related assets when supported
- route and request trace metadata for reproducibility

## Skill Modules

| Skill | Role | Typical tasks |
| --- | --- | --- |
| `meta-capability` | General capability layer | Cross-platform retrieval, route discovery, structured extraction, plus generic execution and fallback for comment threads, search, rankings, livestreams, product pages, and other supported objects |
| `single-work-analysis` | Single-work specialist skill | Extracting and analyzing one video, note, post, or article |
| `creator-analysis` | Creator specialist skill | Collecting and analyzing creator pages, channels, and content collections |

Suggested choices:

- Want to analyze one content item: install `single-work-analysis`
- Want to analyze a creator page or content collection: install `creator-analysis`
- Want to keep a general TikOmni entry point available: install `meta-capability`
- Not sure which one you need yet: install `all`

## More Mature High-Frequency Flows

On top of the general capability layer, this repository already includes a set of more reusable high-frequency flows.

Current areas with the most validation and ongoing iteration include:

- Douyin single-work analysis
- Xiaohongshu single-work analysis
- Douyin creator-page analysis
- Xiaohongshu creator-page analysis

These flows represent the most mature and easiest-to-adopt paths today.  
They matter, but they do not define the full capability boundary of this repository.

## 30-Second Quick Start

### 1. Sign up and get an API key

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com

### 2. Install skills

Install directly from npm.

First, list the currently available skills:

```bash
npx @tikomni/skills list
```

Install into Codex:

```bash
# Install all skills
npx @tikomni/skills install codex all

# Install one specific skill
npx @tikomni/skills install codex single-work-analysis
```

Default target: `$CODEX_HOME/skills`, default `~/.codex/skills`

Install into Claude Code:

```bash
# Install all skills
npx @tikomni/skills install claude-code all

# Install only the creator-analysis skill
npx @tikomni/skills install claude-code creator-analysis
```

Default target: `~/.claude/skills`

Install into OpenClaw:

```bash
# Install all skills
npx @tikomni/skills install openclaw all

# Install into a custom directory
npx @tikomni/skills install openclaw meta-capability --dir "/custom/skills"
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

- "Install all TikOmni skills into Codex."
- "Install `creator-analysis` into the Claude Code skills directory."
- "Install `meta-capability` into OpenClaw and use `/custom/skills` as the target directory."

## How to Use It After Installation

Once configured, you can trigger tasks in natural language, for example:

- "Extract the structured fields and subtitles from this Douyin video."
- "Analyze this Xiaohongshu note and output a work card plus a content breakdown."
- "Fetch the latest 20 posts from this Douyin creator page and summarize topic patterns."
- "Analyze this Xiaohongshu account and output a creator profile with representative content traits."
- "Search this keyword on Douyin and summarize the top 20 result patterns."
- "Fetch this livestream's information and return a structured summary."

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
