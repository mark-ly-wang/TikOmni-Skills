# Threads-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/threads-web-api.md`](../api-tags/threads-web-api.md)
- Current contract file: `api-contracts/threads-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `11`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Threads Web数据接口/Threads-Web-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-threads-web-fetch-post-comments"></a>
### `GET /api/u1/v1/threads/web/fetch_post_comments`

- Summary: 获取帖子评论/Get post comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_threads_web_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads帖子评论列表
> - 价格：0.002$ / 次
> ### 参数:
> - post_id: 帖子ID，例如：3390920896561588969
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 帖子评论列表数据，包含:
>     - comments: 评论列表
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Get Threads post comments list
> - Price: 0.002$ / time
> ### Parameters:
> - post_id: Post ID, for example: 3390920896561588969
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - Post comments list data, including:
>     - comments: Comment list
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>
> # [示例/Example]
> post_id = "3390920896561588969"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID | None | 3390920896561588969 | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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

<a id="get-api-u1-v1-threads-web-fetch-post-detail"></a>
### `GET /api/u1/v1/threads/web/fetch_post_detail`

- Summary: 获取帖子详情/Get post detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_api_v1_threads_web_fetch_post_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads帖子详情
> - 价格：0.002$ / 次
> ### 参数:
> - post_id: 帖子ID（纯数字），例如：3349029093483693129，可以从其他接口获取，如果是使用URL获取，去调用 /fetch_post_detail_v2 接口。
> ### 返回:
> - 帖子详情数据，包含:
>     - id: 帖子ID
>     - text: 帖子文本内容
>     - user: 发布者信息
>     - image_versions2: 图片信息
>     - video_versions: 视频信息
>     - like_count: 点赞数
>     - text_post_app_info: 帖子应用信息
>     - 等等...
>
> # [English]
> ### Purpose:
> - Get Threads post detail
> - Price: 0.002$ / time
> ### Parameters:
> - post_id: Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API.
> ### Return:
> - Post detail data, including:
>     - id: Post ID
>     - text: Post text content
>     - user: Publisher information
>     - image_versions2: Image information
>     - video_versions: Video information
>     - like_count: Like count
>     - text_post_app_info: Post app information
>     - etc...
>
> # [示例/Example]
> post_id = "3349029093483693129"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID | None | 3349029093483693129 | None |

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

<a id="get-api-u1-v1-threads-web-fetch-post-detail-v2"></a>
### `GET /api/u1/v1/threads/web/fetch_post_detail_v2`

- Summary: 获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads帖子详情（支持短代码和完整URL）
> - 价格：0.002$ / 次
> ### 参数:
> - post_id: 帖子短代码（可选），例如：DPVUglOjOUu，可以从帖子URL中提取，例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu 中的 DPVUglOjOUu
> - url: 完整的帖子URL（可选），例如：https://www.threads.com/@taylorswift/post/DPVUglOjOUu
> - 注意：post_id 和 url 至少提供一个参数
> ### 返回:
> - 帖子详情数据，包含:
>     - post_id: 帖子ID
>     - text: 帖子文本内容
>     - user: 发布者信息
>     - media: 媒体信息（图片、视频）
>     - like_count: 点赞数
>     - reply_count: 回复数
>     - repost_count: 转发数
>     - timestamp: 发布时间
>     - 等等...
>
> # [English]
> ### Purpose:
> - Get Threads post detail (supports short code and full URL)
> - Price: 0.002$ / time
> ### Parameters:
> - post_id: Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu
> - url: Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu
> - Note: At least one of post_id or url must be provided
> ### Return:
> - Post detail data, including:
>     - post_id: Post ID
>     - text: Post text content
>     - user: Publisher information
>     - media: Media information (images, videos)
>     - like_count: Like count
>     - reply_count: Reply count
>     - repost_count: Repost count
>     - timestamp: Publish timestamp
>     - etc...
>
> # [示例/Example]
> post_id = "DPVUglOjOUu"
> # or
> url = "https://www.threads.com/@taylorswift/post/DPVUglOjOUu"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | No | 帖子短代码/Post short code | None | DPVUglOjOUu | None |
| url | query | string | No | 完整帖子URL/Full post URL | None | https://www.threads.com/@taylorswift/post/DPVUglOjOUu | None |

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

<a id="get-api-u1-v1-threads-web-fetch-user-info"></a>
### `GET /api/u1/v1/threads/web/fetch_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_threads_web_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads用户信息
> - 价格：0.002$ / 次
> ### 参数:
> - username: 用户名，例如：lilbieber，可以从用户主页链接中获取，例如：https://www.threads.net/@lilbieber 中的 lilbieber。
> ### 返回:
> - 用户信息数据，包含:
>     - pk: 用户ID
>     - username: 用户名
>     - full_name: 全名
>     - biography: 个人简介
>     - profile_pic_url: 头像URL
>     - follower_count: 粉丝数
>     - is_verified: 是否认证
>     - 等等...
>
> # [English]
> ### Purpose:
> - Get Threads user information
> - Price: 0.002$ / time
> ### Parameters:
> - username: Username, for example: lilbieber, can be obtained from the user's homepage link, for example: lilbieber in https://www.threads.net/@lilbieber
> ### Return:
> - User information data, including:
>     - pk: User ID
>     - username: Username
>     - full_name: Full name
>     - biography: Biography
>     - profile_pic_url: Profile picture URL
>     - follower_count: Follower count
>     - is_verified: Is verified
>     - etc...
>
> # [示例/Example]
> username = "lilbieber"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | lilbieber | None |

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

<a id="get-api-u1-v1-threads-web-fetch-user-info-by-id"></a>
### `GET /api/u1/v1/threads/web/fetch_user_info_by_id`

- Summary: 根据用户ID获取用户信息/Get user info by ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据用户ID获取Threads用户信息
> - 价格：0.002$ / 次
> ### 参数:
> - user_id: 用户ID，例如：67027868801，可以从用户主页API或帖子数据中获取。
> ### 返回:
> - 用户信息数据，包含:
>     - pk: 用户ID
>     - username: 用户名
>     - full_name: 全名
>     - biography: 个人简介
>     - profile_pic_url: 头像URL
>     - follower_count: 粉丝数
>     - is_verified: 是否认证
>     - 等等...
>
> # [English]
> ### Purpose:
> - Get Threads user information by user ID
> - Price: 0.002$ / time
> ### Parameters:
> - user_id: User ID, for example: 67027868801, can be obtained from user profile API or post data
> ### Return:
> - User information data, including:
>     - pk: User ID
>     - username: Username
>     - full_name: Full name
>     - biography: Biography
>     - profile_pic_url: Profile picture URL
>     - follower_count: Follower count
>     - is_verified: Is verified
>     - etc...
>
> # [示例/Example]
> user_id = "67027868801"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 67027868801 | None |

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

<a id="get-api-u1-v1-threads-web-fetch-user-posts"></a>
### `GET /api/u1/v1/threads/web/fetch_user_posts`

- Summary: 获取用户帖子列表/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_threads_web_fetch_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads用户的帖子列表
> - 价格：0.002$ / 次
> ### 参数:
> - user_id: 用户ID，例如：63625256886，可以从用户主页API获取。
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 用户帖子列表数据，包含:
>     - threads: 帖子列表数组
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>     - 每个帖子包含:
>         - id: 帖子ID
>         - text: 帖子文本内容
>         - user: 发布者信息
>         - image_versions2: 图片信息
>         - video_versions: 视频信息
>         - like_count: 点赞数
>         - text_post_app_info: 帖子应用信息
>         - 等等...
>
> # [English]
> ### Purpose:
> - Get Threads user's post list
> - Price: 0.002$ / time
> ### Parameters:
> - user_id: User ID, for example: 63625256886, can be obtained from user profile API
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - User post list data, including:
>     - threads: Post list array
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>     - Each post contains:
>         - id: Post ID
>         - text: Post text content
>         - user: Publisher information
>         - image_versions2: Image information
>         - video_versions: Video information
>         - like_count: Like count
>         - text_post_app_info: Post app information
>         - etc...
>
> # [示例/Example]
> user_id = "63625256886"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 63625256886 | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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

<a id="get-api-u1-v1-threads-web-fetch-user-replies"></a>
### `GET /api/u1/v1/threads/web/fetch_user_replies`

- Summary: 获取用户回复列表/Get user replies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_replies_api_v1_threads_web_fetch_user_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads用户的回复列表
> - 价格：0.002$ / 次
> ### 参数:
> - user_id: 用户ID，例如：63625256886
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 用户回复列表数据，包含:
>     - threads: 回复列表
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Get Threads user's reply list
> - Price: 0.002$ / time
> ### Parameters:
> - user_id: User ID, for example: 63625256886
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - User reply list data, including:
>     - threads: Reply list
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>
> # [示例/Example]
> user_id = "63625256886"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 63625256886 | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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

<a id="get-api-u1-v1-threads-web-fetch-user-reposts"></a>
### `GET /api/u1/v1/threads/web/fetch_user_reposts`

- Summary: 获取用户转发列表/Get user reposts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Threads用户的转发列表
> - 价格：0.002$ / 次
> ### 参数:
> - user_id: 用户ID，例如：63625256886
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 用户转发列表数据，包含:
>     - threads: 转发列表
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Get Threads user's repost list
> - Price: 0.002$ / time
> ### Parameters:
> - user_id: User ID, for example: 63625256886
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - User repost list data, including:
>     - threads: Repost list
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>
> # [示例/Example]
> user_id = "63625256886"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 63625256886 | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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

<a id="get-api-u1-v1-threads-web-search-profiles"></a>
### `GET /api/u1/v1/threads/web/search_profiles`

- Summary: 搜索用户档案/Search profiles
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_profiles_api_v1_threads_web_search_profiles_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索Threads用户档案
> - 价格：0.002$ / 次
> ### 参数:
> - query: 搜索关键词，例如：mark
> ### 返回:
> - 搜索结果数据，包含:
>     - users: 用户列表
>     - 每个用户包含:
>         - pk: 用户ID
>         - username: 用户名
>         - full_name: 全名
>         - profile_pic_url: 头像URL
>         - is_verified: 是否认证
>         - follower_count: 粉丝数
>         - 等等...
>
> # [English]
> ### Purpose:
> - Search Threads user profiles
> - Price: 0.002$ / time
> ### Parameters:
> - query: Search query, for example: mark
> ### Return:
> - Search result data, including:
>     - users: User list
>     - Each user contains:
>         - pk: User ID
>         - username: Username
>         - full_name: Full name
>         - profile_pic_url: Profile picture URL
>         - is_verified: Is verified
>         - follower_count: Follower count
>         - etc...
>
> # [示例/Example]
> query = "mark"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query | None | mark | None |

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

<a id="get-api-u1-v1-threads-web-search-recent"></a>
### `GET /api/u1/v1/threads/web/search_recent`

- Summary: 搜索最新内容/Search recent content
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_recent_api_v1_threads_web_search_recent_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索Threads最新内容
> - 价格：0.002$ / 次
> ### 参数:
> - query: 搜索关键词，例如：bitcoin
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 搜索结果数据，包含:
>     - threads: 帖子列表
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Search Threads recent content
> - Price: 0.002$ / time
> ### Parameters:
> - query: Search query, for example: bitcoin
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - Search result data, including:
>     - threads: Post list
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>
> # [示例/Example]
> query = "bitcoin"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query | None | bitcoin | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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

<a id="get-api-u1-v1-threads-web-search-top"></a>
### `GET /api/u1/v1/threads/web/search_top`

- Summary: 搜索热门内容/Search top content
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_top_api_v1_threads_web_search_top_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索Threads热门内容
> - 价格：0.002$ / 次
> ### 参数:
> - query: 搜索关键词，例如：bitcoin
> - end_cursor: 分页游标（可选），用于获取下一页数据
> ### 返回:
> - 搜索结果数据，包含:
>     - threads: 帖子列表
>     - next_cursor: 下一页游标
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Search Threads top content
> - Price: 0.002$ / time
> ### Parameters:
> - query: Search query, for example: bitcoin
> - end_cursor: Pagination cursor (optional), used to get next page data
> ### Return:
> - Search result data, including:
>     - threads: Post list
>     - next_cursor: Next page cursor
>     - has_more: Has more data
>
> # [示例/Example]
> query = "bitcoin"
> end_cursor = None  # or a cursor string from previous response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query | None | bitcoin | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor (optional) | None | None | None |

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
