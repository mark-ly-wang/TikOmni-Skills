# 配置说明

本文档定义用户应在哪里配置这个 skill。

## 0. 先回答你的问题：什么叫“本地配置”？

1. 本地 = 当前运行 Agent 的环境。
2. 你在电脑里打开 CLI/CUI 跑任务时，本地就是你的电脑。
3. 你在 GitHub Actions 或其他 CI 跑任务时，本地就是 CI 的 Runner。
4. 所以“在 CUI 里配置”本质上也是本地配置。

## 1. 配置来源

1. 当前工作区 `.env`：用于密钥和运行环境配置（最常见）。
2. `skills/tikomni-skill/references/runtime-config.zh-CN.md`：用于用户可见的执行策略配置。
3. 可选：用户可在提示词里指定其他配置文档路径，Agent 应优先读取该路径。
4. 环境变量模板：`skills/tikomni-skill/env.example`（示例文件，不含真实密钥）。

## 2. `.env` 必填项

```bash
TIKOMNI_API_KEY="<required>"
```

可选项：

```bash
TIKOMNI_BASE_URL="https://api.tikomni.com"
TIKOMNI_TIMEOUT_MS="60000"
```

## 3. 推荐目录与文件

1. `./.env`：你自己的私有配置（本机调试最方便）。
2. `skills/tikomni-skill/env.example`：模板文件，可复制后再填值。
3. `skills/tikomni-skill/references/runtime-config.zh-CN.md`：策略配置（输出目录、标签、策略）。

## 4. CI 如何读取而不暴露过程

在 CI 或脚本里读取 `.env` 文件时，关闭命令回显，避免日志泄露：

```bash
set +x
set -a
source "skills/tikomni-skill/.env.local"
set +a
```

说明：

1. `set +x` 会关闭命令回显，避免把敏感值打印到日志。
2. `skills/tikomni-skill/.env.local` 不应提交到仓库。

## 5. 运行时配置契约

`runtime-config.zh-CN.md` 是本 skill 的策略配置文档，建议包含以下区块：

1. API 运行参数（base URL、鉴权环境变量、超时）。
2. 输出目录策略（根目录与子目录命名）。
3. Markdown 元信息默认值（标签、标题前缀、语言）。
4. 功能开关与提取策略（批量行为、转写策略）。
5. 路由与 fallback 策略覆盖项（用户需要自定义时）。

## 6. Agent 执行约束

1. 调用任何接口前，先读取 `runtime-config.zh-CN.md`（或用户指定配置路径）。
2. 将配置值作为路由、提取、输出的一级输入。
3. 若配置缺失或不完整，执行前应向用户确认兜底值。
