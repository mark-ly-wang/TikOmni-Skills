# Xigua-App-V2-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/xigua-app-v2-api.md`
- Full contract: [`api-contracts/xigua-app-v2-api.md`](../api-contracts/xigua-app-v2-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `7`
- Common capabilities: content details / profiles / accounts / comments / search
- Default auth: Header `Authorization` Bearer
- Common inputs: `item_id`, `user_id`, `offset`, `max_behot_time`, `count`, `keyword`, `order_type`, `min_duration`, `max_duration`
- Tag description: **(西瓜视频App V2数据接口/Xigua-App-V2-API data endpoints)**

## Routes

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_play_url`

- Summary: 获取单个作品的播放链接/Get single video play URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video-play-url`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video-play-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video-v2`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-one-video-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/xigua/app/v2/fetch_user_info`

- Summary: 个人信息/Personal information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-user-info`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-user-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户id/User id |

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

### `GET /api/u1/v1/xigua/app/v2/fetch_user_post_list`

- Summary: 获取个人作品列表/Get user post list
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-user-post-list`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-user-post-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户id/User id |
| max_behot_time | query | string | No | 最大行为时间/Maximum behavior time |

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

### `GET /api/u1/v1/xigua/app/v2/fetch_video_comment_list`

- Summary: 视频评论列表/Video comment list
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-video-comment-list`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-fetch-video-comment-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Count |

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

### `GET /api/u1/v1/xigua/app/v2/search_video`

- Summary: 搜索视频/Search video
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_video_api_v1_xigua_app_v2_search_video_get`
- Full contract: [`api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-search-video`](../api-contracts/xigua-app-v2-api.md#get-api-u1-v1-xigua-app-v2-search-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| order_type | query | string | No | 排序方式/Order type |
| min_duration | query | integer | No | 最小时长/Minimum duration |
| max_duration | query | integer | No | 最大时长/Maximum duration |

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
