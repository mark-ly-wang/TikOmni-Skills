# tikomni-skill

`tikomni-skill` 是一个面向 AI Agent 的 direct API skill：不走 MCP，直接调用 `https://api.tikomni.com` 的 u1/u2 公开接口，并把过程与结果落地为 Markdown 产物。

英文版：`README.md`。

## 1. Tikomni 平台介绍

1. Tikomni 是面向多平台内容数据与 AI Agent 自动化的统一 API 平台。
2. 平台提供统一接口面与统一 API Key，可覆盖 20+ 平台能力。
3. 本 skill 负责让 Agent 自动路由接口、执行提取流程并落地 `.md` 结果。

平台入口：

1. 官网首页：`https://tikomni.com`
2. 控制台与注册：`https://app.tikomni.com`
3. API 基础地址：`https://api.tikomni.com`
4. API 文档：`https://docs.tikomni.com`

## 2. 平台覆盖与实现版本

1. `references/api-catalog` 已覆盖 20+ 平台能力，包括抖音、小红书、TikTok、YouTube、X/Twitter、Threads、Instagram、微博、Bilibili、快手、知乎、Reddit、LinkedIn、Lemon8、皮皮虾、头条、西瓜、微信公众号、微信视频号等。
2. 目录覆盖表示可路由调用；固定流程化 playbook 会持续按平台发布。

`v0.1.0-direct`（2026-02-20）：

1. 已流程化（GA）：抖音主页提取。
2. 已流程化（GA）：小红书主页提取。
3. 可路由（Beta）：其他已覆盖平台意图到接口调用。
4. 输出契约：统一产出 `run/result/error` 三类 markdown。
5. 执行模型：由 Agent 直接编排 HTTP 调用（暂未提供独立 runtime 包）。

## 3. 注册与获取 API Key

1. 打开控制台：`https://app.tikomni.com`
2. 注册账号并完成邮箱验证。
3. 进入用户后台，打开 API Key / API Token 菜单。
4. 创建 API Key，并在创建后立即保存。
5. 将 Key 写入本地 `.env`：

```bash
TIKOMNI_API_KEY="<your_api_key>"
```

## 4. 配置方式（用户可编辑）

这个 skill 支持配置化。对用户可见的行为策略，统一放在配置文档中管理，而不是写死在提示词里。

1. 环境变量模板：`skills/tikomni-skill/env.example`（先复制再填真实 key）。
2. 环境变量配置：工作区 `.env`，或 `skills/tikomni-skill/.env.local`（CI 常用）。
3. 运行时配置文档：`skills/tikomni-skill/references/runtime-config.zh-CN.md`。
4. 配置说明文档：`skills/tikomni-skill/references/configuration.zh-CN.md`。
5. 说明：你在本机 CLI/CUI 跑任务时，`.env` 就是“本地配置”；在 CI 跑任务时，Runner 里的环境变量也是“本地配置”。
6. skill 执行时会先读取运行时配置文档，再按用户定义应用输出目录、markdown 元信息与提取策略。

## 5. 自然语言创建与定制

1. 用户可以直接用自然语言指令让 CLI/OpenClaw/Codex/Claude Code 等 Agent 从 GitHub 安装此 skill。
2. 用户可以用自然语言描述定制平台功能，例如新增路由规则、字段标准化、fallback 策略、markdown 模板。
3. 团队可以基于私有 fork 做组织化扩展，再把通用能力通过 PR 回馈到主仓库。

示例指令：

```text
请从 <repo-url>/skills/tikomni-skill 安装这个 skill，并跑一次冒烟提取。

请更新 skills/tikomni-skill/references/runtime-config.zh-CN.md：
- 输出根目录改为 docs/my-project-output
- markdown 默认标签增加 market=cn, team=growth
- 文件名保留 job_id 后缀。

请为 Bilibili 主页提取新增一个定制 playbook，并挂接到目录路由。
```

## 6. 安装方式

### 6.1 推荐方式：Agent-first（最推荐）

1. 把 GitHub 仓库地址直接发给你的 Agent。
2. 明确要求从 `skills/tikomni-skill` 安装。
3. 安装后要求 Agent 立刻执行一次冒烟任务。

### 6.2 Codex / CodeX

1. 使用 Codex 自带 skill installer 从 GitHub 安装：

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

2. 可选 URL 方式：

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --url "https://github.com/<owner>/<repo>/tree/<ref>/skills/tikomni-skill"
```

### 6.3 Claude Code（本地 skills 目录安装）

1. 把 skill 目录复制到 Claude Code 的 skills 目录：

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

2. 新开 Claude Code 会话，明确要求使用 `tikomni-skill`。

### 6.4 OpenClaw 与其他 Agent 工具

1. 优先方式：直接提供 GitHub 仓库并要求 Agent 自动安装 `skills/tikomni-skill`。
2. 手动兜底：将该目录复制到对应工具的本地 skills 目录，并按 `tikomni-skill` 名称调用。

## 7. 快速开始

1. 在 `.env` 设置 `TIKOMNI_API_KEY`。
2. 生成全量接口目录：

```bash
node "skills/tikomni-skill/scripts/generate-api-catalog.mjs"
```

3. 查看目录索引：

```text
skills/tikomni-skill/references/api-catalog/index.md
```

4. 编辑运行时配置：

```text
skills/tikomni-skill/references/runtime-config.zh-CN.md
```

## 8. 贡献方式

1. 欢迎 PR：新增平台 playbook、字段标准化规则、markdown 模板、回归样例。
2. 欢迎 Issue：功能提案、路由策略调整、提取质量问题反馈。
3. 更新规则时请同步维护中英文文档语义一致。

## 9. 参考文档

1. `skills/tikomni-skill/SKILL.md`
2. `skills/tikomni-skill/references/configuration.zh-CN.md`
3. `skills/tikomni-skill/references/runtime-config.zh-CN.md`
4. `skills/tikomni-skill/references/routing-rules.zh-CN.md`
5. `skills/tikomni-skill/references/normalize-rules.zh-CN.md`
6. `skills/tikomni-skill/references/playbooks/douyin-home-extract.zh-CN.md`
7. `skills/tikomni-skill/references/playbooks/xiaohongshu-home-extract.zh-CN.md`
8. `skills/tikomni-skill/references/playbooks/copy-extract-rules.zh-CN.md`
9. `skills/tikomni-skill/references/output-markdown.zh-CN.md`
10. `skills/tikomni-skill/references/customization-guide.zh-CN.md`
