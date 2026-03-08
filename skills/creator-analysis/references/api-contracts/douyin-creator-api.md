# Douyin-Creator-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-creator-api.md`](../api-tags/douyin-creator-api.md)
- 当前契约文件：`api-contracts/douyin-creator-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`16`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音创作者数据接口/Douyin-Creator-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-douyin-creator-fetch-creator-activity-detail"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_detail`

- 摘要：获取创作者活动详情/Get creator activity detail
- 能力：创作者 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者活动详情数据
> ### 参数:
> - activity_id: 活动ID（从活动列表接口获取）
> ### 返回:
> - 创作者活动详情数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator activity detail data
> ### Parameters:
> - activity_id: Activity ID (obtained from activity list interface)
> ### Return:
> - Creator activity detail data
>
> # [示例/Example]
> activity_id = "7545335931785450534"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| activity_id | query | string | 是 | 活动ID/Activity ID | 无 | 7545335931785450534 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-activity-list"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_list`

- 摘要：获取创作者活动列表/Get creator activity list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者活动列表数据
> ### 参数:
> - start_time: 开始时间戳
> - end_time: 结束时间戳
> ### 返回:
> - 创作者活动列表数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator activity list data
> ### Parameters:
> - start_time: Start timestamp
> - end_time: End timestamp
> ### Return:
> - Creator activity list data
>
> # [示例/Example]
> start_time = 1756656000
> end_time = 1759247999

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| start_time | query | integer | 是 | 开始时间戳/Start timestamp | 无 | 1756656000 | 无 |
| end_time | query | integer | 是 | 结束时间戳/End timestamp | 无 | 1759247999 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-content-category"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_content_category`

- 摘要：获取创作者内容创作合集分类/Get creator content creation category
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台内容创作的合集分类列表
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 内容创作合集分类数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator platform content creation category list
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Content creation category data

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-content-course"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_content_course`

- 摘要：获取创作者内容创作课程/Get creator content creation course
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台指定分类的内容创作课程
> ### 参数:
> - category_id: 分类ID (更多分类ID请通过内容创作合集分类接口获取)
>     常见分类ID示例:
>     - 184: 视频创作
>     - 185: 直播创作
>     - 186: 图文创作
>     - 188: 美食视频创作
>     - 180: 内容创作基础
> - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传)
> - limit: 每页数量 (建议24，范围1-100)
> - offset: 偏移量 (起始位置)
> ### 返回:
> - 指定分类的内容创作课程数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator platform content creation courses for specified category
> ### Parameters:
> - category_id: Category ID (for more category IDs, please refer to the content creation category interface)
>     Common category ID examples:
>     - 184: Video Creation
>     - 185: Live Streaming Creation
>     - 186: Image & Text Creation
>     - 188: Food Video Creation
>     - 180: Content Creation Basics
> - order: Order type (1=recommended order, 2=most popular, 3=latest upload)
> - limit: Items per page (recommended 24, range 1-100)
> - offset: Offset (starting position)
> ### Return:
> - Content creation course data for specified category

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category_id | query | integer | 是 | 分类ID/Category ID | 无 | 180 | 无 |
| order | query | integer | 否 | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) | 1 | 1 | 无 |
| limit | query | integer | 否 | 每页数量/Items per page | 24 | 24 | 无 |
| offset | query | integer | 否 | 偏移量/Offset (starting position) | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-challenge-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard`

- 摘要：获取创作者热门挑战榜单/Get creator hot challenge billboard
- 能力：热点/榜单 / 创作者 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台热门挑战榜单数据
> ### 返回:
> - 热门挑战榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator platform hot challenge billboard data
> ### Return:
> - Hot challenge billboard data
>
> # [示例/Example]
> 无需参数，直接调用即可获取当前热门挑战榜单
> No parameters required, call directly to get current hot challenge billboard

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-course"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_course`

- 摘要：获取创作者热门课程/Get creator hot course
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台热门课程数据或精选专题课程
> ### 参数:
> - order: 排序方式 (1=推荐排序, 2=最受欢迎, 3=最新上传)
> - limit: 每页数量 (建议24，范围1-100)
> - offset: 偏移量 (起始位置)
> - category_id: 精选专题分类ID (不传则获取热门课程，传入则获取指定分类的精选专题)
>     可选值:
>     - 6976547830546582816: 知识品类
>     - 6976547923849006336: 生活品类
>     - 6976547940311633165: 娱乐品类
>     - 6976547972108635404: 美食品类
>     - 6980288134957272352: 正能量
>     - 6980288181744766219: 游戏品类
>     - 6980288219548011776: 通用
> ### 返回:
> - 热门课程数据或精选专题课程数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator platform hot course data or selected topic courses
> ### Parameters:
> - order: Order type (1=recommended order, 2=most popular, 3=latest upload)
> - limit: Items per page (recommended 24, range 1-100)
> - offset: Offset (starting position)
> - category_id: Selected topic category ID (empty for hot courses, specific ID for selected topics)
>     Available values:
>     - 6976547830546582816: Knowledge Category
>     - 6976547923849006336: Life Category
>     - 6976547940311633165: Entertainment Category
>     - 6976547972108635404: Food Category
>     - 6980288134957272352: Positive Energy
>     - 6980288181744766219: Gaming Category
>     - 6980288219548011776: General
> ### Return:
> - Hot course data or selected topic course data
>
> # [示例/Example]
> ```
> # 获取热门课程/Get hot courses
> GET /fetch_creator_hot_course?order=1&limit=24&offset=0
>
> # 获取知识品类精选专题/Get knowledge category selected topics
> GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547830546582816
>
> # 获取美食品类精选专题/Get food category selected topics
> GET /fetch_creator_hot_course?order=1&limit=24&offset=0&category_id=6976547972108635404
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| order | query | integer | 否 | 排序方式/Order type (1=推荐排序, 2=最受欢迎, 3=最新上传) | 1 | 1 | 无 |
| limit | query | integer | 否 | 每页数量/Items per page (建议24) | 24 | 24 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 0 | 无 |
| category_id | query | string | 否 | 精选专题分类ID/Selected topic category ID - 不传则为热门课程，传入则为精选专题 可选值/Available values: 6976547830546582816=知识品类, 6976547923849006336=生活品类, 6976547940311633165=娱乐品类, 6976547972108635404=美食品… | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-music-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard`

- 摘要：获取创作者热门音乐榜单/Get creator hot music billboard
- 能力：热点/榜单 / 创作者 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台热门音乐榜单数据
> ### 参数:
> - billboard_tag: 榜单标签，0=全部，其他值请通过配置接口获取
> - order_key: 排序键 (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多)
> - time_filter: 时间筛选 (1=24小时, 2=7天, 3=30天)
> ### 返回:
> - 热门音乐榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator platform hot music billboard data
> ### Parameters:
> - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface
> - order_key: Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions)
> - time_filter: Time filter (1=24 hours, 2=7 days, 3=30 days)
> ### Return:
> - Hot music billboard data
>
> # [示例/Example]
> billboard_tag = 0   # 全部/All
> order_key = 1   # 播放最高/Highest views
> time_filter = 1 # 24小时/24 hours

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签/Billboard tag (0=全部，具体分类值可通过配置接口获取) | 0 | 0 | 无 |
| order_key | query | integer | 否 | 排序键/Order key (1=播放最高, 2=点赞最多, 4=热度最高, 5=投稿最多) | 1 | 1 | 无 |
| time_filter | query | integer | 否 | 时间筛选/Time filter (1=24小时, 2=7天, 3=30天) | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-props-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard`

- 摘要：获取创作者热门道具榜单/Get creator hot props billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者热门道具榜单数据
> ### 参数:
> - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取
>     - 0: 全部
>     - 333: 美食
>     - 334: 旅行
>     - 299: 泛生活
>     - 335: 汽车
>     - 336: 科技
>     - 302: 游戏
>     - 296: 二次元
>     - 337: 娱乐
>     - 311: 明星
>     - 298: 体育
>     - 300: 文化教育
>     - 301: 校园
>     - 297: 政务
>     - 305: 时尚
>     - 306: 才艺
>     - 669: 财经
>     - 314: 随拍
>     - 307: 动植物
>     - 309: 图文控
>     - 308: 剧情
>     - 315: 亲子
>     - 718: 三农
>     - 310: 创意
>     - 312: 户外
>     - 926: 公益
> - order_key: 排序键
>     - 1: 播放最高
>     - 5: 投稿最多
>     - 6: 展现最高
>     - 7: 收藏最高
> - time_filter: 时间筛选
>     - 1: 24小时
>     - 2: 7天
>     - 3: 30天
> ### 返回:
> - 创作者热门道具榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator hot props billboard data
> ### Parameters:
> - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface
>     - 0: All
>     - 333: Food
>     - 334: Travel
>     - 299: Lifestyle
>     - 335: Automotive
>     - 336: Technology
>     - 302: Gaming
>     - 296: Anime
>     - 337: Entertainment
>     - 311: Celebrity
>     - 298: Sports
>     - 300: Culture & Education
>     - 301: Campus
>     - 297: Government
>     - 305: Fashion
>     - 306: Talent Show
>     - 669: Finance
>     - 314: Random
>     - 307: Animals & Plants
>     - 309: Graphics & Text
>     - 308: Drama
>     - 315: Parenting
>     - 718: Agriculture
>     - 310: Creative
>     - 312: Outdoor
>     - 926: Public Welfare
> - order_key: Order key
>     - 1: Highest views
>     - 5: Most submissions
>     - 6: Highest exposure
>     - 7: Most favorites
> - time_filter: Time filter
>     - 1: 24 hours
>     - 2: 7 days
>     - 3: 30 days
> ### Return:
> - Creator hot props billboard data
>
> # [示例/Example]
> billboard_tag = 0
> order_key = 1  # 播放最高/Highest views
> time_filter = 1  # 24小时/24 hours

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface | 0 | 无 | 无 |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 5=投稿最多, 6=展现最高, 7=收藏最高/Order key: 1=highest views, 5=most submissions, 6=highest exposure, 7=most favorites | 1 | 无 | 无 |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-spot-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard`

- 摘要：获取创作者中心创作热点/Get creator hot spot billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者热点榜单数据
> ### 参数:
> - billboard_tag: 热点标签，多个标签用逗号分隔
>     可选值:
>     - 站内玩法: 1004,1000,1002,1003,1001
>     - 话题互动: 20001,20006,20000,20003,20005,20002,20
>     - 娱乐: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006
>     - 社会: 4005,4006,4007,4003,4004,4000
>     - 二次元: 13000
>     - 交通: 23000
>     - 亲子: 19000
>     - 体育: 5002,5000,5001
>     - 军事: 21000
>     - 剧情: 18000
>     - 动物萌宠: 8000
>     - 天气: 22001,22002
>     - 才艺: 17000
>     - 文化教育: 14000
>     - 旅行: 10000
>     - 时尚: 16000
>     - 时政: 3000,3001,3002
>     - 校园: 15000
>     - 汽车: 11000
>     - 游戏: 12000,12001
>     - 科技: 6000
>     - 美食: 9000
>     - 财经: 7000
> - hot_search_type: 热搜类型
>     - 1: 热点总榜
>     - 2: 同城热点榜
>     - 3: 热点上升榜
> - city_code: 城市代码，当hot_search_type=2时必需
> ### 返回:
> - 创作者热点榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator hot spot billboard data
> ### Parameters:
> - billboard_tag: Hot spot tag - multiple tags separated by comma
>     Available values:
>     - Platform Features: 1004,1000,1002,1003,1001
>     - Topic Interaction: 20001,20006,20000,20003,20005,20002,20
>     - Entertainment: 2007,2000,2011,2012,2009,2010,2004,2005,2003,2008,2001,2002,2006
>     - Society: 4005,4006,4007,4003,4004,4000
>     - Anime: 13000
>     - Transportation: 23000
>     - Parenting: 19000
>     - Sports: 5002,5000,5001
>     - Military: 21000
>     - Drama: 18000
>     - Animals & Pets: 8000
>     - Weather: 22001,22002
>     - Talent Show: 17000
>     - Culture & Education: 14000
>     - Travel: 10000
>     - Fashion: 16000
>     - Politics: 3000,3001,3002
>     - Campus: 15000
>     - Automotive: 11000
>     - Gaming: 12000,12001
>     - Technology: 6000
>     - Food: 9000
>     - Finance: 7000
> - hot_search_type: Hot search type
>     - 1: Hot Spot Overall Ranking
>     - 2: Local Hot Spot Ranking
>     - 3: Rising Hot Spot Ranking
> - city_code: City code - required when hot_search_type=2
> ### Return:
> - Creator hot spot billboard data
>
> # [示例/Example]
> billboard_tag = "0"  # 全部/All
> hot_search_type = 1  # 热点总榜/Overall ranking
> city_code = None  # 可选/Optional

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_tag | query | string | 否 | 热点标签，多个标签用逗号分隔，如'1004,1000,1002'/Hot spot tag - multiple tags separated by comma, like '1004,1000,1002' | 0 | 无 | 无 |
| hot_search_type | query | integer | 否 | 热搜类型: 1=热点总榜, 2=同城热点榜, 3=热点上升榜/Hot search type: 1=Overall ranking, 2=Local ranking, 3=Rising ranking | 1 | 无 | 无 |
| city_code | query | string | 否 | 城市代码，当hot_search_type=2时必需/City code - required when hot_search_type=2 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-hot-topic-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard`

- 摘要：获取创作者热门话题榜单/Get creator hot topic billboard
- 能力：热点/榜单 / 创作者 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者热门话题榜单数据
> ### 参数:
> - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取
>     - 0: 全部
>     - 333: 美食
>     - 334: 旅行
>     - 299: 泛生活
>     - 335: 汽车
>     - 336: 科技
>     - 302: 游戏
>     - 296: 二次元
>     - 337: 娱乐
>     - 311: 明星
>     - 298: 体育
>     - 300: 文化教育
>     - 301: 校园
>     - 297: 政务
>     - 305: 时尚
>     - 306: 才艺
>     - 669: 财经
>     - 314: 随拍
>     - 307: 动植物
>     - 309: 图文控
>     - 308: 剧情
>     - 315: 亲子
>     - 718: 三农
>     - 310: 创意
>     - 312: 户外
>     - 926: 公益
> - order_key: 排序键
>     - 1: 播放最高
>     - 2: 点赞最多
>     - 3: 评论最多
>     - 4: 投稿最多
> - time_filter: 时间筛选
>     - 1: 24小时
>     - 2: 7天
>     - 3: 30天
> ### 返回:
> - 创作者热门话题榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator hot topic billboard data
> ### Parameters:
> - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface
>     - 0: All
>     - 333: Food
>     - 334: Travel
>     - 299: Lifestyle
>     - 335: Automotive
>     - 336: Technology
>     - 302: Gaming
>     - 296: Anime
>     - 337: Entertainment
>     - 311: Celebrity
>     - 298: Sports
>     - 300: Culture & Education
>     - 301: Campus
>     - 297: Government
>     - 305: Fashion
>     - 306: Talent Show
>     - 669: Finance
>     - 314: Random
>     - 307: Animals & Plants
>     - 309: Graphics & Text
>     - 308: Drama
>     - 315: Parenting
>     - 718: Agriculture
>     - 310: Creative
>     - 312: Outdoor
>     - 926: Public Welfare
> - order_key: Order key
>     - 1: Highest views
>     - 2: Most likes
>     - 3: Most comments
>     - 4: Most submissions
> - time_filter: Time filter
>     - 1: 24 hours
>     - 2: 7 days
>     - 3: 30 days
> ### Return:
> - Creator hot topic billboard data
>
> # [示例/Example]
> billboard_tag = 0
> order_key = 1  # 播放最高/Highest views
> time_filter = 1  # 24小时/24 hours

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface | 0 | 无 | 无 |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=投稿最多/Order key: 1=highest views, 2=most likes, 3=most comments, 4=most submissions | 1 | 无 | 无 |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-material-center-billboard"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard`

- 摘要：获取创作者中心热门视频榜单/Get creator material center billboard
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者中心热门视频榜单数据
> ### 参数:
> - billboard_tag: 榜单标签，0=全部，其他值请通过config接口获取
>     - 0: 全部
>     - 333: 美食
>     - 334: 旅行
>     - 299: 泛生活
>     - 335: 汽车
>     - 336: 科技
>     - 302: 游戏
>     - 296: 二次元
>     - 337: 娱乐
>     - 311: 明星
>     - 298: 体育
>     - 300: 文化教育
>     - 301: 校园
>     - 297: 政务
>     - 305: 时尚
>     - 306: 才艺
>     - 669: 财经
>     - 314: 随拍
>     - 307: 动植物
>     - 309: 图文控
>     - 308: 剧情
>     - 315: 亲子
>     - 718: 三农
>     - 310: 创意
>     - 312: 户外
>     - 926: 公益
> - order_key: 排序键
>     - 1: 播放最高
>     - 2: 点赞最多
>     - 3: 评论最多
>     - 4: 热度最高
> - time_filter: 时间筛选
>     - 1: 24小时
>     - 2: 7天
>     - 3: 30天
> ### 返回:
> - 创作者中心热门视频榜单数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator material center billboard data
> ### Parameters:
> - billboard_tag: Billboard tag, 0=all, other values can be obtained through config interface
>     - 0: All
>     - 333: Food
>     - 334: Travel
>     - 299: Lifestyle
>     - 335: Automotive
>     - 336: Technology
>     - 302: Gaming
>     - 296: Anime
>     - 337: Entertainment
>     - 311: Celebrity
>     - 298: Sports
>     - 300: Culture & Education
>     - 301: Campus
>     - 297: Government
>     - 305: Fashion
>     - 306: Talent Show
>     - 669: Finance
>     - 314: Random
>     - 307: Animals & Plants
>     - 309: Graphics & Text
>     - 308: Drama
>     - 315: Parenting
>     - 718: Agriculture
>     - 310: Creative
>     - 312: Outdoor
>     - 926: Public Welfare
> - order_key: Order key
>     - 1: Highest views
>     - 2: Most likes
>     - 3: Most comments
>     - 4: Highest popularity
> - time_filter: Time filter
>     - 1: 24 hours
>     - 2: 7 days
>     - 3: 30 days
> ### Return:
> - Creator material center billboard data
>
> # [示例/Example]
> billboard_tag = 0
> order_key = 1  # 播放最高/Highest views
> time_filter = 1  # 24小时/24 hours

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| billboard_tag | query | integer | 否 | 榜单标签，0=全部，其他值请通过config接口获取/Billboard tag, 0=all, other values can be obtained through config interface | 0 | 无 | 无 |
| order_key | query | integer | 否 | 排序键: 1=播放最高, 2=点赞最多, 3=评论最多, 4=热度最高/Order key: 1=highest views, 2=most likes, 3=most comments, 4=highest popularity | 1 | 无 | 无 |
| time_filter | query | integer | 否 | 时间筛选: 1=24小时, 2=7天, 3=30天/Time filter: 1=24 hours, 2=7 days, 3=30 days | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-creator-material-center-config"></a>
### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_config`

- 摘要：获取创作者中心配置/Get creator material center config
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者中心配置信息
> ### 返回:
> - 创作者中心配置数据
>
> # [English]
> ### Purpose:
> - Get Douyin creator material center configuration
> ### Return:
> - Creator material center config data

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

<a id="get-api-u1-v1-douyin-creator-fetch-industry-category-config"></a>
### `GET /api/u1/v1/douyin/creator/fetch_industry_category_config`

- 摘要：获取行业分类配置/Get industry category config
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台的行业分类配置
> - 返回所有可用的行业分类层级结构
> - **建议在调用商单任务列表接口前先调用此接口获取完整的行业分类信息**
>
> ### 重要说明:
> - 此接口已优化为Redis缓存，首次调用后数据将缓存30天
> - 缓存键: `douyin_creator:industry_categories`
> - 数据结构包含一级行业和二级行业的完整映射关系
>
> ### 数据结构:
> ```json
> {
>     "status_code": 0,
>     "status_msg": "success",
>     "data": {
>         "industry_categories": [
>             {"key": "-1", "label": "全部"},
>             {"key": 1901, "label": "3C及电器"},
>             {"key": 1913, "label": "游戏"},
>             ...
>         ],
>         "industry_subcategories": {
>             1913: [
>                 {"key": "-1", "label": "全部"},
>                 {"key": 191301, "label": "休闲游戏"},
>                 {"key": 191302, "label": "棋牌桌游"},
>                 ...
>             ],
>             ...
>         }
>     }
> }
> ```
>
> ### 在商单任务筛选中的使用:
> 1. **获取全部行业任务**: `industry_lv1=-1` (此时industry_lv2无需设置)
> 2. **获取特定一级行业**: `industry_lv1=1913` (游戏行业)
> 3. **获取特定二级行业**: `industry_lv1=1913&industry_lv2=191301` (游戏-休闲游戏)
>
> ### 性能优化:
> - 首次调用时从本地JSON文件读取并缓存到Redis
> - 后续调用直接从Redis缓存读取，大幅提升响应速度
> - 缓存有效期30天，确保数据时效性
>
> ### 返回:
> - 返回完整的行业分类树结构
> - 包含32个一级行业分类和对应的二级行业分类
> - 每个分类包含分类ID(key)和名称(label)
>
> # [English]
> ### Purpose:
> - Get industry category configuration from Douyin Creator platform
> - Returns all available industry classification hierarchy
> - **Recommend calling this API first before using mission task list API to get complete industry classification info**
>
> ### Important Notes:
> - This API is optimized with Redis caching, data will be cached for 30 days after first call
> - Cache key: `douyin_creator:industry_categories`
> - Data structure contains complete mapping relationship between primary and secondary industries
>
> ### Data Structure:
> ```json
> {
>     "status_code": 0,
>     "status_msg": "success",
>     "data": {
>         "industry_categories": [
>             {"key": "-1", "label": "All"},
>             {"key": 1901, "label": "3C & Electronics"},
>             {"key": 1913, "label": "Gaming"},
>             ...
>         ],
>         "industry_subcategories": {
>             1913: [
>                 {"key": "-1", "label": "All"},
>                 {"key": 191301, "label": "Casual Games"},
>                 {"key": 191302, "label": "Board Games"},
>                 ...
>             ],
>             ...
>         }
>     }
> }
> ```
>
> ### Usage in Mission Task Filtering:
> 1. **Get all industry tasks**: `industry_lv1=-1` (industry_lv2 not needed)
> 2. **Get specific primary industry**: `industry_lv1=1913` (Gaming industry)
> 3. **Get specific secondary industry**: `industry_lv1=1913&industry_lv2=191301` (Gaming-Casual Games)
>
> ### Performance Optimization:
> - First call reads from local JSON file and caches to Redis
> - Subsequent calls read directly from Redis cache, significantly improving response speed
> - Cache validity period of 30 days ensures data timeliness
>
> ### Return:
> - Returns complete industry classification tree structure
> - Contains 32 primary industry categories and corresponding secondary industry categories
> - Each category contains category ID(key) and name(label)

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

<a id="get-api-u1-v1-douyin-creator-fetch-mission-task-list"></a>
### `GET /api/u1/v1/douyin/creator/fetch_mission_task_list`

- 摘要：获取商单任务列表/Get mission task list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者平台的商单任务列表
> - 支持多种筛选条件，包括行业分类、付费类型、平台渠道等
>
> ### 重要参数使用说明:
> #### 行业分类组合规则:
> - **industry_lv1=-1 (全部)**: 当选择全部一级行业时，industry_lv2参数将被忽略，无需设置
> - **industry_lv1=具体值**: 当选择具体一级行业时，可配合industry_lv2进行二级筛选
>     - industry_lv2=-1: 该一级行业下的所有二级分类
>     - industry_lv2=具体值: 该一级行业下的具体二级分类
>
> #### 可选参数 (选择"全部"时无需传入):
> - **platform_channel**: 不传入表示全部平台渠道
> - **pay_type**: 不传入表示全部付费类型
> - **greater_than_cost_progress**: 不传入表示不限制成本进度
> - **publish_time_start**: 不传入表示不限制发布时间
> - **quick_selector_scene**: 不传入表示不使用快速筛选
> - **keyword**: 不传入表示不进行关键词搜索
>
> ### 参数详解:
> - cursor: 游标，用于分页，0表示第一页
> - limit: 每页返回的任务数量，建议24
> - mission_type: 任务类型，通常为1
> - tab_scene: 场景类型
>     - 1: 可投稿 (可以直接投稿的任务)
>     - 2: 可报名 (需要报名审核的任务)
>     - 3: 好物测评 (商品测评类任务)
> - industry_lv1/lv2: 行业分类 (建议先调用fetch_industry_category_config获取完整分类)
>     - -1: 全部行业
>     - 具体数值: 对应具体行业类别 (如1913=游戏, 1903=食品饮料)
> - platform_channel: 平台渠道 (可选)
>     - 1: 抖音视频
>     - 2: 抖音直播
>     - 3: 抖音图文
> - pay_type: 付费类型 (可选)
>     - 1: 视频等级 (按粉丝量等级定价)
>     - 2: 自定义 (商家自定义价格)
>     - 3: 按转化付费 (按转化效果付费)
>     - 4: 按有效播放量 (按播放量付费)
>     - 5: 按销售量 (按商品销售量付费)
>     - 9: 按核销量 (按核销数量付费)
>     - 14: 按付费分佣 (按分佣比例付费)
> - greater_than_cost_progress: 成本进度筛选 (可选)
>     - 20: 高于20%成本进度的任务
>     - 50: 高于50%成本进度的任务
>     - 80: 高于80%成本进度的任务
> - publish_time_start: 发布开始时间过滤 (可选，时间戳格式)
> - quick_selector_scene: 快速筛选场景 (可选)
>     - 1: 高收益任务
>     - 4: 保底收入任务
>     - 5: 曾经合作过的商家
> - keyword: 关键词搜索 (可选，支持任务名称或任务ID)
>
> ### 使用示例:
> ```
> # 获取全部行业的可投稿任务
> GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1
>
> # 获取游戏行业休闲游戏分类的按播放量付费任务
> GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4
>
> # 获取高收益的抖音视频任务
> GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1
> ```
>
> ### 返回:
> - 返回符合条件的商单任务列表
> - 包含任务详情、报酬信息、要求等
>
> # [English]
> ### Purpose:
> - Get mission task list from Douyin Creator platform
> - Supports multiple filtering conditions including industry classification, payment type, platform channel, etc.
>
> ### Important Parameter Usage Guidelines:
> #### Industry Classification Combination Rules:
> - **industry_lv1=-1 (All)**: When selecting all primary industries, industry_lv2 parameter will be ignored, no need to set
> - **industry_lv1=specific value**: When selecting specific primary industry, can be combined with industry_lv2 for secondary filtering
>     - industry_lv2=-1: All secondary categories under the primary industry
>     - industry_lv2=specific value: Specific secondary category under the primary industry
>
> #### Optional Parameters (No need to pass when selecting "All"):
> - **platform_channel**: Not passing means all platform channels
> - **pay_type**: Not passing means all payment types
> - **greater_than_cost_progress**: Not passing means no cost progress restriction
> - **publish_time_start**: Not passing means no publish time restriction
> - **quick_selector_scene**: Not passing means no quick filtering
> - **keyword**: Not passing means no keyword search
>
> ### Parameter Details:
> - cursor: Cursor for pagination, 0 for first page
> - limit: Number of tasks per page, recommended 24
> - mission_type: Mission type, usually 1
> - tab_scene: Scene type
>     - 1: Submittable (tasks that can be submitted directly)
>     - 2: Registrable (tasks that require registration and approval)
>     - 3: Product Review (product evaluation tasks)
> - industry_lv1/lv2: Industry classification (recommend calling fetch_industry_category_config first)
>     - -1: All industries
>     - Specific values: Corresponding to specific industry categories (e.g., 1913=Gaming, 1903=Food&Beverage)
> - platform_channel: Platform channel (optional)
>     - 1: Douyin Video
>     - 2: Douyin Live
>     - 3: Douyin Image&Text
> - pay_type: Payment type (optional)
>     - 1: Video Level (pricing by follower level)
>     - 2: Custom (merchant custom pricing)
>     - 3: Conversion-based (pay by conversion effect)
>     - 4: Valid Views (pay by view count)
>     - 5: Sales Volume (pay by product sales)
>     - 9: Verification Volume (pay by verification count)
>     - 14: Commission-based (pay by commission ratio)
> - greater_than_cost_progress: Cost progress filter (optional)
>     - 20: Tasks with more than 20% cost progress
>     - 50: Tasks with more than 50% cost progress
>     - 80: Tasks with more than 80% cost progress
> - publish_time_start: Publish start time filter (optional, timestamp format)
> - quick_selector_scene: Quick filter scene (optional)
>     - 1: High revenue tasks
>     - 4: Guaranteed income tasks
>     - 5: Previously collaborated merchants
> - keyword: Keyword search (optional, supports task name or task ID)
>
> ### Usage Examples:
> ```
> # Get submittable tasks from all industries
> GET /fetch_mission_task_list?industry_lv1=-1&tab_scene=1
>
> # Get tasks from gaming industry casual games category with view-based payment
> GET /fetch_mission_task_list?industry_lv1=1913&industry_lv2=191301&pay_type=4
>
> # Get high-revenue Douyin video tasks
> GET /fetch_mission_task_list?platform_channel=1&quick_selector_scene=1
> ```
>
> ### Return:
> - Returns mission task list matching the conditions
> - Contains task details, compensation info, requirements, etc.

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cursor | query | integer | 否 | 游标/Cursor (分页) | 0 | 0 | 无 |
| limit | query | integer | 否 | 每页数量/Items per page | 24 | 24 | 无 |
| mission_type | query | integer | 否 | 任务类型/Mission type | 1 | 1 | 无 |
| tab_scene | query | integer | 否 | 场景类型/Scene type (1=可投稿, 2=可报名, 3=好物测评) | 1 | 1 | 无 |
| industry_lv1 | query | integer | 否 | 一级行业/Primary industry (-1=全部) | -1 | 1913 | 无 |
| industry_lv2 | query | integer | 否 | 二级行业/Secondary industry (-1=全部) | -1 | 191301 | 无 |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel (1=抖音视频, 2=抖音直播, 3=抖音图文) | 无 | 1 | 无 |
| pay_type | query | integer | 否 | 付费类型/Pay type (1=视频等级, 2=自定义, 3=按转化付费, 4=按有效播放量, 5=按销售量, 9=按核销量, 14=按付费分佣) | 无 | 4 | 无 |
| greater_than_cost_progress | query | integer | 否 | 成本进度/Cost progress (20=高于20%, 50=高于50%, 80=高于80%) | 无 | 20 | 无 |
| publish_time_start | query | integer | 否 | 发布开始时间/Publish start time (时间戳) | 无 | 1757097636 | 无 |
| quick_selector_scene | query | integer | 否 | 快速选择场景/Quick selector (1=高收益, 4=保底收入, 5=合作过) | 无 | 无 | 无 |
| keyword | query | string | 否 | 关键词/Keyword (任务名称或ID) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-user-search"></a>
### `GET /api/u1/v1/douyin/creator/fetch_user_search`

- 摘要：搜索用户/Search users
- 能力：搜索 / 创作者 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_douyin_creator_fetch_user_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索抖音用户，支持抖音号和抖音昵称搜索
> ### 参数:
> - user_name: 用户名 (支持抖音号和抖音昵称)
>     - 抖音号: 如 "rmrbxmt"
>     - 抖音昵称: 如 "Y"、"人民日报"
> ### 返回:
> - 最多返回20个匹配的用户信息
> - 包含用户基本信息如头像、昵称、抖音号等
>
> # [English]
> ### Purpose:
> - Search Douyin users by Douyin ID or nickname
> ### Parameters:
> - user_name: Username (supports Douyin ID and nickname)
>     - Douyin ID: e.g., "rmrbxmt"
>     - Nickname: e.g., "Y", "人民日报"
> ### Return:
> - Returns up to 20 matching user information
> - Contains basic user info like avatar, nickname, Douyin ID, etc.

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_name | query | string | 是 | 用户名/Username (支持抖音号和抖音昵称) | 无 | Y | 无 |

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

<a id="get-api-u1-v1-douyin-creator-fetch-video-danmaku-list"></a>
### `GET /api/u1/v1/douyin/creator/fetch_video_danmaku_list`

- 摘要：获取作品弹幕列表/Get video danmaku list
- 能力：创作者 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定作品的弹幕列表，支持管理和筛选弹幕
> ### 参数:
> - item_id: 作品ID (必需参数，从作品链接或API获取)
> - count: 每页弹幕数量 (建议20，范围1-100)
> - offset: 偏移量 (分页使用，起始位置)
> - order_type: 排序类型 (1=时间排序, 2=其他排序)
> - is_blocked: 是否获取被屏蔽的弹幕 (false=正常弹幕, true=被屏蔽弹幕)
> ### 返回:
> - 作品弹幕列表数据
>
> # [English]
> ### Purpose:
> - Get danmaku list for specified video, supports management and filtering
> ### Parameters:
> - item_id: Video item ID (required, get from video link or API)
> - count: Items per page (recommended 20, range 1-100)
> - offset: Offset (for pagination, starting position)
> - order_type: Order type (1=time order, 2=other order)
> - is_blocked: Whether to get blocked danmaku (false=normal, true=blocked)
> ### Return:
> - Video danmaku list data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品ID/Video item ID | 无 | 7545659154417896746 | 无 |
| count | query | integer | 否 | 每页数量/Items per page | 20 | 20 | 无 |
| offset | query | integer | 否 | 偏移量/Offset (starting position) | 0 | 0 | 无 |
| order_type | query | integer | 否 | 排序类型/Order type (1=时间排序, 2=其他排序) | 1 | 1 | 无 |
| is_blocked | query | boolean | 否 | 是否被屏蔽/Is blocked | false | false | 无 |

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
