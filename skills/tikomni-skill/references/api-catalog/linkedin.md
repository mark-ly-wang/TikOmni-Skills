# linkedin API Catalog

- operation_count: 25

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/linkedin/web/get_company_job_count | 获取公司职位数量/Get company job count | query:company_id | - | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_company_jobs | 获取公司职位/Get company jobs | query:company_id | query:page, query:sort_by, query:date_posted, query:experience_level, query:remote, query:job_type, query:easy_apply, query:under_10_applicants, ...(+1) | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_company_people | 获取公司员工/Get company people | query:company_id | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_company_posts | 获取公司帖子/Get company posts | query:company_id | query:page, query:sort_by | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_company_profile | 获取公司资料/Get company profile | - | query:company, query:company_id | author_profile | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_job_detail | 获取职位详情/Get job detail | query:job_id | query:include_skills | single_post | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_about | 获取用户简介/Get user about | query:urn | - | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_certifications | 获取用户认证/Get user certifications | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_comments | 获取用户评论/Get user comments | query:urn | query:page, query:pagination_token | comments | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_contact | 获取用户联系信息/Get user contact information | query:username | - | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_educations | 获取用户教育背景/Get user educations | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_experience | 获取用户工作经历/Get user experience | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_follower_and_connection | 获取用户粉丝和连接数/Get user follower and connection | query:username | - | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_honors | 获取用户荣誉奖项/Get user honors | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_images | 获取用户图片/Get user images | query:urn | query:page, query:pagination_token | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_interests_companies | 获取用户感兴趣的公司/Get user interests companies | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_interests_groups | 获取用户感兴趣的群组/Get user interests groups | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_posts | 获取用户帖子/Get user posts | query:urn | query:page, query:pagination_token | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_profile | 获取用户资料/Get user profile | query:username | query:include_follower_and_connection, query:include_experiences, query:include_skills, query:include_certifications, query:include_publications, query:include_educations, query:include_volunteers, query:include_honors, ...(+2) | author_profile | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_publications | 获取用户出版物/Get user publications | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_recommendations | 获取用户推荐信/Get user recommendations | query:urn | query:page, query:type, query:pagination_token | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_skills | 获取用户技能/Get user skills | query:urn | query:page | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/get_user_videos | 获取用户视频/Get user videos | query:urn | query:page, query:pagination_token | other | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/search_jobs | 搜索职位/Search jobs | query:keyword | query:page, query:sort_by, query:date_posted, query:geocode, query:company, query:experience_level, query:remote, query:job_type, ...(+4) | search | LinkedIn-Web-API |
| GET | /api/u1/v1/linkedin/web/search_people | 搜索用户/Search people | - | query:name, query:first_name, query:last_name, query:title, query:company, query:school, query:page, query:geocode_location, ...(+4) | search | LinkedIn-Web-API |

