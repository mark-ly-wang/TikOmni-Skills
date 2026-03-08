# LinkedIn-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/linkedin-web-api.md`](../api-tags/linkedin-web-api.md)
- 当前契约文件：`api-contracts/linkedin-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`25`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**

## 路由契约

<a id="get-api-u1-v1-linkedin-web-get-company-job-count"></a>
### `GET /api/u1/v1/linkedin/web/get_company_job_count`

- 摘要：获取公司职位数量/Get company job count
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn公司职位数量
>
> ### 参数:
> - company_id: 公司ID（必填）
>
> ### 返回:
> - 公司职位数量数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn company job count
>
> ### Parameters:
> - company_id: Company ID (required)
>
> ### Returns:
> - Company job count data
>
> # [示例/Example]
> company_id = "783611"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID | 无 | 783611 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-company-jobs"></a>
### `GET /api/u1/v1/linkedin/web/get_company_jobs`

- 摘要：获取公司职位/Get company jobs
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn公司职位列表
>
> ### 参数:
> - company_id: 公司ID（必填）
> - page: 页码（可选），默认为1
> - sort_by: 排序方式（可选）：recent(最新), relevant(相关)
> - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours
> - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive
> - remote: 工作地点类型（可选）：onsite, remote, hybrid
> - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other
> - easy_apply: 是否易申请（可选）
> - under_10_applicants: 是否少于10个申请者（可选）
> - fair_chance_employer: 是否公平机会雇主（可选）
>
> ### 返回:
> - 公司职位列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn company jobs list
>
> ### Parameters:
> - company_id: Company ID (required)
> - page: Page number (optional), default is 1
> - sort_by: Sort by (optional): recent, relevant
> - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours
> - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive
> - remote: Remote filter (optional): onsite, remote, hybrid
> - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other
> - easy_apply: Easy apply filter (optional)
> - under_10_applicants: Under 10 applicants filter (optional)
> - fair_chance_employer: Fair chance employer filter (optional)
>
> ### Returns:
> - Company jobs list data
>
> # [示例/Example]
> company_id = "783611"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID | 无 | 783611 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| sort_by | query | string | 否 | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant | 无 | 无 | 无 |
| date_posted | query | string | 否 | 发布时间过滤：anytime, past_month, past_week, past_24_hours | 无 | 无 | 无 |
| experience_level | query | string | 否 | 经验级别：internship, entry_level, associate, mid_senior, director, executive | 无 | 无 | 无 |
| remote | query | string | 否 | 工作地点类型：onsite, remote, hybrid | 无 | 无 | 无 |
| job_type | query | string | 否 | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other | 无 | 无 | 无 |
| easy_apply | query | boolean | 否 | 是否易申请/Filter easy apply jobs | 无 | 无 | 无 |
| under_10_applicants | query | boolean | 否 | 是否少于10个申请者/Filter jobs with under 10 applicants | 无 | 无 | 无 |
| fair_chance_employer | query | boolean | 否 | 是否公平机会雇主/Filter fair chance employer jobs | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-company-people"></a>
### `GET /api/u1/v1/linkedin/web/get_company_people`

- 摘要：获取公司员工/Get company people
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_people_api_v1_linkedin_web_get_company_people_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn公司员工列表
>
> ### 参数:
> - company_id: 公司ID（必填）
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 公司员工列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn company people/employees list
>
> ### Parameters:
> - company_id: Company ID (required)
> - page: Page number (optional), default is 1
>
> ### Returns:
> - Company people list data
>
> # [示例/Example]
> company_id = "1066442"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID | 无 | 1066442 | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-company-posts"></a>
### `GET /api/u1/v1/linkedin/web/get_company_posts`

- 摘要：获取公司帖子/Get company posts
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_posts_api_v1_linkedin_web_get_company_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn公司发布的帖子
>
> ### 参数:
> - company_id: 公司ID（必填）
> - page: 页码（可选），默认为1
> - sort_by: 排序方式（可选），默认为top
>     - top: 热门帖子
>     - recent: 最新帖子
>
> ### 返回:
> - 公司帖子列表数据
>
> # [English]
> ### Purpose:
> - Get posts published by LinkedIn company
>
> ### Parameters:
> - company_id: Company ID (required)
> - page: Page number (optional), default is 1
> - sort_by: Sort by (optional), default is top
>     - top: Top posts
>     - recent: Recent posts
>
> ### Returns:
> - Company posts list data
>
> # [示例/Example]
> company_id = "10649600"
> page = 1
> sort_by = "top"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID | 无 | 10649600 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| sort_by | query | string | 否 | 排序方式：top(热门)或recent(最新)/Sort by: top or recent | top | top | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-company-profile"></a>
### `GET /api/u1/v1/linkedin/web/get_company_profile`

- 摘要：获取公司资料/Get company profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_profile_api_v1_linkedin_web_get_company_profile_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn公司资料信息
>
> ### 参数:
> - company: 公司名称（可选）
> - company_id: 公司ID（可选，额外消耗1次请求）
>
> ### 注意:
> - company和company_id至少需要提供一个
>
> ### 返回:
> - 公司资料数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn company profile information
>
> ### Parameters:
> - company: Company name (optional)
> - company_id: Company ID (optional, +1 request)
>
> ### Note:
> - At least one of company or company_id must be provided
>
> ### Returns:
> - Company profile data
>
> # [示例/Example]
> company = "rapidapi"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company | query | string | 否 | 公司名称/Company name | 无 | rapidapi | 无 |
| company_id | query | string | 否 | 公司ID（额外消耗1次请求）/Company ID (+1 request) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-job-detail"></a>
### `GET /api/u1/v1/linkedin/web/get_job_detail`

- 摘要：获取职位详情/Get job detail
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_job_detail_api_v1_linkedin_web_get_job_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn职位详情
>
> ### 参数:
> - job_id: 职位ID（必填）
> - include_skills: 包含职位技能要求（可选，额外消耗1次请求）
>
> ### 返回:
> - 职位详情数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn job detail
>
> ### Parameters:
> - job_id: Job ID (required)
> - include_skills: Include job skills (optional, +1 request)
>
> ### Returns:
> - Job detail data
>
> # [示例/Example]
> job_id = "4172815660"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| job_id | query | string | 是 | 职位ID/Job ID | 无 | 4172815660 | 无 |
| include_skills | query | boolean | 否 | 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-about"></a>
### `GET /api/u1/v1/linkedin/web/get_user_about`

- 摘要：获取用户简介/Get user about
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_about_api_v1_linkedin_web_get_user_about_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户简介/关于信息
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
>
> ### 返回:
> - 用户简介数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user about/bio information
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
>
> ### Returns:
> - User about data
>
> # [示例/Example]
> urn = "ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-certifications"></a>
### `GET /api/u1/v1/linkedin/web/get_user_certifications`

- 摘要：获取用户认证/Get user certifications
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户认证
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户认证列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user certifications
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User certifications list data
>
> # [示例/Example]
> urn = "ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4 | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-comments"></a>
### `GET /api/u1/v1/linkedin/web/get_user_comments`

- 摘要：获取用户评论/Get user comments
- 能力：评论 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_comments_api_v1_linkedin_web_get_user_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户的评论
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
> - pagination_token: 分页令牌（可选）
>
> ### 返回:
> - 用户评论列表数据
>
> # [English]
> ### Purpose:
> - Get comments made by LinkedIn user
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
> - pagination_token: Pagination token (optional)
>
> ### Returns:
> - User comments list data
>
> # [示例/Example]
> urn = "ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| pagination_token | query | string | 否 | 分页令牌/Pagination token | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-contact"></a>
### `GET /api/u1/v1/linkedin/web/get_user_contact`

- 摘要：获取用户联系信息/Get user contact information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_contact_api_v1_linkedin_web_get_user_contact_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户的联系信息
>
> ### 参数:
> - username: LinkedIn用户名（必填）
>
> ### 返回:
> - 用户联系信息数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user contact information
>
> ### Parameters:
> - username: LinkedIn username (required)
>
> ### Returns:
> - User contact information data
>
> # [示例/Example]
> username = "shubhangi-shrivastava-39161bb7"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username | 无 | shubhangi-shrivastava-39161bb7 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-educations"></a>
### `GET /api/u1/v1/linkedin/web/get_user_educations`

- 摘要：获取用户教育背景/Get user educations
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_educations_api_v1_linkedin_web_get_user_educations_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户教育背景
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户教育背景列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user educations
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User educations list data
>
> # [示例/Example]
> urn = "ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4 | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-experience"></a>
### `GET /api/u1/v1/linkedin/web/get_user_experience`

- 摘要：获取用户工作经历/Get user experience
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_experience_api_v1_linkedin_web_get_user_experience_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户工作经历
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户工作经历列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user work experience
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User experience list data
>
> # [示例/Example]
> urn = "ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-follower-and-connection"></a>
### `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`

- 摘要：获取用户粉丝和连接数/Get user follower and connection
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户粉丝和连接数
>
> ### 参数:
> - username: LinkedIn用户名（必填）
>
> ### 返回:
> - 用户粉丝和连接数数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user follower and connection count
>
> ### Parameters:
> - username: LinkedIn username (required)
>
> ### Returns:
> - User follower and connection data
>
> # [示例/Example]
> username = "zoranmilosevic"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username | 无 | zoranmilosevic | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-honors"></a>
### `GET /api/u1/v1/linkedin/web/get_user_honors`

- 摘要：获取用户荣誉奖项/Get user honors
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_honors_api_v1_linkedin_web_get_user_honors_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户荣誉奖项
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户荣誉奖项列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user honors and awards
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User honors list data
>
> # [示例/Example]
> urn = "ACoAAC41xVEBx77koDz3k1eJ5E9t8UZ7g0IVGj4"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAC41xVEBx77koDz3k1eJ5E9t8UZ7g0IVGj4 | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-images"></a>
### `GET /api/u1/v1/linkedin/web/get_user_images`

- 摘要：获取用户图片/Get user images
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_images_api_v1_linkedin_web_get_user_images_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户发布的图片
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
> - pagination_token: 分页令牌（可选）
>
> ### 返回:
> - 用户图片列表数据
>
> # [English]
> ### Purpose:
> - Get images published by LinkedIn user
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
> - pagination_token: Pagination token (optional)
>
> ### Returns:
> - User images list data
>
> # [示例/Example]
> urn = "ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| pagination_token | query | string | 否 | 分页令牌/Pagination token | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-interests-companies"></a>
### `GET /api/u1/v1/linkedin/web/get_user_interests_companies`

- 摘要：获取用户感兴趣的公司/Get user interests companies
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户感兴趣的公司
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户感兴趣的公司列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user interests - companies
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User interests companies list data
>
> # [示例/Example]
> urn = "ACoAAEDH77YBEVIYXAaEwTicp5CcB_hR7DfFL9o"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAEDH77YBEVIYXAaEwTicp5CcB_hR7DfFL9o | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-interests-groups"></a>
### `GET /api/u1/v1/linkedin/web/get_user_interests_groups`

- 摘要：获取用户感兴趣的群组/Get user interests groups
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户感兴趣的群组
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户感兴趣的群组列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user interests - groups
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User interests groups list data
>
> # [示例/Example]
> urn = "ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-posts"></a>
### `GET /api/u1/v1/linkedin/web/get_user_posts`

- 摘要：获取用户帖子/Get user posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_posts_api_v1_linkedin_web_get_user_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户发布的帖子
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
> - pagination_token: 分页令牌（可选）
>
> ### 返回:
> - 用户帖子列表数据
>
> # [English]
> ### Purpose:
> - Get posts published by LinkedIn user
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
> - pagination_token: Pagination token (optional)
>
> ### Returns:
> - User posts list data
>
> # [示例/Example]
> urn = "ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| pagination_token | query | string | 否 | 分页令牌/Pagination token | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-profile"></a>
### `GET /api/u1/v1/linkedin/web/get_user_profile`

- 摘要：获取用户资料/Get user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_profile_api_v1_linkedin_web_get_user_profile_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户资料信息
>
> ### 参数:
> - username: LinkedIn用户名（必填），可以从个人资料URL中获取，例如：https://www.linkedin.com/in/jack 则用户名为 jack
> - include_follower_and_connection: 包含粉丝和连接数（可选，额外消耗1次请求）
> - include_experiences: 包含工作经历（可选，额外消耗1次请求）
> - include_skills: 包含技能（可选，额外消耗1次请求）
> - include_certifications: 包含认证（可选，额外消耗1次请求）
> - include_publications: 包含出版物（可选，额外消耗1次请求）
> - include_educations: 包含教育背景（可选，额外消耗1次请求）
> - include_volunteers: 包含志愿者经历（可选，额外消耗1次请求）
> - include_honors: 包含荣誉奖项（可选，额外消耗1次请求）
> - include_interests: 包含兴趣（可选，额外消耗1次请求）
> - include_bio: 包含个人简介（可选，额外消耗1次请求）
>
> ### 返回:
> - 用户资料数据，包含：
>     - id: 用户ID
>     - urn: 用户URN
>     - public_identifier: 公开标识符
>     - first_name: 名
>     - last_name: 姓
>     - full_name: 全名
>     - headline: 头衔/职位描述
>     - is_premium: 是否高级会员
>     - is_open_to_work: 是否开放工作机会
>     - is_hiring: 是否在招聘
>     - location: 位置信息
>     - cover: 封面图片
>     - 以及根据参数选择的其他信息
>
> # [English]
> ### Purpose:
> - Get LinkedIn user profile information
>
> ### Parameters:
> - username: LinkedIn username (required), can be obtained from profile URL, e.g., for https://www.linkedin.com/in/jack, the username is jack
> - include_follower_and_connection: Include follower and connection count (optional, +1 request)
> - include_experiences: Include work experiences (optional, +1 request)
> - include_skills: Include skills (optional, +1 request)
> - include_certifications: Include certifications (optional, +1 request)
> - include_publications: Include publications (optional, +1 request)
> - include_educations: Include educational background (optional, +1 request)
> - include_volunteers: Include volunteer experiences (optional, +1 request)
> - include_honors: Include honors and awards (optional, +1 request)
> - include_interests: Include interests (optional, +1 request)
> - include_bio: Include bio/about (optional, +1 request)
>
> ### Returns:
> - User profile data including:
>     - id: User ID
>     - urn: User URN
>     - public_identifier: Public identifier
>     - first_name: First name
>     - last_name: Last name
>     - full_name: Full name
>     - headline: Headline/job description
>     - is_premium: Premium member status
>     - is_open_to_work: Open to work status
>     - is_hiring: Hiring status
>     - location: Location information
>     - cover: Cover images
>     - And other information based on selected parameters
>
> # [示例/Example]
> username = "jack"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username | 无 | jack | 无 |
| include_follower_and_connection | query | boolean | 否 | 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request) | 无 | 无 | 无 |
| include_experiences | query | boolean | 否 | 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request) | 无 | 无 | 无 |
| include_skills | query | boolean | 否 | 包含技能（额外消耗1次请求）/Include skills (+1 request) | 无 | 无 | 无 |
| include_certifications | query | boolean | 否 | 包含认证（额外消耗1次请求）/Include certifications (+1 request) | 无 | 无 | 无 |
| include_publications | query | boolean | 否 | 包含出版物（额外消耗1次请求）/Include publications (+1 request) | 无 | 无 | 无 |
| include_educations | query | boolean | 否 | 包含教育背景（额外消耗1次请求）/Include educational background (+1 request) | 无 | 无 | 无 |
| include_volunteers | query | boolean | 否 | 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request) | 无 | 无 | 无 |
| include_honors | query | boolean | 否 | 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request) | 无 | 无 | 无 |
| include_interests | query | boolean | 否 | 包含兴趣（额外消耗1次请求）/Include interests (+1 request) | 无 | 无 | 无 |
| include_bio | query | boolean | 否 | 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request) | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-publications"></a>
### `GET /api/u1/v1/linkedin/web/get_user_publications`

- 摘要：获取用户出版物/Get user publications
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_publications_api_v1_linkedin_web_get_user_publications_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户出版物
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户出版物列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user publications
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User publications list data
>
> # [示例/Example]
> urn = "ACoAAB8rG_UB7cstjC__gk5318uYsZOIVkyysi4"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAB8rG_UB7cstjC__gk5318uYsZOIVkyysi4 | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-recommendations"></a>
### `GET /api/u1/v1/linkedin/web/get_user_recommendations`

- 摘要：获取用户推荐信/Get user recommendations
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户的推荐信
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
> - type: 推荐类型（可选），默认为received
>     - received: 收到的推荐信
>     - given: 给出的推荐信
> - pagination_token: 分页令牌（可选）
>
> ### 返回:
> - 用户推荐信列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user recommendations
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
> - type: Recommendation type (optional), default is received
>     - received: Recommendations received
>     - given: Recommendations given
> - pagination_token: Pagination token (optional)
>
> ### Returns:
> - User recommendations list data
>
> # [示例/Example]
> urn = "ACoAAC3iNKcB3qbWJrP7K5Z3i89AF5c1snr8bhc"
> page = 1
> type = "received"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAAC3iNKcB3qbWJrP7K5Z3i89AF5c1snr8bhc | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| type | query | string | 否 | 推荐类型：received(收到的)或given(给出的)/Type: received or given | received | received | 无 |
| pagination_token | query | string | 否 | 分页令牌/Pagination token | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-get-user-skills"></a>
### `GET /api/u1/v1/linkedin/web/get_user_skills`

- 摘要：获取用户技能/Get user skills
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_skills_api_v1_linkedin_web_get_user_skills_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户技能
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
>
> ### 返回:
> - 用户技能列表数据
>
> # [English]
> ### Purpose:
> - Get LinkedIn user skills
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
>
> ### Returns:
> - User skills list data
>
> # [示例/Example]
> urn = "ACoAACkphDcBDruPBdXiAnqyc834jkTkd_4kRnU"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAACkphDcBDruPBdXiAnqyc834jkTkd_4kRnU | 无 |
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

<a id="get-api-u1-v1-linkedin-web-get-user-videos"></a>
### `GET /api/u1/v1/linkedin/web/get_user_videos`

- 摘要：获取用户视频/Get user videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_videos_api_v1_linkedin_web_get_user_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取LinkedIn用户发布的视频
>
> ### 参数:
> - urn: 用户URN（必填），可通过get_user_profile接口获取
> - page: 页码（可选），默认为1
> - pagination_token: 分页令牌（可选）
>
> ### 返回:
> - 用户视频列表数据
>
> # [English]
> ### Purpose:
> - Get videos published by LinkedIn user
>
> ### Parameters:
> - urn: User URN (required), can be obtained from get_user_profile endpoint
> - page: Page number (optional), default is 1
> - pagination_token: Pagination token (optional)
>
> ### Returns:
> - User videos list data
>
> # [示例/Example]
> urn = "ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | 无 | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| pagination_token | query | string | 否 | 分页令牌/Pagination token | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-search-jobs"></a>
### `GET /api/u1/v1/linkedin/web/search_jobs`

- 摘要：搜索职位/Search jobs
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_jobs_api_v1_linkedin_web_search_jobs_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索LinkedIn职位
>
> ### 参数:
> - keyword: 搜索关键词（必填）
> - page: 页码（可选），默认为1
> - sort_by: 排序方式（可选）：recent(最新), relevant(相关)
> - date_posted: 发布时间过滤（可选）：anytime, past_month, past_week, past_24_hours
> - geocode: 地理位置代码（可选）
> - company: 公司ID过滤（可选）
> - experience_level: 经验级别（可选）：internship, entry_level, associate, mid_senior, director, executive
> - remote: 工作地点类型（可选）：onsite, remote, hybrid
> - job_type: 工作类型（可选）：full_time, part_time, contract, temporary, volunteer, internship, other
> - easy_apply: 是否易申请（可选）
> - has_verifications: 是否有公司认证（可选）
> - under_10_applicants: 是否少于10个申请者（可选）
> - fair_chance_employer: 是否公平机会雇主（可选）
>
> ### 返回:
> - 职位搜索结果列表数据
>
> # [English]
> ### Purpose:
> - Search LinkedIn jobs
>
> ### Parameters:
> - keyword: Search keyword (required)
> - page: Page number (optional), default is 1
> - sort_by: Sort by (optional): recent, relevant
> - date_posted: Date posted filter (optional): anytime, past_month, past_week, past_24_hours
> - geocode: Geocode for location (optional)
> - company: Company ID filter (optional)
> - experience_level: Experience level (optional): internship, entry_level, associate, mid_senior, director, executive
> - remote: Remote filter (optional): onsite, remote, hybrid
> - job_type: Job type (optional): full_time, part_time, contract, temporary, volunteer, internship, other
> - easy_apply: Easy apply filter (optional)
> - has_verifications: Has verifications filter (optional)
> - under_10_applicants: Under 10 applicants filter (optional)
> - fair_chance_employer: Fair chance employer filter (optional)
>
> ### Returns:
> - Job search results list data
>
> # [示例/Example]
> keyword = "backend"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | backend | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| sort_by | query | string | 否 | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant | 无 | 无 | 无 |
| date_posted | query | string | 否 | 发布时间过滤：anytime, past_month, past_week, past_24_hours | 无 | 无 | 无 |
| geocode | query | string | 否 | 地理位置代码，可通过Search Geocode Location获取/Geocode for location | 无 | 103644278 | 无 |
| company | query | string | 否 | 公司ID过滤/Company ID filter (e.g., 1441 for Google) | 无 | 1441 | 无 |
| experience_level | query | string | 否 | 经验级别：internship, entry_level, associate, mid_senior, director, executive | 无 | 无 | 无 |
| remote | query | string | 否 | 工作地点类型：onsite, remote, hybrid | 无 | 无 | 无 |
| job_type | query | string | 否 | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other | 无 | 无 | 无 |
| easy_apply | query | boolean | 否 | 是否易申请/Filter easy apply jobs | 无 | 无 | 无 |
| has_verifications | query | boolean | 否 | 是否有公司认证/Filter jobs with company verifications | 无 | 无 | 无 |
| under_10_applicants | query | boolean | 否 | 是否少于10个申请者/Filter jobs with under 10 applicants | 无 | 无 | 无 |
| fair_chance_employer | query | boolean | 否 | 是否公平机会雇主/Filter fair chance employer jobs | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-linkedin-web-search-people"></a>
### `GET /api/u1/v1/linkedin/web/search_people`

- 摘要：搜索用户/Search people
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_people_api_v1_linkedin_web_search_people_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索LinkedIn用户
>
> ### 参数:
> - name: 搜索关键词（可选）
> - first_name: 名（可选）
> - last_name: 姓（可选）
> - title: 职位（可选）
> - company: 公司（可选）
> - school: 学校（可选）
> - page: 页码（可选），默认为1
> - geocode_location: 地理位置代码（可选）
> - current_company: 当前公司ID（可选）
> - profile_language: 个人资料语言（可选）
> - industry: 行业ID（可选）
> - service_category: 服务类别ID（可选）
>
> ### 返回:
> - 用户搜索结果列表数据
>
> # [English]
> ### Purpose:
> - Search LinkedIn people
>
> ### Parameters:
> - name: Search keyword (optional)
> - first_name: First name (optional)
> - last_name: Last name (optional)
> - title: Title (optional)
> - company: Company (optional)
> - school: School (optional)
> - page: Page number (optional), default is 1
> - geocode_location: Geocode for location (optional)
> - current_company: Current company ID (optional)
> - profile_language: Profile language (optional)
> - industry: Industry ID (optional)
> - service_category: Service category ID (optional)
>
> ### Returns:
> - People search results list data
>
> # [示例/Example]
> name = "john"
> first_name = "john"
> last_name = "oliver"
> title = "manager"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| name | query | string | 否 | 搜索关键词/Search keyword for people | 无 | john | 无 |
| first_name | query | string | 否 | 名/First name | 无 | john | 无 |
| last_name | query | string | 否 | 姓/Last name | 无 | oliver | 无 |
| title | query | string | 否 | 职位/Title | 无 | manager | 无 |
| company | query | string | 否 | 公司/Company | 无 | 无 | 无 |
| school | query | string | 否 | 学校/School | 无 | 无 | 无 |
| page | query | integer | 否 | 页码/Page number | 1 | 1 | 无 |
| geocode_location | query | string | 否 | 地理位置代码/Geocode for location (e.g., 103644278 for United States) | 无 | 103644278 | 无 |
| current_company | query | string | 否 | 当前公司ID/Current company ID | 无 | 无 | 无 |
| profile_language | query | string | 否 | 个人资料语言/Profile language | 无 | 无 | 无 |
| industry | query | string | 否 | 行业ID/Industry ID | 无 | 无 | 无 |
| service_category | query | string | 否 | 服务类别ID/Service category ID | 无 | 无 | 无 |

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
