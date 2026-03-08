# Instagram-V1-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/instagram-v1-api.md`
- Full contract: [`api-contracts/instagram-v1-api.md`](../api-contracts/instagram-v1-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `29`
- Common capabilities: profiles / accounts / content details / general / comments / media / download / topics
- Default auth: Header `Authorization` Bearer
- Common inputs: `user_id`, `max_id`, `count`, `end_cursor`, `media_id`, `username`, `page`, `min_id`, `location_id`, `post_url`
- Tag description: **(Instagram V1数据接口（优先使用V1接口，V2接口仅在V1接口无法满足需求时使用）/Instagram-V1-API endpoints (Prefer using V1 endpoints, V2 endpoints are only for use when V1 endpoints cannot meet the requirements))**

## Routes

### `GET /api/u1/v1/instagram/v1/fetch_cities`

- Summary: 获取国家城市列表/Get cities by country
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_cities_api_v1_instagram_v1_fetch_cities_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-cities`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-cities)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| country_code | query | string | Yes | 国家代码（如US、CN、JP）/Country code (e.g. US, CN, JP) |
| page | query | integer | No | 页码/Page number |

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

### `GET /api/u1/v1/instagram/v1/fetch_comment_replies`

- Summary: 获取评论的子评论列表/Get comment replies
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-comment-replies`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | Yes | 帖子ID（媒体ID）/Post ID (Media ID) |
| comment_id | query | string | Yes | 父评论ID/Parent comment ID |
| min_id | query | string | No | 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id |

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

### `GET /api/u1/v1/instagram/v1/fetch_explore_sections`

- Summary: 获取探索页面分类/Get explore page sections
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-explore-sections`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-explore-sections)

#### Parameters

None

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

### `GET /api/u1/v1/instagram/v1/fetch_hashtag_posts`

- Summary: 获取话题标签下的帖子/Get posts by hashtag
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-hashtag-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-hashtag-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| hashtag | query | string | Yes | 话题标签名称（不含#号）/Hashtag name (without #) |
| end_cursor | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_location_info`

- Summary: 获取地点信息/Get location info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_location_info_api_v1_instagram_v1_fetch_location_info_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-location-info`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-location-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_location_posts`

- Summary: 获取地点下的帖子/Get posts by location
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-location-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-location-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID |
| tab | query | string | No | 排序方式：ranked(热门)/recent(最新)/Sorting: ranked(top)/recent(latest) |
| end_cursor | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_locations`

- Summary: 获取城市地点列表/Get locations by city
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_locations_api_v1_instagram_v1_fetch_locations_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-locations`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-locations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| city_id | query | string | Yes | 城市ID（从fetch_cities获取）/City ID (from fetch_cities) |
| page | query | integer | No | 页码/Page number |

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

### `GET /api/u1/v1/instagram/v1/fetch_music_posts`

- Summary: 获取使用特定音乐的帖子/Get posts using specific music
- Capabilities: content details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-music-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-music-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| music_id | query | string | No | 音乐ID/Music ID |
| music_url | query | string | No | 音乐URL（与music_id二选一）/Music URL (alternative to music_id) |
| max_id | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_post_by_id`

- Summary: 通过ID获取帖子详情/Get post by ID
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-id`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_post_by_url`

- Summary: 通过URL获取帖子详情/Get post by URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-url`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_url | query | string | Yes | 帖子URL/Post URL |

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

### `GET /api/u1/v1/instagram/v1/fetch_post_by_url_v2`

- Summary: 通过URL获取帖子详情 V2/Get post by URL V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-url-v2`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-by-url-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| post_url | query | string | Yes | 帖子URL/Post URL |

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

### `GET /api/u1/v1/instagram/v1/fetch_post_comments_v2`

- Summary: 获取帖子评论列表V2/Get post comments V2
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-comments-v2`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-post-comments-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | Yes | 帖子ID（媒体ID）/Post ID (Media ID) |
| sort_order | query | string | No | 排序方式：popular(热门)/recent(最新)/Sorting: popular/recent |
| min_id | query | string | No | 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id |

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

### `GET /api/u1/v1/instagram/v1/fetch_related_profiles`

- Summary: 获取相关用户推荐/Get related profiles
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-related-profiles`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-related-profiles)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_search`

- Summary: 搜索用户/话题/地点/Search users/hashtags/places
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_api_v1_instagram_v1_fetch_search_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-search`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword |
| select | query | string | No | 筛选类型：users/hashtags/places，不传则返回全部/Filter type: users/hashtags/places, omit for all |

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

### `GET /api/u1/v1/instagram/v1/fetch_section_posts`

- Summary: 获取分类下的帖子/Get posts by section
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-section-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-section-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| section_id | query | string | Yes | 分类ID（从fetch_explore_sections获取）/Section ID (from fetch_explore_sections) |
| count | query | integer | No | 每页数量/Count per page |
| max_id | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_about_info`

- Summary: 获取用户的About信息/Get user about info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-about-info`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-about-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id`

- Summary: 根据用户ID获取用户数据/Get user data by user ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-id`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id_v2`

- Summary: 根据用户ID获取用户数据V2/Get user data by user ID V2
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-id-v2`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-id-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username`

- Summary: 根据用户名获取用户数据/Get user data by username
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | Instagram用户名/Instagram username |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v2`

- Summary: 根据用户名获取用户数据V2/Get user data by username V2
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v2`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | Instagram用户名/Instagram username |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v3`

- Summary: 根据用户名获取用户数据V3/Get user data by username V3
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v3`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | Instagram用户名/Instagram username |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_posts`

- Summary: 获取用户帖子列表/Get user posts list
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |
| count | query | integer | No | 每页数量/Count per page |
| max_id | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_posts_v2`

- Summary: 获取用户帖子列表V2/Get user posts list V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-posts-v2`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-posts-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |
| count | query | integer | No | 每页数量/Count per page |
| end_cursor | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_reels`

- Summary: 获取用户Reels列表/Get user Reels list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-reels`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-reels)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |
| count | query | integer | No | 每页数量/Count per page |
| max_id | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_reposts`

- Summary: 获取用户转发列表/Get user reposts list
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-reposts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-reposts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |
| max_id | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/fetch_user_tagged_posts`

- Summary: 获取用户被标记的帖子/Get user tagged posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-tagged-posts`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-fetch-user-tagged-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | Instagram用户ID/Instagram user ID |
| count | query | integer | No | 每页数量/Count per page |
| end_cursor | query | string | No | 分页游标，用于获取下一页/Pagination cursor for next page |

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

### `GET /api/u1/v1/instagram/v1/media_id_to_shortcode`

- Summary: Media ID转Shortcode/Convert media ID to shortcode
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-media-id-to-shortcode`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-media-id-to-shortcode)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| media_id | query | string | Yes | 帖子Media ID/Post media ID |

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

### `GET /api/u1/v1/instagram/v1/shortcode_to_media_id`

- Summary: Shortcode转Media ID/Convert shortcode to media ID
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-shortcode-to-media-id`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-shortcode-to-media-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| shortcode | query | string | Yes | 帖子Shortcode/Post shortcode |

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

### `GET /api/u1/v1/instagram/v1/user_id_to_username`

- Summary: 用户ID转用户信息/Get user info by user ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `user_id_to_username_api_v1_instagram_v1_user_id_to_username_get`
- Full contract: [`api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-user-id-to-username`](../api-contracts/instagram-v1-api.md#get-api-u1-v1-instagram-v1-user-id-to-username)

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
