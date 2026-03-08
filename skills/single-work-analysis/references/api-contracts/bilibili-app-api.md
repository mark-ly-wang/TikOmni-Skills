# Bilibili-App-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/bilibili-app-api.md`](../api-tags/bilibili-app-api.md)
- Current contract file: `api-contracts/bilibili-app-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `11`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(哔哩哔哩App数据接口/Bilibili-App-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-bilibili-app-fetch-bangumi-tab"></a>
### `GET /api/u1/v1/bilibili/app/fetch_bangumi_tab`

- Summary: 获取番剧推荐/Get bangumi tab
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取主页番剧推荐
> ### 返回:
> - 番剧推荐数据
>
> # [English]
> ### Purpose:
> - Get bangumi tab (anime recommendations)
> ### Return:
> - Bangumi tab data

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-cinema-tab"></a>
### `GET /api/u1/v1/bilibili/app/fetch_cinema_tab`

- Summary: 获取影视推荐/Get cinema tab
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取主页影视推荐
> ### 返回:
> - 影视推荐数据
>
> # [English]
> ### Purpose:
> - Get cinema tab (movies/TV recommendations)
> ### Return:
> - Cinema tab data

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-home-feed"></a>
### `GET /api/u1/v1/bilibili/app/fetch_home_feed`

- Summary: 获取主页推荐视频流/Get home feed
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取主页推荐视频流
> ### 参数:
> - idx: 页面索引，默认使用当前时间戳
> - flush: 刷新标记（0=普通加载, 1=刷新）
> - pull: 是否下拉刷新
> ### 返回:
> - 推荐视频流数据
>
> # [English]
> ### Purpose:
> - Get home feed (recommended videos)
> ### Parameters:
> - idx: Page index, defaults to current timestamp
> - flush: Flush flag (0=normal load, 1=refresh)
> - pull: Pull to refresh
> ### Return:
> - Home feed data

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| idx | query | integer | No | 页面索引/Page index | None | None | None |
| flush | query | integer | No | 刷新标记/Flush flag (0=普通加载, 1=刷新) | 0 | None | None |
| pull | query | boolean | No | 是否下拉刷新/Pull to refresh | true | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-one-video"></a>
### `GET /api/u1/v1/bilibili/app/fetch_one_video`

- Summary: 获取单个视频详情信息/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_bilibili_app_fetch_one_video_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个视频详情信息（APP接口）
> ### 参数:
> - av_id: AV号（与bv_id二选一）
> - bv_id: BV号（与av_id二选一）
> ### 返回:
> - 视频详情信息
>
> # [English]
> ### Purpose:
> - Get single video data (APP API)
> ### Parameters:
> - av_id: AV ID (choose one of av_id or bv_id)
> - bv_id: BV ID (choose one of av_id or bv_id)
> ### Return:
> - Video data
>
> # [示例/Example]
> av_id = "115568241811221"
> bv_id = "BV18SCrBGE9E"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| av_id | query | string | No | AV号/AV ID | None | 115568241811221 | None |
| bv_id | query | string | No | BV号/BV ID | None | BV18SCrBGE9E | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-popular-feed"></a>
### `GET /api/u1/v1/bilibili/app/fetch_popular_feed`

- Summary: 获取热门推荐/Get popular feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取热门推荐视频
> ### 参数:
> - idx: 页面索引（从1开始）
> - last_param: 上一页最后一个视频的ID（用于分页）
> ### 返回:
> - 热门推荐视频数据
>
> # [English]
> ### Purpose:
> - Get popular feed
> ### Parameters:
> - idx: Page index (starting from 1)
> - last_param: Last video ID from previous page (for pagination)
> ### Return:
> - Popular feed data
>
> # [示例/Example]
> idx = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| idx | query | integer | No | 页面索引/Page index | 1 | None | None |
| last_param | query | string | No | 上一页最后一个视频ID/Last video ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-reply-detail"></a>
### `GET /api/u1/v1/bilibili/app/fetch_reply_detail`

- Summary: 获取二级评论回复/Get reply detail
- Capabilities: comment replies / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取二级评论回复
> ### 参数:
> - root: 一级评论ID（必填）
> - av_id: AV号（与bv_id二选一）
> - bv_id: BV号（与av_id二选一）
> - next_offset: 下一页游标
> - ps: 每页数量
> ### 返回:
> - 二级评论列表数据
>
> # [English]
> ### Purpose:
> - Get reply detail (second level comments)
> ### Parameters:
> - root: Root comment ID (required)
> - av_id: AV ID (choose one of av_id or bv_id)
> - bv_id: BV ID (choose one of av_id or bv_id)
> - next_offset: Next page cursor
> - ps: Page size
> ### Return:
> - Reply data
>
> # [示例/Example]
> root = "241743663521"
> av_id = "113100682434775"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| root | query | string | Yes | 一级评论ID/Root comment ID | None | 241743663521 | None |
| av_id | query | string | No | AV号/AV ID | None | 113100682434775 | None |
| bv_id | query | string | No | BV号/BV ID | None | BV18SCrBGE9E | None |
| next_offset | query | integer | No | 下一页游标/Next page cursor | 0 | None | None |
| ps | query | integer | No | 每页数量/Page size | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-search-all"></a>
### `GET /api/u1/v1/bilibili/app/fetch_search_all`

- Summary: 综合搜索/search all
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_all_api_v1_bilibili_app_fetch_search_all_get`

#### Notes

> # [中文]
> ### 用途:
> - 综合搜索（返回所有类型的搜索结果）
> ### 参数:
> - keyword: 搜索关键词（必填）
> - page: 页码，从1开始
> - page_size: 每页结果数量
> - order: 排序方式（0=综合排序）
> ### 返回:
> - 搜索结果，包含nav（分类导航）、item（搜索结果）、pagination（分页信息）等
>
> # [English]
> ### Purpose:
> -  search all (returns all types of search results)
> ### Parameters:
> - keyword: Search keyword (required)
> - page: Page number, starting from 1
> - page_size: Results per page
> - order: Sort order (0=comprehensive)
> ### Return:
> - Search results including nav (category navigation), item (results), pagination, etc.
>
> # [示例/Example]
> keyword = "原神"
> page = 1
> page_size = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 原神 | None |
| page | query | integer | No | 页码/Page number | 1 | None | None |
| page_size | query | integer | No | 每页数量/Page size | 20 | None | None |
| order | query | integer | No | 排序方式/Sort order (0=综合排序) | 0 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-search-by-type"></a>
### `GET /api/u1/v1/bilibili/app/fetch_search_by_type`

- Summary: 分类搜索/ search by type
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get`

#### Notes

> # [中文]
> ### 用途:
> - 分类搜索（按类型搜索）
> ### 参数:
> - keyword: 搜索关键词（必填）
> - search_type: 搜索类型
>     - video: 视频
>     - bangumi: 番剧
>     - pgc: 影视
>     - live: 直播
>     - article: 专栏
>     - user: 用户
> - page: 页码，从1开始
> - page_size: 每页结果数量
> - order: 排序方式
>     - 0: 综合排序
>     - 1: 最新发布
>     - 2: 播放量
>     - 3: 弹幕数
> ### 返回:
> - 搜索结果
>
> # [English]
> ### Purpose:
> -  search by type
> ### Parameters:
> - keyword: Search keyword (required)
> - search_type: Search type
>     - video: Videos
>     - bangumi: Anime
>     - pgc: Movies/TV
>     - live: Live streams
>     - article: Articles
>     - user: Users
> - page: Page number, starting from 1
> - page_size: Results per page
> - order: Sort order
>     - 0: Comprehensive
>     - 1: Latest
>     - 2: Play count
>     - 3: Danmaku count
> ### Return:
> - Search results
>
> # [示例/Example]
> keyword = "原神"
> search_type = "video"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 原神 | None |
| search_type | query | string | No | 搜索类型/Search type (video/bangumi/pgc/live/article/user) | video | None | None |
| page | query | integer | No | 页码/Page number | 1 | None | None |
| page_size | query | integer | No | 每页数量/Page size | 20 | None | None |
| order | query | integer | No | 排序方式/Sort order (0=综合, 1=最新, 2=播放量, 3=弹幕数) | 0 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-user-info"></a>
### `GET /api/u1/v1/bilibili/app/fetch_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_bilibili_app_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户信息
> ### 参数:
> - user_id: 用户ID（必填）
> ### 返回:
> - 用户信息（包含粉丝数、关注数、投稿数等）
>
> # [English]
> ### Purpose:
> - Get user info
> ### Parameters:
> - user_id: User ID (required)
> ### Return:
> - User info (including followers, following, videos count, etc.)
>
> # [示例/Example]
> user_id = "203680252"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 203680252 | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-user-videos"></a>
### `GET /api/u1/v1/bilibili/app/fetch_user_videos`

- Summary: 获取用户投稿视频/Get user videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户投稿视频列表
> ### 参数:
> - user_id: 用户ID（必填）
> - post_filter: 过滤类型（archive=投稿, season=合集, contribute=贡献）
> - page: 页码
> - ps: 每页数量
> ### 返回:
> - 用户投稿视频列表
>
> # [English]
> ### Purpose:
> - Get user uploaded videos
> ### Parameters:
> - user_id: User ID (required)
> - post_filter: Filter type (archive/season/contribute)
> - page: Page number
> - ps: Page size
> ### Return:
> - User videos data
>
> # [示例/Example]
> user_id = "203680252"
> post_filter = "archive"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 203680252 | None |
| post_filter | query | string | No | 过滤类型/Filter type (archive/season/contribute) | archive | None | None |
| page | query | integer | No | 页码/Page number | 1 | None | None |
| ps | query | integer | No | 每页数量/Page size | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-bilibili-app-fetch-video-comments"></a>
### `GET /api/u1/v1/bilibili/app/fetch_video_comments`

- Summary: 获取视频评论列表/Get video comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取视频评论列表
> ### 参数:
> - av_id: AV号（与bv_id二选一）
> - bv_id: BV号（与av_id二选一）
> - mode: 排序模式（3=热门, 2=时间）
> - next_offset: 分页游标
> ### 返回:
> - 评论列表数据
>
> # [English]
> ### Purpose:
> - Get video comments
> ### Parameters:
> - av_id: AV ID (choose one of av_id or bv_id)
> - bv_id: BV ID (choose one of av_id or bv_id)
> - mode: Sort mode (3=hot, 2=time)
> - next_offset: Pagination cursor
> ### Return:
> - Comments data
>
> # [示例/Example]
> bv_id = "BV18SCrBGE9E"
> mode = 3
> next_offset = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| av_id | query | string | No | AV号/AV ID | None | 115568241811221 | None |
| bv_id | query | string | No | BV号/BV ID | None | BV18SCrBGE9E | None |
| mode | query | integer | No | 排序模式/Sort mode (3=热门/hot, 2=时间/time) | 3 | None | None |
| next_offset | query | integer | No | 分页游标/Pagination cursor | 1 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |
