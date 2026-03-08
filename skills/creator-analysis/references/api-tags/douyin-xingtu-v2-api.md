# Douyin-Xingtu-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-xingtu-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`21`
- 常见能力：创作者 / 通用能力 / 热点/榜单 / 评论 / 详情 / 主页/账号
- 常见入参：`o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period`
- 标签说明：**(抖音星图V2数据接口/Douyin-Xingtu-V2-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_base_info`

- 能力：创作者
- 入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `recommend`, `need_sec_uid`, `need_linkage_info`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info`

- 能力：创作者
- 入参：query: `o_author_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords`

- 能力：热点/榜单 / 创作者
- 入参：query: `author_id*`, `keyword_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens`

- 能力：评论 / 热点/榜单 / 创作者
- 入参：query: `author_id*`, `num`, `without_emoji`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_local_info`

- 能力：创作者
- 入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `time_range`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_market_fields`

- 能力：创作者
- 入参：query: `market_scene`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_show_items`

- 能力：创作者
- 入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `limit`, `only_assign`, `flow_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_spread_info`

- 能力：创作者
- 入参：query: `o_author_id*`, `platform_source`, `platform_channel`, `type`, `flow_type`, `only_assign`, `range`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list`

- 能力：通用能力
- 入参：query: `mcn_name`, `page`, `limit`, `order_by`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list`

- 能力：通用能力
- 入参：query: `platform_source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail`

- 能力：详情
- 入参：query: `id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get`

### `POST /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `query_start_time*`:string, `query_end_time*`:string, `industry_id_list`[string], `category_list`[integer], `status_list`[integer]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post`

### `POST /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post`

### `GET /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list`

- 能力：通用能力
- 入参：query: `category`, `name`, `qualifier`, `period`, `date`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog`

- 能力：通用能力
- 入参：query: `codes`, `biz_scene`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data`

- 能力：通用能力
- 入参：query: `code`, `qualifier`, `version`, `period`, `date`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get`

### `POST /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors`

- 能力：创作者
- 入参：无
- 请求体：application/json: `author_ids*`[string], `similar_type`:string, `page`:integer, `limit`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post`

### `GET /api/u1/v1/douyin/xingtu_v2/get_resource_list`

- 能力：通用能力
- 入参：query: `resource_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get`

### `GET /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode`

- 能力：主页/账号
- 入参：query: `core_user_id`, `sec_uid`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get`
