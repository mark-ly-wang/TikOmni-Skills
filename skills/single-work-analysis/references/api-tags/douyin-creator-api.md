# Douyin-Creator-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-creator-api.md`
- 完整契约：[`api-contracts/douyin-creator-api.md`](../api-contracts/douyin-creator-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`16`
- 常见能力：创作者 / 热点/榜单 / 话题 / 详情 / 音乐/音频 / 搜索
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time`
- 标签说明：**(抖音创作者数据接口/Douyin-Creator-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_detail`

- 摘要：获取创作者活动详情/Get creator activity detail
- 能力：创作者 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-detail`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| activity_id | query | string | 是 | 活动ID/Activity ID |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_list`

- 摘要：获取创作者活动列表/Get creator activity list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-activity-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| start_time | query | integer | 是 | 开始时间戳/Start timestamp |
| end_time | query | integer | 是 | 结束时间戳/End timestamp |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_category`

- 摘要：获取创作者内容创作合集分类/Get creator content creation category
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-category`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-category)

#### 参数

无

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_course`

- 摘要：获取创作者内容创作课程/Get creator content creation course
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-course`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-content-course)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| category_id | query | integer | 是 | 分类ID/Category ID |
| order | query | integer | 否 | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) |
| limit | query | integer | 否 | 每页数量/Items per page |
| offset | query | integer | 否 | 偏移量/Offset (starting position) |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard`

- 摘要：获取创作者热门挑战榜单/Get creator hot challenge billboard
- 能力：热点/榜单 / 创作者 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-challenge-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-challenge-billboard)

#### 参数

无

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_course`

- 摘要：获取创作者热门课程/Get creator hot course
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-course`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-course)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| order | query | integer | 否 | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) |
| limit | query | integer | 否 | 每页数量/Items per page (建议24) |
| offset | query | integer | 否 | 偏移量/Offset |
| category_id | query | string | 否 | 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题 可选值/Available values: 6976547830546582816=知识品类, 697654792384900… |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard`

- 摘要：获取创作者热门音乐榜单/Get creator hot music billboard
- 能力：热点/榜单 / 创作者 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-music-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-music-billboard)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取) |
| order_key | query | integer | 否 | 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) |
| time_filter | query | integer | 否 | 时间筛选/Time filter (1=24小时, 2=7天, 3=30天) |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard`

- 摘要：获取创作者热门道具榜单/Get creator hot props billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-props-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-props-billboard)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard`

- 摘要：获取创作者中心创作热点/Get creator hot spot billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-spot-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-spot-billboard)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_tag | query | string | 否 | 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002' |
| hot_search_type | query | integer | 否 | 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking |
| city_code | query | string | 否 | 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2 |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard`

- 摘要：获取创作者热门话题榜单/Get creator hot topic billboard
- 能力：热点/榜单 / 创作者 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-topic-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-hot-topic-billboard)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard`

- 摘要：获取创作者中心热门视频榜单/Get creator material center billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-billboard`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-billboard)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days |

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

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_config`

- 摘要：获取创作者中心配置/Get creator material center config
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-config`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-creator-material-center-config)

#### 参数

无

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

### `GET /api/u1/v1/douyin/creator/fetch_industry_category_config`

- 摘要：获取行业分类配置/Get industry category config
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-industry-category-config`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-industry-category-config)

#### 参数

无

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

### `GET /api/u1/v1/douyin/creator/fetch_mission_task_list`

- 摘要：获取商单任务列表/Get mission task list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-mission-task-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-mission-task-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cursor | query | integer | 否 | 游标/Cursor (分页) |
| limit | query | integer | 否 | 每页数量/Items per page |
| mission_type | query | integer | 否 | 任务类型/Mission type |
| tab_scene | query | integer | 否 | 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评) |
| industry_lv1 | query | integer | 否 | 一级行业/Primary industry (-1=全部) |
| industry_lv2 | query | integer | 否 | 二级行业/Secondary industry (-1=全部) |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文) |
| pay_type | query | integer | 否 | 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣) |
| greater_than_cost_progress | query | integer | 否 | 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%) |
| publish_time_start | query | integer | 否 | 发布开始时间/Publish start time (时间戳) |
| quick_selector_scene | query | integer | 否 | 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过) |
| keyword | query | string | 否 | 关键词/Keyword (任务名称或ID) |

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

### `GET /api/u1/v1/douyin/creator/fetch_user_search`

- 摘要：搜索用户/Search users
- 能力：搜索 / 创作者 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_douyin_creator_fetch_user_search_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-user-search`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-user-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_name | query | string | 是 | 用户名/Username (支持抖音号和抖音昵称) |

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

### `GET /api/u1/v1/douyin/creator/fetch_video_danmaku_list`

- 摘要：获取作品弹幕列表/Get video danmaku list
- 能力：创作者 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get`
- 完整契约：[`api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-video-danmaku-list`](../api-contracts/douyin-creator-api.md#get-api-u1-v1-douyin-creator-fetch-video-danmaku-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品ID/Video item ID |
| count | query | integer | 否 | 每页数量/Items per page |
| offset | query | integer | 否 | 偏移量/Offset (starting position) |
| order_type | query | integer | 否 | 排序类型/Order type (1=时间排序, 2=其他排序) |
| is_blocked | query | boolean | 否 | 是否被屏蔽/Is blocked |

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
