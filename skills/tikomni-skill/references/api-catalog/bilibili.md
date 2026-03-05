# bilibili API Catalog

- operation_count: 41

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/bilibili/app/fetch_bangumi_tab | 获取番剧推荐/Get bangumi tab | header:authorization | - | other | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_cinema_tab | 获取影视推荐/Get cinema tab | header:authorization | - | other | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_home_feed | 获取主页推荐视频流/Get home feed | header:authorization | query:idx, query:flush, query:pull | home_posts | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_one_video | 获取单个视频详情信息/Get single video data | header:authorization | query:av_id, query:bv_id | single_post | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_popular_feed | 获取热门推荐/Get popular feed | header:authorization | query:idx, query:last_param | other | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_reply_detail | 获取二级评论回复/Get reply detail | header:authorization, query:root | query:av_id, query:bv_id, query:next_offset, query:ps | single_post | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_search_all | 综合搜索/search all | header:authorization, query:keyword | query:page, query:page_size, query:order | search | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_search_by_type | 分类搜索/ search by type | header:authorization, query:keyword | query:search_type, query:page, query:page_size, query:order | search | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_user_info | 获取用户信息/Get user info | header:authorization, query:user_id | - | author_profile | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_user_videos | 获取用户投稿视频/Get user videos | header:authorization, query:user_id | query:post_filter, query:page, query:ps | other | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/app/fetch_video_comments | 获取视频评论列表/Get video comments | header:authorization | query:av_id, query:bv_id, query:mode, query:next_offset | comments | Bilibili-App-API |
| GET | /api/u1/v1/bilibili/web/bv_to_aid | 通过bv号获得视频aid号/Generate aid by bvid | header:authorization, query:bv_id | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_all_live_areas | 获取所有直播分区列表/Get a list of all live areas | header:authorization | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_collect_folders | 获取用户所有收藏夹信息/Get user collection folders | header:authorization, query:uid | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_com_popular | 获取综合热门视频信息/Get comprehensive popular video information | header:authorization | query:pn | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_comment_reply | 获取视频下指定评论的回复/Get reply to the specified comment | header:authorization, query:bv_id, query:rpid | query:pn | comments | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_dynamic_detail | 获取动态详情/Get dynamic detail | header:authorization, query:dynamic_id | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_dynamic_detail_v2 | 获取动态详情v2/Get dynamic detail v2 | header:authorization, query:dynamic_id | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_general_search | 获取综合搜索信息/Get general search data | header:authorization, query:keyword, query:order, query:page, query:page_size | query:duration, query:pubtime_begin_s, query:pubtime_end_s | search | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_get_user_id | 提取用户ID/Extract user ID | header:authorization, query:share_link | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_hot_search | 获取热门搜索信息/Get hot search data | header:authorization, query:limit | - | search | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_live_room_detail | 获取指定直播间信息/Get information of specified live room | header:authorization, query:room_id | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_live_streamers | 获取指定分区正在直播的主播/Get live streamers of specified live area | header:authorization, query:area_id | query:pn | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_live_videos | 获取直播间视频流/Get live video data of specified room | header:authorization, query:room_id | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_one_video | 获取单个视频详情信息/Get single video data | header:authorization, query:bv_id | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_one_video_v2 | 获取单个视频详情信息V2/Get single video data V2 | header:authorization, query:a_id, query:c_id | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_one_video_v3 | 获取单个视频详情信息V3/Get single video data V3 | header:authorization, query:url | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_collection_videos | 获取指定收藏夹内视频数据/Gets video data from a collection folder | header:authorization, query:folder_id | query:pn | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_dynamic | 获取指定用户动态/Get dynamic information of specified user | header:authorization, query:uid | query:offset | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_post_videos | 获取用户主页作品数据/Get user homepage video data | header:authorization, query:uid | query:pn, query:order | home_posts | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_profile | 获取指定用户的信息/Get information of specified user | header:authorization, query:uid | - | author_profile | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_relation_stat | 获取用户关系状态统计/Get user relation stat (following and followers) | header:authorization, query:uid | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_user_up_stat | 获取UP主状态统计/Get UP stat (total likes and views) | header:authorization, query:uid | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_comments | 获取指定视频的评论/Get comments on the specified video | header:authorization, query:bv_id | query:pn | comments | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_danmaku | 获取视频实时弹幕/Get Video Danmaku | header:authorization, query:cid | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_detail | 获取单个视频详情/Get single video detail | header:authorization, query:aid | - | single_post | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_parts | 通过bv号获得视频分p信息/Get Video Parts By bvid | header:authorization, query:bv_id | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_play_info | 获取单个视频播放信息/Get single video play info | header:authorization, query:url | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_playurl | 获取视频流地址/Get video playurl | header:authorization, query:bv_id, query:cid | - | other | Bilibili-Web-API |
| GET | /api/u1/v1/bilibili/web/fetch_video_subtitle | 获取视频字幕信息/Get video subtitle info | header:authorization, query:a_id, query:c_id | - | asr_transcription | Bilibili-Web-API |
| POST | /api/u1/v1/bilibili/web/fetch_vip_video_playurl | 获取大会员清晰度视频流地址/Get VIP video playurl | header:authorization, body:bv_id, body:cid, body:cookie | - | other | Bilibili-Web-API |

