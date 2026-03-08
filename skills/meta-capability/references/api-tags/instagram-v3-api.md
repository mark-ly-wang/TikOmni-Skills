# Instagram-V3-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/instagram-v3-api.md`
- Full contract: [`api-contracts/instagram-v3-api.md`](../api-contracts/instagram-v3-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `26`
- Common capabilities: profiles / accounts / content details / comments / search / general / topics
- Default auth: Header `Authorization` Bearer
- Common inputs: `user_id`, `username`, `url`, `first`, `after`, `query`, `media_id`, `code`, `max_id`, `comment_id`
- Tag description: **(Instagram V3数据接口/Instagram-V3-API endpoints)**

## Routes

### `GET /api/u1/v1/instagram/v3/bulk_translate_comments`

- Summary: 批量翻译评论/Bulk translate comments
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-bulk-translate-comments`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-bulk-translate-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| comment_ids | query | string | Yes | 评论ID列表，逗号分隔/Comment ID list, comma separated |

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

### `GET /api/u1/v1/instagram/v3/general_search`

- Summary: 综合搜索（支持分页）/General search (with pagination)
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `general_search_api_v1_instagram_v3_general_search_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-general-search`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-general-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword |
| next_max_id | query | string | No | 分页ID，首次请求不传，从上一次响应的next_max_id获取/Pagination ID, omit for first request, get from previous response next_max_id |
| rank_token | query | string | No | 排序token，首次请求不传，从上一次响应获取/Rank token, omit for first request, get from previous response |
| enable_metadata | query | boolean | No | 是否启用元数据/Enable metadata |

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

### `GET /api/u1/v1/instagram/v3/get_comment_replies`

- Summary: 获取评论的子评论/回复/Get comment replies
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_comment_replies_api_v1_instagram_v3_get_comment_replies_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-comment-replies`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID |
| code | query | string | No | 帖子短代码/Post shortcode |
| url | query | string | No | 帖子URL/Post URL |
| comment_id | query | string | Yes | 父评论ID/Parent comment ID |
| min_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_min_child_cursor 获取/Pagination cursor, omit for first request, get from previous response next… |

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

### `GET /api/u1/v1/instagram/v3/get_explore`

- Summary: 获取探索页推荐帖子/Get explore feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_explore_api_v1_instagram_v3_get_explore_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-explore`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-explore)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id |

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

### `GET /api/u1/v1/instagram/v3/get_highlight_stories`

- Summary: 获取Highlight精选详情/Get highlight stories
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-highlight-stories`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-highlight-stories)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| highlight_id | query | string | Yes | 精选ID/Highlight ID (格式/format: highlight:xxx) |
| reel_ids | query | string | No | 精选ID列表，逗号分隔，如不提供则仅查询highlight_id/Highlight ID list, comma separated, if not provided only query highlight_id |

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

### `GET /api/u1/v1/instagram/v3/get_location_info`

- Summary: 获取地点详情/Get location info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_location_info_api_v1_instagram_v3_get_location_info_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-location-info`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-location-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID |
| show_nearby | query | boolean | No | 是否显示附近地点/Whether to show nearby places |

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

### `GET /api/u1/v1/instagram/v3/get_location_posts`

- Summary: 获取地点相关帖子/Get location posts
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_location_posts_api_v1_instagram_v3_get_location_posts_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-location-posts`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-location-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID |
| tab | query | string | No | 帖子类型: ranked(热门), recent(最新)/Post type: ranked(top), recent(latest) |
| page_size_override | query | integer | No | 每页数量/Page size |

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

### `GET /api/u1/v1/instagram/v3/get_post_comments`

- Summary: 获取帖子评论/Get post comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_comments_api_v1_instagram_v3_get_post_comments_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-comments`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID |
| code | query | string | No | 帖子短代码/Post shortcode (e.g., DUajw4YkorV) |
| url | query | string | No | 帖子URL/Post URL |
| min_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_min_id 获取/Pagination cursor, omit for first request, get from previous response next_min_id |
| sort_order | query | string | No | 排序方式: popular(热门), newest(最新)/Sort order: popular, newest |

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

### `GET /api/u1/v1/instagram/v3/get_post_info`

- Summary: 获取帖子详情/Get post info (media_id or URL)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_info_api_v1_instagram_v3_get_post_info_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-info`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID |
| url | query | string | No | 帖子URL/Post URL |

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

### `GET /api/u1/v1/instagram/v3/get_post_info_by_code`

- Summary: 获取帖子详情(code)/Get post info by shortcode
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-info-by-code`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-info-by-code)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| code | query | string | No | 帖子短代码/Post shortcode |
| url | query | string | No | 帖子URL（自动提取短代码）/Post URL (auto extract shortcode) |

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

### `GET /api/u1/v1/instagram/v3/get_post_oembed`

- Summary: 获取帖子oEmbed内嵌信息/Get post oEmbed info
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_oembed_api_v1_instagram_v3_get_post_oembed_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-oembed`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-post-oembed)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| url | query | string | Yes | Instagram帖子的完整URL/Full URL of Instagram post |
| hidecaption | query | boolean | No | 是否隐藏帖子文本/Whether to hide caption |
| maxwidth | query | integer | No | 最大宽度（像素）/Max width in pixels |

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

### `GET /api/u1/v1/instagram/v3/get_recommended_reels`

- Summary: 获取Reels推荐列表/Get recommended Reels feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-recommended-reels`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-recommended-reels)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| first | query | integer | No | 获取数量/Number of reels to fetch |
| after | query | string | No | 分页游标，首次请求不传，从上一次响应的 page_info.end_cursor 获取/Pagination cursor, omit for first request, get from previous response page_… |

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

### `GET /api/u1/v1/instagram/v3/get_user_about`

- Summary: 获取用户账户简介/Get user about info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_about_api_v1_instagram_v3_get_user_about_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-about`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-about)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |

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

### `GET /api/u1/v1/instagram/v3/get_user_brief`

- Summary: 获取用户短详情/Get user brief info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_brief_api_v1_instagram_v3_get_user_brief_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-brief`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-brief)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID |
| username | query | string | Yes | 用户名/Username |

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

### `GET /api/u1/v1/instagram/v3/get_user_followers`

- Summary: 获取用户粉丝列表/Get user followers list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_followers_api_v1_instagram_v3_get_user_followers_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-followers`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-followers)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| count | query | integer | No | 每次获取数量/Number of users to fetch per request |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id |

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

### `GET /api/u1/v1/instagram/v3/get_user_following`

- Summary: 获取用户关注列表/Get user following list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_following_api_v1_instagram_v3_get_user_following_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-following`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-following)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| count | query | integer | No | 每次获取数量/Number of users to fetch per request |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id |

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

### `GET /api/u1/v1/instagram/v3/get_user_highlights`

- Summary: 获取用户精选Highlights列表/Get user highlights
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_highlights_api_v1_instagram_v3_get_user_highlights_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-highlights`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-highlights)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| first | query | integer | No | 获取数量/Number of highlights to fetch |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) |

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

### `GET /api/u1/v1/instagram/v3/get_user_posts`

- Summary: 获取用户帖子列表/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posts_api_v1_instagram_v3_get_user_posts_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-posts`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username |
| user_id | query | string | No | 用户ID/User ID |
| first | query | integer | No | 获取帖子数量/Number of posts to fetch |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) |

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

### `GET /api/u1/v1/instagram/v3/get_user_profile`

- Summary: 获取用户信息/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_api_v1_instagram_v3_get_user_profile_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-profile`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |

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

### `GET /api/u1/v1/instagram/v3/get_user_reels`

- Summary: 获取用户Reels列表/Get user reels
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_reels_api_v1_instagram_v3_get_user_reels_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-reels`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-reels)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| first | query | integer | No | 获取数量/Number of reels to fetch |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) |

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

### `GET /api/u1/v1/instagram/v3/get_user_stories`

- Summary: 获取用户Stories（快拍）/Get user stories
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_stories_api_v1_instagram_v3_get_user_stories_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-stories`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-stories)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| reel_ids | query | string | No | 用户ID列表，逗号分隔，可同时获取多个用户的Stories（如不提供则仅查询user_id）/User ID list, comma separated, fetch multiple users' stories at once (if… |

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

### `GET /api/u1/v1/instagram/v3/get_user_tagged_posts`

- Summary: 获取用户被标记的帖子/Get user tagged posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-tagged-posts`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-get-user-tagged-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID |
| username | query | string | No | 用户名/Username |
| first | query | integer | No | 获取帖子数量/Number of posts to fetch |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) |

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

### `GET /api/u1/v1/instagram/v3/search_hashtags`

- Summary: 搜索话题标签/Search hashtags
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_hashtags_api_v1_instagram_v3_search_hashtags_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-hashtags`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-hashtags)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/instagram/v3/search_places`

- Summary: 搜索地点/Search places
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_places_api_v1_instagram_v3_search_places_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-places`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-places)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/instagram/v3/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_instagram_v3_search_users_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-users`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-search-users)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/instagram/v3/translate_comment`

- Summary: 翻译评论/帖子文本/Translate comment or caption
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `translate_comment_api_v1_instagram_v3_translate_comment_get`
- Full contract: [`api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-translate-comment`](../api-contracts/instagram-v3-api.md#get-api-u1-v1-instagram-v3-translate-comment)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| comment_id | query | string | Yes | 帖子媒体ID/Post media ID |

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
