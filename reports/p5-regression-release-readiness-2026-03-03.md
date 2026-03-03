# P5 验收报告（回归 + 发布准备收口）

- 仓库：`TikOmni-Skills`
- 分支：`feat/p5-regression-release-readiness`
- 日期：2026-03-03
- 范围：仅 P5 收尾（不扩功能）

## 1) 回归用例与结果

### 用例 A：single_video 路由（含默认映射优先）
- 验证点：当 `content_kind=single_video` 且手动 `card_type=author` 时，默认应优先走 `content_kind` 映射（=> `work`）。
- 结果：通过
  - effective_card_type: `work`
  - route: `10-内容系统/15-对标研究/01-作品对标卡`

### 用例 B：author_home 样本路由
- 验证点：`content_kind=author_home` 应映射到 `author_sample_work`。
- 结果：通过
  - effective_card_type: `author_sample_work`
  - route: `10-内容系统/15-对标研究/02-作者样本集/douyin-回归作者`

### 用例 C：author_analysis 路由映射（路由层）
- 验证点：`content_kind=author_analysis` 应映射到 `author`。
- 结果：通过
  - effective_card_type: `author`
  - route: `10-内容系统/15-对标研究/03-作者对标卡`

## 2) 配置友好收口验证

### 验证点 1：配置文件路径无效时，脚本仍可运行（回退 builtin defaults）
- 方法：`run_douyin_single_video.py --config /tmp/not-exists-p5-config.yaml --no-write-card`
- 观察：
  - config source = `builtin-defaults`
  - 脚本返回业务错误 `missing_share_url`（非配置错误）
- 结论：通过（配置无效时可回退并继续执行）

### 验证点 2：content_kind 映射默认优先
- 方法：`requested_card_type=author + content_kind=single_video + force=false`
- 结果：`effective_card_type=work`
- 结论：通过

### 验证点 3：`--force-card-type` 覆盖生效
- 方法：`requested_card_type=author + content_kind=single_video + force=true`
- 结果：`effective_card_type=author`
- 结论：通过

## 3) 必需检查结果

- `python3 scripts/ci_skill_validate.py` ✅ 通过
- `python3 scripts/ci_secret_scan.py` ✅ 通过
- `python3 scripts/ci_package_manifest.py` ✅ 通过
- `python3 scripts/ci_build_skill_zip.py` ✅ 通过

## 4) 风险余项

1. 当前回归以“路由层+配置层”为主，未覆盖真实 API 在线链路（本次 P5 收尾范围内可接受）。
2. `write_benchmark_card` 的内容分析段依赖外部 `openclaw agent` 调用；在无可用 agent 响应环境下，可能引入较长等待（超时窗口默认较大）。建议在发布后补一条“离线/降级策略”专项验证。

## 5) Go / No-Go 建议

- 建议：**Go（可发布）**
- 理由：
  1) P5 指定关键路由与配置收口点均通过；
  2) 四项必需 CI 检查均通过；
  3) 余项风险已识别，且不阻断本次 P5 收尾目标。
