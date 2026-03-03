# tikomni-skill

`tikomni-skill` 是一个面向 AI Agent 的 direct API skill。  
它直接调用 Tikomni 公共 API（`u1` + `u2`），并把过程与结果落地成 Markdown。

🌐 English: [README.md](./README.md)

## ✨ Tikomni 平台介绍

1. Tikomni 是面向多平台内容数据与 AI Agent 自动化的统一 API 平台。
2. 平台提供统一接口面与统一 API Key，可覆盖 20+ 平台能力。
3. 本 skill 负责让 Agent 自动路由接口、执行提取流程并落地 `.md` 结果。

平台入口：

1. 官网首页：[tikomni.com](https://tikomni.com)
2. 控制台与注册：[app.tikomni.com](https://app.tikomni.com)
3. API 地址：[api.tikomni.com](https://api.tikomni.com)
4. API 文档：[docs.tikomni.com](https://docs.tikomni.com)

## 🚧 平台覆盖与当前版本

1. 已覆盖 20+ 平台能力，包括抖音、小红书、TikTok、YouTube、X/Twitter、Threads、Instagram、微博、Bilibili、快手、知乎、Reddit、LinkedIn、Lemon8、皮皮虾、头条、西瓜、微信公众号、微信视频号等。
2. 目录覆盖表示可路由调用；固定流程化 playbook 持续按平台发布。

`v0.1.0-direct`（2026-02-20）：

1. 已流程化（GA）：抖音主页提取。
2. 已流程化（GA）：小红书主页提取。
3. 可路由（Beta）：其他已覆盖平台意图到接口调用。
4. 输出契约：统一产出 `run/result/error` 三类 markdown。

## 🔑 注册与获取 API Key

1. 打开控制台：[app.tikomni.com](https://app.tikomni.com)
2. 注册账号并完成邮箱验证。
3. 打开 API Key / API Token 菜单。
4. 创建 API Key，并在创建后立即保存。
5. 将 Key 写入本地环境变量：

```bash
TIKOMNI_API_KEY="<your_api_key>"
```

## ⚙️ 配置方式（用户可编辑）

1. 环境变量模板：[./env.example](./env.example)
2. 环境变量文件：工作区 `.env` 或 `./.env.local`
3. 运行时配置：[./references/runtime-config.zh-CN.md](./references/runtime-config.zh-CN.md)
4. 脚本默认模板：[./references/config-templates/defaults.yaml](./references/config-templates/defaults.yaml)
5. 配置说明：[./references/configuration.zh-CN.md](./references/configuration.zh-CN.md)
6. skill 执行时会先读取运行时配置，再应用输出目录、markdown 元信息与提取策略。

## 🤖 自然语言创建与定制

你可以直接用自然语言让 Agent 安装和定制本 skill。

示例：

```text
请从 <repo-url>/skills/tikomni-skill 安装这个 skill，并跑一次冒烟提取。

请更新 ./references/runtime-config.zh-CN.md：
- 输出根目录改为 docs/my-project-output
- markdown 默认标签增加 market=cn, team=growth
```

## 📦 安装方式

### 推荐：Agent-first（最推荐）

1. 把 GitHub 仓库地址发给 Agent。
2. 明确要求从 `skills/tikomni-skill` 安装。
3. 安装后执行一次冒烟任务。

### Codex / CodeX

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

可选 URL 安装：

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --url "https://github.com/<owner>/<repo>/tree/<ref>/skills/tikomni-skill"
```

### Claude Code

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

## 🚀 快速开始

1. 在 `.env` 设置 `TIKOMNI_API_KEY`
2. 生成目录：

```bash
node "./scripts/generate-api-catalog.mjs"
```

3. 查看目录索引：[./references/api-catalog/index.md](./references/api-catalog/index.md)
4. 编辑运行时配置：[./references/runtime-config.zh-CN.md](./references/runtime-config.zh-CN.md)

## 🤝 贡献方式

1. 欢迎 PR：平台 playbook、字段标准化、markdown 模板、回归样例。
2. 欢迎 Issue：功能提案、策略调整、提取质量反馈。
3. 更新规则时请保持中英文语义一致。

## 📚 参考文档

1. [SKILL.md](./SKILL.md)
2. [configuration.zh-CN.md](./references/configuration.zh-CN.md)
3. [runtime-config.zh-CN.md](./references/runtime-config.zh-CN.md)
4. [routing-rules.zh-CN.md](./references/routing-rules.zh-CN.md)
5. [normalize-rules.zh-CN.md](./references/normalize-rules.zh-CN.md)
6. [douyin-home-extract.zh-CN.md](./references/playbooks/douyin-home-extract.zh-CN.md)
7. [xiaohongshu-home-extract.zh-CN.md](./references/playbooks/xiaohongshu-home-extract.zh-CN.md)
8. [copy-extract-rules.zh-CN.md](./references/playbooks/copy-extract-rules.zh-CN.md)
9. [output-markdown.zh-CN.md](./references/output-markdown.zh-CN.md)
10. [customization-guide.zh-CN.md](./references/customization-guide.zh-CN.md)
