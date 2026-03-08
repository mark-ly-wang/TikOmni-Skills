# TikTok-Analytics-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/tiktok-analytics-api.md`](../api-tags/tiktok-analytics-api.md)
- 当前契约文件：`api-contracts/tiktok-analytics-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`4`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(TikTok数据分析接口/TikTok-Analytics-API data analysis endpoints)**

## 路由契约

<a id="get-api-u1-v1-tiktok-analytics-detect-fake-views"></a>
### `GET /api/u1/v1/tiktok/analytics/detect_fake_views`

- 摘要：检测视频虚假流量分析/Detect fake views in video
- 能力：数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`detect_fake_views_api_v1_tiktok_analytics_detect_fake_views_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过高级算法分析TikTok视频流量数据，精确检测可能存在的虚假观看量和不自然互动
> - 基于TikTok赛马机制(Traffic Pool)流量池理论，评估内容真实性和流量质量
> - 提供全面的欺诈风险分析，包含8种维度、20+指标的深度评估
> - 为创作者、MCN机构和内容管理者提供专业的流量质量报告和优化建议
>
> ### 参数:
> - item_id: 视频作品ID，必填参数，可从视频URL中提取(例如: https://www.tiktok.com/@tiktok/video/7460937381265411370 中的7460937381265411370)
> - content_category: 内容分类，可选参数，影响互动率基准值，选项包括:
>   - default: 默认类别，通用内容
>   - entertainment: 娱乐内容，预期有较高互动率
>   - education: 教育内容，预期有适中互动和较高收藏率
>   - product: 产品内容，预期有较低互动但较高转化
>   - verified_large: 大型认证账号，预期互动率适当降低
>
> ### 返回内容详解:
> - `video_metrics`: 视频核心指标
>   - `total_views`: 总观看量，视频被观看的总次数
>   - `total_likes`: 总点赞数，用户点赞互动次数
>   - `total_comments`: 总评论数，用户评论互动次数
>   - `total_favorites`: 总收藏数，用户收藏次数
>   - `total_shares`: 总分享数，用户分享次数
>   - `engagement_rates`: 互动率指标，值越高越好
>     - `like_ratio`: 点赞率，正常值 1-10%，大账号可能较低
>     - `comment_ratio`: 评论率，正常值 0.1-0.5%，高于1%极佳
>     - `favorite_ratio`: 收藏率，正常值 0.05-0.8%
>     - `share_ratio`: 分享率，正常值 0.05-0.5%，高于1%极佳
>
> - `creator_metrics`: 创作者账号健康指标
>   - `account_age_days`: 账号存在天数，越长越可信
>   - `follower_count`: 粉丝数量，影响预期观看量
>   - `verified`: 是否验证账号，认证账号可信度更高
>   - `trust_score`: 账号信任度评分(0-100)，越高越可信
>
> - `content_metrics`: 内容质量指标
>   - `content_type`: 内容类型(video, image等)
>   - `created_by_ai`: 是否AI生成，AI生成内容可能有特定流量模式
>   - `high_quality_upload`: 是否高质量上传，高质量上传更可信
>
> - `fake_view_analysis`: 虚假流量综合分析
>   - `fake_score`: 虚假流量评分(0-100)，评分越低越好:
>     - 0-20: 极低风险，自然流量模式
>     - 20-40: 低风险，可能有少量异常但不构成问题
>     - 40-60: 中等风险，存在值得关注的异常
>     - 60-80: 高风险，明显的虚假流量特征
>     - 80-100: 极高风险，几乎确定存在虚假流量
>   - `confidence_level`: 风险等级，分为"Minimal", "Low", "Medium", "High"
>   - `estimated_fake_views`: 估计虚假观看量，基于虚假流量模型推算
>   - `fake_view_percentage`: 虚假观看百分比，虚假占总量的比例
>   - `is_suspicious`: 是否可疑，综合判断是否需要关注
>   - `main_detection_reason`: 主要检测原因，最显著的异常特征
>   - `component_scores`: 各维度异常评分，各项都是0-100，越低越好:
>     - `engagement_score`: 互动异常评分
>     - `distribution_score`: 分布异常评分
>     - `consistency_score`: 一致性异常评分
>     - `creator_credibility_score`: 创作者可信度异常评分
>     - `content_authenticity_score`: 内容真实性异常评分
>     - `follower_correlation_score`: 粉丝相关性异常评分
>     - `racing_mechanism_score`: 赛马机制异常评分
>     - `fan_growth_score`: 粉丝增长异常评分
>
> - `traffic_pool`: 流量池分析(TikTok赛马机制)
>   - `current_tier`: 当前流量池级别(1-8)，越高代表流量越大
>   - `current_tier_name`: 当前流量池名称
>   - `expected_tier`: 预期流量池级别，基于有机流量预测
>   - `expected_tier_name`: 预期流量池名称
>   - `current_views_range`: 当前流量池预期观看范围
>   - `expected_views_range`: 预期流量池观看范围
>   - `estimated_organic_views`: 估计有机观看量，扣除虚假后的真实观看
>
> - `suspicious_features`: 可疑特征列表，检测到的具体异常现象
>
> - `recommendations`: 建议操作
>   - `action`: 建议操作类型，可能值包括:
>     - `no_action`: 无需操作，健康内容
>     - `monitor`: 持续监控，存在轻微异常
>     - `scheduled_review`: 安排审核，存在值得关注的异常
>     - `immediate_review`: 立即审核，存在严重异常
>   - `risk_level`: 风险等级("low", "medium", "high", "critical")
>   - `potential_revenue_impact`: 潜在收益影响
>   - `suggested_steps`: 建议步骤，具体操作建议
>
> - `mcn_report`: (可选)MCN商业影响分析报告，适用于商业账号
>   - `summary`: 摘要信息
>   - `business_impact`: 商业影响评估
>     - `revenue_impact`: 收益影响评估
>     - `brand_safety_impact`: 品牌安全影响
>     - `platform_relationship`: 平台关系影响
>     - `contract_impact`: 合约影响评估
>   - `recommended_actions`: 建议操作清单
>   - `historical_context`: 历史背景数据
>
> ### 特性与优势:
> - 基于TikTok原生流量池(Traffic Pool)理论构建的精确评估系统
> - 8个维度、20+指标的全面分析，覆盖流量、互动、创作者、内容等全方位评估
> - 自适应算法，根据账号规模、认证状态、内容类型自动调整阈值
> - 基于大数据统计模型的异常检测，准确识别不自然流量模式
> - 为不同规模账号(微型、小型、中型、大型、超大型)提供定制化评估标准
> - 提供详细的商业影响分析和具体可行的建议步骤
>
> ### 示例响应:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/detect_fake_views",
>   "params": {
>     "item_id": "7460937381265411370",
>     "content_category": "verified_large"
>   },
>   "data": {
>     "video_metrics": {
>       "total_views": 159414915,
>       "total_likes": 15817234,
>       "total_comments": 392493,
>       "total_favorites": 1051470,
>       "total_shares": 1312741,
>       "engagement_rates": {
>         "like_ratio": 0.09922,
>         "comment_ratio": 0.00246,
>         "favorite_ratio": 0.0066,
>         "share_ratio": 0.00823
>       }
>     },
>     "creator_metrics": {
>       "account_age_days": 3733.94,
>       "follower_count": 89827771,
>       "verified": true,
>       "trust_score": 100
>     },
>     "content_metrics": {
>       "content_type": "video",
>       "created_by_ai": false,
>       "high_quality_upload": true
>     },
>     "fake_view_analysis": {
>       "fake_score": 7.16,
>       "confidence_level": "Minimal",
>       "estimated_fake_views": 7970745,
>       "fake_view_percentage": 5.0,
>       "is_suspicious": false,
>       "main_detection_reason": "Statistical View Anomalies",
>       "component_scores": {
>         "engagement_score": 0.0,
>         "distribution_score": 10.0,
>         "consistency_score": 0,
>         "creator_credibility_score": 0,
>         "content_authenticity_score": 34.0,
>         "follower_correlation_score": 35.0,
>         "racing_mechanism_score": 0,
>         "fan_growth_score": 45
>       }
>     },
>     "traffic_pool": {
>       "current_tier": 8,
>       "current_tier_name": "8th-Level Traffic Pool",
>       "expected_tier": 8,
>       "expected_tier_name": "8th-Level Traffic Pool",
>       "current_views_range": "30M+",
>       "expected_views_range": "30M+",
>       "estimated_organic_views": 148000807
>     },
>     "suspicious_features": [
>       "Suspicious: Reached 100000 followers from 10000 in only 31 days",
>       "Suspicious: Account gaining 24063 followers per day on average"
>     ],
>     "recommendations": {
>       "action": "no_action",
>       "risk_level": "low",
>       "potential_revenue_impact": "minimal",
>       "suggested_steps": [
>         "No immediate action required",
>         "Include in routine monitoring"
>       ]
>     },
>     "mcn_report": {
>       "summary": {
>         "estimated_revenue_impact": 7970.745,
>         "recommended_actions": "No immediate action required"
>       },
>       "business_impact": {
>         "revenue_impact": {
>           "level": "low",
>           "estimated_amount": 7970.745
>         },
>         "brand_safety_impact": {
>           "level": "minimal"
>         },
>         "platform_relationship": {
>           "status": "good"
>         }
>       }
>     }
>   }
> }
> ```
>
> # [English]
> ### Purpose:
> - Analyze TikTok video traffic data using advanced algorithms to precisely detect potential fake views and unnatural engagement
> - Evaluate content authenticity and traffic quality based on TikTok's Traffic Pool theory
> - Provide comprehensive fraud risk analysis with in-depth assessment across 8 dimensions and 20+ metrics
> - Deliver professional traffic quality reports and optimization recommendations for creators, MCN agencies, and content managers
>
> ### Parameters:
> - item_id: Video ID, required parameter, can be extracted from video URL (e.g., 7460937381265411370 from https://www.tiktok.com/@tiktok/video/7460937381265411370)
> - content_category: Content category, optional parameter, affects engagement rate benchmarks, options include:
>   - default: Default category for general content
>   - entertainment: Entertainment content, expected to have higher engagement
>   - education: Educational content, expected to have moderate engagement and higher save rates
>   - product: Product content, expected to have lower engagement but higher conversion
>   - verified_large: Large verified accounts, expected to have appropriately lower engagement rates
>
> ### Return Description:
> - `video_metrics`: Core video metrics
>   - `total_views`: Total number of views
>   - `total_likes`: Total number of likes
>   - `total_comments`: Total number of comments
>   - `total_favorites`: Total number of saves
>   - `total_shares`: Total number of shares
>   - `engagement_rates`: Engagement rate metrics, higher is better
>     - `like_ratio`: Like rate, normal range 1-10%, may be lower for large accounts
>     - `comment_ratio`: Comment rate, normal range 0.1-0.5%, excellent if above 1%
>     - `favorite_ratio`: Save rate, normal range 0.05-0.8%
>     - `share_ratio`: Share rate, normal range 0.05-0.5%, excellent if above 1%
>
> - `creator_metrics`: Creator account health indicators
>   - `account_age_days`: Account age in days, longer is more credible
>   - `follower_count`: Number of followers, affects expected view count
>   - `verified`: Whether account is verified, verified accounts have higher credibility
>   - `trust_score`: Account trust score (0-100), higher is more trustworthy
>
> - `content_metrics`: Content quality indicators
>   - `content_type`: Content type (video, image, etc.)
>   - `created_by_ai`: Whether AI-generated, AI-generated content may have specific traffic patterns
>   - `high_quality_upload`: Whether high-quality upload, high-quality uploads are more credible
>
> - `fake_view_analysis`: Comprehensive fake traffic analysis
>   - `fake_score`: Fake view score (0-100), lower is better:
>     - 0-20: Very low risk, natural traffic patterns
>     - 20-40: Low risk, may have minor anomalies but not problematic
>     - 40-60: Medium risk, anomalies worth attention
>     - 60-80: High risk, obvious fake traffic characteristics
>     - 80-100: Very high risk, almost certainly fake traffic
>   - `confidence_level`: Risk level, categorized as "Minimal", "Low", "Medium", "High"
>   - `estimated_fake_views`: Estimated fake views, calculated based on fake traffic model
>   - `fake_view_percentage`: Fake view percentage, proportion of fake views to total views
>   - `is_suspicious`: Whether suspicious, comprehensive judgment if attention is needed
>   - `main_detection_reason`: Main detection reason, most significant anomaly feature
>   - `component_scores`: Dimensional anomaly scores, each 0-100, lower is better:
>     - `engagement_score`: Engagement anomaly score
>     - `distribution_score`: Distribution anomaly score
>     - `consistency_score`: Consistency anomaly score
>     - `creator_credibility_score`: Creator credibility anomaly score
>     - `content_authenticity_score`: Content authenticity anomaly score
>     - `follower_correlation_score`: Follower correlation anomaly score
>     - `racing_mechanism_score`: Racing mechanism anomaly score
>     - `fan_growth_score`: Fan growth anomaly score
>
> - `traffic_pool`: Traffic pool analysis (TikTok racing mechanism)
>   - `current_tier`: Current traffic pool level (1-8), higher means more traffic
>   - `current_tier_name`: Current traffic pool name
>   - `expected_tier`: Expected traffic pool level, based on organic traffic prediction
>   - `expected_tier_name`: Expected traffic pool name
>   - `current_views_range`: Current traffic pool expected view range
>   - `expected_views_range`: Expected traffic pool view range
>   - `estimated_organic_views`: Estimated organic views, real views after deducting fake ones
>
> - `suspicious_features`: List of suspicious features, specific detected anomalies
>
> - `recommendations`: Recommended actions
>   - `action`: Recommended action type, possible values include:
>     - `no_action`: No action needed, healthy content
>     - `monitor`: Continuous monitoring, minor anomalies present
>     - `scheduled_review`: Schedule review, anomalies worth attention
>     - `immediate_review`: Immediate review, serious anomalies present
>   - `risk_level`: Risk level ("low", "medium", "high", "critical")
>   - `potential_revenue_impact`: Potential revenue impact
>   - `suggested_steps`: Suggested steps, specific action recommendations
>
> - `mcn_report`: (Optional) MCN business impact analysis report, applicable for business accounts
>   - `summary`: Summary information
>   - `business_impact`: Business impact assessment
>     - `revenue_impact`: Revenue impact assessment
>     - `brand_safety_impact`: Brand safety impact
>     - `platform_relationship`: Platform relationship impact
>     - `contract_impact`: Contract impact assessment
>   - `recommended_actions`: Recommended action list
>   - `historical_context`: Historical background data
>
> ### Features and Advantages:
> - Precise evaluation system built on TikTok's native Traffic Pool theory
> - Comprehensive analysis across 8 dimensions and 20+ metrics, covering traffic, engagement, creator, content, etc.
> - Adaptive algorithm automatically adjusts thresholds based on account size, verification status, content type
> - Anomaly detection based on big data statistical models, accurately identifies unnatural traffic patterns
> - Provides customized evaluation standards for different account sizes (micro, small, medium, large, extra-large)
> - Delivers detailed business impact analysis and specific, actionable recommendations
>
> ### Example Response:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/detect_fake_views",
>   "params": {
>     "item_id": "7460937381265411370",
>     "content_category": "verified_large"
>   },
>   "data": {
>     "video_metrics": {
>       "total_views": 159414915,
>       "total_likes": 15817234,
>       "total_comments": 392493,
>       "total_favorites": 1051470,
>       "total_shares": 1312741,
>       "engagement_rates": {
>         "like_ratio": 0.09922,
>         "comment_ratio": 0.00246,
>         "favorite_ratio": 0.0066,
>         "share_ratio": 0.00823
>       }
>     },
>     "creator_metrics": {
>       "account_age_days": 3733.94,
>       "follower_count": 89827771,
>       "verified": true,
>       "trust_score": 100
>     },
>     "content_metrics": {
>       "content_type": "video",
>       "created_by_ai": false,
>       "high_quality_upload": true
>     },
>     "fake_view_analysis": {
>       "fake_score": 7.16,
>       "confidence_level": "Minimal",
>       "estimated_fake_views": 7970745,
>       "fake_view_percentage": 5.0,
>       "is_suspicious": false,
>       "main_detection_reason": "Statistical View Anomalies",
>       "component_scores": {
>         "engagement_score": 0.0,
>         "distribution_score": 10.0,
>         "consistency_score": 0,
>         "creator_credibility_score": 0,
>         "content_authenticity_score": 34.0,
>         "follower_correlation_score": 35.0,
>         "racing_mechanism_score": 0,
>         "fan_growth_score": 45
>       }
>     },
>     "traffic_pool": {
>       "current_tier": 8,
>       "current_tier_name": "8th-Level Traffic Pool",
>       "expected_tier": 8,
>       "expected_tier_name": "8th-Level Traffic Pool",
>       "current_views_range": "30M+",
>       "expected_views_range": "30M+",
>       "estimated_organic_views": 148000807
>     },
>     "suspicious_features": [
>       "Suspicious: Reached 100000 followers from 10000 in only 31 days",
>       "Suspicious: Account gaining 24063 followers per day on average"
>     ],
>     "recommendations": {
>       "action": "no_action",
>       "risk_level": "low",
>       "potential_revenue_impact": "minimal",
>       "suggested_steps": [
>         "No immediate action required",
>         "Include in routine monitoring"
>       ]
>     },
>     "mcn_report": {
>       "summary": {
>         "estimated_revenue_impact": 7970.745,
>         "recommended_actions": "No immediate action required"
>       },
>       "business_impact": {
>         "revenue_impact": {
>           "level": "low",
>           "estimated_amount": 7970.745
>         },
>         "brand_safety_impact": {
>           "level": "minimal"
>         },
>         "platform_relationship": {
>           "status": "good"
>         }
>       }
>     }
>   }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7460937381265411370 | 无 |
| content_category | query | string | 否 | 内容分类/Content category, options: default, entertainment, education, product, verified_large | default | 无 | 无 |

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

<a id="get-api-u1-v1-tiktok-analytics-fetch-comment-keywords"></a>
### `GET /api/u1/v1/tiktok/analytics/fetch_comment_keywords`

- 摘要：获取视频评论关键词分析/Get comment keywords analysis
- 能力：评论 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_comment_keywords_api_v1_tiktok_analytics_fetch_comment_keywords_get`

#### 说明

> # [中文]
> ### 用途:
> - 分析视频评论中出现的热门关键词和话题，挖掘用户反馈
> - 提取观众评论中的主要内容和观点，帮助理解受众关注点
> - 支持创作者优化内容策略，增强与观众的互动和连接
>
> ### 参数:
> - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取
>
> ### 返回内容说明:
> - `item_id`: 请求的视频ID
> - `key_words`: 评论中提取的关键词列表，包含以下字段:
>   - `key_word`: 关键词文本
>   - `comments`: 包含该关键词的评论列表，每条评论包含:
>     - `cid`: 评论ID
>     - `text`: 评论内容
>     - `create_date`: 评论创建时间戳
>     - `digg_count`: 评论获赞数量
>     - `comment_type`: 评论类型
>     - `comment_author`: 评论作者信息
>       - `uid`: 用户ID
>       - `nick_name`: 用户昵称
>       - `cover`: 用户头像信息
>         - `url_list`: 头像URL列表
>
> ### 示例响应:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_comment_keywords",
>   "params": {
>     "item_id": "7502551047378832671"
>   },
>   "data": {
>     "item_id": "7502551047378832671",
>     "key_words": [
>       {
>         "key_word": "tik tok",
>         "comments": [
>           {
>             "cid": "7502621950457463574",
>             "comment_author": {
>               "nick_name": "ollie_russell05",
>               "uid": "7332627012203414560"
>             },
>             "create_date": 1746840350,
>             "digg_count": 17,
>             "text": "Imagine been tik tok and only getting 700 likes 🥀🙏😭"
>           }
>         ]
>       },
>       {
>         "key_word": "go viral",
>         "comments": [
>           {
>             "cid": "7502743477604680465",
>             "comment_author": {
>               "nick_name": "★ 🇦🇫",
>               "uid": "7274239704915149829"
>             },
>             "create_date": 1746868614,
>             "digg_count": 13,
>             "text": "I want to go viral"
>           }
>         ]
>       }
>     ]
>   }
> }
> ```
>
> # [English]
> ### Purpose:
> - Analyze popular keywords and topics in video comments to uncover user feedback
> - Extract main content and opinions from audience comments to understand viewer focus points
> - Support creators in optimizing content strategy and enhancing audience engagement and connection
>
> ### Parameters:
> - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio
>
> ### Return Description:
> - `item_id`: The requested video ID
> - `key_words`: List of keywords extracted from comments, including:
>   - `key_word`: Keyword text
>   - `comments`: List of comments containing this keyword, each comment includes:
>     - `cid`: Comment ID
>     - `text`: Comment content
>     - `create_date`: Comment creation timestamp
>     - `digg_count`: Number of likes on the comment
>     - `comment_type`: Comment type
>     - `comment_author`: Comment author information
>       - `uid`: User ID
>       - `nick_name`: User nickname
>       - `cover`: User avatar information
>         - `url_list`: List of avatar URLs
>
> ### Example Response:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_comment_keywords",
>   "params": {
>     "item_id": "7502551047378832671"
>   },
>   "data": {
>     "item_id": "7502551047378832671",
>     "key_words": [
>       {
>         "key_word": "tik tok",
>         "comments": [
>           {
>             "cid": "7502621950457463574",
>             "comment_author": {
>               "nick_name": "ollie_russell05",
>               "uid": "7332627012203414560"
>             },
>             "create_date": 1746840350,
>             "digg_count": 17,
>             "text": "Imagine been tik tok and only getting 700 likes 🥀🙏😭"
>           }
>         ]
>       },
>       {
>         "key_word": "go viral",
>         "comments": [
>           {
>             "cid": "7502743477604680465",
>             "comment_author": {
>               "nick_name": "★ 🇦🇫",
>               "uid": "7274239704915149829"
>             },
>             "create_date": 1746868614,
>             "digg_count": 13,
>             "text": "I want to go viral"
>           }
>         ]
>       }
>     ]
>   }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7502551047378832671 | 无 |

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

<a id="get-api-u1-v1-tiktok-analytics-fetch-creator-info-and-milestones"></a>
### `GET /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones`

- 摘要：获取创作者信息和里程碑数据/Get creator info and milestones
- 能力：创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_info_and_milestones_api_v1_tiktok_analytics_fetch_creator_info_and_milestones_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok创作者账号的基本信息和关键统计数据
> - 查看创作者账号的成长历程和达成的重要里程碑
> - 分析创作者账号发展轨迹，了解粉丝增长和内容影响力变化
>
> ### 参数:
> - user_id: 创作者用户ID，必填参数，可从用户主页URL或TikTok后台获取
>
> ### 返回内容说明:
> - `user_id`: 请求的创作者ID
> - `creator_info`: The creator's basic information
>   - `nickname`: 创作者昵称
>   - `sec_user_id`: 安全用户ID
>   - `unique_id`: 唯一用户名
>   - `avatar_url`: 头像URL
>   - `follower_count`: 粉丝数量
>   - `like_count`: 获赞总数
> - `milestones`: 创作者账号里程碑列表，每个里程碑包含:
>   - `milestone`: 里程碑类型ID
>   - `milestone_title`: 里程碑标题（如"达到100万粉丝"）
>   - `milestone_year`: 里程碑达成年份
>   - `milestone_month_day`: 里程碑达成月日
>   - `creator_summary`: 里程碑相关描述
>
> ### 示例响应:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_creator_info_and_milestones",
>   "params": {
>     "user_id": "107955"
>   },
>   "data": {
>     "user_id": "107955",
>     "creator_info": {
>       "avatar_url": "https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp",
>       "follower_count": 89812099,
>       "like_count": 382411162,
>       "nickname": "TikTok",
>       "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
>       "unique_id": "tiktok"
>     },
>     "milestones": [
>       {
>         "milestone": 6,
>         "milestone_month_day": "10/4",
>         "milestone_title": "Reached 1 million followers",
>         "milestone_year": "2015"
>       },
>       {
>         "milestone": 1,
>         "milestone_month_day": "2/27",
>         "milestone_title": "Started posting on TikTok",
>         "milestone_year": "2015"
>       }
>     ]
>   }
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve basic information and key metrics for TikTok creator accounts
> - View creator growth journey and important achieved milestones
> - Analyze creator account development trajectory, understand follower growth and content influence changes
>
> ### Parameters:
> - user_id: Creator user ID, required parameter, can be obtained from user profile URL or TikTok backend
>
> ### Return Description:
> - `user_id`: The requested creator ID
> - `creator_info`: The creator's basic information
>   - `nickname`: Creator's display name
>   - `sec_user_id`: Security user ID
>   - `unique_id`: Unique username
>   - `avatar_url`: Profile picture URL
>   - `follower_count`: Number of followers
>   - `like_count`: Total number of likes received
> - `milestones`: List of creator account milestones, each milestone includes:
>   - `milestone`: Milestone type ID
>   - `milestone_title`: Milestone title (e.g., "Reached 1 million followers")
>   - `milestone_year`: Year when the milestone was achieved
>   - `milestone_month_day`: Month and day when the milestone was achieved
>   - `creator_summary`: Milestone-related description
>
> ### Example Response:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_creator_info_and_milestones",
>   "params": {
>     "user_id": "107955"
>   },
>   "data": {
>     "user_id": "107955",
>     "creator_info": {
>       "avatar_url": "https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp",
>       "follower_count": 89812099,
>       "like_count": 382411162,
>       "nickname": "TikTok",
>       "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
>       "unique_id": "tiktok"
>     },
>     "milestones": [
>       {
>         "milestone": 6,
>         "milestone_month_day": "10/4",
>         "milestone_title": "Reached 1 million followers",
>         "milestone_year": "2015"
>       },
>       {
>         "milestone": 1,
>         "milestone_month_day": "2/27",
>         "milestone_title": "Started posting on TikTok",
>         "milestone_year": "2015"
>       }
>     ]
>   }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户id/User id | 无 | 107955 | 无 |

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

<a id="get-api-u1-v1-tiktok-analytics-fetch-video-metrics"></a>
### `GET /api/u1/v1/tiktok/analytics/fetch_video_metrics`

- 摘要：获取作品的统计数据/Get video metrics
- 能力：作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_metrics_api_v1_tiktok_analytics_fetch_video_metrics_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok视频的详细统计数据，包括观看量、点赞数、评论数和收藏数等核心指标
> - 提供总量统计以及从发布日期起14天的每日趋势数据，便于分析视频表现
> - 帮助创作者分析内容效果，评估用户互动情况，优化内容策略
>
> ### 参数:
> - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取
>
> ### 返回内容说明:
> - `item_id`: 请求的视频ID
> - `video_views`: 视频总观看次数
>   - `value`: 观看次数数值
> - `video_views_14_days`: 近14天的每日观看量趋势数据
>   - `interval`: 数据间隔类型
>   - `value`: 每日数据列表
> - `likes`: 视频总点赞数
>   - `value`: 点赞数值
> - `likes_14_days`: 近14天的每日点赞数趋势数据
> - `comments`: 视频总评论数
>   - `value`: 评论数值
> - `comments_14_days`: 近14天的每日评论数趋势数据
> - `favorites`: 视频总收藏数
>   - `value`: 收藏数值
> - `favorites_14_days`: 近14天的每日收藏数趋势数据
> - `video_summary`: 视频表现的概览分析
>   - `title`: 概览标题
>   - `content`: 概览内容
>   - `summary_type`: 概览类型
>
> ### 示例响应:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_video_metrics",
>   "params": {
>     "item_id": "7502551047378832671"
>   },
>   "data": {
>     "item_id": "7502551047378832671",
>     "video_views": {
>       "value": 1555500
>     },
>     "likes": {
>       "value": 11571
>     },
>     "comments": {
>       "value": 6920
>     },
>     "favorites": {
>       "value": 1243
>     },
>     "video_summary": {
>       "title": "Overview",
>       "content": "This post received more comments per view than most other posts."
>     }
>   }
> }
> ```
>
> # [English]
> ### Purpose:
> - Retrieve detailed analytics data for TikTok videos, including views, likes, comments, and favorites
> - Provide total statistics and daily trends for 14 days since the release date, facilitating video performance analysis
> - Help creators analyze content effectiveness, evaluate user engagement, and optimize content strategy
>
> ### Parameters:
> - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio
>
> ### Return Description:
> - `item_id`: The requested video ID
> - `video_views`: Total number of video views
>   - `value`: View count value
> - `video_views_14_days`: Daily view trends for the past 14 days
>   - `interval`: Data interval type
>   - `value`: List of daily data
> - `likes`: Total number of likes on the video
>   - `value`: Like count value
> - `likes_14_days`: Daily like trends for the past 14 days
> - `comments`: Total number of comments on the video
>   - `value`: Comment count value
> - `comments_14_days`: Daily comment trends for the past 14 days
> - `favorites`: Total number of times the video was favorited
>   - `value`: Favorite count value
> - `favorites_14_days`: Daily favorite trends for the past 14 days
> - `video_summary`: Overview analysis of video performance
>   - `title`: Overview title
>   - `content`: Overview content
>   - `summary_type`: Overview type
>
> ### Example Response:
> ```json
> {
>   "code": 200,
>   "router": "/api/v1/tiktok/analytics/fetch_video_metrics",
>   "params": {
>     "item_id": "7502551047378832671"
>   },
>   "data": {
>     "item_id": "7502551047378832671",
>     "video_views": {
>       "value": 1555500
>     },
>     "likes": {
>       "value": 11571
>     },
>     "comments": {
>       "value": 6920
>     },
>     "favorites": {
>       "value": 1243
>     },
>     "video_summary": {
>       "title": "Overview",
>       "content": "This post received more comments per view than most other posts."
>     }
>   }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7502551047378832671 | 无 |

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
