# Douyin-Creator-V2-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-creator-v2-api.md`](../api-tags/douyin-creator-v2-api.md)
- 当前契约文件：`api-contracts/douyin-creator-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`14`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音创作者V2数据接口（需要用户Cookie，可获取作品流量总览等数据）/Douyin-Creator-V2-API data endpoints (Requires user Cookie, can get item traffic overview data))**

## 路由契约

<a id="post-api-u1-v1-douyin-creator-v2-fetch-author-diagnosis"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis`

- 摘要：获取创作者账号诊断/Fetch author diagnosis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_author_diagnosis_api_v1_douyin_creator_v2_fetch_author_diagnosis_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者账号的诊断数据和优化建议
> - 自动分析最近一周（从当天起往前7天）的账号表现
> - 提供完播率、互动指数等关键指标的评估和改进建议
> - 帮助创作者了解账号健康度，优化内容策略
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
> - **无需指定时间范围，系统自动获取最近7天数据**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
>
> ### 数据更新时间:
> - **更新周期**: 次日12点更新昨日作品数据
> - **示例**: 2025年10月10日的作品数据会在2025年10月11日12点更新
> - **时间范围**: 自动获取最近一周的数据（从当天起往前7天）
> - **首次使用**: 获取权限后次日起生产数据
>
> ### 数据指标含义:
>
> **名词定义**:
> - **同类创作者**: 具有相似创作领域或粉丝量级的创作者
> - **时间粒度**: 时间粒度是数据更新计算的周期
> - **抖音精选**: 包含精选APP+抖音电脑端+抖音APP_精选Tab的数据表现
>
> **账号诊断类指标**:
> - **投稿数**: 根据统计周期内发布的作品个数得出
> - **互动指数**: 作品的观看、点赞、评论、转发的综合得分
> - **视频播放量**: 作品被观看的次数
> - **视频完播率**: 作品完整播放次数的占比
>   - 每日完播率：当日完播浏览量与总浏览量的比值
>   - 每十分钟级完播率：累计完播浏览量与累计浏览量的比值
> - **粉丝净增量**: 账号净增粉丝数，通过涨粉数减去掉粉数得出
>
> ### 返回数据说明:
> 返回账号诊断数据，包括以下五个核心维度：
>
> **1. 互动指数 (Interact)**:
> - **OwnValue**: 账号自身的互动指数值（观看、点赞、评论、转发的综合得分）
> - **SimilarCount**: 同类创作者总数
> - **AuthorRank**: 账号在自身历史数据中的排名百分位（0-1之间，越大表示当前表现越好）
> - **SimilarRank**: 账号在同类创作者中的排名百分位（0-1之间，越大表示排名越靠前）
> - **SimilarValue**: 同类创作者的平均互动指数值
> - **解读**: AuthorRank=0.26表示当前互动指数超过了自己历史26%的时期
> - **解读**: SimilarRank=0.52表示在同类创作者中排名超过52%
>
> **2. 粉丝净增量 (NewFans)**:
> - **OwnValue**: 统计周期内账号净增粉丝数（涨粉数 - 掉粉数）
> - **SimilarCount**: 同类创作者总数
> - **AuthorRank**: 账号在自身历史涨粉数据中的排名百分位
> - **SimilarRank**: 账号在同类创作者中的涨粉排名百分位
> - **SimilarValue**: 同类创作者的平均粉丝净增量
> - **解读**: OwnValue=2表示本周期净增2个粉丝
>
> **3. 视频播放量 (PlayCnt)**:
> - **OwnValue**: 统计周期内作品被观看的总次数
> - **SimilarCount**: 同类创作者总数
> - **AuthorRank**: 账号在自身历史播放量中的排名百分位
> - **SimilarRank**: 账号在同类创作者中的播放量排名百分位
> - **SimilarValue**: 同类创作者的平均播放量
> - **解读**: OwnValue=192表示本周期总播放量为192次
>
> **4. 视频完播率 (PlayFinishRatio)**:
> - **OwnValue**: 作品完整播放次数的占比（0-1之间的小数）
> - **SimilarCount**: 同类创作者总数
> - **AuthorRank**: 账号在自身历史完播率中的排名百分位
> - **SimilarRank**: 账号在同类创作者中的完播率排名百分位
> - **SimilarValue**: 同类创作者的平均完播率
> - **解读**: OwnValue=0.15表示完播率为15%
> - **提升建议**: "想要作品吸引人，前3秒钟是关键，可以多分析同行业热门作品的人设、镜头技巧和音乐"
>
> **5. 投稿活跃度 (PublishActivation)**:
> - **OwnValue**: 统计周期内发布的作品个数
> - **SimilarCount**: 同类创作者总数
> - **AuthorRank**: 账号在自身历史投稿数据中的排名百分位
> - **SimilarRank**: 账号在同类创作者中的投稿活跃度排名百分位
> - **SimilarValue**: 同类创作者的平均投稿数
> - **解读**: OwnValue=2表示本周期发布了2个作品
>
> ### 返回数据结构示例:
> ```json
> {
>     "code": 0,
>     "data": {
>         "Interact": {
>             "OwnValue": 0.0052,
>             "SimilarCount": 1494654282,
>             "AuthorRank": 0.2633,
>             "SimilarRank": 0.5169,
>             "SimilarValue": 0.0909
>         },
>         "NewFans": {
>             "OwnValue": 2,
>             "AuthorRank": 0.7924,
>             "SimilarRank": 0.6343
>         },
>         "PlayCnt": {
>             "OwnValue": 192,
>             "AuthorRank": 0.8427,
>             "SimilarRank": 0.5132
>         },
>         "PlayFinishRatio": {
>             "OwnValue": 0.1545,
>             "AuthorRank": 0.3851,
>             "SimilarRank": 0.5086
>         },
>         "PublishActivation": {
>             "OwnValue": 2,
>             "AuthorRank": 0.7345,
>             "SimilarRank": 0.5675
>         }
>     }
> }
> ```
>
> ### 数据解读技巧:
> - **OwnValue**: 查看实际数值，了解账号当前表现
> - **AuthorRank**: 与自己过去比较，数值越高说明当前状态越好
> - **SimilarRank**: 与同行比较，数值越高说明在同类创作者中排名越靠前
> - **建议**: AuthorRank和SimilarRank都低于0.5时需要重点优化该项指标
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin creator account diagnosis data and optimization suggestions
> - Automatically analyze account performance for the past 7 days
> - Provide assessment and improvement suggestions for key metrics
> - Help creators understand account health and optimize content strategy
> - **This API requires valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie transmitted in request body, more secure**
> - **No need to specify time range, system automatically fetches data for past 7 days**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required)
>
> ### Data Update Time:
> - **Update Cycle**: Yesterday's video data is updated at 12:00 noon the next day
> - **Example**: Video data from October 10, 2025 will be updated at 12:00 on October 11, 2025
> - **Time Range**: Automatically fetches data for the past 7 days
> - **First Use**: Data generation starts from the next day after obtaining permission
>
> ### Data Metrics Definition:
>
> **Term Definitions**:
> - **Similar Creators**: Creators with similar creation fields or fan levels
> - **Time Granularity**: The period for data update calculations
> - **Douyin Featured**: Data performance including Featured APP + Douyin Desktop + Douyin APP Featured Tab
>
> **Account Diagnosis Metrics**:
> - **Submission Count**: Number of works published during the statistical period
> - **Engagement Index**: Comprehensive score of views, likes, comments, and shares
> - **Video Views**: Number of times the work has been viewed
> - **Video Completion Rate**: Proportion of complete playbacks
>   - Daily completion rate: Ratio of daily complete views to total views
>   - 10-minute completion rate: Ratio of cumulative complete views to cumulative views
> - **Net Fan Growth**: Net increase in account followers (new followers minus unfollowers)
>
> ### Return Data Description:
> Account diagnosis data including five core dimensions:
>
> **1. Engagement Index (Interact)**:
> - **OwnValue**: Account's own engagement index value (comprehensive score of views, likes, comments, shares)
> - **SimilarCount**: Total number of similar creators
> - **AuthorRank**: Ranking percentile in account's historical data (0-1, higher means better current performance)
> - **SimilarRank**: Ranking percentile among similar creators (0-1, higher means better ranking)
> - **SimilarValue**: Average engagement index value of similar creators
> - **Interpretation**: AuthorRank=0.26 means current engagement exceeds 26% of own history
> - **Interpretation**: SimilarRank=0.52 means ranking exceeds 52% of similar creators
>
> **2. Net Fan Growth (NewFans)**:
> - **OwnValue**: Net increase in followers during the period (new followers - unfollowers)
> - **SimilarCount**: Total number of similar creators
> - **AuthorRank**: Ranking percentile in account's historical fan growth data
> - **SimilarRank**: Fan growth ranking percentile among similar creators
> - **SimilarValue**: Average net fan growth of similar creators
> - **Interpretation**: OwnValue=2 means net gain of 2 followers in this period
>
> **3. Video Views (PlayCnt)**:
> - **OwnValue**: Total number of times works were viewed during the period
> - **SimilarCount**: Total number of similar creators
> - **AuthorRank**: Ranking percentile in account's historical view count
> - **SimilarRank**: View count ranking percentile among similar creators
> - **SimilarValue**: Average view count of similar creators
> - **Interpretation**: OwnValue=192 means total views of 192 in this period
>
> **4. Video Completion Rate (PlayFinishRatio)**:
> - **OwnValue**: Proportion of complete playbacks (decimal between 0-1)
> - **SimilarCount**: Total number of similar creators
> - **AuthorRank**: Ranking percentile in account's historical completion rate
> - **SimilarRank**: Completion rate ranking percentile among similar creators
> - **SimilarValue**: Average completion rate of similar creators
> - **Interpretation**: OwnValue=0.15 means 15% completion rate
> - **Tip**: Focus on first 3 seconds to improve retention
>
> **5. Publishing Activity (PublishActivation)**:
> - **OwnValue**: Number of works published during the period
> - **SimilarCount**: Total number of similar creators
> - **AuthorRank**: Ranking percentile in account's historical publishing data
> - **SimilarRank**: Publishing activity ranking percentile among similar creators
> - **SimilarValue**: Average number of submissions by similar creators
> - **Interpretation**: OwnValue=2 means published 2 works in this period
>
> ### Return Data Structure Example:
> ```json
> {
>     "code": 0,
>     "data": {
>         "Interact": {
>             "OwnValue": 0.0052,
>             "SimilarCount": 1494654282,
>             "AuthorRank": 0.2633,
>             "SimilarRank": 0.5169,
>             "SimilarValue": 0.0909
>         },
>         "NewFans": {
>             "OwnValue": 2,
>             "AuthorRank": 0.7924,
>             "SimilarRank": 0.6343
>         },
>         "PlayCnt": {
>             "OwnValue": 192,
>             "AuthorRank": 0.8427,
>             "SimilarRank": 0.5132
>         },
>         "PlayFinishRatio": {
>             "OwnValue": 0.1545,
>             "AuthorRank": 0.3851,
>             "SimilarRank": 0.5086
>         },
>         "PublishActivation": {
>             "OwnValue": 2,
>             "AuthorRank": 0.7345,
>             "SimilarRank": 0.5675
>         }
>     }
> }
> ```
>
> ### Data Interpretation Tips:
> - **OwnValue**: Check actual values to understand current account performance
> - **AuthorRank**: Compare with own past, higher value means better current status
> - **SimilarRank**: Compare with peers, higher value means better ranking among similar creators
> - **Recommendation**: Focus on optimizing metrics when both AuthorRank and SimilarRank are below 0.5
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-involved-vertical"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical`

- 摘要：获取作品垂类标签/Fetch item analysis involved vertical
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_involved_vertical_api_v1_douyin_creator_v2_fetch_item_analysis_involved_vertical_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定时间段内投稿作品涉及的垂类标签
> - 用于后续调用投稿分析接口时的参数
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - start_date: 开始日期，格式YYYYMMDD（必填）
> - end_date: 结束日期，格式YYYYMMDD（必填）
> - **注意：日期范围最多90天**
>
> ### 返回数据说明:
> - primary_verticals: 垂类标签列表
>   - 返回该账号在指定时间段内发布的作品涉及的垂类
>   - 例如：["动物", "美食", "旅游"]
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get the vertical tags involved in submitted items within the specified time period
> - Used as parameters for subsequent calls to the submission analysis interface
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - start_date: Start date in YYYYMMDD format (required)
> - end_date: End date in YYYYMMDD format (required)
> - **Note: Date range maximum 90 days**
>
> ### Return Data Description:
> - primary_verticals: List of vertical tags
>   - Returns the verticals involved in items published during the specified time period
>   - Example: ["Animals", "Food", "Travel"]
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_date": "20250713",
>     "end_date": "20251011"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "primary_verticals": ["动物", "美食", "旅游"],
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> - primary_verticals列表包含该账号投稿作品涉及的所有垂类
> - 如果返回空列表，说明该时间段内没有投稿或垂类未分类
> - 获取到垂类后，可用于投稿分析接口的primary_verticals参数
>
> ### 注意事项/Notes:
> - 日期格式必须为YYYYMMDD（8位数字）
> - 时间跨度不能超过90天
> - 建议先调用此接口获取垂类，再调用投稿分析接口
> - 如果时间范围内无投稿，可能返回空列表

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) | 无 | 20250713 | 无 |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) | 无 | 20251011 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-item-performance"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance`

- 摘要：获取投稿表现数据/Fetch item analysis item performance
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_item_performance_api_v1_douyin_creator_v2_fetch_item_analysis_item_performance_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取投稿作品的表现数据，包括播放量、点赞量、评论量、分享量等指标
> - 分析不同体裁和垂类的内容表现
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
> - **建议先调用 fetch_item_analysis_involved_vertical 接口获取垂类标签**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - start_date: 开始日期，格式YYYYMMDD（必填）
> - end_date: 结束日期，格式YYYYMMDD（必填）
> - genres: 体裁类型列表（可选，默认包含所有体裁）
>   - 1: 1分钟以内视频
>   - 2: 1-3分钟视频
>   - 3: 3-5分钟视频
>   - 4: 5分钟以上视频
>   - 5: 图文
>   - 8: 长图文
> - primary_verticals: 垂类标签列表（必填，从 fetch_item_analysis_involved_vertical 接口获取）
> - metric_type: 指标类型（可选，默认为1）
>   - 1: 播放量 (Views)
>   - 2: 点赞量 (Likes)
>   - 3: 评论量 (Comments)
>   - 4: 分享量 (Shares)
> - **注意：日期范围最多90天**
>
> ### 返回数据说明:
> - 包含所选指标在不同体裁和垂类下的表现数据
> - 趋势分析、对比数据等
> - 帮助了解内容在各个维度的表现
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get performance data for submitted items, including views, likes, comments, shares, etc.
> - Analyze content performance across different genres and verticals
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
> - **Recommend calling fetch_item_analysis_involved_vertical first to get vertical tags**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - start_date: Start date in YYYYMMDD format (required)
> - end_date: End date in YYYYMMDD format (required)
> - genres: Genre type list (optional, defaults to all genres)
>   - 1: Videos under 1 minute
>   - 2: 1-3 minute videos
>   - 3: 3-5 minute videos
>   - 4: Videos over 5 minutes
>   - 5: Photo posts
>   - 8: Long photo posts
> - primary_verticals: Vertical tag list (required, obtained from fetch_item_analysis_involved_vertical)
> - metric_type: Metric type (optional, defaults to 1)
>   - 1: Views
>   - 2: Likes
>   - 3: Comments
>   - 4: Shares
> - **Note: Date range maximum 90 days**
>
> ### Return Data Description:
> - Contains performance data for selected metrics across different genres and verticals
> - Trend analysis and comparison data
> - Helps understand content performance across various dimensions
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_date": "20250713",
>     "end_date": "20251011",
>     "genres": [2, 3, 4, 5, 8],
>     "primary_verticals": ["动物"],
>     "metric_type": 1
> }
> ```
>
> ### 指标类型说明/Metric Type Description:
> - **metric_type=1 (播放量/Views)**: 查看作品的播放量表现
> - **metric_type=2 (点赞量/Likes)**: 查看作品的点赞量表现
> - **metric_type=3 (评论量/Comments)**: 查看作品的评论量表现
> - **metric_type=4 (分享量/Shares)**: 查看作品的分享量表现
>
> ### 体裁类型说明/Genre Type Description:
> - **1**: 1分钟以内视频（短视频）- 快速吸引注意力
> - **2**: 1-3分钟视频（中短视频）- 平衡内容与时长
> - **3**: 3-5分钟视频（中视频）- 深度内容展示
> - **4**: 5分钟以上视频（长视频）- 完整故事叙述
> - **5**: 图文（图片+文字）- 静态内容展示
> - **8**: 长图文（多图片+长文字）- 深度图文内容
>
> ### 使用流程/Usage Flow:
> 1. 先调用 `fetch_item_analysis_involved_vertical` 获取垂类标签
> 2. 使用返回的 primary_verticals 作为参数
> 3. 选择需要分析的指标类型 (metric_type)
> 4. 调用本接口获取投稿表现数据
> 5. 分析不同体裁和垂类的表现差异
>
> ### 数据解读/Data Interpretation:
> - **播放量 (metric_type=1)**: 反映内容的曝光度和吸引力
> - **点赞量 (metric_type=2)**: 反映内容的质量和受欢迎程度
> - **评论量 (metric_type=3)**: 反映内容的互动性和话题性
> - **分享量 (metric_type=4)**: 反映内容的传播力和价值
>
> ### 优化建议/Optimization Suggestions:
> 1. **播放量优化**:
>    - 优化标题和封面，提高点击率
>    - 选择合适的发布时间
>    - 利用热门话题和标签
>
> 2. **点赞量优化**:
>    - 提升内容质量，引发共鸣
>    - 在视频中引导点赞
>    - 创作有价值、有趣的内容
>
> 3. **评论量优化**:
>    - 设置互动话题，引导评论
>    - 在评论区积极回复
>    - 创作有争议或讨论性的内容
>
> 4. **分享量优化**:
>    - 创作有价值、实用的内容
>    - 制作有趣、有共鸣的内容
>    - 适当加入情感元素
>
> 5. **体裁选择**:
>    - 根据不同指标表现选择合适的体裁
>    - 短视频适合快速传播
>    - 中长视频适合深度内容
>    - 图文适合知识分享
>
> 6. **垂类聚焦**:
>    - 专注于表现好的垂类
>    - 分析垂类特点和受众偏好
>    - 持续优化内容方向
>
> ### 注意事项/Notes:
> - 日期格式必须为YYYYMMDD（8位数字）
> - 时间跨度不能超过90天
> - primary_verticals参数必须从 fetch_item_analysis_involved_vertical 接口获取
> - 如果时间范围内无投稿，可能返回空数据
> - genres参数可以自由组合，按需筛选体裁
> - 不同metric_type展示不同维度的表现数据
> - 建议结合多个指标综合分析内容表现
> - 数据分析建议至少有7天以上的投稿数据

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string], `metric_type`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) | 无 | 20250713 | 无 |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) | 无 | 20251011 | 无 |
| genres | array<integer> | 否 | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 | [1, 2, 3, 4, 5, 8] | [2, 3, 4, 5, 8] | 无 |
| primary_verticals | array<string> | 是 | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) | 无 | ["动物"] | 无 |
| metric_type | integer | 否 | 指标类型/Metric type: 1=播放量(Views), 2=点赞量(Likes), 3=评论量(Comments), 4=分享量(Shares) | 1 | 1 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-overview"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview`

- 摘要：获取投稿分析概览/Fetch item analysis overview
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_overview_api_v1_douyin_creator_v2_fetch_item_analysis_overview_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取账号投稿作品的综合分析数据
> - 包括不同体裁、垂类的投稿表现统计
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
> - **建议先调用 fetch_item_analysis_involved_vertical 接口获取垂类标签**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - start_date: 开始日期，格式YYYYMMDD（必填）
> - end_date: 结束日期，格式YYYYMMDD（必填）
> - genres: 体裁类型列表（可选，默认包含所有体裁）
>   - 1: 1分钟以内视频
>   - 2: 1-3分钟视频
>   - 3: 3-5分钟视频
>   - 4: 5分钟以上视频
>   - 5: 图文
>   - 8: 长图文
> - primary_verticals: 垂类标签列表（必填，从 fetch_item_analysis_involved_vertical 接口获取）
> - **注意：日期范围最多90天**
>
> ### 返回数据说明:
> - 包含不同体裁和垂类的投稿数据分析
> - 播放量、点赞量、评论量、分享量等指标
> - 不同体裁的内容表现对比
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get comprehensive analysis data for account submitted items
> - Including submission performance statistics for different genres and verticals
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
> - **Recommend calling fetch_item_analysis_involved_vertical first to get vertical tags**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - start_date: Start date in YYYYMMDD format (required)
> - end_date: End date in YYYYMMDD format (required)
> - genres: Genre type list (optional, defaults to all genres)
>   - 1: Videos under 1 minute
>   - 2: 1-3 minute videos
>   - 3: 3-5 minute videos
>   - 4: Videos over 5 minutes
>   - 5: Photo posts
>   - 8: Long photo posts
> - primary_verticals: Vertical tag list (required, obtained from fetch_item_analysis_involved_vertical)
> - **Note: Date range maximum 90 days**
>
> ### Return Data Description:
> - Contains submission data analysis for different genres and verticals
> - Metrics including views, likes, comments, shares, etc.
> - Performance comparison of different genres
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_date": "20250713",
>     "end_date": "20251011",
>     "genres": [1, 2, 3, 4, 5, 8],
>     "primary_verticals": ["动物"]
> }
> ```
>
> ### 体裁类型说明/Genre Type Description:
> - **1**: 1分钟以内视频（短视频）
> - **2**: 1-3分钟视频（中短视频）
> - **3**: 3-5分钟视频（中视频）
> - **4**: 5分钟以上视频（长视频）
> - **5**: 图文（图片+文字）
> - **8**: 长图文（多图片+长文字）
>
> ### 使用流程/Usage Flow:
> 1. 先调用 `fetch_item_analysis_involved_vertical` 获取垂类标签
> 2. 使用返回的 primary_verticals 作为参数
> 3. 调用本接口获取投稿分析数据
> 4. 分析不同体裁和垂类的表现
>
> ### 数据解读/Data Interpretation:
> - 可以看到不同体裁内容的表现差异
> - 了解哪种体裁更受欢迎
> - 分析垂类内容的表现趋势
> - 优化内容创作方向
>
> ### 优化建议/Optimization Suggestions:
> 1. **体裁优化**: 根据数据选择表现更好的体裁类型
> 2. **内容时长**: 分析观众偏好的视频时长
> 3. **垂类聚焦**: 专注于表现好的垂类领域
> 4. **内容多样化**: 尝试不同体裁和垂类的组合
> 5. **发布策略**: 根据不同体裁的表现调整发布频率
>
> ### 注意事项/Notes:
> - 日期格式必须为YYYYMMDD（8位数字）
> - 时间跨度不能超过90天
> - primary_verticals参数必须从 fetch_item_analysis_involved_vertical 接口获取
> - 如果时间范围内无投稿，可能返回空数据
> - genres参数可以自由组合，按需筛选体裁
> - 数据分析建议至少有7天以上的投稿数据

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) | 无 | 20250713 | 无 |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) | 无 | 20251011 | 无 |
| genres | array<integer> | 否 | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 | [1, 2, 3, 4, 5, 8] | [1, 2, 3, 4, 5, 8] | 无 |
| primary_verticals | array<string> | 是 | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) | 无 | ["动物"] | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-audience-others"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_others`

- 摘要：获取作品观众其他数据分析/Fetch item audience others analysis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_audience_others_api_v1_douyin_creator_v2_fetch_item_audience_others_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的观众其他数据分析，包括受众分布和受众关注词
> - 了解观众是否为粉丝，以及观众关注的兴趣话题
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
>
> ### 返回数据说明:
> - **audience_distribution (受众分布)**:
>   - fan_list: 粉丝占比列表
>     - key: "1"=粉丝, "0"=非粉丝
>     - value: 占比（0-1之间的小数）
>
> - **audience_keyword (受众关注词)**:
>   - keyword_list: 观众关注的话题/关键词列表
>     - keyword: 关键词内容
>     - value: 该关键词的关注度占比
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item audience other data analysis, including audience distribution and audience keywords
> - Understand whether the audience are fans and what topics they are interested in
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
>
> ### Return Data Description:
> - **audience_distribution (Audience Distribution)**:
>   - fan_list: Fan proportion list
>     - key: "1"=Fan, "0"=Non-fan
>     - value: Proportion (decimal between 0-1)
>
> - **audience_keyword (Audience Keywords)**:
>   - keyword_list: List of topics/keywords that audiences are interested in
>     - keyword: Keyword content
>     - value: Interest proportion for this keyword
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "audience_distribution": {
>         "fan_list": [
>             {
>                 "key": "1",
>                 "value": 0.156
>             },
>             {
>                 "key": "0",
>                 "value": 0.844
>             }
>         ]
>     },
>     "audience_keyword": {
>         "keyword_list": [
>             {
>                 "keyword": "美食",
>                 "value": 0.35
>             },
>             {
>                 "keyword": "旅游",
>                 "value": 0.28
>             },
>             {
>                 "keyword": "生活",
>                 "value": 0.22
>             },
>             {
>                 "keyword": "娱乐",
>                 "value": 0.15
>             }
>         ]
>     },
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
>
> **受众分布 (audience_distribution)**:
> - key="1": 表示粉丝，value=0.156 表示15.6%的观众是已关注的粉丝
> - key="0": 表示非粉丝，value=0.844 表示84.4%的观众是未关注的路人
> - 粉丝占比高说明内容对现有粉丝吸引力强
> - 非粉丝占比高说明作品破圈能力强，吸引了很多新观众
>
> **受众关注词 (audience_keyword)**:
> - keyword_list展示观众群体关注的其他话题
> - 可以了解观众的兴趣偏好，用于内容规划
> - 示例中观众主要关注"美食"(35%)、"旅游"(28%)等话题
> - 可以结合这些关键词创作相关内容，提高吸引力
>
> ### 优化建议/Optimization Suggestions:
> 1. **粉丝维护**: 如果粉丝占比高(>30%)，说明内容符合粉丝预期，继续保持风格
> 2. **破圈拓展**: 如果非粉丝占比高(>80%)，说明内容有爆款潜力，可加大推广
> 3. **内容规划**: 根据audience_keyword规划相关主题内容，覆盖观众兴趣点
> 4. **跨界合作**: 结合高占比关键词，进行跨领域内容创作
> 5. **粉丝转化**: 对于非粉丝占比高的爆款作品，在评论区引导关注
> 6. **兴趣匹配**: 关注观众兴趣词与作品内容的匹配度，调整内容方向
> 7. **话题借势**: 利用观众关注的热门话题，制作相关内容蹭热度
> 8. **受众画像**: 结合关注词描绘完整的受众兴趣画像
>
> ### 注意事项/Notes:
> - 观众数据需要一定播放量才准确，建议作品有1000+播放后查看
> - 数据可能有延迟，通常在作品发布24-48小时后更新
> - 粉丝占比与作品是否爆款无关，重点看内容质量和推广效果
> - 受众关注词反映的是观众整体兴趣，不一定与当前作品主题相关
> - 如果返回空列表，说明该作品目前暂无足够数据
> - 结合其他数据（如观众画像）综合分析效果更好

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-audience-portrait"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait`

- 摘要：获取作品观众数据分析/Fetch item audience portrait
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_audience_portrait_api_v1_douyin_creator_v2_fetch_item_audience_portrait_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的观众数据分析
> - 了解观看作品的用户画像特征
> - 包含活跃分布、性别分布、地域分布、年龄分布等多维度数据
> - 帮助创作者精准定位目标受众，优化内容策略
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
>
> ### 返回数据说明:
> 返回作品的观众画像数据，包括以下维度：
>
> **1. 活跃分布 (active)**:
> - key: 活跃时段标识（"2"=上午, "3"=下午, "4"=晚上, "-1"=其他）
> - value: 该时段的活跃用户占比（0-1之间的小数）
>
> **2. 性别分布 (gender)**:
> - ratio_list: 性别占比列表
>   - key: "male"（男性）或 "female"（女性）
>   - value: 该性别用户占比（0-1之间的小数）
> - tgi_list: 性别TGI指数列表（Target Group Index，目标群体指数）
>   - key: 性别标识
>   - value: TGI值（100为平均水平，>100表示高于平均）
>
> **3. 地域分布 (province)**:
> - ratio_list: 省份占比列表
>   - key: 省份名称（如"浙江"、"广东"、"北京"）
>   - value: 该省份用户占比（0-1之间的小数）
> - tgi_list: 省份TGI指数列表
>   - key: 省份名称
>   - value: TGI值（反映该地区用户的活跃度）
>
> **4. 年龄分布 (age)**:
> - ratio_list: 年龄段占比列表
>   - key: 年龄段（"-18", "18-23", "24-30", "31-40", "41-50", "50-"）
>   - value: 该年龄段用户占比（0-1之间的小数）
> - tgi_list: 年龄段TGI指数列表
>   - key: 年龄段
>   - value: TGI值（反映该年龄段用户的偏好度）
>
> **5. 其他维度**:
> - career: 职业分布（可能为空）
> - city_level: 城市等级分布（包含ratio_list和tgi_list）
> - new_user: 新用户占比（可能为空）
>
> **TGI指数说明**:
> - TGI = 100: 该群体表现与平台平均水平一致
> - TGI > 100: 该群体在此作品中的占比高于平台平均，是核心受众
> - TGI < 100: 该群体在此作品中的占比低于平台平均
> - TGI越高，说明该群体对此类内容越感兴趣
>
> **注意**: 如果某些数据为空或占比为0，可能原因：
> - 作品刚发布，样本量不足
> - 该维度暂无数据或数据未达到统计阈值
> - 某些地区或年龄段的用户较少
>
> ### 数据价值:
> - **精准定位**: 了解核心受众群体特征
> - **内容优化**: 根据受众特点调整内容风格和主题
> - **发布时机**: 根据活跃时间优化发布时间
> - **地域策略**: 针对主要地域用户定制内容
> - **年龄适配**: 调整内容深度和表达方式
> - **性别偏好**: 理解不同性别用户的内容偏好
>
> ### 应用场景:
> 1. **内容定位**: 根据主要受众群体调整内容方向
> 2. **发布优化**: 在目标受众活跃时段发布作品
> 3. **地域营销**: 针对主要地域用户进行本地化内容创作
> 4. **年龄策略**: 根据年龄分布调整内容复杂度和话题
> 5. **性别营销**: 平衡或侧重特定性别受众的内容设计
> 6. **受众拓展**: 识别潜力受众群体，扩大影响力
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item audience portrait data
> - Understand viewer demographic characteristics
> - Includes active distribution, gender distribution, region distribution, age distribution
> - Help creators precisely target audiences and optimize content strategy
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
>
> ### Return Data Description:
> Returns audience portrait data with multiple dimensions:
>
> **1. Active Distribution (active)**:
> - key: Time period identifier ("2"=morning, "3"=afternoon, "4"=evening, "-1"=other)
> - value: Active user ratio in this period (decimal between 0-1)
>
> **2. Gender Distribution (gender)**:
> - ratio_list: Gender ratio list
>   - key: "male" or "female"
>   - value: Gender user ratio (decimal between 0-1)
> - tgi_list: Gender TGI index list (Target Group Index)
>   - key: Gender identifier
>   - value: TGI value (100=average, >100=above average)
>
> **3. Region Distribution (province)**:
> - ratio_list: Province ratio list
>   - key: Province name (e.g., "浙江", "广东", "北京")
>   - value: Province user ratio (decimal between 0-1)
> - tgi_list: Province TGI index list
>   - key: Province name
>   - value: TGI value (reflects regional user activity)
>
> **4. Age Distribution (age)**:
> - ratio_list: Age range ratio list
>   - key: Age range ("-18", "18-23", "24-30", "31-40", "41-50", "50-")
>   - value: Age range user ratio (decimal between 0-1)
> - tgi_list: Age range TGI index list
>   - key: Age range
>   - value: TGI value (reflects age group preference)
>
> **5. Other Dimensions**:
> - career: Career distribution (may be empty)
> - city_level: City level distribution (contains ratio_list and tgi_list)
> - new_user: New user ratio (may be empty)
>
> **TGI Index Explanation**:
> - TGI = 100: Group performance matches platform average
> - TGI > 100: Group ratio is higher than platform average, core audience
> - TGI < 100: Group ratio is lower than platform average
> - Higher TGI indicates greater interest in this content type
>
> **Note**: If some data is empty or zero, possible reasons:
> - Item just published with insufficient sample size
> - No data available for this dimension or below statistical threshold
> - Few users in certain regions or age groups
>
> ### Data Value:
> - **Precise Targeting**: Understand core audience characteristics
> - **Content Optimization**: Adjust content style based on audience traits
> - **Publishing Timing**: Optimize publish time based on active periods
> - **Regional Strategy**: Customize content for main regional users
> - **Age Adaptation**: Adjust content depth and expression
> - **Gender Preference**: Understand content preferences by gender
>
> ### Application Scenarios:
> 1. **Content Positioning**: Adjust content direction based on main audience
> 2. **Publishing Optimization**: Publish during target audience active hours
> 3. **Regional Marketing**: Create localized content for main regions
> 4. **Age Strategy**: Adjust content complexity based on age distribution
> 5. **Gender Marketing**: Balance or focus on specific gender audiences
> 6. **Audience Expansion**: Identify potential audience groups to expand influence
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "active": [
>         {
>             "key": "2",
>             "value": 0.0949367088607595
>         },
>         {
>             "key": "3",
>             "value": 0.15822784810126583
>         },
>         {
>             "key": "4",
>             "value": 0.6962025316455697
>         },
>         {
>             "key": "-1",
>             "value": 0.05063291139240506
>         }
>     ],
>     "gender": {
>         "ratio_list": [
>             {
>                 "key": "male",
>                 "value": 0.7612903225806451
>             },
>             {
>                 "key": "female",
>                 "value": 0.23870967741935484
>             }
>         ],
>         "tgi_list": [
>             {
>                 "key": "male",
>                 "value": 135.47066238136884
>             },
>             {
>                 "key": "female",
>                 "value": 54.49489346627035
>             }
>         ]
>     },
>     "province": {
>         "ratio_list": [
>             {
>                 "key": "浙江",
>                 "value": 0.24050632911392406
>             },
>             {
>                 "key": "江苏",
>                 "value": 0.12025316455696203
>             },
>             {
>                 "key": "广东",
>                 "value": 0.0759493670886076
>             },
>             {
>                 "key": "湖北",
>                 "value": 0.06329113924050633
>             }
>         ],
>         "tgi_list": [
>             {
>                 "key": "浙江",
>                 "value": 379.3041755346526
>             },
>             {
>                 "key": "江苏",
>                 "value": 169.70798949761055
>             },
>             {
>                 "key": "广东",
>                 "value": 70.0324843724158
>             },
>             {
>                 "key": "湖北",
>                 "value": 164.36825973059874
>             }
>         ]
>     },
>     "age": {
>         "ratio_list": [
>             {
>                 "key": "18-23",
>                 "value": 0.3548387096774194
>             },
>             {
>                 "key": "-18",
>                 "value": 0.1935483870967742
>             },
>             {
>                 "key": "31-40",
>                 "value": 0.14838709677419354
>             },
>             {
>                 "key": "50-",
>                 "value": 0.11612903225806452
>             },
>             {
>                 "key": "41-50",
>                 "value": 0.10967741935483871
>             },
>             {
>                 "key": "24-30",
>                 "value": 0.07741935483870968
>             }
>         ],
>         "tgi_list": [
>             {
>                 "key": "-18",
>                 "value": 563.217280988937
>             },
>             {
>                 "key": "18-23",
>                 "value": 191.33476395324902
>             },
>             {
>                 "key": "50-",
>                 "value": 80.07137972518639
>             },
>             {
>                 "key": "41-50",
>                 "value": 73.75840394976595
>             },
>             {
>                 "key": "31-40",
>                 "value": 49.79826524888418
>             },
>             {
>                 "key": "24-30",
>                 "value": 41.07687409864829
>             }
>         ]
>     },
>     "career": [],
>     "city_level": {
>         "ratio_list": [],
>         "tgi_list": []
>     },
>     "new_user": [],
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> **活跃分布 (active)**:
> - key="2": 上午时段（通常指6:00-12:00）
> - key="3": 下午时段（通常指12:00-18:00）
> - key="4": 晚上时段（通常指18:00-24:00）
> - key="-1": 其他时段或未分类
> - value值越高，说明该时段观众越多
> - 示例中晚上时段（key="4"）占比69.6%，是主要观看时段
>
> **性别分布 (gender)**:
> - ratio_list显示实际性别占比
> - tgi_list显示性别偏好度（TGI>100表示该性别用户偏好此内容）
> - 示例中男性占比76.1%，TGI为135.5，说明男性用户是核心受众
> - 女性TGI仅54.5，低于平均水平，可考虑优化以吸引女性用户
>
> **地域分布 (province)**:
> - ratio_list显示各省份用户占比
> - tgi_list显示地域偏好度
> - 示例中浙江占比24%，TGI高达379，说明浙江用户特别喜欢此类内容
> - 江苏、湖北的TGI也较高（>160），是重点地域
> - 可针对高TGI地域制作本地化内容
>
> **年龄分布 (age)**:
> - "-18": 18岁以下，TGI高达563，说明未成年用户特别喜欢
> - "18-23": 18-23岁，占比35.5%，TGI为191，是主力受众
> - "24-30": 24-30岁，TGI仅41，低于平均水平
> - "31-40", "41-50", "50-": 中老年用户占比和TGI都较低
> - 此作品明显偏向年轻化受众
>
> **TGI指数应用**:
> - TGI>150: 高度偏好，是核心目标群体
> - TGI 100-150: 中度偏好，有潜力拓展
> - TGI 50-100: 低度偏好，需要优化内容吸引
> - TGI<50: 不匹配，可能不是目标受众
>
> ### 优化建议/Optimization Suggestions:
> 1. **时间优化**: 根据active数据，在高活跃时段发布（示例中晚上最佳）
> 2. **内容适配**: 根据高TGI年龄段调整内容风格（示例应偏向18-23岁年轻化）
> 3. **性别策略**: 针对高TGI性别深化内容，或优化以平衡性别受众
> 4. **地域营销**: 为高TGI地域（如浙江、江苏）创作本地化内容或方言版本
> 5. **受众拓展**: 关注TGI低的群体（如24-30岁），寻找增长机会
> 6. **精准定位**: 聚焦TGI>150的群体，他们是最有价值的核心受众
> 7. **内容调整**: 如果想拓展受众，需要调整内容以提升低TGI群体的兴趣
> 8. **A/B测试**: 针对不同TGI群体制作差异化内容，测试效果
>
> ### 注意事项/Notes:
> - 观众数据需要一定播放量才准确，建议作品有1000+播放后查看
> - 数据可能有延迟，通常在作品发布24-48小时后更新
> - Index值用于与平台均值对比，帮助识别特色受众
> - 结合作品内容特点和目标受众综合分析
> - 不同内容类型的受众特征差异较大，需要针对性优化

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-danmaku-analysis"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis`

- 摘要：获取作品弹幕分析/Fetch item bullet analysis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_danmaku_analysis_api_v1_douyin_creator_v2_fetch_item_danmaku_analysis_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的弹幕分析数据
> - 了解观众在视频各个时间点的弹幕互动情况
> - 帮助创作者识别视频中的热点片段和观众反应
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
>
> ### 返回数据说明:
> 返回作品的弹幕分析数据，包括：
> - bullet_distribution: 弹幕分布数据
>   - time_point: 时间点（秒）
>   - count: 该时间点的弹幕数量
>   - percentage: 该时间点弹幕占总弹幕的百分比
> - hot_words: 热门弹幕词汇
>   - word: 弹幕词汇
>   - count: 出现次数
>   - sentiment: 情感倾向（正面/负面/中性）
> - total_count: 弹幕总数
> - peak_time: 弹幕高峰时间点
>
> **注意**: 如果返回空数据或弹幕数量为0，说明该作品目前没有弹幕数据，可能原因：
> - 作品刚发布，还没有观众发送弹幕
> - 作品类型不适合弹幕互动
> - 弹幕功能未开启
>
> ### 数据价值:
> - **热点识别**: 识别观众最感兴趣的视频片段
> - **情感分析**: 了解观众对内容的情感反应
> - **互动优化**: 在高弹幕区域优化内容呈现
> - **内容改进**: 根据弹幕反馈调整后续内容
>
> ### 应用场景:
> 1. **内容优化**: 找出观众最喜欢的片段，在后续视频中强化类似内容
> 2. **节奏调整**: 弹幕密集的时间点说明内容吸引人，可以延长类似内容时长
> 3. **情感把控**: 通过弹幕情感分析了解观众真实反应
> 4. **互动设计**: 在弹幕高峰处设计互动环节，提升参与度
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item bullet (danmaku) analysis data
> - Understand audience bullet interaction at various video time points
> - Help creators identify hot segments and audience reactions
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
>
> ### Return Data Description:
> Returns item bullet analysis data, including:
> - bullet_distribution: Bullet distribution data
>   - time_point: Time point (seconds)
>   - count: Number of bullets at this time point
>   - percentage: Percentage of bullets at this time point
> - hot_words: Popular bullet words
>   - word: Bullet word
>   - count: Occurrence count
>   - sentiment: Sentiment orientation (positive/negative/neutral)
> - total_count: Total bullet count
> - peak_time: Peak time point for bullets
>
> **Note**: If empty data or zero bullets returned, it means there is currently no bullet data for this item, possible reasons:
> - Item was just published and no viewers have sent bullets yet
> - Item type is not suitable for bullet interaction
> - Bullet feature is not enabled
>
> ### Data Value:
> - **Hot Spot Identification**: Identify video segments with highest audience interest
> - **Sentiment Analysis**: Understand audience emotional reactions to content
> - **Interaction Optimization**: Optimize content presentation in high-bullet areas
> - **Content Improvement**: Adjust future content based on bullet feedback
>
> ### Application Scenarios:
> 1. **Content Optimization**: Find favorite segments and reinforce similar content
> 2. **Pacing Adjustment**: Dense bullet areas indicate engaging content, extend similar segments
> 3. **Emotion Control**: Understand genuine audience reactions through bullet sentiment
> 4. **Interaction Design**: Design interactive elements at bullet peaks to boost engagement
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "bullet_distribution": [
>         {
>             "time_point": 5,
>             "count": 328,
>             "percentage": 15.2
>         },
>         {
>             "time_point": 12,
>             "count": 562,
>             "percentage": 26.1
>         },
>         {
>             "time_point": 18,
>             "count": 445,
>             "percentage": 20.6
>         }
>     ],
>     "hot_words": [
>         {
>             "word": "哈哈哈",
>             "count": 156,
>             "sentiment": "positive"
>         },
>         {
>             "word": "精彩",
>             "count": 98,
>             "sentiment": "positive"
>         },
>         {
>             "word": "学到了",
>             "count": 76,
>             "sentiment": "positive"
>         }
>     ],
>     "total_count": 2156,
>     "peak_time": 12,
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> - **弹幕分布 (Bullet Distribution)**:
>   - time_point 显示哪个时间点弹幕最密集
>   - count 越高表示该片段越引起观众共鸣
>   - percentage 帮助识别弹幕集中度
>   - 多个弹幕高峰说明视频有多个精彩片段
>
> - **热门词汇 (Hot Words)**:
>   - 高频正面词汇（如"精彩"、"学到了"）说明内容质量好
>   - 负面词汇可能揭示内容问题点
>   - 疑问词汇（如"为什么"）可能是用户困惑点
>
> - **总弹幕数 (Total Count)**:
>   - 弹幕数量反映视频互动热度
>   - 相对播放量的弹幕率可以衡量内容吸引力
>   - 持续增长说明内容有长尾效应
>
> ### 优化建议/Optimization Suggestions:
> 1. **强化高峰**: 在弹幕高峰时间点前后强化内容质量
> 2. **延长精彩**: 延长弹幕密集片段的时长，满足观众期待
> 3. **回应反馈**: 根据热门词汇调整内容方向
> 4. **引导互动**: 在弹幕较少的时间点添加引导性内容
> 5. **情感共鸣**: 多设计能引发正面情感的片段
> 6. **问题解答**: 针对疑问类弹幕在后续视频中解答
>
> ### 注意事项/Notes:
> - 弹幕数据可能有延迟，建议作品发布一段时间后查看
> - 弹幕分析需要一定的样本量才准确，新作品可能数据不足
> - 结合其他指标（互动率、完播率）综合分析效果更好
> - 不同类型内容的弹幕特点不同，需要针对性分析

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-list"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list`

- 摘要：获取投稿作品列表/Fetch item list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_list_api_v1_douyin_creator_v2_fetch_item_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定时间范围内发布的所有投稿作品列表
> - 支持分页查询，每次最多返回100条数据
> - 数据更新说明：
>   - **播放量、点赞量、评论量、分享量、收藏量实时更新**
>   - **其他指标每小时更新一次**
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - start_time: 开始时间戳，单位毫秒（必填）
> - end_time: 结束时间戳，单位毫秒（必填）
> - count: 每页返回的数量，默认10，最多100（可选）
> - order_by: 排序方式，支持26种排序（可选，默认1）
> - fields: 需要返回的字段，默认 "metrics,review,visibility"（可选）
>   - metrics: 流量指标（播放量、点赞量、评论量、分享量、收藏量等）
>   - review: 审核状态
>   - visibility: 可见性状态
> - need_cooperation: 是否需要合作信息，默认true（可选）
> - need_long_article: 是否包含长图文，默认true（可选）
> - cursor: 分页游标，首次请求不传，后续分页使用返回的cursor（可选）
>
> ### 排序方式详解 (order_by):
>
> | 值 | 排序字段 | 排序方向 | 更新频率 | 说明 |
> |----|---------|---------|---------|------|
> | 1 | 发布时间 | 从新到旧 ↓ | - | 默认排序，最新发布的在前 |
> | 2 | 发布时间 | 从旧到新 ↑ | - | 最早发布的在前 |
> | 3 | 播放量 | 从高到低 ↓ | 实时 | 作品被观看的次数 |
> | 4 | 播放量 | 从低到高 ↑ | 实时 | 播放量最少的在前 |
> | 5 | 点赞量 | 从高到低 ↓ | 实时 | 作品获得点赞的次数 |
> | 6 | 点赞量 | 从低到高 ↑ | 实时 | 点赞量最少的在前 |
> | 7 | 评论量 | 从高到低 ↓ | 实时 | 作品获得评论的次数 |
> | 8 | 评论量 | 从低到高 ↑ | 实时 | 评论量最少的在前 |
> | 9 | 分享量 | 从高到低 ↓ | 实时 | 作品获得分享的次数 |
> | 10 | 分享量 | 从低到高 ↑ | 实时 | 分享量最少的在前 |
> | 11 | 收藏量 | 从高到低 ↓ | 实时 | 作品获得收藏的次数 |
> | 12 | 收藏量 | 从低到高 ↑ | 实时 | 收藏量最少的在前 |
> | 13 | 2s跳出率 | 从高到低 ↓ | 每小时 | 播放后2s内跳出的播放量/总播放量 |
> | 14 | 2s跳出率 | 从低到高 ↑ | 每小时 | 2s跳出率最低的在前 |
> | 15 | 5s完播率 | 从高到低 ↓ | 每小时 | 播放后超过5s的播放量/总播放量 |
> | 16 | 5s完播率 | 从低到高 ↑ | 每小时 | 5s完播率最低的在前 |
> | 17 | 完播率 | 从高到低 ↓ | 每小时 | 完整播完的播放量/总播放量 |
> | 18 | 完播率 | 从低到高 ↑ | 每小时 | 完播率最低的在前 |
> | 19 | 封面点击率 | 从高到低 ↓ | 每小时 | 作品封面的点击量/曝光量 |
> | 20 | 封面点击率 | 从低到高 ↑ | 每小时 | 封面点击率最低的在前 |
> | 21 | 平均播放时长 | 从高到低 ↓ | 每小时 | 视频被播放的平均时长 |
> | 22 | 平均播放时长 | 从低到高 ↑ | 每小时 | 平均播放时长最短的在前 |
> | 23 | 主页访问量 | 从高到低 ↓ | 每天 | 用户观看作品后访问主页的次数 |
> | 24 | 主页访问量 | 从低到高 ↑ | 每天 | 主页访问量最少的在前 |
> | 25 | 粉丝增量 | 从高到低 ↓ | 每小时 | 观众观看作品后关注作者的数量 |
> | 26 | 粉丝增量 | 从低到高 ↑ | 每小时 | 粉丝增量最少的在前 |
>
> ### 排序使用建议:
> - **寻找爆款**: 使用 order_by=3 (播放量↓) 或 order_by=5 (点赞量↓)
> - **优化内容**: 使用 order_by=13 (2s跳出率↓) 找出需要优化的作品
> - **提升完播**: 使用 order_by=17 (完播率↓) 分析高完播率作品
> - **涨粉分析**: 使用 order_by=25 (粉丝增量↓) 找出涨粉效果好的作品
> - **封面优化**: 使用 order_by=19 (封面点击率↓) 分析封面吸引力
>
> ### 返回:
> - 投稿作品列表数据，包含作品的详细指标信息
> - has_more: 是否还有更多数据
> - cursor: 下一页的游标，用于分页查询
> - items: 作品列表数组
>
> ### 使用流程:
> 1. **第一次请求**：不传cursor参数，获取第一页数据
> 2. **检查has_more**：如果为true，说明还有更多数据
> 3. **分页请求**：使用返回的cursor值作为下次请求的cursor参数
> 4. **重复步骤2-3**：直到has_more为false
>
> ### 功能限制:
> - 仅支持筛选：所选周期内，前100条作品的体裁
> - 如需导出更多数据，请使用 `/fetch_item_list_download` 接口（支持导出前1000条）
>
> ### 时间戳转换:
> - JavaScript: `new Date('2025-07-01').getTime()` -> 1719763200000
> - Python: `int(datetime(2025, 7, 1).timestamp() * 1000)` -> 1719763200000
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get all published items within the specified time range
> - Support pagination query, maximum 100 items per request
> - Data update description:
>   - **Views, likes, comments, shares, favorites update in real-time**
>   - **Other metrics update hourly**
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - start_time: Start timestamp in milliseconds (required)
> - end_time: End timestamp in milliseconds (required)
> - count: Number of items per page, default 10, max 100 (optional)
> - order_by: Sort method, supports 26 types (optional, default 1)
> - fields: Fields to return, default "metrics,review,visibility" (optional)
>   - metrics: Traffic metrics (views, likes, comments, shares, favorites, etc.)
>   - review: Review status
>   - visibility: Visibility status
> - need_cooperation: Need cooperation info, default true (optional)
> - need_long_article: Include long articles, default true (optional)
> - cursor: Pagination cursor, don't pass for first request, use returned cursor for pagination (optional)
>
> ### Sort Options (order_by):
>
> | Value | Sort Field | Direction | Update Freq | Description |
> |-------|-----------|-----------|-------------|-------------|
> | 1 | Publish Time | Desc ↓ | - | Default, newest first |
> | 2 | Publish Time | Asc ↑ | - | Oldest first |
> | 3 | Views | Desc ↓ | Real-time | Video views count |
> | 4 | Views | Asc ↑ | Real-time | Least views first |
> | 5 | Likes | Desc ↓ | Real-time | Likes count |
> | 6 | Likes | Asc ↑ | Real-time | Least likes first |
> | 7 | Comments | Desc ↓ | Real-time | Comments count |
> | 8 | Comments | Asc ↑ | Real-time | Least comments first |
> | 9 | Shares | Desc ↓ | Real-time | Shares count |
> | 10 | Shares | Asc ↑ | Real-time | Least shares first |
> | 11 | Favorites | Desc ↓ | Real-time | Favorites count |
> | 12 | Favorites | Asc ↑ | Real-time | Least favorites first |
> | 13 | 2s Bounce Rate | Desc ↓ | Hourly | Views bounced within 2s / total views |
> | 14 | 2s Bounce Rate | Asc ↑ | Hourly | Lowest bounce rate first |
> | 15 | 5s Completion | Desc ↓ | Hourly | Views over 5s / total views |
> | 16 | 5s Completion | Asc ↑ | Hourly | Lowest 5s completion first |
> | 17 | Completion Rate | Desc ↓ | Hourly | Full plays / total views |
> | 18 | Completion Rate | Asc ↑ | Hourly | Lowest completion rate first |
> | 19 | Cover CTR | Desc ↓ | Hourly | Cover clicks / cover impressions |
> | 20 | Cover CTR | Asc ↑ | Hourly | Lowest CTR first |
> | 21 | Avg Play Duration | Desc ↓ | Hourly | Average video play duration |
> | 22 | Avg Play Duration | Asc ↑ | Hourly | Shortest duration first |
> | 23 | Profile Visits | Desc ↓ | Daily | Profile visits after watching |
> | 24 | Profile Visits | Asc ↑ | Daily | Least profile visits first |
> | 25 | Follower Growth | Desc ↓ | Hourly | New followers from this video |
> | 26 | Follower Growth | Asc ↑ | Hourly | Least follower growth first |
>
> ### Sort Usage Tips:
> - **Find Hits**: Use order_by=3 (Views↓) or order_by=5 (Likes↓)
> - **Content Optimization**: Use order_by=13 (Bounce Rate↓) to find videos to improve
> - **Improve Completion**: Use order_by=17 (Completion↓) to analyze high-completion videos
> - **Follower Analysis**: Use order_by=25 (Follower Growth↓) to find best performing videos
> - **Cover Optimization**: Use order_by=19 (Cover CTR↓) to analyze cover attractiveness
>
> ### Return:
> - Item list data with detailed metric information
> - has_more: Whether there are more items
> - cursor: Cursor for next page, used for pagination
> - items: Array of items
>
> ### Usage Flow:
> 1. **First request**: Don't pass cursor parameter, get first page
> 2. **Check has_more**: If true, there are more items
> 3. **Paginate**: Use returned cursor value as cursor parameter for next request
> 4. **Repeat steps 2-3**: Until has_more is false
>
> ### Limitations:
> - Only supports filtering: Top 100 items by genre in selected period
> - For exporting more data, use `/fetch_item_list_download` API (supports top 1000 items)
>
> ### Timestamp Conversion:
> - JavaScript: `new Date('2025-07-01').getTime()` -> 1719763200000
> - Python: `int(datetime(2025, 7, 1).timestamp() * 1000)` -> 1719763200000
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ### 基础请求/Basic Request (默认按发布时间排序):
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_time": 1758988800000,
>     "end_time": 1760198399000,
>     "count": 10
> }
> ```
>
> ### 按播放量排序/Sort by Views (找爆款视频):
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_time": 1758988800000,
>     "end_time": 1760198399000,
>     "count": 20,
>     "order_by": 3
> }
> ```
>
> ### 按完播率排序/Sort by Completion Rate (优质内容分析):
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_time": 1758988800000,
>     "end_time": 1760198399000,
>     "count": 20,
>     "order_by": 17
> }
> ```
>
> ### 按粉丝增量排序/Sort by Follower Growth (涨粉效果分析):
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_time": 1758988800000,
>     "end_time": 1760198399000,
>     "count": 20,
>     "order_by": 25
> }
> ```
>
> ### 分页请求/Pagination Request:
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_time": 1758988800000,
>     "end_time": 1760198399000,
>     "count": 10,
>     "cursor": 1234567890
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "has_more": true,
>     "cursor": 1234567890,
>     "items": [
>         {
>             "item_id": "7559536212910853422",
>             "metrics": {
>                 "play_count": 12345,
>                 "digg_count": 678,
>                 "comment_count": 90,
>                 "share_count": 45,
>                 "collect_count": 123
>             },
>             "review": {
>                 "status": 2
>             },
>             "visibility": {
>                 "is_public": true
>             }
>         }
>     ]
> }
> ```
>
> ### 注意事项/Notes:
> 1. **时间范围**: 建议不要设置过长的时间范围，可能导致请求超时
> 2. **分页查询**: 如果has_more=true，务必使用返回的cursor继续请求
> 3. **数据更新频率**:
>    - 实时更新：播放量、点赞量、评论量、分享量、收藏量
>    - 每小时更新：跳出率、完播率、封面点击率、平均播放时长、粉丝增量
>    - 每天更新：主页访问量
> 4. **数据量限制**: 单次请求最多返回100条，如需更多请使用分页或导出接口
> 5. **体裁筛选**: 仅支持前100条作品的体裁筛选
> 6. **排序选择**: 根据分析目标选择合适的排序方式（共26种）
> 7. **Cookie有效性**: 如果返回错误，请检查Cookie是否过期
> 8. **排序说明**: ↓表示从高到低，↑表示从低到高

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `count`:integer, `order_by`:integer, `fields`:string, `need_cooperation`:boolean, `start_time*`:integer, `end_time*`:integer, `need_long_article`:boolean, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| count | integer | 否 | 每页数量/Count per page (最多100条) | 10 | 10 | 无 |
| order_by | integer | 否 | 排序方式/Order by (1-26): 1=发布时间↓(新到旧), 2=发布时间↑(旧到新), 3=播放量↓, 4=播放量↑, 5=点赞量↓, 6=点赞量↑, 7=评论量↓, 8=评论量↑, 9=分享量↓, 10=分享量↑, 11=收藏量↓, 12=收藏量↑, 13=2s跳出率↓, 14=2s跳出率↑, 15=5s完播率↓, 16=5s完播率↑, 17… | 1 | 1 | 无 |
| fields | string | 否 | 需要返回的字段/Fields to return | metrics,review,visibility | metrics,review,visibility | 无 |
| need_cooperation | boolean | 否 | 是否需要合作信息/Need cooperation info | true | true | 无 |
| start_time | integer | 是 | 开始时间戳(毫秒)/Start time timestamp (milliseconds) | 无 | 1758988800000 | 无 |
| end_time | integer | 是 | 结束时间戳(毫秒)/End time timestamp (milliseconds) | 无 | 1760198399000 | 无 |
| need_long_article | boolean | 否 | 是否包含长图文/Include long articles | true | true | 无 |
| cursor | integer | 否 | 分页游标/Pagination cursor (可选) | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-list-download"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list_download`

- 摘要：导出投稿作品列表/Download item list
- 能力：创作者 / 下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_list_download_api_v1_douyin_creator_v2_fetch_item_list_download_post`

#### 说明

> # [中文]
> ### 用途:
> - 导出指定时间范围内前1000条投稿作品的详细数据
> - 支持按体裁类型筛选导出内容
> - **此接口用于批量导出数据，不适合实时查询**
> - **导出任务为异步处理，需要等待服务器生成文件**
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - min_cursor: 最小游标，即开始时间戳（毫秒）（必填）
> - max_cursor: 最大游标，即结束时间戳（毫秒）（必填）
> - type_filters: 体裁类型过滤列表，默认全选 [1,2,3,4,5,8]（可选）
>   - **1**: 1分钟以内视频
>   - **2**: 1-3分钟视频
>   - **3**: 3-5分钟视频
>   - **4**: 5分钟以上视频
>   - **5**: 图文作品
>   - **8**: 长图文作品
> - need_long_article: 是否包含长图文，默认true（可选）
>
> ### 返回:
> - **直接返回Excel文件流**，浏览器会自动下载
> - 文件名：作品列表导出.xlsx
> - 文件格式：Excel (.xlsx)
> - Content-Type: application/vnd.ms-excel
>
> ### 使用流程:
> 1. **发起导出请求**：提交时间范围和筛选条件
> 2. **接收文件**：接口会直接返回Excel文件流
> 3. **自动下载**：浏览器会自动触发文件下载
> 4. **数据分析**：打开Excel文件进行数据分析
>
> ### 功能限制:
> - 仅支持导出：所选周期内，前1000条作品的数据
> - 支持按体裁类型筛选（可选择1-6种体裁的任意组合）
> - 不支持实时查询，适合批量数据分析场景
>
> ### 体裁类型说明:
> | 类型值 | 体裁名称 | 说明 | 使用场景 |
> |-------|---------|------|---------|
> | 1 | 1min以内视频 | 短视频 | 快速传播，高互动 |
> | 2 | 1-3min视频 | 中短视频 | 平衡内容与时长 |
> | 3 | 3-5min视频 | 中长视频 | 深度内容呈现 |
> | 4 | 5min+视频 | 长视频 | 专业内容，深度分析 |
> | 5 | 图文 | 图文作品 | 图片+文字形式 |
> | 8 | 长图文 | 长图文作品 | 深度图文内容 |
>
> ### 导出数据包含:
> - 作品基本信息（ID、标题、发布时间等）
> - 流量指标（播放量、点赞量、评论量、分享量、收藏量）
> - 审核状态
> - 可见性设置
> - 其他创作者相关数据
>
> ### 时间戳转换:
> - JavaScript: `new Date('2025-07-01').getTime()` -> 1719763200000
> - Python: `int(datetime(2025, 7, 1).timestamp() * 1000)` -> 1719763200000
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Export detailed data of top 1000 items within the specified time range
> - Support filtering export content by genre types
> - **This API is for batch export, not suitable for real-time queries**
> - **Export tasks are processed asynchronously, need to wait for server to generate file**
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - min_cursor: Min cursor, i.e., start timestamp in milliseconds (required)
> - max_cursor: Max cursor, i.e., end timestamp in milliseconds (required)
> - type_filters: Genre type filter list, default all [1,2,3,4,5,8] (optional)
>   - **1**: Videos under 1 minute
>   - **2**: 1-3 minute videos
>   - **3**: 3-5 minute videos
>   - **4**: Videos over 5 minutes
>   - **5**: Image posts
>   - **8**: Long image posts
> - need_long_article: Include long articles, default true (optional)
>
> ### Return:
> - **Directly returns Excel file stream**, browser will auto-download
> - Filename: 作品列表导出.xlsx (Item List Export.xlsx)
> - File Format: Excel (.xlsx)
> - Content-Type: application/vnd.ms-excel
>
> ### Usage Flow:
> 1. **Initiate export request**: Submit time range and filter conditions
> 2. **Receive file**: API returns Excel file stream directly
> 3. **Auto download**: Browser automatically triggers file download
> 4. **Data analysis**: Open Excel file for data analysis
>
> ### Limitations:
> - Only supports exporting: Top 1000 items in selected period
> - Support filtering by genre types (can select any combination of 1-6 genres)
> - Not suitable for real-time queries, designed for batch data analysis
>
> ### Genre Type Description:
> | Type | Genre Name | Description | Use Case |
> |------|-----------|-------------|----------|
> | 1 | <1min video | Short video | Fast spread, high engagement |
> | 2 | 1-3min video | Medium-short video | Balance content & duration |
> | 3 | 3-5min video | Medium-long video | Deep content presentation |
> | 4 | 5min+ video | Long video | Professional content, deep analysis |
> | 5 | Image post | Image post | Picture + text format |
> | 8 | Long image post | Long image post | Deep image-text content |
>
> ### Export Data Includes:
> - Item basic info (ID, title, publish time, etc.)
> - Traffic metrics (views, likes, comments, shares, favorites)
> - Review status
> - Visibility settings
> - Other creator-related data
>
> ### Timestamp Conversion:
> - JavaScript: `new Date('2025-07-01').getTime()` -> 1719763200000
> - Python: `int(datetime(2025, 7, 1).timestamp() * 1000)` -> 1719763200000
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ### 导出所有体裁/Export All Genres:
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "min_cursor": 1752336000000,
>     "max_cursor": 1760198399000,
>     "type_filters": [1, 2, 3, 4, 5, 8],
>     "need_long_article": true
> }
> ```
>
> ### 仅导出视频作品/Export Only Videos:
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "min_cursor": 1752336000000,
>     "max_cursor": 1760198399000,
>     "type_filters": [1, 2, 3, 4],
>     "need_long_article": false
> }
> ```
>
> ### 仅导出图文作品/Export Only Image Posts:
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "min_cursor": 1752336000000,
>     "max_cursor": 1760198399000,
>     "type_filters": [5, 8],
>     "need_long_article": true
> }
> ```
>
> ### 返回数据说明/Response Description:
> - 此接口直接返回Excel文件流，不返回JSON数据
> - 响应头包含 `Content-Disposition: attachment; filename="作品列表导出.xlsx"`
> - 浏览器会自动识别并触发文件下载
> - 文件内容为二进制流（application/vnd.ms-excel）
>
> ### 使用方式示例/Usage Examples:
>
> **使用 cURL 下载:**
> ```bash
> curl -X POST "https://your-api.com/api/v1/douyin_creator_v2/fetch_item_list_download"       -H "Authorization: Bearer YOUR_TOKEN"       -H "Content-Type: application/json"       -d '{
>     "cookie": "Your_Cookie_Here",
>     "min_cursor": 1752336000000,
>     "max_cursor": 1760198399000,
>     "type_filters": [1,2,3,4,5,8]
>   }'       -o "作品列表导出.xlsx"
> ```
>
> **使用 Python requests:**
> ```python
> import requests
>
> response = requests.post(
>     "https://your-api.com/api/v1/douyin_creator_v2/fetch_item_list_download",
>     headers={"Authorization": "Bearer YOUR_TOKEN"},
>     json={
>         "cookie": "Your_Cookie_Here",
>         "min_cursor": 1752336000000,
>         "max_cursor": 1760198399000,
>         "type_filters": [1,2,3,4,5,8]
>     }
> )
>
> # 保存文件
> with open("作品列表导出.xlsx", "wb") as f:
>     f.write(response.content)
> ```
>
> **使用 JavaScript (Axios):**
> ```javascript
> const axios = require('axios');
> const fs = require('fs');
>
> axios.post('https://your-api.com/api/v1/douyin_creator_v2/fetch_item_list_download', {
>     cookie: 'Your_Cookie_Here',
>     min_cursor: 1752336000000,
>     max_cursor: 1760198399000,
>     type_filters: [1,2,3,4,5,8]
> }, {
>     headers: { 'Authorization': 'Bearer YOUR_TOKEN' },
>     responseType: 'arraybuffer'
> }).then(response => {
>     fs.writeFileSync('作品列表导出.xlsx', response.data);
> });
> ```
>
> ### 注意事项/Notes:
> 1. **数据量限制**: 最多导出前1000条作品数据
> 2. **即时生成**: 接口会立即生成Excel文件并返回，无需等待
> 3. **时间范围**: 建议不要设置过长的时间范围，以免数据量过大导致超时
> 4. **体裁筛选**: 可以根据分析需求选择特定体裁类型
> 5. **文件格式**: Excel (.xlsx) 格式，兼容 Microsoft Excel、WPS、Google Sheets等
> 6. **响应类型**: 返回二进制流，不是JSON，请使用正确的响应处理方式
> 7. **Cookie有效性**: 如果返回错误，请检查Cookie是否过期
> 8. **超时设置**: 建议设置较长的超时时间（60秒以上），因为需要生成文件
> 9. **文件编码**: 文件名使用UTF-8编码，支持中文显示

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `min_cursor*`:integer, `max_cursor*`:integer, `type_filters`[integer], `need_long_article`:boolean

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| min_cursor | integer | 是 | 最小游标(开始时间戳,毫秒)/Min cursor (start timestamp in milliseconds) | 无 | 1752336000000 | 无 |
| max_cursor | integer | 是 | 最大游标(结束时间戳,毫秒)/Max cursor (end timestamp in milliseconds) | 无 | 1760198399000 | 无 |
| type_filters | array<integer> | 否 | 体裁类型过滤/Type filters: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 | [1, 2, 3, 4, 5, 8] | [2, 3, 4, 5, 1, 8] | 无 |
| need_long_article | boolean | 否 | 是否包含长图文/Include long articles | true | true | 无 |

#### 成功响应

##### `200 application/json`

- Schema 摘要：无结构声明

无字段表

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-overview-data"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_overview_data`

- 摘要：获取作品总览数据/Fetch item overview data
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_overview_data_api_v1_douyin_creator_v2_fetch_item_overview_data_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品总览数据，包括流量指标、审核状态、播放信息等
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - ids: 作品ID列表，多个ID用逗号分隔（例如: "7559536212910853422,7559536212910853423"）
> - fields: 需要返回的字段，默认为 "metrics,review,play_info,dou_plus,integrated_incentive,incentive_life,content_analysis"
>   - 可选字段（用逗号分隔，可自行组合）:
>     - metrics: 流量指标数据（播放量、点赞量、评论量等）
>     - review: 审核状态信息
>     - play_info: 播放相关信息
>     - dou_plus: 抖+推广信息
>     - integrated_incentive: 综合激励数据
>     - incentive_life: 激励生命周期信息
>     - content_analysis: 内容分析数据
>
> ### 返回:
> - 作品总览数据，根据 fields 参数返回对应的字段内容
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item overview data, including traffic metrics, review status, play info, etc.
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - ids: Item ID list, separated by comma (e.g., "7559536212910853422,7559536212910853423")
> - fields: Fields to return, default is "metrics,review,play_info,dou_plus,integrated_incentive,incentive_life,content_analysis"
>   - Available fields (comma-separated, customizable):
>     - metrics: Traffic metrics data (views, likes, comments, etc.)
>     - review: Review status information
>     - play_info: Play related information
>     - dou_plus: DOU+ promotion information
>     - integrated_incentive: Integrated incentive data
>     - incentive_life: Incentive lifecycle information
>     - content_analysis: Content analysis data
>
> ### Return:
> - Item overview data, returns corresponding fields based on the fields parameter
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "ids": "7559536212910853422",
>     "fields": "metrics,review,play_info,dou_plus,integrated_incentive,incentive_life,content_analysis"
> }
> ```
>
> ### 字段组合示例/Field Combination Examples:
> - 只获取流量指标: "metrics"
> - 获取流量和审核: "metrics,review"
> - 获取所有字段: "metrics,review,play_info,dou_plus,integrated_incentive,incentive_life,content_analysis"

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `ids*`:string, `fields`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| ids | string | 是 | 作品ID列表,多个ID用逗号分隔/Item IDs, separated by comma | 无 | 7559536212910853422,7559536212910853423 | 无 |
| fields | string | 否 | 需要返回的字段,多个字段用逗号分隔/Fields to return, separated by comma. 可选值: metrics(指标),review(审核),play_info(播放信息),dou_plus(抖+),integrated_incentive(综合激励),incentive_life(激励生命周期),content_analysis… | metrics,review,play_info,dou_plus,integrated_incentive,incentive_life,content_a… | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-play-source"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_play_source`

- 摘要：获取作品流量来源统计/Fetch item play source statistics
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_play_source_api_v1_douyin_creator_v2_fetch_item_play_source_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的流量来源统计数据
> - 流量来源统计了作品从不同途径播放的占比
> - **若暂时没有看到某个渠道，说明对应渠道暂时没有播放**
> - **作品刚发布推荐页流量占比可能偏低，请等待系统推流**
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
>
> ### 返回数据说明:
> - play_source: 流量来源列表，包含各渠道的播放占比
>   - key: 流量来源渠道标识
>   - value: 当前占比（0-1之间的小数，如0.85表示85%）
>   - history_difference: 与历史数据的差异
>   - app_id: 应用ID
>
> ### 流量来源渠道说明:
> - **homepage_hot**: 推荐页（系统推荐流量）
> - **familiar**: 朋友页（关注的人、好友推荐）
> - **search**: 搜索（用户主动搜索）
> - **homepage**: 个人主页（访问主页观看）
> - **message**: 消息页（通过消息入口）
> - **other**: 其他（其他途径）
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item play source statistics
> - Statistics of the proportion of item views from different sources
> - **If a channel is not shown, it means there are no views from that channel yet**
> - **For newly published items, the recommended page traffic may be low initially, please wait for system distribution**
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
>
> ### Return Data Description:
> - play_source: List of traffic sources with play proportion for each channel
>   - key: Traffic source channel identifier
>   - value: Current proportion (decimal between 0-1, e.g., 0.85 means 85%)
>   - history_difference: Difference from historical data
>   - app_id: Application ID
>
> ### Traffic Source Channel Description:
> - **homepage_hot**: Recommended page (system recommendation traffic)
> - **familiar**: Friends page (followed people, friend recommendations)
> - **search**: Search (user active search)
> - **homepage**: Personal homepage (views from homepage visits)
> - **message**: Message page (through message entry)
> - **other**: Other (other sources)
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "play_source": [
>         {
>             "app_id": 1128,
>             "history_difference": 0.8543689320388349,
>             "key": "homepage_hot",
>             "value": 0.8543689320388349
>         },
>         {
>             "app_id": 1128,
>             "history_difference": 0.05825242718446602,
>             "key": "familiar",
>             "value": 0.05825242718446602
>         },
>         {
>             "app_id": 1128,
>             "history_difference": 0.04854368932038835,
>             "key": "search",
>             "value": 0.04854368932038835
>         }
>     ],
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> - value 值表示该渠道的流量占比，例如 0.85 表示 85% 的流量来自该渠道
> - homepage_hot 占比高说明作品获得了较好的系统推荐
> - familiar 占比高说明作品在关注用户中传播较好
> - search 占比高说明作品搜索热度高

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-search-keyword"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword`

- 摘要：获取作品搜索关键词统计/Fetch item search keywords statistics
- 能力：搜索 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_search_keyword_api_v1_douyin_creator_v2_fetch_item_search_keyword_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的搜索关键词统计数据
> - 了解用户通过哪些搜索关键词找到并观看了该作品
> - 帮助创作者优化内容标题、标签和描述，提升搜索曝光
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
>
> ### 返回数据说明:
> 返回用户搜索该作品时使用的关键词列表，包括：
> - keyword: 搜索关键词
> - count: 该关键词被搜索的次数
> - percentage: 该关键词占总搜索量的百分比
>
> **注意**: 如果返回空列表，说明该作品目前暂无搜索关键词数据，可能原因：
> - 作品刚发布，还没有用户通过搜索观看
> - 作品主要通过推荐、关注等非搜索渠道传播
> - 数据统计周期内没有搜索行为
>
> ### 数据价值:
> - **优化标题**: 根据热门关键词调整作品标题
> - **优化标签**: 添加相关的热门搜索词作为标签
> - **内容策划**: 了解用户兴趣点，制作更符合需求的内容
> - **SEO优化**: 提升作品在搜索结果中的排名
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item search keywords statistics
> - Understand which search keywords users used to find and watch the item
> - Help creators optimize content titles, tags, and descriptions to improve search exposure
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
>
> ### Return Data Description:
> Returns a list of keywords users searched for to find this item, including:
> - keyword: Search keyword
> - count: Number of times this keyword was searched
> - percentage: Percentage of this keyword in total searches
>
> **Note**: If an empty list is returned, it means there is currently no search keyword data for this item, possible reasons:
> - Item was just published and no users have searched for it yet
> - Item is mainly spread through recommendations, follows, etc., not through search
> - No search behavior during the statistics period
>
> ### Data Value:
> - **Optimize Title**: Adjust item title based on popular keywords
> - **Optimize Tags**: Add relevant popular search terms as tags
> - **Content Planning**: Understand user interests and create more relevant content
> - **SEO Optimization**: Improve item ranking in search results
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422"
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "keywords": [
>         {
>             "keyword": "搞笑视频",
>             "count": 1250,
>             "percentage": 35.5
>         },
>         {
>             "keyword": "热门音乐",
>             "count": 850,
>             "percentage": 24.2
>         },
>         {
>             "keyword": "舞蹈教学",
>             "count": 620,
>             "percentage": 17.6
>         }
>     ],
>     "total_count": 3520,
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> - 关键词列表按搜索次数降序排列
> - percentage 值越高，说明该关键词越受用户关注
> - 可以根据高频关键词优化作品的标题、描述和标签
> - 发现意外的热门关键词可能揭示新的内容方向
> - **空列表**: 说明作品暂无搜索数据，作品主要通过其他渠道传播
>
> ### 应用建议/Application Suggestions:
> 1. **标题优化**: 在标题中自然融入高频关键词
> 2. **标签策略**: 使用搜索量高的关键词作为标签
> 3. **内容调整**: 创作更多用户搜索的相关内容
> 4. **竞品分析**: 对比不同作品的关键词差异

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-item-watch-trend"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend`

- 摘要：获取作品观看趋势分析/Fetch item watch trend analysis
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_watch_trend_api_v1_douyin_creator_v2_fetch_item_watch_trend_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音作品的观看趋势分析数据
> - 了解用户在观看作品时的行为模式
> - 帮助创作者优化视频内容结构和节奏
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - item_id: 作品ID（必填）
> - analysis_type: 分析类型（可选，默认为1）
>   - **1**: 留存分析 - 显示用户在各个时间点的留存情况
>   - **2**: 点赞分析 - 显示用户在各个时间点的点赞情况
>   - **7**: 跳出分析 - 显示用户在各个时间点的跳出情况
>
> ### 分析类型说明:
> - **留存分析 (analysis_type=1)**:
>   - 展示观众在视频各时间点的留存比例
>   - 留存率越高，说明该时间段内容越吸引人
>   - **注意**: 播放量超过200后，数据更准确
>   - 适合分析：哪些片段吸引观众持续观看
>
> - **点赞分析 (analysis_type=2)**:
>   - 展示观众在视频各时间点的点赞比例
>   - 点赞率高的时间点说明该片段特别受欢迎
>   - 适合分析：哪些片段最能引发用户互动
>
> - **跳出分析 (analysis_type=7)**:
>   - 展示观众在视频各时间点的跳出比例
>   - 跳出率高的时间点可能存在内容问题
>   - 适合分析：哪些片段导致观众离开
>
> ### 返回数据说明:
> - analysis_trend: 趋势分析数据
>   - current_item: 当前作品的数据点列表
>     - key: 时间点（格式：mm:ss，如 "00:05" 表示第5秒）
>     - value: 该时间点的比例值（0-1之间的小数）
>   - similar_author: 同类作者的平均数据（用于对比）
>     - key: 时间点
>     - value: 同类作者在该时间点的平均比例
>
> ### 数据价值:
> - **内容优化**: 识别观众流失的关键时间点
> - **节奏调整**: 优化视频的起承转合节奏
> - **对比分析**: 与同类作者对比，找出差距和优势
> - **A/B测试**: 测试不同版本的内容效果
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin item watch trend analysis data
> - Understand user behavior patterns while watching the item
> - Help creators optimize video content structure and pacing
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - item_id: Item ID (required)
> - analysis_type: Analysis type (optional, default is 1)
>   - **1**: Retention Analysis - Shows user retention at each time point
>   - **2**: Like Analysis - Shows user like behavior at each time point
>   - **7**: Bounce Analysis - Shows user bounce rate at each time point
>
> ### Analysis Type Description:
> - **Retention Analysis (analysis_type=1)**:
>   - Shows viewer retention rate at various video time points
>   - Higher retention means more engaging content at that moment
>   - **Note**: Data is more accurate when views exceed 200
>   - Good for: Identifying which segments keep viewers watching
>
> - **Like Analysis (analysis_type=2)**:
>   - Shows viewer like rate at various video time points
>   - Higher like rate indicates particularly popular segments
>   - Good for: Identifying segments that drive user engagement
>
> - **Bounce Analysis (analysis_type=7)**:
>   - Shows viewer bounce rate at various video time points
>   - High bounce rate indicates potential content issues
>   - Good for: Identifying segments that cause viewers to leave
>
> ### Return Data Description:
> - analysis_trend: Trend analysis data
>   - current_item: Data points for current item
>     - key: Time point (format: mm:ss, e.g., "00:05" for 5 seconds)
>     - value: Proportion at this time point (decimal between 0-1)
>   - similar_author: Average data from similar authors (for comparison)
>     - key: Time point
>     - value: Average proportion at this time point
>
> ### Data Value:
> - **Content Optimization**: Identify key drop-off points
> - **Pacing Adjustment**: Optimize video rhythm and flow
> - **Comparative Analysis**: Compare with similar creators to find gaps
> - **A/B Testing**: Test different content versions
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "item_id": "7559536212910853422",
>     "analysis_type": 1
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "analysis_trend": {
>         "current_item": [
>             {
>                 "key": "00:00",
>                 "value": 0.2653
>             },
>             {
>                 "key": "00:01",
>                 "value": 0.2653
>             },
>             {
>                 "key": "00:05",
>                 "value": 0.0272
>             },
>             {
>                 "key": "00:10",
>                 "value": 0.1429
>             }
>         ],
>         "similar_author": [
>             {
>                 "key": "00:00",
>                 "value": 0.1594
>             },
>             {
>                 "key": "00:01",
>                 "value": 0.2229
>             }
>         ]
>     },
>     "status_code": 0,
>     "status_msg": ""
> }
> ```
>
> ### 数据解读/Data Interpretation:
> **留存分析 (Retention)**:
> - value 值表示该时间点的留存比例
> - 数值越高表示越多观众看到这个时间点
> - 对比 current_item 和 similar_author 可以看出作品表现
> - 留存曲线下降陡峭说明内容吸引力不足
>
> **点赞分析 (Like)**:
> - value 值表示该时间点的点赞比例
> - 数值越高表示该时间段内容越能引发点赞
> - 点赞高峰通常出现在高潮、反转、笑点等位置
> - 可以帮助识别最有价值的内容片段
>
> **跳出分析 (Bounce)**:
> - value 值表示该时间点的跳出比例
> - 数值越高表示越多观众在此时离开
> - 跳出率高的时间点需要重点优化
> - 开头几秒的跳出率尤其重要
>
> ### 优化建议/Optimization Suggestions:
> 1. **前3秒黄金法则**: 确保开头吸引眼球，降低初期跳出
> 2. **节奏把控**: 在留存率下降前插入高潮或转折
> 3. **时长优化**: 根据留存曲线调整视频时长
> 4. **点赞热点**: 在点赞率高的时间段前后放置核心内容
> 5. **对标学习**: 参考 similar_author 数据优化内容
> 6. **持续测试**: 不同类型内容的最佳节奏不同
>
> ### 注意事项/Notes:
> - 播放量超过 200 后，留存分析数据更准确
> - 数据可能有延迟，建议作品发布一段时间后查看
> - 结合其他指标（完播率、互动率）综合分析

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string, `analysis_type`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| item_id | string | 是 | 作品ID/Item ID | 无 | 7559536212910853422 | 无 |
| analysis_type | integer | 否 | 分析类型/Analysis type: 1=留存分析(Retention), 2=点赞分析(Like), 7=跳出分析(Bounce) | 1 | 1 | 无 |

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

<a id="post-api-u1-v1-douyin-creator-v2-fetch-live-room-history-list"></a>
### `POST /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list`

- 摘要：获取直播场次历史记录/Fetch live room history list
- 能力：创作者 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_history_list_api_v1_douyin_creator_v2_fetch_live_room_history_list_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音创作者的直播场次历史记录
> - 查看指定时间范围内的所有直播场次数据
> - 支持查询正在进行的直播和历史直播记录
> - **此接口需要用户提供有效的抖音创作者平台Cookie**
> - **使用 POST 方法，Cookie 在请求体中传输，更安全**
>
> ### 请求体参数:
> - cookie: 用户的抖音创作者平台Cookie（必填，在请求体中传输）
> - start_date: 开始日期，格式为 YYYY-MM-DD（必填，例如: "2025-09-11"）
> - end_date: 结束日期，格式为 YYYY-MM-DD（必填，例如: "2025-10-11"）
> - limit: 每页数量限制，默认400，最多400条
> - need_living: 是否包含正在直播的场次（0=不包含, 1=包含，默认1）
> - download: 是否下载（0=不下载, 1=下载，默认0）
>
> ### 返回数据说明:
> 返回直播场次历史记录列表，数据位于 `data.data.series` 数组中，每个场次包含以下信息：
>
> **基本信息**:
> - roomID: 直播间ID
> - roomTitle: 直播标题
> - coverUri: 直播封面图片URL
> - startTime: 开始时间（格式: "YYYY-MM-DD HH:mm:ss"）
> - endTime: 结束时间（格式: "YYYY-MM-DD HH:mm:ss"）
> - liveDurationWithoutPause: 直播时长（不含暂停时间，格式如: "1分钟5秒"）
> - playStatus: 播放状态（4=已结束）
>
> **流量数据**:
> - watchCnt: 总观看人次
> - serverWatchUcntTdDirect: 直接观看用户数（来自服务端统计）
> - pcu: 峰值同时在线人数（Peak Concurrent Users）
> - liveServerWatchDurationTdPavg: 平均观看时长
>
> **互动数据**:
> - serverLikeCntTd: 点赞数
> - clientCommentUcntTd: 评论用户数
> - liveNewFollowUcnt: 新增关注数
>
> **消费/转化数据**:
> - liveConsumeUcnt: 消费用户数
> - liveFansConsumeUcntTd: 粉丝消费用户数
> - roomLiveEarnScore: 直播收益积分
>
> ### 数据价值:
> - **历史回顾**: 查看所有直播场次的完整记录
> - **数据对比**: 对比不同场次的表现差异
> - **趋势分析**: 分析直播效果的变化趋势
> - **优化方向**: 找出高转化场次的共同特点
> - **时间规划**: 根据历史数据优化直播时间
> - **内容策略**: 根据不同主题的效果调整内容
>
> ### 应用场景:
> 1. **定期复盘**: 每周/每月查看直播数据进行总结
> 2. **效果评估**: 评估不同时段、不同主题的直播效果
> 3. **数据报表**: 生成直播数据报表供团队分析
> 4. **策略优化**: 基于历史数据制定下一步直播策略
> 5. **KPI追踪**: 追踪直播相关的关键指标完成情况
> 6. **趋势预测**: 预测未来直播的潜在表现
>
> ### 注意事项:
> 1. **时间范围**: 建议查询时间不超过3个月，避免数据量过大
> 2. **数量限制**: 单次最多返回400条记录
> 3. **数据延迟**: 直播数据可能有1-2小时的延迟
> 4. **正在直播**: 设置need_living=1可以查看当前正在进行的直播
> 5. **Cookie有效性**: 确保Cookie未过期，否则无法获取数据
> 6. **日期格式**: 必须使用YYYY-MM-DD格式，如2025-09-11
>
> ### Cookie 获取方式:
> 1. 登录抖音创作者平台 (https://creator.douyin.com)
> 2. 打开浏览器开发者工具（F12）
> 3. 切换到 Network 标签
> 4. 刷新页面或进行操作
> 5. 找到任意请求，复制 Cookie 请求头的值
>
> # [English]
> ### Purpose:
> - Get Douyin creator's live room history list
> - View all live session data within a specified time range
> - Support querying ongoing and historical live sessions
> - **This API requires users to provide valid Douyin Creator Platform Cookie**
> - **Use POST method, Cookie is transmitted in request body, more secure**
>
> ### Request Body Parameters:
> - cookie: User's Douyin Creator Platform Cookie (required, transmitted in request body)
> - start_date: Start date in YYYY-MM-DD format (required, e.g., "2025-09-11")
> - end_date: End date in YYYY-MM-DD format (required, e.g., "2025-10-11")
> - limit: Limit per page, default 400, max 400
> - need_living: Include ongoing live sessions (0=No, 1=Yes, default 1)
> - download: Download flag (0=No download, 1=Download, default 0)
>
> ### Return Data Description:
> Returns a list of live session history, data is located in `data.data.series` array, each session includes:
>
> **Basic Info**:
> - roomID: Live room ID
> - roomTitle: Live title
> - coverUri: Live cover image URL
> - startTime: Start time (format: "YYYY-MM-DD HH:mm:ss")
> - endTime: End time (format: "YYYY-MM-DD HH:mm:ss")
> - liveDurationWithoutPause: Duration without pause (format: "1 minute 5 seconds")
> - playStatus: Play status (4=Ended)
>
> **Traffic Data**:
> - watchCnt: Total watch count
> - serverWatchUcntTdDirect: Direct watch user count (from server statistics)
> - pcu: Peak Concurrent Users
> - liveServerWatchDurationTdPavg: Average watch duration
>
> **Engagement Data**:
> - serverLikeCntTd: Likes count
> - clientCommentUcntTd: Comment user count
> - liveNewFollowUcnt: New followers count
>
> **Consumption/Conversion Data**:
> - liveConsumeUcnt: Consuming user count
> - liveFansConsumeUcntTd: Fan consuming user count
> - roomLiveEarnScore: Live room earn score
>
> ### Data Value:
> - **History Review**: View complete records of all live sessions
> - **Data Comparison**: Compare performance across sessions
> - **Trend Analysis**: Analyze changes in live performance
> - **Optimization**: Identify common traits of high-conversion sessions
> - **Time Planning**: Optimize live timing based on historical data
> - **Content Strategy**: Adjust content based on theme performance
>
> ### Use Cases:
> 1. **Regular Review**: Weekly/monthly live data summary
> 2. **Effect Evaluation**: Evaluate performance by time and theme
> 3. **Data Reports**: Generate reports for team analysis
> 4. **Strategy Optimization**: Develop strategies based on data
> 5. **KPI Tracking**: Track live-related KPIs
> 6. **Trend Prediction**: Predict future live performance
>
> ### Notes:
> 1. **Time Range**: Recommended not to exceed 3 months
> 2. **Quantity Limit**: Max 400 records per request
> 3. **Data Delay**: 1-2 hours delay possible
> 4. **Ongoing Live**: Set need_living=1 to include current live
> 5. **Cookie Validity**: Ensure Cookie is not expired
> 6. **Date Format**: Must use YYYY-MM-DD format
>
> ### How to get Cookie:
> 1. Login to Douyin Creator Platform (https://creator.douyin.com)
> 2. Open browser developer tools (F12)
> 3. Switch to Network tab
> 4. Refresh page or perform operations
> 5. Find any request and copy the Cookie header value
>
> # [示例/Example]
> ```json
> {
>     "cookie": "Your_Cookie_Here",
>     "start_date": "2025-09-11",
>     "end_date": "2025-10-11",
>     "limit": 400,
>     "need_living": 1,
>     "download": 0
> }
> ```
>
> ### 返回数据示例/Response Example:
> ```json
> {
>     "data": {
>         "code": 0,
>         "componentID": "",
>         "data": {
>             "series": [
>                 {
>                     "clientCommentUcntTd": "0",
>                     "coverUri": "https://p3-webcast-sign.douyinpic.com/...",
>                     "endTime": "2025-11-20 13:52:20",
>                     "liveConsumeUcnt": "1",
>                     "liveDurationWithoutPause": "1分钟5秒",
>                     "liveFansConsumeUcntTd": "1",
>                     "liveNewFollowUcnt": "0",
>                     "liveServerWatchDurationTdPavg": "0.5666666666666667",
>                     "pcu": "1",
>                     "playStatus": "4",
>                     "roomID": "75746809889xxxxxx",
>                     "roomLiveEarnScore": "1",
>                     "roomTitle": "xxxxxxxx",
>                     "serverLikeCntTd": "0",
>                     "serverWatchUcntTdDirect": "1",
>                     "startTime": "2025-11-20 13:51:15",
>                     "watchCnt": "1"
>                 }
>             ]
>         },
>         "meta": ""
>     }
> }
> ```
>
> ### 数据解读/Data Interpretation:
> - **watchCnt**: 总观看人次，反映直播的曝光度和吸引力
> - **pcu**: 峰值同时在线人数（Peak Concurrent Users），反映直播的热度峰值
> - **liveServerWatchDurationTdPavg**: 平均观看时长，反映内容的吸引力
> - **liveNewFollowUcnt**: 新增关注数，反映直播的转粉效果
> - **roomLiveEarnScore**: 直播收益积分，反映直播的收益能力
> - **liveConsumeUcnt/liveFansConsumeUcntTd**: 消费用户数/粉丝消费用户数，反映直播的转化能力
> - **互动率**: (serverLikeCntTd+clientCommentUcntTd)/watchCnt，反映用户活跃度
>
> ### 优化建议/Optimization Suggestions:
> 1. **高峰分析**: 分析pcu最高出现的时间点，强化该时段的内容
> 2. **留存优化**: 提升liveServerWatchDurationTdPavg平均观看时长，增加内容的连贯性和吸引力
> 3. **互动引导**: 在直播中增加互动环节，提升serverLikeCntTd点赞数、clientCommentUcntTd评论数
> 4. **转粉策略**: 在直播中适时引导关注，提升liveNewFollowUcnt新增关注数
> 5. **消费转化**: 分析高roomLiveEarnScore场次的特点，优化直播策略
> 6. **时间选择**: 根据历史数据选择watchCnt观看人次最多的时段开播

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `limit`:integer, `need_living`:integer, `download`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie | 无 | Your_Cookie_Here | 无 |
| start_date | string | 是 | 开始日期(格式YYYY-MM-DD)/Start date (format YYYY-MM-DD) | 无 | 2025-09-11 | 无 |
| end_date | string | 是 | 结束日期(格式YYYY-MM-DD)/End date (format YYYY-MM-DD) | 无 | 2025-10-11 | 无 |
| limit | integer | 否 | 每页数量限制/Limit per page (最多400条) | 400 | 400 | 无 |
| need_living | integer | 否 | 是否包含正在直播的场次/Include living rooms: 0=不包含, 1=包含 | 1 | 1 | 无 |
| download | integer | 否 | 是否下载/Download: 0=不下载, 1=下载 | 0 | 0 | 无 |

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
