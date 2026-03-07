# 小红书 Creator 指引

## 先读什么

- 先读 `references/api-capability-catalog.md` 中 `Xiaohongshu-App-V2-API`、`Xiaohongshu-App-API`、`Xiaohongshu-Web-V2-API`。
- 当前仓库已验证的是“主页输入 -> user_id/xsec_token 解析 -> profile 多路由级联 -> posts 多路由级联”。

## 作者侧优先资源

- 昵称
- handle
- IP 属地
- 头像
- 粉丝数、累计获赞数、作品数

## 作品侧优先资源

- 作品 ID：`note_id`
- 标题 / 文案：`title` / `desc` / `content`
- 视频作品优先检查原生字幕
- 互动指标：点赞、评论、收藏、分享、播放

## 当前优先路由链

1. 主页标识解析：`GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
   - OpenAPI 必填入参：`share_link`
   - 当前实现会同时冗余传 `share_url`、`url`
2. 作者 profile 级联：
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_info`
   - 典型入参：`user_id`，必要时补 `share_text` / `xsec_token`
3. 主页作品分页级联：
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_notes`
   - 典型入参：`user_id`、`cursor`

## 需要落到的统一字段

- 作者卡：`platform_author_id`、`author_handle`、`nickname`、`ip_location`、`signature`、`avatar_url`、`fans_count`、`liked_count`、`collected_count`、`works_count`、`verified`
- 作品卡：`platform_work_id`、`title`、`caption_raw`、`published_date`、`digg_count`、`comment_count`、`collect_count`、`share_count`、`play_count`、`video_download_url`

## 选路规则

- 已有 `user_id` 时，直接跳过 resolve route；`xsec_token` 作为补充，不是所有路由都必需。
- profile 和 posts 都必须按级联顺序尝试，并基于字段完整度判断是否切 fallback。
- 主页作品页拿不到稳定字段时，再回全量目录找补充 route，不要直接把半残字段送进作者分析。

## 当前可运行实现

- `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
