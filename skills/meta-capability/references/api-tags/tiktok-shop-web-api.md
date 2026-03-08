# TikTok-Shop-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-shop-web-api.md`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md`](../api-contracts/tiktok-shop-web-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`15`
- 常见能力：电商 / 搜索 / 详情 / 热点/榜单
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id`
- 标签说明：**(TikTok电商网页版数据接口/TikTok-Shop-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list`

- 摘要：获取热卖商品列表/Get hot selling products list
- 能力：热点/榜单 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-hot-selling-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-hot-selling-products-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| region | query | string | 否 | 地区代码/Region code |
| count | query | integer | 否 | 返回商品数量/Number of products to return |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail`

- 摘要：获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID |
| seller_id | query | string | 否 | 卖家ID(可选)/Seller ID (optional) |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2`

- 摘要：获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID |
| seller_id | query | string | 否 | 卖家ID(可选)/Seller ID (optional) |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3`

- 摘要：获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v3`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v3)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1`

- 摘要：获取商品评论V1/Get product reviews V1
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v1`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v1)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID |
| sort_type | query | integer | 否 | 排序方式/Sort type: 1=相关性/Relevance, 2=最新/Recent |
| filter_id | query | string | 否 | 筛选ID/Filter ID |
| offset | query | integer | 否 | 分页偏移量/Offset for pagination |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2`

- 摘要：获取商品评论V2/Get product reviews V2
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID |
| page_start | query | integer | 否 | 起始页码/Page start |
| sort_rule | query | integer | 否 | 排序规则/Sort rule |
| filter_type | query | integer | 否 | 筛选类型/Filter type: 1=默认, 2=有图片/视频, 3=真实购买 |
| filter_value | query | integer | 否 | 星级筛选/Star filter: 6=全部, 5-1=对应星级 |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id`

- 摘要：根据分类ID获取商品列表/Get products by category ID
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-by-category-id`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-by-category-id)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| category_id | query | integer | 是 | 分类ID/Category ID |
| offset | query | integer | 否 | 翻页偏移量/Offset for pagination |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_category_list`

- 摘要：获取商品分类列表/Get product category list
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-category-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-category-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list`

- 摘要：搜索商品列表V1/Search products list V1
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| page_token | query | string | 否 | 分页标记/Page token |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2`

- 摘要：搜索商品列表V2(移动端)/Search products list V2 (Mobile)
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| page_token | query | string | 否 | 分页标记/Page token |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3`

- 摘要：搜索商品列表V3/Search products list V3
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v3`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v3)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| offset | query | integer | 否 | 偏移量/Offset |
| region | query | string | 否 | 地区代码/Region code (Alpha-2) |
| sort_by | query | string | 否 | 排序方式/Sort by: RELEVANCE, PRICE_ASC, PRICE_DESC, BEST_SELLERS |
| filters_data | query | string | 否 | 筛选数据JSON/Filters data JSON |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion`

- 摘要：获取搜索关键词建议V1/Get search keyword suggestions V1
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword |
| lang | query | string | 否 | 语言/Language |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2`

- 摘要：获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword |
| lang | query | string | 否 | 语言/Language |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list`

- 摘要：获取商家商品列表V1/Get seller products list V1
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 卖家ID/Seller ID |
| search_params | query | string | 否 | 搜索参数(用于分页)/Search params (for pagination) |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2`

- 摘要：获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get`
- 完整契约：[`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list-v2)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 卖家ID/Seller ID |
| searchParams | query | string | 否 | 搜索参数/Search params |
| region | query | string | 否 | 地区代码/Region code |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。
