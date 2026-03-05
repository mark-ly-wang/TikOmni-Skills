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

## ✅ 当前已可用能力（面向用户）

> 以下是当前可直接使用的功能范围（持续更新）：

### 1) 抖音 / 小红书单作品分析
- 单视频（或单笔记）提取：标题、作者、发布时间、互动数据等基础信息
- 文本能力：字幕/文案提取（接口支持时）
- 产出：标准化结构结果 + 作品卡（便于复盘、对标、沉淀）

### 2) 抖音 / 小红书作者主页分析
- 支持作者维度抓取与分析（按最新内容进行分页拉取）
- 默认全量抓取，上限 200 条（未特别指定时）
- 产出：
  - 单作品卡合集（逐条作品）
  - 作者画像信息（昵称、平台ID、IP属地、粉丝/获赞/收藏、签名、头像、作品数等）
  - 作者商业分析 + 对标分析

### 3) 通用能力
- 跨平台统一字段与结构化输出
- 结果可用于后续工作流（策略分析、内容复盘、知识沉淀）
- 输出包含可追踪元信息，便于排查与复现

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
# 必填绝对路径
TIKOMNI_OUTPUT_ROOT="/absolute/path/to/tikomni-output"
# 必填绝对路径
TIKOMNI_CARD_ROOT="/absolute/path/to/tikomni-cards"
```

高级可选：
```bash
# 运行时
TIKOMNI_TIMEOUT_MS="60000"

# 输出根目录下的子目录
# 默认值：_runs / results / _errors
TIKOMNI_OUTPUT_RUNS_DIR="_runs"
TIKOMNI_OUTPUT_RESULTS_DIR="results"
TIKOMNI_OUTPUT_ERRORS_DIR="_errors"

# 命名规则
TIKOMNI_FILENAME_PATTERN="{type}-{timestamp}-{job_id}.md"

# 卡片目录语言预设（默认 zh）
TIKOMNI_PATH_LOCALE="zh"   # zh | en

# 显式路由（最高优先级，分隔符：|）
TIKOMNI_CARD_ROUTE_WORK="content-system|benchmark|work-cards"
TIKOMNI_CARD_ROUTE_AUTHOR="content-system|benchmark|author-cards"
TIKOMNI_CARD_ROUTE_AUTHOR_SAMPLE_WORK="content-system|benchmark|author-samples|{platform}-{author_slug}"
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
