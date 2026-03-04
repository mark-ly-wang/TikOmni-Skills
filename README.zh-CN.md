# TikOmni Skills ✨

中文 | [English (README.md)](./README.md)

这是一个给 AI Agent 使用的 TikOmni Skill 仓库，用于从主流自媒体平台获取结构化数据。

## 🚀 这是什么仓库

本仓库提供 `tikomni-skill`。

它可以让 Agent：
- 跨平台抓取公开内容数据
- 统一字段结构，输出标准化结果
- 生成可用于后续流程的 Markdown 结构化产物

## 🌐 官方入口

- 官网：https://tikomni.com
- 注册/控制台（获取 API Key）：https://app.tikomni.com
- API 地址：https://api.tikomni.com
- API 文档：https://docs.tikomni.com

## 📦 支持平台

当前目录覆盖主流平台（示例）：
- 抖音、小红书、快手、B站、微博
- TikTok、YouTube、Instagram、Threads、Twitter/X、Reddit、LinkedIn
- 视频号、公众号、头条、西瓜、知乎、Lemon8、皮皮虾

完整列表见：`skills/tikomni-skill/references/api-catalog/index.md`

## 🧩 可获取哪些结构化数据

按不同平台/接口可返回：
- 作者/账号信息
- 作品/视频基础信息
- 互动指标（点赞、评论、分享等，视接口可用性）
- 字幕/转写/文案文本（接口支持时）
- 路由与请求追踪信息（方便复现）

## 🔧 如何安装本 Skill

按你的 Agent 运行环境安装即可。

### OpenClaw
把本仓库（或 `skills/tikomni-skill`）放到 OpenClaw 的 skills 目录，让系统加载。

### Codex
把 `skills/tikomni-skill` 复制到 Codex 的 skills 目录。

### Claude Code
把 `skills/tikomni-skill` 复制到 Claude Code 的 skills 目录。

## ⚙️ 安装后怎么配置（仅 env）

TikOmni 用户配置统一走 **环境变量**，不需要编辑 YAML。

必填：
```bash
TIKOMNI_API_KEY="你的真实 key"
```

高级可选（都有默认值）：
```bash
# 运行时
TIKOMNI_TIMEOUT_MS="60000"

# 输出目录
TIKOMNI_OUTPUT_ROOT="docs/skill-output"
TIKOMNI_OUTPUT_RUNS_DIR="_runs"
TIKOMNI_OUTPUT_RESULTS_DIR="results"
TIKOMNI_OUTPUT_ERRORS_DIR="_errors"

# 命名规则
TIKOMNI_FILENAME_PATTERN="{type}-{timestamp}-{job_id}.md"

# 卡片根目录（默认：/mnt/openclaw/data/WIKI）
TIKOMNI_CARD_ROOT="/mnt/openclaw/data/WIKI"

# 卡片目录语言预设（默认 zh）
TIKOMNI_PATH_LOCALE="zh"   # zh | en

# 显式路由（最高优先级，分隔符：|）
TIKOMNI_CARD_ROUTE_WORK="10-内容系统|15-对标研究|01-作品对标卡"
TIKOMNI_CARD_ROUTE_AUTHOR="10-内容系统|15-对标研究|03-作者对标卡"
TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK="10-内容系统|15-对标研究|02-作者样本集|{platform}-{author_slug}"
```

路由优先级：
1) 显式 `TIKOMNI_CARD_ROUTE_*`
2) `TIKOMNI_PATH_LOCALE` 预设（`zh`/`en`，默认 `zh`）
3) 内置/默认配置

推荐配置位置：
- `<repo_root>/.env`
- `skills/tikomni-skill/.env.local`（本地覆盖）

## ▶️ 怎么使用

在你的 AI Agent 里直接用自然语言下指令，例如：
- “提取这个抖音主页数据”
- “抓取这个小红书账号近 20 条并总结选题方向”
- “提取视频字幕/文案并输出结构化 markdown”

## 🔐 安全说明

- 不要把真实密钥提交到 Git（`.env`、`.env.local`、CI secrets）
- 不要在日志或输出中泄露 API Key

## 📚 核心参考

- Skill 入口：[`skills/tikomni-skill/SKILL.md`](./skills/tikomni-skill/SKILL.md)
- API 目录：[`skills/tikomni-skill/references/api-catalog/index.md`](./skills/tikomni-skill/references/api-catalog/index.md)
