# YouTube-Web-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/youtube-web-api.md`
- Full contract: [`api-contracts/youtube-web-api.md`](../api-contracts/youtube-web-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `21`
- Common capabilities: content details / profiles / accounts / search / comments / trends / rankings / subtitles / transcription
- Default auth: Header `Authorization` Bearer
- Common inputs: `continuation_token`, `language_code`, `country_code`, `channel_id`, `video_id`, `need_format`, `search_query`, `sort_by`, `lang`, `time_zone`
- Tag description: **(YouTube Web数据接口/YouTube-Web-API endpoints)**

## Routes

### `GET /api/u1/v1/youtube/web/get_channel_description`

- Summary: 获取频道描述信息/Get channel description
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_description_api_v1_youtube_web_get_channel_description_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-description`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-description)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | No | 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id_v2接口从频道URL获取/Channel ID, can be obtained from channel URL via get_… |
| continuation_token | query | string | No | 翻页标志（用于获取频道注册时间等高级信息）/Continuation token for getting advanced info like channel creation date |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, JP等）/Country code |
| need_format | query | boolean | No | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web/get_channel_id`

- Summary: 获取频道ID/Get channel ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_id_api_v1_youtube_web_get_channel_id_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-id`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_name | query | string | Yes | 频道名称/Channel name |

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

### `GET /api/u1/v1/youtube/web/get_channel_id_v2`

- Summary: 从频道URL获取频道ID V2/Get channel ID from URL V2
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-id-v2`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-id-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_url | query | string | Yes | 频道URL/Channel URL，支持多种格式如：https://www.youtube.com/@username, https://www.youtube.com/channel/UCxxxxxx, https://www.yout… |

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

### `GET /api/u1/v1/youtube/web/get_channel_info`

- Summary: 获取频道信息/Get channel information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_info_api_v1_youtube_web_get_channel_info_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-info`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |

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

### `GET /api/u1/v1/youtube/web/get_channel_short_videos`

- Summary: 获取频道短视频/Get channel short videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-short-videos`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-short-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/get_channel_url`

- Summary: 从频道ID获取频道URL/Get channel URL from channel ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_url_api_v1_youtube_web_get_channel_url_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-url`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID (格式如：UCeu6U67OzJhV1KwBansH3Dg) |

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

### `GET /api/u1/v1/youtube/web/get_channel_videos`

- Summary: 获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_videos_api_v1_youtube_web_get_channel_videos_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/get_channel_videos_v2`

- Summary: 获取频道视频 V2/Get channel videos V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos-v2`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |
| lang | query | string | No | 视频结果语言代码/Video result language code |
| sortBy | query | string | No | 排序方式/Sort by |
| contentType | query | string | No | 内容类型/Content type |
| nextToken | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/get_channel_videos_v3`

- Summary: 获取频道视频 V3/Get channel videos V3
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos-v3`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-channel-videos-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, JP等）/Country code |
| continuation_token | query | string | No | 分页token，用于获取下一页/Pagination token for next page |
| need_format | query | boolean | No | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web/get_general_search`

- Summary: 综合搜索（支持过滤条件）/General search with filters
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_general_search_api_v1_youtube_web_get_general_search_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-general-search`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-general-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_query | query | string | Yes | 搜索关键字/Search keyword |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, CN等）/Country code |
| time_zone | query | string | No | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone |
| upload_time | query | string enum[hour, today, week, month, year] | No | 上传时间过滤 \| Upload time filter |
| duration | query | string enum[short, medium, long] | No | 视频时长过滤 \| Duration filter |
| content_type | query | string enum[video, channel, playlist, movie] | No | 内容类型过滤 \| Content type filter |
| feature | query | string enum[live, 4k, hd, subtitles, creative_commons, 360, ...] | No | 特征过滤 \| Feature filter |
| sort_by | query | string enum[relevance, upload_date, view_count, rating] | No | 排序方式 \| Sort by |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/get_relate_video`

- Summary: 获取推荐视频/Get related videos
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_relate_video_api_v1_youtube_web_get_relate_video_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-relate-video`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-relate-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/get_shorts_search`

- Summary: YouTube Shorts短视频搜索/YouTube Shorts search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_shorts_search_api_v1_youtube_web_get_shorts_search_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-shorts-search`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-shorts-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_query | query | string | Yes | 搜索关键字/Search keyword |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, CN等）/Country code |
| time_zone | query | string | No | 时区（如America/Los_Angeles, Asia/Shanghai等）/Time zone |
| upload_time | query | string enum[hour, today, week, month, year] | No | 上传时间过滤 \| Upload time filter for Shorts |
| sort_by | query | string enum[relevance, upload_date, view_count, rating] | No | 排序方式 \| Sort by for Shorts |
| continuation_token | query | string | No | 翻页令牌/Pagination token |
| filter_mixed_content | query | boolean | No | 是否过滤混合内容（长视频），默认True / Filter mixed content (long videos), default True |

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

### `GET /api/u1/v1/youtube/web/get_trending_videos`

- Summary: 获取趋势视频/Get trending videos
- Capabilities: trends / rankings / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_trending_videos_api_v1_youtube_web_get_trending_videos_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-trending-videos`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-trending-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| language_code | query | string | No | 语言代码/Language code |
| country_code | query | string | No | 国家代码/Country code |
| section | query | string | No | 类型/Section |

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

### `GET /api/u1/v1/youtube/web/get_video_comment_replies`

- Summary: 获取视频二级评论/Get video sub comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-comment-replies`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| continuation_token | query | string | Yes | 回复的continuation token（从一级评论的reply_continuation_token字段获取）/Reply continuation token from first-level comment |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, JP等）/Country code |
| need_format | query | boolean | No | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web/get_video_comments`

- Summary: 获取视频评论/Get video comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_comments_api_v1_youtube_web_get_video_comments_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-comments`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
| country_code | query | string | No | 国家代码（如US, JP等）/Country code |
| sort_by | query | string enum[top, newest] | No | 排序方式 \| Sort by |
| continuation_token | query | string | No | 翻页令牌/Pagination token |
| need_format | query | boolean | No | 是否需要清洗数据，提取关键内容，移除冗余数据/Whether to clean and format the data |

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

### `GET /api/u1/v1/youtube/web/get_video_info`

- Summary: 获取视频信息 V1/Get video information V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_info_api_v1_youtube_web_get_video_info_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |
| url_access | query | string enum[normal, blocked] | No | URL访问模式：normal（包含音视频URL）\| blocked（不包含音视频URL） / URL access mode |
| lang | query | string | No | 语言代码（IETF标签），默认en-US / Language code |
| videos | query | string enum[auto, true, raw, false] | No | 视频格式：auto（自动）\| true（简化格式）\| raw（原始格式）\| false（不获取） / Video format selection |
| audios | query | string enum[auto, true, raw, false] | No | 音频格式：auto（自动）\| true（简化格式）\| raw（原始格式）\| false（不获取） / Audio format selection |
| subtitles | query | boolean | No | 是否获取字幕 / Include subtitles |
| related | query | boolean | No | 是否获取相关视频 / Include related content |

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

### `GET /api/u1/v1/youtube/web/get_video_info_v2`

- Summary: 获取视频信息 V2/Get video information V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info-v2`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |

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

### `GET /api/u1/v1/youtube/web/get_video_info_v3`

- Summary: 获取视频详情 V3/Get video information V3
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info-v3`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-info-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |

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

### `GET /api/u1/v1/youtube/web/get_video_subtitles`

- Summary: 获取视频字幕/Get video subtitles
- Capabilities: subtitles / transcription / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-subtitles`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-get-video-subtitles)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| subtitle_url | query | string | Yes | 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details |
| format | query | string enum[srt, xml, vtt, txt] | No | 字幕格式：srt/xml/vtt/txt / Subtitle format |
| fix_overlap | query | boolean | No | 修复重叠字幕（默认开启） / Fix overlapping subtitles |
| target_lang | query | string | No | 目标语言代码（留空保持原语言） / Target language code |

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

### `GET /api/u1/v1/youtube/web/search_channel`

- Summary: 搜索频道/Search channel
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_channel_api_v1_youtube_web_search_channel_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-search-channel`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-search-channel)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | Yes | 频道ID/Channel ID |
| search_query | query | string | Yes | 搜索关键字/Search keyword |
| language_code | query | string | No | 语言代码/Language code |
| country_code | query | string | No | 国家代码/Country code |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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

### `GET /api/u1/v1/youtube/web/search_video`

- Summary: 搜索视频/Search video
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_video_api_v1_youtube_web_search_video_get`
- Full contract: [`api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-search-video`](../api-contracts/youtube-web-api.md#get-api-u1-v1-youtube-web-search-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| search_query | query | string | Yes | 搜索关键字/Search keyword |
| language_code | query | string | No | 语言代码/Language code |
| order_by | query | string | No | 排序方式/Order by |
| country_code | query | string | No | 国家代码/Country code |
| continuation_token | query | string | No | 翻页令牌/Pagination token |

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
