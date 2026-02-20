# xigua API Catalog

- operation_count: 7

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/xigua/app/v2/fetch_one_video | 获取单个作品数据/Get single video data | query:item_id | - | single_post | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/fetch_one_video_play_url | 获取单个作品的播放链接/Get single video play URL | query:item_id | - | single_post | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2 | query:item_id | - | single_post | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/fetch_user_info | 个人信息/Personal information | query:user_id | - | author_profile | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/fetch_user_post_list | 获取个人作品列表/Get user post list | query:user_id | query:max_behot_time | other | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/fetch_video_comment_list | 视频评论列表/Video comment list | query:item_id | query:offset, query:count | comments | Xigua-App-V2-API |
| GET | /api/u1/v1/xigua/app/v2/search_video | 搜索视频/Search video | query:keyword | query:offset, query:order_type, query:min_duration, query:max_duration | search | Xigua-App-V2-API |

