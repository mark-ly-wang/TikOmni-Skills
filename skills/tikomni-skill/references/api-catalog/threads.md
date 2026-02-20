# threads API Catalog

- operation_count: 11

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/threads/web/fetch_post_comments | 获取帖子评论/Get post comments | query:post_id | query:end_cursor | comments | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_post_detail | 获取帖子详情/Get post detail | query:post_id | - | single_post | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_post_detail_v2 | 获取帖子详情 V2(支持链接)/Get post detail V2(supports URL) | - | query:post_id, query:url | single_post | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_user_info | 获取用户信息/Get user info | query:username | - | author_profile | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_user_info_by_id | 根据用户ID获取用户信息/Get user info by ID | query:user_id | - | author_profile | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_user_posts | 获取用户帖子列表/Get user posts | query:user_id | query:end_cursor | other | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_user_replies | 获取用户回复列表/Get user replies | query:user_id | query:end_cursor | other | Threads-Web-API |
| GET | /api/u1/v1/threads/web/fetch_user_reposts | 获取用户转发列表/Get user reposts | query:user_id | query:end_cursor | other | Threads-Web-API |
| GET | /api/u1/v1/threads/web/search_profiles | 搜索用户档案/Search profiles | query:query | - | author_profile | Threads-Web-API |
| GET | /api/u1/v1/threads/web/search_recent | 搜索最新内容/Search recent content | query:query | query:end_cursor | search | Threads-Web-API |
| GET | /api/u1/v1/threads/web/search_top | 搜索热门内容/Search top content | query:query | query:end_cursor | search | Threads-Web-API |

