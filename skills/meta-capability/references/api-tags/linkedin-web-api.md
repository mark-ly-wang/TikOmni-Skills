# LinkedIn-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/linkedin-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`25`
- 常见能力：主页/账号 / 通用能力 / 作品详情 / 搜索 / 详情 / 评论
- 常见入参：`page`, `urn`, `company_id`, `pagination_token`, `sort_by`, `company`, `username`, `date_posted`, `experience_level`, `remote`
- 标签说明：**(LinkedIn Web数据接口/LinkedIn-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/linkedin/web/get_company_job_count`

- 能力：通用能力
- 入参：query: `company_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_company_job_count_api_v1_linkedin_web_get_company_job_count_get`

### `GET /api/u1/v1/linkedin/web/get_company_jobs`

- 能力：通用能力
- 入参：query: `company_id*`, `page`, `sort_by`, `date_posted`, `experience_level`, `remote`, `job_type`, `easy_apply`, `under_10_applicants`, `fair_chance_employer`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_company_jobs_api_v1_linkedin_web_get_company_jobs_get`

### `GET /api/u1/v1/linkedin/web/get_company_people`

- 能力：通用能力
- 入参：query: `company_id*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_company_people_api_v1_linkedin_web_get_company_people_get`

### `GET /api/u1/v1/linkedin/web/get_company_posts`

- 能力：作品详情
- 入参：query: `company_id*`, `page`, `sort_by`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_company_posts_api_v1_linkedin_web_get_company_posts_get`

### `GET /api/u1/v1/linkedin/web/get_company_profile`

- 能力：主页/账号
- 入参：query: `company`, `company_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_company_profile_api_v1_linkedin_web_get_company_profile_get`

### `GET /api/u1/v1/linkedin/web/get_job_detail`

- 能力：详情
- 入参：query: `job_id*`, `include_skills`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_job_detail_api_v1_linkedin_web_get_job_detail_get`

### `GET /api/u1/v1/linkedin/web/get_user_about`

- 能力：主页/账号
- 入参：query: `urn*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_about_api_v1_linkedin_web_get_user_about_get`

### `GET /api/u1/v1/linkedin/web/get_user_certifications`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_certifications_api_v1_linkedin_web_get_user_certifications_get`

### `GET /api/u1/v1/linkedin/web/get_user_comments`

- 能力：评论 / 主页/账号
- 入参：query: `urn*`, `page`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_comments_api_v1_linkedin_web_get_user_comments_get`

### `GET /api/u1/v1/linkedin/web/get_user_contact`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_contact_api_v1_linkedin_web_get_user_contact_get`

### `GET /api/u1/v1/linkedin/web/get_user_educations`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_educations_api_v1_linkedin_web_get_user_educations_get`

### `GET /api/u1/v1/linkedin/web/get_user_experience`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_experience_api_v1_linkedin_web_get_user_experience_get`

### `GET /api/u1/v1/linkedin/web/get_user_follower_and_connection`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_follower_and_connection_api_v1_linkedin_web_get_user_follower_and_connection_get`

### `GET /api/u1/v1/linkedin/web/get_user_honors`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_honors_api_v1_linkedin_web_get_user_honors_get`

### `GET /api/u1/v1/linkedin/web/get_user_images`

- 能力：主页/账号
- 入参：query: `urn*`, `page`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_images_api_v1_linkedin_web_get_user_images_get`

### `GET /api/u1/v1/linkedin/web/get_user_interests_companies`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_interests_companies_api_v1_linkedin_web_get_user_interests_companies_get`

### `GET /api/u1/v1/linkedin/web/get_user_interests_groups`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_interests_groups_api_v1_linkedin_web_get_user_interests_groups_get`

### `GET /api/u1/v1/linkedin/web/get_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `urn*`, `page`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_posts_api_v1_linkedin_web_get_user_posts_get`

### `GET /api/u1/v1/linkedin/web/get_user_profile`

- 能力：主页/账号
- 入参：query: `username*`, `include_follower_and_connection`, `include_experiences`, `include_skills`, `include_certifications`, `include_publications`, `include_educations`, `include_volunteers`, `include_honors`, `include_interests`, `include_bio`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_profile_api_v1_linkedin_web_get_user_profile_get`

### `GET /api/u1/v1/linkedin/web/get_user_publications`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_publications_api_v1_linkedin_web_get_user_publications_get`

### `GET /api/u1/v1/linkedin/web/get_user_recommendations`

- 能力：主页/账号
- 入参：query: `urn*`, `page`, `type`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_recommendations_api_v1_linkedin_web_get_user_recommendations_get`

### `GET /api/u1/v1/linkedin/web/get_user_skills`

- 能力：主页/账号
- 入参：query: `urn*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_skills_api_v1_linkedin_web_get_user_skills_get`

### `GET /api/u1/v1/linkedin/web/get_user_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `urn*`, `page`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_videos_api_v1_linkedin_web_get_user_videos_get`

### `GET /api/u1/v1/linkedin/web/search_jobs`

- 能力：搜索
- 入参：query: `keyword*`, `page`, `sort_by`, `date_posted`, `geocode`, `company`, `experience_level`, `remote`, `job_type`, `easy_apply`, `has_verifications`, `under_10_applicants`, `fair_chance_employer`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_jobs_api_v1_linkedin_web_search_jobs_get`

### `GET /api/u1/v1/linkedin/web/search_people`

- 能力：搜索
- 入参：query: `name`, `first_name`, `last_name`, `title`, `company`, `school`, `page`, `geocode_location`, `current_company`, `profile_language`, `industry`, `service_category`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_people_api_v1_linkedin_web_search_people_get`
