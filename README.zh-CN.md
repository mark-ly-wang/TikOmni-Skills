# TikOmni Skills

中文 | [English](./README.md)

让 AI Agent 直接使用 TikOmni 的跨平台内容获取与结构化分析能力。

适用于 `Codex`、`Claude Code`、`OpenClaw`。  
面向内容抓取、单作品分析、创作者分析、搜索结果、评论线程、榜单、直播间和结构化结果产出。

- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API Docs: https://docs.tikomni.com
- Releases: https://github.com/mark-ly-wang/TikOmni-Skills/releases

## 为什么有这个仓库

`TikOmni-Skills` 是 TikOmni 面向 AI Agent 的 Skill 交付层。

它的目标不是堆一批平台脚本，也不只是沉淀几个固定模板；它更重要的作用，是把 TikOmni 的原能力组织成 Agent 可安装、可调用、可组合的 Skills，让 Agent 能直接完成：

- 获取单条内容、账号主页和内容集合
- 获取评论线程、搜索结果、榜单、直播间和商品页等具体对象
- 提取标题、文案、字幕、转写和结构化字段
- 输出标准化 JSON 与 Markdown 卡片
- 基于真实抓取结果继续做分析、总结和归档

如果你把 TikOmni 看作跨平台能力底座，这个仓库就是把这些能力交付给 Agent 的使用层。

## 📦 支持平台

当前目录覆盖主流平台（示例）：

- 抖音、小红书、快手、B站、微博
- TikTok、YouTube、Instagram、Threads、Twitter/X、Reddit、LinkedIn
- 视频号、公众号、头条、西瓜、知乎、Lemon8、皮皮虾

完整列表见官方文档目录：https://docs.tikomni.com

## 🧩 可获取哪些结构化数据

按不同平台/接口可返回：

- 作者/账号信息
- 作品/视频基础信息
- 评论与回复数据
- 搜索结果、榜单结果、直播间信息、商品相关数据
- 互动指标（点赞、评论、分享等，视接口可用性）
- 字幕/转写/文案文本（接口支持时）
- 媒体地址等可提取资源（接口支持时）
- 路由与请求追踪信息（方便复现）

## Skill 模块

| Skill | 作用 | 典型任务 |
| --- | --- | --- |
| `meta-capability` | 通用能力层 | 跨平台获取、路由探索、结构化抓取，以及评论线程、搜索、榜单、直播间、商品页等对象的通用执行与兜底 |
| `single-work-analysis` | 单作品专项 Skill | 单个视频、单篇笔记、单条帖子、单篇文章的提取与分析 |
| `creator-analysis` | 创作者专项 Skill | 账号主页、作者页、频道页、内容集合的抓取与聚合分析 |

选择建议：

- 想分析单个内容对象：安装 `single-work-analysis`
- 想分析账号主页或内容集合：安装 `creator-analysis`
- 想保留通用 TikOmni 能力入口：安装 `meta-capability`
- 不确定会用到哪些场景：直接安装 `all`

## 当前更成熟的高频链路

在通用能力层之上，本仓库已经沉淀出一批更适合直接复用的高频方案。

当前重点验证和持续打磨的方向包括：

- Douyin 单作品分析
- Xiaohongshu 单作品分析
- Douyin 创作者主页分析
- Xiaohongshu 创作者主页分析

这些链路代表当前最成熟、最适合直接上手的实践路径。  
它们很重要，但不等于本仓库能力边界的全部定义。

## 30 秒快速开始

### 1. 注册并获取 API Key

- 官网：https://tikomni.com
- 控制台：https://app.tikomni.com
- API 文档：https://docs.tikomni.com

### 2. 安装 Skills

如果 npm 包已发布，可以直接使用：

```bash
npx @tikomni/skills list
npx @tikomni/skills install codex all
npx @tikomni/skills install claude-code creator-analysis
npx @tikomni/skills install openclaw meta-capability --dir "/custom/skills"
```

默认安装目录：

- `codex` -> `$CODEX_HOME/skills`，默认 `~/.codex/skills`
- `claude-code` -> `~/.claude/skills`
- `openclaw` -> 优先 `~/.openclaw/workspace/skills`，否则 `~/.openclaw/skills`

如果你暂时不走 npm 分发，也可以手动把目标 Skill 目录复制到对应运行时的 `skills` 目录。

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

- “帮我把 TikOmni skills 全部安装到 Codex。”
- “把 `creator-analysis` 安装到 Claude Code 的 skills 目录。”
- “把 `meta-capability` 安装到 OpenClaw，目标目录是 `/custom/skills`。”

## 安装完成后怎么用

配置完成后，可以直接通过自然语言发起任务，例如：

- “提取这个抖音视频的结构化信息和字幕。”
- “分析这个小红书笔记，输出作品卡和内容拆解。”
- “抓取这个抖音主页近 20 条内容，并总结选题方向。”
- “分析这个小红书账号，输出作者画像和代表性内容特征。”
- “搜索这个关键词下的抖音结果，并整理前 20 条内容特征。”
- “获取这个直播间的信息并输出结构化摘要。”

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
