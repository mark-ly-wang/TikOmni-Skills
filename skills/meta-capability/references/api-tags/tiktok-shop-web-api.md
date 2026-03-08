# TikTok-Shop-Web-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-shop-web-api.md`
- Full contract: [`api-contracts/tiktok-shop-web-api.md`](../api-contracts/tiktok-shop-web-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `15`
- Common capabilities: commerce / search / details / trends / rankings
- Default auth: Header `Authorization` Bearer
- Common inputs: `region`, `product_id`, `offset`, `seller_id`, `search_word`, `page_token`, `lang`, `count`, `sort_type`, `filter_id`
- Tag description: **(TikTok电商网页版数据接口/TikTok-Shop-Web-API data endpoints)**

## Routes

### `GET /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list`

- Summary: 获取热卖商品列表/Get hot selling products list
- Capabilities: trends / rankings / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-hot-selling-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-hot-selling-products-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| region | query | string | No | 地区代码/Region code |
| count | query | integer | No | 返回商品数量/Number of products to return |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail`

- Summary: 获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品ID/Product ID |
| seller_id | query | string | No | 卖家ID(可选)/Seller ID (optional) |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2`

- Summary: 获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品ID/Product ID |
| seller_id | query | string | No | 卖家ID(可选)/Seller ID (optional) |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3`

- Summary: 获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v3`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品ID/Product ID |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1`

- Summary: 获取商品评论V1/Get product reviews V1
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v1`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v1)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品ID/Product ID |
| sort_type | query | integer | No | 排序方式/Sort type: 1=相关性/Relevance, 2=最新/Recent |
| filter_id | query | string | No | 筛选ID/Filter ID |
| offset | query | integer | No | 分页偏移量/Offset for pagination |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2`

- Summary: 获取商品评论V2/Get product reviews V2
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品ID/Product ID |
| page_start | query | integer | No | 起始页码/Page start |
| sort_rule | query | integer | No | 排序规则/Sort rule |
| filter_type | query | integer | No | 筛选类型/Filter type: 1=默认, 2=有图片/视频, 3=真实购买 |
| filter_value | query | integer | No | 星级筛选/Star filter: 6=全部, 5-1=对应星级 |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id`

- Summary: 根据分类ID获取商品列表/Get products by category ID
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-by-category-id`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-by-category-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| category_id | query | integer | Yes | 分类ID/Category ID |
| offset | query | integer | No | 翻页偏移量/Offset for pagination |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_products_category_list`

- Summary: 获取商品分类列表/Get product category list
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-category-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-products-category-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list`

- Summary: 搜索商品列表V1/Search products list V1
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_word | query | string | Yes | 搜索关键词/Search keyword |
| offset | query | integer | No | 偏移量/Offset |
| page_token | query | string | No | 分页标记/Page token |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2`

- Summary: 搜索商品列表V2(移动端)/Search products list V2 (Mobile)
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_word | query | string | Yes | 搜索关键词/Search keyword |
| offset | query | integer | No | 偏移量/Offset |
| page_token | query | string | No | 分页标记/Page token |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3`

- Summary: 搜索商品列表V3/Search products list V3
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v3`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| offset | query | integer | No | 偏移量/Offset |
| region | query | string | No | 地区代码/Region code (Alpha-2) |
| sort_by | query | string | No | 排序方式/Sort by: RELEVANCE, PRICE_ASC, PRICE_DESC, BEST_SELLERS |
| filters_data | query | string | No | 筛选数据JSON/Filters data JSON |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion`

- Summary: 获取搜索关键词建议V1/Get search keyword suggestions V1
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_word | query | string | Yes | 搜索关键词/Search keyword |
| lang | query | string | No | 语言/Language |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2`

- Summary: 获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_word | query | string | Yes | 搜索关键词/Search keyword |
| lang | query | string | No | 语言/Language |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list`

- Summary: 获取商家商品列表V1/Get seller products list V1
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 卖家ID/Seller ID |
| search_params | query | string | No | 搜索参数(用于分页)/Search params (for pagination) |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2`

- Summary: 获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get`
- Full contract: [`api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list-v2`](../api-contracts/tiktok-shop-web-api.md#get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 卖家ID/Seller ID |
| searchParams | query | string | No | 搜索参数/Search params |
| region | query | string | No | 地区代码/Region code |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.
