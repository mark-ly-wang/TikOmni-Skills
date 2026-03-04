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

## ⚙️ 安装后怎么配置

要调用 TikOmni API，需要先配置 API Key。

必填：
```bash
TIKOMNI_API_KEY="你的真实 key"
```

推荐配置位置：
- `<repo_root>/.env`
- 或 `skills/tikomni-skill/.env.local`（本地覆盖）

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
