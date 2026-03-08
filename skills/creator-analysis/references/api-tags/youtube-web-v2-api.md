# YouTube-Web-V2-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/youtube-web-v2-api.md`
- Full contract: [`api-contracts/youtube-web-v2-api.md`](../api-contracts/youtube-web-v2-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `16`
- Common capabilities: content details / profiles / accounts / search / livestream / comments
- Default auth: Header `Authorization` Bearer
- Common inputs: `continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query`
- Tag description: **(YouTube Web V2数据接口/YouTube-Web-V2-API endpoints)**

## Routes

### `GET /api/u1/v1/youtube/web_v2/get_channel_description`

- Summary: 获取频道描述信息/Get channel description
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_description_api_v1_youtube_web_v2_get_channel_description_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-description`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-description)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | No | 频道ID（格式如：UCeu6U67OzJhV1KwBansH3Dg），可通过get_channel_id接口从频道URL获取/Channel ID, can be obtained from channel URL via get_cha… |
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

### `GET /api/u1/v1/youtube/web_v2/get_channel_id`

- Summary: 从频道URL获取频道ID /Get channel ID from URL
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_id_api_v1_youtube_web_v2_get_channel_id_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-id`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-id)

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_shorts`

- Summary: 获取频道短视频列表/Get channel shorts
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-shorts`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-shorts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| channel_id | query | string | No | 频道ID/Channel ID (e.g., UCuAXFkgsw1L7xaCfnd5JJOw) |
| channel_url | query | string | No | 频道URL/Channel URL (如果提供channel_id则忽略/Ignored if channel_id is provided) |
| continuation_token | query | string | No | 分页token/Pagination token |
| need_format | query | boolean | No | 是否格式化数据/Whether to format data |

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_url`

- Summary: 从频道ID获取频道URL/Get channel URL from channel ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_url_api_v1_youtube_web_v2_get_channel_url_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-url`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-url)

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

### `GET /api/u1/v1/youtube/web_v2/get_channel_videos`

- Summary: 获取频道视频 /Get channel videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-videos`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-channel-videos)

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

### `GET /api/u1/v1/youtube/web_v2/get_general_search`

- Summary: 综合搜索（支持过滤条件）/General search with filters
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_general_search_api_v1_youtube_web_v2_get_general_search_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-general-search`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-general-search)

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

### `GET /api/u1/v1/youtube/web_v2/get_related_videos`

- Summary: 获取视频相似内容/Get related videos
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_related_videos_api_v1_youtube_web_v2_get_related_videos_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-related-videos`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-related-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | No | 视频ID/Video ID |
| video_url | query | string | No | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |
| need_format | query | boolean | No | 是否格式化数据。true: 返回格式化的结构化数据，false: 返回原始API结构/Whether to format data. true: return formatted structured data, false: retur… |

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

### `GET /api/u1/v1/youtube/web_v2/get_search_suggestions`

- Summary: 获取搜索推荐词/Get search suggestions
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-search-suggestions`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-search-suggestions)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| language | query | string | No | 语言代码/Language code (e.g., en, zh-cn, ja) |
| region | query | string | No | 地区代码/Region code (e.g., US, SG, CN, JP) |

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

### `GET /api/u1/v1/youtube/web_v2/get_shorts_search`

- Summary: YouTube Shorts短视频搜索/YouTube Shorts search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-shorts-search`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-shorts-search)

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

### `GET /api/u1/v1/youtube/web_v2/get_signed_stream_url`

- Summary: 获取已签名的视频流URL/Get signed video stream URL
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-signed-stream-url`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-signed-stream-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | No | 视频ID/Video ID |
| video_url | query | string | No | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |
| itag | query | integer | Yes | 格式标识符 itag (从 get_video_streams 接口获取)/Format identifier itag (obtained from get_video_streams endpoint) |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_comment_replies`

- Summary: 获取视频二级评论/Get video sub comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comment-replies`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comment-replies)

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

### `GET /api/u1/v1/youtube/web_v2/get_video_comments`

- Summary: 获取视频评论/Get video comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_comments_api_v1_youtube_web_v2_get_video_comments_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comments`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-comments)

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

### `GET /api/u1/v1/youtube/web_v2/get_video_info`

- Summary: 获取视频详情 /Get video information
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_info_api_v1_youtube_web_v2_get_video_info_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-info`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | Yes | 视频ID/Video ID |
| language_code | query | string | No | 语言代码（如zh-CN, en-US等）/Language code |
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

### `GET /api/u1/v1/youtube/web_v2/get_video_streams`

- Summary: 获取视频流信息/Get video streams info
- Capabilities: content details / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_streams_api_v1_youtube_web_v2_get_video_streams_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | No | 视频ID/Video ID |
| video_url | query | string | No | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |

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

### `GET /api/u1/v1/youtube/web_v2/get_video_streams_v2`

- Summary: 获取视频流信息 V2/Get video streams info V2
- Capabilities: content details / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams-v2`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-get-video-streams-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| video_id | query | string | No | 视频ID/Video ID |
| video_url | query | string | No | 视频URL/Video URL (如果提供video_id则忽略此参数/Ignored if video_id is provided) |

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

### `GET /api/u1/v1/youtube/web_v2/search_channels`

- Summary: 搜索频道/Search channels
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_channels_api_v1_youtube_web_v2_search_channels_get`
- Full contract: [`api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-search-channels`](../api-contracts/youtube-web-v2-api.md#get-api-u1-v1-youtube-web-v2-search-channels)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | No | 搜索关键词/Search keyword |
| continuation_token | query | string | No | 分页token/Pagination token |
| need_format | query | boolean | No | 是否格式化数据/Whether to format data |

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
