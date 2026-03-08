# Xiaohongshu-App-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xiaohongshu-app-v2-api.md`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md`](../api-contracts/xiaohongshu-app-v2-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`21`
- 常见能力：作品详情 / 电商 / 搜索 / 详情 / 主页/账号 / 创作者
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab`
- 标签说明：**(小红书App V2数据接口/Xiaohongshu-App-V2-API data endpoints)** ⭐ 推荐优先使用/Recommended first choice - 稳定性最高、功能最全/Most stable and feature-rich

## 路由列表

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`

- 摘要：获取创作者热点灵感列表/Get creator hot inspiration feed
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_hot_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_hot_inspiration_feed_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-hot-inspiration-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-hot-inspiration-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cursor | query | string | 否 | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed`

- 摘要：获取创作者推荐灵感列表/Get creator inspiration feed
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_inspiration_feed_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-inspiration-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-creator-inspiration-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cursor | query | string | 否 | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| tab | query | integer | 否 | 标签类型/Tab type |
| source | query | string | 否 | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`

- 摘要：获取图文笔记详情/Get image note detail
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_image_note_detail_api_v1_xiaohongshu_app_v2_get_image_note_detail_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-image-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-image-note-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID |
| share_text | query | string | 否 | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`

- 摘要：获取首页推荐流笔记详情/Get mixed note detail from feed
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_mixed_note_detail_api_v1_xiaohongshu_app_v2_get_mixed_note_detail_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-mixed-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-mixed-note-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID |
| share_text | query | string | 否 | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_comments`

- 摘要：获取笔记评论列表/Get note comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_comments_api_v1_xiaohongshu_app_v2_get_note_comments_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-comments`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID |
| share_text | query | string | 否 | 分享链接/Share link |
| cursor | query | string | 否 | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| index | query | integer | 否 | 评论索引，首次请求传0/Comment index, pass 0 for first request |
| sort_strategy | query | string | 否 | 排序策略/Sort strategy: default, latest_v2, like_count |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments`

- 摘要：获取笔记二级评论列表/Get note sub comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_sub_comments_api_v1_xiaohongshu_app_v2_get_note_sub_comments_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-sub-comments`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-note-sub-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID |
| share_text | query | string | 否 | 分享链接/Share link |
| comment_id | query | string | 是 | 父评论ID/Parent comment ID |
| cursor | query | string | 否 | 分页游标，首次留空，翻页时从$.data.data.cursor中提取cursor值/Pagination cursor, leave empty for first request, extract cursor from $.data… |
| index | query | integer | 否 | 分页索引，首次传1，翻页时从$.data.data.cursor中提取index值/Pagination index, pass 1 for first request, extract index from $.data.cursor… |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_detail`

- 摘要：获取商品详情/Get product detail
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_detail_api_v1_xiaohongshu_app_v2_get_product_detail_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sku_id | query | string | 是 | 商品SKU ID/Product SKU ID |
| source | query | string | 否 | 来源/Source |
| pre_page | query | string | 否 | 前置页面/Previous page |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations`

- 摘要：获取商品推荐列表/Get product recommendations
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_recommendations_api_v1_xiaohongshu_app_v2_get_product_recommendations_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-recommendations`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-recommendations)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sku_id | query | string | 是 | 商品SKU ID/Product SKU ID |
| cursor_score | query | string | 否 | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |
| region | query | string | 否 | 地区/Region |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview`

- 摘要：获取商品评论总览/Get product review overview
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_review_overview_api_v1_xiaohongshu_app_v2_get_product_review_overview_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-review-overview`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-review-overview)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sku_id | query | string | 是 | 商品SKU ID/Product SKU ID |
| tab | query | integer | 否 | 标签类型/Tab type |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_reviews`

- 摘要：获取商品评论列表/Get product reviews
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_reviews_api_v1_xiaohongshu_app_v2_get_product_reviews_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-reviews`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-product-reviews)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sku_id | query | string | 是 | 商品SKU ID/Product SKU ID |
| page | query | integer | 否 | 页码，从0开始/Page number, start from 0 |
| sort_strategy_type | query | integer | 否 | 排序策略：0=综合排序, 1=最新排序/Sort strategy: 0=general, 1=latest |
| share_pics_only | query | integer | 否 | 仅看有图评论：0=否, 1=是/Show reviews with images only: 0=no, 1=yes |
| from_page | query | string | 否 | 来源页面/From page |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_feed`

- 摘要：获取话题笔记列表/Get topic feed
- 能力：话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_topic_feed_api_v1_xiaohongshu_app_v2_get_topic_feed_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-feed`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-feed)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page_id | query | string | 是 | 话题页面ID/Topic page ID |
| sort | query | string | 否 | 排序方式/Sort: trend(最热), time(最新) |
| cursor_score | query | string | 否 | 分页游标分数，翻页时传入/Pagination cursor score for next page |
| last_note_id | query | string | 否 | 上一页最后一条笔记ID，翻页时传入/Last note ID from previous page |
| last_note_ct | query | string | 否 | 上一页最后一条笔记创建时间，翻页时传入/Last note create time from previous page |
| session_id | query | string | 否 | 会话ID，翻页时保持一致/Session ID, keep consistent for pagination |
| first_load_time | query | string | 否 | 首次加载时间戳，翻页时保持一致/First load timestamp, keep consistent for pagination |
| source | query | string | 否 | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_info`

- 摘要：获取话题详情/Get topic info
- 能力：话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_topic_info_api_v1_xiaohongshu_app_v2_get_topic_info_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-info`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-topic-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page_id | query | string | 是 | 话题页面ID/Topic page ID |
| source | query | string | 否 | 来源/Source |
| note_id | query | string | 否 | 来源笔记ID，从笔记跳转到话题时传入/Source note ID, pass when jumping from note to topic |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes`

- 摘要：获取用户收藏笔记列表/Get user faved notes
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_faved_notes_api_v1_xiaohongshu_app_v2_get_user_faved_notes_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-faved-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-faved-notes)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID |
| share_text | query | string | 否 | 分享链接/Share link |
| cursor | query | string | 否 | 分页游标，首次请求留空，翻页时传入上一页最后一条笔记的note_id/Pagination cursor, leave empty for first request, pass last note_id from previous pa… |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`

- 摘要：获取用户信息/Get user info
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_info_api_v1_xiaohongshu_app_v2_get_user_info_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-info`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID |
| share_text | query | string | 否 | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`

- 摘要：获取用户笔记列表/Get user posted notes
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_posted_notes_api_v1_xiaohongshu_app_v2_get_user_posted_notes_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-posted-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-user-posted-notes)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户ID/User ID |
| share_text | query | string | 否 | 分享链接/Share link |
| cursor | query | string | 否 | 分页游标，首次请求留空/Pagination cursor, leave empty for first request |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`

- 摘要：获取视频笔记详情/Get video note detail
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_note_detail_api_v1_xiaohongshu_app_v2_get_video_note_detail_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-video-note-detail`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-get-video-note-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID |
| share_text | query | string | 否 | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_groups`

- 摘要：搜索群聊/Search groups
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_groups_api_v1_xiaohongshu_app_v2_search_groups_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-groups`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-groups)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page_no | query | integer | 否 | 页码，从0开始/Page number, start from 0 |
| search_id | query | string | 否 | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | 否 | 来源/Source |
| is_recommend | query | integer | 否 | 是否推荐：0=否, 1=是/Is recommend: 0=no, 1=yes |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_images`

- 摘要：搜索图片/Search images
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_images_api_v1_xiaohongshu_app_v2_search_images_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-images`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-images)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | 否 | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| search_session_id | query | string | 否 | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination |
| word_request_id | query | string | 否 | 词请求ID，翻页时传入首次搜索返回的值/Word request ID for pagination |
| source | query | string | 否 | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_notes`

- 摘要：搜索笔记/Search notes
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_notes_api_v1_xiaohongshu_app_v2_search_notes_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-notes`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-notes)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码，从1开始/Page number, start from 1 |
| sort_type | query | string | 否 | 排序方式/Sort type |
| note_type | query | string | 否 | 笔记类型/Note type: 不限, 视频笔记, 普通笔记, 直播笔记 |
| time_filter | query | string | 否 | 发布时间筛选/Time filter: 不限, 一天内, 一周内, 半年内 |
| search_id | query | string | 否 | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| search_session_id | query | string | 否 | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination |
| source | query | string | 否 | 来源/Source |
| ai_mode | query | integer | 否 | AI模式：0=关闭, 1=开启/AI mode: 0=off, 1=on |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_products`

- 摘要：搜索商品/Search products
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_products_api_v1_xiaohongshu_app_v2_search_products_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-products`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-products)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | 否 | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | 否 | 来源/Source |

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

### `GET /api/u1/v1/xiaohongshu/app_v2/search_users`

- 摘要：搜索用户/Search users
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_users_api_v1_xiaohongshu_app_v2_search_users_get`
- 完整契约：[`api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-users`](../api-contracts/xiaohongshu-app-v2-api.md#get-api-u1-v1-xiaohongshu-app-v2-search-users)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码，从1开始/Page number, start from 1 |
| search_id | query | string | 否 | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination |
| source | query | string | 否 | 来源/Source |

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
