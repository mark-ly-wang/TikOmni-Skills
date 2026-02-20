# 运行时配置模板

通过编辑本文件自定义 skill 行为。

## 0. 先说明白：什么是“本地配置”？

1. “本地”指当前运行 Agent 的环境。
2. 你在自己电脑的 CLI/CUI 里运行时，本地就是你的电脑。
3. 你在服务器或 CI 跑任务时，本地就是那台服务器/Runner。
4. 结论：CUI/CLI 里配置 `.env`，本质也是本地配置。

## 1. 快速上手（小白版）

1. 先准备密钥文件（不要提交真实密钥）：
   - 复制 `skills/tikomni-skill/env.example` 为你的私有文件（如仓库根目录 `.env`，或 `skills/tikomni-skill/.env.local`）。
2. 填入真实 `TIKOMNI_API_KEY`。
3. 再编辑本文件，按业务需求改输出目录、标签、策略。
4. 运行 skill 时，先读取本文件，再按 `auth_env_key` 到环境变量取 key。

## 2. 配置档案（你是谁、输出语言）

```yaml
# 配置名称，仅用于区分不同配置档案
profile_name: default
# 负责人/使用人，可留空
owner: ""
# 输出语言，常用 zh-CN 或 en
language: zh-CN
```

## 3. API 运行参数（怎么连 Tikomni）

```yaml
# API 根地址，默认不需要改
base_url: https://api.tikomni.com
# 从环境变量里读取哪个字段作为 API Key
auth_env_key: TIKOMNI_API_KEY
# 单次请求超时（毫秒）
timeout_ms: 60000
# 可选：记录你把密钥放在哪个文件（用于团队约定）
env_file: .env
```

说明：

1. `env_file` 只是声明路径，不应在日志打印其内容。
2. 真实密钥始终从环境变量读取，不写进 markdown 输出。

## 4. 输出目录结构（产物落在哪里）

```yaml
# 所有输出的根目录
root_dir: docs/skill-output
# 运行轨迹目录
runs_dir: _runs
# 结果目录
results_dir: results
# 错误目录
errors_dir: _errors
# 文件命名规则，可用占位符：{type} {timestamp} {job_id}
filename_pattern: "{type}-{timestamp}-{job_id}.md"
```

示例结果路径：

1. `docs/skill-output/_runs/run-20260220-220000-job123.md`
2. `docs/skill-output/results/result-20260220-220000-job123.md`

## 5. Markdown 默认值（标题/标签）

```yaml
# 标题前缀
title_prefix: Tikomni Extraction
# 默认标签，会写入 frontmatter
default_tags:
  - tikomni
  - extraction
# 额外 frontmatter 字段（键值对）
frontmatter_extra: {}
```

## 6. 提取策略（业务行为）

```yaml
# 主页提取时是否逐条开启文案提取
homepage_batch_copy_enabled: true
# 文案语言策略：auto / zh-CN / en
copy_language: auto
# 小红书是否优先字幕字段
xhs_subtitle_first: true
# 抖音文案是否固定走 U2
douyin_copy_via_u2: true
```

## 7. 路由策略（接口选择）

```yaml
# 同平台同意图的接口优先级
endpoint_priority:
  - app
  - web_v2
  - web
# 是否允许 fallback
fallback_enabled: true
# fallback 最大尝试次数
max_fallback_attempts: 2
```

## 8. 常见问题

1. 我不懂“本地配置”在哪？
   - 如果你在本机 CLI/CUI 里跑，就在当前仓库 `.env` 配置。
   - 如果你在 CI 跑，就在 CI 的环境变量或私有 env 文件配置。
2. 怎么避免泄露 key？
   - 不要提交真实 `.env` 文件。
   - 日志里不要打印 `TIKOMNI_API_KEY`。
