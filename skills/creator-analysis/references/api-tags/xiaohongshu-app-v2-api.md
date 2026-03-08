# Xiaohongshu-App-V2-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/xiaohongshu-app-v2-api.md`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md`](../api-contracts/xiaohongshu-app-v2-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `21`
- Common capabilities: content details / commerce / search / details / profiles / accounts / creators
- Default auth: Header `Authorization` Bearer
- Common inputs: `source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab`
- Tag description: **(小红书App V2数据接口/Xiaohongshu-App-V2-API data endpoints)** ⭐ 推荐优先使用/Recommended first choice - 稳定性最高、功能最全/Most stable and feature-rich

## Routes

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`

- Summary: 获取创作者热点灵感列表/Get creator hot inspiration feed
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_hot_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_hot_inspiration_feed_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-hot-inspiration-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-hot-inspiration-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed`

- Summary: 获取创作者推荐灵感列表/Get creator inspiration feed
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_inspiration_feed_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-inspiration-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-inspiration-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| tab | query | integer | No | 标签类型/Tab type |
| source | query | string | No | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`

- Summary: 获取图文笔记详情/Get image note detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_image_note_detail_api_v1_xiaohongshu_app_v2_get_image_note_detail_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-image-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-image-note-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID |
| share_text | query | string | No | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`

- Summary: 获取首页推荐流笔记详情/Get mixed note detail from feed
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_mixed_note_detail_api_v1_xiaohongshu_app_v2_get_mixed_note_detail_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-mixed-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-mixed-note-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID |
| share_text | query | string | No | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_comments`

- Summary: 获取笔记评论列表/Get note comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_comments_api_v1_xiaohongshu_app_v2_get_note_comments_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-comments`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID |
| share_text | query | string | No | 分享链接/Share link |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| index | query | integer | No | 评论索引，首次请求传0/Comment index, pass 0 for first request |
| sort_strategy | query | string | No | 排序策略/Sort strategy: default, latest_v2, like_count |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments`

- Summary: 获取笔记二级评论列表/Get note sub comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_sub_comments_api_v1_xiaohongshu_app_v2_get_note_sub_comments_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-sub-comments`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-sub-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID |
| share_text | query | string | No | 分享链接/Share link |
| comment_id | query | string | Yes | 父评论ID/Parent comment ID |
| cursor | query | string | No | 分页游标，首次留空，翻页时从$.data.data.cursor中提取cursor值/Pagination cursor, leave empty for first request, extract cursor from $.data… |
| index | query | integer | No | 分页索引，首次传1，翻页时从$.data.data.cursor中提取index值/Pagination index, pass 1 for first request, extract index from $.data.cursor… |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_detail`

- Summary: 获取商品详情/Get product detail
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_detail_api_v1_xiaohongshu_app_v2_get_product_detail_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID |
| source | query | string | No | 来源/Source |
| pre_page | query | string | No | 前置页面/Previous page |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations`

- Summary: 获取商品推荐列表/Get product recommendations
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_recommendations_api_v1_xiaohongshu_app_v2_get_product_recommendations_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-recommendations`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-recommendations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID |
| cursor_score | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| region | query | string | No | 地区/Region |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview`

- Summary: 获取商品评论总览/Get product review overview
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_review_overview_api_v1_xiaohongshu_app_v2_get_product_review_overview_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-review-overview`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-review-overview)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID |
| tab | query | integer | No | 标签类型/Tab type |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_reviews`

- Summary: 获取商品评论列表/Get product reviews
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_reviews_api_v1_xiaohongshu_app_v2_get_product_reviews_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-reviews`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-reviews)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID |
| page | query | integer | No | 页码，从0开始/Page number, start from 0 |
| sort_strategy_type | query | integer | No | 排序策略：0=综合排序, 1=最新排序/Sort strategy: 0=general, 1=latest |
| share_pics_only | query | integer | No | 仅看有图评论：0=否, 1=是/Show reviews with images only: 0=no, 1=yes |
| from_page | query | string | No | 来源页面/From page |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_feed`

- Summary: 获取话题笔记列表/Get topic feed
- Capabilities: topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_topic_feed_api_v1_xiaohongshu_app_v2_get_topic_feed_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-feed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 话题页面ID/Topic page ID |
| sort | query | string | No | 排序方式/Sort: trend(最热), time(最新) |
| cursor_score | query | string | No | 分页游标分数，翻页时传入/Pagination cursor score for next page |
| last_note_id | query | string | No | 上一页最后一条笔记ID，翻页时传入/Last note ID from previous page |
| last_note_ct | query | string | No | 上一页最后一条笔记创建时间，翻页时传入/Last note create time from previous page |
| session_id | query | string | No | 会话ID，翻页时保持一致/Session ID, keep consistent for pagination |
| first_load_time | query | string | No | 首次加载时间戳，翻页时保持一致/First load timestamp, keep consistent for pagination |
| source | query | string | No | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_info`

- Summary: 获取话题详情/Get topic info
- Capabilities: topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_topic_info_api_v1_xiaohongshu_app_v2_get_topic_info_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-info`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 话题页面ID/Topic page ID |
| source | query | string | No | 来源/Source |
| note_id | query | string | No | 来源笔记ID，从笔记跳转到话题时传入/Source note ID, pass when jumping from note to topic |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes`

- Summary: 获取用户收藏笔记列表/Get user faved notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_faved_notes_api_v1_xiaohongshu_app_v2_get_user_faved_notes_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-faved-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-faved-notes)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| share_text | query | string | No | 分享链接/Share link |
| cursor | query | string | No | 分页游标，首次请求留空，翻页时传入上一页最后一条笔记的note_id/Pagination cursor, leave empty for first request, pass last note_id from previous pa… |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_xiaohongshu_app_v2_get_user_info_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-info`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| share_text | query | string | No | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`

- Summary: 获取用户笔记列表/Get user posted notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posted_notes_api_v1_xiaohongshu_app_v2_get_user_posted_notes_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-posted-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-posted-notes)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| share_text | query | string | No | 分享链接/Share link |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`

- Summary: 获取视频笔记详情/Get video note detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_note_detail_api_v1_xiaohongshu_app_v2_get_video_note_detail_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-video-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-video-note-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID |
| share_text | query | string | No | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_groups`

- Summary: 搜索群聊/Search groups
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_groups_api_v1_xiaohongshu_app_v2_search_groups_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-groups`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-groups)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page_no | query | integer | No | 页码，从0开始/Page number, start from 0 |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | No | 来源/Source |
| is_recommend | query | integer | No | 是否推荐：0=否, 1=是/Is recommend: 0=no, 1=yes |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_images`

- Summary: 搜索图片/Search images
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_images_api_v1_xiaohongshu_app_v2_search_images_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-images`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-images)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| search_session_id | query | string | No | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination |
| word_request_id | query | string | No | 词请求ID，翻页时传入首次搜索返回的值/Word request ID for pagination |
| source | query | string | No | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_notes`

- Summary: 搜索笔记/Search notes
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_notes_api_v1_xiaohongshu_app_v2_search_notes_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-notes)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 |
| sort_type | query | string | No | 排序方式/Sort type |
| note_type | query | string | No | 笔记类型/Note type: 不限, 视频笔记, 普通笔记, 直播笔记 |
| time_filter | query | string | No | 发布时间筛选/Time filter: 不限, 一天内, 一周内, 半年内 |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| search_session_id | query | string | No | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination |
| source | query | string | No | 来源/Source |
| ai_mode | query | integer | No | AI模式：0=关闭, 1=开启/AI mode: 0=off, 1=on |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_products`

- Summary: 搜索商品/Search products
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_products_api_v1_xiaohongshu_app_v2_search_products_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-products`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-products)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | No | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_xiaohongshu_app_v2_search_users_get`
- Full contract: [`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-users`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-users)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | No | 来源/Source |

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
