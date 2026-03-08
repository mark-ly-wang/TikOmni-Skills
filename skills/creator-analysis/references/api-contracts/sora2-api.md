# Sora2-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/sora2-api.md`](../api-tags/sora2-api.md)
- 当前契约文件：`api-contracts/sora2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`17`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(Sora2 接口/Sora2 API endpoints)**

## 路由契约

<a id="post-api-u1-v1-sora2-create-video"></a>
### `POST /api/u1/v1/sora2/create_video`

- 摘要：[已弃用/Deprecated] 文本/图片生成视频/Create video from text or image
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`create_video_api_v1_sora2_create_video_post`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io
> ### 用途:
> - 通过文本描述生成 Sora 视频（支持纯文本生成或图片+文本生成）
> - 支持两种生成模式：
>     - **纯文本生成**：AI 根据文本描述自动生成视频内容
>     - **图生视频**：基于上传的图片和文本描述生成视频（需要先调用 upload_image 接口）
> - 支持两种视频比例：
>     - **portrait（竖屏）**: 9:16 比例，适合移动端、社交媒体短视频
>     - **landscape（横屏）**: 16:9 比例，适合桌面端、宽屏展示、电影风格
> - 返回生成任务 ID，需要通过其他接口查询生成进度和结果
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 **$0.1 美元**
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数
>
> ### 参数:
> - **prompt** (必填): 视频描述文本，最多 2000 字符
>     - 描述要生成的视频内容、场景、动作、情节等
>     - 建议使用清晰、具体的描述以获得更好的生成效果
>     - 示例："A cat is playing Minecraft"
> - **orientation** (可选): 视频方向，默认为 portrait（竖屏）
>     - `portrait`: 竖屏（9:16 比例）
>     - `landscape`: 横屏（16:9 比例）
> - **media_id** (可选): 图片 media_id，用于图生视频
>     - 通过 `/upload_image` 接口上传图片后获取
>     - 格式：`media_xxxxxxxxxxxxxxxxxxxxxxxxxx`
>     - 如果不提供，则为纯文本生成视频
>
> ### 返回:
> - **id**: 视频生成任务 ID
>     - 格式：`task_xxxxxxxxxxxxxxxxxxxxxxxxxx`
>     - 使用此 ID 可以查询生成进度和获取最终视频
> - **priority**: 任务优先级
>     - 通常为 1（标准优先级）
>
> ### 注意:
> - 这是一个异步生成任务，不会立即返回视频
> - 视频生成通常需要几分钟时间
> - 需要使用任务 ID 通过其他接口轮询查询生成状态
> - 请自行保留任务 ID，以便后续查询，否则将无法获取生成结果
>
> # [English]
> ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io
> ### Purpose:
> - Generate Sora video from text description (supports text-only or image+text generation)
> - Supports two generation modes:
>     - **Text-only generation**: AI automatically generates video content based on text description
>     - **Image-to-video**: Generate video based on uploaded image and text description (requires calling upload_image endpoint first)
> - Supports two video ratios:
>     - **portrait**: 9:16 ratio, suitable for mobile devices, social media short videos
>     - **landscape**: 16:9 ratio, suitable for desktop viewing, widescreen display, cinematic style
> - Returns generation task ID, need to query generation progress and results through other endpoints
>
> ### Pricing:
> - This API costs **$0.1 USD per request**
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard
>
> ### Parameters:
> - **prompt** (required): Video description text, maximum 2000 characters
>     - Describe the video content, scenes, actions, plots, etc. to be generated
>     - Recommend using clear and specific descriptions for better generation results
>     - Example: "A cat is playing Minecraft"
> - **orientation** (optional): Video orientation, defaults to portrait
>     - `portrait`: Portrait (9:16 ratio)
>     - `landscape`: Landscape (16:9 ratio)
> - **media_id** (optional): Image media_id for image-to-video generation
>     - Obtained from `/upload_image` endpoint after uploading an image
>     - Format: `media_xxxxxxxxxxxxxxxxxxxxxxxxxx`
>     - If not provided, text-only video generation will be used
>
> ### Return:
> - **id**: Video generation task ID
>     - Format: `task_xxxxxxxxxxxxxxxxxxxxxxxxxx`
>     - Use this ID to query generation progress and get final video
> - **priority**: Task priority
>     - Usually 1 (standard priority)
>
> ### Note:
> - This is an asynchronous generation task, will not return video immediately
> - Video generation usually takes several minutes
> - Need to use task ID to poll generation status through other endpoints
> - Please keep the task ID for future queries, otherwise you will not be able to get the generation results
>
> # [示例/Example]
> ```python
> import requests
>
> # 示例 1：纯文本生成竖屏视频/Example 1: Text-only portrait video
> url = "https://api.tikhub.io/api/v1/sora2/create_video"
> headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
> payload = {
>     "prompt": "A cat is playing Minecraft",
>     "orientation": "portrait"
> }
> response = requests.post(url, headers=headers, json=payload)
>
> # 示例 2：图片+文本生成视频（图生视频）/Example 2: Image-to-video generation
> # 步骤1：上传图片获取 media_id/Step 1: Upload image to get media_id
> upload_url = "https://api.tikhub.io/api/v1/sora2/upload_image"
> with open("image.png", "rb") as f:
>     files = {"file": ("image.png", f, "image/png")}
>     upload_resp = requests.post(upload_url, headers=headers, files=files)
>     media_id = upload_resp.json()["data"]["id"]  # 例如: "media_01k7..."
>
> # 步骤2：使用 media_id 生成视频/Step 2: Use media_id to generate video
> payload = {
>     "prompt": "Transform this image into a dynamic video scene",
>     "orientation": "landscape",
>     "media_id": media_id  # 来自 upload_image 的 media_id
> }
> response = requests.post(url, headers=headers, json=payload)
>
> # 返回示例/Return example
> {
>     "code": 200,
>     "data": {
>         "id": "task_01k7e05chaem08va8sq5qy2een",
>         "priority": 1
>     }
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`prompt*`:string, `orientation`:string, `media_id`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| prompt | string | 是 | 视频描述文本（最多2000字符）/Video description text (max 2000 chars) | 无 | A cat is playing Minecraft | 无 |
| orientation | string enum[portrait, landscape] | 否 | 视频方向：portrait(竖屏9:16) 或 landscape(横屏16:9)/Video orientation: portrait(9:16) or landscape(16:9) | portrait | 无 | enum[portrait, landscape] |
| media_id | string | 否 | 图片 media_id（可选），从 upload_image 接口获取，用于图生视频/Image media_id (optional) from upload_image endpoint for image-to-video generation | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-cameo-leaderboard"></a>
### `GET /api/u1/v1/sora2/get_cameo_leaderboard`

- 摘要：获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora Cameo 出镜秀达人排行榜
> - 展示在 Cameo 功能中被使用最多的用户
> - 支持分页获取更多排行榜数据
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取，每页返回 10 个用户
>
> ### 返回:
> - items: 用户排行榜列表（每页 10 个用户）
>     - user_id: 用户 ID
>     - username: 用户名
>     - display_name: 显示名称
>     - profile_picture_url: 头像链接
>     - follower_count: 粉丝数
>     - cameo_count: 被使用次数
> - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）
>
> # [English]
> ### Purpose:
> - Fetch Sora Cameo leaderboard
> - Shows the most featured users in the Cameo function
> - Supports pagination to get more leaderboard data
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response, returns 10 users per page
>
> ### Return:
> - items: User leaderboard list (10 users per page)
>     - user_id: User ID
>     - username: Username
>     - display_name: Display name
>     - profile_picture_url: Profile picture URL
>     - follower_count: Follower count
>     - cameo_count: Feature count
> - cursor: Next page parameter for fetching more data (null means last page)
>
> # [示例/Example]
> ```python
> # 获取第一页排行榜
> # Get first page of leaderboard
> response = await get_cameo_leaderboard()
>
> # 使用 cursor 获取下一页
> # Use cursor to get next page
> cursor = response['cursor']
> next_page = await get_cameo_leaderboard(cursor=cursor)
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cursor | query | string | 否 | 翻页参数（可选）/Cursor for pagination (optional) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-comment-replies"></a>
### `GET /api/u1/v1/sora2/get_comment_replies`

- 摘要：获取评论的回复/Fetch comment replies
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_comment_replies_api_v1_sora2_get_comment_replies_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取一级评论的回复列表（二级评论）
> - 支持分页加载，每页返回 10 条回复
> - 用于展示评论的完整对话树
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - comment_id: 一级评论的 ID，必填（可从 get_post_comments 接口的返回中获取）
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - children: 回复数据
>     - items: 回复列表（10条/页）
>         - id: 回复 ID
>         - text: 回复文本内容
>         - posted_by: 回复者用户 ID
>         - posted_at: 回复时间戳
>         - like_count: 点赞数
>         - profile: 回复者信息
>             - username: 用户名
>             - display_name: 显示名称
>             - profile_picture_url: 头像链接
>     - cursor: 下一页参数（用于获取更多回复，无更多时为 null）
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch replies for a first-level comment (second-level comments)
> - Supports pagination, returns 10 replies per page
> - Used to display complete comment conversation tree
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - comment_id: First-level comment ID, required (can be obtained from get_post_comments response)
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - children: Reply data
>     - items: Reply list (10 items/page)
>         - id: Reply ID
>         - text: Reply text content
>         - posted_by: Replier user ID
>         - posted_at: Reply timestamp
>         - like_count: Like count
>         - profile: Replier information
>             - username: Username
>             - display_name: Display name
>             - profile_picture_url: Avatar URL
>     - cursor: Next page cursor (for loading more replies, null when no more)
>     - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 首先获取一级评论
> # post_comments = get_post_comments("s_68e647d78e5081918cdeaf27e7edc735")
> # comment_id = post_comments['children']['items'][0]['id']  # 第一条评论的 ID
>
> # 然后获取该评论的回复
> comment_id = "68e659c5a37081919618c57baf499d0c"
> cursor = ""  # 首次请求留空
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| comment_id | query | string | 是 | 一级评论ID/First-level comment ID | 无 | 68e659c5a37081919618c57baf499d0c | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-feed"></a>
### `GET /api/u1/v1/sora2/get_feed`

- 摘要：获取Feed流（热门/推荐视频）/Fetch feed
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_feed_api_v1_sora2_get_feed_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 的 Feed 流（热门或推荐视频列表）
> - 默认返回过去 7 天的热门视频
> - 支持分页加载，每页返回约 15 条视频
> - 可通过 eager_views 参数提供观看记录来获得个性化推荐
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
> - eager_views: 观看记录（可选），JSON 字符串格式
>     - 默认值：`{"views":[]}`（空观看记录，返回通用热门）
>     - 包含观看记录示例：`{"views":[{"id":"s_xxx","watch_time":0.24,"dwell_time":3.94}]}`
>     - 提供观看记录可获得更个性化的推荐结果
>
> ### 返回:
> - items: 视频列表（约15条/页）
>     - post: 作品信息
>         - id: 作品 ID
>         - text: 作品描述
>         - attachments: 视频附件信息
>         - like_count: 点赞数
>         - view_count: 浏览数
>         - reply_count: 评论数
>         - posted_at: 发布时间戳
>     - profile: 作者信息
> - cursor: 下一页参数（用于获取更多视频，无更多时为 null）
> - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch Sora's feed stream (trending or recommended video list)
> - Returns trending videos from the past 7 days by default
> - Supports pagination, returns approximately 15 videos per page
> - Can provide watch history via eager_views parameter for personalized recommendations
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
> - eager_views: Watch history (optional), JSON string format
>     - Default value: `{"views":[]}` (empty watch history, returns general trending)
>     - With watch history example: `{"views":[{"id":"s_xxx","watch_time":0.24,"dwell_time":3.94}]}`
>     - Providing watch history enables more personalized recommendation results
>
> ### Return:
> - items: Video list (approx. 15 items/page)
>     - post: Post information
>         - id: Post ID
>         - text: Post description
>         - attachments: Video attachment info
>         - like_count: Like count
>         - view_count: View count
>         - reply_count: Comment count
>         - posted_at: Post timestamp
>     - profile: Author information
> - cursor: Next page cursor (for loading more videos, null when no more)
> - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 第一次请求（获取热门视频，无观看记录）
> cursor = ""
> eager_views = '{"views":[]}'
>
> # 第二次请求（带观看记录，获得个性化推荐）
> eager_views = '{"views":[{"id":"s_68e853d2ad448191b3c81e830f53c3a2","watch_time":0.24,"dwell_time":3.94}]}'
>
> # 第三次请求（获取下一页）
> cursor = "eyJjdXQiOiJuZjJfdG9wXzdkIiwibGltaXQiOjE1LCJvZmZzZXQiOjE1fQ=="
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |
| eager_views | query | string | 否 | 观看记录JSON字符串（可选），用于个性化推荐/Watch history JSON string (optional), for personalized recommendations | 无 | {"views":[]} | 无 |

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

<a id="get-api-u1-v1-sora2-get-post-comments"></a>
### `GET /api/u1/v1/sora2/get_post_comments`

- 摘要：获取作品一级评论/Fetch post comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_post_comments_api_v1_sora2_get_post_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 作品的一级评论列表（顶层评论）
> - 支持分页加载，每页返回 10 条评论
> - 可用于评论展示、数据分析等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - post_id: 作品 ID，必填
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - children: 评论数据
>     - items: 评论列表（10条/页）
>         - id: 评论 ID
>         - text: 评论文本内容
>         - posted_by: 评论者用户 ID
>         - posted_at: 评论时间戳
>         - like_count: 点赞数
>         - reply_count: 回复数（二级评论数）
>         - profile: 评论者信息
>             - username: 用户名
>             - display_name: 显示名称
>             - profile_picture_url: 头像链接
>     - cursor: 下一页参数（用于获取更多评论，无更多时为 null）
>     - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch first-level comments (top-level comments) for a Sora post
> - Supports pagination, returns 10 comments per page
> - Can be used for comment display, data analysis, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - post_id: Post ID, required
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - children: Comment data
>     - items: Comment list (10 items/page)
>         - id: Comment ID
>         - text: Comment text content
>         - posted_by: Commenter user ID
>         - posted_at: Comment timestamp
>         - like_count: Like count
>         - reply_count: Reply count (second-level comments)
>         - profile: Commenter information
>             - username: Username
>             - display_name: Display name
>             - profile_picture_url: Avatar URL
>     - cursor: Next page cursor (for loading more comments, null when no more)
>     - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 第一次请求（获取前 10 条评论）
> post_id = "s_68e647d78e5081918cdeaf27e7edc735"
> cursor = ""  # 首次请求留空
>
> # 第二次请求（获取下一页）
> # 使用上一次响应中的 cursor 值
> cursor = "eyJwb3N0X2lkIjoiNjhlNjQ3ZDc4ZTUwODE5MThjZGVhZjI3ZTdlZGM3MzUi..."
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | 是 | 作品ID/Post ID | 无 | s_68e647d78e5081918cdeaf27e7edc735 | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-post-detail"></a>
### `GET /api/u1/v1/sora2/get_post_detail`

- 摘要：获取单一作品详情/Fetch single post detail
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_post_detail_api_v1_sora2_get_post_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 作品的完整详情信息，包括视频信息、作者信息、统计数据等
> - 支持通过作品 ID 或作品链接查询
> - 可用于数据分析、无水印视频下载等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2`
> - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2`
> - **注意**: post_id 和 post_url 至少提供一个
>
> ### 返回:
> - post: 作品详细信息
>     - id: 作品 ID
>     - text: 作品描述文本
>     - attachments: 附件列表（视频信息）
>         - url: 无水印视频链接
>         - downloadable_url: 有水印视频链接
>         - width/height: 视频尺寸
>         - encodings: 不同质量的编码版本
>     - like_count: 点赞数
>     - view_count: 浏览数
>     - reply_count: 评论数
>     - remix_count: 混剪数
>     - shared_by: 作者用户 ID
>     - posted_at: 发布时间戳
>     - permalink: 作品永久链接
> - profile: 作者信息
>     - user_id: 用户 ID
>     - username: 用户名
>     - display_name: 显示名称
>     - profile_picture_url: 头像链接
>     - follower_count: 粉丝数
>
> # [English]
> ### Purpose:
> - Fetch complete details of a Sora post, including video info, author info, and statistics
> - Supports querying by post ID or post URL
> - Can be used for data analysis, watermark-free video downloads, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2`
> - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2`
> - **Note**: At least one of post_id or post_url must be provided
>
> ### Return:
> - post: Post detailed information
>     - id: Post ID
>     - text: Post description text
>     - attachments: Attachment list (video info)
>         - url: No watermark video link
>         - downloadable_url: Watermarked video link
>         - width/height: Video dimensions
>         - encodings: Different quality encoding versions
>     - like_count: Like count
>     - view_count: View count
>     - reply_count: Comment count
>     - remix_count: Remix count
>     - shared_by: Author user ID
>     - posted_at: Post timestamp
>     - permalink: Permanent link
> - profile: Author information
>     - user_id: User ID
>     - username: Username
>     - display_name: Display name
>     - profile_picture_url: Avatar URL
>     - follower_count: Follower count
>
> # [示例/Example]
> ```python
> # 使用作品 ID 查询
> post_id = "s_68e853d2ad448191b3c81e830f53c3a2"
>
> # 或使用作品链接查询
> post_url = "https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2"
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | 否 | 作品ID（可选）/Post ID (optional) | 无 | s_68e853d2ad448191b3c81e830f53c3a2 | 无 |
| post_url | query | string | 否 | 作品链接（可选）/Post URL (optional) | 无 | https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2 | 无 |

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

<a id="get-api-u1-v1-sora2-get-post-remix-list"></a>
### `GET /api/u1/v1/sora2/get_post_remix_list`

- 摘要：获取作品的 Remix 列表/Fetch post remix list
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_post_remix_list_api_v1_sora2_get_post_remix_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 作品的 Remix 列表
> - 支持通过作品 ID 或作品链接查询
> - 支持分页获取更多 Remix 作品
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - post_id: 作品 ID（可选），格式如 `s_68e466aa780c8191b`
> - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39`
> - cursor: 翻页参数（可选），从上一次响应的 cursor 字段获取
> - **注意**: post_id 和 post_url 至少提供一个
>
> ### 返回:
> - items: Remix 作品列表
>     - id: 作品 ID
>     - text: 作品描述文本
>     - attachments: 附件列表（视频信息）
>     - like_count: 点赞数
>     - view_count: 浏览数
>     - reply_count: 评论数
>     - remix_count: 混剪数
>     - shared_by: 作者用户 ID
>     - posted_at: 发布时间戳
> - cursor: 下一页参数，用于获取更多数据（如果为 null 表示已到末页）
>
> # [English]
> ### Purpose:
> - Fetch the Remix list of a Sora post
> - Supports querying by post ID or post URL
> - Supports pagination to get more Remix posts
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - post_id: Post ID (optional), format like `s_68e466aa780c8191b`
> - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e466aa780c8191b2357907ce7d1a39`
> - cursor: Cursor for pagination (optional), obtained from the cursor field of the previous response
> - **Note**: At least one of post_id or post_url must be provided
>
> ### Return:
> - items: Remix post list
>     - id: Post ID
>     - text: Post description text
>     - attachments: Attachment list (video info)
>     - like_count: Like count
>     - view_count: View count
>     - reply_count: Comment count
>     - remix_count: Remix count
>     - shared_by: Author user ID
>     - posted_at: Post timestamp
> - cursor: Next page parameter for fetching more data (null means last page)
>
> # [示例/Example]
> ```python
> # 使用作品 ID 查询第一页
> post_id = "s_68e466aa780c8191b"
>
> # 使用 cursor 获取下一页
> cursor = "eyJsYXN0X3Bvc3RfaWQiOiJzXzY4ZTQ2NmFhNzgwYzgxOTFiIn0="
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | 否 | 作品ID（可选）/Post ID (optional) | 无 | s_690acc0f4fcc8191ab5a75a96b6b6caf | 无 |
| post_url | query | string | 否 | 作品链接（可选）/Post URL (optional) | 无 | https://sora.chatgpt.com/p/s_690acc0f4fcc8191ab5a75a96b6b6caf | 无 |
| cursor | query | string | 否 | 翻页参数（可选）/Cursor for pagination (optional) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-task-detail"></a>
### `GET /api/u1/v1/sora2/get_task_detail`

- 摘要：[已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free)
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_task_detail_api_v1_sora2_get_task_detail_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io
> ### 用途:
> - **获取视频生成任务的完整作品详情，包含无水印版本的视频链接**
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - task_id: 任务 ID（可选），格式如 `task_01k7e17rnkeh79qnrcdwf5fcfs`
>     - 从 create_video 接口返回的任务 ID
>     - 必须以 'task_' 开头
> - generation_id: 生成 ID（可选），格式如 `gen_01k7e1bff9eq6rxe9pntk7xdcf`
>     - 从 get_task_status 接口返回的 generations[0].id
>     - 必须以 'gen_' 开头
> - **注意**: task_id 和 generation_id 至少需要提供一个
>
> ### 返回（无水印完整作品详情）:
> - post: 作品详细信息
>     - id: 作品 ID
>     - text: 作品描述文本
>     - attachments: 附件列表（**无水印视频信息**）
>         - **url: 无水印视频链接（原始质量）** ⭐
>         - downloadable_url: 有水印视频链接
>         - width/height: 视频尺寸
>         - encodings: 不同质量的编码版本
>             - **thumbnail: 缩略图（无水印）**
>             - **md: 中等质量视频（无水印）**
>             - **gif: 预览 GIF（无水印）**
>     - like_count: 点赞数
>     - view_count: 浏览数
>     - reply_count: 评论数
>     - remix_count: 混剪数
>     - posted_at: 发布时间戳
>     - permalink: 作品永久链接
>
> ### 注意:
> - **本接口返回的视频链接是无水印的原始质量版本**
> - 只有任务状态为 succeeded 时才能成功调用
> - 如果任务未完成，会返回相应的错误信息
> - 推荐使用 generation_id 参数
> - 视频链接有时效性，建议及时下载
>
> # [English]
> ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io
> ### Purpose:
> - **Get complete post details of video generation task, including watermark-free video links**
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - task_id: Task ID (optional), format like `task_01k7e17rnkeh79qnrcdwf5fcfs`
>     - Task ID returned from create_video endpoint
>     - Must start with 'task_'
> - generation_id: Generation ID (optional), format like `gen_01k7e1bff9eq6rxe9pntk7xdcf`
>     - Get from generations[0].id returned by get_task_status endpoint
>     - Must start with 'gen_'
> - **Note**: At least one of task_id or generation_id must be provided
>
> ### Return (Watermark-free Complete Post Details):
> - post: Post detailed information
>     - id: Post ID
>     - text: Post description text
>     - attachments: Attachment list (**Watermark-free video info**)
>         - **url: Watermark-free video link (original quality)** ⭐
>         - downloadable_url: Watermarked video link
>         - width/height: Video dimensions
>         - encodings: Different quality encoding versions
>             - **thumbnail: Thumbnail (watermark-free)**
>             - **md: Medium quality video (watermark-free)**
>             - **gif: Preview GIF (watermark-free)**
>     - like_count: Like count
>     - view_count: View count
>     - reply_count: Comment count
>     - remix_count: Remix count
>     - posted_at: Post timestamp
>     - permalink: Permanent link
>
> ### Note:
> - **This endpoint returns watermark-free original quality video links**
> - Can only be called successfully when task status is succeeded
> - Will return error message if task is not completed
> - Recommend using task_id parameter, will auto-fetch required generation_id
> - Video links have expiration time, recommend downloading promptly
>
> # [示例/Example]
> ```python
> # 返回示例 (无水印完整信息)
> # Return example (watermark-free complete info)
> {
>    "post":{
>       "id":"s_68ecb45b40988191b89a0af80135a33c",
>       "posted_to_public":false,
>       "posted_at":1760343131.252443,
>       "updated_at":1760343140.655776,
>       "like_count":0,
>       "recursive_reply_count":0,
>       "reply_count":0,
>       "view_count":0,
>       "unique_view_count":0,
>       "remix_count":0,
>       "user_liked":false,
>       "source":"sy",
>       "text":"A cat is playing Minecraft",
>       "caption":null,
>       "cover_photo_url":null,
>       "preview_image_url":"https://ogimg.chatgpt.com/?postId=s_68ecb45b40988191b89a0af80135a33c",
>       "attachments":[
>          {
>             "id":"s_68ecb45b40988191b89a0af80135a33c-attachment-0",
>             "tags":[
>                "sora"
>             ],
>             "kind":"sora",
>             "generation_id":"gen_01k7e9yzk2e4vr88ykfbtpz1ka",
>             "generation_type":"video_gen",
>             "url":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus",
>             "downloadable_url":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus",
>             "width":352,
>             "height":640,
>             "prompt":null,
>             "task_id":null,
>             "output_blocked":false,
>             "title":null,
>             "source":null,
>             "encodings":{
>                "source":{
>                   "path":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=NOaGqX50rV7s4Rrmpk8s0eJoHlhS3WHagn0Cz1wuDAM%3D&az=oaivgprodscus"
>                },
>                "source_wm":{
>                   "path":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000_wm%2Fsrc.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xiYmjG29NvQi9t5BGqu0tHl2%2BnRoA8eLNssPbLzmTxI%3D&az=oaivgprodscus"
>                },
>                "thumbnail":{
>                   "path":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fthumbnail.webp?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=qKQRiyaELAV9lr5B0mJ89vvHSptRXWrAvZHvSPLfBjc%3D&az=oaivgprodscus"
>                },
>                "unfurl":null,
>                "md":{
>                   "path":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fmd.mp4?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2FlBkZ6aqa8z6vwP2x%2FDezkCuM65t%2FM5vtglAEv85v5U%3D&az=oaivgprodscus"
>                },
>                "gif":{
>                   "path":"https://videos.openai.com/vg-assets/assets%2Ftask_01k7e9v8q3fvyaawqarkv00gpg%2Ftask_01k7e9v8q3fvyaawqarkv00gpg_genid_36b770af-8068-4bc3-b6c3-73339db3d241_25_10_13_08_10_919283%2Fvideos%2F00000%2Fpreview.gif?st=2025-10-13T06%3A42%3A42Z&se=2025-10-19T07%3A42%3A42Z&sks=b&skt=2025-10-13T06%3A42%3A42Z&ske=2025-10-19T07%3A42%3A42Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=mZsaMyviqaR13sMjZ3W8GAuFPHCYQA2BcPS5jwnIaDg%3D&az=oaivgprodscus"
>                }
>             },
>             "asset_pointer":null,
>             "conversation_id":null
>          }
>       ],
>       "parent_post_id":null,
>       "root_post_id":null,
>       "parent_path":null,
>       "tombstoned_at":null,
>       "permalink":"https://sora.chatgpt.com/p/s_68ecb45b40988191b89a0af80135a33c",
>       "text_facets":[
>
>       ],
>       "cameo_profiles":null,
>       "disabled_cameo_user_ids":null,
>       "groups":[
>
>       ],
>       "user_disliked":false,
>       "verifications":[
>
>       ],
>       "dislike_count":0,
>       "remix_posts":{
>          "items":[
>
>          ],
>          "cursor":null
>       },
>       "ancestors":{
>          "items":[
>
>          ],
>          "cursor":null
>       },
>       "parent_post":null,
>       "emoji":"🐱‍💻",
>       "is_featured":null
>    }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| task_id | query | string | 否 | 任务ID（可选，与generation_id二选一）/Task ID (optional, choose one with generation_id) | 无 | task_01k7e17rnkeh79qnrcdwf5fcfs | 无 |
| generation_id | query | string | 否 | 生成ID（可选，与task_id二选一）/Generation ID (optional, choose one with task_id) | 无 | gen_01k7e1bff9eq6rxe9pntk7xdcf | 无 |

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

<a id="get-api-u1-v1-sora2-get-task-status"></a>
### `GET /api/u1/v1/sora2/get_task_status`

- 摘要：[已弃用/Deprecated] 查询任务状态/Get task status
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_task_status_api_v1_sora2_get_task_status_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用。AI 相关接口已迁移至独立的 TikHub AI API 服务，与 TikHub 社交媒体 API 分离部署。请访问：https://ai.tikhub.io
> ### 用途:
> - 查询视频生成任务的当前状态和结果
> - 用于轮询检查视频生成进度
> - 任务完成后可获取生成的视频信息（包括 generation_id）
> - 配合 create_video 接口使用，用于获取异步生成的视频结果
>
> ### 收费说明:
> - 本接口完全免费，不消耗任何费用
> - 速率限制：每秒最多请求 1 次（1 request/second）
> - 如果请求过快可能会被限流，建议间隔至少 1 秒
>
> ### 参数:
> - task_id: 任务 ID，必填，格式如 `task_01k7dttf0xfx3t7zhhzycjq8e3`
>     - 从 create_video 接口返回的任务 ID
>     - 必须以 'task_' 开头
>
> ### 返回:
> - id: 任务 ID
> - status: 任务状态
>     - queued: 排队中
>     - processing: 处理中
>     - succeeded: 已完成
>     - failed: 失败
> - prompt: 视频生成时使用的文本描述
> - title: 视频标题（如果有）
> - progress_pct: 任务进度（0.0-1.0，1.0 表示 100%）
> - generations: 生成结果数组（任务完成后才有）
>     - id: 生成 ID（generation_id，格式：gen_xxxxxx）
>     - kind: 类型（如 sora_draft）
>     - url: 视频链接（有水印）
>     - downloadable_url: 下载链接（有水印）
>     - width: 视频宽度
>     - height: 视频高度
>     - created_at: 创建时间戳
>     - prompt: 生成提示词
>     - encodings: 不同质量的编码版本
>         - source: 源文件
>         - source_wm: 带水印的源文件
>         - thumbnail: 缩略图
>         - md: 中等质量视频
>         - gif: 预览 GIF
>
> ### 注意:
> - **速率限制**: 本接口每秒最多请求 1 次，建议轮询间隔设置为 1-2 秒
> - 建议每 1-2 秒轮询一次，直到 status 变为 succeeded 或 failed
> - 只有 status 为 succeeded 时，generations 数组才会包含视频数据
> - **重要**: 本接口返回的视频链接**只包含有水印的版本**
> - **获取无水印视频**: 当任务成功后，需要使用 task_id 或 generation_id 调用 `get_task_detail` 接口才能获取**无水印版本**
> - 从 generations[0].id 可以获取 generation_id，用于后续调用 get_task_detail 接口
>
> # [English]
> ## ⚠️ This endpoint has been deprecated. AI-related endpoints have been migrated to a dedicated TikHub AI API service, which operates separately from the TikHub Social Media API. Please visit: https://ai.tikhub.io
> ### Purpose:
> - Query current status and results of video generation task
> - Used to poll and check video generation progress
> - Get generated video information (including generation_id) after task completion
> - Use with create_video endpoint to get asynchronously generated video results
>
> ### Pricing:
> - This API is completely free, no charges
> - Rate limit: Maximum 1 request per second (1 request/second)
> - Requests may be throttled if too frequent, recommend at least 1 second interval
>
> ### Parameters:
> - task_id: Task ID, required, format like `task_01k7dttf0xfx3t7zhhzycjq8e3`
>     - Task ID returned from create_video endpoint
>     - Must start with 'task_'
>
> ### Return:
> - id: Task ID
> - status: Task status
>     - queued: Queued
>     - processing: Processing
>     - succeeded: Completed
>     - failed: Failed
> - prompt: Text description used for video generation
> - title: Video title (if any)
> - progress_pct: Task progress (0.0-1.0, 1.0 means 100%)
> - generations: Generation result array (available after task completion)
>     - id: Generation ID (generation_id, format: gen_xxxxxx)
>     - kind: Type (e.g., sora_draft)
>     - url: Video link (with watermark)
>     - downloadable_url: Download link (with watermark)
>     - width: Video width
>     - height: Video height
>     - created_at: Creation timestamp
>     - prompt: Generation prompt
>     - encodings: Different quality encoding versions
>         - source: Source file
>         - source_wm: Source file with watermark
>         - thumbnail: Thumbnail
>         - md: Medium quality video
>         - gif: Preview GIF
>
> ### Note:
> - **Rate limit**: Maximum 1 request per second, recommend polling interval of 1-2 seconds
> - Recommend polling every 1-2 seconds until status becomes succeeded or failed
> - Only when status is succeeded, generations array will contain video data
> - **Important**: This endpoint returns video links **with watermark only**
> - **Get watermark-free video**: After task succeeds, use task_id or generation_id to call `get_task_detail` endpoint to get **watermark-free version**
> - Get generation_id from generations[0].id for subsequent get_task_detail API call
>
> # [示例/Example]
> ```python
> # 返回示例（任务进行中）
> # Return example (task in progress)
> {
>     "id": "task_01k7dttf0xfx3t7zhhzycjq8e3",
>     "status": "processing",
>     "prompt": "A cat playing Minecraft",
>     "progress_pct": 0.45
> }
>
> # 返回示例（任务完成）
> # Return example (task completed)
> {
>     "id": "task_01k7dttf0xfx3t7zhhzycjq8e3",
>     "status": "succeeded",
>     "prompt": "A cat playing Minecraft",
>     "progress_pct": 1.0,
>     "generations": [
>         {
>             "id": "gen_01k7e1bff9eq6rxe9pntk7xdcf",
>             "kind": "sora_draft",
>             "url": "https://videos.openai.com/...",
>             "width": 640,
>             "height": 352,
>             "encodings": {
>                 "thumbnail": {"path": "https://..."},
>                 "gif": {"path": "https://..."}
>             }
>         }
>     ]
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| task_id | query | string | 是 | 任务ID（从create_video返回）/Task ID (returned from create_video) | 无 | task_01k7dttf0xfx3t7zhhzycjq8e3 | 无 |

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

<a id="get-api-u1-v1-sora2-get-user-cameo-appearances"></a>
### `GET /api/u1/v1/sora2/get_user_cameo_appearances`

- 摘要：获取用户Cameo出镜秀列表/Fetch user cameo appearances
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 用户的 Cameo 出镜秀列表
> - Cameo 出镜秀指该用户在其他创作者作品中的出镜视频
> - 支持分页加载，每页返回 30 条记录
> - 可用于展示用户的协作作品、出镜记录等
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - user_id: 用户 ID，必填
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - items: Cameo 出镜秀列表（30条/页）
>     - post: 作品信息（该用户出镜的作品）
>         - id: 作品 ID
>         - text: 作品描述
>         - attachments: 视频附件信息
>         - like_count: 点赞数
>         - view_count: 浏览数
>         - shared_by: 原创作者 ID
>         - posted_at: 发布时间戳
>     - profile: 原创作者信息
> - cursor: 下一页参数（用于获取更多记录，无更多时为 null）
> - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch Sora user's Cameo appearance list
> - Cameo appearances refer to videos where the user appears in other creators' works
> - Supports pagination, returns 30 records per page
> - Can be used to display user's collaborative works, appearance records, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - user_id: User ID, required
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - items: Cameo appearance list (30 items/page)
>     - post: Post information (works where the user appears)
>         - id: Post ID
>         - text: Post description
>         - attachments: Video attachment info
>         - like_count: Like count
>         - view_count: View count
>         - shared_by: Original creator ID
>         - posted_at: Post timestamp
>     - profile: Original creator information
> - cursor: Next page cursor (for loading more records, null when no more)
> - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 获取用户的 Cameo 出镜秀
> user_id = "user-xiCyLclE6KJcdTXyvVq3Ontc"
> cursor = ""  # 首次请求留空
>
> # 返回该用户在其他人作品中的出镜记录
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | user-xiCyLclE6KJcdTXyvVq3Ontc | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-user-followers"></a>
### `GET /api/u1/v1/sora2/get_user_followers`

- 摘要：获取用户粉丝列表/Fetch user followers
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_followers_api_v1_sora2_get_user_followers_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 用户的粉丝列表
> - 支持分页加载，每页返回 50 个粉丝
> - 可用于粉丝关系分析、社交网络研究等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - user_id: 用户 ID，必填
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - items: 粉丝列表（50个/页）
>     - user_id: 粉丝用户 ID
>     - username: 粉丝用户名
>     - display_name: 粉丝显示名称
>     - profile_picture_url: 粉丝头像链接
>     - follower_count: 粉丝的粉丝数
>     - following_count: 粉丝的关注数
>     - bio: 粉丝个人简介
>     - is_verified: 是否认证用户
> - cursor: 下一页参数（用于获取更多粉丝，无更多时为 null）
> - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch Sora user's follower list
> - Supports pagination, returns 50 followers per page
> - Can be used for follower relationship analysis, social network research, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - user_id: User ID, required
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - items: Follower list (50 items/page)
>     - user_id: Follower user ID
>     - username: Follower username
>     - display_name: Follower display name
>     - profile_picture_url: Follower avatar URL
>     - follower_count: Follower's follower count
>     - following_count: Follower's following count
>     - bio: Follower biography
>     - is_verified: Whether verified user
> - cursor: Next page cursor (for loading more followers, null when no more)
> - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 第一次请求（获取前 50 个粉丝）
> user_id = "user-xiCyLclE6KJcdTXyvVq3Ontc"
> cursor = ""  # 首次请求留空
>
> # 第二次请求（获取下一页）
> cursor = "eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi..."
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | user-xiCyLclE6KJcdTXyvVq3Ontc | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-user-following"></a>
### `GET /api/u1/v1/sora2/get_user_following`

- 摘要：获取用户关注列表/Fetch user following
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_following_api_v1_sora2_get_user_following_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 用户的关注列表（用户关注的其他人）
> - 支持分页加载，每页返回 50 个关注对象
> - 可用于关注关系分析、推荐算法等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - user_id: 用户 ID，必填
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - items: 关注列表（50个/页）
>     - user_id: 被关注用户 ID
>     - username: 被关注用户名
>     - display_name: 被关注用户显示名称
>     - profile_picture_url: 被关注用户头像链接
>     - follower_count: 被关注用户的粉丝数
>     - following_count: 被关注用户的关注数
>     - bio: 被关注用户个人简介
>     - is_verified: 是否认证用户
> - cursor: 下一页参数（用于获取更多关注，无更多时为 null）
> - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch Sora user's following list (users that the user follows)
> - Supports pagination, returns 50 following per page
> - Can be used for following relationship analysis, recommendation algorithms, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - user_id: User ID, required
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - items: Following list (50 items/page)
>     - user_id: Followed user ID
>     - username: Followed username
>     - display_name: Followed display name
>     - profile_picture_url: Followed avatar URL
>     - follower_count: Followed user's follower count
>     - following_count: Followed user's following count
>     - bio: Followed user biography
>     - is_verified: Whether verified user
> - cursor: Next page cursor (for loading more following, null when no more)
> - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 第一次请求（获取前 50 个关注）
> user_id = "user-BOXD64QrAyZVybLCeXTqJWm3"
> cursor = ""  # 首次请求留空
>
> # 第二次请求（获取下一页）
> cursor = "eyJ1c2VyX2lkIjoidXNlci1CT1hENjRRckF5WlZ5YkxDZVhUcUpXbTMi..."
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | user-BOXD64QrAyZVybLCeXTqJWm3 | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-user-posts"></a>
### `GET /api/u1/v1/sora2/get_user_posts`

- 摘要：获取用户发布的帖子列表/Fetch user posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_posts_api_v1_sora2_get_user_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 用户发布的作品列表
> - 支持分页加载，每页返回 30 条作品
> - 可用于用户主页展示、作品数据采集等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - user_id: 用户 ID，必填
> - cursor: 翻页参数（可选），首次请求留空，后续请求使用上一次响应中的 cursor 值
>
> ### 返回:
> - items: 作品列表（30条/页）
>     - post: 作品信息
>         - id: 作品 ID
>         - text: 作品描述
>         - attachments: 视频附件信息
>         - like_count: 点赞数
>         - view_count: 浏览数
>         - reply_count: 评论数
>         - posted_at: 发布时间戳
>     - profile: 作者信息
> - cursor: 下一页参数（用于获取更多作品，无更多时为 null）
> - has_more: 是否有更多数据
>
> # [English]
> ### Purpose:
> - Fetch list of posts published by a Sora user
> - Supports pagination, returns 30 posts per page
> - Can be used for user homepage display, post data collection, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - user_id: User ID, required
> - cursor: Pagination cursor (optional), leave empty for first request, use cursor from previous response for subsequent requests
>
> ### Return:
> - items: Post list (30 items/page)
>     - post: Post information
>         - id: Post ID
>         - text: Post description
>         - attachments: Video attachment info
>         - like_count: Like count
>         - view_count: View count
>         - reply_count: Comment count
>         - posted_at: Post timestamp
>     - profile: Author information
> - cursor: Next page cursor (for loading more posts, null when no more)
> - has_more: Whether there are more data
>
> # [示例/Example]
> ```python
> # 第一次请求（获取前 30 条作品）
> user_id = "user-xiCyLclE6KJcdTXyvVq3Ontc"
> cursor = ""  # 首次请求留空
>
> # 第二次请求（获取下一页）
> cursor = "eyJ1c2VyX2lkIjoidXNlci14aUN5TGNsRTZLSmNkVFh5dlZxM09udGMi..."
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | user-xiCyLclE6KJcdTXyvVq3Ontc | 无 |
| cursor | query | string | 否 | 翻页参数，从上一次响应中获取/Pagination cursor from previous response | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-sora2-get-user-profile"></a>
### `GET /api/u1/v1/sora2/get_user_profile`

- 摘要：获取用户信息档案/Fetch user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_profile_api_v1_sora2_get_user_profile_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 用户的个人信息档案
> - 包含用户基本信息、统计数据、社交关系等
> - 可用于用户资料展示、数据分析等场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - user_id: 用户 ID，必填，格式如 `user-xiCyLclE6KJcdTXyvVq3Ontc`
>
> ### 返回:
> - profile: 用户信息
>     - user_id: 用户 ID
>     - username: 用户名
>     - display_name: 显示名称
>     - bio: 个人简介
>     - profile_picture_url: 头像链接
>     - banner_image_url: 横幅图片链接
>     - follower_count: 粉丝数
>     - following_count: 关注数
>     - post_count: 作品数
>     - like_count: 获赞总数
>     - view_count: 浏览总数
>     - is_verified: 是否认证用户
>     - created_at: 账号创建时间戳
>     - social_links: 社交媒体链接（如有）
>
> # [English]
> ### Purpose:
> - Fetch Sora user's profile information
> - Includes user basic info, statistics, social relationships, etc.
> - Can be used for user profile display, data analysis, etc.
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - user_id: User ID, required, format like `user-xiCyLclE6KJcdTXyvVq3Ontc`
>
> ### Return:
> - profile: User information
>     - user_id: User ID
>     - username: Username
>     - display_name: Display name
>     - bio: Biography
>     - profile_picture_url: Avatar URL
>     - banner_image_url: Banner image URL
>     - follower_count: Follower count
>     - following_count: Following count
>     - post_count: Post count
>     - like_count: Total likes received
>     - view_count: Total views
>     - is_verified: Whether verified user
>     - created_at: Account creation timestamp
>     - social_links: Social media links (if any)
>
> # [示例/Example]
> ```python
> # 获取用户信息
> user_id = "user-xiCyLclE6KJcdTXyvVq3Ontc"
>
> # 返回示例
> {
>     "profile": {
>         "username": "creator123",
>         "display_name": "Amazing Creator",
>         "follower_count": 12500,
>         "post_count": 45
>     }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户ID/User ID | 无 | user-xiCyLclE6KJcdTXyvVq3Ontc | 无 |

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

<a id="get-api-u1-v1-sora2-get-video-download-info"></a>
### `GET /api/u1/v1/sora2/get_video_download_info`

- 摘要：获取无水印视频下载信息/Fetch none watermark video download info
- 能力：作品详情 / 下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_download_info_api_v1_sora2_get_video_download_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取 Sora 作品的简化下载信息，专为视频下载场景优化
> - 直接返回无水印视频链接和关键信息，无需解析复杂的完整数据
> - 适合需要快速下载视频的场景
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - post_id: 作品 ID（可选），格式如 `s_68e853d2ad448191b3c81e830f53c3a2`
> - post_url: 作品链接（可选），格式如 `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2`
> - **注意**: post_id 和 post_url 至少提供一个
>
> ### 返回:
> - post_id: 作品 ID
> - title: 作品描述文本
> - video: 视频信息
>     - no_watermark: 无水印视频链接（原始质量）
>     - watermark: 有水印视频链接
>     - width: 视频宽度
>     - height: 视频高度
>     - thumbnail: 缩略图链接
>     - preview_gif: 预览 GIF 链接
>     - medium_quality: 中等质量视频链接
> - author: 作者信息
>     - user_id: 用户 ID
>     - username: 用户名
>     - display_name: 显示名称
>     - avatar: 头像链接
> - stats: 统计数据
>     - like_count: 点赞数
>     - view_count: 浏览数
>     - comment_count: 评论数
>     - remix_count: 混剪数
> - permalink: 作品永久链接
> - created_at: 创建时间戳
>
> # [English]
> ### Purpose:
> - Get simplified download information for Sora posts, optimized for video download scenarios
> - Directly returns watermark-free video links and key information without parsing complex full data
> - Suitable for quick video download scenarios
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - post_id: Post ID (optional), format like `s_68e853d2ad448191b3c81e830f53c3a2`
> - post_url: Post URL (optional), format like `https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2`
> - **Note**: At least one of post_id or post_url must be provided
>
> ### Return:
> - post_id: Post ID
> - title: Post description text
> - video: Video information
>     - no_watermark: No watermark video link (original quality)
>     - watermark: Watermarked video link
>     - width: Video width
>     - height: Video height
>     - thumbnail: Thumbnail link
>     - preview_gif: Preview GIF link
>     - medium_quality: Medium quality video link
> - author: Author information
>     - user_id: User ID
>     - username: Username
>     - display_name: Display name
>     - avatar: Avatar URL
> - stats: Statistics
>     - like_count: Like count
>     - view_count: View count
>     - comment_count: Comment count
>     - remix_count: Remix count
> - permalink: Permanent link
> - created_at: Creation timestamp
>
> # [示例/Example]
> ```python
> # 使用作品 ID 查询
> post_id = "s_68e853d2ad448191b3c81e830f53c3a2"
>
> # 返回示例
> {
>     "video": {
>         "no_watermark": "https://cdn.openai.com/...",  # 直接下载此链接
>         "thumbnail": "https://cdn.openai.com/...",
>         "width": 1920,
>         "height": 1080
>     },
>     "title": "Amazing Sora video",
>     "author": {"username": "creator123"}
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | 否 | 作品ID（可选）/Post ID (optional) | 无 | s_68e853d2ad448191b3c81e830f53c3a2 | 无 |
| post_url | query | string | 否 | 作品链接（可选）/Post URL (optional) | 无 | https://sora.chatgpt.com/p/s_68e853d2ad448191b3c81e830f53c3a2 | 无 |

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

<a id="get-api-u1-v1-sora2-search-users"></a>
### `GET /api/u1/v1/sora2/search_users`

- 摘要：搜索用户/Search users
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_users_api_v1_sora2_search_users_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索 Sora 用户（主要用于 @ 提及功能）
> - 根据用户名关键词搜索匹配的用户
> - 返回用户信息和提及 Token（用于在评论中 @ 用户）
> - 注意：实际返回结果可能超过 20 个，比预期的更多
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.05 美元
> - 本接口支持使用免费额度，每天可通过在用户后台签到获取免费调用次数。
>
> ### 参数:
> - username: 搜索关键词，必填，支持部分匹配
>
> ### 返回:
> - items: 用户搜索结果列表
>     - profile: 用户信息
>         - user_id: 用户 ID
>         - username: 用户名
>         - display_name: 显示名称
>         - profile_picture_url: 头像链接
>         - follower_count: 粉丝数
>         - following_count: 关注数
>         - bio: 个人简介
>         - is_verified: 是否认证用户
>     - token: 提及 Token（用于 @ 提及功能）
>         - 格式：`<@user-xxxxxxxx>`
>         - 在评论中使用此 Token 可以提及该用户
>
> # [English]
> ### Purpose:
> - Search Sora users (mainly for @ mention functionality)
> - Search for matching users based on username keywords
> - Returns user information and mention tokens (for @mentioning users in comments)
> - Note: Actual results may exceed 20 users, more than expected
>
> ### Pricing:
> - This API costs $0.05 per request
> - This API supports free quota, you can get free requests by checking in daily at the user dashboard.
>
> ### Parameters:
> - username: Search keyword, required, supports partial matching
>
> ### Return:
> - items: User search result list
>     - profile: User information
>         - user_id: User ID
>         - username: Username
>         - display_name: Display name
>         - profile_picture_url: Avatar URL
>         - follower_count: Follower count
>         - following_count: Following count
>         - bio: Biography
>         - is_verified: Whether verified user
>     - token: Mention token (for @ mention functionality)
>         - Format: `<@user-xxxxxxxx>`
>         - Use this token in comments to mention the user
>
> # [示例/Example]
> ```python
> # 搜索用户名包含 "sam" 的用户
> username = "sam"
>
> # 返回示例
> {
>     "items": [
>         {
>             "profile": {
>                 "username": "samuel",
>                 "display_name": "Samuel Creator",
>                 "follower_count": 20000
>             },
>             "token": "<@user-abc123xyz>"
>         },
>         {
>             "profile": {
>                 "username": "samantha",
>                 "display_name": "Samantha Artist"
>             },
>             "token": "<@user-def456uvw>"
>         }
>     ]
> }
>
> # 在评论中使用 token 提及用户
> # comment_text = "Great work <@user-abc123xyz>!"
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | 搜索关键词（用户名）/Search keyword (username) | 无 | sam | 无 |

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

<a id="post-api-u1-v1-sora2-upload-image"></a>
### `POST /api/u1/v1/sora2/upload_image`

- 摘要：上传图片获取media_id/Upload image to get media_id
- 能力：媒体上传/公网URL
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`upload_image_api_v1_sora2_upload_image_post`

#### 说明

> # [中文]
> ### 用途:
> - 上传图片到 Sora 服务器获取 media_id
> - 获取的 media_id 可用于后续的 AI 视频生成功能
> - 支持 PNG、JPG、JPEG 格式的图片文件
>
> ### 收费说明:
> - 本接口请求价格为 1 次调用消耗 0.001 美元 （防止恶意请求）
> - 速率限制：每秒最多请求 1 次（1 request/second）
> - 如果请求过快可能会被限流，建议间隔至少 1 秒
>
> ### 参数说明:
> - **file** (必填): 图片文件
>   - 支持格式: PNG, JPG, JPEG
>   - 文件大小: 最大 10MB
>
> ### 返回数据:
> - **id**: Media ID（用于视频生成）
> - **url**: 图片访问链接
> - **kind**: 资源类型（通常为 "image"）
> - **width**: 图片宽度（像素）
> - **height**: 图片高度（像素）
> - **file_name**: 文件名
>
> ### 注意事项:
> - 上传的图片会存储在服务器上
> - 返回的 media_id 有效期通常为 24 小时
> - 建议在获取 media_id 后及时使用
> - 文件名会自动清理特殊字符以确保安全
>
> ---
>
> # [English]
> ### Purpose:
> - Upload image to Sora server to get media_id
> - The obtained media_id can be used for subsequent AI video generation
> - Supports PNG, JPG, JPEG format image files
>
> ### Pricing:
> - This API costs $0.001 per request (to prevent abuse requests)
> - Rate limit: Maximum 1 request per second
> - If requests are too frequent, you may be rate limited; it is recommended to wait at least 1 second between requests
>
> ### Parameters:
> - **file** (required): Image file
>   - Supported formats: PNG, JPG, JPEG
>   - File size: Maximum 10MB
>
> ### Response Data:
> - **id**: Media ID (for video generation)
> - **url**: Image access link
> - **kind**: Resource type (usually "image")
> - **width**: Image width (pixels)
> - **height**: Image height (pixels)
> - **file_name**: File name
>
> ### Notes:
> - Uploaded images are stored on the server
> - The returned media_id is usually valid for 24 hours
> - Recommend using media_id promptly after obtaining
> - File names are automatically sanitized for security
>
> ---
>
> # [示例/Example]
> ```python
> {
>    "id":"media_01k7edmn2ge988d9x6g5zg1hhw",
>    "type":"image",
>    "created_at":"2025-10-13T09:15:20.063403Z",
>    "filename":"20760448.jpeg",
>    "extension":"jpeg",
>    "mime_type":"image/jpeg",
>    "url":"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpeg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=3xnRz6u%2BJcO3Db7EAvDXkw08xDttCc5xSvvL2k2nEN8%3D&az=oaivgprodscus",
>    "width":460,
>    "height":460,
>    "duration_sec":null,
>    "n_frames":1,
>    "size_bytes":51902,
>    "thumbnail_url":"https://videos.openai.com/vg-assets/assets%2Fclient_upload%2Fmedia%2F084bcb820761572154494edb38c9ff2b4a3254fd%2Fmedia_01k7edmn2ge988d9x6g5zg1hhw.jpg?se=2025-10-13T10%3A15%3A20Z&sp=r&sv=2024-08-04&sr=b&skoid=8ffff87a-01f1-47c9-9090-32999d4d6380&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-13T08%3A24%3A12Z&ske=2025-10-13T12%3A29%3A12Z&sks=b&skv=2024-08-04&sig=chcnDmB%2BKipH%2BOAPHQGmZv8zCldny/U0HDtsvjuZoqA%3D&az=oaivgprodscus"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `multipart/form-data`

- Schema 摘要：`file*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| file | string(binary) | 是 | PNG/JPG/JPEG | 无 | 无 | 无 |

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
