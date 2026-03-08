# Instagram-V3-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/instagram-v3-api.md`](../api-tags/instagram-v3-api.md)
- Current contract file: `api-contracts/instagram-v3-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `26`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Instagram V3数据接口/Instagram-V3-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-instagram-v3-bulk-translate-comments"></a>
### `GET /api/u1/v1/instagram/v3/bulk_translate_comments`

- Summary: 批量翻译评论/Bulk translate comments
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 批量翻译Instagram评论
> - 支持同时翻译多条评论，效率更高
> - 评论ID可从 get_post_comments 接口获取
> ### 参数:
> - comment_ids: 评论ID列表，多个ID用逗号分隔，**最多10条**
>     - 例如: `18099342953509681` （单个）
>     - 例如: `18099342953509681,18099342953509682,18099342953509683` （多个）
> ### 注意:
> - 单次请求最多支持10条评论ID，超过会返回错误
> ### 返回:
> - `data.comment_translations`: 翻译结果映射
>     - key: 评论ID
>     - value: 翻译后的文本
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Bulk translate Instagram comments
> - Support translating multiple comments at once for better efficiency
> - Comment IDs can be obtained from get_post_comments API
> ### Parameters:
> - comment_ids: Comment ID list, separated by commas, **max 10 IDs**
>     - Example: `18099342953509681` (single)
>     - Example: `18099342953509681,18099342953509682,18099342953509683` (multiple)
> ### Note:
> - Maximum 10 comment IDs per request, exceeding will return an error
> ### Return:
> - `data.comment_translations`: Translation result mapping
>     - key: Comment ID
>     - value: Translated text
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> comment_ids = "18099342953509681"
> # comment_ids = "18099342953509681,18099342953509682"
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| comment_ids | query | string | Yes | 评论ID列表，逗号分隔/Comment ID list, comma separated | None | 18099342953509681 | None |

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

<a id="get-api-u1-v1-instagram-v3-general-search"></a>
### `GET /api/u1/v1/instagram/v3/general_search`

- Summary: 综合搜索（支持分页）/General search (with pagination)
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `general_search_api_v1_instagram_v3_general_search_get`

#### Notes

> # [中文]
> ### 用途:
> - Instagram综合搜索接口（支持分页）
> - 支持通过 next_max_id 分页获取大量搜索结果
> - 返回用户、话题标签、地点等综合结果
> ### 参数:
> - query: 搜索关键词
> - next_max_id: 分页ID，首次请求不传，从上一次响应的 `data.next_max_id` 获取
> - rank_token: 排序token，首次请求不传，从上一次响应的 `data.rank_token` 获取
> - enable_metadata: 是否启用元数据
> ### 返回:
> - `data.num_results`: 结果数量
> - `data.users`: 用户搜索结果列表
> - `data.places`: 地点搜索结果列表
> - `data.hashtags`: 话题标签搜索结果列表
> - `data.next_max_id`: 下一页分页ID（传给下次请求的next_max_id参数）
> - `data.rank_token`: 排序token（传给下次请求的rank_token参数）
> - `data.has_more`: 是否有更多结果
> ### 注意事项:
> - ⚠️ **已知问题**: 综合搜索结果可能存在重复数据，这是 Instagram API 的已知行为
> - 搜索话题标签时，query 需要带上 `#` 前缀，例如搜索 fashion 话题应传入 `#fashion`
> - `#` 符号在 URL 中需要进行 URL 编码为 `%23`，例如: `?query=%23fashion`
> - 如果使用 HTTP 客户端库（如 requests/httpx），直接传入 `#fashion` 即可，库会自动处理编码
> ### 分页使用方法:
> 1. 首次请求：只传 `query` 参数
> 2. 获取响应中的 `next_max_id` 和 `rank_token`
> 3. 下次请求：传入 `query`、`next_max_id` 和 `rank_token`
> 4. 重复步骤 2-3 直到 `has_more` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Instagram general search API (with pagination)
> - Support pagination via next_max_id to fetch more search results
> - Returns blended results of users, hashtags, places, etc.
> ### Parameters:
> - query: Search keyword
> - next_max_id: Pagination ID, omit for first request, get from previous response `data.next_max_id`
> - rank_token: Rank token, omit for first request, get from previous response `data.rank_token`
> - enable_metadata: Enable metadata
> ### Return:
> - `data.num_results`: Number of results
> - `data.users`: User search results
> - `data.places`: Place search results
> - `data.hashtags`: Hashtag search results
> - `data.next_max_id`: Next page pagination ID (use as next_max_id in next request)
> - `data.rank_token`: Rank token (use as rank_token in next request)
> - `data.has_more`: Whether has more results
> ### Notes:
> - ⚠️ **Known Issue**: General search results may contain duplicate data, this is a known behavior of Instagram API
> - When searching for hashtags, `query` must include the `#` prefix, e.g., use `#fashion` to search for the fashion hashtag
> - The `#` character must be URL-encoded as `%23` in the URL, e.g., `?query=%23fashion`
> - If using an HTTP client library (e.g., requests/httpx), just pass `#fashion` directly and the library will handle encoding automatically
> ### Pagination usage:
> 1. First request: Only pass `query` parameter
> 2. Get `next_max_id` and `rank_token` from response
> 3. Next request: Pass `query`, `next_max_id` and `rank_token`
> 4. Repeat steps 2-3 until `has_more` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> query = "justin"
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | justin | None |
| next_max_id | query | string | No | 分页ID，首次请求不传，从上一次响应的next_max_id获取/Pagination ID, omit for first request, get from previous response next_max_id | None | None | None |
| rank_token | query | string | No | 排序token，首次请求不传，从上一次响应获取/Rank token, omit for first request, get from previous response | None | None | None |
| enable_metadata | query | boolean | No | 是否启用元数据/Enable metadata | true | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-comment-replies"></a>
### `GET /api/u1/v1/instagram/v3/get_comment_replies`

- Summary: 获取评论的子评论/回复/Get comment replies
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_comment_replies_api_v1_instagram_v3_get_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram评论的子评论（回复）列表
> - 支持分页获取所有回复
> - 父评论的 comment_id 可从 get_post_comments 接口的评论列表中获取
> - 支持通过 media_id、短代码（code）或帖子URL定位帖子
> ### 参数（三选一定位帖子）:
> - media_id: 帖子的媒体ID（数字ID）
> - code: 帖子短代码（如 DUajw4YkorV）
> - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`）
> ### 必填参数:
> - comment_id: 父评论ID（从 get_post_comments 返回的评论中获取 `pk` 字段）
> ### 其他参数:
> - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_child_cursor` 获取
> ### 返回:
> - `data.child_comments`: 子评论列表
>     - `user`: 评论者信息
>     - `text`: 评论文本
>     - `created_at`: 评论时间戳
>     - `comment_like_count`: 评论点赞数
>     - `pk`: 评论ID
> - `data.next_min_child_cursor`: 下一页分页游标（传给下次请求的min_id参数）
> - `data.has_more_tail_child_comments`: 是否有更多子评论
> - `data.num_tail_child_comments`: 剩余子评论数
> ### 分页使用方法:
> 1. 首次请求：传 `media_id` 和 `comment_id` 参数
> 2. 获取响应中的 `data.next_min_child_cursor`
> 3. 下次请求：传入 `media_id`、`comment_id` 和 `min_id` (使用上次的next_min_child_cursor)
> 4. 重复步骤 2-3 直到 `data.has_more_tail_child_comments` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram comment's child comments (replies) list
> - Support pagination to fetch all replies
> - Parent comment's comment_id can be obtained from get_post_comments API
> - Support querying by media_id, shortcode (code), or post URL
> ### Parameters (one of to locate post):
> - media_id: Post media ID (numeric ID)
> - code: Post shortcode (e.g., DUajw4YkorV)
> - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`)
> ### Required:
> - comment_id: Parent comment ID (get `pk` field from get_post_comments response)
> ### Other parameters:
> - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_child_cursor`
> ### Return:
> - `data.child_comments`: Child comments list
>     - `user`: Commenter info
>     - `text`: Comment text
>     - `created_at`: Comment timestamp
>     - `comment_like_count`: Comment likes count
>     - `pk`: Comment ID
> - `data.next_min_child_cursor`: Next page cursor (use as min_id in next request)
> - `data.has_more_tail_child_comments`: Whether has more child comments
> - `data.num_tail_child_comments`: Remaining child comments count
> ### Pagination usage:
> 1. First request: Pass `media_id` and `comment_id` parameters
> 2. Get `data.next_min_child_cursor` from response
> 3. Next request: Pass `media_id`, `comment_id`, and `min_id` (use next_min_child_cursor from previous)
> 4. Repeat steps 2-3 until `data.has_more_tail_child_comments` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> media_id = "3829530490739515971"
> comment_id = "18065937092249736"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID | None | 3829530490739515971 | None |
| code | query | string | No | 帖子短代码/Post shortcode | None | DUajw4YkorV | None |
| url | query | string | No | 帖子URL/Post URL | None | https://www.instagram.com/p/DUajw4YkorV/ | None |
| comment_id | query | string | Yes | 父评论ID/Parent comment ID | None | 18065937092249736 | None |
| min_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_min_child_cursor 获取/Pagination cursor, omit for first request, get from previous response next_min_child_cursor | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-explore"></a>
### `GET /api/u1/v1/instagram/v3/get_explore`

- Summary: 获取探索页推荐帖子/Get explore feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_explore_api_v1_instagram_v3_get_explore_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram探索/发现页的推荐帖子
> - 返回个性化推荐的帖子列表
> - 支持分页获取更多推荐内容
> ### 参数:
> - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取
> ### 返回:
> - `data.sectional_items`: 推荐内容分区列表
>     - `layout_content.medias`: 媒体列表
>         - `media.id`: 帖子ID
>         - `media.code`: 帖子短代码
>         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）
>         - `media.like_count`: 点赞数
>         - `media.comment_count`: 评论数
>         - `media.caption.text`: 帖子文本
>         - `media.user`: 发布者信息
>         - `media.image_versions2`: 图片版本列表
>         - `media.video_versions`: 视频版本列表（视频时存在）
> - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数）
> - `data.more_available`: 是否有更多内容
> ### 分页使用方法:
> 1. 首次请求：不传任何参数
> 2. 获取响应中的 `data.next_max_id`
> 3. 下次请求：传入 `max_id` (使用上次的next_max_id)
> 4. 重复步骤 2-3 直到 `data.more_available` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram Explore/Discover page recommended posts
> - Returns personalized recommended post list
> - Support pagination to fetch more recommendations
> ### Parameters:
> - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id`
> ### Return:
> - `data.sectional_items`: Recommended content section list
>     - `layout_content.medias`: Media list
>         - `media.id`: Post ID
>         - `media.code`: Post shortcode
>         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)
>         - `media.like_count`: Likes count
>         - `media.comment_count`: Comments count
>         - `media.caption.text`: Post caption text
>         - `media.user`: Publisher info
>         - `media.image_versions2`: Image version list
>         - `media.video_versions`: Video version list (exists for videos)
> - `data.next_max_id`: Next page cursor (use as max_id in next request)
> - `data.more_available`: Whether has more content
> ### Pagination usage:
> 1. First request: No parameters needed
> 2. Get `data.next_max_id` from response
> 3. Next request: Pass `max_id` (use next_max_id from previous)
> 4. Repeat steps 2-3 until `data.more_available` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> # 第一页 / First page (不传参数 / no parameters)
> # 第二页 / Second page
> # max_id = "..."  # 从第一页响应中获取 / Get from first page response
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-highlight-stories"></a>
### `GET /api/u1/v1/instagram/v3/get_highlight_stories`

- Summary: 获取Highlight精选详情/Get highlight stories
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram Highlight精选的详细故事/帖子内容
> - 返回精选集合中的所有Stories媒体
> ### 参数:
> - highlight_id: 精选ID，格式为 `highlight:xxx`（从 get_user_highlights 接口获取）
> - reel_ids: 精选ID列表，逗号分隔（可选，如不提供则仅查询highlight_id指定的精选）
>     - 例如: `highlight:18064916456320419,highlight:18155682898389765`
>     - 可同时查询多个精选的内容
> ### 返回:
> - `data.story_highlight_tray`: 精选故事集合
>     - `id`: 精选ID
>     - `title`: 精选标题
>     - `items`: 故事列表
>         - `id`: 故事ID
>         - `pk`: 故事PK
>         - `taken_at`: 发布时间戳
>         - `media_type`: 媒体类型（1=图片, 2=视频）
>         - `image_versions2`: 图片版本列表
>         - `video_versions`: 视频版本列表（视频时存在）
>         - `user`: 发布者信息
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram Highlight's detailed story/post content
> - Returns all Stories media in the highlight collection
> ### Parameters:
> - highlight_id: Highlight ID, format `highlight:xxx` (get from get_user_highlights API)
> - reel_ids: Highlight ID list, comma separated (optional, if not provided only queries the highlight_id)
>     - Example: `highlight:18064916456320419,highlight:18155682898389765`
>     - Can query multiple highlights at once
> ### Return:
> - `data.story_highlight_tray`: Highlight story collection
>     - `id`: Highlight ID
>     - `title`: Highlight title
>     - `items`: Story list
>         - `id`: Story ID
>         - `pk`: Story PK
>         - `taken_at`: Published timestamp
>         - `media_type`: Media type (1=image, 2=video)
>         - `image_versions2`: Image version list
>         - `video_versions`: Video version list (exists for videos)
>         - `user`: Publisher info
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> highlight_id = "highlight:18064916456320419"
> # reel_ids = "highlight:18064916456320419,highlight:18155682898389765"
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| highlight_id | query | string | Yes | 精选ID/Highlight ID (格式/format: highlight:xxx) | None | highlight:18064916456320419 | None |
| reel_ids | query | string | No | 精选ID列表，逗号分隔，如不提供则仅查询highlight_id/Highlight ID list, comma separated, if not provided only query highlight_id | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-location-info"></a>
### `GET /api/u1/v1/instagram/v3/get_location_info`

- Summary: 获取地点详情/Get location info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_location_info_api_v1_instagram_v3_get_location_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram地点的详细信息
> - 包含地点名称、地址、坐标、附近地点等
> - 地点ID可从搜索接口（search_places）或帖子详情中获取
> ### 参数:
> - location_id: 地点ID（数字）
> - show_nearby: 是否显示附近地点（默认true）
> ### 返回:
> - `data.native_location_data`: 地点基本信息
>     - `name`: 地点名称
>     - `address`: 地址
>     - `city`: 城市
>     - `lat`: 纬度
>     - `lng`: 经度
>     - `website`: 网站
>     - `phone`: 电话
>     - `category`: 分类
>     - `media_count`: 关联帖子数
> - `data.ranked`: 热门帖子信息
> - `data.recent`: 最新帖子信息
> - `data.nearby_locations`: 附近地点列表（show_nearby=true时）
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram location/place detail info
> - Including name, address, coordinates, nearby places, etc.
> - Location ID can be obtained from search API (search_places) or post details
> ### Parameters:
> - location_id: Location ID (numeric)
> - show_nearby: Whether to show nearby places (default true)
> ### Return:
> - `data.native_location_data`: Location basic info
>     - `name`: Location name
>     - `address`: Address
>     - `city`: City
>     - `lat`: Latitude
>     - `lng`: Longitude
>     - `website`: Website
>     - `phone`: Phone
>     - `category`: Category
>     - `media_count`: Associated posts count
> - `data.ranked`: Top posts info
> - `data.recent`: Recent posts info
> - `data.nearby_locations`: Nearby locations list (when show_nearby=true)
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> location_id = "1016248898"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID | None | 1016248898 | None |
| show_nearby | query | boolean | No | 是否显示附近地点/Whether to show nearby places | true | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-location-posts"></a>
### `GET /api/u1/v1/instagram/v3/get_location_posts`

- Summary: 获取地点相关帖子/Get location posts
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_location_posts_api_v1_instagram_v3_get_location_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram地点相关的帖子列表
> - 支持按热门或最新排序
> - 地点ID可从搜索接口（search_places）或帖子详情中获取
> ### 参数:
> - location_id: 地点ID（数字）
> - tab: 帖子排序方式
>     - `ranked`: 热门帖子（默认）
>     - `recent`: 最新帖子
> - page_size_override: 每页帖子数量（默认12）
> ### 返回:
> - `data.sections`: 帖子分区列表
>     - `layout_content.medias`: 媒体列表
>         - `media.id`: 帖子ID
>         - `media.code`: 帖子短代码
>         - `media.media_type`: 媒体类型（1=图片, 2=视频, 8=合集）
>         - `media.like_count`: 点赞数
>         - `media.comment_count`: 评论数
>         - `media.caption.text`: 帖子文本
>         - `media.user`: 发布者信息
> - `data.next_max_id`: 下一页分页游标
> - `data.next_page`: 下一页信息
> - `data.more_available`: 是否有更多内容
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram location-related posts
> - Support sorting by top or latest
> - Location ID can be obtained from search API (search_places) or post details
> ### Parameters:
> - location_id: Location ID (numeric)
> - tab: Post sort order
>     - `ranked`: Top posts (default)
>     - `recent`: Latest posts
> - page_size_override: Posts per page (default 12)
> ### Return:
> - `data.sections`: Post section list
>     - `layout_content.medias`: Media list
>         - `media.id`: Post ID
>         - `media.code`: Post shortcode
>         - `media.media_type`: Media type (1=image, 2=video, 8=carousel)
>         - `media.like_count`: Likes count
>         - `media.comment_count`: Comments count
>         - `media.caption.text`: Post caption text
>         - `media.user`: Publisher info
> - `data.next_max_id`: Next page cursor
> - `data.next_page`: Next page info
> - `data.more_available`: Whether has more content
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> location_id = "1016248898"
> tab = "ranked"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID | None | 1016248898 | None |
| tab | query | string | No | 帖子类型: ranked(热门), recent(最新)/Post type: ranked(top), recent(latest) | ranked | None | None |
| page_size_override | query | integer | No | 每页数量/Page size | 12 | 12 | None |

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

<a id="get-api-u1-v1-instagram-v3-get-post-comments"></a>
### `GET /api/u1/v1/instagram/v3/get_post_comments`

- Summary: 获取帖子评论/Get post comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_comments_api_v1_instagram_v3_get_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram帖子的评论列表
> - 支持分页获取所有评论
> - 支持按热门或最新排序
> - 支持通过 media_id、短代码（code）或帖子URL查询
> ### 参数（三选一）:
> - media_id: 帖子的媒体ID（数字ID）
> - code: 帖子短代码（如 DUajw4YkorV）
> - url: 帖子URL（如 `https://www.instagram.com/p/DUajw4YkorV/`）
> ### 其他参数:
> - min_id: 分页游标，首次请求不传，从上一次响应的 `data.next_min_id` 获取
> - sort_order: 排序方式
>     - `popular`: 按热门排序（默认）
>     - `newest`: 按最新排序
> ### 返回:
> - `data.comments`: 评论列表
>     - `user`: 评论者信息
>     - `text`: 评论文本
>     - `created_at`: 评论时间戳
>     - `comment_like_count`: 评论点赞数
>     - `child_comment_count`: 子评论数
> - `data.next_min_id`: 下一页分页游标（传给下次请求的min_id参数）
> - `data.has_more_comments`: 是否有更多评论
> - `data.comment_count`: 评论总数
> ### 分页使用方法:
> 1. 首次请求：传 `media_id`/`code`/`url` 参数
> 2. 获取响应中的 `data.next_min_id`
> 3. 下次请求：传入 `media_id` 和 `min_id` (使用上次的next_min_id)
> 4. 重复步骤 2-3 直到 `data.has_more_comments` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram post comment list
> - Support pagination to fetch all comments
> - Support sorting by popular or newest
> - Support querying by media_id, shortcode (code), or post URL
> ### Parameters (one of):
> - media_id: Post media ID (numeric ID)
> - code: Post shortcode (e.g., DUajw4YkorV)
> - url: Post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`)
> ### Other parameters:
> - min_id: Pagination cursor, omit for first request, get from previous response `data.next_min_id`
> - sort_order: Sort order
>     - `popular`: Sort by popular (default)
>     - `newest`: Sort by newest
> ### Return:
> - `data.comments`: Comment list
>     - `user`: Commenter info
>     - `text`: Comment text
>     - `created_at`: Comment timestamp
>     - `comment_like_count`: Comment likes count
>     - `child_comment_count`: Child comments count
> - `data.next_min_id`: Next page cursor (use as min_id in next request)
> - `data.has_more_comments`: Whether has more comments
> - `data.comment_count`: Total comment count
> ### Pagination usage:
> 1. First request: Pass `media_id`/`code`/`url` parameter
> 2. Get `data.next_min_id` from response
> 3. Next request: Pass `media_id` and `min_id` (use next_min_id from previous)
> 4. Repeat steps 2-3 until `data.has_more_comments` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> media_id = "3815455163747032886"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID | None | 3815455163747032886 | None |
| code | query | string | No | 帖子短代码/Post shortcode (e.g., DUajw4YkorV) | None | DUajw4YkorV | None |
| url | query | string | No | 帖子URL/Post URL | None | https://www.instagram.com/p/DUajw4YkorV/ | None |
| min_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_min_id 获取/Pagination cursor, omit for first request, get from previous response next_min_id | None | None | None |
| sort_order | query | string | No | 排序方式: popular(热门), newest(最新)/Sort order: popular, newest | popular | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-post-info"></a>
### `GET /api/u1/v1/instagram/v3/get_post_info`

- Summary: 获取帖子详情/Get post info (media_id or URL)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_info_api_v1_instagram_v3_get_post_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取帖子详情
> - 支持通过 media_id 或帖子 URL 获取
> - 返回帖子的完整信息，包括图片/视频、点赞数、评论数、发布者信息等
> ### 参数（二选一）:
> - media_id: 帖子的媒体ID（数字ID）
> - url: 帖子的完整URL（如 `https://www.instagram.com/p/DUajw4YkorV/`）
> ### 返回:
> - `data.items`: 帖子信息列表（通常只有一个元素）
>     - `id`: 帖子ID
>     - `code`: 帖子短代码
>     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）
>     - `like_count`: 点赞数
>     - `comment_count`: 评论数
>     - `caption.text`: 帖子文本
>     - `user`: 发布者信息
>     - `image_versions2`: 图片版本列表
>     - `video_versions`: 视频版本列表（视频时存在）
>     - `carousel_media`: 合集媒体列表（合集时存在）
>     - `taken_at`: 发布时间戳
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get post details
> - Support fetching by media_id or post URL
> - Returns complete post info including images/videos, likes, comments, author info, etc.
> ### Parameters (one of):
> - media_id: Post media ID (numeric ID)
> - url: Full post URL (e.g., `https://www.instagram.com/p/DUajw4YkorV/`)
> ### Return:
> - `data.items`: Post info list (usually only one element)
>     - `id`: Post ID
>     - `code`: Post shortcode
>     - `media_type`: Media type (1=image, 2=video, 8=carousel)
>     - `like_count`: Likes count
>     - `comment_count`: Comments count
>     - `caption.text`: Post caption text
>     - `user`: Publisher info
>     - `image_versions2`: Image version list
>     - `video_versions`: Video version list (exists for videos)
>     - `carousel_media`: Carousel media list (exists for carousels)
>     - `taken_at`: Published timestamp
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> media_id = "3800418264661789225"
> # 或通过URL / Or by URL
> # url = "https://www.instagram.com/p/DUajw4YkorV/"
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | No | 帖子媒体ID/Post media ID | None | 3800418264661789225 | None |
| url | query | string | No | 帖子URL/Post URL | None | https://www.instagram.com/p/DUajw4YkorV/ | None |

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

<a id="get-api-u1-v1-instagram-v3-get-post-info-by-code"></a>
### `GET /api/u1/v1/instagram/v3/get_post_info_by_code`

- Summary: 获取帖子详情(code)/Get post info by shortcode
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过帖子的短代码（code/shortcode）或URL获取帖子详情
> - 短代码即帖子URL中的标识符，如 `https://www.instagram.com/p/DUajw4YkorV/` 中的 `DUajw4YkorV`
> - 返回帖子的完整信息
> ### 参数（二选一）:
> - code: 帖子短代码（如 DUajw4YkorV）
> - url: 帖子URL（自动提取短代码）
> ### 返回:
> - `data.items`: 帖子信息列表
>     - `id`: 帖子ID
>     - `code`: 帖子短代码
>     - `media_type`: 媒体类型（1=图片, 2=视频, 8=合集）
>     - `like_count`: 点赞数
>     - `comment_count`: 评论数
>     - `caption.text`: 帖子文本
>     - `user`: 发布者信息
>     - `image_versions2`: 图片版本列表
>     - `video_versions`: 视频版本列表（视频时存在）
>     - `carousel_media`: 合集媒体列表（合集时存在）
>     - `taken_at`: 发布时间戳
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get post details by shortcode
> - Shortcode is the identifier in the post URL, e.g., `DUajw4YkorV` from `https://www.instagram.com/p/DUajw4YkorV/`
> - Returns complete post info
> ### Parameters:
> - code: Post shortcode (e.g., DUajw4YkorV)
> ### Return:
> - `data.items`: Post info list
>     - `id`: Post ID
>     - `code`: Post shortcode
>     - `media_type`: Media type (1=image, 2=video, 8=carousel)
>     - `like_count`: Likes count
>     - `comment_count`: Comments count
>     - `caption.text`: Post caption text
>     - `user`: Publisher info
>     - `image_versions2`: Image version list
>     - `video_versions`: Video version list (exists for videos)
>     - `carousel_media`: Carousel media list (exists for carousels)
>     - `taken_at`: Published timestamp
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> code = "DUajw4YkorV"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code | query | string | No | 帖子短代码/Post shortcode | None | DUajw4YkorV | None |
| url | query | string | No | 帖子URL（自动提取短代码）/Post URL (auto extract shortcode) | None | https://www.instagram.com/p/DUajw4YkorV/ | None |

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

<a id="get-api-u1-v1-instagram-v3-get-post-oembed"></a>
### `GET /api/u1/v1/instagram/v3/get_post_oembed`

- Summary: 获取帖子oEmbed内嵌信息/Get post oEmbed info
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_post_oembed_api_v1_instagram_v3_get_post_oembed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram帖子的oEmbed内嵌信息
> - 返回可直接嵌入网页的HTML代码和帖子元信息
> - 适用于需要在第三方网站嵌入Instagram帖子的场景
> ### 参数:
> - url: Instagram帖子的完整URL（如 `https://www.instagram.com/p/xxx/` 或 `https://www.instagram.com/reel/xxx/`）
> - hidecaption: 是否隐藏帖子文本（默认false）
> - maxwidth: 嵌入的最大宽度（像素，默认540）
> ### 返回:
> - `data.version`: oEmbed版本
> - `data.title`: 帖子标题
> - `data.author_name`: 作者名称
> - `data.author_url`: 作者主页URL
> - `data.author_id`: 作者ID
> - `data.media_id`: 媒体ID
> - `data.provider_name`: 提供者名称（Instagram）
> - `data.provider_url`: 提供者URL
> - `data.type`: 类型（rich）
> - `data.width`: 宽度
> - `data.html`: HTML嵌入代码
> - `data.thumbnail_url`: 缩略图URL
> - `data.thumbnail_width`: 缩略图宽度
> - `data.thumbnail_height`: 缩略图高度
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram post oEmbed embed info
> - Returns HTML code for embedding and post metadata
> - Suitable for embedding Instagram posts on third-party websites
> ### Parameters:
> - url: Full Instagram post URL (e.g., `https://www.instagram.com/p/xxx/` or `https://www.instagram.com/reel/xxx/`)
> - hidecaption: Whether to hide caption (default false)
> - maxwidth: Max embed width in pixels (default 540)
> ### Return:
> - `data.version`: oEmbed version
> - `data.title`: Post title
> - `data.author_name`: Author name
> - `data.author_url`: Author profile URL
> - `data.author_id`: Author ID
> - `data.media_id`: Media ID
> - `data.provider_name`: Provider name (Instagram)
> - `data.provider_url`: Provider URL
> - `data.type`: Type (rich)
> - `data.width`: Width
> - `data.html`: HTML embed code
> - `data.thumbnail_url`: Thumbnail URL
> - `data.thumbnail_width`: Thumbnail width
> - `data.thumbnail_height`: Thumbnail height
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> url = "https://www.instagram.com/reel/DUlObENDmJD"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | Instagram帖子的完整URL/Full URL of Instagram post | None | https://www.instagram.com/reel/DUlObENDmJD | None |
| hidecaption | query | boolean | No | 是否隐藏帖子文本/Whether to hide caption | false | None | None |
| maxwidth | query | integer | No | 最大宽度（像素）/Max width in pixels | 540 | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-recommended-reels"></a>
### `GET /api/u1/v1/instagram/v3/get_recommended_reels`

- Summary: 获取Reels推荐列表/Get recommended Reels feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram Reels推荐列表
> - 支持分页获取更多Reels
> ### 参数:
> - first: 每次获取的Reels数量（默认12）
> - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取
> ### 返回:
> - `data.edges`: Reels列表
>     - `node.media`: Reels媒体信息
>         - `code`: 帖子短代码
>         - `pk`: 帖子ID
>         - `like_count`: 点赞数
>         - `comment_count`: 评论数
>         - `play_count`: 播放数
>         - `caption.text`: 描述文本
>         - `user`: 发布者信息
>         - `video_versions`: 视频版本列表
>         - `image_versions2`: 封面图版本列表
> - `data.page_info`: 分页信息
>     - `has_next_page`: 是否有下一页
>     - `end_cursor`: 下一页游标（传给下次请求的after参数）
> ### 分页使用方法:
> 1. 首次请求：只传 `first` 参数
> 2. 获取响应中的 `data.page_info.end_cursor`
> 3. 下次请求：传入 `first` 和 `after` (使用上次的end_cursor)
> 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram Reels recommendation feed
> - Support pagination to fetch more Reels
> ### Parameters:
> - first: Number of Reels to fetch per request (default 12)
> - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`
> ### Return:
> - `data.edges`: Reels list
>     - `node.media`: Reels media info
>         - `code`: Post shortcode
>         - `pk`: Post ID
>         - `like_count`: Likes count
>         - `comment_count`: Comments count
>         - `play_count`: Play count
>         - `caption.text`: Description text
>         - `user`: Publisher info
>         - `video_versions`: Video version list
>         - `image_versions2`: Cover image version list
> - `data.page_info`: Pagination info
>     - `has_next_page`: Whether has next page
>     - `end_cursor`: Next page cursor (use as after parameter in next request)
> ### Pagination usage:
> 1. First request: Only pass `first` parameter
> 2. Get `data.page_info.end_cursor` from response
> 3. Next request: Pass `first` and `after` (use end_cursor from previous)
> 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> first = 12

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| first | query | integer | No | 获取数量/Number of reels to fetch | 12 | 12 | None |
| after | query | string | No | 分页游标，首次请求不传，从上一次响应的 page_info.end_cursor 获取/Pagination cursor, omit for first request, get from previous response page_info.end_cursor | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-about"></a>
### `GET /api/u1/v1/instagram/v3/get_user_about`

- Summary: 获取用户账户简介/Get user about info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_about_api_v1_instagram_v3_get_user_about_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的账户简介信息（About This Account）
> - 包含账户创建日期、所在地区、曾用名等信息
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> ### 返回:
> - 账户创建日期
> - 账户所在地区/国家
> - 曾用名历史
> - 其他账户相关信息
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's About This Account information
> - Including account creation date, location, former usernames, etc.
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Return:
> - Account creation date
> - Account location/country
> - Former username history
> - Other account related info
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "791258468"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 791258468 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-brief"></a>
### `GET /api/u1/v1/instagram/v3/get_user_brief`

- Summary: 获取用户短详情/Get user brief info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_brief_api_v1_instagram_v3_get_user_brief_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的短详情/悬浮卡片信息
> - 返回用户核心信息，响应速度比 get_user_profile 更快
> - 适用于批量获取用户摘要信息的场景
> ### 参数:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> ### 返回:
> - `data.id`: 用户ID
> - `data.username`: 用户名
> - `data.full_name`: 全名
> - `data.biography`: 个人简介
> - `data.profile_pic_url`: 头像URL
> - `data.is_verified`: 是否认证
> - `data.is_private`: 是否私密账号
> - `data.edge_followed_by.count`: 粉丝数
> - `data.edge_follow.count`: 关注数
> - `data.edge_owner_to_timeline_media`: 最近帖子预览
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user brief/hover card info
> - Returns core user info, faster response than get_user_profile
> - Suitable for batch fetching user summary info
> ### Parameters:
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Return:
> - `data.id`: User ID
> - `data.username`: Username
> - `data.full_name`: Full name
> - `data.biography`: Biography
> - `data.profile_pic_url`: Profile picture URL
> - `data.is_verified`: Whether verified
> - `data.is_private`: Whether private account
> - `data.edge_followed_by.count`: Followers count
> - `data.edge_follow.count`: Following count
> - `data.edge_owner_to_timeline_media`: Recent posts preview
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "77919494141"
> username = "emo.__0202"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 77919494141 | None |
| username | query | string | Yes | 用户名/Username | None | emo.__0202 | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-followers"></a>
### `GET /api/u1/v1/instagram/v3/get_user_followers`

- Summary: 获取用户粉丝列表/Get user followers list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_followers_api_v1_instagram_v3_get_user_followers_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的粉丝列表
> - 返回关注该用户的所有账号信息
> - 支持分页获取
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - count: 每次获取数量（默认12）
> - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取
> ### 返回:
> - `data.users`: 粉丝用户列表
>     - `pk`: 用户ID
>     - `username`: 用户名
>     - `full_name`: 全名
>     - `is_private`: 是否私密账号
>     - `is_verified`: 是否认证
>     - `profile_pic_url`: 头像URL
> - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数）
> - `data.big_list`: 是否有更多数据
> - `data.page_size`: 每页数量
> - `data.status`: 状态
> ### 分页使用方法:
> 1. 首次请求：只传 `user_id` 和 `count` 参数
> 2. 获取响应中的 `data.next_max_id`
> 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id)
> 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's followers list
> - Returns all accounts that follow this user
> - Support pagination
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - count: Number of users to fetch per request (default 12)
> - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id`
> ### Return:
> - `data.users`: Followers user list
>     - `pk`: User ID
>     - `username`: Username
>     - `full_name`: Full name
>     - `is_private`: Whether private account
>     - `is_verified`: Whether verified
>     - `profile_pic_url`: Profile picture URL
> - `data.next_max_id`: Next page cursor (use as max_id in next request)
> - `data.big_list`: Whether has more data
> - `data.page_size`: Page size
> - `data.status`: Status
> ### Pagination usage:
> 1. First request: Only pass `user_id` and `count` parameters
> 2. Get `data.next_max_id` from response
> 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous)
> 4. Repeat steps 2-3 until response has no `next_max_id` field
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"
> count = 12

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| count | query | integer | No | 每次获取数量/Number of users to fetch per request | 12 | 12 | None |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-following"></a>
### `GET /api/u1/v1/instagram/v3/get_user_following`

- Summary: 获取用户关注列表/Get user following list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_following_api_v1_instagram_v3_get_user_following_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的关注列表
> - 返回用户关注的所有账号信息
> - 支持分页获取
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - count: 每次获取数量（默认12）
> - max_id: 分页游标，首次请求不传，从上一次响应的 `data.next_max_id` 获取
> ### 返回:
> - `data.users`: 关注用户列表
>     - `pk`: 用户ID
>     - `username`: 用户名
>     - `full_name`: 全名
>     - `is_private`: 是否私密账号
>     - `is_verified`: 是否认证
>     - `profile_pic_url`: 头像URL
> - `data.next_max_id`: 下一页分页游标（传给下次请求的max_id参数）
> - `data.big_list`: 是否有更多数据
> - `data.page_size`: 每页数量
> - `data.status`: 状态
> ### 分页使用方法:
> 1. 首次请求：只传 `user_id` 和 `count` 参数
> 2. 获取响应中的 `data.next_max_id`
> 3. 下次请求：传入 `user_id`、`count` 和 `max_id` (使用上次的next_max_id)
> 4. 重复步骤 2-3 直到响应中没有 `next_max_id` 字段
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's following list
> - Returns all accounts the user follows
> - Support pagination
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - count: Number of users to fetch per request (default 12)
> - max_id: Pagination cursor, omit for first request, get from previous response `data.next_max_id`
> ### Return:
> - `data.users`: Following user list
>     - `pk`: User ID
>     - `username`: Username
>     - `full_name`: Full name
>     - `is_private`: Whether private account
>     - `is_verified`: Whether verified
>     - `profile_pic_url`: Profile picture URL
> - `data.next_max_id`: Next page cursor (use as max_id in next request)
> - `data.big_list`: Whether has more data
> - `data.page_size`: Page size
> - `data.status`: Status
> ### Pagination usage:
> 1. First request: Only pass `user_id` and `count` parameters
> 2. Get `data.next_max_id` from response
> 3. Next request: Pass `user_id`, `count`, and `max_id` (use next_max_id from previous)
> 4. Repeat steps 2-3 until response has no `next_max_id` field
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"
> count = 12

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| count | query | integer | No | 每次获取数量/Number of users to fetch per request | 12 | 12 | None |
| max_id | query | string | No | 分页游标，首次请求不传，从上一次响应的 next_max_id 获取/Pagination cursor, omit for first request, get from previous response next_max_id | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-highlights"></a>
### `GET /api/u1/v1/instagram/v3/get_user_highlights`

- Summary: 获取用户精选Highlights列表/Get user highlights
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_highlights_api_v1_instagram_v3_get_user_highlights_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的精选Highlights列表
> - 返回用户创建的所有精选集合
> - 支持分页获取
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - first: 每次获取的精选数量（默认10）
> - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取
> ### 返回:
> - `data.edges`: 精选列表
>     - `node.id`: 精选ID（格式: highlight:xxx）
>     - `node.title`: 精选标题
>     - `node.cover_media`: 封面媒体信息
>     - `node.cover_media_cropped_thumbnail`: 裁剪后的封面缩略图
>     - `node.media_count`: 精选中的故事数量
> - `data.page_info`: 分页信息
>     - `has_next_page`: 是否有下一页
>     - `end_cursor`: 下一页游标（传给下次请求的after参数）
> ### 分页使用方法:
> 1. 首次请求：只传 `user_id` 和 `first` 参数
> 2. 获取响应中的 `data.page_info.end_cursor`
> 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor)
> 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's Highlights list
> - Returns all highlight collections created by the user
> - Support pagination
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - first: Number of highlights to fetch per request (default 10)
> - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`
> ### Return:
> - `data.edges`: Highlights list
>     - `node.id`: Highlight ID (format: highlight:xxx)
>     - `node.title`: Highlight title
>     - `node.cover_media`: Cover media info
>     - `node.cover_media_cropped_thumbnail`: Cropped cover thumbnail
>     - `node.media_count`: Number of stories in highlight
> - `data.page_info`: Pagination info
>     - `has_next_page`: Whether has next page
>     - `end_cursor`: Next page cursor (use as after parameter in next request)
> ### Pagination usage:
> 1. First request: Only pass `user_id` and `first` parameters
> 2. Get `data.page_info.end_cursor` from response
> 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous)
> 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"
> first = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| first | query | integer | No | 获取数量/Number of highlights to fetch | 10 | 10 | None |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-posts"></a>
### `GET /api/u1/v1/instagram/v3/get_user_posts`

- Summary: 获取用户帖子列表/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posts_api_v1_instagram_v3_get_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的帖子列表
> - 支持分页获取，可获取用户的所有帖子
> ### 参数（二选一）:
> - username: Instagram用户名
> - user_id: Instagram用户ID（数字，内部会自动转换为用户名）
> - first: 每次获取的帖子数量（默认12）
> - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取
> ### 返回:
> - `data.edges`: 帖子列表
>     - `node.id`: 帖子ID
>     - `node.code`: 帖子短代码
>     - `node.display_url`: 展示图片URL
>     - `node.taken_at`: 发布时间戳
>     - `node.like_count`: 点赞数
>     - `node.comment_count`: 评论数
>     - `node.caption.text`: 帖子文本
> - `data.page_info`: 分页信息
>     - `has_next_page`: 是否有下一页
>     - `end_cursor`: 下一页游标（传给下次请求的after参数）
> ### 分页使用方法:
> 1. 首次请求：只传 `username` 和 `first` 参数
> 2. 获取响应中的 `data.page_info.end_cursor`
> 3. 下次请求：传入 `username`、`first` 和 `after` (使用上次的end_cursor)
> 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's post list
> - Support pagination to fetch all user posts
> ### Parameters (one of):
> - username: Instagram username
> - user_id: Instagram user ID (numeric, will be auto-converted to username)
> ### Other parameters:
> - first: Number of posts to fetch per request (default 12)
> - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`
> ### Return:
> - `data.edges`: Post list
>     - `node.id`: Post ID
>     - `node.code`: Post shortcode
>     - `node.display_url`: Display image URL
>     - `node.taken_at`: Published timestamp
>     - `node.like_count`: Likes count
>     - `node.comment_count`: Comments count
>     - `node.caption.text`: Post caption text
> - `data.page_info`: Pagination info
>     - `has_next_page`: Whether has next page
>     - `end_cursor`: Next page cursor (use as after parameter in next request)
> ### Pagination usage:
> 1. First request: Only pass `username` and `first` parameters
> 2. Get `data.page_info.end_cursor` from response
> 3. Next request: Pass `username`, `first`, and `after` (use end_cursor from previous)
> 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> # 第一页 / First page
> username = "liensue.talks"
> first = 12
>
> # 第二页 / Second page
> # username = "liensue.talks"
> # first = 12
> # after = "QVFCcmN1YlF..."  # 从第一页响应中获取 / Get from first page response
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| first | query | integer | No | 获取帖子数量/Number of posts to fetch | 12 | 12 | None |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-profile"></a>
### `GET /api/u1/v1/instagram/v3/get_user_profile`

- Summary: 获取用户信息/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_api_v1_instagram_v3_get_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的完整个人资料信息
> - 包含用户基本信息、统计数据、最近帖子等
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> ### 返回:
> - `data.user.id`: 用户ID
> - `data.user.username`: 用户名
> - `data.user.full_name`: 全名
> - `data.user.biography`: 个人简介
> - `data.user.external_url`: 外部链接
> - `data.user.profile_pic_url`: 头像URL（标准）
> - `data.user.profile_pic_url_hd`: 头像URL（高清）
> - `data.user.is_verified`: 是否认证
> - `data.user.is_private`: 是否私密账号
> - `data.user.edge_followed_by.count`: 粉丝数
> - `data.user.edge_follow.count`: 关注数
> - `data.user.edge_owner_to_timeline_media.count`: 帖子总数
> - `data.user.edge_felix_video_timeline.count`: Reels/视频数
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get complete Instagram user profile information
> - Including basic info, statistics, recent posts, etc.
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Return:
> - `data.user.id`: User ID
> - `data.user.username`: Username
> - `data.user.full_name`: Full name
> - `data.user.biography`: Biography
> - `data.user.external_url`: External URL
> - `data.user.profile_pic_url`: Profile picture URL (standard)
> - `data.user.profile_pic_url_hd`: Profile picture URL (HD)
> - `data.user.is_verified`: Whether verified
> - `data.user.is_private`: Whether private account
> - `data.user.edge_followed_by.count`: Followers count
> - `data.user.edge_follow.count`: Following count
> - `data.user.edge_owner_to_timeline_media.count`: Total posts count
> - `data.user.edge_felix_video_timeline.count`: Reels/videos count
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-reels"></a>
### `GET /api/u1/v1/instagram/v3/get_user_reels`

- Summary: 获取用户Reels列表/Get user reels
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_reels_api_v1_instagram_v3_get_user_reels_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的Reels列表
> - 支持分页获取用户发布的所有Reels
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - first: 每次获取的Reels数量（默认12）
> - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取
> ### 返回:
> - `data.edges`: Reels列表
>     - `node.media`: Reels媒体信息
>         - `code`: 帖子短代码
>         - `pk`: 帖子ID
>         - `like_count`: 点赞数
>         - `comment_count`: 评论数
>         - `play_count`: 播放数
>         - `caption.text`: 描述文本
>         - `user`: 发布者信息
>         - `video_versions`: 视频版本列表
>         - `image_versions2`: 封面图版本列表
> - `data.page_info`: 分页信息
>     - `has_next_page`: 是否有下一页
>     - `end_cursor`: 下一页游标（传给下次请求的after参数）
> ### 分页使用方法:
> 1. 首次请求：只传 `user_id` 和 `first` 参数
> 2. 获取响应中的 `data.page_info.end_cursor`
> 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor)
> 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's Reels list
> - Support pagination to fetch all user's Reels
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - first: Number of Reels to fetch per request (default 12)
> - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`
> ### Return:
> - `data.edges`: Reels list
>     - `node.media`: Reels media info
>         - `code`: Post shortcode
>         - `pk`: Post ID
>         - `like_count`: Likes count
>         - `comment_count`: Comments count
>         - `play_count`: Play count
>         - `caption.text`: Description text
>         - `user`: Publisher info
>         - `video_versions`: Video version list
>         - `image_versions2`: Cover image version list
> - `data.page_info`: Pagination info
>     - `has_next_page`: Whether has next page
>     - `end_cursor`: Next page cursor (use as after parameter in next request)
> ### Pagination usage:
> 1. First request: Only pass `user_id` and `first` parameters
> 2. Get `data.page_info.end_cursor` from response
> 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous)
> 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"
> first = 12

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| first | query | integer | No | 获取数量/Number of reels to fetch | 12 | 12 | None |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-stories"></a>
### `GET /api/u1/v1/instagram/v3/get_user_stories`

- Summary: 获取用户Stories（快拍）/Get user stories
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_stories_api_v1_instagram_v3_get_user_stories_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的Stories（快拍）列表
> - 即点击用户头像后展示的24小时内发布的快拍内容
> - 支持同时获取多个用户的Stories
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - reel_ids: 用户ID列表，逗号分隔（可选，如不提供则仅查询user_id指定的用户）
>     - 例如: `58208242181,791258468`
>     - 可同时查询多个用户的Stories
> ### 返回:
> - `data.reels_media`: Stories列表（按用户分组）
>     - `id`: 用户ID
>     - `user`: 用户信息
>         - `username`: 用户名
>         - `full_name`: 全名
>         - `profile_pic_url`: 头像URL
>     - `items`: Stories条目列表
>         - `id`: Story ID
>         - `pk`: Story PK
>         - `taken_at`: 发布时间戳
>         - `media_type`: 媒体类型（1=图片, 2=视频）
>         - `image_versions2`: 图片版本列表
>         - `video_versions`: 视频版本列表（视频时存在）
>         - `story_cta`: Story链接（如果有）
> - `data.reels`: Stories详细信息
> ### 注意:
> - Stories有24小时有效期，过期后无法获取
> - 私密账号的Stories需要关注后才能查看
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's Stories list
> - Stories displayed when clicking on user's profile picture (published within 24 hours)
> - Support fetching multiple users' Stories at once
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - reel_ids: User ID list, comma separated (optional, if not provided only queries the user_id)
>     - Example: `58208242181,791258468`
>     - Can query multiple users' Stories at once
> ### Return:
> - `data.reels_media`: Stories list (grouped by user)
>     - `id`: User ID
>     - `user`: User info
>         - `username`: Username
>         - `full_name`: Full name
>         - `profile_pic_url`: Profile picture URL
>     - `items`: Stories item list
>         - `id`: Story ID
>         - `pk`: Story PK
>         - `taken_at`: Published timestamp
>         - `media_type`: Media type (1=image, 2=video)
>         - `image_versions2`: Image version list
>         - `video_versions`: Video version list (exists for videos)
>         - `story_cta`: Story link (if any)
> - `data.reels`: Stories detailed info
> ### Note:
> - Stories have a 24-hour expiration, cannot be fetched after expiration
> - Private account's Stories require following to view
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> ```
> user_id = "58208242181"
> # reel_ids = "58208242181,791258468"
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| reel_ids | query | string | No | 用户ID列表，逗号分隔，可同时获取多个用户的Stories（如不提供则仅查询user_id）/User ID list, comma separated, fetch multiple users' stories at once (if not provided, only queries user_id) | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-get-user-tagged-posts"></a>
### `GET /api/u1/v1/instagram/v3/get_user_tagged_posts`

- Summary: 获取用户被标记的帖子/Get user tagged posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户被标记（tagged）的帖子列表
> - 即其他用户在帖子中标记了该用户的内容
> - 支持分页获取
> ### 参数（二选一）:
> - user_id: Instagram用户ID（数字）
> - username: Instagram用户名
> - first: 每次获取的帖子数量（默认12）
> - after: 分页游标，首次请求不传，从上一次响应的 `data.page_info.end_cursor` 获取
> ### 返回:
> - `data.edges`: 帖子列表
>     - `node.id`: 帖子ID
>     - `node.code`: 帖子短代码
>     - `node.display_url`: 展示图片URL
>     - `node.taken_at`: 发布时间戳
>     - `node.like_count`: 点赞数
>     - `node.comment_count`: 评论数
>     - `node.caption.text`: 帖子文本
>     - `node.user`: 发帖者信息
> - `data.page_info`: 分页信息
>     - `has_next_page`: 是否有下一页
>     - `end_cursor`: 下一页游标（传给下次请求的after参数）
> ### 分页使用方法:
> 1. 首次请求：只传 `user_id` 和 `first` 参数
> 2. 获取响应中的 `data.page_info.end_cursor`
> 3. 下次请求：传入 `user_id`、`first` 和 `after` (使用上次的end_cursor)
> 4. 重复步骤 2-3 直到 `data.page_info.has_next_page` 为 false
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's tagged posts list
> - Posts where other users tagged this user
> - Support pagination
> ### Parameters (one of):
> - user_id: Instagram user ID (numeric)
> - username: Instagram username
> ### Other parameters:
> - first: Number of posts to fetch per request (default 12)
> - after: Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`
> ### Return:
> - `data.edges`: Post list
>     - `node.id`: Post ID
>     - `node.code`: Post shortcode
>     - `node.display_url`: Display image URL
>     - `node.taken_at`: Published timestamp
>     - `node.like_count`: Likes count
>     - `node.comment_count`: Comments count
>     - `node.caption.text`: Post caption text
>     - `node.user`: Post author info
> - `data.page_info`: Pagination info
>     - `has_next_page`: Whether has next page
>     - `end_cursor`: Next page cursor (use as after parameter in next request)
> ### Pagination usage:
> 1. First request: Only pass `user_id`/`username` and `first` parameters
> 2. Get `data.page_info.end_cursor` from response
> 3. Next request: Pass `user_id`, `first`, and `after` (use end_cursor from previous)
> 4. Repeat steps 2-3 until `data.page_info.has_next_page` is false
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> user_id = "58208242181"
> first = 12

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 58208242181 | None |
| username | query | string | No | 用户名/Username | None | liensue.talks | None |
| first | query | integer | No | 获取帖子数量/Number of posts to fetch | 12 | 12 | None |
| after | query | string | No | 分页游标（从上次响应的page_info.end_cursor获取）/Pagination cursor (from previous response page_info.end_cursor) | None | None | None |

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

<a id="get-api-u1-v1-instagram-v3-search-hashtags"></a>
### `GET /api/u1/v1/instagram/v3/search_hashtags`

- Summary: 搜索话题标签/Search hashtags
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_hashtags_api_v1_instagram_v3_search_hashtags_get`

#### Notes

> # [中文]
> ### 用途:
> - Instagram话题标签搜索接口
> - 仅返回话题标签搜索结果
> ### 参数:
> - query: 搜索关键词
> ### 返回:
> - `data.hashtags`: 话题标签搜索结果列表
> - `data.rank_token`: 排序token
> - `data.see_more`: 更多信息
> - `data.inform_module`: 提示模块
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Instagram hashtag search API
> - Returns only hashtag search results
> ### Parameters:
> - query: Search keyword
> ### Return:
> - `data.hashtags`: Hashtag search results
> - `data.rank_token`: Rank token
> - `data.see_more`: See more info
> - `data.inform_module`: Inform module
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> query = "fashion"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | fashion | None |

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

<a id="get-api-u1-v1-instagram-v3-search-places"></a>
### `GET /api/u1/v1/instagram/v3/search_places`

- Summary: 搜索地点/Search places
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_places_api_v1_instagram_v3_search_places_get`

#### Notes

> # [中文]
> ### 用途:
> - Instagram地点搜索接口
> - 仅返回地点搜索结果
> ### 参数:
> - query: 搜索关键词
> ### 返回:
> - `data.places`: 地点搜索结果列表
> - `data.rank_token`: 排序token
> - `data.see_more`: 更多信息
> - `data.inform_module`: 提示模块
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Instagram place search API
> - Returns only place search results
> ### Parameters:
> - query: Search keyword
> ### Return:
> - `data.places`: Place search results
> - `data.rank_token`: Rank token
> - `data.see_more`: See more info
> - `data.inform_module`: Inform module
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> query = "tokyo"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | tokyo | None |

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

<a id="get-api-u1-v1-instagram-v3-search-users"></a>
### `GET /api/u1/v1/instagram/v3/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_instagram_v3_search_users_get`

#### Notes

> # [中文]
> ### 用途:
> - Instagram用户搜索接口
> - 仅返回用户搜索结果
> ### 参数:
> - query: 搜索关键词
> ### 返回:
> - `data.users`: 用户搜索结果列表
> - `data.rank_token`: 排序token
> - `data.see_more`: 更多信息
> - `data.inform_module`: 提示模块
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Instagram user search API
> - Returns only user search results
> ### Parameters:
> - query: Search keyword
> ### Return:
> - `data.users`: User search results
> - `data.rank_token`: Rank token
> - `data.see_more`: See more info
> - `data.inform_module`: Inform module
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> query = "justin"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | justin | None |

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

<a id="get-api-u1-v1-instagram-v3-translate-comment"></a>
### `GET /api/u1/v1/instagram/v3/translate_comment`

- Summary: 翻译评论/帖子文本/Translate comment or caption
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `translate_comment_api_v1_instagram_v3_translate_comment_get`

#### Notes

> # [中文]
> ### 用途:
> - 翻译Instagram帖子文本（caption）
> - 内部强制 is_caption=True，专门用于翻译帖子的文字说明
> ### 参数:
> - comment_id: 帖子媒体ID
> ### 返回:
> - `data.translation`: 翻译后的文本
> - `data.source_language`: 原文语言
> ### 注意:
> - 翻译目标语言取决于请求所使用的 Cookie 对应账号的语言设置（通常为英语）
> - 无法指定翻译目标语言，由 Instagram 服务端根据账号设置自动决定
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Translate Instagram post caption
> - Internally forces is_caption=True, specifically for translating post captions
> ### Parameters:
> - comment_id: Post media ID
> ### Return:
> - `data.translation`: Translated text
> - `data.source_language`: Source language
> ### Note:
> - The target translation language depends on the language setting of the account associated with the cookie used (usually English)
> - Cannot specify the target language, it is automatically determined by Instagram based on the account settings
> ### Price:
> - 0.002 USD/request
>
> ### 示例/Example
> comment_id = "18191961100350646"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| comment_id | query | string | Yes | 帖子媒体ID/Post media ID | None | 18191961100350646 | None |

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
