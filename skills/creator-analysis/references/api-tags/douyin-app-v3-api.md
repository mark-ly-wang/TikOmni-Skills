# Douyin-App-V3-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-app-v3-api.md`
- Full contract: [`api-contracts/douyin-app-v3-api.md`](../api-contracts/douyin-app-v3-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `47`
- Common capabilities: content details / search / profiles / accounts / details / trends / rankings / music / audio
- Default auth: Header `Authorization` Bearer
- Common inputs: `count`, `cursor`, `keyword`, `aweme_id`, `sec_user_id`, `offset`, `sort_type`, `publish_time`, `filter_duration`, `aweme_ids`
- Tag description: **(抖音-App-V3数据接口（当前最新版本）/Douyin-App-V3-API (Current latest version))**

## Routes

### `GET /api/u1/v1/douyin/app/v3/add_video_play_count`

- Summary: 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-add-video-play-count`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-add-video-play-count)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_type | query | integer | Yes | 作品类型/Video type |
| item_id | query | string | Yes | 作品id/Video id |
| cookie | query | string | No | 可选，默认使用游客Cookie/Optional, use guest Cookie by default |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list`

- Summary: 获取抖音品牌热榜分类数据/Get Douyin brand hot search list data
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list)

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

### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list_detail`

- Summary: 获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data
- Capabilities: search / trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| category_id | query | integer | Yes | 分类id/Category id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_general_search_result`

- Summary: 获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-general-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-general-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| sort_type | query | string | No | 排序类型/Sort type |
| publish_time | query | string | No | 发布时间/Publish time |
| filter_duration | query | string | No | 时长/Duration |
| content_type | query | string | No | 内容类型/Content type |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_detail`

- Summary: 获取指定话题的详情数据/Get details of specified hashtag
- Capabilities: details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| ch_id | query | integer | Yes | 话题id/Hashtag id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_search_result`

- Summary: 获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_video_list`

- Summary: 获取指定话题的作品数据/Get video list of specified hashtag
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-video-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hashtag-video-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| ch_id | query | string | Yes | 话题id/Hashtag id |
| cursor | query | integer | No | 游标/Cursor |
| sort_type | query | integer | No | 排序类型/Sort type |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_hot_search_list`

- Summary: 获取抖音热搜榜数据/Get Douyin hot search list data
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hot-search-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-hot-search-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| board_type | query | string | No | 榜单类型/Board type |
| board_sub_type | query | string | No | 榜单子类型/Board sub type |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_live_hot_search_list`

- Summary: 获取抖音直播热搜榜数据/Get Douyin live hot search list data
- Capabilities: search / trends / rankings / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-live-hot-search-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-live-hot-search-list)

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

### `GET /api/u1/v1/douyin/app/v3/fetch_live_search_result`

- Summary: 获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-live-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-live-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| cursor | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video`

- Summary: 批量获取视频信息 V1/Batch Get Video Information V1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post`
- Full contract: [`api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video`](../api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| [] | array<string> | Yes | None |

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

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url`

- Summary: 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post`
- Full contract: [`api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video-high-quality-play-url`](../api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video-high-quality-play-url)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `aweme_ids`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| aweme_ids | string | No | 作品id列表，用逗号分隔，最多50个/Video id list, separated by commas, up to 50 |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_multi_video_statistics`

- Summary: 根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-multi-video-statistics`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-multi-video-statistics)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_ids | query | string | Yes | 作品id/Video id |

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

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_v2`

- Summary: 批量获取视频信息 V2/Batch Get Video Information V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post`
- Full contract: [`api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video-v2`](../api-contracts/douyin-app-v3-api.md#post-api-u1-v1-douyin-app-v3-fetch-multi-video-v2)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| [] | array<string> | Yes | None |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_music_detail`

- Summary: 获取指定音乐的详情数据/Get details of specified music
- Capabilities: details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_music_hot_search_list`

- Summary: 获取抖音音乐榜数据/Get Douyin music hot search list data
- Capabilities: search / trends / rankings / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-hot-search-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-hot-search-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| chart_type | query | string | No | 榜单类型/Chart type |
| cursor | query | string | No | 游标/Cursor |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_music_search_result`

- Summary: 获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_music_video_list`

- Summary: 获取指定音乐的视频列表数据/Get video list of specified music
- Capabilities: content details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-video-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-music-video-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`

- Summary: 根据分享链接获取单个作品数据/Get single video data by sharing link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-by-share-url`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-by-share-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_url | query | string | Yes | 分享链接/Share link |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-v2`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v3`

- Summary: 获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-v3`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-one-video-v3)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品或文章ID/Video or Article ID |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_series_detail`

- Summary: 获取短剧详情信息/Get series detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-series-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-series-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| series_id | query | string | Yes | 短剧id/Series id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_series_video_list`

- Summary: 获取短剧视频列表/Get series video list
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-series-video-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-series-video-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| series_id | query | string | Yes | 短剧id/Series id |
| cursor | query | integer | No | 游标/Cursor |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_share_info_by_share_code`

- Summary: 根据分享口令获取分享信息/Get share info by share code
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-share-info-by-share-code`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-share-info-by-share-code)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| share_code | query | string | Yes | 分享口令/Share code |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_fans_list`

- Summary: 获取用户粉丝列表/Get user fans list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-fans-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-fans-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| max_time | query | string | No | 最大时间戳/Maximum timestamp |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_following_list`

- Summary: 获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-following-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-following-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id |
| max_time | query | string | No | 最大时间戳/Maximum timestamp |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_like_videos`

- Summary: 获取用户喜欢作品数据/Get user like video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-like-videos`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-like-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 用户sec_user_id/User sec_user_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| counts | query | integer | No | 每页数量/Number per page |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`

- Summary: 获取用户主页作品数据/Get user homepage video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-post-videos`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-post-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 用户sec_user_id/User sec_user_id |
| max_cursor | query | integer | No | 最大游标/Maximum cursor |
| count | query | integer | No | 每页数量/Number per page |
| sort_type | query | integer | No | 排序类型/Sort type |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_search_result`

- Summary: 获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| douyin_user_fans | query | string | No | 粉丝数/Fans |
| douyin_user_type | query | string | No | 用户类型/User type |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_user_series_list`

- Summary: 获取用户短剧合集列表/Get user series list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-series-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-user-series-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户id/User id |
| sec_user_id | query | string | No | 用户加密id/User sec id |
| cursor | query | integer | No | 游标/Cursor |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_comment_replies`

- Summary: 获取指定视频的评论回复数据/Get comment replies data of specified video
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-comment-replies`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-comment-replies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |
| comment_id | query | string | Yes | 评论id/Comment id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_comments`

- Summary: 获取单个视频评论数据/Get single video comments data
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-comments`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url`

- Summary: 获取视频的最高画质播放链接/Get the highest quality play URL of the video
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-high-quality-play-url`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-high-quality-play-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | No | 作品id/Video id |
| share_url | query | string | No | 可选，分享链接/Optional, share link |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_detail`

- Summary: 获取抖音视频合集详情数据/Get Douyin video mix detail data
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-mix-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-mix-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| mix_id | query | string | Yes | 合集id/Mix id |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_post_list`

- Summary: 获取抖音视频合集作品列表数据/Get Douyin video mix post list data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-mix-post-list`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-mix-post-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| mix_id | query | string | Yes | 合集id/Mix id |
| cursor | query | integer | No | 游标/Cursor |
| count | query | integer | No | 数量/Number |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result`

- Summary: 获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-search-result`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-search-result)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| offset | query | integer | No | 偏移量/Offset |
| count | query | integer | No | 数量/Number |
| sort_type | query | string | No | 排序类型/Sort type |
| publish_time | query | string | No | 发布时间/Publish time |
| filter_duration | query | string | No | 时长/Duration |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result_v2`

- Summary: 获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-search-result-v2`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-search-result-v2)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |
| sort_type | query | string | No | 排序类型/Sort type |
| publish_time | query | string | No | 发布时间/Publish time |
| filter_duration | query | string | No | 视频时长/Duration filter |
| page | query | integer | No | 页码/Page |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging |

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

### `GET /api/u1/v1/douyin/app/v3/fetch_video_statistics`

- Summary: 根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-statistics`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-fetch-video-statistics)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_ids | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/douyin/app/v3/generate_douyin_short_url`

- Summary: 生成抖音短链接/Generate Douyin short link
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-generate-douyin-short-url`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-generate-douyin-short-url)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| url | query | string | Yes | 抖音链接/Douyin link |

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

### `GET /api/u1/v1/douyin/app/v3/generate_douyin_video_share_qrcode`

- Summary: 生成抖音视频分享二维码/Generate Douyin video share QR code
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-generate-douyin-video-share-qrcode`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-generate-douyin-video-share-qrcode)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| object_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/douyin/app/v3/handler_user_profile`

- Summary: 获取指定用户的信息/Get information of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-handler-user-profile`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-handler-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 用户sec_user_id/User sec_user_id |

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

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_keyword_search`

- Summary: 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-keyword-search`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-keyword-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword |

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

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_send_private_message`

- Summary: 生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-send-private-message`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-send-private-message)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid |

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

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_user_profile`

- Summary: 生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-user-profile`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid |

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

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_video_detail`

- Summary: 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-video-detail`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-open-douyin-app-to-video-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/douyin/app/v3/register_device`

- Summary: 抖音APP注册设备/Douyin APP register device
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `register_device_api_v1_douyin_app_v3_register_device_get`
- Full contract: [`api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-register-device`](../api-contracts/douyin-app-v3-api.md#get-api-u1-v1-douyin-app-v3-register-device)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| proxy | query | string | No | 代理/Proxy |

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
