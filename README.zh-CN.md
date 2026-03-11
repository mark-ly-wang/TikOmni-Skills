# TikOmni Skills

中文 | [English](./README.md)

让 AI Agent 直接使用 TikOmni 的跨平台内容获取与结构化数据能力。

适用于 `Codex`、`Claude Code`、`OpenClaw`。  
面向内容抓取、结构化提取、ASR 文本获取、结构化 JSON 结果和事实卡落盘。

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com
- Releases: https://github.com/mark-ly-wang/TikOmni-Skills/releases

## 为什么有这个仓库

`TikOmni-Skills` 是 TikOmni 面向 AI Agent 的 Skill 交付层。

它的目标不是堆一批平台脚本，也不只是沉淀几个固定模板；更重要的是把 TikOmni 的原能力组织成 Agent 可安装、可调用、可组合的 Skill，让 Agent 能直接完成：

- 获取单条内容、账号主页和内容集合
- 获取评论线程、搜索结果、榜单、直播间和商品页等具体对象
- 提取标题、文案、字幕、转写和结构化字段
- 输出标准化 JSON 与事实卡
- 将结果继续接入归档、知识库或后续工作流

如果你把 TikOmni 看作跨平台能力底座，这个仓库就是把这些能力交付给 Agent 的使用层。

## 支持平台

当前能力覆盖主流平台（示例）：

- 抖音、小红书、快手、B站、微博
- TikTok、YouTube、Instagram、Threads、Twitter/X、Reddit、LinkedIn
- 视频号、公众号、头条、西瓜、知乎、Lemon8、皮皮虾

完整列表见官方文档目录：https://docs.tikomni.com

## 可获取哪些结构化数据

按不同平台和接口能力，可返回：

- 作者/账号信息
- 作品/视频基础信息
- 评论与回复数据
- 搜索结果、榜单结果、直播间信息、商品相关数据
- 互动指标（点赞、评论、收藏、分享等，视接口可用性）
- 字幕、转写、文案等文本字段（接口支持时）
- 媒体地址等可提取资源（接口支持时）
- 路由与请求追踪信息（方便复现和归档）

## 当前更成熟的固定 Pipeline

在这些通用能力之上，当前已经固定并重点验证了 4 条高频 pipeline：

- 抖音作品
- 抖音主页
- 小红书作品
- 小红书主页

这些固定 pipeline 是当前更成熟、可直接复用的高频链路。  
它们很重要，但不等于本仓库能力边界的全部定义。

## 对外 Skill

当前 npm 包对外公开的 Skill 为：

| Skill | 作用 |
| --- | --- |
| `social-media-crawl` | 跨平台结构化抓取、固定 pipeline、事实卡入库、MCP-first 通用调用 |

## 30 秒快速开始

### 1. 注册并获取 API Key

- 官网：https://tikomni.com
- 控制台：https://app.tikomni.com
- API 文档：https://docs.tikomni.com

### 2. 安装 Skills

使用 npm 直接安装。

先查看当前可安装的 Skills：

```bash
npx @tikomni/skills list
```

当前 npm 包对外提供 `social-media-crawl`。

安装到 Codex：

```bash
# 安装公开 Skill
npx @tikomni/skills install codex all

# 显式安装同一个 Skill
npx @tikomni/skills install codex social-media-crawl
```

默认目录：`$CODEX_HOME/skills`，默认值 `~/.codex/skills`

安装到 Claude Code：

```bash
# 安装公开 Skill
npx @tikomni/skills install claude-code all

# 显式安装同一个 Skill
npx @tikomni/skills install claude-code social-media-crawl
```

默认目录：`~/.claude/skills`

安装到 OpenClaw：

```bash
# 安装公开 Skill
npx @tikomni/skills install openclaw all

# 安装到自定义目录
npx @tikomni/skills install openclaw social-media-crawl --dir "/custom/skills"
```

默认目录：优先 `~/.openclaw/workspace/skills`，否则 `~/.openclaw/skills`

常用参数：

- `--dir <path>`：显式指定目标 `skills` 目录
- `--force`：覆盖已存在的同名 Skill 目录

如果你不想使用 npm，也可以手动把目标 Skill 目录复制到对应运行时的 `skills` 目录。

### 3. 配置环境变量

推荐做法：

- CLI 安装后，目标 `skills` 根目录会自带一份共享 [`env.example`](./env.example)
- 把这份 `skills/env.example` 复制为 `skills/.env`
- 如有局部覆盖需求，再在对应 Skill 目录下增加 `.env.local`

最少需要配置：

```bash
TIKOMNI_API_KEY="your_real_key"
TIKOMNI_OUTPUT_ROOT="/absolute/path/to/tikomni-output"
TIKOMNI_CARD_ROOT="/absolute/path/to/tikomni-cards"
```

更多高级变量见 [`env.example`](./env.example)。

## 也可以直接让 Agent 帮你安装

除了手动执行命令，你也可以直接对 Agent 说：

- “把 `social-media-crawl` 安装到 Codex。”
- “把 `social-media-crawl` 安装到 Claude Code 的 skills 目录。”
- “把 `social-media-crawl` 安装到 OpenClaw，目标目录是 `/custom/skills`。”

## 安装完成后怎么用

配置完成后，可以直接通过自然语言发起任务，例如：

- “提取这个抖音视频的结构化字段和主文本。”
- “抓取这个小红书作品并写入事实卡。”
- “抓取这个主页的作品并持续入库到作者目录。”
- “通过 TikOmni MCP 获取这个评论线程并输出标准 JSON。”
- “通过 TikOmni MCP 获取搜索或榜单结果，并保持结构化返回。”

## 版本与发布

当前包版本见 [`package.json`](./package.json)。

更多版本与发布信息见：

- [Releases](https://github.com/mark-ly-wang/TikOmni-Skills/releases)
- [`RELEASING.md`](./RELEASING.md)
- [`RELEASING.zh-CN.md`](./RELEASING.zh-CN.md)

## 安全说明

- 不要把真实 API Key 提交到 Git
- 不要在日志、截图或产物中泄露敏感配置
- 建议使用 `.env` / `.env.local` 管理本地密钥

## 相关链接

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API: https://api.tikomni.com
- Docs: https://docs.tikomni.com
- Issues: https://github.com/mark-ly-wang/TikOmni-Skills/issues
