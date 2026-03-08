# LinkedIn-Web-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/linkedin-web-api.md`
- Full contract: [`api-contracts/linkedin-web-api.md`](../api-contracts/linkedin-web-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `25`
- Common capabilities: profiles / accounts / general / content details / search / details / comments
- Default auth: Header `Authorization` Bearer
- Common inputs: `page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote`
- Tag description: **(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**

## Routes

### `GET /api/u1/v1/linkedin/web/get_company_job_count`

- Summary: 获取公司职位数量/Get company job count
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-job-count`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-job-count)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_company_jobs`

- Summary: 获取公司职位/Get company jobs
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-jobs`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-jobs)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID |
| page | query | integer | No | 页码/Page number |
| sort_by | query | string | No | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant |
| date_posted | query | string | No | 发布时间过滤：anytime, past_month, past_week, past_24_hours |
| experience_level | query | string | No | 经验级别：internship, entry_level, associate, mid_senior, director, executive |
| remote | query | string | No | 工作地点类型：onsite, remote, hybrid |
| job_type | query | string | No | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other |
| easy_apply | query | boolean | No | 是否易申请/Filter easy apply jobs |
| under_10_applicants | query | boolean | No | 是否少于10个申请者/Filter jobs with under 10 applicants |
| fair_chance_employer | query | boolean | No | 是否公平机会雇主/Filter fair chance employer jobs |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_company_people`

- Summary: 获取公司员工/Get company people
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_people_api_v1_linkedin_web_get_company_people_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-people`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-people)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_company_posts`

- Summary: 获取公司帖子/Get company posts
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_posts_api_v1_linkedin_web_get_company_posts_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-posts`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| company_id | query | string | Yes | 公司ID/Company ID |
| page | query | integer | No | 页码/Page number |
| sort_by | query | string | No | 排序方式：top(热门)或recent(最新)/Sort by: top or recent |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_company_profile`

- Summary: 获取公司资料/Get company profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_company_profile_api_v1_linkedin_web_get_company_profile_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-profile`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| company | query | string | No | 公司名称/Company name |
| company_id | query | string | No | 公司ID（额外消耗1次请求）/Company ID (+1 request) |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_job_detail`

- Summary: 获取职位详情/Get job detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_job_detail_api_v1_linkedin_web_get_job_detail_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-job-detail`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-job-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| job_id | query | string | Yes | 职位ID/Job ID |
| include_skills | query | boolean | No | 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request) |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_about`

- Summary: 获取用户简介/Get user about
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_about_api_v1_linkedin_web_get_user_about_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-about`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-about)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_certifications`

- Summary: 获取用户认证/Get user certifications
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-certifications`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-certifications)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_comments`

- Summary: 获取用户评论/Get user comments
- Capabilities: comments / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_comments_api_v1_linkedin_web_get_user_comments_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-comments`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-comments)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |
| pagination_token | query | string | No | 分页令牌/Pagination token |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_contact`

- Summary: 获取用户联系信息/Get user contact information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_contact_api_v1_linkedin_web_get_user_contact_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-contact`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-contact)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_educations`

- Summary: 获取用户教育背景/Get user educations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_educations_api_v1_linkedin_web_get_user_educations_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-educations`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-educations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_experience`

- Summary: 获取用户工作经历/Get user experience
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_experience_api_v1_linkedin_web_get_user_experience_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-experience`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-experience)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`

- Summary: 获取用户粉丝和连接数/Get user follower and connection
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-follower-and-connection`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-follower-and-connection)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_honors`

- Summary: 获取用户荣誉奖项/Get user honors
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_honors_api_v1_linkedin_web_get_user_honors_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-honors`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-honors)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_images`

- Summary: 获取用户图片/Get user images
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_images_api_v1_linkedin_web_get_user_images_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-images`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-images)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |
| pagination_token | query | string | No | 分页令牌/Pagination token |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_interests_companies`

- Summary: 获取用户感兴趣的公司/Get user interests companies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-companies`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-companies)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_interests_groups`

- Summary: 获取用户感兴趣的群组/Get user interests groups
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-groups`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-groups)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_posts`

- Summary: 获取用户帖子/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posts_api_v1_linkedin_web_get_user_posts_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-posts`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-posts)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |
| pagination_token | query | string | No | 分页令牌/Pagination token |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_profile`

- Summary: 获取用户资料/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_api_v1_linkedin_web_get_user_profile_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-profile`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-profile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| username | query | string | Yes | LinkedIn用户名/LinkedIn username |
| include_follower_and_connection | query | boolean | No | 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request) |
| include_experiences | query | boolean | No | 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request) |
| include_skills | query | boolean | No | 包含技能（额外消耗1次请求）/Include skills (+1 request) |
| include_certifications | query | boolean | No | 包含认证（额外消耗1次请求）/Include certifications (+1 request) |
| include_publications | query | boolean | No | 包含出版物（额外消耗1次请求）/Include publications (+1 request) |
| include_educations | query | boolean | No | 包含教育背景（额外消耗1次请求）/Include educational background (+1 request) |
| include_volunteers | query | boolean | No | 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request) |
| include_honors | query | boolean | No | 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request) |
| include_interests | query | boolean | No | 包含兴趣（额外消耗1次请求）/Include interests (+1 request) |
| include_bio | query | boolean | No | 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request) |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_publications`

- Summary: 获取用户出版物/Get user publications
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_publications_api_v1_linkedin_web_get_user_publications_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-publications`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-publications)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_recommendations`

- Summary: 获取用户推荐信/Get user recommendations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-recommendations`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-recommendations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |
| type | query | string | No | 推荐类型：received(收到的)或given(给出的)/Type: received or given |
| pagination_token | query | string | No | 分页令牌/Pagination token |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_skills`

- Summary: 获取用户技能/Get user skills
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_skills_api_v1_linkedin_web_get_user_skills_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-skills`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-skills)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/get_user_videos`

- Summary: 获取用户视频/Get user videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_videos_api_v1_linkedin_web_get_user_videos_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-videos`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-videos)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| urn | query | string | Yes | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | No | 页码/Page number |
| pagination_token | query | string | No | 分页令牌/Pagination token |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/search_jobs`

- Summary: 搜索职位/Search jobs
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_jobs_api_v1_linkedin_web_search_jobs_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-jobs`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-jobs)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码/Page number |
| sort_by | query | string | No | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant |
| date_posted | query | string | No | 发布时间过滤：anytime, past_month, past_week, past_24_hours |
| geocode | query | string | No | 地理位置代码，可通过Search Geocode Location获取/Geocode for location |
| company | query | string | No | 公司ID过滤/Company ID filter (e.g., 1441 for Google) |
| experience_level | query | string | No | 经验级别：internship, entry_level, associate, mid_senior, director, executive |
| remote | query | string | No | 工作地点类型：onsite, remote, hybrid |
| job_type | query | string | No | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other |
| easy_apply | query | boolean | No | 是否易申请/Filter easy apply jobs |
| has_verifications | query | boolean | No | 是否有公司认证/Filter jobs with company verifications |
| under_10_applicants | query | boolean | No | 是否少于10个申请者/Filter jobs with under 10 applicants |
| fair_chance_employer | query | boolean | No | 是否公平机会雇主/Filter fair chance employer jobs |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.

### `GET /api/u1/v1/linkedin/web/search_people`

- Summary: 搜索用户/Search people
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_people_api_v1_linkedin_web_search_people_get`
- Full contract: [`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-people`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-people)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| name | query | string | No | 搜索关键词/Search keyword for people |
| first_name | query | string | No | 名/First name |
| last_name | query | string | No | 姓/Last name |
| title | query | string | No | 职位/Title |
| company | query | string | No | 公司/Company |
| school | query | string | No | 学校/School |
| page | query | integer | No | 页码/Page number |
| geocode_location | query | string | No | 地理位置代码/Geocode for location (e.g., 103644278 for United States) |
| current_company | query | string | No | 当前公司ID/Current company ID |
| profile_language | query | string | No | 个人资料语言/Profile language |
| industry | query | string | No | 行业ID/Industry ID |
| service_category | query | string | No | 服务类别ID/Service category ID |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.
