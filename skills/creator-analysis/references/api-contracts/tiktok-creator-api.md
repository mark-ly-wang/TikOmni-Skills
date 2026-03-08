# TikTok-Creator-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/tiktok-creator-api.md`](../api-tags/tiktok-creator-api.md)
- 当前契约文件：`api-contracts/tiktok-creator-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`14`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(TikTok创作者数据和账号收益数据接口/TikTok-Creator-API data and account revenue data endpoints)**

## 路由契约

<a id="post-api-u1-v1-tiktok-creator-get-account-health-status"></a>
### `POST /api/u1/v1/tiktok/creator/get_account_health_status`

- 摘要：获取创作者账号健康状态/Get Creator Account Health Status
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_health_status_api_v1_tiktok_creator_get_account_health_status_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号的健康状况信息，包括过去 90 天内的健康评分（风险等级）以及当前累计的违规积分数量。
> - 关于违规积分：
>     - 违规积分是 TikTok 用于衡量账号健康状况的重要指标。
>     - 违规积分越高，账号健康状况越差，可能面临限流、禁播、封禁等处罚。
>     - 违规积分将直接影响账号的曝光量和推荐量。
>
> ### 累计违规积分对应的惩罚等级：
> | 分数范围  | 惩罚措施                                                | 惩罚时长 |
> | --------- | --------------------------------------------------------- | -------- |
> | 9-11      | 警告（Warning）                                           | 无       |
> | 12-14     | 暂停电商权限（视频、直播、商品展示功能）                  | 24 小时  |
> | 15-17     | 暂停电商权限                                              | 48 小时  |
> | 18-20     | 暂停电商权限                                              | 72 小时  |
> | 21-23     | 暂停电商权限                                              | 1 周     |
> | 24 及以上 | 永久移除电商权限，封禁 TikTok Shop 创作者账号             | 永久禁用 |
>
> ### 备注:
> - 此接口仅适用于已开通 TikTok Shop 的创作者账号。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - `risk_info`（健康状态信息）:
>   - `risk_level_text`: 当前风险等级描述（如 Healthy）
>   - `light_color`: 健康状态浅色展示色值（rgba 格式）
>   - `dark_color`: 健康状态深色展示色值（rgba 格式）
> - `vio_score_rule_learn_url`: 查看违规积分规则说明的链接
> - `is_show_score`: 是否展示违规积分（布尔值）
> - `violation_score`: 当前违规积分数量
> - `creator_status`: 创作者账号状态码（0=正常）
>
> # [English]
> ### Purpose:
> - Retrieve the health status of a TikTok Shop creator account, including the health score over the past 90 days and the current number of accumulated violation points.
> - About violation points:
>     - Violation points are key metrics used by TikTok to measure the health of a creator account.
>     - Higher violation points indicate worse account health, and may lead to restrictions such as reduced exposure, suspension, or account bans.
>     - Violation points directly impact the account’s visibility and recommendation on the platform.
>
> ### Punishment Levels for Accumulated Violation Points:
> | Score Range | Punishment Measures                                       | Duration         |
> | ----------- | ---------------------------------------------------------- | ---------------- |
> | 9-11        | Warning                                                     | None             |
> | 12-14       | E-commerce permissions suspended (video, live, product showcase) | 24 hours         |
> | 15-17       | E-commerce permissions suspended                           | 48 hours         |
> | 18-20       | E-commerce permissions suspended                           | 72 hours         |
> | 21-23       | E-commerce permissions suspended                           | 1 week           |
> | 24+         | Permanent removal of e-commerce permissions and banning of TikTok Shop creator account | Permanently disabled |
>
> ### Notes:
> - This API is only applicable to TikTok Shop creator accounts.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - proxy: Optional HTTP proxy address, can be omitted if not needed
>     - Example format: `http://username:password@host:port`
>
> ### Response:
> - `risk_info`: Account health status:
>   - `risk_level_text`: Current health level description (e.g., Healthy)
>   - `light_color`: Light color code for health level display (RGBA format)
>   - `dark_color`: Dark color code for health level display (RGBA format)
> - `vio_score_rule_learn_url`: URL to learn more about violation point rules
> - `is_show_score`: Whether to display violation points (boolean)
> - `violation_score`: Current violation score
> - `creator_status`: Creator account status code (0 = normal)
>
> # [示例/Example]
> ```json
> payload = {
>     "cookie": "your_cookie"
> }

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-account-insights-overview"></a>
### `POST /api/u1/v1/tiktok/creator/get_account_insights_overview`

- 摘要：获取创作者账号概览/Get Creator Account Overview
- 能力：创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_insights_overview_api_v1_tiktok_creator_get_account_insights_overview_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号在指定时间范围内的表现概览，包括收益、曝光、点击、成交等多维度数据。
> - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。
>
> ### 备注:
> - 此接口仅适用于已开通 TikTok Shop 功能的创作者账号。
> - 数据按照时间粒度进行分段统计，可用于数据分析和趋势观察。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询开始时间，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - `segments`（分段数据列表）:
>   - `time_selector`: 当前统计段的时间设置，包括周期、起止时间戳、时区、语言等
>   - `timed_stats`: 每天/每段的详细数据，包含以下字段：
>     - `live_revenue.amount`: 直播带货收益
>     - `video_revenue.amount`: 视频带货收益
>     - `revenue.amount`: 总收益（直播 + 视频）
>     - `base_revenue.amount`: 基础收益
>     - `commission_estimated.amount`: 预估佣金
>     - `alc_base_revenue.amount`: ALC 模式下基础收益
>     - `overall_item_sold_cnt`: 商品成交数
>     - `product_show_cnt`: 商品展示次数
>     - `product_click_cnt`: 商品点击次数
>     - `alc_pay_sku_order_cnt`: ALC 成交订单数
> - `meta.is_bound_shop`: 是否绑定 TikTok 店铺
>
> # [English]
> ### Purpose:
> - Retrieve performance overview of a TikTok Shop creator account within a specified date range, including metrics like revenue, exposure, clicks, and orders.
> - By default, it aggregates data from the month of `start_date` (e.g., if `start_date` is 2025-04-01, it retrieves data for the entire month of April).
>
> ### Notes:
> - This API is only applicable to TikTok accounts that have TikTok Shop enabled.
> - Data is segmented by time granularity (daily/monthly), and can be used for performance analysis or trend monitoring.
>
> ### Parameters:
> - cookie: User cookie string for authentication
> - start_date: Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'
> - proxy: Optional HTTP proxy address. Leave empty if not needed.
>     - Example format: `http://username:password@host:port`
>
> ### Response:
> - `segments`: List of data segments, each containing:
>   - `time_selector`: Time settings for the segment, including period, timestamp range, timezone, and locale
>   - `timed_stats`: Daily or interval-based statistics, including:
>     - `live_revenue.amount`: Revenue from livestream sales
>     - `video_revenue.amount`: Revenue from video sales
>     - `revenue.amount`: Total revenue (live + video)
>     - `base_revenue.amount`: Base revenue
>     - `commission_estimated.amount`: Estimated commission
>     - `alc_base_revenue.amount`: Base revenue under ALC model
>     - `overall_item_sold_cnt`: Total items sold
>     - `product_show_cnt`: Product exposure count
>     - `product_click_cnt`: Product click count
>     - `alc_pay_sku_order_cnt`: Orders under ALC model
> - `meta.is_bound_shop`: Whether the TikTok account is bound to a shop

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-account-violation-list"></a>
### `POST /api/u1/v1/tiktok/creator/get_account_violation_list`

- 摘要：获取创作者账号违规记录列表/Get Creator Account Violation Record List
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_violation_list_api_v1_tiktok_creator_get_account_violation_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号的违规记录信息，用于了解账号在运营期间的违规历史和处理情况。
> - 返回的违规记录包含违规类型、违规时间、违规原因、违规处理措施、申诉状态、是否可申诉等信息。
> - 支持分页查询，可按时间顺序获取多条违规记录。
> - 适用于创作者账号违规风险管理、账号健康监控和数据合规审计。
>
> ### 备注:
> - 此接口仅适用于 TikTok Shop 创作者账号。
> - 支持分页查询，每次默认返回最新的违规记录。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - page: 整数类型，页码，默认为第 1 页
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - `records`（违规记录列表）:
>   - `record_id`: 违规记录 ID
>   - `violation_time`: 违规发生时间（Unix 时间戳）
>   - `violation_info`:
>     - `violation_reason`: 违规原因描述
>     - `violation_detail`: 违规详情描述
>     - `violation_suggestion`: 平台提供的整改建议
>     - `policy_url`: 相关政策链接
>     - `violation_type`: 违规类别（如视频违规）
>   - `record_status`: 记录状态（1 表示有效）
>   - `appeal_status`: 申诉状态（0=未申诉，1=已申诉）
>   - `enforcement_title`: 平台针对违规采取的执行措施描述（例如扣分、佣金冻结等）
>   - `appeal_valid_time`: 申诉有效截止时间（Unix 时间戳）
>   - `can_appeal`: 是否允许发起申诉（布尔值）
> - `total`: 总违规记录数
> - `has_more`: 是否还有更多数据
> - `start_time`: 查询起始时间
> - `end_time`: 查询结束时间
> - `creator_status`: 创作者账号状态码（如 0=正常）
>
> # [English]
> ### Purpose:
> - Retrieve the violation history of a TikTok Shop creator account, providing details about past violations and corresponding enforcement actions.
> - The returned violation records include violation type, violation time, violation reasons, enforcement actions, appeal status, and eligibility for appeal.
> - Pagination is supported to retrieve multiple records in chronological order.
> - Suitable for creator account risk management, health monitoring, and compliance auditing.
>
> ### Notes:
> - This API is available only for TikTok Shop creator accounts.
> - Pagination is supported; by default, it retrieves the latest violation records.
>
> ### Parameters:
> - cookie: User's Cookie string for authentication
> - page: Integer, page number (default is `1`)
> - proxy: Optional HTTP proxy address, can be omitted if not needed
>     - Example format: `http://username:password@host:port`
>
> ### Response:
> - `records`: List of violation records:
>   - `record_id`: Unique ID of the violation record
>   - `violation_time`: Time when the violation occurred (Unix timestamp)
>   - `violation_info`:
>     - `violation_reason`: Reason for the violation
>     - `violation_detail`: Detailed description (may be empty)
>     - `violation_suggestion`: Recommended corrective action
>     - `policy_url`: Link to the related policy
>     - `violation_type`: Type of violation (e.g., Video violation)
>   - `record_status`: Record status (1 = active)
>   - `appeal_status`: Appeal status (0 = not appealed, 1 = appealed)
>   - `enforcement_title`: List of enforcement actions taken (e.g., point assignment, commission withholding)
>   - `appeal_valid_time`: Deadline for submitting an appeal (Unix timestamp)
>   - `can_appeal`: Whether the record is eligible for appeal (boolean)
> - `total`: Total number of violation records
> - `has_more`: Whether there are more records to fetch
> - `start_time`: Query start time
> - `end_time`: Query end time
> - `creator_status`: Creator account status code (e.g., 0 = normal)
>
> # [示例/Example]
> ```json
> {
>     "cookie": "your_cookie_here",
>     "page": 1
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `page`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| page | integer | 否 | 页码/Page Number | 1 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-creator-account-info"></a>
### `POST /api/u1/v1/tiktok/creator/get_creator_account_info`

- 摘要：获取创作者账号信息/Get Creator Account Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_account_info_api_v1_tiktok_creator_get_creator_account_info_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号的基础信息，包括用户名、头像链接、账号ID、注册地区、绑定合作伙伴信息、权限列表等。
> - 可用于账号状态验证、账号信息展示、合作关系检查及后续业务逻辑处理。
>
> ### 备注:
> - 适用于所有 TikTok 创作者账号。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `user_id`: 用户ID（字符串）
> - `user_type`: 用户类型（数字，代表账号类型）
> - `register_region_id`: 注册地区代码（如 "us"）
> - `user_name`: 用户名
> - `avatar`: 头像信息对象
>   - `uri`: 头像资源URI
>   - `url_list`: 头像图片URL列表
> - `permission_list`: 权限列表（整数数组）
> - `partner_id`: 合作伙伴ID
> - `partner_name`: 合作伙伴名称
> - `shop_account_official`: 是否为官方认证店铺账号（布尔值）
> - `switch_info`: 功能开关信息（如直播功能开关，字符串格式）
> - `tt_uid`: TikTok UID（字符串）
> - `nick_name`: 昵称
> - `live_streamer_menu_experiment`: 直播菜单实验字段（字符串，可能为空）
> - `experiment_variants`: 实验变种配置（对象）
>
> # [English]
> ### Purpose:
> - Retrieve basic information of a TikTok Shop creator account, including username, avatar URLs, account ID, register region, partner binding info, and permission list.
> - Useful for verifying account status, displaying user profile data, checking partner binding status, and determining access permissions for business processes.
>
> ### Notes:
> - Applicable to all TikTok creator accounts.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - proxy: Optional HTTP proxy address, can be omitted if not used
>     - Example format: `http://username:password@host:port`
>
> ### Return Content Description:
> - `user_id`: User ID (string)
> - `user_type`: User type (integer, indicates account type)
> - `register_region_id`: Registered region code (e.g., "us")
> - `user_name`: Username
> - `avatar`: Avatar info object
>   - `uri`: Avatar resource URI
>   - `url_list`: List of avatar image URLs
> - `permission_list`: Permission list (list of integers)
> - `partner_id`: Partner ID
> - `partner_name`: Partner name
> - `shop_account_official`: Whether it's an official shop account (boolean)
> - `switch_info`: Feature switch info (e.g., live event switch, string format)
> - `tt_uid`: TikTok UID (string)
> - `nick_name`: Nickname
> - `live_streamer_menu_experiment`: Live streamer menu experiment field (string, may be empty)
> - `experiment_variants`: Experiment variant configurations (object)
>
> # [示例/Example]
> ```json
> {
>   "cookie": "your_cookie"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-live-analytics-summary"></a>
### `POST /api/u1/v1/tiktok/creator/get_live_analytics_summary`

- 摘要：获取创作者直播概览/Get Creator Live Overview
- 能力：创作者 / 数据分析 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_live_overview_api_v1_tiktok_creator_get_live_analytics_summary_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号在指定时间范围内的直播表现数据概览。
> - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。
>
> ### 返回内容说明:
> - `segments`（分段数据列表）:
>   - `time_selector`: 时间范围设置（周期、起止时间戳、时区、语言）
>   - `filter.creator_id`: 创作者 ID
>   - `timed_stats`: 每个时间段（通常按日或月分段）的直播表现数据，包含：
>     - `live_revenue.amount`: 直播带货收入
>     - `live_show_gpm.amount`: 直播场均带货收入
>     - `new_follower_cnt`: 新增粉丝数量
>     - `sku_order_paid_cnt`: 已付款 SKU 数量
>     - `item_sold_cnt`: 成交商品件数
>     - `product_view`: 商品曝光次数（浏览量）
>     - `product_click`: 商品点击次数
>     - `live_pay_order_ucnt`: 直播支付订单人数
>     - `live_ctr`: 直播点击率（Click-Through Rate）
>     - `live_co`: 直播转化率（Conversion Rate）
>     - `live_like_cnt`: 直播点赞次数
>     - `live_comment_cnt`: 直播评论次数
>     - `live_show_cnt`: 直播场次
>     - `live_watch_cnt`: 直播观看人数
>
> ### 备注:
> - 此接口仅适用于 TikTok Shop 创作者账号。
> - 直播期间数据按自然日拆分。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询开始时间（格式 `MM-DD-YYYY`），如 `04-01-2025`
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - 创作者账号直播数据概览
>
> # [English]
> ### Purpose:
> - Retrieve a summary of live streaming performance for a TikTok Shop creator account within a specified time range.
> - By default, it covers one full calendar month starting from the provided `start_date` (e.g., input `04-01-2025` will fetch data for the entire April 2025).
>
> ### Response Fields:
> - `segments` (List of segmented data):
>   - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
>   - `filter.creator_id`: Creator ID
>   - `timed_stats`: Live performance statistics per time segment, including:
>     - `live_revenue.amount`: Live streaming revenue
>     - `live_show_gpm.amount`: Average revenue per live show
>     - `new_follower_cnt`: Number of new followers
>     - `sku_order_paid_cnt`: Number of SKUs paid
>     - `item_sold_cnt`: Number of items sold
>     - `product_view`: Number of product views
>     - `product_click`: Number of product clicks
>     - `live_pay_order_ucnt`: Number of unique users who placed live orders
>     - `live_ctr`: Live Click-Through Rate (CTR)
>     - `live_co`: Live Conversion Rate (CO)
>     - `live_like_cnt`: Number of live likes
>     - `live_comment_cnt`: Number of live comments
>     - `live_show_cnt`: Number of live sessions
>     - `live_watch_cnt`: Number of live viewers
>
> ### Notes:
> - This API is only applicable to TikTok Shop creator accounts.
> - Data is split by natural days during the live sessions.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - start_date: Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`
> - proxy: Optional HTTP proxy address, can be omitted if not used
>     - Example format: `http://username:password@host:port`
>
> ### Return:
> - Creator live streaming performance overview
>
> # [示例/Example]
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-product-analytics-list"></a>
### `POST /api/u1/v1/tiktok/creator/get_product_analytics_list`

- 摘要：获取创作者商品列表分析/Get Creator Product List Analytics
- 能力：创作者 / 电商 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_analytics_list_api_v1_tiktok_creator_get_product_analytics_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号在指定时间范围内推广的商品列表及其销售数据分析。
> - 支持按商品成交额、商品上架时间排序，可分页查询。
>
> ### 返回内容说明:
> - `segments`（分段数据列表）:
>   - `filter.creator_id`: 创作者账号 ID
>   - `list_control`:
>     - `rules`: 列表排序规则（如按成交额、商品 ID 排序）
>     - `next_pagination`: 翻页信息（是否还有更多页、下一页页码、总页数、总记录数）
>   - `timed_lists`: 每个时间段内的商品数据，包括：
>     - `product`:
>       - `id`: 商品 ID
>       - `name`: 商品标题
>       - `cover_image.thumb_url_list`: 商品封面图列表
>     - `item_sold_cnt`: 销售商品数量
>     - `revenue.amount`: 该商品带来的总成交金额（GMV）
>     - `commission.amount`: 该商品预估佣金收入
>
> ### 备注:
> - 此接口仅适用于 TikTok Shop 创作者账号。
> - 数据以自然月或自定义时间范围统计。
> - 默认排序为成交额（GMV）从高到低。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 开始日期，格式为 'YYYY-MM-DD'，如 '2025-04-01'
> - end_date: 结束日期，格式为 'YYYY-MM-DD'，如 '2025-05-01'
> - page: 页码，默认为第一页 `0`
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - 创作者账号商品列表及商品销售分析数据
>
> # [English]
> ### Purpose:
> - Retrieve the list of products promoted by a TikTok Shop creator account within a specified time range, along with their sales analytics.
> - Supports sorting by revenue or product publish time and allows pagination.
>
> ### Response Fields:
> - `segments` (List of segmented data):
>   - `filter.creator_id`: Creator account ID
>   - `list_control`:
>     - `rules`: Sorting rules (e.g., by revenue, by product ID)
>     - `next_pagination`: Pagination info (has more pages, next page number, total pages, total records)
>   - `timed_lists`: List of product statistics within each time range, including:
>     - `product`:
>       - `id`: Product ID
>       - `name`: Product title
>       - `cover_image.thumb_url_list`: List of product thumbnail URLs
>     - `item_sold_cnt`: Number of items sold
>     - `revenue.amount`: Total Gross Merchandise Value (GMV) generated by the product
>     - `commission.amount`: Estimated commission income from the product
>
> ### Notes:
> - This API is only available for TikTok Shop creator accounts.
> - Data is aggregated by natural month or the customized date range.
> - Default sorting is by GMV in descending order.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - start_date: Start date, formatted as 'YYYY-MM-DD', e.g., '2025-04-01'
> - end_date: End date, formatted as 'YYYY-MM-DD', e.g., '2025-05-01'
> - page: Page number, default is the first page `0`
> - proxy: Optional HTTP proxy address, can be omitted if not used
>     - Example format: `http://username:password@host:port`
>
> ### Return:
> - Creator product list and corresponding sales analytics data
>
> # [示例/Example]
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "2025-04-01",
>   "end_date": "2025-05-01",
>   "page": 0
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `end_date`:string, `page`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 开始日期，如 '2025-04-01'/ Start Date, e.g. '2025-04-01' | 2025-04-01 | 无 | 无 |
| end_date | string | 否 | 结束日期，如 '2025-05-01'/ End Date, e.g. '2025-05-01' | 2025-05-01 | 无 | 无 |
| page | integer | 否 | 页码/Page Number | 0 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-product-related-videos"></a>
### `POST /api/u1/v1/tiktok/creator/get_product_related_videos`

- 摘要：获取同款商品关联视频/Get Product Related Videos
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_related_videos_api_v1_tiktok_creator_get_product_related_videos_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取与指定商品关联的所有视频列表和对应的互动数据（如点赞数、评论数、分享数）。
> - 可用于分析同款商品在不同创作者视频中的推广效果和差异。
> - 支持按时间筛选，默认查询指定 start_date 所在自然月内的数据。
>
> ### 备注:
> - 必须同时提供 item_id（当前视频 ID）和 product_id（商品 ID）。
> - 返回数据按时间范围查询，同一商品下的其他视频列表。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - item_id: 当前视频 ID，例如 "7496499484705246507"
> - product_id: 商品 ID，例如 "1731050202505515549"
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `segments`（数据分段列表）:
>   - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
>   - `filter`: 查询条件（creator_id, product_id, item_id）
>   - `timed_lists`: 视频列表
>     - `start_timestamp`: 开始时间戳
>     - `end_timestamp`: 结束时间戳
>     - `stats`:
>       - `video_product_id`: 商品 ID
>       - `video`:
>         - `item_id`: 视频 ID
>         - `video_id`: 视频内部唯一 ID
>         - `name`: 视频文案标题
>         - `publish_time`: 发布时间戳
>         - `duration`: 视频时长（秒）
>         - `video_play_info`:
>           - `post_url`: 视频封面图片链接
>           - `video_infos.main_url`: 视频播放地址
>       - `video_like_cnt`: 视频点赞数
>       - `video_comment_cnt`: 视频评论数
>       - `video_share_cnt`: 视频分享数
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507",
>   "product_id": "1731050202505515549"
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve the list of all videos associated with a specified product along with their interaction metrics (such as like count, comment count, share count).
> - Useful for analyzing the promotional effectiveness and differences of the same product across different creators' videos.
> - Supports time-based filtering, defaulting to the calendar month of the specified start_date.
>
> ### Notes:
> - Requires both item_id (current video ID) and product_id (product ID).
> - Returns a list of other videos where the same product is featured.
>
> ### Return Description:
> - `segments`:
>   - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
>   - `filter`: Query conditions (creator_id, product_id, item_id)
>   - `timed_lists`: List of related videos
>     - `start_timestamp`: Start timestamp
>     - `end_timestamp`: End timestamp
>     - `stats`:
>       - `video_product_id`: Product ID
>       - `video`:
>         - `item_id`: Video ID
>         - `video_id`: Video internal ID
>         - `name`: Video caption/title
>         - `publish_time`: Publish timestamp
>         - `duration`: Video duration (seconds)
>         - `video_play_info`:
>           - `post_url`: Video cover image link
>           - `video_infos.main_url`: Main video URL
>       - `video_like_cnt`: Like count
>       - `video_comment_cnt`: Comment count
>       - `video_share_cnt`: Share count
>
> ### Example Request Body:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507",
>   "product_id": "1731050202505515549"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| item_id | string | 是 | 视频 ID/Video ID | 无 | 无 | 无 |
| product_id | string | 是 | 商品 ID/Product ID | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-showcase-product-list"></a>
### `POST /api/u1/v1/tiktok/creator/get_showcase_product_list`

- 摘要：获取橱窗商品列表/Get Showcase Product List
- 能力：创作者 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_showcase_product_list_api_v1_tiktok_creator_get_showcase_product_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号橱窗中正在展示的商品列表。
> - 可用于商品管理、数据分析、查看当前推广商品等场景。
>
> ### 备注:
> - 仅适用于已开通橱窗功能的 TikTok Shop 创作者账号。
> - 支持分页查询，通过 `count` 和 `offset` 控制数据量。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - count: 每页返回商品数量，默认 20
> - offset: 分页偏移量，默认 0
> - proxy: 可选 HTTP 代理地址
>     - 示例: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `products` (List[Dict]): 商品列表，每项包含以下字段：
>   - `product_id` (str): 商品ID
>   - `title` (str): 商品标题
>   - `format_available_price` (str): 商品展示价格（格式化后的字符串，如 `$7.94`）
>   - `seller_info` (dict):
>     - `seller_id` (str): 卖家ID
>     - `shop_name` (str): 店铺名称
>   - `cover` (dict): 主图信息
>     - `url_list` (List[str]): 主图 URL 列表（300x300）
>   - `images` (List[dict]): 图片列表
>     - 每张图片包含 `url_list` (原图 URL)
>   - `source` (str): 商品来源渠道（如 `Affiliate`）
>   - `stock_status` (int): 库存状态（1: 有货）
>   - `review_status` (int): 审核状态（1: 通过）
>   - `affiliate_info` (dict): 联盟佣金信息
>     - `commission_with_currency` (str): 佣金金额（如 `$0.95`）
>     - `commission_rate` (int): 佣金比例（如 1200 = 12%）
>   - `category_info` (dict): 类目信息
>     - `name` (str): 主分类名（如 `Beauty & Personal Care`）
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie_string",
>   "count": 20,
>   "offset": 0
> }
> ```
>
> ### 示例返回数据片段:
> ```json
> {
>   "products": [
>     {
>       "product_id": "1730905148396180014",
>       "title": "Car Paint Care Spray",
>       "format_available_price": "$7.94",
>       "seller_info": {
>         "seller_id": "7496108716782225966",
>         "shop_name": "moon moon shop shop"
>       },
>       "cover": {
>         "url_list": [
>           "https://example.com/xxx.jpg"
>         ]
>       },
>       "images": [
>         {
>           "url_list": [
>             "https://example.com/xxx.jpg"
>           ]
>         }
>       ],
>       "source": "Affiliate",
>       "stock_status": 1,
>       "review_status": 1,
>       "affiliate_info": {
>         "commission_with_currency": "$0.95",
>         "commission_rate": 1200
>       },
>       "category_info": {
>         "name": "Beauty & Personal Care"
>       }
>     }
>   ]
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve the list of products currently displayed in a TikTok Shop creator's showcase.
> - Useful for product management, analytics, and monitoring promoted items.
>
> ### Notes:
> - Only available for TikTok creator accounts with the showcase feature enabled.
> - Supports pagination via `count` and `offset`.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - count: Number of products per page (default 20)
> - offset: Pagination offset (default 0)
> - proxy: Optional HTTP proxy address
>     - Example: `http://username:password@host:port`
>
> ### Return Structure:
> - `products` (List[Dict]): List of showcased products, including:
>   - `product_id`, `title`, `format_available_price`, `seller_info`, `cover`, `images`, `source`, `stock_status`, `review_status`, `affiliate_info`, `category_info`.
>
> ### Example Request:
> ```json
> {
>   "cookie": "your_cookie_string",
>   "count": 20,
>   "offset": 0
> }
> ```
>
> ### Example Response Snippet:
> ```json
> {
>   "products": [
>     {
>       "product_id": "1730905148396180014",
>       "title": "Car Paint Care Spray",
>       "format_available_price": "$7.94",
>       "seller_info": {
>         "seller_id": "7496108716782225966",
>         "shop_name": "moon moon shop shop"
>       },
>       "cover": {
>         "url_list": [
>           "https://example.com/xxx.jpg"
>         ]
>       },
>       "images": [...],
>       "source": "Affiliate",
>       "stock_status": 1,
>       "review_status": 1,
>       "affiliate_info": {
>         "commission_with_currency": "$0.95",
>         "commission_rate": 1200
>       },
>       "category_info": {
>         "name": "Beauty & Personal Care"
>       }
>     }
>   ]
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `count`:integer, `offset`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| count | integer | 否 | 每页数量/Page Size | 20 | 无 | 无 |
| offset | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-analytics-summary"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_analytics_summary`

- 摘要：获取创作者视频概览/Get Creator Video Overview
- 能力：创作者 / 作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_analytics_summary_api_v1_tiktok_creator_get_video_analytics_summary_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号在指定时间范围内的视频表现概览。
> - 默认统计从调用当天向前 30 天的数据（或按平台设定的自然月分段）。
> - 适合用于视频表现分析，例如视频数量、播放量、粉丝增长、成交数据等。
>
> ### 返回内容说明:
> - `segments`（分段数据列表）:
>   - `time_selector`: 时间范围设置信息（周期、起止时间戳、时区、语言）
>   - `filter.creator_id`: 创作者账号 ID
>   - `timed_stats`: 每个时间段的视频表现数据，包含：
>     - `vv_cnt`: 视频播放量（Video Views Count）
>     - `new_follower_cnt`: 新增粉丝数量
>     - `video_cnt`: 发布视频数量
>     - `gmv.amount`: 视频带货产生的 GMV 金额
>     - `items_sold`: 售出商品数量
>
> ### 备注:
> - 此接口仅适用于 TikTok Shop 创作者账号。
> - 如果某个时间段无数据，返回的 `stats` 字段可能为空 `{}`。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - 创作者账号视频表现概览
>
> # [English]
> ### Purpose:
> - Retrieve a video performance overview for a TikTok Shop creator account over a specified time range.
> - By default, the API fetches data for the past 30 days (or full calendar month based on the platform settings).
> - Useful for analyzing metrics like video count, views, new followers, and generated GMV.
>
> ### Response Fields:
> - `segments` (List of segmented data):
>   - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
>   - `filter.creator_id`: Creator account ID
>   - `timed_stats`: Video performance statistics for each time segment, including:
>     - `vv_cnt`: Video Views Count
>     - `new_follower_cnt`: Number of new followers
>     - `video_cnt`: Number of videos published
>     - `gmv.amount`: Gross Merchandise Value generated by videos
>     - `items_sold`: Number of items sold
>
> ### Notes:
> - This API is only available for TikTok Shop creator accounts.
> - If no data is available for a time segment, the `stats` field might be an empty `{}`.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - proxy: Optional HTTP proxy address, can be omitted if not used
>     - Example format: `http://username:password@host:port`
>
> ### Return:
> - Creator account video performance overview
>
> # [示例/Example]
> ```json
> {
>   "cookie": "your_cookie"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-associated-product-list"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_associated_product_list`

- 摘要：获取视频关联商品列表/Get Video Associated Product List
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_associated_product_list_api_v1_tiktok_creator_get_video_associated_product_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定视频在 TikTok Shop 中关联展示的商品列表及其推广表现数据。
> - 可用于分析每个视频挂载商品的数量、商品价格区间、商品跳转链接，以及商品销售和推广效果。
>
> ### 备注:
> - 必须提供 item_ids（视频 ID 列表）。
> - 时间范围默认使用 start_date 所在自然月。
> - 支持单次查询多个视频，返回每个视频关联的所有商品信息及对应商品的推广数据。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - item_ids: 视频 ID 列表，例如 ["7496499484705246507", "7496110433699482923"]
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `segments`（分段数据列表）:
>   - `time_selector`: 时间筛选信息（起止时间戳）
>   - `filter`: 查询条件（视频 ID 列表）
>   - `timed_lists`: 每个时间段下的视频商品关联列表
>     - `videoToProductsMap`:
>       - `item_id`: 视频 ID
>       - `products`: 关联商品列表
>         - `id`: 商品 ID
>         - `name`: 商品名称
>         - `cover_image.thumb_url_list`: 商品图片 URL 列表
>         - `product_detail_page_url`: 商品跳转链接
>         - `price_min` / `price_max`: 商品价格区间
>       - `stats`:
>         - `product.id`: 商品 ID
>         - 商品销售推广表现（如销量、点击率等）
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_ids": ["7496499484705246507", "7496110433699482923"]
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve the list of products associated with specified videos on TikTok Shop, along with their promotional performance data.
> - Useful for analyzing the number of products linked to each video, the product price range, product detail page links, and sales performance metrics.
>
> ### Notes:
> - Requires item_ids (list of video IDs).
> - The time range defaults to the calendar month of the specified start_date.
> - Supports querying multiple videos at once.
>
> ### Return Description:
> - `segments`:
>   - `time_selector`: Time filter information (start/end timestamps)
>   - `filter`: Query conditions (video ID list)
>   - `timed_lists`: Product list associated with videos in the selected time range
>     - `videoToProductsMap`:
>       - `item_id`: Video ID
>       - `products`:
>         - `id`: Product ID
>         - `name`: Product name
>         - `cover_image.thumb_url_list`: List of product image URLs
>         - `product_detail_page_url`: Product detail page link
>         - `price_min` / `price_max`: Price range
>       - `stats`:
>         - `product.id`: Product ID
>         - Promotional performance metrics (e.g., sales volume, CTR)
>
> ### Example Request Body:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_ids": ["7496499484705246507", "7496110433699482923"]
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_ids*`[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| item_ids | array<string> | 是 | 视频 ID 列表/Video ID List | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-audience-stats"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_audience_stats`

- 摘要：获取视频受众分析数据/Get Video Audience Analysis Data
- 能力：创作者 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_audience_stats_api_v1_tiktok_creator_get_video_audience_stats_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定 TikTok 视频观众的用户画像统计数据，包括性别分布、年龄分布、地区分布等维度。
> - 可用于精准了解视频观众群体特征，指导内容创作、商品选择和营销策略优化。
> - 支持按时间段（日/周/月）分析变化趋势。
>
> ### 备注:
> - 此接口需要提供 item_id（视频 ID）。
> - 受众画像数据来源于观看和互动用户的统计特征。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - item_id: 视频 ID，例如 "7496499484705246507"
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `segments`（数据分段列表）:
>   - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
>   - `filter`: 查询条件（creator_id, item_id）
>   - `timed_profile`: 分段画像统计数据
>     - `start_timestamp`: 开始时间戳
>     - `end_timestamp`: 结束时间戳
>     - `stats`:
>       - `follower_genders`: 性别分布
>         - `key`: 性别（female/male）
>         - `value`: 占比（字符串，0-1）
>       - `follower_ages`: 年龄段分布
>         - `key`: 年龄段（如 "18-24", "25-34", 等）
>         - `value`: 占比（字符串，0-1）
>       - `follower_regions`: 地区分布
>         - `key`: 国家代码（如 "US"）
>         - `value`: 占比（字符串，0-1）
>       - `profile_type`: 画像类型，固定值 2（受众画像）
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507"
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve audience profile statistics for a specified TikTok video, including gender distribution, age distribution, and regional distribution.
> - Useful for accurately understanding the characteristics of the video audience to guide content creation, product selection, and marketing strategy optimization.
> - Supports trend analysis across different time intervals (daily/weekly/monthly).
>
> ### Notes:
> - Requires item_id (video ID).
> - Audience profile data is based on characteristics of users who viewed and interacted with the video.
>
> ### Return Description:
> - `segments`:
>   - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
>   - `filter`: Query conditions (creator_id, item_id)
>   - `timed_profile`: Audience profile statistics
>     - `start_timestamp`: Start timestamp
>     - `end_timestamp`: End timestamp
>     - `stats`:
>       - `follower_genders`: Gender distribution
>         - `key`: Gender ("female" or "male")
>         - `value`: Proportion (string, range 0-1)
>       - `follower_ages`: Age group distribution
>         - `key`: Age group (e.g., "18-24", "25-34")
>         - `value`: Proportion (string, range 0-1)
>       - `follower_regions`: Regional distribution
>         - `key`: Country code (e.g., "US")
>         - `value`: Proportion (string, range 0-1)
>       - `profile_type`: Profile type, fixed value 2 (Audience Profile)
>
> ### Example Request Body:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| item_id | string | 是 | 视频 ID/Video ID | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-detailed-stats"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_detailed_stats`

- 摘要：获取视频详细分段统计数据/Get Video Detailed Statistics
- 能力：创作者 / 作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_detailed_stats_api_v1_tiktok_creator_get_video_detailed_stats_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定 TikTok 视频在指定自然月内的详细分段统计数据。
> - 支持按时间段（日/周/月）统计新粉丝、点赞、评论、分享、商品浏览、完播率等多维指标。
> - 可用于深入分析单个视频在不同时间段的表现变化，优化内容策略和推广效果。
>
> ### 备注:
> - 必须提供 item_id（视频 ID）。
> - 时间范围基于 start_date 所在自然月。
> - 若数据量大，返回的数据将按不同时间粒度分段统计（granularity=日/周/月）。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - item_id: 视频 ID，例如 "7496499484705246507"
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `segments`（数据分段列表）:
>   - `time_selector`: 时间筛选条件（period, granularity, start_timestamp, end_timestamp）
>   - `filter`: 查询条件（creator_id, item_id）
>   - `timed_stats`: 按时间段返回的统计数据列表
>     - `start_timestamp`: 开始时间戳
>     - `end_timestamp`: 结束时间戳
>     - `stats`:
>       - `creator_id`: 创作者账号 ID
>       - `item_id`: 视频 ID
>       - `new_follower_cnt`: 新增粉丝数量
>       - `share_cnt`: 分享次数
>       - `comment_cnt`: 评论次数
>       - `like_cnt`: 点赞次数
>       - `product_view_cnt`: 商品浏览量
>       - `video_completion_rate`: 视频完播率（字符串，0-1）
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507"
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve detailed segmented statistics for a specified TikTok video within a given calendar month.
> - Supports analyzing new followers, likes, comments, shares, product views, and video completion rates across different time segments (daily/weekly/monthly).
> - Useful for deeply analyzing the performance changes of a single video over time, optimizing content strategies and promotional outcomes.
>
> ### Notes:
> - Requires item_id (video ID).
> - Time range is based on the calendar month of start_date.
> - Large datasets will be automatically segmented based on granularity (daily/weekly/monthly).
>
> ### Return Description:
> - `segments`:
>   - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
>   - `filter`: Query conditions (creator_id, item_id)
>   - `timed_stats`: Segmented statistics list
>     - `start_timestamp`: Start timestamp
>     - `end_timestamp`: End timestamp
>     - `stats`:
>       - `creator_id`: Creator ID
>       - `item_id`: Video ID
>       - `new_follower_cnt`: Number of new followers
>       - `share_cnt`: Number of shares
>       - `comment_cnt`: Number of comments
>       - `like_cnt`: Number of likes
>       - `product_view_cnt`: Number of product views
>       - `video_completion_rate`: Video completion rate (string, range 0-1)
>
> ### Example Request Body:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| item_id | string | 是 | 视频 ID/Video ID | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-list-analytics"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_list_analytics`

- 摘要：获取创作者视频列表分析/Get Creator Video List Analytics
- 能力：创作者 / 作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_list_api_v1_tiktok_creator_get_video_list_analytics_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取 TikTok Shop 创作者账号在指定时间范围内发布的视频列表及其详细数据表现。
> - 支持分页查询，每页返回指定时间段内的视频及其播放、成交等详细数据。
>
> ### 返回内容说明:
> - `segments`（分段数据列表）:
>   - `time_selector`: 查询时间范围（起止时间戳、时区、语言等）
>   - `filter.creator_id`: 创作者账号 ID
>   - `list_control`:
>     - `rules`: 列表排序规则（通常按发布时间降序）
>     - `next_pagination`: 翻页信息（是否有更多页，当前页，总页数，总记录数）
>   - `timed_lists`: 每个时间段内的视频数据，包括：
>     - `video_meta`:
>       - `item_id`: 视频 Item ID
>       - `name`: 视频标题
>       - `publish_time`: 视频发布时间（Unix 时间戳）
>       - `duration`: 视频时长（秒）
>       - `video_play_info`: 视频播放资源信息（封面图、播放链接等）
>     - `new_follower_cnt`: 视频期间新增粉丝数
>     - `vv_cnt`: 视频播放量
>     - `ctr`: 商品点击率（Click Through Rate）
>     - `gmv.amount`: 视频带货产生的总 GMV 金额
>     - `item_sold_cnt`: 视频带动的商品售出数量
>     - `direct_gmv.amount`: 直接带货 GMV
>     - `completion_rate`: 视频观看完成率
>
> ### 备注:
> - 此接口仅适用于 TikTok Shop 创作者账号。
> - 数据按自然日或周分组，且每条视频数据对应一段时间内的统计值。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - page: 页码，默认为第一页 `0`
> - rules: 列表排序规则，默认按发布时间排序，可选值如下：
>     - `"VIDEO_LIST_PUBLISH_TIME"`：按发布时间排序
>     - `"VIDEO_LIST_GMV"`：按商品交易总额排序
>     - `"VIDEO_LIST_DIRECT_GMV"`：按直接商品交易总额排序
>     - `"VIDEO_LIST_VV_CNT"`：按观看人次数排序
>     - `"VIDEO_LIST_ITEM_SOLD_CNT"`：按成交件数排序
>     - `"VIDEO_LIST_CTR"`：按商品点击率排序
>     - `"VIDEO_LIST_COMPLETION_RATE"`：按观看完播率排序
>     - `"VIDEO_LIST_LIKE_CNT"`：按点赞数排序
>     - `"VIDEO_LIST_NEW_FOLLOWER_CNT"`：按新增粉丝数排序
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回:
> - 创作者账号视频列表及详细分析数据
>
> # [English]
> ### Purpose:
> - Retrieve a list of videos published by a TikTok Shop creator account within a specified time range, along with detailed performance metrics.
> - Supports pagination to fetch multiple pages of video records within the given time range.
>
> ### Response Fields:
> - `segments` (List of segmented data):
>   - `time_selector`: Time range settings (start/end timestamps, timezone, locale)
>   - `filter.creator_id`: Creator account ID
>   - `list_control`:
>     - `rules`: List sorting rules (typically by publish time descending)
>     - `next_pagination`: Pagination information (has more pages, current page, total pages, total records)
>   - `timed_lists`: List of videos for each time range, including:
>     - `video_meta`:
>       - `item_id`: Video Item ID
>       - `name`: Video title
>       - `publish_time`: Video publish time (Unix timestamp)
>       - `duration`: Video duration (seconds)
>       - `video_play_info`: Video play resources (cover image, playback URL, etc.)
>     - `new_follower_cnt`: Number of new followers during the video's period
>     - `vv_cnt`: Video views count
>     - `ctr`: Click Through Rate for associated products
>     - `gmv.amount`: Gross Merchandise Value generated by the video
>     - `item_sold_cnt`: Number of items sold due to the video
>     - `direct_gmv.amount`: Direct GMV from the video
>     - `completion_rate`: Video completion rate
>
> ### Notes:
> - This API is only available for TikTok Shop creator accounts.
> - Data is grouped by natural day or week, and each video's stats represent the corresponding period.
>
> ### Parameters:
> - cookie: User Cookie string for authentication
> - start_date: Query start date, formatted as 'MM-DD-YYYY', e.g., '04-01-2025'
> - page: Page number, default is the first page `0`
> - rules: List sorting rules, default is by publish time. Available options:
>     - `"VIDEO_LIST_PUBLISH_TIME"`: Sort by video publish time
>     - `"VIDEO_LIST_GMV"`: Sort by gross merchandise value (GMV)
>     - `"VIDEO_LIST_DIRECT_GMV"`: Sort by direct GMV
>     - `"VIDEO_LIST_VV_CNT"`: Sort by video view count
>     - `"VIDEO_LIST_ITEM_SOLD_CNT"`: Sort by number of items sold
>     - `"VIDEO_LIST_CTR"`: Sort by click-through rate
>     - `"VIDEO_LIST_COMPLETION_RATE"`: Sort by video completion rate
>     - `"VIDEO_LIST_LIKE_CNT"`: Sort by number of likes
>     - `"VIDEO_LIST_NEW_FOLLOWER_CNT"`: Sort by number of new followers
> - proxy: Optional HTTP proxy address, can be omitted if not used
>     - Example format: `http://username:password@host:port`
>
> ### Return:
> - Detailed video list and performance analysis for the creator account
>
> # [示例/Example]
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "page": 0
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `page`:integer, `rules`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| page | integer | 否 | 页码/Page Number | 0 | 无 | 无 |
| rules | string | 否 | 列表排序规则，默认按发布时间排序/ List sorting rule, default is by publish time | VIDEO_LIST_PUBLISH_TIME | 无 | 无 |

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

<a id="post-api-u1-v1-tiktok-creator-get-video-to-product-stats"></a>
### `POST /api/u1/v1/tiktok/creator/get_video_to_product_stats`

- 摘要：获取视频与商品关联统计数据/Get Video-Product Association Statistics
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_to_product_stats_api_v1_tiktok_creator_get_video_to_product_stats_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定 TikTok 视频与指定商品关联的推广详细统计数据。
> - 支持分析视频为商品带来的商品浏览量、点击量、销售量、订单量、商品收入、直接收入等多维度指标。
> - 返回数据按时间段（日/周/月）分段统计，便于观察趋势变化。
>
> ### 备注:
> - 必须同时提供 item_id（视频 ID）和 product_id（商品 ID）。
> - 时间范围基于 start_date 所在自然月。
>
> ### 参数:
> - cookie: 用户 Cookie 字符串（用于身份认证）
> - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
> - item_id: 视频 ID，例如 "7496499484705246507"
> - product_id: 商品 ID，例如 "1731050202505515549"
> - proxy: 可选 HTTP 代理地址，如不使用可省略
>     - 示例格式: `http://username:password@host:port`
>
> ### 返回内容说明:
> - `segments`（数据分段列表）:
>   - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
>   - `filter`: 查询条件（creator_id, item_id, product_id）
>   - `timed_stats`: 按时间段分段的统计数据
>     - `start_timestamp`: 时间段开始时间戳
>     - `end_timestamp`: 时间段结束时间戳
>     - `stats`:
>       - `item_id`: 视频 ID
>       - `product_id`: 商品 ID
>       - `product_revenue.amount_formatted`: 商品产生的总收入（格式化字符串，如 "$100.00"）
>       - `product_revenue.amount`: 商品产生的总收入（数值）
>       - `direct_revenue.amount_formatted`: 直接成交产生的收入（格式化字符串）
>       - `product_sales_cnt`: 商品销售数量
>       - `product_view_cnt`: 商品浏览量
>       - `product_click_cnt`: 商品点击量
>       - `order_cnt`: 生成订单数量
>
> ### 示例请求体:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507",
>   "product_id": "1731050202505515549"
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve detailed promotional statistics between a specific TikTok video and a specific product.
> - Supports analyzing metrics such as product views, clicks, sales, order counts, product revenue, and direct revenue.
> - The data is segmented by time intervals (daily/weekly/monthly) to observe trends over time.
>
> ### Notes:
> - Requires both item_id (video ID) and product_id (product ID).
> - The time range is based on the calendar month of the specified start_date.
>
> ### Return Description:
> - `segments`:
>   - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
>   - `filter`: Query conditions (creator_id, item_id, product_id)
>   - `timed_stats`: Segmented statistics list
>     - `start_timestamp`: Start timestamp
>     - `end_timestamp`: End timestamp
>     - `stats`:
>       - `item_id`: Video ID
>       - `product_id`: Product ID
>       - `product_revenue.amount_formatted`: Total product revenue (formatted string, e.g., "$100.00")
>       - `product_revenue.amount`: Total product revenue (numeric)
>       - `direct_revenue.amount_formatted`: Direct sales revenue (formatted string)
>       - `product_sales_cnt`: Number of products sold
>       - `product_view_cnt`: Number of product views
>       - `product_click_cnt`: Number of product clicks
>       - `order_cnt`: Number of orders created
>
> ### Example Request Body:
> ```json
> {
>   "cookie": "your_cookie",
>   "start_date": "04-01-2025",
>   "item_id": "7496499484705246507",
>   "product_id": "1731050202505515549"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String | Your_Cookie_String | 无 | 无 |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address | 无 | 无 | 无 |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' | 04-01-2025 | 无 | 无 |
| item_id | string | 是 | 视频 ID/Video ID | 无 | 无 | 无 |
| product_id | string | 是 | 商品 ID/Product ID | 无 | 无 | 无 |

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
