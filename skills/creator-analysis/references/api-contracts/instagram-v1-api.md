# Instagram-V1-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/instagram-v1-api.md`](../api-tags/instagram-v1-api.md)
- 当前契约文件：`api-contracts/instagram-v1-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`29`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(Instagram V1数据接口（优先使用V1接口，V2接口仅在V1接口无法满足需求时使用）/Instagram-V1-API endpoints (Prefer using V1 endpoints, V2 endpoints are only for use when V1 endpoints cannot meet the requirements))**

## 路由契约

<a id="get-api-u1-v1-instagram-v1-fetch-cities"></a>
### `GET /api/u1/v1/instagram/v1/fetch_cities`

- 摘要：获取国家城市列表/Get cities by country
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_cities_api_v1_instagram_v1_fetch_cities_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定国家的城市/地区列表
> ### 参数:
> - country_code: 国家代码，如US、CN、JP
> - page: 页码，默认1
> ### 返回:
> - `country_info`: 国家信息
> - `city_list`: 城市列表
> - `next_page`: 下一页页码
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get cities/regions list of specified country
> ### Parameters:
> - country_code: Country code, e.g. US, CN, JP
> - page: Page number, default 1
> ### Return:
> - `country_info`: Country info
> - `city_list`: Cities list
> - `next_page`: Next page number
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> country_code = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| country_code | query | string | 是 | 国家代码（如US、CN、JP）/Country code (e.g. US, CN, JP) | 无 | US | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-comment-replies"></a>
### `GET /api/u1/v1/instagram/v1/fetch_comment_replies`

- 摘要：获取评论的子评论列表/Get comment replies
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定评论下的子评论（二级评论/回复），支持分页
> ### 参数:
> - media_id: 帖子ID（媒体ID）
> - comment_id: 父评论ID（从fetch_post_comments_v2返回的评论pk字段获取）
> - min_id: 分页游标，首次请求不传，从上一次响应的`page_info.next_min_id`字段获取
> ### 返回:
> - `child_comments`: 子评论列表，每个评论包含：
>   - `pk`: 评论ID
>   - `text`: 评论内容
>   - `created_at`/`created_at_utc`: 评论时间戳
>   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）
>   - `comment_like_count`: 评论点赞数
>   - `parent_comment_id`: 父评论ID
>   - `has_translation`: 是否有翻译
> - `child_comment_count`: 子评论总数
> - `has_more_tail_child_comments`: 是否有更多子评论
> - `next_min_child_cursor`: 下一页游标
> - `page_info`: 分页信息汇总
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get child comments (replies) under a specific comment with pagination
> ### Parameters:
> - media_id: Post ID (Media ID)
> - comment_id: Parent comment ID (get from pk field in fetch_post_comments_v2 response)
> - min_id: Pagination cursor, omit for first request, get from previous response's `page_info.next_min_id`
> ### Return:
> - `child_comments`: Child comment list, each comment contains:
>   - `pk`: Comment ID
>   - `text`: Comment content
>   - `created_at`/`created_at_utc`: Comment timestamp
>   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url, etc.)
>   - `comment_like_count`: Comment like count
>   - `parent_comment_id`: Parent comment ID
>   - `has_translation`: Has translation
> - `child_comment_count`: Total child comment count
> - `has_more_tail_child_comments`: Has more child comments
> - `next_min_child_cursor`: Next page cursor
> - `page_info`: Pagination info summary
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> media_id = "3766120364183949816"
> comment_id = "17871667485468098"
> min_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | 是 | 帖子ID（媒体ID）/Post ID (Media ID) | 无 | 3766120364183949816 | 无 |
| comment_id | query | string | 是 | 父评论ID/Parent comment ID | 无 | 17871667485468098 | 无 |
| min_id | query | string | 否 | 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-explore-sections"></a>
### `GET /api/u1/v1/instagram/v1/fetch_explore_sections`

- 摘要：获取探索页面分类/Get explore page sections
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取Instagram探索页面的所有分类和子分类
> ### 返回:
> - `sections`: 分类列表，包含分类名称、子分类和推荐内容
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get all sections and subsections of Instagram explore page
> ### Return:
> - `sections`: Sections list with names, subsections and recommended content
> ### Price:
> - 0.001 USD/request

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-hashtag-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_hashtag_posts`

- 摘要：获取话题标签下的帖子/Get posts by hashtag
- 能力：作品详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定话题标签下的帖子列表
> ### 参数:
> - hashtag: 话题标签名称（不含#号）
> - end_cursor: 分页游标，首次请求不传
> ### 返回:
> - GraphQL风格响应，包含`data.hashtag.edge_hashtag_to_media`
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts under specific hashtag
> ### Parameters:
> - hashtag: Hashtag name (without #)
> - end_cursor: Pagination cursor, omit for first request
> ### Return:
> - GraphQL style response with `data.hashtag.edge_hashtag_to_media`
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> hashtag = "cat"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hashtag | query | string | 是 | 话题标签名称（不含#号）/Hashtag name (without #) | 无 | cat | 无 |
| end_cursor | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-location-info"></a>
### `GET /api/u1/v1/instagram/v1/fetch_location_info`

- 摘要：获取地点信息/Get location info
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_location_info_api_v1_instagram_v1_fetch_location_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定地点的详细信息
> ### 参数:
> - location_id: 地点ID
> ### 返回:
> - `location_info`: 地点信息，包含名称、地址、坐标等
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get detailed information of specified location
> ### Parameters:
> - location_id: Location ID
> ### Return:
> - `location_info`: Location info including name, address, coordinates etc.
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> location_id = "703457703"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| location_id | query | string | 是 | 地点ID/Location ID | 无 | 703457703 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-location-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_location_posts`

- 摘要：获取地点下的帖子/Get posts by location
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定地点标记的帖子列表
> ### 参数:
> - location_id: 地点ID
> - tab: 排序方式，ranked(热门)/recent(最新)
> - end_cursor: 分页游标，首次请求不传
> ### 返回:
> - `edges`: 帖子列表
> - `page_info`: 分页信息
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts tagged at specified location
> ### Parameters:
> - location_id: Location ID
> - tab: Sorting method, ranked(top)/recent(latest)
> - end_cursor: Pagination cursor, omit for first request
> ### Return:
> - `edges`: Posts list
> - `page_info`: Pagination info
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> location_id = "703457703"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| location_id | query | string | 是 | 地点ID/Location ID | 无 | 703457703 | 无 |
| tab | query | string | 否 | 排序方式：ranked(热门)/recent(最新)/Sorting: ranked(top)/recent(latest) | ranked | 无 | 无 |
| end_cursor | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-locations"></a>
### `GET /api/u1/v1/instagram/v1/fetch_locations`

- 摘要：获取城市地点列表/Get locations by city
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_locations_api_v1_instagram_v1_fetch_locations_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定城市下的Instagram地点列表
> ### 参数:
> - city_id: 城市ID（可从fetch_cities接口获取）
> - page: 页码，默认1
> ### 返回:
> - `country_info`: 国家信息
> - `city_info`: 城市信息
> - `location_list`: 地点列表
> - `next_page`: 下一页页码
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram locations list of specified city
> ### Parameters:
> - city_id: City ID (from fetch_cities API)
> - page: Page number, default 1
> ### Return:
> - `country_info`: Country info
> - `city_info`: City info
> - `location_list`: Locations list
> - `next_page`: Next page number
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> city_id = "c2791472"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| city_id | query | string | 是 | 城市ID（从fetch_cities获取）/City ID (from fetch_cities) | 无 | c2791472 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-music-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_music_posts`

- 摘要：获取使用特定音乐的帖子/Get posts using specific music
- 能力：作品详情 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取使用指定音乐/音频的Reels和帖子列表
> ### 参数:
> - music_id: 音乐ID（与music_url二选一）
> - music_url: 音乐URL，会自动提取ID（与music_id二选一）
> - max_id: 分页游标，首次请求不传
> ### 返回:
> - `items`: 帖子列表
> - `metadata`: 音乐元数据
> - `paging_info`: 分页信息
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get Reels and posts using specific music/audio
> ### Parameters:
> - music_id: Music ID (alternative to music_url)
> - music_url: Music URL, ID will be extracted automatically (alternative to music_id)
> - max_id: Pagination cursor, omit for first request
> ### Return:
> - `items`: Posts list
> - `metadata`: Music metadata
> - `paging_info`: Pagination info
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> music_id = "564058920086577"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| music_id | query | string | 否 | 音乐ID/Music ID | 无 | 564058920086577 | 无 |
| music_url | query | string | 否 | 音乐URL（与music_id二选一）/Music URL (alternative to music_id) | 无 | https://www.instagram.com/reels/audio/564058920086577 | 无 |
| max_id | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-post-by-id"></a>
### `GET /api/u1/v1/instagram/v1/fetch_post_by_id`

- 摘要：通过ID获取帖子详情/Get post by ID
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过ID获取单个帖子的详细信息
> ### 参数:
> - post_id: 帖子ID
> ### 返回:
> - 帖子详情对象，包含媒体、点赞数、评论等
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get single post details by ID
> ### Parameters:
> - post_id: Post ID
> ### Return:
> - Post details object with media, likes, comments etc.
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> post_id = "3742637871112032100"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | 是 | 帖子ID/Post ID | 无 | 3742637871112032100 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-post-by-url"></a>
### `GET /api/u1/v1/instagram/v1/fetch_post_by_url`

- 摘要：通过URL获取帖子详情/Get post by URL
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过URL获取单个帖子的详细信息
> ### 参数:
> - post_url: 帖子URL
> ### 返回:
> - 帖子详情对象，包含媒体、点赞数、评论等
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get single post details by URL
> ### Parameters:
> - post_url: Post URL
> ### Return:
> - Post details object with media, likes, comments etc.
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> post_url = "https://www.instagram.com/p/DPwhVB-jo9k/"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_url | query | string | 是 | 帖子URL/Post URL | 无 | https://www.instagram.com/p/DPwhVB-jo9k/ | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-post-by-url-v2"></a>
### `GET /api/u1/v1/instagram/v1/fetch_post_by_url_v2`

- 摘要：通过URL获取帖子详情 V2/Get post by URL V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过URL获取单个帖子的详细信息 V2 - 数据没有V1完整，但速度更快，用于下载大量帖子时推荐使用。
> ### 参数:
> - post_url: 帖子URL
> ### 返回:
> - 帖子详情对象，包含媒体、点赞数、评论等
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get single post details by URL V2 - Data is not as complete as V1, but faster. Recommended for downloading large number of posts.
> ### Parameters:
> - post_url: Post URL
> ### Return:
> - Post details object with media, likes, comments etc.
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> post_url = "https://www.instagram.com/p/DPwhVB-jo9k/"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_url | query | string | 是 | 帖子URL/Post URL | 无 | https://www.instagram.com/p/DPwhVB-jo9k/ | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-post-comments-v2"></a>
### `GET /api/u1/v1/instagram/v1/fetch_post_comments_v2`

- 摘要：获取帖子评论列表V2/Get post comments V2
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取帖子评论列表，支持分页
> - 返回的评论数据更完整，包含子评论预览和更多元数据
> ### 参数:
> - media_id: 帖子ID（媒体ID）
> - sort_order: 排序方式，popular(热门)/recent(最新)
> - min_id: 分页游标，首次请求不传，从上一次响应的`next_min_id`字段获取
> ### 返回:
> - `comment_count`: 评论总数
> - `comments`: 评论列表，每个评论包含：
>   - `pk`: 评论ID
>   - `text`: 评论内容
>   - `created_at`/`created_at_utc`: 评论时间戳
>   - `user`: 评论者信息（pk, username, full_name, is_verified, profile_pic_url等）
>   - `comment_like_count`: 评论点赞数
>   - `child_comment_count`: 子评论数量
>   - `preview_child_comments`: 子评论预览列表
>   - `is_liked_by_media_owner`: 是否被帖子作者点赞
>   - `has_translation`: 是否有翻译
> - `next_min_id`: 下一页游标（JSON格式字符串）
> - `has_more_headload_comments`: 是否有更多评论
> - `caption`: 帖子描述信息
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get post comments list with pagination
> - Returns more complete comment data including child comment previews and more metadata
> ### Parameters:
> - media_id: Post ID (Media ID)
> - sort_order: Sorting method, popular/recent
> - min_id: Pagination cursor, omit for first request, get from previous response's `next_min_id`
> ### Return:
> - `comment_count`: Total comments count
> - `comments`: Comments list, each comment contains:
>   - `pk`: Comment ID
>   - `text`: Comment content
>   - `created_at`/`created_at_utc`: Comment timestamp
>   - `user`: Commenter info (pk, username, full_name, is_verified, profile_pic_url etc.)
>   - `comment_like_count`: Comment likes count
>   - `child_comment_count`: Child comments count
>   - `preview_child_comments`: Child comments preview list
>   - `is_liked_by_media_owner`: Whether liked by post author
>   - `has_translation`: Whether translation available
> - `next_min_id`: Next page cursor (JSON format string)
> - `has_more_headload_comments`: Whether more comments available
> - `caption`: Post caption info
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> media_id = "3766120364183949816"
> sort_order = "recent"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | 是 | 帖子ID（媒体ID）/Post ID (Media ID) | 无 | 3766120364183949816 | 无 |
| sort_order | query | string | 否 | 排序方式：popular(热门)/recent(最新)/Sorting: popular/recent | recent | recent | 无 |
| min_id | query | string | 否 | 分页游标，从上一次响应的next_min_id获取/Pagination cursor from previous response's next_min_id | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-related-profiles"></a>
### `GET /api/u1/v1/instagram/v1/fetch_related_profiles`

- 摘要：获取相关用户推荐/Get related profiles
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取与指定用户相关/相似的用户推荐列表
> ### 参数:
> - user_id: Instagram用户ID
> ### 返回:
> - GraphQL风格响应，包含`data.user.edge_related_profiles`
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get related/similar user recommendations
> ### Parameters:
> - user_id: Instagram user ID
> ### Return:
> - GraphQL style response with `data.user.edge_related_profiles`
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-search"></a>
### `GET /api/u1/v1/instagram/v1/fetch_search`

- 摘要：搜索用户/话题/地点/Search users/hashtags/places
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_api_v1_instagram_v1_fetch_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram上的用户、话题标签或地点
> ### 参数:
> - query: 搜索关键词
> - select: 筛选类型（可选）
>   - `users`: 仅返回用户
>   - `hashtags`: 仅返回话题标签
>   - `places`: 仅返回地点
>   - 不传: 返回所有类型
> ### 返回:
> - `users`: 用户列表
> - `hashtags`: 话题列表
> - `places`: 地点列表
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Search users, hashtags or places on Instagram
> ### Parameters:
> - query: Search keyword
> - select: Filter type (optional)
>   - `users`: Only return users
>   - `hashtags`: Only return hashtags
>   - `places`: Only return places
>   - omit: Return all types
> ### Return:
> - `users`: Users list
> - `hashtags`: Hashtags list
> - `places`: Places list
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> query = "taylorswift"
> select = "users"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | taylorswift | 无 |
| select | query | string | 否 | 筛选类型：users/hashtags/places，不传则返回全部/Filter type: users/hashtags/places, omit for all | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-section-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_section_posts`

- 摘要：获取分类下的帖子/Get posts by section
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取探索页面某个分类下的帖子列表
> ### 参数:
> - section_id: 分类ID（可从fetch_explore_sections接口获取）
> - count: 每页数量，默认20
> - max_id: 分页游标，首次请求不传
> ### 返回:
> - `section_name`: 分类名称
> - `items`: 帖子列表
> - `subsections`: 子分类列表
> - `max_id`: 下一页游标
> - `more_available`: 是否有更多数据
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts under specific explore section
> ### Parameters:
> - section_id: Section ID (from fetch_explore_sections API)
> - count: Count per page, default 20
> - max_id: Pagination cursor, omit for first request
> ### Return:
> - `section_name`: Section name
> - `items`: Posts list
> - `subsections`: Subsections list
> - `max_id`: Next page cursor
> - `more_available`: Whether more data available
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> section_id = "10156104410190727"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| section_id | query | string | 是 | 分类ID（从fetch_explore_sections获取）/Section ID (from fetch_explore_sections) | 无 | 10156104410190727 | 无 |
| count | query | integer | 否 | 每页数量/Count per page | 20 | 无 | 无 |
| max_id | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-about-info"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_about_info`

- 摘要：获取用户的About信息/Get user about info
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户的"关于此账户"（About This Account）信息
> - 包含账户创建日期、所在地区、认证状态等详细信息
> ### 参数:
> - user_id: Instagram用户ID（数字格式）
> ### 返回:
> - `status`: 请求状态
> - `user_id`: 用户ID
> - `username`: 用户名
> - `profile_pic_url`: 头像URL
> - `is_verified`: 是否认证
> - `date_joined`: 账户创建日期（如："June 2012"）
> - `account_based_in`: 账户所在地区（如："United States"）
> - `verified_date`: 认证日期（如："August 2017"，未认证则为None）
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user's "About This Account" information
> - Contains account creation date, location, verification status and more
> ### Parameters:
> - user_id: Instagram user ID (numeric format)
> ### Return:
> - `status`: Request status
> - `user_id`: User ID
> - `username`: Username
> - `profile_pic_url`: Profile picture URL
> - `is_verified`: Whether verified
> - `date_joined`: Account creation date (e.g., "June 2012")
> - `account_based_in`: Account location (e.g., "United States")
> - `verified_date`: Verification date (e.g., "August 2017", None if not verified)
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "182988865"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 182988865 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-info-by-id"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id`

- 摘要：根据用户ID获取用户数据/Get user data by user ID
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据Instagram用户ID获取用户数据
> ### 参数:
> - user_id: Instagram用户ID
> ### 返回:
> - 用户信息对象，包含时间线媒体、高清头像等完整数据
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user data by Instagram user ID
> ### Parameters:
> - user_id: Instagram user ID
> ### Return:
> - User information object with timeline media, HD avatar and complete data
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-info-by-id-v2"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id_v2`

- 摘要：根据用户ID获取用户数据V2/Get user data by user ID V2
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据Instagram用户ID获取用户数据，返回更详细的信息
> ### 参数:
> - user_id: Instagram用户ID
> ### 返回:
> - 用户信息对象，包含bio_links、hd_profile_pic_url_info等更多字段
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user data by Instagram user ID with more details
> ### Parameters:
> - user_id: Instagram user ID
> ### Return:
> - User information object with bio_links, hd_profile_pic_url_info and more
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-info-by-username"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username`

- 摘要：根据用户名获取用户数据/Get user data by username
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据Instagram用户名获取用户数据
> ### 参数:
> - username: Instagram用户名
> ### 返回:
> - 用户信息对象，包含以下主要字段：
>   - `id`: 用户ID
>   - `username`: 用户名
>   - `full_name`: 用户全名
>   - `biography`: 个人简介
>   - `bio_links`: 个人简介链接列表
>   - `edge_followed_by`: 粉丝数 {count: xxx}
>   - `edge_follow`: 关注数 {count: xxx}
>   - `profile_pic_url`: 头像URL
>   - `profile_pic_url_hd`: 高清头像URL
>   - `is_private`: 是否私密账户
>   - `is_verified`: 是否已认证
>   - `external_url`: 外部链接
>   - `is_business_account`: 是否商业账户
>   - `is_professional_account`: 是否专业账户
>   - `highlight_reel_count`: 精选集数量
>   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近帖子）
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user data by Instagram username
> ### Parameters:
> - username: Instagram username
> ### Return:
> - User information object with main fields:
>   - `id`: User ID
>   - `username`: Username
>   - `full_name`: Full name
>   - `biography`: Bio
>   - `bio_links`: Bio links list
>   - `edge_followed_by`: Followers count {count: xxx}
>   - `edge_follow`: Following count {count: xxx}
>   - `profile_pic_url`: Profile picture URL
>   - `profile_pic_url_hd`: HD profile picture URL
>   - `is_private`: Whether account is private
>   - `is_verified`: Whether account is verified
>   - `external_url`: External link
>   - `is_business_account`: Whether business account
>   - `is_professional_account`: Whether professional account
>   - `highlight_reel_count`: Highlights count
>   - `edge_owner_to_timeline_media`: Timeline media (contains recent posts)
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> username = "instagram"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | Instagram用户名/Instagram username | 无 | instagram | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v2"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v2`

- 摘要：根据用户名获取用户数据V2/Get user data by username V2
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据Instagram用户名获取用户数据
> ### 参数:
> - username: Instagram用户名
> ### 返回:
> - 用户信息对象，包含以下主要字段：
>   - `id`: 用户ID
>   - `username`: 用户名
>   - `full_name`: 用户全名
>   - `biography`: 个人简介
>   - `bio_links`: 个人简介链接列表
>   - `edge_followed_by`: 粉丝数 {count: xxx}
>   - `edge_follow`: 关注数 {count: xxx}
>   - `profile_pic_url`: 头像URL
>   - `profile_pic_url_hd`: 高清头像URL
>   - `is_private`: 是否私密账户
>   - `is_verified`: 是否已认证
>   - `external_url`: 外部链接
>   - `is_business_account`: 是否商业账户
>   - `is_professional_account`: 是否专业账户
>   - `highlight_reel_count`: 精选集数量
>   - `edge_owner_to_timeline_media`: 时间线媒体（包含最近12条帖子）
>   - `status`: 请求状态
>   - `attempts`: 尝试次数
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user data by Instagram username
> ### Parameters:
> - username: Instagram username
> ### Return:
> - User information object with main fields:
>   - `id`: User ID
>   - `username`: Username
>   - `full_name`: Full name
>   - `biography`: Bio
>   - `bio_links`: Bio links list
>   - `edge_followed_by`: Followers count {count: xxx}
>   - `edge_follow`: Following count {count: xxx}
>   - `profile_pic_url`: Profile picture URL
>   - `profile_pic_url_hd`: HD profile picture URL
>   - `is_private`: Whether account is private
>   - `is_verified`: Whether account is verified
>   - `external_url`: External link
>   - `is_business_account`: Whether business account
>   - `is_professional_account`: Whether professional account
>   - `highlight_reel_count`: Highlights count
>   - `edge_owner_to_timeline_media`: Timeline media (contains recent 12 posts)
>   - `status`: Request status
>   - `attempts`: Retry attempts
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> username = "instagram"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | Instagram用户名/Instagram username | 无 | instagram | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-info-by-username-v3"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v3`

- 摘要：根据用户名获取用户数据V3/Get user data by username V3
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据Instagram用户名获取用户数据，返回更详细的信息
> ### 参数:
> - username: Instagram用户名
> ### 返回:
> - 用户信息对象，包含以下主要字段：
>   - `pk/id`: 用户ID
>   - `username`: 用户名
>   - `full_name`: 用户全名
>   - `biography`: 个人简介
>   - `bio_links`: 个人简介链接列表
>   - `follower_count`: 粉丝数
>   - `following_count`: 关注数
>   - `media_count`: 媒体数量
>   - `profile_pic_url`: 头像URL
>   - `hd_profile_pic_url_info`: 高清头像URL信息
>   - `is_private`: 是否私密账户
>   - `is_verified`: 是否已认证
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user data by Instagram username with more details
> ### Parameters:
> - username: Instagram username
> ### Return:
> - User information object with main fields:
>   - `pk/id`: User ID
>   - `username`: Username
>   - `full_name`: Full name
>   - `biography`: Bio
>   - `bio_links`: Bio links list
>   - `follower_count`: Followers count
>   - `following_count`: Following count
>   - `media_count`: Media count
>   - `profile_pic_url`: Profile picture URL
>   - `hd_profile_pic_url_info`: HD profile picture URL info
>   - `is_private`: Whether account is private
>   - `is_verified`: Whether account is verified
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> username = "instagram"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | Instagram用户名/Instagram username | 无 | instagram | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_posts`

- 摘要：获取用户帖子列表/Get user posts list
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户帖子列表，支持分页
> ### 参数:
> - user_id: Instagram用户ID
> - count: 每页数量，默认12
> - max_id: 分页游标，首次请求不传
> ### 返回:
> - `items`: 帖子列表
> - `more_available`: 是否有更多数据
> - `next_max_id`: 下一页游标
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user posts list with pagination support
> ### Parameters:
> - user_id: Instagram user ID
> - count: Count per page, default 12
> - max_id: Pagination cursor, omit for first request
> ### Return:
> - `items`: Posts list
> - `more_available`: Whether more data available
> - `next_max_id`: Next page cursor
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |
| count | query | integer | 否 | 每页数量/Count per page | 12 | 无 | 无 |
| max_id | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-posts-v2"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_posts_v2`

- 摘要：获取用户帖子列表V2/Get user posts list V2
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户帖子列表，支持分页
> ### 参数:
> - user_id: Instagram用户ID
> - count: 每页数量，默认12
> - end_cursor: 分页游标，首次请求不传
> ### 返回:
> - GraphQL风格响应，包含`data.user.edge_owner_to_timeline_media`
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user posts list with pagination
> ### Parameters:
> - user_id: Instagram user ID
> - count: Count per page, default 12
> - end_cursor: Pagination cursor, omit for first request
> ### Return:
> - GraphQL style response with `data.user.edge_owner_to_timeline_media`
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |
| count | query | integer | 否 | 每页数量/Count per page | 12 | 无 | 无 |
| end_cursor | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-reels"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_reels`

- 摘要：获取用户Reels列表/Get user Reels list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户Reels短视频列表，支持分页
> ### 参数:
> - user_id: Instagram用户ID
> - count: 每页数量，默认12
> - max_id: 分页游标，首次请求不传
> ### 返回:
> - `items`: Reels列表
> - `paging_info`: 分页信息
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user Reels list with pagination
> ### Parameters:
> - user_id: Instagram user ID
> - count: Count per page, default 12
> - max_id: Pagination cursor, omit for first request
> ### Return:
> - `items`: Reels list
> - `paging_info`: Pagination info
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |
| count | query | integer | 否 | 每页数量/Count per page | 12 | 无 | 无 |
| max_id | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-reposts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_reposts`

- 摘要：获取用户转发列表/Get user reposts list
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户转发/分享的帖子列表，支持分页
> ### 参数:
> - user_id: Instagram用户ID
> - max_id: 分页游标，首次请求不传
> ### 返回:
> - `items`: 转发帖子列表
> - `more_available`: 是否有更多数据
> - `next_max_id`: 下一页游标
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user reposts/shares list with pagination
> ### Parameters:
> - user_id: Instagram user ID
> - max_id: Pagination cursor, omit for first request
> ### Return:
> - `items`: Reposts list
> - `more_available`: Whether more data available
> - `next_max_id`: Next page cursor
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |
| max_id | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-fetch-user-tagged-posts"></a>
### `GET /api/u1/v1/instagram/v1/fetch_user_tagged_posts`

- 摘要：获取用户被标记的帖子/Get user tagged posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取其他用户帖子中标记了该用户的帖子列表
> ### 参数:
> - user_id: Instagram用户ID
> - count: 每页数量，默认12
> - end_cursor: 分页游标，首次请求不传
> ### 返回:
> - GraphQL风格响应，包含`data.user.edge_user_to_photos_of_you`
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts where this user is tagged by others
> ### Parameters:
> - user_id: Instagram user ID
> - count: Count per page, default 12
> - end_cursor: Pagination cursor, omit for first request
> ### Return:
> - GraphQL style response with `data.user.edge_user_to_photos_of_you`
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "25025320"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | Instagram用户ID/Instagram user ID | 无 | 25025320 | 无 |
| count | query | integer | 否 | 每页数量/Count per page | 12 | 无 | 无 |
| end_cursor | query | string | 否 | 分页游标，用于获取下一页/Pagination cursor for next page | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-media-id-to-shortcode"></a>
### `GET /api/u1/v1/instagram/v1/media_id_to_shortcode`

- 摘要：Media ID转Shortcode/Convert media ID to shortcode
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get`

#### 说明

> # [中文]
> ### 用途:
> - 将Instagram帖子的Media ID转换为Shortcode
> - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/
> ### 参数:
> - media_id: 帖子的Media ID
> ### 返回:
> - `status`: 转换状态
> - `media_id`: 原始Media ID
> - `shortcode`: 转换后的Shortcode
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Convert Instagram post media ID to shortcode
> - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/
> ### Parameters:
> - media_id: Post media ID
> ### Return:
> - `status`: Conversion status
> - `media_id`: Original media ID
> - `shortcode`: Converted shortcode
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> media_id = "3774507992167247878"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | 是 | 帖子Media ID/Post media ID | 无 | 3774507992167247878 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-shortcode-to-media-id"></a>
### `GET /api/u1/v1/instagram/v1/shortcode_to_media_id`

- 摘要：Shortcode转Media ID/Convert shortcode to media ID
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 将Instagram帖子的Shortcode转换为Media ID
> - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG
> ### 参数:
> - shortcode: 帖子的Shortcode
> ### 返回:
> - `status`: 转换状态
> - `shortcode`: 原始Shortcode
> - `media_id`: 转换后的Media ID
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Convert Instagram post shortcode to media ID
> - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/
> ### Parameters:
> - shortcode: Post shortcode
> ### Return:
> - `status`: Conversion status
> - `shortcode`: Original shortcode
> - `media_id`: Converted media ID
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> shortcode = "DRhvwVLAHAG"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shortcode | query | string | 是 | 帖子Shortcode/Post shortcode | 无 | DRhvwVLAHAG | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-instagram-v1-user-id-to-username"></a>
### `GET /api/u1/v1/instagram/v1/user_id_to_username`

- 摘要：用户ID转用户信息/Get user info by user ID
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`user_id_to_username_api_v1_instagram_v1_user_id_to_username_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过Instagram用户ID获取用户信息
> - 可用于将用户ID转换为用户名及获取完整用户资料
> ### 参数:
> - user_id: 用户ID
> ### 返回:
> - `pk`/`pk_id`: 用户ID
> - `username`: 用户名
> - `full_name`: 用户全名
> - `is_private`: 是否私密账户
> - `is_verified`: 是否已认证
> - `profile_pic_url`: 头像URL
> - `biography`: 个人简介
> - `follower_count`: 粉丝数
> - `following_count`: 关注数
> - `media_count`: 帖子数
> ### 价格:
> - 0.001 USD/请求
>
> # [English]
> ### Purpose:
> - Get user info by Instagram user ID
> - Can be used to convert user ID to username and get full profile
> ### Parameters:
> - user_id: User ID
> ### Return:
> - `pk`/`pk_id`: User ID
> - `username`: Username
> - `full_name`: Full name
> - `is_private`: Whether account is private
> - `is_verified`: Whether account is verified
> - `profile_pic_url`: Profile picture URL
> - `biography`: Bio
> - `follower_count`: Followers count
> - `following_count`: Following count
> - `media_count`: Posts count
> ### Price:
> - 0.001 USD/request
>
> # [示例/Example]
> user_id = "18527"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | 18527 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |
