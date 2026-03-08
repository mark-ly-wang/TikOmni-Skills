# LinkedIn-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/linkedin-web-api.md`
- 完整契约：[`api-contracts/linkedin-web-api.md`](../api-contracts/linkedin-web-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`25`
- 常见能力：主页/账号 / 通用能力 / 作品详情 / 搜索 / 详情 / 评论
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote`
- 标签说明：**(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/linkedin/web/get_company_job_count`

- 摘要：获取公司职位数量/Get company job count
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-job-count`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-job-count)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_company_jobs`

- 摘要：获取公司职位/Get company jobs
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-jobs`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-jobs)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID |
| page | query | integer | 否 | 页码/Page number |
| sort_by | query | string | 否 | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant |
| date_posted | query | string | 否 | 发布时间过滤：anytime, past_month, past_week, past_24_hours |
| experience_level | query | string | 否 | 经验级别：internship, entry_level, associate, mid_senior, director, executive |
| remote | query | string | 否 | 工作地点类型：onsite, remote, hybrid |
| job_type | query | string | 否 | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other |
| easy_apply | query | boolean | 否 | 是否易申请/Filter easy apply jobs |
| under_10_applicants | query | boolean | 否 | 是否少于10个申请者/Filter jobs with under 10 applicants |
| fair_chance_employer | query | boolean | 否 | 是否公平机会雇主/Filter fair chance employer jobs |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_company_people`

- 摘要：获取公司员工/Get company people
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_people_api_v1_linkedin_web_get_company_people_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-people`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-people)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_company_posts`

- 摘要：获取公司帖子/Get company posts
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_posts_api_v1_linkedin_web_get_company_posts_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-posts`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| company_id | query | string | 是 | 公司ID/Company ID |
| page | query | integer | 否 | 页码/Page number |
| sort_by | query | string | 否 | 排序方式：top(热门)或recent(最新)/Sort by: top or recent |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_company_profile`

- 摘要：获取公司资料/Get company profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_company_profile_api_v1_linkedin_web_get_company_profile_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-profile`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-company-profile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| company | query | string | 否 | 公司名称/Company name |
| company_id | query | string | 否 | 公司ID（额外消耗1次请求）/Company ID (+1 request) |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_job_detail`

- 摘要：获取职位详情/Get job detail
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_job_detail_api_v1_linkedin_web_get_job_detail_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-job-detail`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-job-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| job_id | query | string | 是 | 职位ID/Job ID |
| include_skills | query | boolean | 否 | 包含职位技能要求（额外消耗1次请求）/Include job skills (+1 request) |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_about`

- 摘要：获取用户简介/Get user about
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_about_api_v1_linkedin_web_get_user_about_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-about`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-about)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_certifications`

- 摘要：获取用户认证/Get user certifications
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-certifications`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-certifications)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_comments`

- 摘要：获取用户评论/Get user comments
- 能力：评论 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_comments_api_v1_linkedin_web_get_user_comments_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-comments`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |
| pagination_token | query | string | 否 | 分页令牌/Pagination token |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_contact`

- 摘要：获取用户联系信息/Get user contact information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_contact_api_v1_linkedin_web_get_user_contact_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-contact`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-contact)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_educations`

- 摘要：获取用户教育背景/Get user educations
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_educations_api_v1_linkedin_web_get_user_educations_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-educations`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-educations)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_experience`

- 摘要：获取用户工作经历/Get user experience
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_experience_api_v1_linkedin_web_get_user_experience_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-experience`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-experience)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`

- 摘要：获取用户粉丝和连接数/Get user follower and connection
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-follower-and-connection`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-follower-and-connection)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_honors`

- 摘要：获取用户荣誉奖项/Get user honors
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_honors_api_v1_linkedin_web_get_user_honors_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-honors`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-honors)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_images`

- 摘要：获取用户图片/Get user images
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_images_api_v1_linkedin_web_get_user_images_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-images`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-images)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |
| pagination_token | query | string | 否 | 分页令牌/Pagination token |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_interests_companies`

- 摘要：获取用户感兴趣的公司/Get user interests companies
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-companies`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-companies)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_interests_groups`

- 摘要：获取用户感兴趣的群组/Get user interests groups
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-groups`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-interests-groups)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_posts`

- 摘要：获取用户帖子/Get user posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_posts_api_v1_linkedin_web_get_user_posts_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-posts`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |
| pagination_token | query | string | 否 | 分页令牌/Pagination token |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_profile`

- 摘要：获取用户资料/Get user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_profile_api_v1_linkedin_web_get_user_profile_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-profile`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-profile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | query | string | 是 | LinkedIn用户名/LinkedIn username |
| include_follower_and_connection | query | boolean | 否 | 包含粉丝和连接数（额外消耗1次请求）/Include follower and connection count (+1 request) |
| include_experiences | query | boolean | 否 | 包含工作经历（额外消耗1次请求）/Include work experiences (+1 request) |
| include_skills | query | boolean | 否 | 包含技能（额外消耗1次请求）/Include skills (+1 request) |
| include_certifications | query | boolean | 否 | 包含认证（额外消耗1次请求）/Include certifications (+1 request) |
| include_publications | query | boolean | 否 | 包含出版物（额外消耗1次请求）/Include publications (+1 request) |
| include_educations | query | boolean | 否 | 包含教育背景（额外消耗1次请求）/Include educational background (+1 request) |
| include_volunteers | query | boolean | 否 | 包含志愿者经历（额外消耗1次请求）/Include volunteer experiences (+1 request) |
| include_honors | query | boolean | 否 | 包含荣誉奖项（额外消耗1次请求）/Include honors and awards (+1 request) |
| include_interests | query | boolean | 否 | 包含兴趣（额外消耗1次请求）/Include interests (+1 request) |
| include_bio | query | boolean | 否 | 包含个人简介（额外消耗1次请求）/Include bio/about (+1 request) |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_publications`

- 摘要：获取用户出版物/Get user publications
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_publications_api_v1_linkedin_web_get_user_publications_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-publications`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-publications)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_recommendations`

- 摘要：获取用户推荐信/Get user recommendations
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-recommendations`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-recommendations)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |
| type | query | string | 否 | 推荐类型：received(收到的)或given(给出的)/Type: received or given |
| pagination_token | query | string | 否 | 分页令牌/Pagination token |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_skills`

- 摘要：获取用户技能/Get user skills
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_skills_api_v1_linkedin_web_get_user_skills_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-skills`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-skills)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/get_user_videos`

- 摘要：获取用户视频/Get user videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_videos_api_v1_linkedin_web_get_user_videos_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-videos`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-get-user-videos)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| urn | query | string | 是 | 用户URN，可通过get_user_profile接口获取/User URN, can be obtained from get_user_profile endpoint |
| page | query | integer | 否 | 页码/Page number |
| pagination_token | query | string | 否 | 分页令牌/Pagination token |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/search_jobs`

- 摘要：搜索职位/Search jobs
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_jobs_api_v1_linkedin_web_search_jobs_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-jobs`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-jobs)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |
| sort_by | query | string | 否 | 排序方式：recent(最新)或relevant(相关)/Sort by: recent or relevant |
| date_posted | query | string | 否 | 发布时间过滤：anytime, past_month, past_week, past_24_hours |
| geocode | query | string | 否 | 地理位置代码，可通过Search Geocode Location获取/Geocode for location |
| company | query | string | 否 | 公司ID过滤/Company ID filter (e.g., 1441 for Google) |
| experience_level | query | string | 否 | 经验级别：internship, entry_level, associate, mid_senior, director, executive |
| remote | query | string | 否 | 工作地点类型：onsite, remote, hybrid |
| job_type | query | string | 否 | 工作类型：full_time, part_time, contract, temporary, volunteer, internship, other |
| easy_apply | query | boolean | 否 | 是否易申请/Filter easy apply jobs |
| has_verifications | query | boolean | 否 | 是否有公司认证/Filter jobs with company verifications |
| under_10_applicants | query | boolean | 否 | 是否少于10个申请者/Filter jobs with under 10 applicants |
| fair_chance_employer | query | boolean | 否 | 是否公平机会雇主/Filter fair chance employer jobs |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。

### `GET /api/u1/v1/linkedin/web/search_people`

- 摘要：搜索用户/Search people
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_people_api_v1_linkedin_web_search_people_get`
- 完整契约：[`api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-people`](../api-contracts/linkedin-web-api.md#get-api-u1-v1-linkedin-web-search-people)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | query | string | 否 | 搜索关键词/Search keyword for people |
| first_name | query | string | 否 | 名/First name |
| last_name | query | string | 否 | 姓/Last name |
| title | query | string | 否 | 职位/Title |
| company | query | string | 否 | 公司/Company |
| school | query | string | 否 | 学校/School |
| page | query | integer | 否 | 页码/Page number |
| geocode_location | query | string | 否 | 地理位置代码/Geocode for location (e.g., 103644278 for United States) |
| current_company | query | string | 否 | 当前公司ID/Current company ID |
| profile_language | query | string | 否 | 个人资料语言/Profile language |
| industry | query | string | 否 | 行业ID/Industry ID |
| service_category | query | string | 否 | 服务类别ID/Service category ID |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。
