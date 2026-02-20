# pipixia API Catalog

- operation_count: 17

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/pipixia/app/fetch_hashtag_detail | 获取话题详情/Get hashtag detail | query:hashtag_id | - | single_post | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_hashtag_post_list | 获取话题作品列表/Get hashtag post list | query:hashtag_id | query:cursor, query:feed_count, query:hashtag_request_type, query:hashtag_sort_type | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_home_feed | 获取首页推荐/Get home feed | - | query:cursor | home_posts | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_home_short_drama_feed | 获取首页短剧推荐/Get home short drama feed | - | query:page | home_posts | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_hot_search_board_detail | 获取热搜榜单详情/Get hot search board detail | query:block_type | - | single_post | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_hot_search_board_list | 获取热搜榜单列表/Get hot search board list | - | - | search | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_hot_search_words | 获取热搜词条/Get hot search words | - | - | search | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_increase_post_view_count | 增加作品浏览数/Increase post view count | query:cell_id | query:cell_type | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_post_comment_list | 获取作品评论列表/Get post comment list | query:cell_id | query:cell_type, query:offset | comments | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_post_detail | 获取单个作品数据/Get single video data | query:cell_id | query:cell_type | single_post | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_post_statistics | 获取作品统计数据/Get post statistics | query:cell_id | - | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_search | 搜索接口/Search API | query:keyword | query:offset, query:search_type | search | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_short_url | 生成短连接/Generate short URL | query:original_url | - | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_user_follower_list | 获取用户粉丝列表/Get user follower list | query:user_id | query:cursor | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_user_following_list | 获取用户关注列表/Get user following list | query:user_id | query:cursor | other | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_user_info | 获取用户信息/Get user information | query:user_id | - | author_profile | PiPiXia-App-API |
| GET | /api/u1/v1/pipixia/app/fetch_user_post_list | 获取用户作品列表/Get user post list | query:user_id | query:cursor, query:feed_count | other | PiPiXia-App-API |

