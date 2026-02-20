# weibo API Catalog

- operation_count: 64

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/weibo/app/fetch_ai_smart_search | AI智搜/AI Smart Search | query:query | query:page | search | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_home_recommend_feed | 获取首页推荐Feed流/Get home recommend feed | - | query:page, query:count | home_posts | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_hot_search | 获取热搜榜/Get hot search | - | query:category, query:page, query:count | search | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_hot_search_categories | 获取热搜分类列表/Get hot search categories | - | - | search | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_search_all | 综合搜索/Comprehensive search | query:query | query:page, query:search_type | search | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_status_comments | 获取微博评论/Get post comments | query:status_id | query:max_id, query:sort_type | comments | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_status_detail | 获取微博详情/Get post detail | query:status_id | - | single_post | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_status_likes | 获取微博点赞列表/Get post likes | query:status_id | query:attitude_type | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_status_reposts | 获取微博转发列表/Get post reposts | query:status_id | query:max_id | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_album | 获取用户相册/Get user album | query:uid | query:since_id | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_articles | 获取用户文章列表/Get user articles | query:uid | query:since_id | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_audios | 获取用户音频列表/Get user audios | query:uid | query:since_id | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_info | 获取用户信息/Get user information | query:uid | - | author_profile | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_info_detail | 获取用户详细信息/Get user detail information | query:uid | - | author_profile | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_profile_feed | 获取用户主页动态/Get user profile feed | query:uid | query:since_id | author_profile | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_super_topics | 获取用户参与的超话列表/Get user super topics | query:uid | query:page | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_timeline | 获取用户发布的微博/Get user timeline | query:uid | query:page, query:filter_type, query:month | home_posts | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_user_videos | 获取用户视频列表/Get user videos | query:uid | query:since_id | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_video_detail | 获取视频详情/Get video detail | query:mid | - | single_post | Weibo-App-API |
| GET | /api/u1/v1/weibo/app/fetch_video_featured_feed | 获取短视频精选Feed流/Get video featured feed | - | query:page | other | Weibo-App-API |
| GET | /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic | 检查微博是否允许带图评论/Check if Weibo allows image comments | query:id | - | comments | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_advanced_search | 微博高级搜索/Weibo Advanced Search | query:q | query:search_type, query:include_type, query:timescope, query:page | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_ai_related_search | 微博AI搜索内容扩展/Weibo AI Search Content Extension | query:keyword | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_ai_search | 微博智能搜索/Weibo AI Search | query:query | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_all_groups | 获取所有分组信息/Get all groups information | - | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_city_list | 地区省市映射/Region City List | - | query:normalized | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking | 获取微博文娱榜单/Get Weibo entertainment ranking | - | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline | 获取微博热门榜单时间轴/Get hot ranking timeline | query:ranking_type | query:since_id, query:max_id, query:count | home_posts | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_hot_search | 获取微博热搜榜单/Get Weibo hot search ranking | - | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_hot_search_index | 获取微博热搜词条(10条)/Get Weibo hot search index (10 items) | - | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_hot_search_summary | 获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items) | - | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_life_ranking | 获取微博生活榜单/Get Weibo life ranking | - | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_pic_search | 图片搜索/Weibo picture search | query:query | query:page | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_post_comments | 获取微博评论/Get Weibo comments | query:id | query:count, query:max_id | comments | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_post_detail | 获取单个作品数据/Get single post data | query:id | query:is_get_long_text | single_post | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_post_sub_comments | 获取微博子评论/Get Weibo sub-comments | query:id | query:count, query:max_id | comments | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_realtime_search | 实时搜索/Weibo Realtime Search | query:query | query:page | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_similar_search | 获取微博相似搜索词推荐/Get Weibo similar search recommendations | query:keyword | - | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_social_ranking | 获取微博社会榜单/Get Weibo social ranking | - | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_topic_search | 话题搜索/Weibo topic search | query:query | query:page | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_basic_info | 获取用户基本信息/Get user basic information | query:uid | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_fans | 获取用户粉丝列表/Get user fans list | query:uid | query:page | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_following | 获取用户关注列表/Get user following list | query:uid | query:page | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_info | 获取用户信息/Get user information | - | query:uid, query:custom | author_profile | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_original_posts | 获取微博用户原创微博数据/Get Weibo user original posts | query:uid | query:page, query:since_id | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_posts | 获取微博用户文章数据/Get Weibo user posts | query:uid | query:page, query:feature, query:since_id | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline | 获取微博主页推荐时间轴/Get user recommend timeline | - | query:refresh, query:group_id, query:containerid, query:extparam, query:max_id, query:count | home_posts | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_search | 用户搜索/User search | - | query:query, query:page, query:region, query:auth, query:gender, query:age, query:nickname, query:tag, ...(+2) | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail | 获取用户微博视频收藏夹详情/Get user video collection detail | query:cid | query:cursor, query:tab_code | single_post | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list | 获取用户微博视频收藏夹列表/Get user video collection list | query:uid | - | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_user_video_list | 获取微博用户全部视频/Get user all videos | query:uid | query:cursor | other | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/fetch_video_search | 视频搜索（热门/全部）/Weibo video search (hot/all) | query:query | query:mode, query:page | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web_v2/search_user_posts | 搜索用户微博/Search user posts | query:uid, query:q, query:starttime, query:endtime | query:page, query:hasori, query:hasret, query:hastext, query:haspic, query:hasvideo, query:hasmusic | search | Weibo-Web-V2-API |
| GET | /api/u1/v1/weibo/web/fetch_channel_feed | 根据频道名称获取热门内容/Get channel feed by name | - | query:channel_name, query:page | other | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_comment_replies | 获取评论子评论/Get comment replies | query:cid | query:max_id | comments | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_config_list | 获取频道配置列表/Get channel config list | - | - | other | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_hot_search | 获取热搜榜/Get hot search ranking | - | - | search | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_post_comments | 获取微博评论/Get post comments | query:post_id, query:mid | query:max_id, query:max_id_type | comments | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_post_detail | 获取微博详情/Get post detail | query:post_id | - | single_post | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_search | 搜索微博/Search Weibo | query:keyword | query:page, query:search_type, query:time_scope | search | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_search_topics | 获取搜索页热搜词/Get search page hot topics | - | - | search | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_trend_top | 获取频道热门趋势/Get channel trend top | query:containerid | query:page | other | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_user_info | 获取用户信息/Get user information | query:uid | - | author_profile | Weibo-Web-API |
| GET | /api/u1/v1/weibo/web/fetch_user_posts | 获取用户微博列表/Get user posts | query:uid | query:page, query:since_id | other | Weibo-Web-API |

