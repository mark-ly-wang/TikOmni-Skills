# TikOmni Skills

中文 | [English (README.md)](./README.md)

本仓库提供 TikOmni 的 Agent Skill（`skills/tikomni-skill`），用于直连 TikOmni 公共 API（`u1` + `u2`）并产出结构化 Markdown 结果。

## 平台入口

- 官网：https://tikomni.com
- 控制台：https://app.tikomni.com
- API：https://api.tikomni.com
- API 文档：https://docs.tikomni.com

## 快速开始

```bash
# 1）准备配置（任选其一）
cp ./skills/tikomni-skill/env.example ./.env
# 或
cp ./skills/tikomni-skill/env.example ./skills/tikomni-skill/.env.local

# 2）填入真实 TIKOMNI_API_KEY 后，检查就绪状态
python3 ./skills/tikomni-skill/scripts/check_tikomni_readiness.py

# 3）（可选）生成 API 目录
node ./skills/tikomni-skill/scripts/generate-api-catalog.mjs

# 4）运行提取
python3 ./skills/tikomni-skill/scripts/run_tikomni_extract.py "<url_or_id>"
```

## 配置说明（重点）

对用户来说，配置来源**只有两个**：
1. `<repo_root>/.env`
2. `skills/tikomni-skill/.env.local`

加载优先级：`process env > .env.local > .env`

### 必填变量

```bash
TIKOMNI_API_KEY="tk_xxx"
```

### 可选变量

```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
TIKOMNI_CONFIG_FILE="skills/tikomni-skill/references/config-templates/defaults.yaml"
```

## 常用命令

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

## 扩展说明

扩展点位于 `skills/tikomni-skill/references/`：
- `routing-rules.md`
- `normalize-rules.md`
- `playbooks/`
- `config-templates/defaults.yaml`

## 安全说明

- 不要提交真实密钥（`.env`、`.env.local`、CI secrets）
- 不要在日志或 markdown 输出中打印 `TIKOMNI_API_KEY`
- CI 加载 env 前建议先 `set +x`

## 核心参考

- [`skills/tikomni-skill/SKILL.md`](./skills/tikomni-skill/SKILL.md)
- [`skills/tikomni-skill/references/runtime-config.md`](./skills/tikomni-skill/references/runtime-config.md)
- [`skills/tikomni-skill/references/routing-rules.md`](./skills/tikomni-skill/references/routing-rules.md)
- [`skills/tikomni-skill/references/normalize-rules.md`](./skills/tikomni-skill/references/normalize-rules.md)
- [`skills/tikomni-skill/references/api-catalog/index.md`](./skills/tikomni-skill/references/api-catalog/index.md)
