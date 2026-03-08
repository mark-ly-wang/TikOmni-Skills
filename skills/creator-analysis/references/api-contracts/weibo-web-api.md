# Weibo-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/weibo-web-api.md`](../api-tags/weibo-web-api.md)
- Current contract file: `api-contracts/weibo-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `11`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(新浪微博Web数据接口/Weibo-Web-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-weibo-web-fetch-channel-feed"></a>
### `GET /api/u1/v1/weibo/web/fetch_channel_feed`

- Summary: 根据频道名称获取热门内容/Get channel feed by name
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据频道名称获取热门内容（便捷接口）
> ### 参数:
> - channel_name: 频道名称，如 "热门"、"榜单"、"社会" 等，不传则使用默认频道
> - page: 页码，默认1
> ### 返回:
> - 热门微博列表
> ### 说明:
> - 此接口会自动调用 fetch_config_list 获取频道配置，然后获取对应频道的热门内容
> - 如果指定的频道名称不存在，会返回错误信息
> - 可用频道：热门、榜单、同城、社会、科技、明星、电影、音乐、数码、汽车、游戏
>
> # [English]
> ### Purpose:
> - Get trending content by channel name (convenience endpoint)
> ### Parameters:
> - channel_name: Channel name, such as "热门", "榜单", "社会", etc. Use default if not provided
> - page: Page number, default 1
> ### Return:
> - Trending Weibo list
> ### Note:
> - This endpoint will automatically call fetch_config_list to get channel config, then fetch trending content
> - Returns error if the specified channel name does not exist
> - Available channels: 热门, 榜单, 同城, 社会, 科技, 明星, 电影, 音乐, 数码, 汽车, 游戏
>
> # [示例/Example]
> channel_name = "热门"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| channel_name | query | string | No | 频道名称，不传则使用默认频道/Channel name, use default if not provided | None | 热门 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-comment-replies"></a>
### `GET /api/u1/v1/weibo/web/fetch_comment_replies`

- Summary: 获取评论子评论/Get comment replies
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取评论的子评论（回复）
> ### 参数:
> - cid: 根评论ID（从 fetch_post_comments 返回的评论中获取）
> - max_id: 翻页用的ID，默认0为第一页，从上一页返回结果中获取下一页的max_id
> ### 返回:
> - 子评论列表
>
> # [English]
> ### Purpose:
> - Get comment replies (sub-comments)
> ### Parameters:
> - cid: Root comment ID (from fetch_post_comments response)
> - max_id: Pagination ID, default 0 for first page, get next page max_id from previous response
> ### Return:
> - Sub-comments list
>
> # [示例/Example]
> cid = "5100663573318494"
> max_id = "0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cid | query | string | Yes | 根评论ID/Root comment ID | None | 5100663573318494 | None |
| max_id | query | string | No | 翻页ID，默认0为第一页/Pagination ID, default 0 for first page | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-config-list"></a>
### `GET /api/u1/v1/weibo/web/fetch_config_list`

- Summary: 获取频道配置列表/Get channel config list
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_config_list_api_v1_weibo_web_fetch_config_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博移动端所有频道的配置信息
> ### 返回:
> - 频道列表，包含频道名称和 containerid
> ### 说明:
> - 返回的 containerid 可用于 fetch_trend_top 接口获取对应频道的热门内容
>
> # [English]
> ### Purpose:
> - Get all channel configuration information from Weibo mobile
> ### Return:
> - Channel list, including channel name and containerid
> ### Note:
> - The returned containerid can be used in fetch_trend_top endpoint to get trending content of the corresponding channel

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

<a id="get-api-u1-v1-weibo-web-fetch-hot-search"></a>
### `GET /api/u1/v1/weibo/web/fetch_hot_search`

- Summary: 获取热搜榜/Get hot search ranking
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博实时热搜榜（Top 50）和实时上升热点
> ### 返回:
> - 热搜榜列表，包含：
>     - **实时热搜榜**: 当前最热门的50个话题，按热度排序
>     - **实时上升热点**: 正在快速上升的热门话题
> ### 说明:
> - 这是微博官方热搜榜数据
> - 每个热搜包含：排名、话题名、热度值、标签（如：新、热、沸）等
> - 与 `fetch_search_topics` 不同，此接口返回的是完整的热搜排行榜
>
> # [English]
> ### Purpose:
> - Get Weibo real-time hot search ranking (Top 50) and rising trends
> ### Return:
> - Hot search list, including:
>     - **Real-time Hot Search**: Top 50 hottest topics, sorted by popularity
>     - **Rising Trends**: Topics that are rapidly gaining attention
> ### Note:
> - This is official Weibo hot search data
> - Each entry includes: rank, topic name, heat value, tags (new, hot, trending), etc.
> - Different from `fetch_search_topics`, this returns the complete hot search ranking

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

<a id="get-api-u1-v1-weibo-web-fetch-post-comments"></a>
### `GET /api/u1/v1/weibo/web/fetch_post_comments`

- Summary: 获取微博评论/Get post comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博的评论列表（热门评论流）
> ### 参数:
> - post_id: 微博ID
> - mid: 微博MID
> - max_id: 翻页用的ID，从上一页返回结果中获取
> - max_id_type: max_id类型，默认0
> ### 返回:
> - 评论列表
>
> # [English]
> ### Purpose:
> - Get Weibo post comments (hot comments flow)
> ### Parameters:
> - post_id: Post ID
> - mid: Post MID
> - max_id: Pagination ID from previous page result
> - max_id_type: max_id type, default 0
> ### Return:
> - Comments list
>
> # [示例/Example]
> post_id = "5100663548412324"
> mid = "5100663548412324"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 微博ID/Post ID | None | 5100663548412324 | None |
| mid | query | string | Yes | 微博MID/Post MID | None | 5100663548412324 | None |
| max_id | query | string | No | 翻页ID/Pagination ID | None | None | None |
| max_id_type | query | integer | No | 翻页ID类型/Pagination ID type | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-post-detail"></a>
### `GET /api/u1/v1/weibo/web/fetch_post_detail`

- Summary: 获取微博详情/Get post detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单条微博的详情
> ### 参数:
> - post_id: 微博ID
> ### 返回:
> - 微博详情
>
> # [English]
> ### Purpose:
> - Get single Weibo post detail
> ### Parameters:
> - post_id: Post ID
> ### Return:
> - Post detail
>
> # [示例/Example]
> post_id = "5092682368025584"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 微博ID/Post ID | None | 5092682368025584 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-search"></a>
### `GET /api/u1/v1/weibo/web/fetch_search`

- Summary: 搜索微博/Search Weibo
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_api_v1_weibo_web_fetch_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索微博内容
> ### 参数:
> - **keyword**: 搜索关键词
>     - 普通搜索: `游戏`、`新闻`
>     - 话题搜索: `#话题名#`（如 `#大冰建议女生不要找老登#`）
> - **page**: 页码
>     - 从 **1** 开始递增: 1, 2, 3, 4...
>     - 每页约返回 10-20 条结果
>     - **不是** 1, 10, 20 这种偏移量模式
> - **search_type**: 搜索类型
>     - **1**: 综合（默认，按相关性排序）
>     - **61**: 实时（按时间排序，最新优先）
>     - **3**: 用户（搜索用户账号）
>     - **60**: 热门（按热度排序）
>     - **64**: 视频（仅视频内容）
>     - **63**: 图片（仅图片内容）
>     - **21**: 文章（仅长文章）
> - **time_scope**: 时间范围筛选
>     - **null/不传**: 不限时间（默认）
>     - **hour**: 一小时内
>     - **day**: 一天内（24小时）
>     - **week**: 一周内
>     - **month**: 一个月内
> ### 返回:
> - 搜索结果列表
> ### 注意:
> - 此接口会自动生成游客Cookie，无需登录即可使用
> - 如遇到 432 错误，系统会自动重试
>
> # [English]
> ### Purpose:
> - Search Weibo content
> ### Parameters:
> - **keyword**: Search keyword
>     - Normal search: `game`, `news`
>     - Hashtag search: `#topic#` (e.g., `#TopicName#`)
> - **page**: Page number
>     - Starts from **1** and increments: 1, 2, 3, 4...
>     - Returns ~10-20 results per page
>     - **NOT** offset mode like 1, 10, 20
> - **search_type**: Search type
>     - **1**: Comprehensive (default, sorted by relevance)
>     - **61**: Real-time (sorted by time, newest first)
>     - **3**: Users (search user accounts)
>     - **60**: Hot (sorted by popularity)
>     - **64**: Video (video content only)
>     - **63**: Pictures (image content only)
>     - **21**: Articles (long articles only)
> - **time_scope**: Time range filter
>     - **null/empty**: No time limit (default)
>     - **hour**: Within one hour
>     - **day**: Within one day (24 hours)
>     - **week**: Within one week
>     - **month**: Within one month
> ### Return:
> - Search results list
> ### Note:
> - This endpoint auto-generates visitor cookies, no login required
> - Auto-retry on 432 error
>
> # [示例/Example]
> keyword = "游戏"
> page = 1
> search_type = "1"
> time_scope = null

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词，支持话题搜索如 #话题名#/Search keyword, supports hashtag like #topic# | None | 游戏 | None |
| page | query | integer | No | 页码，从1开始递增(1,2,3...)，每页约10-20条/Page number, starts from 1 (1,2,3...), ~10-20 results per page | 1 | 1 | None |
| search_type | query | string | No | 搜索类型/Search type: 1=综合, 61=实时, 3=用户, 60=热门, 64=视频, 63=图片, 21=文章 | 1 | 1 | None |
| time_scope | query | string | No | 时间范围/Time scope: hour=一小时内, day=一天内, week=一周内, month=一个月内, null=不限 | None | None | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-search-topics"></a>
### `GET /api/u1/v1/weibo/web/fetch_search_topics`

- Summary: 获取搜索页热搜词/Get search page hot topics
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取搜索页的热搜词列表（搜索建议/热门话题）
> ### 返回:
> - 搜索热词列表
> ### 说明:
> - 这是搜索页面展示的热门搜索词
> - 通常用于搜索框下方的热门推荐
> - 与 `fetch_hot_search` 不同，此接口返回的是搜索建议词
>
> # [English]
> ### Purpose:
> - Get search page hot topics list (search suggestions/trending topics)
> ### Return:
> - Search hot topics list
> ### Note:
> - These are hot search terms displayed on the search page
> - Usually used for trending recommendations below the search box
> - Different from `fetch_hot_search`, this returns search suggestion terms

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

<a id="get-api-u1-v1-weibo-web-fetch-trend-top"></a>
### `GET /api/u1/v1/weibo/web/fetch_trend_top`

- Summary: 获取频道热门趋势/Get channel trend top
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定频道的热门趋势内容
> ### 参数:
> - containerid: 频道容器ID，可从 fetch_config_list 接口获取
> - page: 页码，默认1
> ### 返回:
> - 热门微博列表
> ### 说明:
> - containerid 示例: 102803_ctg1_8999_-_ctg1_8999_home
> - 可通过 fetch_config_list 获取所有可用的 containerid
>
> # [English]
> ### Purpose:
> - Get trending content of the specified channel
> ### Parameters:
> - containerid: Channel container ID, can be obtained from fetch_config_list endpoint
> - page: Page number, default 1
> ### Return:
> - Trending Weibo list
> ### Note:
> - containerid example: 102803_ctg1_8999_-_ctg1_8999_home
> - You can get all available containerids from fetch_config_list
>
> # [示例/Example]
> containerid = "102803_ctg1_8999_-_ctg1_8999_home"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| containerid | query | string | Yes | 频道容器ID/Channel container ID | None | 102803_ctg1_8999_-_ctg1_8999_home | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-user-info"></a>
### `GET /api/u1/v1/weibo/web/fetch_user_info`

- Summary: 获取用户信息/Get user information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_weibo_web_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博用户信息
> ### 参数:
> - uid: 用户ID
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get Weibo user information
> ### Parameters:
> - uid: User ID
> ### Return:
> - User information
>
> # [示例/Example]
> uid = "2992978081"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 2992978081 | None |

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

<a id="get-api-u1-v1-weibo-web-fetch-user-posts"></a>
### `GET /api/u1/v1/weibo/web/fetch_user_posts`

- Summary: 获取用户微博列表/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博用户的微博列表
> ### 参数:
> - uid: 用户ID
> - page: 页码，默认1
> - since_id: 翻页用的ID，从上一页返回结果中获取
> ### 返回:
> - 用户微博列表
>
> # [English]
> ### Purpose:
> - Get Weibo user's posts list
> ### Parameters:
> - uid: User ID
> - page: Page number, default 1
> - since_id: Pagination ID from previous page result
> ### Return:
> - User posts list
>
> # [示例/Example]
> uid = "7277477906"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 7277477906 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| since_id | query | string | No | 翻页ID，从上一页结果获取/Pagination ID from previous page | None | None | None |

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
