# LinkedIn-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/linkedin-web-api.md`](../api-tags/linkedin-web-api.md)
- Current contract file: `api-contracts/linkedin-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `25`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-linkedin-web-get-company-job-count"></a>
### `GET /api/u1/v1/linkedin/web/get_company_job_count`

- Summary: 获取公司职位数量/Get company job count
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID | None | 783611 | None |

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

<a id="get-api-u1-v1-linkedin-web-get-company-jobs"></a>
### `GET /api/u1/v1/linkedin/web/get_company_jobs`

- Summary: 获取公司职位/Get company jobs
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID | None | 783611 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| sort_by | query | string | No | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant | None | None | None |
| date_posted | query | string | No | 发布时间过滤：anytime, past_month, past_week, past_24_hours | None | None | None |
| experience_level | query | string | No | 经验级别：internship, entry_level, associate, mid_senior, director, executive | None | None | None |
| remote | query | string | No | 工作地点类型：onsite, remote, hybrid | None | None | None |
| job_type | query | string | No | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other | None | None | None |
| easy_apply | query | boolean | No | 是否易申请/Filter easy apply jobs | None | None | None |
| under_10_applicants | query | boolean | No | 是否少于10个申请者/Filter jobs with under 10 applicants | None | None | None |
| fair_chance_employer | query | boolean | No | 是否公平机会雇主/Filter fair chance employer jobs | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-company-people"></a>
### `GET /api/u1/v1/linkedin/web/get_company_people`

- Summary: 获取公司员工/Get company people
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_people_api_v1_linkedin_web_get_company_people_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID | None | 1066442 | None |
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

<a id="get-api-u1-v1-linkedin-web-get-company-posts"></a>
### `GET /api/u1/v1/linkedin/web/get_company_posts`

- Summary: 获取公司帖子/Get company posts
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_posts_api_v1_linkedin_web_get_company_posts_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID | None | 10649600 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| sort_by | query | string | No | 排序方式：top(热门)或recent(最新)/Sort by: top or recent | top | top | None |

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

<a id="get-api-u1-v1-linkedin-web-get-company-profile"></a>
### `GET /api/u1/v1/linkedin/web/get_company_profile`

- Summary: 获取公司资料/Get company profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_profile_api_v1_linkedin_web_get_company_profile_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| company | query | string | No | 公司名称/Company name | None | rapidapi | None |
| company_id | query | string | No | 公司ID（额外消耗1次请求）/Company ID (+1 request) | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-job-detail"></a>
### `GET /api/u1/v1/linkedin/web/get_job_detail`

- Summary: 获取职位详情/Get job detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_job_detail_api_v1_linkedin_web_get_job_detail_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| job_id | query | string | Yes | 职位ID/Job ID | None | 4172815660 | None |
| include_skills | query | boolean | No | 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request) | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-about"></a>
### `GET /api/u1/v1/linkedin/web/get_user_about`

- Summary: 获取用户简介/Get user about
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_about_api_v1_linkedin_web_get_user_about_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-certifications"></a>
### `GET /api/u1/v1/linkedin/web/get_user_certifications`

- Summary: 获取用户认证/Get user certifications
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4 | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-comments"></a>
### `GET /api/u1/v1/linkedin/web/get_user_comments`

- Summary: 获取用户评论/Get user comments
- Capabilities: comments / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_comments_api_v1_linkedin_web_get_user_comments_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| pagination_token | query | string | No | 分页令牌/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-contact"></a>
### `GET /api/u1/v1/linkedin/web/get_user_contact`

- Summary: 获取用户联系信息/Get user contact information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_contact_api_v1_linkedin_web_get_user_contact_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username | None | shubhangi-shrivastava-39161bb7 | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-educations"></a>
### `GET /api/u1/v1/linkedin/web/get_user_educations`

- Summary: 获取用户教育背景/Get user educations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_educations_api_v1_linkedin_web_get_user_educations_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAARpiwIBp_SzoeHPlUfOvmtibe08Ea1iCh4 | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-experience"></a>
### `GET /api/u1/v1/linkedin/web/get_user_experience`

- Summary: 获取用户工作经历/Get user experience
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_experience_api_v1_linkedin_web_get_user_experience_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-follower-and-connection"></a>
### `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`

- Summary: 获取用户粉丝和连接数/Get user follower and connection
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username | None | zoranmilosevic | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-honors"></a>
### `GET /api/u1/v1/linkedin/web/get_user_honors`

- Summary: 获取用户荣誉奖项/Get user honors
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_honors_api_v1_linkedin_web_get_user_honors_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAC41xVEBx77koDz3k1eJ5E9t8UZ7g0IVGj4 | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-images"></a>
### `GET /api/u1/v1/linkedin/web/get_user_images`

- Summary: 获取用户图片/Get user images
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_images_api_v1_linkedin_web_get_user_images_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| pagination_token | query | string | No | 分页令牌/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-interests-companies"></a>
### `GET /api/u1/v1/linkedin/web/get_user_interests_companies`

- Summary: 获取用户感兴趣的公司/Get user interests companies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAEDH77YBEVIYXAaEwTicp5CcB_hR7DfFL9o | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-interests-groups"></a>
### `GET /api/u1/v1/linkedin/web/get_user_interests_groups`

- Summary: 获取用户感兴趣的群组/Get user interests groups
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAAjpjWIBMh1iBR4OgSPK5GXetlQ6dYUT-qo | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-posts"></a>
### `GET /api/u1/v1/linkedin/web/get_user_posts`

- Summary: 获取用户帖子/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posts_api_v1_linkedin_web_get_user_posts_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| pagination_token | query | string | No | 分页令牌/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-profile"></a>
### `GET /api/u1/v1/linkedin/web/get_user_profile`

- Summary: 获取用户资料/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_api_v1_linkedin_web_get_user_profile_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username | None | jack | None |
| include_follower_and_connection | query | boolean | No | 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request) | None | None | None |
| include_experiences | query | boolean | No | 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request) | None | None | None |
| include_skills | query | boolean | No | 包含技能（额外消耗1次请求）/Include skills (+1 request) | None | None | None |
| include_certifications | query | boolean | No | 包含认证（额外消耗1次请求）/Include certifications (+1 request) | None | None | None |
| include_publications | query | boolean | No | 包含出版物（额外消耗1次请求）/Include publications (+1 request) | None | None | None |
| include_educations | query | boolean | No | 包含教育背景（额外消耗1次请求）/Include educational background (+1 request) | None | None | None |
| include_volunteers | query | boolean | No | 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request) | None | None | None |
| include_honors | query | boolean | No | 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request) | None | None | None |
| include_interests | query | boolean | No | 包含兴趣（额外消耗1次请求）/Include interests (+1 request) | None | None | None |
| include_bio | query | boolean | No | 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request) | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-publications"></a>
### `GET /api/u1/v1/linkedin/web/get_user_publications`

- Summary: 获取用户出版物/Get user publications
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_publications_api_v1_linkedin_web_get_user_publications_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAB8rG_UB7cstjC__gk5318uYsZOIVkyysi4 | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-recommendations"></a>
### `GET /api/u1/v1/linkedin/web/get_user_recommendations`

- Summary: 获取用户推荐信/Get user recommendations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAAC3iNKcB3qbWJrP7K5Z3i89AF5c1snr8bhc | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| type | query | string | No | 推荐类型：received(收到的)或given(给出的)/Type: received or given | received | received | None |
| pagination_token | query | string | No | 分页令牌/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-get-user-skills"></a>
### `GET /api/u1/v1/linkedin/web/get_user_skills`

- Summary: 获取用户技能/Get user skills
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_skills_api_v1_linkedin_web_get_user_skills_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAACkphDcBDruPBdXiAnqyc834jkTkd_4kRnU | None |
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

<a id="get-api-u1-v1-linkedin-web-get-user-videos"></a>
### `GET /api/u1/v1/linkedin/web/get_user_videos`

- Summary: 获取用户视频/Get user videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_videos_api_v1_linkedin_web_get_user_videos_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint | None | ACoAABCtiL8B26nfi3Nbpo_AM8ngg4LeClT1Wh8 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| pagination_token | query | string | No | 分页令牌/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-search-jobs"></a>
### `GET /api/u1/v1/linkedin/web/search_jobs`

- Summary: 搜索职位/Search jobs
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_jobs_api_v1_linkedin_web_search_jobs_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | backend | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| sort_by | query | string | No | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant | None | None | None |
| date_posted | query | string | No | 发布时间过滤：anytime, past_month, past_week, past_24_hours | None | None | None |
| geocode | query | string | No | 地理位置代码，可通过Search Geocode Location获取/Geocode for location | None | 103644278 | None |
| company | query | string | No | 公司ID过滤/Company ID filter (e.g., 1441 for Google) | None | 1441 | None |
| experience_level | query | string | No | 经验级别：internship, entry_level, associate, mid_senior, director, executive | None | None | None |
| remote | query | string | No | 工作地点类型：onsite, remote, hybrid | None | None | None |
| job_type | query | string | No | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other | None | None | None |
| easy_apply | query | boolean | No | 是否易申请/Filter easy apply jobs | None | None | None |
| has_verifications | query | boolean | No | 是否有公司认证/Filter jobs with company verifications | None | None | None |
| under_10_applicants | query | boolean | No | 是否少于10个申请者/Filter jobs with under 10 applicants | None | None | None |
| fair_chance_employer | query | boolean | No | 是否公平机会雇主/Filter fair chance employer jobs | None | None | None |

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

<a id="get-api-u1-v1-linkedin-web-search-people"></a>
### `GET /api/u1/v1/linkedin/web/search_people`

- Summary: 搜索用户/Search people
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_people_api_v1_linkedin_web_search_people_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| name | query | string | No | 搜索关键词/Search keyword for people | None | john | None |
| first_name | query | string | No | 名/First name | None | john | None |
| last_name | query | string | No | 姓/Last name | None | oliver | None |
| title | query | string | No | 职位/Title | None | manager | None |
| company | query | string | No | 公司/Company | None | None | None |
| school | query | string | No | 学校/School | None | None | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |
| geocode_location | query | string | No | 地理位置代码/Geocode for location (e.g., 103644278 for United States) | None | 103644278 | None |
| current_company | query | string | No | 当前公司ID/Current company ID | None | None | None |
| profile_language | query | string | No | 个人资料语言/Profile language | None | None | None |
| industry | query | string | No | 行业ID/Industry ID | None | None | None |
| service_category | query | string | No | 服务类别ID/Service category ID | None | None | None |

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
