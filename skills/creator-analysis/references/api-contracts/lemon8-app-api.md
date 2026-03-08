# Lemon8-App-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/lemon8-app-api.md`](../api-tags/lemon8-app-api.md)
- Current contract file: `api-contracts/lemon8-app-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `16`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Lemon8 APP数据接口/Lemon8-APP-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-lemon8-app-fetch-discover-banners"></a>
### `GET /api/u1/v1/lemon8/app/fetch_discover_banners`

- Summary: 获取发现页Banner/Get banners of discover page
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取发现页Banner（搜索页上方的滚动内容）
> ### 返回:
> - Banner列表
>
> # [English]
> ### Purpose:
> - Get banners of discover page
> ### Return:
> - Banners list
>
> # [示例/Example]

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

<a id="get-api-u1-v1-lemon8-app-fetch-discover-tab"></a>
### `GET /api/u1/v1/lemon8/app/fetch_discover_tab`

- Summary: 获取发现页主体内容/Get main content of discover page
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取发现页（搜索页主体内容）
> ### 返回:
> - 主体内容
>
> # [English]
> ### Purpose:
> - Get main content of discover page
> ### Return:
> - Main content
>
> # [示例/Example]

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

<a id="get-api-u1-v1-lemon8-app-fetch-discover-tab-information-tabs"></a>
### `GET /api/u1/v1/lemon8/app/fetch_discover_tab_information_tabs`

- Summary: 获取发现页的 Editor's Picks/Get Editor's Picks of discover page
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取发现页（搜索页下方的推荐内容 - Editor's Picks）
> ### 返回:
> - 推荐内容
>
> # [English]
> ### Purpose:
> - Get Editor's Picks of discover page
> ### Return:
> - Editor's Picks
>
> # [示例/Example]

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

<a id="get-api-u1-v1-lemon8-app-fetch-hot-search-keywords"></a>
### `GET /api/u1/v1/lemon8/app/fetch_hot_search_keywords`

- Summary: 获取热搜关键词/Get hot search keywords
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取热搜关键词
> ### 返回:
> - 热搜关键词列表
>
> # [English]
> ### Purpose:
> - Get hot search keywords
> ### Return:
> - Hot search keywords list
>
> # [示例/Example]

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

<a id="get-api-u1-v1-lemon8-app-fetch-post-comment-list"></a>
### `GET /api/u1/v1/lemon8/app/fetch_post_comment_list`

- Summary: 获取指定作品的评论列表/Get comments list of specified post
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定作品的评论列表
> ### 参数:
> - group_id: 作品的group_id，可以从接口`/lemon8/app/fetch_post_detail`获取
> - item_id: 作品的item_id，可以从接口`/lemon8/app/fetch_post_detail` 或 `/lemon8/app/get_item_id`获取
> - media_id: 作品的media_id，可以从接口`/lemon8/app/fetch_post_detail`获取
> - offset: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的offset进行翻页。
> ### 返回:
> - 评论列表
>
> # [English]
> ### Purpose:
> - Get comments list of specified post
> ### Parameters:
> - group_id: Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail`
> - item_id: Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id`
> - media_id: Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail`
> - offset: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the offset returned by the last request is used for subsequent requests.
> ### Return:
> - Comments list
>
> # [示例/Example]
> group_id = "7361926875709129222"
> item_id = "7361926875709129222"
> media_id = "7428056850216862763"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| group_id | query | string | Yes | 作品的group_id/Post's group_id | None | 7361926875709129222 | None |
| item_id | query | string | Yes | 作品的item_id/Post's item_id | None | 7361926875709129222 | None |
| media_id | query | string | Yes | 作品的media_id/Post's media_id | None | 7428056850216862763 | None |
| offset | query | string | No | 翻页参数/Pagination parameter | 0 | 0 | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-post-detail"></a>
### `GET /api/u1/v1/lemon8/app/fetch_post_detail`

- Summary: 获取指定作品的信息/Get information of specified post
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定作品的信息
> ### 参数:
> - item_id: 作品ID，可以从接口`/lemon8/app/get_item_id`获取
> ### 返回:
> - 作品信息
>
> # [English]
> ### Purpose:
> - Get information of specified post
> ### Parameters:
> - item_id: Post ID, can be obtained from the interface `/lemon8/app/get_item_id`
> ### Return:
> - Post information
>
> # [示例/Example]
> item_id = "7361926875709129222"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品ID/Post ID | None | 7361926875709129222 | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-search"></a>
### `GET /api/u1/v1/lemon8/app/fetch_search`

- Summary: 搜索接口/Search API
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_api_v1_lemon8_app_fetch_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索接口
> ### 参数:
> - query: 搜索关键词
> - max_cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。
> - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：
>     - 空字符串：All（全部，默认使用此参数搜索）
>     - video：只搜索视频作品
>     - posts：只搜索文章作品
> - order_by: 搜索排序方式，默认为空字符串，可选值如下：
>     - 空字符串：Relevance（相关度，默认使用此参数排序）
>     - popular：流行度排序
>     - recent：从新到旧排序
> - search_tab: 搜索类型，默认为`main`，可选值如下：
>     - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）
>     - user：APP中显示为 `Accounts` （搜索用户账号）
>     - hashtag：APP中显示为 `Hashtags`（搜索话题）
>     - article：APP中显示为 `Posts`（搜索文章）
> ### 返回:
> - 搜索结果
>
> # [English]
> ### Purpose:
> - Search API
> ### Parameters:
> - query: Search keyword
> - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the `max_cursor` returned by the last request is used for subsequent requests. You can judge whether there is more data by the `has_more` field in the return result.
> - filter_type: Search filter type, default is an empty string, optional values are as follows:
>     - Empty string: All (default using this parameter to search)
>     - video: Search only video
>     - posts: Search only posts
> - order_by: Search sort type, default is an empty string, optional values are as follows:
>     - Empty string: Relevance (default using this parameter to sort)
>     - popular: Sort by popularity
>     - recent: Sort from new to old
> - search_tab: Search type, default is `main`, optional values are as follows:
>     - main: Display as `Top` in the APP (comprehensive search, default using this parameter to search)
>     - user: Display as `Accounts` in the APP (search user accounts)
>     - hashtag: Display as `Hashtags` in the APP (search hashtags)
>     - article: Display as `Posts` in the APP (search articles)
> ### Return:
> - Search results
>
> # [示例/Example]
> query = "lemon8"
> max_cursor = ""
> filter_type = ""
> order_by = ""
> search_tab = "main"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | lemon8 | None |
| max_cursor | query | string | No | 翻页参数/Pagination parameter | None | None | None |
| filter_type | query | string | No | 搜索过滤类型/Search filter type | None | None | None |
| order_by | query | string | No | 搜索排序方式/Search sort type | None | None | None |
| search_tab | query | string | No | 搜索类型/Search type | main | main | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-topic-info"></a>
### `GET /api/u1/v1/lemon8/app/fetch_topic_info`

- Summary: 获取话题信息/Get topic information
- Capabilities: topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取话题信息
> ### 参数:
> - forum_id: 话题ID，可以从下面的接口获取
>     - 获取指定作品的信息：`/lemon8/app/fetch_post_detail`
>     - 获取发现页的 Editor's Picks：`/lemon8/app/fetch_discover_tab_information_tabs`
>     - 通过接口搜索 Hashtag：`/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8`
> ### 返回:
> - 话题信息
>
> # [English]
> ### Purpose:
> - Get topic information
> ### Parameters:
> - forum_id: Topic ID, can be obtained from the following interfaces
>     - Get information of specified post: `/lemon8/app/fetch_post_detail`
>     - Get Editor's Picks of discover page: `/lemon8/app/fetch_discover_tab_information_tabs`
>     - Search Hashtag through interface: `/lemon8/app/fetch_search?search_tab=hashtag&keyword=lemon8`
> ### Return:
> - Topic information
>
> # [示例/Example]
> forum_id = "7174447913778593798"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| forum_id | query | string | Yes | 话题ID/Topic ID | None | 7174447913778593798 | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-topic-post-list"></a>
### `GET /api/u1/v1/lemon8/app/fetch_topic_post_list`

- Summary: 获取话题作品列表/Get topic post list
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取话题作品列表
> ### 参数:
> - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取
> - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。
> - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取
> - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取
> - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。
> ### 返回:
> - 作品列表
>
> # [English]
> ### Purpose:
> - Get topic post list
> ### Parameters:
> - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
> - max_behot_time: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests.
> - category_parameter: Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
> - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`
> - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass other values.
> ### Return:
> - Post list
>
> # [示例/Example]
> category = "590"
> max_behot_time = ""
> category_parameter = "7174447913778593798"
> hashtag_name = "lemon8christmas"
> sort_type = "0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category | query | string | Yes | 话题分类 ID/Topic category ID | None | 590 | None |
| max_behot_time | query | string | No | 翻页参数/Pagination parameter | None | None | None |
| category_parameter | query | string | Yes | 分类参数/Category parameter | None | 7174447913778593798 | None |
| hashtag_name | query | string | Yes | Hashtag名称/Hashtag name | None | lemon8christmas | None |
| sort_type | query | string | No | 排序方式/Sort type | 0 | None | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-user-follower-list"></a>
### `GET /api/u1/v1/lemon8/app/fetch_user_follower_list`

- Summary: 获取指定用户的粉丝列表/Get fans list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的粉丝列表
> ### 参数:
> - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
> - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
> ### 返回:
> - 粉丝列表
>
> # [English]
> ### Purpose:
> - Get fans list of specified user
> ### Parameters:
> - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
> - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests.
> ### Return:
> - Fans list
>
> # [示例/Example]
> user_id = "7428056850216862763"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 7428056850216862763 | None |
| cursor | query | string | No | 翻页参数/Pagination parameter | None | None | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-user-following-list"></a>
### `GET /api/u1/v1/lemon8/app/fetch_user_following_list`

- Summary: 获取指定用户的关注列表/Get following list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的关注列表
> ### 参数:
> - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
> - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
> ### 返回:
> - 关注列表
>
> # [English]
> ### Purpose:
> - Get following list of specified user
> ### Parameters:
> - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
> - cursor: Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests.
> ### Return:
> - Following list
>
> # [示例/Example]
> user_id = "7428056850216862763"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 7428056850216862763 | None |
| cursor | query | string | No | 翻页参数/Pagination parameter | None | None | None |

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

<a id="get-api-u1-v1-lemon8-app-fetch-user-profile"></a>
### `GET /api/u1/v1/lemon8/app/fetch_user_profile`

- Summary: 获取指定用户的信息/Get information of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的信息
> ### 参数:
> - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user
> ### Parameters:
> - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
> ### Return:
> - User information
>
> # [示例/Example]
> user_id = "7217844966059656197"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 7217844966059656197 | None |

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

<a id="get-api-u1-v1-lemon8-app-get-item-id"></a>
### `GET /api/u1/v1/lemon8/app/get_item_id`

- Summary: 通过分享链接获取作品ID/Get post ID through sharing link
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_item_id_api_v1_lemon8_app_get_item_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取作品ID
> ### 参数:
> - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
> ### 返回:
> - 作品ID
>
> # [English]
> ### Purpose:
> - Get post ID through sharing link
> ### Parameters:
> - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP.
> ### Return:
> - Post ID
>
> # [示例/Example]
> share_text = "https://www.lemon8-app.com/@deathlabs_/7445613324903006766"
> share_text = "https://v.lemon8-app.com/al/OghwFTppx"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | Yes | 分享链接/Share link | None | https://v.lemon8-app.com/al/OghwFTppx | None |

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

<a id="post-api-u1-v1-lemon8-app-get-item-ids"></a>
### `POST /api/u1/v1/lemon8/app/get_item_ids`

- Summary: 通过分享链接批量获取作品ID/Get post IDs in batch through sharing links
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_item_ids_api_v1_lemon8_app_get_item_ids_post`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接批量获取作品ID，一次最多获取10个
> ### 参数:
> - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
> ### 返回:
> - 作品ID列表
>
> # [English]
> ### Purpose:
> - Get post IDs in batch through sharing links, up to 10 at a time
> ### Parameters:
> - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP.
> ### Return:
> - Post IDs list
>
> # [示例/Example]
> share_texts = [
>     "https://www.lemon8-app.com/@deathlabs_/7445613324903006766",
>     "https://v.lemon8-app.com/al/OghwFTppx"
> ]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [Not declared]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<Not declared> | Yes | 分享链接列表/Share links list | None | None | None |

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

<a id="get-api-u1-v1-lemon8-app-get-user-id"></a>
### `GET /api/u1/v1/lemon8/app/get_user_id`

- Summary: 通过分享链接获取用户ID/Get user ID through sharing link
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_id_api_v1_lemon8_app_get_user_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取用户ID
> ### 参数:
> - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
> ### 返回:
> - 用户ID
>
> # [English]
> ### Purpose:
> - Get user ID through sharing link
> ### Parameters:
> - share_text: Share link, supports long links and short links, can be obtained and copied from the share button on the web and APP.
> ### Return:
> - User ID
>
> # [示例/Example]
> share_text = "https://www.lemon8-app.com/lemon8cars?region=us"
> share_text = "https://v.lemon8-app.com/al/OgZrsUppx"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | Yes | 分享链接/Share link | None | https://v.lemon8-app.com/al/OgZrsUppx | None |

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

<a id="post-api-u1-v1-lemon8-app-get-user-ids"></a>
### `POST /api/u1/v1/lemon8/app/get_user_ids`

- Summary: 通过分享链接批量获取用户ID/Get user IDs in batch through sharing links
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_ids_api_v1_lemon8_app_get_user_ids_post`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接批量获取用户ID，一次最多获取10个
> ### 参数:
> - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
> ### 返回:
> - 用户ID列表
>
> # [English]
> ### Purpose:
> - Get user IDs in batch through sharing links, up to 10 at a time
> ### Parameters:
> - share_texts: Share links list, supports long links and short links, can be obtained and copied from the share button on the web and APP.
> ### Return:
> - User IDs list
>
> # [示例/Example]
> share_texts = [
>     "https://www.lemon8-app.com/lemon8cars?region=us",
>     "https://v.lemon8-app.com/al/OgZrsUppx"
> ]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [Not declared]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<Not declared> | Yes | 分享链接列表/Share links list | None | None | None |

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
