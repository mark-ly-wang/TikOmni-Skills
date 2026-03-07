# `@tikomni/skills` 发布说明

## 前置条件

- 你已经有 `@tikomni` scope 的 npm 发布权限。
- 仓库 GitHub Actions 已配置 `NPM_TOKEN` secret。
- 发布前工作区需要确认干净，至少不能夹带不想发到 npm 的 skill 改动。

## 实际发布的是什么

npm 包里会带上 `package.json` 声明的 CLI 和 `skills/` 内容。

用户安装时不会去 GitHub 动态拉 skill。实际流程是：用户从 npm registry 下载这个包，然后执行包里的 CLI，把包内自带的 skill 目录复制到目标运行时目录。

## 推荐发布流程

1. 更新 `package.json` 的版本号。
2. 本地先跑验证：
   - `npm test`
   - `npm run pack:dry-run`
   - `python3 scripts/ci_skill_validate.py`
   - `python3 scripts/ci_secret_scan.py`
   - `python3 scripts/ci_package_manifest.py`
   - `python3 scripts/ci_build_skill_zip.py`
3. 提交版本变更。
4. 创建并推送 `v<版本号>` 形式的 tag。
   - 例如：`v0.1.0`
5. GitHub Actions 的 `npm-publish` workflow 会自动：
   - 校验 tag 和 `package.json` 版本一致
   - 重跑测试和仓库校验
   - 执行 `npm pack --dry-run`
   - 发布到 npm

## 手动 dry-run

也可以直接手动触发 `npm-publish` workflow，并设置：

- `npm_dist_tag`：例如 `latest`、`next`、`beta`
- `dry_run`：设为 `true`

这很适合第一次正式发布前做演练。

## 回滚建议

- 如果发布内容有问题但仍应保留可安装性，优先直接补发一个新版本修正。
- 如果某个版本需要显式标记为不推荐使用，使用 `npm deprecate`。
- 不要把 `npm unpublish` 当成常规回滚手段。
