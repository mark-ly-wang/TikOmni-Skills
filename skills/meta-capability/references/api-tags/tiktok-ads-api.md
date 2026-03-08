# TikTok-Ads-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-ads-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`31`
- 常见能力：广告 / 搜索 / 详情 / 创作者 / 电商 / 话题
- 常见入参：`limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id`
- 标签说明：**(TikTok广告创意中心数据接口/TikTok-Ads-Creative-Center-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/ads/get_ad_interactive_analysis`

- 能力：广告
- 入参：query: `material_id*`, `metric_type`, `period_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get`

### `GET /api/u1/v1/tiktok/ads/get_ad_keyframe_analysis`

- 能力：广告
- 入参：query: `material_id*`, `metric`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get`

### `GET /api/u1/v1/tiktok/ads/get_ad_percentile`

- 能力：广告
- 入参：query: `material_id*`, `metric`, `period_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get`

### `GET /api/u1/v1/tiktok/ads/get_ads_detail`

- 能力：详情 / 广告
- 入参：query: `ads_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get`

### `GET /api/u1/v1/tiktok/ads/get_creative_patterns`

- 能力：广告
- 入参：query: `first_industry_id`, `period_type`, `order_field`, `order_type`, `week`, `page`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get`

### `GET /api/u1/v1/tiktok/ads/get_creator_filters`

- 能力：创作者 / 广告
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get`

### `GET /api/u1/v1/tiktok/ads/get_creator_list`

- 能力：创作者 / 广告
- 入参：query: `page`, `limit`, `sort_by`, `creator_country`, `audience_country`, `audience_count`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creator_list_api_v1_tiktok_ads_get_creator_list_get`

### `GET /api/u1/v1/tiktok/ads/get_hashtag_creator`

- 能力：创作者 / 广告 / 话题
- 入参：query: `hashtag*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get`

### `GET /api/u1/v1/tiktok/ads/get_hashtag_filters`

- 能力：广告 / 话题
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get`

### `GET /api/u1/v1/tiktok/ads/get_hashtag_list`

- 能力：广告 / 话题
- 入参：query: `page`, `limit`, `period`, `country_code`, `sort_by`, `industry_id`, `filter_by`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get`

### `GET /api/u1/v1/tiktok/ads/get_keyword_details`

- 能力：详情 / 广告
- 入参：query: `keyword`, `page`, `limit`, `period`, `country_code`, `order_by`, `order_type`, `industry`, `objective`, `keyword_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get`

### `GET /api/u1/v1/tiktok/ads/get_keyword_filters`

- 能力：广告
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get`

### `GET /api/u1/v1/tiktok/ads/get_keyword_insights`

- 能力：广告 / 数据分析
- 入参：query: `page`, `limit`, `period`, `country_code`, `order_by`, `order_type`, `industry`, `objective`, `keyword_type`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get`

### `GET /api/u1/v1/tiktok/ads/get_keyword_list`

- 能力：广告
- 入参：query: `keyword`, `period`, `page`, `limit`, `country_code`, `industry`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get`

### `GET /api/u1/v1/tiktok/ads/get_popular_trends`

- 能力：热点/榜单 / 广告
- 入参：query: `period`, `page`, `limit`, `order_by`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get`

### `GET /api/u1/v1/tiktok/ads/get_product_detail`

- 能力：详情 / 电商 / 广告
- 入参：query: `id*`, `last`, `ecom_type`, `period_type`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_detail_api_v1_tiktok_ads_get_product_detail_get`

### `GET /api/u1/v1/tiktok/ads/get_product_filters`

- 能力：电商 / 广告
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_filters_api_v1_tiktok_ads_get_product_filters_get`

### `GET /api/u1/v1/tiktok/ads/get_product_metrics`

- 能力：电商 / 广告
- 入参：query: `id*`, `last`, `metrics`, `ecom_type`, `period_type`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get`

### `GET /api/u1/v1/tiktok/ads/get_query_suggestions`

- 能力：搜索 / 广告
- 入参：query: `count`, `scenario`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get`

### `GET /api/u1/v1/tiktok/ads/get_recommended_ads`

- 能力：广告
- 入参：query: `material_id*`, `industry`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get`

### `GET /api/u1/v1/tiktok/ads/get_related_keywords`

- 能力：广告
- 入参：query: `keyword`, `period`, `country_code`, `rank_type`, `content_type`, `page`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get`

### `GET /api/u1/v1/tiktok/ads/get_sound_detail`

- 能力：详情 / 广告
- 入参：query: `clip_id*`, `period`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get`

### `GET /api/u1/v1/tiktok/ads/get_sound_filters`

- 能力：广告
- 入参：query: `rank_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get`

### `GET /api/u1/v1/tiktok/ads/get_sound_rank_list`

- 能力：广告
- 入参：query: `period`, `page`, `limit`, `rank_type`, `new_on_board`, `commercial_music`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get`

### `GET /api/u1/v1/tiktok/ads/get_sound_recommendations`

- 能力：广告
- 入参：query: `clip_id*`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get`

### `GET /api/u1/v1/tiktok/ads/get_top_ads_spotlight`

- 能力：广告
- 入参：query: `industry`, `page`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get`

### `GET /api/u1/v1/tiktok/ads/get_top_products`

- 能力：电商 / 广告
- 入参：query: `last`, `page`, `limit`, `country_code`, `first_ecom_category_id`, `ecom_type`, `period_type`, `order_by`, `order_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_top_products_api_v1_tiktok_ads_get_top_products_get`

### `GET /api/u1/v1/tiktok/ads/search_ads`

- 能力：搜索 / 广告
- 入参：query: `objective`, `like`, `period`, `industry`, `keyword`, `page`, `limit`, `order_by`, `country_code`, `ad_format`, `ad_language`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_ads_api_v1_tiktok_ads_search_ads_get`

### `GET /api/u1/v1/tiktok/ads/search_creators`

- 能力：搜索 / 创作者 / 广告
- 入参：query: `keyword*`, `page`, `limit`, `sort_by`, `creator_country`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_creators_api_v1_tiktok_ads_search_creators_get`

### `GET /api/u1/v1/tiktok/ads/search_sound`

- 能力：搜索 / 广告
- 入参：query: `keyword*`, `period`, `page`, `limit`, `rank_type`, `new_on_board`, `commercial_music`, `country_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_sound_api_v1_tiktok_ads_search_sound_get`

### `GET /api/u1/v1/tiktok/ads/search_sound_hint`

- 能力：搜索 / 广告
- 入参：query: `keyword*`, `period`, `page`, `limit`, `rank_type`, `country_code`, `filter_by_checked`, `commercial_music`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get`
