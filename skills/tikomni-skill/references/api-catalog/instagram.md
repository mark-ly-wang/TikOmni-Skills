# instagram API Catalog

- operation_count: 56

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/instagram/v1/fetch_cities | 获取国家城市列表/Get cities by country | header:authorization, query:country_code | query:page | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_comment_replies | 获取评论的子评论列表/Get comment replies | header:authorization, query:media_id, query:comment_id | query:min_id | comments | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_explore_sections | 获取探索页面分类/Get explore page sections | header:authorization | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_hashtag_posts | 获取话题标签下的帖子/Get posts by hashtag | header:authorization, query:hashtag | query:end_cursor | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_location_info | 获取地点信息/Get location info | header:authorization, query:location_id | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_location_posts | 获取地点下的帖子/Get posts by location | header:authorization, query:location_id | query:tab, query:end_cursor | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_locations | 获取城市地点列表/Get locations by city | header:authorization, query:city_id | query:page | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_music_posts | 获取使用特定音乐的帖子/Get posts using specific music | header:authorization | query:music_id, query:music_url, query:max_id | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_post_by_id | 通过ID获取帖子详情/Get post by ID | header:authorization, query:post_id | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_post_by_url | 通过URL获取帖子详情/Get post by URL | header:authorization, query:post_url | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_post_by_url_v2 | 通过URL获取帖子详情 V2/Get post by URL V2 | header:authorization, query:post_url | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_post_comments_v2 | 获取帖子评论列表V2/Get post comments V2 | header:authorization, query:media_id | query:sort_order, query:min_id | comments | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_related_profiles | 获取相关用户推荐/Get related profiles | header:authorization, query:user_id | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_search | 搜索用户/话题/地点/Search users/hashtags/places | header:authorization, query:query | query:select | search | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_section_posts | 获取分类下的帖子/Get posts by section | header:authorization, query:section_id | query:count, query:max_id | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_about_info | 获取用户的About信息/Get user about info | header:authorization, query:user_id | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_info_by_id | 根据用户ID获取用户数据/Get user data by user ID | header:authorization, query:user_id | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_info_by_id_v2 | 根据用户ID获取用户数据V2/Get user data by user ID V2 | header:authorization, query:user_id | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_info_by_username | 根据用户名获取用户数据/Get user data by username | header:authorization, query:username | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_info_by_username_v2 | 根据用户名获取用户数据V2/Get user data by username V2 | header:authorization, query:username | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_info_by_username_v3 | 根据用户名获取用户数据V3/Get user data by username V3 | header:authorization, query:username | - | author_profile | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_posts | 获取用户帖子列表/Get user posts list | header:authorization, query:user_id | query:count, query:max_id | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_posts_v2 | 获取用户帖子列表V2/Get user posts list V2 | header:authorization, query:user_id | query:count, query:end_cursor | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_reels | 获取用户Reels列表/Get user Reels list | header:authorization, query:user_id | query:count, query:max_id | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_reposts | 获取用户转发列表/Get user reposts list | header:authorization, query:user_id | query:max_id | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/fetch_user_tagged_posts | 获取用户被标记的帖子/Get user tagged posts | header:authorization, query:user_id | query:count, query:end_cursor | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/media_id_to_shortcode | Media ID转Shortcode/Convert media ID to shortcode | header:authorization, query:media_id | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/shortcode_to_media_id | Shortcode转Media ID/Convert shortcode to media ID | header:authorization, query:shortcode | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v1/user_id_to_username | 用户ID转用户信息/Get user info by user ID | header:authorization, query:user_id | - | other | Instagram-V1-API |
| GET | /api/u1/v1/instagram/v2/fetch_comment_replies | 获取评论回复/Get comment replies | header:authorization, query:code_or_url, query:comment_id | query:pagination_token | comments | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_hashtag_posts | 获取话题帖子/Get hashtag posts | header:authorization, query:keyword | query:feed_type, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_highlight_stories | 获取精选故事详情/Get highlight stories | header:authorization, query:highlight_id | - | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_location_posts | 获取地点帖子/Get location posts | header:authorization, query:location_id | query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_music_posts | 获取音乐帖子/Get music posts | header:authorization, query:audio_canonical_id | query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_post_comments | 获取帖子评论/Get post comments | header:authorization, query:code_or_url | query:sort_by, query:pagination_token | comments | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_post_info | 获取帖子详情/Get post info | header:authorization, query:code_or_url | - | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_post_likes | 获取帖子点赞列表/Get post likes | header:authorization, query:code_or_url | query:end_cursor | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_similar_users | 获取相似用户/Get similar users | header:authorization | query:username, query:user_id | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_followers | 获取用户粉丝/Get user followers | header:authorization | query:username, query:user_id, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_following | 获取用户关注/Get user following | header:authorization | query:username, query:user_id, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_highlights | 获取用户精选/Get user highlights | header:authorization | query:username, query:user_id | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_info | 获取用户信息/Get user info | header:authorization | query:username, query:user_id | author_profile | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_posts | 获取用户帖子/Get user posts | header:authorization | query:username, query:user_id, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_reels | 获取用户Reels/Get user reels | header:authorization | query:username, query:user_id, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_stories | 获取用户故事/Get user stories | header:authorization | query:username, query:user_id | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/fetch_user_tagged_posts | 获取用户被标记的帖子/Get user tagged posts | header:authorization | query:username, query:user_id, query:pagination_token | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/general_search | 综合搜索/General search | header:authorization, query:keyword | query:pagination_token | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/media_id_to_shortcode | Media ID转Shortcode/Convert media ID to shortcode | header:authorization, query:media_id | - | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_by_coordinates | 根据坐标搜索地点/Search locations by coordinates | header:authorization, query:latitude, query:longitude | - | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_hashtags | 搜索话题标签/Search hashtags | header:authorization, query:keyword | - | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_locations | 搜索地点/Search locations | header:authorization, query:keyword | - | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_music | 搜索音乐/Search music | header:authorization, query:keyword | - | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_reels | 搜索Reels/Search reels | header:authorization, query:keyword | query:pagination_token | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/search_users | 搜索用户/Search users | header:authorization, query:keyword | - | search | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/shortcode_to_media_id | Shortcode转Media ID/Convert shortcode to media ID | header:authorization, query:shortcode | - | other | Instagram-V2-API |
| GET | /api/u1/v1/instagram/v2/user_id_to_username | 用户ID转用户信息/Get user info by user ID | header:authorization, query:user_id | - | other | Instagram-V2-API |

