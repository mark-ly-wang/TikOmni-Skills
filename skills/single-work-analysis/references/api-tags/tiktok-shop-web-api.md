# TikTok-Shop-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-shop-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`15`
- 常见能力：电商 / 搜索 / 详情 / 热点/榜单
- 常见入参：`region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id`
- 标签说明：**(TikTok电商网页版数据接口/TikTok-Shop-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list`

- 能力：热点/榜单 / 电商
- 入参：query: `region`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `seller_id`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `seller_id`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1`

- 能力：电商
- 入参：query: `product_id*`, `sort_type`, `filter_id`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2`

- 能力：电商
- 入参：query: `product_id*`, `page_start`, `sort_rule`, `filter_type`, `filter_value`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id`

- 能力：电商
- 入参：query: `category_id*`, `offset`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_category_list`

- 能力：电商
- 入参：query: `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list`

- 能力：搜索 / 电商
- 入参：query: `search_word*`, `offset`, `page_token`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2`

- 能力：搜索 / 电商
- 入参：query: `search_word*`, `offset`, `page_token`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3`

- 能力：搜索 / 电商
- 入参：query: `keyword*`, `offset`, `region`, `sort_by`, `filters_data`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion`

- 能力：搜索 / 电商
- 入参：query: `search_word*`, `lang`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2`

- 能力：搜索 / 电商
- 入参：query: `search_word*`, `lang`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list`

- 能力：电商
- 入参：query: `seller_id*`, `search_params`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get`

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2`

- 能力：电商
- 入参：query: `seller_id*`, `searchParams`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get`
