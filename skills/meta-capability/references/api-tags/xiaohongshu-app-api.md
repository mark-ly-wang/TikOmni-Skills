# Xiaohongshu-App-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/xiaohongshu-app-api.md`
- Full contract: [`api-contracts/xiaohongshu-app-api.md`](../api-contracts/xiaohongshu-app-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `12`
- Common capabilities: content details / profiles / accounts / comments / commerce / search / general
- Default auth: Header `Authorization` Bearer
- Common inputs: `note_id`, `session_id`, `share_link`, `start`, `share_text`, `sort`, `user_id`, `keyword`, `page`, `search_id`
- Tag description: **(小红书App数据接口/Xiaohongshu-App-API data endpoints)** - 第二优先/Second choice

## Routes

### `GET /api/u1/v1/xiaohongshu/app/extract_share_info`

- Summary: 提取分享链接信息/Extract share link info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-extract-share-info`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-extract-share-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/xiaohongshu/app/get_note_comments`

- Summary: 获取笔记评论/Get note comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-comments`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID |
| start | query | string | No | 翻页游标/Pagination cursor |
| sort_strategy | query | integer | No | 排序策略：1-默认排序，2-最新评论/Sort strategy: 1-default, 2-latest |

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

### `GET /api/u1/v1/xiaohongshu/app/get_note_info`

- Summary: 获取笔记信息 V1/Get note info V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-info`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-info)

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

### `GET /api/u1/v1/xiaohongshu/app/get_note_info_v2`

- Summary: 获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-info-v2`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-note-info-v2)

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

### `GET /api/u1/v1/xiaohongshu/app/get_notes_by_topic`

- Summary: [已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-notes-by-topic`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-notes-by-topic)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 话题标签ID/Topic tag ID |
| first_load_time | query | string | Yes | 首次请求时间戳（毫秒）/First load timestamp (ms) |
| sort | query | string | No | 排序方式：hot-综合，time-最新，trend-最热/Sort: hot-comprehensive, time-latest, trend-trending |
| session_id | query | string | No | 会话ID/Session ID |
| last_note_ct | query | string | No | 最后一条笔记创建时间/Last note create time |
| last_note_id | query | string | No | 最后一条笔记ID/Last note ID |
| cursor_score | query | string | No | 游标分数/Cursor score |

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

### `GET /api/u1/v1/xiaohongshu/app/get_product_detail`

- Summary: 获取商品详情/Get product detail
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-product-detail`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-product-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品skuId/Product SKU ID |

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

### `GET /api/u1/v1/xiaohongshu/app/get_sub_comments`

- Summary: 获取子评论/Get sub comments
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-sub-comments`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-sub-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| note_id | query | string | Yes | 笔记ID/Note ID |
| comment_id | query | string | Yes | 一级评论ID/Parent comment ID |
| start | query | string | No | 翻页游标/Pagination cursor |

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

### `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`

- Summary: 从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-id-and-xsec-token`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-id-and-xsec-token)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 用户分享链接/User share link |

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

### `GET /api/u1/v1/xiaohongshu/app/get_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_xiaohongshu_app_get_user_info_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-info`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID |

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

### `GET /api/u1/v1/xiaohongshu/app/get_user_notes`

- Summary: 获取用户作品列表/Get user notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-notes`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-get-user-notes)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID |
| cursor | query | string | No | 翻页游标/Pagination cursor |

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

### `GET /api/u1/v1/xiaohongshu/app/search_notes`

- Summary: 搜索笔记/Search notes
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_notes_api_v1_xiaohongshu_app_search_notes_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-search-notes`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-search-notes)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | Yes | 页码（从1开始）/Page number (start from 1) |
| search_id | query | string | No | 搜索ID，翻页时使用/Search ID for pagination |
| session_id | query | string | No | 会话ID，翻页时使用/Session ID for pagination |
| sort_type | query | string | No | 排序方式/Sort type |
| filter_note_type | query | string | No | 笔记类型筛选：不限、视频笔记、普通笔记/Note type filter |
| filter_note_time | query | string | No | 发布时间筛选：不限、一天内、一周内、半年内/Time filter |

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

### `GET /api/u1/v1/xiaohongshu/app/search_products`

- Summary: 搜索商品/Search products
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_products_api_v1_xiaohongshu_app_search_products_get`
- Full contract: [`api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-search-products`](../api-contracts/xiaohongshu-app-api.md#get-api-u1-v1-xiaohongshu-app-search-products)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | Yes | 页码（从1开始）/Page number (start from 1) |
| search_id | query | string | No | 搜索ID，翻页时使用/Search ID for pagination |
| session_id | query | string | No | 会话ID，翻页时使用/Session ID for pagination |
| sort | query | string | No | 排序规则：sales_qty-销量、price_asc-价格升序、price_desc-价格降序/Sort: sales_qty, price_asc, price_desc |
| scope | query | string | No | 搜索范围：purchased-买过的店、following-关注的店/Scope: purchased, following |
| service_guarantee | query | string | No | 物流权益，多选用英文逗号分割/Service guarantee, comma separated |
| min_price | query | string | No | 最低价/Min price |
| max_price | query | string | No | 最高价/Max price |
| super_promotion | query | string | No | 标签ID/Promotion tag ID |

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
