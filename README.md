# TikOmni Skills

> 中文在前，English below. This README is the main human-facing entry for this repository.

## 中文（ZH）

### 1) 这个仓库是什么

这是 TikOmni 的 Agent Skill 仓库，核心是 `skills/tikomni-skill`：
- 通过直连 HTTP 调用 TikOmni 公共 API（u1/u2）
- 产出结构化 Markdown（run / result / error）
- 提供抖音、小红书主页提取等固定 playbook，以及通用目录路由能力

平台入口：
- 官网：https://tikomni.com
- 控制台：https://app.tikomni.com
- API：https://api.tikomni.com
- 文档：https://docs.tikomni.com

### 2) 快速开始

```bash
# 1) 准备配置（任选其一）
cp ./skills/tikomni-skill/env.example ./.env
# 或
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local

# 2) 填入真实 TIKOMNI_API_KEY 后，检查就绪状态（只显示来源，不显示密钥）
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# 3) 生成 API 目录（可选）
node ./skills/tikomni-skill/scripts/generate-api-catalog.mjs

# 4) 运行提取
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"
```

### 3) 配置说明（重点）

对用户来说，**只有这两个配置源**：
1. `<repo_root>/.env`
2. `skills/tikomni-skill/.env.local`

加载优先级：`process env > .env.local > .env`

说明：
- 不要再依赖 `docs/en` / `docs/zh` 里的旧配置文档。当前以本 README + `skills/tikomni-skill/references/runtime-config.md` 为准。
- 若使用相对路径（如 `--env-file` / `runtime.env_file`），按 `<repo_root>` 解析。

### 4) 必填/可选环境变量（含示例）

必填：
```bash
TIKOMNI_API_KEY="tk_xxx"
```

可选：
```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
TIKOMNI_CONFIG_FILE="skills/tikomni-skill/references/config-templates/defaults.yaml"
```

最小 `.env` 示例：
```bash
TIKOMNI_API_KEY="tk_xxx"
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
```

### 5) 常用脚本怎么跑

```bash
# 就绪检查
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# 通用提取入口
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"

# 抖音主页提取
python3 ./skills/tikomni-skill/scripts/run_douyin_extract.py "<douyin_url_or_id>"

# 小红书主页提取
python3 ./skills/tikomni-skill/scripts/run_xiaohongshu_extract.py "<xhs_url_or_id>"
```

### 6) 扩展 / 自定义

扩展能力建议放在 `skills/tikomni-skill/references/`：
- `routing-rules.md`：路由策略
- `normalize-rules.md`：字段归一化
- `playbooks/`：固定流程
- `config-templates/defaults.yaml`：脚本默认配置模板（高级用户/维护者）

新增能力至少明确：输入 schema、主备接口链路、fallback 条件、输出模板。

### 7) 安全说明

- **永远不要提交真实密钥**（`.env`、`.env.local`、CI secrets）
- 日志和 Markdown 产物中禁止输出 `TIKOMNI_API_KEY`
- 建议在 CI 中关闭命令回显（`set +x`）后再加载 env 文件

---

## English (EN)

### 1) What this repo is

This repository hosts TikOmni agent skills, mainly `skills/tikomni-skill`:
- Direct HTTP calls to TikOmni public APIs (u1/u2)
- Structured Markdown artifacts (run / result / error)
- Fixed playbooks for Douyin/Xiaohongshu homepage extraction plus catalog-based routing

Platform entry points:
- Website: https://tikomni.com
- Dashboard: https://app.tikomni.com
- API: https://api.tikomni.com
- API Docs: https://docs.tikomni.com

### 2) Quick start

```bash
# 1) Prepare config (pick one)
cp ./skills/tikomni-skill/env.example ./.env
# or
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local

# 2) Fill real TIKOMNI_API_KEY, then verify readiness (source only, no secret)
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# 3) Generate API catalog (optional)
node ./skills/tikomni-skill/scripts/generate-api-catalog.mjs

# 4) Run extraction
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"
```

### 3) Configuration (important)

For users, there are **ONLY two config sources**:
1. `<repo_root>/.env`
2. `skills/tikomni-skill/.env.local`

Load priority: `process env > .env.local > .env`

Notes:
- Do not rely on legacy docs under `docs/en` or `docs/zh`.
- Use this README + `skills/tikomni-skill/references/runtime-config.md` as source of truth.
- Relative paths (for example `--env-file` / `runtime.env_file`) are resolved from `<repo_root>`.

### 4) Required and optional env vars (with examples)

Required:
```bash
TIKOMNI_API_KEY="tk_xxx"
```

Optional:
```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
TIKOMNI_CONFIG_FILE="skills/tikomni-skill/references/config-templates/defaults.yaml"
```

Minimal `.env` example:
```bash
TIKOMNI_API_KEY="tk_xxx"
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
```

### 5) How to run key scripts

```bash
# Readiness check
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# Generic extraction entry
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"

# Douyin homepage extraction
python3 ./skills/tikomni-skill/scripts/run_douyin_extract.py "<douyin_url_or_id>"

# Xiaohongshu homepage extraction
python3 ./skills/tikomni-skill/scripts/run_xiaohongshu_extract.py "<xhs_url_or_id>"
```

### 6) Extension / customization notes

Extension points are under `skills/tikomni-skill/references/`:
- `routing-rules.md`
- `normalize-rules.md`
- `playbooks/`
- `config-templates/defaults.yaml` (maintainer/advanced use)

For new capabilities, define at least: input schema, primary/fallback endpoint chain, fallback limits, and output template.

### 7) Security note

- **Never commit real secrets** (`.env`, `.env.local`, CI secrets)
- Never print `TIKOMNI_API_KEY` in logs or Markdown artifacts
- In CI, disable command echo (`set +x`) before sourcing env files

## Core references

- Skill spec: [`skills/tikomni-skill/SKILL.md`](./skills/tikomni-skill/SKILL.md)
- Runtime config reference: [`skills/tikomni-skill/references/runtime-config.md`](./skills/tikomni-skill/references/runtime-config.md)
- Routing rules: [`skills/tikomni-skill/references/routing-rules.md`](./skills/tikomni-skill/references/routing-rules.md)
- Normalize rules: [`skills/tikomni-skill/references/normalize-rules.md`](./skills/tikomni-skill/references/normalize-rules.md)
- API catalog index: [`skills/tikomni-skill/references/api-catalog/index.md`](./skills/tikomni-skill/references/api-catalog/index.md)
