# Douyin-Xingtu-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-xingtu-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`22`
- 常见能力：通用能力 / 作品详情 / 评论 / 热点/榜单 / 创作者 / 搜索
- 常见入参：`kolId`, `platformChannel`, `_range`, `page`, `onlyAssign`, `keyword`, `uri`, `durationTS`, `format`, `sec_user_id`
- 标签说明：**(抖音星图数据接口/Douyin-Xingtu-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/xingtu/author_content_hot_comment_keywords_v1`

- 能力：评论 / 热点/榜单 / 创作者
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`author_content_hot_comment_keywords_v1_api_v1_douyin_xingtu_author_content_hot_comment_keywords_v1_get`

### `GET /api/u1/v1/douyin/xingtu/author_hot_comment_tokens_v1`

- 能力：评论 / 热点/榜单 / 创作者
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`author_hot_comment_tokens_v1_api_v1_douyin_xingtu_author_hot_comment_tokens_v1_get`

### `GET /api/u1/v1/douyin/xingtu/get_sign_image`

- 能力：通用能力
- 入参：query: `uri*`, `durationTS`, `format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sign_image_api_v1_douyin_xingtu_get_sign_image_get`

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`

- 能力：主页/账号
- 入参：query: `sec_user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_xingtu_kolid_by_sec_user_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_sec_user_id_get`

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_uid`

- 能力：通用能力
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_xingtu_kolid_by_uid_api_v1_douyin_xingtu_get_xingtu_kolid_by_uid_get`

### `GET /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`

- 能力：通用能力
- 入参：query: `unique_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_xingtu_kolid_by_unique_id_api_v1_douyin_xingtu_get_xingtu_kolid_by_unique_id_get`

### `GET /api/u1/v1/douyin/xingtu/kol_audience_portrait_v1`

- 能力：通用能力
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_audience_portrait_v1_api_v1_douyin_xingtu_kol_audience_portrait_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_base_info_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `platformChannel*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_base_info_v1_api_v1_douyin_xingtu_kol_base_info_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_conversion_ability_analysis_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `_range*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_conversion_ability_analysis_v1_api_v1_douyin_xingtu_kol_conversion_ability_analysis_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_convert_video_display_v1`

- 能力：作品详情
- 入参：query: `kolId*`, `detailType*`, `page*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_convert_video_display_v1_api_v1_douyin_xingtu_kol_convert_video_display_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_cp_info_v1`

- 能力：通用能力
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_cp_info_v1_api_v1_douyin_xingtu_kol_cp_info_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_daily_fans_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `startDate*`, `endDate*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_daily_fans_v1_api_v1_douyin_xingtu_kol_daily_fans_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_data_overview_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `_type*`, `_range*`, `flowType*`, `onlyAssign`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_data_overview_v1_api_v1_douyin_xingtu_kol_data_overview_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_fans_portrait_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `fansType`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_fans_portrait_v1_api_v1_douyin_xingtu_kol_fans_portrait_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_link_struct_v1`

- 能力：通用能力
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_link_struct_v1_api_v1_douyin_xingtu_kol_link_struct_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_rec_videos_v1`

- 能力：作品详情
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_rec_videos_v1_api_v1_douyin_xingtu_kol_rec_videos_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_service_price_v1`

- 能力：通用能力
- 入参：query: `kolId*`, `platformChannel*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_service_price_v1_api_v1_douyin_xingtu_kol_service_price_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_touch_distribution_v1`

- 能力：通用能力
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_touch_distribution_v1_api_v1_douyin_xingtu_kol_touch_distribution_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_video_performance_v1`

- 能力：作品详情
- 入参：query: `kolId*`, `onlyAssign*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_video_performance_v1_api_v1_douyin_xingtu_kol_video_performance_v1_get`

### `GET /api/u1/v1/douyin/xingtu/kol_xingtu_index_v1`

- 能力：通用能力
- 入参：query: `kolId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`kol_xingtu_index_v1_api_v1_douyin_xingtu_kol_xingtu_index_v1_get`

### `GET /api/u1/v1/douyin/xingtu/search_kol_v1`

- 能力：搜索
- 入参：query: `keyword*`, `platformSource*`, `page*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_kol_v1_api_v1_douyin_xingtu_search_kol_v1_get`

### `GET /api/u1/v1/douyin/xingtu/search_kol_v2`

- 能力：搜索
- 入参：query: `keyword*`, `followerRange`, `contentTag`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_kol_v2_api_v1_douyin_xingtu_search_kol_v2_get`
