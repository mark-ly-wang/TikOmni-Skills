# Demo-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/demo-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`9`
- 常见能力：作品详情 / 主页/账号 / 通用能力 / 搜索
- 常见入参：无
- 标签说明：**(TikHub API示例项目/Demo Project)**

## 路由列表

### `GET /api/u1/v1/demo/demo/cache_status`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`view_cache_status_api_v1_demo_demo_cache_status_get`

### `GET /api/u1/v1/demo/douyin/app/fetch_one_video`

- 能力：作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`douyin_app_fetch_one_video_api_v1_demo_douyin_app_fetch_one_video_get`

### `GET /api/u1/v1/demo/douyin/web/fetch_one_video`

- 能力：作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`douyin_web_fetchone_video_demo_api_v1_demo_douyin_web_fetch_one_video_get`

### `GET /api/u1/v1/demo/douyin_search/app/general_search`

- 能力：搜索
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`douyin_search_general_demo_api_v1_demo_douyin_search_app_general_search_get`

### `GET /api/u1/v1/demo/instagram/web/fetch_user_info`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`instagram_web_fetch_user_info_api_v1_demo_instagram_web_fetch_user_info_get`

### `GET /api/u1/v1/demo/kuaishou/web/fetch_one_video`

- 能力：作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kuaishou_web_fetch_one_video_api_v1_demo_kuaishou_web_fetch_one_video_get`

### `GET /api/u1/v1/demo/tiktok/app/fetch_one_video`

- 能力：作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`tiktok_app_fetch_one_video_api_v1_demo_tiktok_app_fetch_one_video_get`

### `GET /api/u1/v1/demo/tiktok/web/fetch_user_profile`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`tiktok_web_fetch_user_profile_api_v1_demo_tiktok_web_fetch_user_profile_get`

### `GET /api/u1/v1/demo/wechat/article_extract`

- 能力：作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`wechat_article_extract_api_v1_demo_wechat_article_extract_get`
