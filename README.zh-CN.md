# tikomni-skill

`tikomni-skill` 是面向 AI Agent 的 direct API skill。
它调用 Tikomni 公共 API（`u1` + `u2`），并输出 run/result/error 三类 Markdown 产物。

🌐 English: [README.md](./README.md)

## 平台入口

1. 官网：[tikomni.com](https://tikomni.com)
2. 控制台 / 注册：[app.tikomni.com](https://app.tikomni.com)
3. API 地址：[api.tikomni.com](https://api.tikomni.com)
4. API 文档：[docs.tikomni.com](https://docs.tikomni.com)

## 覆盖范围

- 已覆盖 20+ 平台目录路由能力。
- 固定 playbook 当前 GA：抖音主页提取、小红书主页提取。
- 其他平台按目录意图路由调用。

## 配置说明

### 1）先复制 env 模板

```bash
cp ./skills/tikomni-skill/env.example ./.env
# 或
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local
```

复制后再替换为真实值。

### 2）三路 key 来源与优先级

`TIKOMNI_API_KEY` 会按固定顺序读取三路来源：

1. 进程环境变量（最高）
2. `skills/tikomni-skill/.env.local`
3. `<workspace_root>/.env`（或当前工作目录 `.env`）

优先级规则：`process env > .env.local > .env`。

### 3）路径配置

- Skill 根目录：`<workspace_root>/skills/tikomni-skill`
- 运行默认配置模板：`skills/tikomni-skill/references/config-templates/defaults.yaml`
- 运行配置文档：
  - EN：`skills/tikomni-skill/references/runtime-config.md`
  - ZH：`skills/tikomni-skill/references/runtime-config.zh-CN.md`

### 4）关键环境变量

- `TIKOMNI_API_KEY`（必填）
- `TIKOMNI_BASE_URL`（可选，默认 `https://api.tikomni.com`）
- `TIKOMNI_TIMEOUT_MS`（可选，默认 `60000`）
- `TIKOMNI_CONFIG_FILE`（可选，运行配置 YAML 路径）

## 安装

### 推荐：Agent-first（GitHub）

1. 让 Agent 从 `skills/tikomni-skill` 安装。
2. 安装后执行一次冒烟提取。

### Codex / CodeX

```bash
python3 "~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo "<owner>/<repo>" --path "skills/tikomni-skill"
```

### Claude Code

```bash
mkdir -p "~/.claude/skills"
cp -R "<repo-root>/skills/tikomni-skill" "~/.claude/skills/tikomni-skill"
```

## 快速开始

```bash
# 1) 通过任一支持来源设置 key
export TIKOMNI_API_KEY="tk_example_123"

# 2) 生成 API 目录
node "./skills/tikomni-skill/scripts/generate-api-catalog.mjs"

# 3) 运行提取脚本
python3 "./skills/tikomni-skill/scripts/run_tikomni_extract.py" "<url_or_id>"
```

## 核心参考

1. [skills/tikomni-skill/SKILL.md](./skills/tikomni-skill/SKILL.md)
2. [configuration.md](./skills/tikomni-skill/references/configuration.md)
3. [runtime-config.md](./skills/tikomni-skill/references/runtime-config.md)
4. [routing-rules.md](./skills/tikomni-skill/references/routing-rules.md)
5. [normalize-rules.md](./skills/tikomni-skill/references/normalize-rules.md)
6. [card-routing.zh-CN.md](./skills/tikomni-skill/references/card-routing.zh-CN.md)
