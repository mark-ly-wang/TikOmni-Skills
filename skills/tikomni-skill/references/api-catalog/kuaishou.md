# kuaishou API Catalog

- operation_count: 33

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/kuaishou/app/fetch_brand_top_list | 快手品牌榜单/Kuaishou brand top list | header:authorization | query:subTabId, query:subTabName | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_hot_board_categories | 快手热榜分类/Kuaishou hot categories | header:authorization | - | trend | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_hot_board_detail | 快手热榜详情/Kuaishou hot board detail | header:authorization | query:boardType, query:boardId | single_post | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_hot_search_person | 快手热搜人物榜单/Kuaishou hot search person board | header:authorization | - | search | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_live_top_list | 快手直播榜单/Kuaishou live top list | header:authorization | query:subTabId, query:subTabName | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_magic_face_hot | 获取魔法表情热门视频/Fetch magic face hot videos | header:authorization, query:magic_face_id | query:pcursor, query:count | trend | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_magic_face_usage | 获取魔法表情使用人数/Fetch magic face usage count | header:authorization, query:magic_face_id | - | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_one_user_v2 | 获取单个用户数据V2/Get single user data V2 | header:authorization, query:user_id | - | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_one_video | 视频详情V1/Video detailsV1 | header:authorization, query:photo_id | - | single_post | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_one_video_by_url | 根据链接获取单个作品数据/Fetch single video by URL | header:authorization, query:share_text | - | single_post | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_one_video_comment | 获取单个作品评论数据/Get single video comment data | header:authorization, query:photo_id | query:pcursor | single_post | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_shopping_top_list | 快手购物榜单/Kuaishou shopping top list | header:authorization | query:subTabId, query:subTabName | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_user_hot_post | 获取用户热门作品数据/Get user hot post data | header:authorization, query:user_id | query:pcursor | trend | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_user_live_info | 获取用户直播信息/Get user live info | header:authorization, query:user_id | - | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_user_post_v2 | 用户视频列表V2/User video list V2 | header:authorization, query:user_id | query:pcursor | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/fetch_videos_batch | 快手批量视频查询接口/Kuaishou batch video query API | header:authorization, query:photo_ids | - | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/generate_kuaishou_share_link | 生成快手分享链接/Generate Kuaishou share link | header:authorization, query:shareObjectId | - | other | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/search_comprehensive | 综合搜索/Comprehensive search | header:authorization, query:keyword | query:pcursor, query:sort_type, query:publish_time, query:duration, query:search_scope | search | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/search_user_v2 | 搜索用户V2/Search user V2 | header:authorization, query:keyword | query:page | search | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/app/search_video_v2 | 搜索视频V2/Search video V2 | header:authorization, query:keyword | query:page | search | Kuaishou-App-API |
| GET | /api/u1/v1/kuaishou/web/fetch_get_user_id | 获取用户ID/Fetch user ID | header:authorization, query:share_link | - | other | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v1 | 获取快手热榜 V1/Fetch Kuaishou Hot List V1 | header:authorization | - | trend | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v2 | 获取快手热榜 V2/Fetch Kuaishou Hot List V2 | header:authorization | query:board_type | trend | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_one_video | 获取单个作品数据 V1/Get single video data V1 | header:authorization, query:share_text | - | single_post | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_one_video_by_url | 链接获取作品数据/Fetch single video by URL | header:authorization, query:url | - | single_post | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_one_video_comment | 获取作品一级评论/Fetch video comments | header:authorization, query:photo_id | query:pcursor | single_post | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_one_video_sub_comment | 获取作品二级评论/Fetch video sub comments | header:authorization, query:photo_id, query:root_comment_id | query:pcursor | single_post | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2 | header:authorization, query:photo_id | - | single_post | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_user_collect | 获取用户收藏作品/Fetch user collect | header:authorization, query:user_id | query:pcursor | other | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_user_info | 获取用户信息/Fetch user info | header:authorization, query:user_id | - | author_profile | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_user_live_replay | 获取用户直播回放/Fetch user live replay | header:authorization, query:user_id | query:pcursor | other | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/fetch_user_post | 获取用户发布作品/Fetch user posts | header:authorization, query:user_id | query:pcursor | other | Kuaishou-Web-API |
| GET | /api/u1/v1/kuaishou/web/generate_share_short_url | 生成分享短连接/Generate share short URL | header:authorization, query:photo_id | - | other | Kuaishou-Web-API |

