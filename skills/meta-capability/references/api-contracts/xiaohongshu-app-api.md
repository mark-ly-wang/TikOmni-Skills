# Xiaohongshu-App-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/xiaohongshu-app-api.md`](../api-tags/xiaohongshu-app-api.md)
- 当前契约文件：`api-contracts/xiaohongshu-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`12`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(小红书App数据接口/Xiaohongshu-App-API data endpoints)** - 第二优先/Second choice

## 路由契约

<a id="get-api-u1-v1-xiaohongshu-app-extract-share-info"></a>
### `GET /api/u1/v1/xiaohongshu/app/extract_share_info`

- 摘要：提取分享链接信息/Extract share link info
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 从分享链接中提取笔记ID和xsec_token
> ### 参数:
> - share_link: 小红书分享链接，支持短链接和长链接
> ### 返回:
> - 提取的信息对象，包含：
>     - note_id: 笔记ID
>     - xsec_token: 安全令牌（如果URL中包含）
>
> ### 使用说明:
> - 支持短链接格式：https://xhslink.com/a/xxxxx
> - 支持长链接格式：
>     - https://www.xiaohongshu.com/discovery/item/xxxxx
>     - https://www.xiaohongshu.com/explore/xxxxx
> - 短链接会自动重定向获取真实链接
> - 提取的note_id可用于get_note_info接口
>
> # [English]
> ### Purpose:
> - Extract note ID and xsec_token from share link
> ### Parameters:
> - share_link: Xiaohongshu share link, support short and long links
> ### Return:
> - Extracted info object containing:
>     - note_id: Note ID
>     - xsec_token: Security token (if exists in URL)
>
> ### Usage Guide:
> - Supports short link format: https://xhslink.com/a/xxxxx
> - Supports long link formats:
>     - https://www.xiaohongshu.com/discovery/item/xxxxx
>     - https://www.xiaohongshu.com/explore/xxxxx
> - Short links will be auto-redirected to get real link
> - Extracted note_id can be used in get_note_info endpoint
>
> # [示例/Example]
> share_link="https://xhslink.com/a/EZ4M9TwMA6c3"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_link | query | string | 是 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-note-comments"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_note_comments`

- 摘要：获取笔记评论/Get note comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取笔记的评论列表
> ### 参数:
> - note_id: 笔记ID（必需）
> - start: 翻页游标，从上一次请求的响应中获取，支持两种格式：
>     1. 简单格式: "682b0133000000001c03618d"
>     2. JSON格式: {"cursor":"682b0133000000001c03618d","index":2,"pageArea":"ALL"}
> - sort_strategy: 排序策略
>     - 1: 默认排序（默认值）
>     - 2: 按最新评论排序
> ### 返回:
> - 评论数据对象，包含：
>     - comments: 评论列表数组，每个评论包含：
>         - id: 评论ID
>         - content: 评论内容
>         - create_time: 创建时间戳
>         - user_info: 评论者信息
>             - user_id: 用户ID
>             - nickname: 昵称
>             - image: 头像URL
>         - interact_info: 互动数据
>             - liked_count: 点赞数
>         - sub_comment_count: 子评论数量
>         - sub_comment_cursor: 子评论翻页游标（如有子评论）
>     - cursor: 翻页游标，用于获取下一页
>     - has_more: 是否有更多数据（布尔值）
>     - total: 总评论数
>
> ### 翻页说明:
> - 首次请求不传start参数
> - 获取下一页时，将上一次返回的cursor作为start参数传入
> - 当has_more为false时，表示没有更多数据
>
> # [English]
> ### Purpose:
> - Get note comments list
> ### Parameters:
> - note_id: Note ID (required)
> - start: Pagination cursor from previous response, supports two formats:
>     1. Simple format: "682b0133000000001c03618d"
>     2. JSON format: {"cursor":"682b0133000000001c03618d","index":2,"pageArea":"ALL"}
> - sort_strategy: Sort strategy
>     - 1: Default sort (default)
>     - 2: Sort by latest comments
> ### Return:
> - Comments data object containing:
>     - comments: Comment list array, each comment includes:
>         - id: Comment ID
>         - content: Comment content
>         - create_time: Creation timestamp
>         - user_info: Commenter info
>             - user_id: User ID
>             - nickname: Nickname
>             - image: Avatar URL
>         - interact_info: Interaction data
>             - liked_count: Like count
>         - sub_comment_count: Sub-comment count
>         - sub_comment_cursor: Sub-comment pagination cursor (if has sub-comments)
>     - cursor: Pagination cursor for next page
>     - has_more: Whether has more data (boolean)
>     - total: Total comment count
>
> ### Pagination Guide:
> - Don't pass start parameter for first request
> - For next page, pass cursor from previous response as start parameter
> - When has_more is false, no more data available
>
> # [示例/Example]
> note_id="677d1909000000002002a892"
> sort_strategy=1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 是 | 笔记ID/Note ID | 无 | 677d1909000000002002a892 | 无 |
| start | query | string | 否 | 翻页游标/Pagination cursor | 无 | 682b0133000000001c03618d | 无 |
| sort_strategy | query | integer | 否 | 排序策略：1-默认排序，2-最新评论/Sort strategy: 1-default, 2-latest | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-note-info"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_note_info`

- 摘要：获取笔记信息 V1/Get note info V1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取笔记信息 V1
> ### 接口优先级:
> - 小红书接口推荐优先级: `App V2` > `App（本接口）` > `Web V2` > `Web`
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 笔记详情数据，包含以下主要字段：
>     - note_id: 笔记ID
>     - title: 笔记标题
>     - desc: 笔记内容描述
>     - type: 笔记类型（normal=图文笔记，video=视频笔记）
>     - user: 作者信息对象
>         - user_id: 用户ID
>         - nickname: 用户昵称
>         - avatar: 用户头像URL
>     - image_list: 图片列表（图文笔记）
>     - video_info: 视频信息（视频笔记）
>     - interact_info: 互动数据
>         - liked_count: 点赞数
>         - collected_count: 收藏数
>         - comment_count: 评论数
>         - share_count: 分享数
>     - tag_list: 话题标签列表
>     - time: 发布时间戳
>     - ip_location: IP属地
>
> # [English]
> ### Purpose:
> - Get note info V1
> ### API Priority:
> - Xiaohongshu API priority: `App V2` > `App (this)` > `Web V2` > `Web`
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Note detail data with main fields:
>     - note_id: Note ID
>     - title: Note title
>     - desc: Note content description
>     - type: Note type (normal=image note, video=video note)
>     - user: Author info object
>         - user_id: User ID
>         - nickname: User nickname
>         - avatar: User avatar URL
>     - image_list: Image list (for image notes)
>     - video_info: Video info (for video notes)
>     - interact_info: Interaction data
>         - liked_count: Like count
>         - collected_count: Collect count
>         - comment_count: Comment count
>         - share_count: Share count
>     - tag_list: Topic tag list
>     - time: Publish timestamp
>     - ip_location: IP location
>
> # [示例/Example]
> note_id="665f95200000000006005624"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID | 无 | 665f95200000000006005624 | 无 |
| share_text | query | string | 否 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-note-info-v2"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_note_info_v2`

- 摘要：获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取笔记信息 V2
> - 除赞、评、藏数据之外此接口能获取到笔记的曝光量（impNum）、阅读量（readNum）、关注量（followCnt）。
> - 但是不是每一篇都有，如果是没有被小红书后台收录的笔记，赞评藏数据返回为0，但是笔记内容是完整的。
> - 通过作者userId，可以去作品列表接口拿到赞、评、藏数据
> ### 参数:
> - note_id: 笔记ID，可以从小红书的分享链接中获取
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 笔记详情数据，包含以下主要字段：
>     - note_id: 笔记ID
>     - title: 笔记标题
>     - desc: 笔记内容描述
>     - type: 笔记类型（normal=图文笔记，video=视频笔记）
>     - user: 作者信息对象
>         - user_id: 用户ID
>         - nickname: 用户昵称
>         - avatar: 用户头像URL
>     - image_list: 图片列表（图文笔记）
>     - video_info: 视频信息（视频笔记）
>     - interact_info: 互动数据
>         - liked_count: 点赞数
>         - collected_count: 收藏数
>         - comment_count: 评论数
>         - share_count: 分享数
>     - tag_list: 话题标签列表
>     - time: 发布时间戳
>     - ip_location: IP属地
>
> # [English]
> ### Purpose:
> - Get note info V2
> - This interface can get note exposure (impNum), read count (readNum), and follow count (followCnt) in addition to like, comment, and collect data.
> - However, not every note has this data. If the note is not indexed by Xiaohongshu backend, like, comment, and collect data will return 0, but the note content is complete.
> - You can get like, comment, and collect data from the note list interface using the author's userId.
> ### Parameters:
> - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Note detail data with main fields:
>     - note_id: Note ID
>     - title: Note title
>     - desc: Note content description
>     - type: Note type (normal=image note, video=video note)
>     - user: Author info object
>         - user_id: User ID
>         - nickname: User nickname
>         - avatar: User avatar URL
>     - image_list: Image list (for image notes)
>     - video_info: Video info (for video notes)
>     - interact_info: Interaction data
>         - liked_count: Like count
>         - collected_count: Collect count
>         - comment_count: Comment count
>         - share_count: Share count
>     - tag_list: Topic tag list
>     - time: Publish timestamp
>     - ip_location: IP location
>
> # [示例/Example]
> note_id="665f95200000000006005624"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 否 | 笔记ID/Note ID | 无 | 665f95200000000006005624 | 无 |
| share_text | query | string | 否 | 分享链接/Share link | 无 | https://xhslink.com/a/EZ4M9TwMA6c3 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-notes-by-topic"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_notes_by_topic`

- 摘要：[已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic
- 能力：作品详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。
> ### 用途:
> - 根据话题标签获取相关笔记
> ### 参数:
> - page_id: 话题标签ID（必需）
> - first_load_time: 首次请求的时间戳，毫秒级时间戳（必需）
>     - 例子: 1698647850000
>     - Python获取当前时间戳: `int(time.time() * 1000)`
> - sort: 排序方式
>     - "hot": 综合排序（默认）
>     - "time": 最新发布
>     - "trend": 最热门
> - session_id: 会话ID，首次不传，由服务端生成，翻页时传入
> - last_note_ct: 最后一条笔记的create_time字段，首次不传，翻页时传入
> - last_note_id: 最后一条笔记的ID，首次不传，翻页时传入
> - cursor_score: 最后一条笔记的cursor_score字段，首次不传，翻页时传入
> ### 返回:
> - 话题笔记数据，包含：
>     - notes: 笔记列表数组，每个元素包含：
>         - id: 元素ID
>         - model_type: 模型类型（通常为"note"）
>         - note: 笔记详情对象
>             - note_id: 笔记ID
>             - title: 标题
>             - desc: 描述
>             - type: 类型（normal/video）
>             - user: 作者信息
>             - interact_info: 互动数据
>             - cover: 封面图
>             - create_time: 创建时间戳
>             - cursor_score: 游标分数（用于翻页）
>     - session_id: 会话ID（翻页必需）
>     - has_more: 是否有更多数据
>
> ### 翻页说明:
> - 首次请求：只传page_id和first_load_time
> - 翻页请求：需要传入
>     1. 上一次返回的session_id
>     2. 最后一条笔记的last_note_ct（create_time）
>     3. 最后一条笔记的last_note_id（id）
>     4. 最后一条笔记的cursor_score
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly.
> ### Purpose:
> - Get notes by topic tag
> ### Parameters:
> - page_id: Topic tag ID (required)
> - first_load_time: First load timestamp in milliseconds (required)
>     - Example: 1698647850000
>     - Get current timestamp in Python: `int(time.time() * 1000)`
> - sort: Sort method
>     - "hot": Comprehensive (default)
>     - "time": Latest published
>     - "trend": Trending
> - session_id: Session ID, not required for first request, use returned value for pagination
> - last_note_ct: Last note create_time field for pagination
> - last_note_id: Last note ID for pagination
> - cursor_score: Last note cursor_score field for pagination
> ### Return:
> - Topic notes data containing:
>     - notes: Notes list array, each element includes:
>         - id: Element ID
>         - model_type: Model type (usually "note")
>         - note: Note detail object
>             - note_id: Note ID
>             - title: Title
>             - desc: Description
>             - type: Type (normal/video)
>             - user: Author info
>             - interact_info: Interaction data
>             - cover: Cover image
>             - create_time: Creation timestamp
>             - cursor_score: Cursor score (for pagination)
>     - session_id: Session ID (required for pagination)
>     - has_more: Whether has more data
>
> ### Pagination Guide:
> - First request: Only pass page_id and first_load_time
> - Next requests: Need to pass
>     1. session_id from previous response
>     2. last_note_ct (create_time of last note)
>     3. last_note_id (id of last note)
>     4. cursor_score of last note
>
> # [示例/Example]
> page_id="5c014b045b29cb0001ead530"
> first_load_time="1698647850000"
> sort="hot"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page_id | query | string | 是 | 话题标签ID/Topic tag ID | 无 | 5c014b045b29cb0001ead530 | 无 |
| first_load_time | query | string | 是 | 首次请求时间戳（毫秒）/First load timestamp (ms) | 无 | 1698647850000 | 无 |
| sort | query | string | 否 | 排序方式：hot-综合，time-最新，trend-最热/Sort: hot-comprehensive, time-latest, trend-trending | hot | hot | 无 |
| session_id | query | string | 否 | 会话ID/Session ID | 无 | 989615e2-ce54-414a-9c7a-6c1e5e79c5f7 | 无 |
| last_note_ct | query | string | 否 | 最后一条笔记创建时间/Last note create time | 无 | 1698647850000 | 无 |
| last_note_id | query | string | 否 | 最后一条笔记ID/Last note ID | 无 | 653f4f2a0000000025017109 | 无 |
| cursor_score | query | string | 否 | 游标分数/Cursor score | 无 | rNqgDUXZhHqdL4z4kKah5Lw6P_OSU9_fgubmTsiop_s | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-product-detail"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_product_detail`

- 摘要：获取商品详情/Get product detail
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取小红书商品详情信息
> ### 参数:
> - sku_id: 商品skuId（必需）
> ### 返回:
> - 商品详情数据
>
> # [English]
> ### Purpose:
> - Get Xiaohongshu product detail info
> ### Parameters:
> - sku_id: Product SKU ID (required)
> ### Return:
> - Product detail data
>
> # [示例/Example]
> sku_id="68be7cbc8c331700011f89d1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sku_id | query | string | 是 | 商品skuId/Product SKU ID | 无 | 68be7cbc8c331700011f89d1 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-sub-comments"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_sub_comments`

- 摘要：获取子评论/Get sub comments
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取评论的子评论（回复）列表
> ### 参数:
> - note_id: 笔记ID（必需）
> - comment_id: 一级评论ID，要查看哪条评论的子评论（必需）
> - start: 翻页游标，从上一次请求的响应中获取，从评论列表的最后一条子评论ID获取：
>     格式如下: "6806642d000000001f01991b"
> ### 返回:
> - 子评论列表数组，每个子评论包含：
>     - id: 子评论ID
>     - content: 评论内容
>     - create_time: 创建时间戳
>     - user_info: 评论者信息
>         - user_id: 用户ID
>         - nickname: 昵称
>         - image: 头像URL
>     - target_comment: 被回复的评论信息（如果是回复其他子评论）
>         - id: 被回复评论ID
>         - user_info: 被回复者信息
>             - nickname: 被回复者昵称
>
> ### 翻页说明:
> - 首次请求不传start参数
> - 获取更多时，将上一次请求返回的最后一条子评论ID作为start参数
>
> # [English]
> ### Purpose:
> - Get sub comments (replies) list
> ### Parameters:
> - note_id: Note ID (required)
> - comment_id: Parent comment ID to get sub comments (required)
> - start: Pagination cursor from previous response, obtained from the last sub-comment ID in the comment list:
>     Format: "6806642d000000001f01991b"
> ### Return:
> - Sub comments array list, each sub-comment includes:
>     - id: Sub-comment ID
>     - content: Comment content
>     - create_time: Creation timestamp
>     - user_info: Commenter info
>         - user_id: User ID
>         - nickname: Nickname
>         - image: Avatar URL
>     - target_comment: Replied comment info (if replying to other sub-comment)
>         - id: Replied comment ID
>         - user_info: Replied user info
>             - nickname: Replied user nickname
>
> ### Pagination Guide:
> - Don't pass start parameter for first request
> - For more data, pass last sub-comment ID from previous response as start parameter
>
> # [示例/Example]
> note_id="677d1909000000002002a892"
> comment_id="677f67e400000000220013f3"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | 是 | 笔记ID/Note ID | 无 | 677d1909000000002002a892 | 无 |
| comment_id | query | string | 是 | 一级评论ID/Parent comment ID | 无 | 677f67e400000000220013f3 | 无 |
| start | query | string | 否 | 翻页游标/Pagination cursor | 无 | 6806642d000000001f01991b | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-user-id-and-xsec-token"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`

- 摘要：从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get`

#### 说明

> # [中文]
> ### 用途:
> - 从用户分享链接中提取用户ID和xsec_token
> ### 参数:
> - share_link: 小红书用户分享链接，支持短链接和长链接
> ### 返回:
> - 提取的信息对象，包含：
>     - user_id: 用户ID
>     - xsec_token: 安全令牌（如果URL中包含）
>
> ### 使用说明:
> - 支持短链接格式：https://xhslink.com/m/xxxxx
> - 支持长链接格式：https://www.xiaohongshu.com/user/profile/xxxxx
> - 提取的user_id可用于get_user_info接口
>
> # [English]
> ### Purpose:
> - Extract user ID and xsec_token from user share link
> ### Parameters:
> - share_link: Xiaohongshu user share link, support short and long links
> ### Return:
> - Extracted info object containing:
>     - user_id: User ID
>     - xsec_token: Security token (if exists in URL)
>
> ### Usage Guide:
> - Supports short link format: https://xhslink.com/m/xxxxx
> - Supports long link format: https://www.xiaohongshu.com/user/profile/xxxxx
> - Extracted user_id can be used in get_user_info endpoint
> # [示例/Example]
> share_link="https://xhslink.com/m/Ap1vXtgAixh"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_link | query | string | 是 | 用户分享链接/User share link | 无 | https://xhslink.com/m/Ap1vXtgAixh | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-user-info"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_user_info`

- 摘要：获取用户信息/Get user info
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_info_api_v1_xiaohongshu_app_get_user_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户详情信息
> ### 参数:
> - user_id: 用户ID（必需）
> ### 返回:
> - 用户详情数据，包含：
>     - user_id: 用户ID
>     - nickname: 昵称
>     - desc: 个人简介
>     - gender: 性别（0=女，1=男，2=未知）
>     - images: 头像URL
>     - imageb: 背景图URL
>     - red_official_verify_type: 官方认证类型（0=无，1=个人，2=机构）
>     - red_official_verify_show: 是否显示认证标识
>     - level: 等级信息
>         - image: 等级图标URL
>         - name: 等级名称
>     - follows: 关注数
>     - fans: 粉丝数
>     - interaction: 获赞与收藏总数
>     - notes: 笔记数
>     - boards: 专辑数
>     - location: 所在地
>     - collected: 收藏数
>     - liked: 点赞数
>
> # [English]
> ### Purpose:
> - Get user detail info
> ### Parameters:
> - user_id: User ID (required)
> ### Return:
> - User detail data including:
>     - user_id: User ID
>     - nickname: Nickname
>     - desc: Personal bio
>     - gender: Gender (0=female, 1=male, 2=unknown)
>     - images: Avatar URL
>     - imageb: Background image URL
>     - red_official_verify_type: Official verify type (0=none, 1=personal, 2=organization)
>     - red_official_verify_show: Whether show verify badge
>     - level: Level info
>         - image: Level icon URL
>         - name: Level name
>     - follows: Following count
>     - fans: Fans count
>     - interaction: Total likes & collects
>     - notes: Notes count
>     - boards: Album count
>     - location: Location
>     - collected: Collect count
>     - liked: Like count
>
> # [示例/Example]
> user_id="5c2f338a000000000701e1c6"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | 5c2f338a000000000701e1c6 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-get-user-notes"></a>
### `GET /api/u1/v1/xiaohongshu/app/get_user_notes`

- 摘要：获取用户作品列表/Get user notes
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户发布的笔记列表
> ### 参数:
> - user_id: 用户ID（必需）
> - cursor: 翻页索引，上一次请求返回的cursor字段，不传默认请求第一页
> - cursor取值方式为notes列表的最后一条笔记的note_id
> ### 返回:
> - 用户笔记列表数据，包含：
>     - notes: 笔记数组，每个笔记包含：
>         - note_id: 笔记ID
>         - type: 类型（normal=图文，video=视频）
>         - display_title: 标题
>         - desc: 描述
>         - liked_count: 点赞数
>         - cover: 封面图信息
>             - url: 图片URL
>             - width: 宽度
>             - height: 高度
>         - user: 作者信息（通常与查询用户相同）
>     - cursor: 翻页游标
>     - has_more: 是否有更多数据
>
> ### 翻页说明:
> - 首次请求：只传user_id
> - 翻页请求：传入上一次返回的cursor
> - 当has_more为false时，表示没有更多笔记
>
> # [English]
> ### Purpose:
> - Get user's published notes list
> ### Parameters:
> - user_id: User ID (required)
> - cursor: Pagination cursor from previous response, omit for first page
> - Cursor value is the note_id of the last note in the notes list
> ### Return:
> - User notes data including:
>     - notes: Notes array, each note contains:
>         - note_id: Note ID
>         - type: Type (normal=image, video=video)
>         - display_title: Title
>         - desc: Description
>         - liked_count: Like count
>         - cover: Cover image info
>             - url: Image URL
>             - width: Width
>             - height: Height
>         - user: Author info (usually same as queried user)
>     - cursor: Pagination cursor
>     - has_more: Whether has more data
>
> ### Pagination Guide:
> - First request: Only pass user_id
> - Next pages: Pass cursor from previous response
> - When has_more is false, no more notes available
>
> # [示例/Example]
> user_id="5c57e6a4000000001802a013"
> cursor="67ee399f000000001c02f36f"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | 5c57e6a4000000001802a013 | 无 |
| cursor | query | string | 否 | 翻页游标/Pagination cursor | 无 | 67ee399f000000001c02f36f | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-search-notes"></a>
### `GET /api/u1/v1/xiaohongshu/app/search_notes`

- 摘要：搜索笔记/Search notes
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_notes_api_v1_xiaohongshu_app_search_notes_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索小红书笔记
> ### 参数:
> - keyword: 要搜索的关键词（必需）
> - page: 第几页，从1开始（必需）
> - search_id: 搜索ID，第一次请求可不传，服务端会生成searchId，翻页时需要携带服务端返回的searchId
> - session_id: 会话ID，第一次请求可不传，服务端会生成sessionId，翻页时携带服务端返回的sessionId
> - sort_type: 排序规则
>     - "general": 综合排序（默认）
>     - "time_descending": 最新发布
>     - "popularity_descending": 最多点赞
>     - "comment_descending": 最多评论
>     - "collect_descending": 最多收藏
> - filter_note_type: 筛选笔记类型
>     - "不限": 所有类型（默认）
>     - "视频笔记": 仅视频
>     - "普通笔记": 仅图文
> - filter_note_time: 筛选笔记发布时间
>     - "不限": 所有时间（默认）
>     - "一天内": 24小时内
>     - "一周内": 7天内
>     - "半年内": 6个月内
> ### 返回:
> - 搜索结果数据，包含：
>     - items: 搜索结果列表，每个元素包含：
>         - id: 元素ID
>         - model_type: 模型类型（通常为"note"）
>         - note: 笔记详情
>             - note_id: 笔记ID
>             - type: 类型（normal=图文，video=视频）
>             - display_title: 标题（关键词会高亮）
>             - desc: 内容描述（搜索接口无法返回完整的 desc，仅部分内容，请使用笔记详情接口获取完整内容）
>             - user: 作者信息
>             - interact_info: 互动数据
>                 - liked_count: 点赞数
>             - cover: 封面图信息
>     - searchId: 搜索ID（翻页必需，不同关键词不要复用）
>     - sessionId: 会话ID（翻页必需）
>     - has_more: 是否有更多数据
>     - total_count: 搜索结果总数
>
> ### 翻页说明:
> - 首次搜索：只传keyword和page=1
> - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId
> - 注意：更换关键词时不要复用之前的searchId
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu notes
> ### Parameters:
> - keyword: Search keyword (required)
> - page: Page number, start from 1 (required)
> - search_id: Search ID, optional for first request, required for pagination
> - session_id: Session ID, optional for first request, required for pagination
> - sort_type: Sort method
>     - "general": Comprehensive (default)
>     - "time_descending": Latest published
>     - "popularity_descending": Most liked
>     - "comment_descending": Most commented
>     - "collect_descending": Most collected
> - filter_note_type: Note type filter
>     - "不限": All types (default)
>     - "视频笔记": Video only
>     - "普通笔记": Image & text only
> - filter_note_time: Time filter
>     - "不限": All time (default)
>     - "一天内": Within 24 hours
>     - "一周内": Within 7 days
>     - "半年内": Within 6 months
> ### Return:
> - Search results data containing:
>     - items: Search results list, each element includes:
>         - id: Element ID
>         - model_type: Model type (usually "note")
>         - note: Note details
>             - note_id: Note ID
>             - type: Type (normal=image, video=video)
>             - display_title: Title (keywords highlighted)
>             - desc: Content description (incomplete in search results, use note detail API for full content)
>             - user: Author info
>             - interact_info: Interaction data
>                 - liked_count: Like count
>             - cover: Cover image info
>     - searchId: Search ID (required for pagination, don't reuse for different keywords)
>     - sessionId: Session ID (required for pagination)
>     - has_more: Whether has more data
>     - total_count: Total search results count
>
> ### Pagination Guide:
> - First search: Only pass keyword and page=1
> - Next pages: Pass same keyword, increment page, include searchId and sessionId from first response
> - Note: Don't reuse searchId when changing keywords
>
> # [示例/Example]
> keyword="猫粮"
> page=1
> sort_type="general"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | 猫粮 | 无 |
| page | query | integer | 是 | 页码（从1开始）/Page number (start from 1) | 无 | 1 | 无 |
| search_id | query | string | 否 | 搜索ID，翻页时使用/Search ID for pagination | 无 | 2egvdsiowvfm9thbt260w | 无 |
| session_id | query | string | 否 | 会话ID，翻页时使用/Session ID for pagination | 无 | 2egvdt4sl2b7rnfg8zk00 | 无 |
| sort_type | query | string | 否 | 排序方式/Sort type | general | general | 无 |
| filter_note_type | query | string | 否 | 笔记类型筛选：不限、视频笔记、普通笔记/Note type filter | 不限 | 不限 | 无 |
| filter_note_time | query | string | 否 | 发布时间筛选：不限、一天内、一周内、半年内/Time filter | 不限 | 不限 | 无 |

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

<a id="get-api-u1-v1-xiaohongshu-app-search-products"></a>
### `GET /api/u1/v1/xiaohongshu/app/search_products`

- 摘要：搜索商品/Search products
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_products_api_v1_xiaohongshu_app_search_products_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索小红书商品
> ### 参数:
> - keyword: 搜索关键词（必需）
> - page: 页码，从1开始（必需）
> - search_id: 搜索ID，第一次请求可不传，翻页时需要携带服务端返回的searchId
> - session_id: 会话ID，第一次请求可不传，翻页时携带服务端返回的sessionId
> - sort: 排序规则，默认综合
>     - "sales_qty": 销量
>     - "price_asc": 价格升序
>     - "price_desc": 价格降序
> - scope: 搜索范围，默认不限
>     - "purchased": 买过的店
>     - "following": 关注的店
> - service_guarantee: 物流权益，多选用英文逗号分割
>     - 可选值: "24小时发货", "七天无理由", "现货", "退货包运费"
> - min_price: 最低价
> - max_price: 最高价
> - super_promotion: 标签ID
> ### 返回:
> - 搜索结果数据，包含：
>     - items: 商品列表
>     - searchId: 搜索ID（翻页必需）
>     - sessionId: 会话ID（翻页必需）
>     - has_more: 是否有更多数据
>
> ### 翻页说明:
> - 首次搜索：只传keyword和page=1
> - 翻页搜索：传入相同keyword，递增page，并携带首次返回的searchId和sessionId
> - 注意：更换关键词时不要复用之前的searchId
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu products
> ### Parameters:
> - keyword: Search keyword (required)
> - page: Page number, start from 1 (required)
> - search_id: Search ID, optional for first request, required for pagination
> - session_id: Session ID, optional for first request, required for pagination
> - sort: Sort method
>     - "sales_qty": By sales
>     - "price_asc": Price ascending
>     - "price_desc": Price descending
> - scope: Search scope
>     - "purchased": Shops you've bought from
>     - "following": Shops you follow
> - service_guarantee: Service guarantees, comma separated
>     - Options: "24小时发货", "七天无理由", "现货", "退货包运费"
> - min_price: Minimum price
> - max_price: Maximum price
> - super_promotion: Promotion tag ID
> ### 返回:
> - Search results containing:
>     - items: Product list
>     - searchId: Search ID (required for pagination)
>     - sessionId: Session ID (required for pagination)
>     - has_more: Whether has more data
>
> ### Pagination Guide:
> - First search: Only pass keyword and page=1
> - Next pages: Pass same keyword, increment page, include searchId and sessionId
> - Note: Don't reuse searchId when changing keywords
>
> # [示例/Example]
> keyword="充电宝"
> page=1
> sort="sales_qty"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | 充电宝 | 无 |
| page | query | integer | 是 | 页码（从1开始）/Page number (start from 1) | 无 | 1 | 无 |
| search_id | query | string | 否 | 搜索ID，翻页时使用/Search ID for pagination | 无 | 无 | 无 |
| session_id | query | string | 否 | 会话ID，翻页时使用/Session ID for pagination | 无 | 无 | 无 |
| sort | query | string | 否 | 排序规则：sales_qty-销量、price_asc-价格升序、price_desc-价格降序/Sort: sales_qty, price_asc, price_desc | 无 | sales_qty | 无 |
| scope | query | string | 否 | 搜索范围：purchased-买过的店、following-关注的店/Scope: purchased, following | 无 | purchased | 无 |
| service_guarantee | query | string | 否 | 物流权益，多选用英文逗号分割/Service guarantee, comma separated | 无 | 24小时发货,七天无理由 | 无 |
| min_price | query | string | 否 | 最低价/Min price | 无 | 1 | 无 |
| max_price | query | string | 否 | 最高价/Max price | 无 | 100 | 无 |
| super_promotion | query | string | 否 | 标签ID/Promotion tag ID | 无 | 695fb0a330425100017ff555 | 无 |

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
