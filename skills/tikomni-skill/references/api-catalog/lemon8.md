# lemon8 API Catalog

- operation_count: 16

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/lemon8/app/fetch_discover_banners | 获取发现页Banner/Get banners of discover page | - | - | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_discover_tab | 获取发现页主体内容/Get main content of discover page | - | - | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_discover_tab_information_tabs | 获取发现页的 Editor's Picks/Get Editor's Picks of discover page | - | - | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_hot_search_keywords | 获取热搜关键词/Get hot search keywords | - | - | search | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_post_comment_list | 获取指定作品的评论列表/Get comments list of specified post | query:group_id, query:item_id, query:media_id | query:offset | comments | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_post_detail | 获取指定作品的信息/Get information of specified post | query:item_id | - | single_post | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_search | 搜索接口/Search API | query:query | query:max_cursor, query:filter_type, query:order_by, query:search_tab | search | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_topic_info | 获取话题信息/Get topic information | query:forum_id | - | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_topic_post_list | 获取话题作品列表/Get topic post list | query:category, query:category_parameter, query:hashtag_name | query:max_behot_time, query:sort_type | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_user_follower_list | 获取指定用户的粉丝列表/Get fans list of specified user | query:user_id | query:cursor | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_user_following_list | 获取指定用户的关注列表/Get following list of specified user | query:user_id | query:cursor | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/fetch_user_profile | 获取指定用户的信息/Get information of specified user | query:user_id | - | author_profile | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/get_item_id | 通过分享链接获取作品ID/Get post ID through sharing link | query:share_text | - | other | Lemon8-App-API |
| POST | /api/u1/v1/lemon8/app/get_item_ids | 通过分享链接批量获取作品ID/Get post IDs in batch through sharing links | body | - | other | Lemon8-App-API |
| GET | /api/u1/v1/lemon8/app/get_user_id | 通过分享链接获取用户ID/Get user ID through sharing link | query:share_text | - | other | Lemon8-App-API |
| POST | /api/u1/v1/lemon8/app/get_user_ids | 通过分享链接批量获取用户ID/Get user IDs in batch through sharing links | body | - | other | Lemon8-App-API |

