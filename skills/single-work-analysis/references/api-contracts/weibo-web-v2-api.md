# Weibo-Web-V2-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/weibo-web-v2-api.md`](../api-tags/weibo-web-v2-api.md)
- 当前契约文件：`api-contracts/weibo-web-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`33`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(新浪微博 Web V2 数据接口/Weibo-Web-V2-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-weibo-web-v2-check-allow-comment-with-pic"></a>
### `GET /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic`

- 摘要：检查微博是否允许带图评论/Check if Weibo allows image comments
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get`

#### 说明

> # [中文]
> ### 用途:
> - 检查指定微博是否允许用户在评论时上传图片。
> ### 参数:
> - id: 微博ID（必填）
> ### 返回:
> - result: true表示允许带图评论，false表示不允许
> ### 注意:
> - 不同微博的图片评论权限可能不同
>
> # [English]
> ### Purpose:
> - Check if a specific Weibo post allows image comments.
> ### Parameters:
> - id: Weibo post ID (required)
> ### Return:
> - result: true means image comments allowed, false means not allowed
> ### Note:
> - Different posts may have different image comment permissions
>
> # [示例/Example]
> id = "5092682368025584"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | 是 | 微博ID/Weibo ID | 无 | 5092682368025584 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-advanced-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_advanced_search`

- 摘要：微博高级搜索/Weibo Advanced Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 微博高级搜索，支持多维度筛选。
> ### 参数:
> - q: 搜索关键词（必填）
> - search_type: 搜索类型（all/hot/original/verified/media/viewpoint）
> - include_type: 包含类型（all/pic/video/music/link）
> - timescope: 时间范围（格式: custom:开始日期:结束日期，如 custom:2025-09-01-0:2025-09-08-23）
> - page: 页码（默认1）
> ### 返回:
> - 搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等
> ### 注意:
> - 视频播放需设置请求头 Referer=https://weibo.com/
>
> # [English]
> ### Purpose:
> - Weibo advanced search with multi-dimensional filtering.
> ### Parameters:
> - q: Search keyword (required)
> - search_type: Search type (all/hot/original/verified/media/viewpoint)
> - include_type: Include type (all/pic/video/music/link)
> - timescope: Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23)
> - page: Page number (default 1)
> ### Return:
> - Search result list, including post content, author info, images, videos, interaction data
> ### Note:
> - Video playback requires setting header Referer=https://weibo.com/
>
> # [示例/Example]
> q = "python"
> search_type = "hot"
> include_type = "pic"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q | query | string | 是 | 搜索关键词/Search keyword | 无 | yu7 | 无 |
| search_type | query | string | 否 | 搜索类型/Search type: all(全部), hot(热门), original(原创), verified(认证用户), media(媒体), viewpoint(观点) | 无 | hot | 无 |
| include_type | query | string | 否 | 包含类型/Include type: all(全部), pic(含图片), video(含视频), music(含音乐), link(含短链) | 无 | pic | 无 |
| timescope | query | string | 否 | 时间范围/Time scope (custom:start:end) | 无 | custom:2025-09-01-0:2025-09-08-23 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-ai-related-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_ai_related_search`

- 摘要：微博AI搜索内容扩展/Weibo AI Search Content Extension
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取与关键词相关的内容扩展（相关问题、博主推荐、参考博文等）。
> ### 参数:
> - keyword: 搜索关键词（必填，建议使用话题格式#话题名#）
> ### 返回:
> - HTML格式的扩展内容，包含相关问题、博主推荐、参考博文等
> ### 注意:
> - 返回内容为HTML格式，需要进行HTML解析处理
> - HTML结构可能会发生变化，需要做好容错处理
>
> # [English]
> ### Purpose:
> - Get content extensions related to keyword (related questions, blogger recommendations, reference posts).
> ### Parameters:
> - keyword: Search keyword (required, recommend using topic format #TopicName#)
> ### Return:
> - HTML format extension content, including related questions, blogger recommendations, reference posts
> ### Note:
> - Returned content is in HTML format, requires HTML parsing
> - HTML structure may change, need proper error handling
>
> # [示例/Example]
> keyword = "#微博奇遇记#"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | #微博奇遇记# | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-ai-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_ai_search`

- 摘要：微博智能搜索/Weibo AI Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过微博AI智能搜索获取搜索结果。
> ### 参数:
> - query: 搜索关键词（必填，建议使用话题格式#话题名#）
> ### 返回:
> - AI搜索结果，包含推荐内容、相关话题等
> ### 注意:
> - AI搜索结果会根据用户行为进行个性化调整
>
> # [English]
> ### Purpose:
> - Get search results through Weibo AI intelligent search.
> ### Parameters:
> - query: Search keyword (required, recommend using topic format #TopicName#)
> ### Return:
> - AI search results, including recommended content, related topics
> ### Note:
> - AI search results are personalized based on user behavior
>
> # [示例/Example]
> query = "#法国#"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | #法国# | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-all-groups"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_all_groups`

- 摘要：获取所有分组信息/Get all groups information
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博平台的所有分组信息，包括默认分组和用户自定义分组。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 分组列表，包含分组ID、名称、容器ID等
> ### 注意:
> - 返回的gid和containerid可用于时间轴接口的参数
> - 分组信息变化不频繁，建议缓存
>
> # [English]
> ### Purpose:
> - Get all group information on Weibo platform, including default and user-defined groups.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Group list, including group ID, name, container ID, etc.
> ### Note:
> - Returned gid and containerid can be used as parameters for timeline API
> - Group information changes infrequently, recommend caching
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-city-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_city_list`

- 摘要：地区省市映射/Region City List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取地区省市映射数据，用于用户搜索等接口的地区筛选参数。
> ### 参数:
> - normalized: 是否返回标准化结构（默认True）
> ### 返回:
> - 省市映射数据，用于fetch_user_search等接口的region参数
> ### 注意:
> - 返回的编码格式为 custom:省代码:市代码，如 custom:11:1
>
> # [English]
> ### Purpose:
> - Get region city mapping data for region filter parameter in user search APIs.
> ### Parameters:
> - normalized: Whether to return normalized structure (default True)
> ### Return:
> - Province-city mapping data, for region parameter in fetch_user_search and other APIs
> ### Note:
> - Returned code format is custom:province_code:city_code, e.g. custom:11:1
>
> # [示例/Example]
> normalized = True

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| normalized | query | boolean | 否 | 是否返回标准化结构（省份列表+城市数组）/Whether to return normalized structure | true | 无 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-entertainment-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking`

- 摘要：获取微博文娱榜单/Get Weibo entertainment ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博文娱榜单数据（娱乐圈、影视、综艺等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 文娱话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get Weibo entertainment ranking data (entertainment, film & TV, variety shows).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Entertainment topic list, including topic, heat value, rank, category
> ### Note:
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-ranking-timeline"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline`

- 摘要：获取微博热门榜单时间轴/Get hot ranking timeline
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博平台各种类型的热门榜单内容。
> ### 参数:
> - ranking_type: 榜单类型（必填）
>     - hour: 小时榜
>     - yesterday: 昨日榜
>     - day_before: 前日榜
>     - week: 周榜
>     - male: 男榜
>     - female: 女榜
> - max_id: 翻页游标，首次请求传"0"
> - count: 获取数量（默认10）
> ### 返回:
> - 热门微博列表，包含微博内容、作者信息、互动数据等
> ### 注意:
> - 不同榜单更新频率不同：小时榜实时性最强，周榜影响力较大
>
> # [English]
> ### Purpose:
> - Get various types of hot ranking content from Weibo platform.
> ### Parameters:
> - ranking_type: Ranking type (required)
>     - hour: Hourly ranking
>     - yesterday: Yesterday ranking
>     - day_before: Day before ranking
>     - week: Weekly ranking
>     - male: Male ranking
>     - female: Female ranking
> - max_id: Pagination cursor, pass "0" for first request
> - count: Count (default 10)
> ### Return:
> - Hot post list, including post content, author info, interaction data
> ### Note:
> - Different rankings have different update frequencies: hourly has highest real-time relevance, weekly has high influence
>
> # [示例/Example]
> ranking_type = "hour"
> max_id = "0"
> count = 10

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ranking_type | query | string | 是 | 榜单类型：hour=小时榜，yesterday=昨日榜，day_before=前日榜，week=周榜，male=男榜，female=女榜/Ranking type: hour=hourly, yesterday=yesterday, day_before=day before, week=weekly, male=male ranking, female=… | 无 | hour | 无 |
| since_id | query | string | 否 | 分页标识，默认为0/Pagination identifier, default is 0 | 0 | 0 | 无 |
| max_id | query | string | 否 | 最大ID，默认为0/Max ID, default is 0 | 0 | 0 | 无 |
| count | query | integer | 否 | 获取数量，默认10/Count, default is 10 | 10 | 10 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search`

- 摘要：获取微博热搜榜单/Get Weibo hot search ranking
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博实时热搜榜单数据。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 热搜数据，包含realtime（实时热搜）、hotgov等多个板块
> ### 注意:
> - 热搜更新频繁，建议缓存2-5分钟
>
> # [English]
> ### Purpose:
> - Get Weibo real-time hot search ranking data.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Hot search data, including realtime (real-time hot search), hotgov and other sections
> ### Note:
> - Hot search updates frequently, recommend caching for 2-5 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search-index"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_index`

- 摘要：获取微博热搜词条(10条)/Get Weibo hot search index (10 items)
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get`

#### 说明

> # [中文]
> ### 用途:
> - 快速获取微博热搜前10条。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 热搜词条列表，包含关键词、热度值、排名等
> ### 注意:
> - 只返回前10条热搜
> - 热搜更新频繁，建议缓存2-5分钟
> - 如需完整热搜，使用fetch_hot_search_summary
>
> # [English]
> ### Purpose:
> - Quickly get top 10 Weibo hot search items.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Hot search term list, including keyword, popularity value, rank
> ### Note:
> - Only returns top 10 hot search items
> - Hot search updates frequently, recommend caching for 2-5 minutes
> - For complete hot search, use fetch_hot_search_summary
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search-summary"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_summary`

- 摘要：获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博完整热搜榜单（50条）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 完整热搜列表，包含排名、关键词、标签（热点/沸点/官宣/新）、热度值
> ### 注意:
> - 与fetch_hot_search_index的区别：本接口返回50条，fetch_hot_search_index返回10条
> - rank为0表示置顶内容
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get complete Weibo hot search ranking (50 items).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Complete hot search list, including rank, keyword, tag (Hot/Boiling/Official/New), heat value
> ### Note:
> - Difference from fetch_hot_search_index: this API returns 50 items, fetch_hot_search_index returns 10 items
> - rank 0 indicates pinned content
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-life-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_life_ranking`

- 摘要：获取微博生活榜单/Get Weibo life ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博生活榜单数据（美食、旅游、健康、时尚等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 生活话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get Weibo life ranking data (food, travel, health, fashion).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Life topic list, including topic, heat value, rank, category
> ### Note:
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-pic-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_pic_search`

- 摘要：图片搜索/Weibo picture search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索微博图片内容，按微博ID聚合多图。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 图片列表，包含微博ID、缩略图、原图链接、作者信息、图片数量
> ### 注意:
> - 缩略图会自动转换为原图链接
>
> # [English]
> ### Purpose:
> - Search Weibo picture content, aggregated by weibo ID.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Image list with weibo ID, thumbnail, large image URL, author info, image count
> ### Note:
> - Thumbnails are automatically converted to large image URLs
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | yu7 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-comments"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_comments`

- 摘要：获取微博评论/Get Weibo comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的一级评论列表。
> ### 参数:
> - id: 微博ID（必填）
> - count: 评论数量（默认10）
> - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值
> ### 返回:
> - 评论列表数据，包含评论内容、评论者信息、点赞数等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 当没有更多评论时，max_id 为空
>
> # [English]
> ### Purpose:
> - Get the first-level comment list of specified post.
> ### Parameters:
> - id: Weibo post ID (required)
> - count: Number of comments (default 10)
> - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests
> ### Return:
> - Comment list data, including comment content, commenter info, likes count
> - Contains max_id field for pagination
> ### Note:
> - When no more comments, max_id is empty
>
> # [示例/Example]
> id = "5188973773455957"
> count = 10
> max_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | 是 | 微博ID/Weibo ID | 无 | 5188973773455957 | 无 |
| count | query | integer | 否 | 评论数量/Number of comments | 10 | 10 | 无 |
| max_id | query | string | 否 | 页码/Page number | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-detail"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_detail`

- 摘要：获取单个作品数据/Get single post data
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的详细信息，包括内容、作者、互动数据等。
> ### 参数:
> - id: 微博ID（必填）
> - is_get_long_text: 是否获取长微博全文（默认"true"）
> ### 返回:
> - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等
>
> # [English]
> ### Purpose:
> - Get detailed information of a specific Weibo post, including content, author, interaction data.
> ### Parameters:
> - id: Weibo post ID (required)
> - is_get_long_text: Whether to get full text of long posts (default "true")
> ### Return:
> - Post detailed data, including full text, images, videos, likes, comments, reposts count
>
> # [示例/Example]
> id = "5092682368025584"
> is_get_long_text = "true"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | 是 | 作品id/Post id | 无 | 5092682368025584 | 无 |
| is_get_long_text | query | string | 否 | 是否获取长微博全文/Whether to get the full text of long Weibo posts (true/false) | true | true | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-sub-comments"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_sub_comments`

- 摘要：获取微博子评论/Get Weibo sub-comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定评论的回复（子评论）列表。
> ### 参数:
> - id: 主评论ID（必填）
> - count: 子评论数量（默认10）
> - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值
> ### 返回:
> - 子评论列表数据，包含回复内容、回复者信息、点赞数等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 与fetch_post_comments的区别：本接口获取的是评论的回复，而非微博的主评论
>
> # [English]
> ### Purpose:
> - Get the reply (sub-comment) list of a specified comment.
> ### Parameters:
> - id: Main comment ID (required)
> - count: Number of sub-comments (default 10)
> - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests
> ### Return:
> - Sub-comment list data, including reply content, replier info, likes count
> - Contains max_id field for pagination
> ### Note:
> - Difference from fetch_post_comments: this API gets replies to comments, not main comments of posts
>
> # [示例/Example]
> id = "5201793550385562"
> count = 10
> max_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | 是 | 主评论ID/Comment ID | 无 | 5201793550385562 | 无 |
| count | query | integer | 否 | 子评论数量/Number of sub-comments | 10 | 10 | 无 |
| max_id | query | string | 否 | 分页标识/Page identifier | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-realtime-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_realtime_search`

- 摘要：实时搜索/Weibo Realtime Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博实时搜索结果（按时间排序的最新微博）。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 实时搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等
> ### 注意:
> - 视频播放需设置请求头 Referer=https://weibo.com/
> - 返回结构与高级搜索一致
>
> # [English]
> ### Purpose:
> - Get Weibo realtime search results (latest posts sorted by time).
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Realtime search result list, including post content, author info, images, videos, interaction data
> ### Note:
> - Video playback requires setting header Referer=https://weibo.com/
> - Return structure is same as advanced search
>
> # [示例/Example]
> query = "苹果发布会"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | yu7 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-similar-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_similar_search`

- 摘要：获取微博相似搜索词推荐/Get Weibo similar search recommendations
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据关键词获取微博推荐的相似搜索词。
> ### 参数:
> - keyword: 搜索关键词（必填，支持话题标签格式如#话题名#）
> ### 返回:
> - 相似搜索词列表，包含推荐词、搜索次数等
> ### 注意:
> - 相似词推荐相对稳定，可缓存15-30分钟
>
> # [English]
> ### Purpose:
> - Get similar search word recommendations based on keyword.
> ### Parameters:
> - keyword: Search keyword (required, supports topic tag format like #TopicName#)
> ### Return:
> - Similar search term list, including suggestion, search count
> ### Note:
> - Similar word recommendations are relatively stable, can cache for 15-30 minutes
>
> # [示例/Example]
> keyword = "#微博奇遇记#"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | #微博奇遇记# | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-social-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_social_ranking`

- 摘要：获取微博社会榜单/Get Weibo social ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博社会榜单数据（时事新闻、社会热点、民生话题等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 社会话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 社会热点变化较快，建议缓存2-5分钟
>
> # [English]
> ### Purpose:
> - Get Weibo social ranking data (current affairs, social hotspots, livelihood topics).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Social topic list, including topic, heat value, rank, category
> ### Note:
> - Social hotspots change rapidly, recommend caching for 2-5 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-topic-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_topic_search`

- 摘要：话题搜索/Weibo topic search
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索微博话题，获取话题名称、封面、讨论量、阅读量。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 话题列表，包含话题名、封面图、讨论数、阅读数
> ### 注意:
> - 数量单位（万/亿）已转换为整数
>
> # [English]
> ### Purpose:
> - Search Weibo topics, get topic name, cover, discussion count, read count.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Topic list with topic name, cover image, discussion count, read count
> ### Note:
> - Count units (万/亿) are converted to integers
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | yu7 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-basic-info"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_basic_info`

- 摘要：获取用户基本信息/Get user basic information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博用户的基本信息（轻量级接口）。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 用户基本信息，包括用户ID、用户名、头像、简介、认证信息
> ### 注意:
> - 与fetch_user_info相比，本接口返回数据更少，响应更快
> - 适合批量用户信息获取和用户卡片展示
>
> # [English]
> ### Purpose:
> - Get basic information of Weibo users (lightweight API).
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - User basic info, including user ID, username, avatar, bio, verification
> ### Note:
> - Compared to fetch_user_info, this API returns less data with faster response
> - Suitable for batch user info retrieval and user card display
>
> # [示例/Example]
> uid = "7277477906"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id | 无 | 7277477906 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-fans"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_fans`

- 摘要：获取用户粉丝列表/Get user fans list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的粉丝列表（谁关注了该用户）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从0开始（默认0）
> ### 返回:
> - 粉丝用户列表，包含用户名、头像、简介、粉丝数等
> ### 注意:
> - 粉丝列表受用户隐私设置影响
> - page参数从0开始，而不是1
> - 与fetch_user_following的区别：本接口获取谁关注了该用户，fetch_user_following获取用户关注了谁
>
> # [English]
> ### Purpose:
> - Get the fans list of specified user (who follows the user).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 0 (default 0)
> ### Return:
> - Fans user list, including username, avatar, bio, followers count
> ### Note:
> - Fans list affected by user privacy settings
> - page parameter starts from 0, not 1
> - Difference from fetch_user_following: this API gets who follows the user, fetch_user_following gets who user follows
>
> # [示例/Example]
> uid = "1722594714"
> page = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID | 无 | 1722594714 | 无 |
| page | query | integer | 否 | 页码/Page number | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-following"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_following`

- 摘要：获取用户关注列表/Get user following list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的关注列表（该用户关注了谁）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从0开始（默认0）
> ### 返回:
> - 关注用户列表，包含用户名、头像、简介、粉丝数等
> ### 注意:
> - 关注列表受用户隐私设置影响
> - page参数从0开始，而不是1
> - 与fetch_user_fans的区别：本接口获取用户关注了谁，fetch_user_fans获取谁关注了该用户
>
> # [English]
> ### Purpose:
> - Get the following list of specified user (who the user follows).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 0 (default 0)
> ### Return:
> - Following user list, including username, avatar, bio, followers count
> ### Note:
> - Following list affected by user privacy settings
> - page parameter starts from 0, not 1
> - Difference from fetch_user_fans: this API gets who user follows, fetch_user_fans gets who follows the user
>
> # [示例/Example]
> uid = "1722594714"
> page = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID | 无 | 1722594714 | 无 |
| page | query | integer | 否 | 页码/Page number | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-info"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_info`

- 摘要：获取用户信息/Get user information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博用户的详细信息，包括昵称、头像、简介、关注数、粉丝数等。
> ### 参数:
> - uid: 用户ID（可选，与custom二选一）
> - custom: 自定义用户名（可选，与uid二选一）
> ### 返回:
> - 用户详细信息数据
> ### 注意:
> - uid和custom参数至少需要提供一个
> - 如果同时提供，优先使用uid
> - 建议优先使用uid参数
>
> # [English]
> ### Purpose:
> - Get detailed information of Weibo users, including nickname, avatar, bio, following count, followers count.
> ### Parameters:
> - uid: User ID (optional, choose one with custom)
> - custom: Custom username (optional, choose one with uid)
> ### Return:
> - User detailed information data
> ### Note:
> - At least one of uid and custom must be provided
> - If both provided, uid takes priority
> - It's recommended to use uid parameter first
>
> # [示例/Example]
> uid = "1722594714"
> # or
> custom = "shuqi"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 否 | 用户id/User id | 无 | 1722594714 | 无 |
| custom | query | string | 否 | 自定义微博用户名/Custom Weibo username | 无 | shuqi | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-original-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_original_posts`

- 摘要：获取微博用户原创微博数据/Get Weibo user original posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的原创微博列表（排除转发内容）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> - since_id: 翻页标识（第一页必须从fetch_user_posts接口获取）
> ### 返回:
> - 原创微博列表，包含微博内容、图片、视频、互动数据等
> ### 注意:
> - 与fetch_user_posts的区别：本接口只返回原创微博，排除转发
> - since_id必须先调用fetch_user_posts获取，第一页必传，后续页面不传
>
> # [English]
> ### Purpose:
> - Get original posts published by specified user (excluding reposts).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> - since_id: Pagination identifier (first page must get from fetch_user_posts)
> ### Return:
> - Original post list, including content, images, videos, interaction data
> ### Note:
> - Difference from fetch_user_posts: this API only returns original posts, excludes reposts
> - since_id must be obtained from fetch_user_posts first, required for first page, not needed for subsequent pages
>
> # [示例/Example]
> uid = "7277477906"
> page = 1
> since_id = "4924526881242703"  # from fetch_user_posts response

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id | 无 | 7277477906 | 无 |
| page | query | integer | 否 | 页数/Page number | 1 | 1 | 无 |
| since_id | query | string | 否 | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_posts`

- 摘要：获取微博用户文章数据/Get Weibo user posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的微博列表，支持分页和多种数据详细程度。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> - feature: 数据特征值（默认0）
>     - 0: 返回10条基础数据
>     - 1: 返回20条扩展数据
>     - 2: 返回20条图片相关数据
>     - 3: 返回20条完整数据
> - since_id: 翻页标识，用于获取下一页数据
> ### 返回:
> - 微博列表数据，包含微博内容、图片、视频等信息
> - 包含 since_id 字段用于翻页
> ### 注意:
> - feature=0性能最佳，feature=3数据最全
>
> # [English]
> ### Purpose:
> - Get the list of posts published by specified user, support pagination and multiple data detail levels.
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> - feature: Data feature value (default 0)
>     - 0: Return 10 basic posts
>     - 1: Return 20 extended posts
>     - 2: Return 20 image-related posts
>     - 3: Return 20 complete posts
> - since_id: Pagination identifier for next page
> ### Return:
> - Post list data, including post content, images, videos, etc.
> - Contains since_id field for pagination
> ### Note:
> - feature=0 has best performance, feature=3 has most complete data
>
> # [示例/Example]
> uid = "7277477906"
> page = 1
> feature = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id | 无 | 7277477906 | 无 |
| page | query | integer | 否 | 页数/Page number | 1 | 1 | 无 |
| feature | query | integer | 否 | 特征值，控制返回数据的数量和字段：0=返回10条基础数据，1=返回20条扩展数据，2=返回20条图片相关数据，3=返回20条视频相关数据，字段逐级增加/Feature type: 0=10 basic posts, 1=20 extended posts, 2=20 image-related posts, 3=20 video-related posts… | 0 | 0 | 无 |
| since_id | query | string | 否 | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-recommend-timeline"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline`

- 摘要：获取微博主页推荐时间轴/Get user recommend timeline
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博主页的推荐时间轴内容，基于用户兴趣展示个性化推荐。
> ### 参数:
> - refresh: 刷新类型（0=正常刷新，1=强制刷新）
> - group_id: 分组ID（可通过fetch_all_groups获取）
> - containerid: 容器ID（通常与group_id相同）
> - extparam: 扩展参数（默认"discover|new_feed"）
> - max_id: 翻页游标，首次请求传"0"
> - count: 获取数量（默认10，建议5-20）
> ### 返回:
> - 推荐微博列表，包含微博内容、作者信息、互动数据等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 建议先调用fetch_all_groups获取可用分组
>
> # [English]
> ### Purpose:
> - Get recommended timeline content from Weibo homepage, displaying personalized recommendations based on user interests.
> ### Parameters:
> - refresh: Refresh type (0=normal refresh, 1=force refresh)
> - group_id: Group ID (can be obtained through fetch_all_groups)
> - containerid: Container ID (usually same as group_id)
> - extparam: Extended parameters (default "discover|new_feed")
> - max_id: Pagination cursor, pass "0" for first request
> - count: Count (default 10, suggested 5-20)
> ### Return:
> - Recommended post list, including post content, author info, interaction data
> - Contains max_id field for pagination
> ### Note:
> - Recommend calling fetch_all_groups first to get available groups
>
> # [示例/Example]
> refresh = 0
> group_id = "102803"
> containerid = "102803"
> max_id = "0"
> count = 10

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refresh | query | integer | 否 | 刷新类型，0=正常刷新，1=强制刷新/Refresh type, 0=normal refresh, 1=force refresh | 0 | 0 | 无 |
| group_id | query | string | 否 | 分组ID/Group ID | 102803 | 102803 | 无 |
| containerid | query | string | 否 | 容器ID/Container ID | 102803 | 102803 | 无 |
| extparam | query | string | 否 | 扩展参数/Extended parameters | discover\|new_feed | discover\|new_feed | 无 |
| max_id | query | string | 否 | 最大ID/Max ID | 0 | 0 | 无 |
| count | query | integer | 否 | 获取数量/Count | 10 | 10 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_search`

- 摘要：用户搜索/User search
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索微博用户，支持多种筛选条件。
> ### 参数:
> - query: 搜索关键词（可选）
> - page: 页码（默认1）
> - region: 地区编码，从/fetch_city_list获取（可选）
> - auth: 认证类型 org_vip/per_vip/ord（可选）
> - gender: 性别 man/women（可选）
> - age: 年龄段 18y/22y/29y/39y/40y（可选）
> - nickname: 昵称筛选（可选）
> - tag: 标签筛选（可选）
> - school: 学校筛选（可选）
> - work: 公司筛选（可选）
> ### 返回:
> - 用户列表，包含uid、昵称、头像、粉丝数、主页链接
> ### 注意:
> - 筛选参数过多可能导致无结果
>
> # [English]
> ### Purpose:
> - Search Weibo users with multiple filter options.
> ### Parameters:
> - query: Search keyword (optional)
> - page: Page number (default 1)
> - region: Region code from /fetch_city_list (optional)
> - auth: Auth type org_vip/per_vip/ord (optional)
> - gender: Gender man/women (optional)
> - age: Age bucket 18y/22y/29y/39y/40y (optional)
> - nickname: Nickname filter (optional)
> - tag: Tag filter (optional)
> - school: School filter (optional)
> - work: Company filter (optional)
> ### Return:
> - User list with uid, nickname, avatar, fans count, profile URL
> ### Note:
> - Too many filters may result in no results
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 否 | 搜索关键词/Query（提供则视为“全部”搜索；留空则仅应用高级筛选参数） | 无 | yu7 | 无 |
| page | query | integer | 否 | 页码/Page | 1 | 1 | 无 |
| region | query | string | 否 | 地区编码，从 /city_list 获取/Region code from /city_list | 无 | custom:11:1 | 无 |
| auth | query | string | 否 | 认证类型 org_vip(机构)/per_vip(个人)/ord(普通)/Auth type | 无 | org_vip | 无 |
| gender | query | string | 否 | 性别 man / women / Gender | 无 | man | 无 |
| age | query | string | 否 | 年龄段 18y/22y/29y/39y/40y / Age bucket | 无 | 22y | 无 |
| nickname | query | string | 否 | 昵称筛选/Nickname filter | 无 | 张三 | 无 |
| tag | query | string | 否 | 标签筛选/Tag filter | 无 | 摄影 | 无 |
| school | query | string | 否 | 学校筛选/School filter | 无 | 清华大学 | 无 |
| work | query | string | 否 | 公司筛选/Company filter | 无 | 字节跳动 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-detail"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail`

- 摘要：获取用户微博视频收藏夹详情/Get user video collection detail
- 能力：主页/账号 / 作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定收藏夹的详细内容，包括视频列表。
> ### 参数:
> - cid: 收藏夹ID（必填，从fetch_user_video_collection_list获取）
> - cursor: 分页游标，首次请求传空，后续使用返回的cursor
> - tab_code: 排序方式（0=默认，1=最热，2=最新）
> ### 返回:
> - 收藏夹信息和视频列表，包含视频标题、封面、时长、播放数等
> - 包含 next_cursor 和 has_more 字段用于翻页
> ### 注意:
> - 不同排序方式的cursor不通用，切换排序需重新开始分页
>
> # [English]
> ### Purpose:
> - Get detailed content of specified collection, including video list.
> ### Parameters:
> - cid: Collection ID (required, get from fetch_user_video_collection_list)
> - cursor: Pagination cursor, pass empty for first request, use returned cursor for subsequent
> - tab_code: Sort type (0=default, 1=hottest, 2=latest)
> ### Return:
> - Collection info and video list, including video title, cover, duration, views
> - Contains next_cursor and has_more fields for pagination
> ### Note:
> - Cursors for different sorting methods are not universal, switching sorting requires restarting pagination
>
> # [示例/Example]
> cid = "4883992307236954"
> cursor = ""
> tab_code = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cid | query | string | 是 | 收藏夹ID/Collection ID | 无 | 4883992307236954 | 无 |
| cursor | query | string | 否 | 分页游标/Pagination cursor | 无 | 无 | 无 |
| tab_code | query | integer | 否 | 排序方式：0=默认，1=最热，2=最新/Sort type: 0=default, 1=hottest, 2=latest | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list`

- 摘要：获取用户微博视频收藏夹列表/Get user video collection list
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的视频收藏夹列表。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 收藏夹列表，包含收藏夹ID、名称、描述、视频数量等
> ### 注意:
> - 收藏夹列表受用户隐私设置影响
> - 部分用户可能没有创建视频收藏夹
>
> # [English]
> ### Purpose:
> - Get video collection list of specified user.
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - Collection list, including collection ID, name, description, video count
> ### Note:
> - Collection list affected by user privacy settings
> - Some users may not have created video collections
>
> # [示例/Example]
> uid = "7277477906"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID | 无 | 7277477906 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_list`

- 摘要：获取微博用户全部视频/Get user all videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的所有视频内容（瀑布流展示）。
> ### 参数:
> - uid: 用户ID（必填）
> - cursor: 翻页游标，初次请求传"0"，后续请求使用返回的next_cursor值
> ### 返回:
> - 视频列表数据，包含视频标题、封面、播放量等信息
> - 包含 next_cursor 和 has_more 字段用于翻页
> ### 注意:
> - 与收藏夹接口的区别：本接口获取用户发布的视频，收藏夹接口获取用户收藏的视频
>
> # [English]
> ### Purpose:
> - Get all videos published by specified user (waterfall layout).
> ### Parameters:
> - uid: User ID (required)
> - cursor: Pagination cursor, pass "0" for first request, use returned next_cursor for subsequent requests
> ### Return:
> - Video list data, including video title, cover, views, etc.
> - Contains next_cursor and has_more fields for pagination
> ### Note:
> - Difference from collection APIs: this API gets user published videos, collection APIs get user collected videos
>
> # [示例/Example]
> uid = "7277477906"
> cursor = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID | 无 | 7277477906 | 无 |
| cursor | query | string | 否 | 分页游标/Pagination cursor | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-video-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_video_search`

- 摘要：视频搜索（热门/全部）/Weibo video search (hot/all)
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索微博视频内容，支持热门和全部模式。
> ### 参数:
> - query: 搜索关键词（必填）
> - mode: 搜索模式 hot=热门 / all=全部（默认hot）
> - page: 页码（默认1）
> ### 返回:
> - 视频列表，包含微博ID、作者、内容、视频链接、互动数据
> ### 注意:
> - 播放视频需设置Referer=https://weibo.com/
>
> # [English]
> ### Purpose:
> - Search Weibo video content, supports hot and all modes.
> ### Parameters:
> - query: Search keyword (required)
> - mode: Search mode hot=popular / all=all (default hot)
> - page: Page number (default 1)
> ### Return:
> - Video list with weibo ID, author, content, video URL, interaction data
> ### Note:
> - Video playback requires setting Referer=https://weibo.com/
>
> # [示例/Example]
> query = "yu7"
> mode = "hot"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword | 无 | yu7 | 无 |
| mode | query | string | 否 | 搜索模式：hot=热门 / all=全部 | hot | hot | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-weibo-web-v2-search-user-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/search_user_posts`

- 摘要：搜索用户微博/Search user posts
- 能力：搜索 / 主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 在指定用户的微博中搜索包含特定关键词的内容。
> ### 参数:
> - uid: 用户ID（必填）
> - q: 搜索关键词（必填）
> - page: 页码，从1开始（默认1）
> - starttime: 开始时间戳（可选，Unix时间戳格式）
> - endtime: 结束时间戳（可选，Unix时间戳格式）
> - hasori: 是否包含原创（默认1包含）
> - hasret: 是否包含转发（默认1包含）
> - hastext: 是否包含文字（默认1包含）
> - haspic: 是否包含图片（默认1包含）
> - hasvideo: 是否包含视频（默认1包含）
> - hasmusic: 是否包含音乐（默认1包含）
> ### 返回:
> - 搜索结果列表，包含微博内容、作者信息、互动数据等
> ### 注意:
> - 搜索结果受用户隐私设置影响
> - 时间戳参数使用Unix时间戳格式
>
> # [English]
> ### Purpose:
> - Search for content containing specific keywords in a specified user's posts.
> ### Parameters:
> - uid: User ID (required)
> - q: Search keyword (required)
> - page: Page number, starts from 1 (default 1)
> - starttime: Start timestamp (optional, Unix timestamp format)
> - endtime: End timestamp (optional, Unix timestamp format)
> - hasori: Include original posts (default 1 include)
> - hasret: Include retweets (default 1 include)
> - hastext: Include text posts (default 1 include)
> - haspic: Include image posts (default 1 include)
> - hasvideo: Include video posts (default 1 include)
> - hasmusic: Include music posts (default 1 include)
> ### Return:
> - Search result list, including post content, author info, interaction data
> ### Note:
> - Search results affected by user privacy settings
> - Timestamp parameters use Unix timestamp format
>
> # [示例/Example]
> uid = "7277477906"
> q = "python"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID | 无 | 7277477906 | 无 |
| q | query | string | 是 | 搜索关键词/Search keyword | 无 | python | 无 |
| page | query | integer | 否 | 页数/Page number | 1 | 1 | 无 |
| starttime | query | integer | 是 | 开始时间戳/Start timestamp | 无 | 无 | 无 |
| endtime | query | integer | 是 | 结束时间戳/End timestamp | 无 | 无 | 无 |
| hasori | query | integer | 否 | 是否包含原创微博，1=包含，0=不包含/Include original posts, 1=include, 0=exclude | 1 | 1 | 无 |
| hasret | query | integer | 否 | 是否包含转发微博，1=包含，0=不包含/Include retweets, 1=include, 0=exclude | 1 | 1 | 无 |
| hastext | query | integer | 否 | 是否包含文字微博，1=包含，0=不包含/Include text posts, 1=include, 0=exclude | 1 | 1 | 无 |
| haspic | query | integer | 否 | 是否包含图片微博，1=包含，0=不包含/Include image posts, 1=include, 0=exclude | 1 | 1 | 无 |
| hasvideo | query | integer | 否 | 是否包含视频微博，1=包含，0=不包含/Include video posts, 1=include, 0=exclude | 1 | 1 | 无 |
| hasmusic | query | integer | 否 | 是否包含音乐微博，1=包含，0=不包含/Include music posts, 1=include, 0=exclude | 1 | 1 | 无 |

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
