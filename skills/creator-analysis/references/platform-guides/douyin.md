# 抖音 Creator 指引

## 先读什么

- 先读 `references/api-capability-catalog.md` 中 `Douyin-App-V3-API` 和 `Douyin-Web-API`。
- 当前仓库已验证的是“主页输入 -> sec_user_id 解析 -> 作者 profile -> 作品分页列表”的主页链路。

## 作者侧优先资源

- 昵称：`nickname`
- handle：`short_id` / `unique_id`
- IP 属地
- 头像
- 粉丝数、累计获赞数、作品数

## 作品侧优先资源

- 作品 ID：`aweme_id`
- 标题 / 文案：`title` / `desc`
- 视频下载链接：优先无水印路径
- 互动指标：点赞、评论、收藏、分享、播放

## 当前优先路由链

1. 主页标识解析：`GET /api/u1/v1/douyin/web/get_sec_user_id`
   - OpenAPI 必填入参：`url`
   - 当前实现会同时冗余传 `share_url`
2. 作者主页：`GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - 必填入参：`sec_user_id`
3. 主页作品分页：`GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
   - 必填入参：`sec_user_id`
   - 常用分页参数：`max_cursor`、`count`、`sort_type`

## 需要落到的统一字段

- 作者卡：`platform_author_id`、`author_handle`、`nickname`、`ip_location`、`signature`、`avatar_url`、`fans_count`、`liked_count`、`works_count`、`verified`
- 作品卡：`platform_work_id`、`title`、`caption_raw`、`published_date`、`digg_count`、`comment_count`、`collect_count`、`share_count`、`play_count`、`video_download_url`

## 选路规则

- 已经有 `sec_user_id` 时，直接跳过解析 route。
- 作者页抓取默认走最新作品分页，不要先随机搜索其他 feed route。
- 如果主页链路拿不到作者关键字段，再回全量能力目录挑补充 route；不要直接放弃作者卡。

## 当前可运行实现

- `skills/creator-analysis/scripts/author_home/adapters/platform_adapters.py`
- `skills/creator-analysis/scripts/author_home/orchestrator/run_author_analysis.py`
