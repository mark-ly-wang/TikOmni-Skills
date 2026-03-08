# Douyin-Creator-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-creator-api.md`
- Full contract: [`api-contracts/douyin-creator-api.md`](../api-contracts/douyin-creator-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `16`
- Common capabilities: creators / trends / rankings / topics / details / music / audio / search
- Default auth: Header `Authorization` Bearer
- Common inputs: `billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time`
- Tag description: **(抖音创作者数据接口/Douyin-Creator-API data endpoints)**

## Routes

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_detail`

- Summary: 获取创作者活动详情/Get creator activity detail
- Capabilities: creators / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-detail`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| activity_id | query | string | Yes | 活动ID/Activity ID |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_list`

- Summary: 获取创作者活动列表/Get creator activity list
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| start_time | query | integer | Yes | 开始时间戳/Start timestamp |
| end_time | query | integer | Yes | 结束时间戳/End timestamp |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_category`

- Summary: 获取创作者内容创作合集分类/Get creator content creation category
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-category`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-category)

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_course`

- Summary: 获取创作者内容创作课程/Get creator content creation course
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-course`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-course)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| category_id | query | integer | Yes | 分类ID/Category ID |
| order | query | integer | No | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) |
| limit | query | integer | No | 每页数量/Items per page |
| offset | query | integer | No | 偏移量/Offset (starting position) |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard`

- Summary: 获取创作者热门挑战榜单/Get creator hot challenge billboard
- Capabilities: trends / rankings / creators / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-challenge-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-challenge-billboard)

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_course`

- Summary: 获取创作者热门课程/Get creator hot course
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-course`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-course)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| order | query | integer | No | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) |
| limit | query | integer | No | 每页数量/Items per page (建议24) |
| offset | query | integer | No | 偏移量/Offset |
| category_id | query | string | No | 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题 可选值/Available values: 6976547830546582816=知识品类, 697654792384900… |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard`

- Summary: 获取创作者热门音乐榜单/Get creator hot music billboard
- Capabilities: trends / rankings / creators / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-music-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-music-billboard)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | No | 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取) |
| order_key | query | integer | No | 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) |
| time_filter | query | integer | No | 时间筛选/Time filter (1=24小时, 2=7天, 3=30天) |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard`

- Summary: 获取创作者热门道具榜单/Get creator hot props billboard
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-props-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-props-billboard)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | No | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | No | 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites |
| time_filter | query | integer | No | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard`

- Summary: 获取创作者中心创作热点/Get creator hot spot billboard
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-spot-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-spot-billboard)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_tag | query | string | No | 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002' |
| hot_search_type | query | integer | No | 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking |
| city_code | query | string | No | 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2 |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard`

- Summary: 获取创作者热门话题榜单/Get creator hot topic billboard
- Capabilities: trends / rankings / creators / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-topic-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-topic-billboard)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | No | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | No | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions |
| time_filter | query | integer | No | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard`

- Summary: 获取创作者中心热门视频榜单/Get creator material center billboard
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-billboard)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | No | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | No | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity |
| time_filter | query | integer | No | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_config`

- Summary: 获取创作者中心配置/Get creator material center config
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-config`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-config)

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

### `GET /api/u1/v1/douyin/creator/fetch_industry_category_config`

- Summary: 获取行业分类配置/Get industry category config
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-industry-category-config`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-industry-category-config)

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

### `GET /api/u1/v1/douyin/creator/fetch_mission_task_list`

- Summary: 获取商单任务列表/Get mission task list
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-mission-task-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-mission-task-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| cursor | query | integer | No | 游标/Cursor (分页) |
| limit | query | integer | No | 每页数量/Items per page |
| mission_type | query | integer | No | 任务类型/Mission type |
| tab_scene | query | integer | No | 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评) |
| industry_lv1 | query | integer | No | 一级行业/Primary industry (-1=全部) |
| industry_lv2 | query | integer | No | 二级行业/Secondary industry (-1=全部) |
| platform_channel | query | integer | No | 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文) |
| pay_type | query | integer | No | 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣) |
| greater_than_cost_progress | query | integer | No | 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%) |
| publish_time_start | query | integer | No | 发布开始时间/Publish start time (时间戳) |
| quick_selector_scene | query | integer | No | 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过) |
| keyword | query | string | No | 关键词/Keyword (任务名称或ID) |

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

### `GET /api/u1/v1/douyin/creator/fetch_user_search`

- Summary: 搜索用户/Search users
- Capabilities: search / creators / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_api_v1_douyin_creator_fetch_user_search_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-user-search`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-user-search)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_name | query | string | Yes | 用户名/Username (支持抖音号和抖音昵称) |

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

### `GET /api/u1/v1/douyin/creator/fetch_video_danmaku_list`

- Summary: 获取作品弹幕列表/Get video danmaku list
- Capabilities: creators / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get`
- Full contract: [`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-video-danmaku-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-video-danmaku-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品ID/Video item ID |
| count | query | integer | No | 每页数量/Items per page |
| offset | query | integer | No | 偏移量/Offset (starting position) |
| order_type | query | integer | No | 排序类型/Order type (1=时间排序, 2=其他排序) |
| is_blocked | query | boolean | No | 是否被屏蔽/Is blocked |

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
