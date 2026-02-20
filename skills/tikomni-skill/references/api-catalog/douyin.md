# douyin API Catalog

- operation_count: 247

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/douyin/app/v3/add_video_play_count | 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID | query:aweme_type, query:item_id | query:cookie | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list | 获取抖音品牌热榜分类数据/Get Douyin brand hot search list data | - | - | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list_detail | 获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data | query:category_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_general_search_result | 获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for altern... | query:keyword | query:offset, query:count, query:sort_type, query:publish_time, query:filter_duration, query:content_type | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_hashtag_detail | 获取指定话题的详情数据/Get details of specified hashtag | query:ch_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_hashtag_search_result | 获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative ... | query:keyword | query:offset, query:count | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_hashtag_video_list | 获取指定话题的作品数据/Get video list of specified hashtag | query:ch_id | query:cursor, query:sort_type, query:count | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_hot_search_list | 获取抖音热搜榜数据/Get Douyin hot search list data | - | query:board_type, query:board_sub_type | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_live_hot_search_list | 获取抖音直播热搜榜数据/Get Douyin live hot search list data | - | - | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_live_search_result | 获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative int... | query:keyword | query:cursor, query:count | search | Douyin-App-V3-API |
| POST | /api/u1/v1/douyin/app/v3/fetch_multi_video | 批量获取视频信息 V1/Batch Get Video Information V1 | body | - | other | Douyin-App-V3-API |
| POST | /api/u1/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url | 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos | - | body:aweme_ids | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_multi_video_statistics | 根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count... | query:aweme_ids | - | other | Douyin-App-V3-API |
| POST | /api/u1/v1/douyin/app/v3/fetch_multi_video_v2 | 批量获取视频信息 V2/Batch Get Video Information V2 | body | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_music_detail | 获取指定音乐的详情数据/Get details of specified music | query:music_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_music_hot_search_list | 获取抖音音乐榜数据/Get Douyin music hot search list data | - | query:chart_type, query:cursor | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_music_search_result | 获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative in... | query:keyword | query:offset, query:count | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_music_video_list | 获取指定音乐的视频列表数据/Get video list of specified music | query:music_id | query:cursor, query:count | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_one_video | 获取单个作品数据/Get single video data | query:aweme_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url | 根据分享链接获取单个作品数据/Get single video data by sharing link | query:share_url | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2 | query:aweme_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_one_video_v3 | 获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions) | query:aweme_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_series_detail | 获取短剧详情信息/Get series detail | query:series_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_series_video_list | 获取短剧视频列表/Get series video list | query:series_id | query:cursor | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_share_info_by_share_code | 根据分享口令获取分享信息/Get share info by share code | query:share_code | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_fans_list | 获取用户粉丝列表/Get user fans list | - | query:sec_user_id, query:max_time, query:count | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_following_list | 获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_f... | - | query:sec_user_id, query:max_time, query:count | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_like_videos | 获取用户喜欢作品数据/Get user like video data | query:sec_user_id | query:max_cursor, query:counts | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_post_videos | 获取用户主页作品数据/Get user homepage video data | query:sec_user_id | query:max_cursor, query:count, query:sort_type | home_posts | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_search_result | 获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative int... | query:keyword | query:offset, query:count, query:douyin_user_fans, query:douyin_user_type | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_user_series_list | 获取用户短剧合集列表/Get user series list | - | query:user_id, query:sec_user_id, query:cursor | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_comment_replies | 获取指定视频的评论回复数据/Get comment replies data of specified video | query:item_id, query:comment_id | query:cursor, query:count | comments | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_comments | 获取单个视频评论数据/Get single video comments data | query:aweme_id | query:cursor, query:count | comments | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url | 获取视频的最高画质播放链接/Get the highest quality play URL of the video | - | query:aweme_id, query:share_url | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_mix_detail | 获取抖音视频合集详情数据/Get Douyin video mix detail data | query:mix_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_mix_post_list | 获取抖音视频合集作品列表数据/Get Douyin video mix post list data | query:mix_id | query:cursor, query:count | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_search_result | 获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative in... | query:keyword | query:offset, query:count, query:sort_type, query:publish_time, query:filter_duration | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_search_result_v2 | 获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alterna... | query:keyword | query:sort_type, query:publish_time, query:filter_duration, query:page, query:search_id | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/fetch_video_statistics | 根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, ... | query:aweme_ids | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/generate_douyin_short_url | 生成抖音短链接/Generate Douyin short link | query:url | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/generate_douyin_video_share_qrcode | 生成抖音视频分享二维码/Generate Douyin video share QR code | query:object_id | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/handler_user_profile | 获取指定用户的信息/Get information of specified user | query:sec_user_id | - | author_profile | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/open_douyin_app_to_keyword_search | 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result | query:keyword | - | search | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/open_douyin_app_to_send_private_message | 生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users | query:uid, query:sec_uid | - | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/open_douyin_app_to_user_profile | 生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile | query:uid, query:sec_uid | - | author_profile | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/open_douyin_app_to_video_detail | 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page | query:aweme_id | - | single_post | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/app/v3/register_device | 抖音APP注册设备/Douyin APP register device | - | query:proxy | other | Douyin-App-V3-API |
| GET | /api/u1/v1/douyin/billboard/fetch_city_list | 获取中国城市列表/Fetch Chinese city list | - | - | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_content_tag | 获取垂类内容标签/Fetch vertical content tags | - | - | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list | 获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users | query:sec_uid | - | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list | 获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms | query:sec_uid | - | search | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list | 获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics | query:sec_uid | - | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list | 获取粉丝画像/Fetch fan portrait | query:sec_uid | query:option | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list | 获取账号作品分析-上周/Fetch account work analysis - last week | query:sec_uid | - | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_account_list | 获取热门账号/Fetch hot account list | - | body:date_window, body:page_num, body:page_size, body:query_tag | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_search_list | 搜索用户名或抖音号/Fetch account search list | query:keyword, query:cursor | - | search | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list | 获取账号粉丝数据趋势/Fetch account fan data trend | query:sec_uid | query:option, query:date_window | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail | 获取活动日历详情/Fetch activity calendar detail | query:calendar_id | - | single_post | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_calendar_list | 获取活动日历/Fetch activity calendar | - | body:city_code, body:category_code, body:end_date, body:start_date | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_category_list | 获取热点榜分类/Fetch hot list category | query:billboard_type | query:snapshot_time, query:start_date, query:end_date, query:keyword | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_challenge_list | 获取挑战热榜/Fetch hot challenge list | query:page, query:page_size | query:keyword | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_city_list | 获取同城热点榜/Fetch city hot list | query:page, query:page_size, query:order | query:city_code, query:sentence_tag, query:keyword | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list | 获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight | query:aweme_id | - | comments | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list | 获取作品数据趋势/Fetch post data trend | - | query:aweme_id, query:option, query:date_window | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_rise_list | 获取上升热点榜/Fetch rising hot list | query:page, query:page_size, query:order | query:sentence_tag, query:keyword | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list | 获取高涨粉率榜/Fetch high fan rate list | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list | 获取高点赞率榜/Fetch high like rate list | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list | 获取高完播率榜/Fetch high completion rate list | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list | 获取热度飙升的搜索榜/Fetch search list with rising popularity | - | body:page_num, body:page_size, body:date_window, body:keyword | search | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list | 获取热度飙升的话题榜/Fetch topic list with rising popularity | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list | 获取内容词详情/Fetch content word details | query:keyword, query:word_id, query:query_day | - | single_post | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list | 获取全部热门内容词/Fetch all hot content words | - | body:page_num, body:page_size, body:date_window, body:keyword | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_total_list | 获取热点总榜/Fetch total hot list | query:page, query:page_size, query:type | query:snapshot_time, query:start_date, query:end_date, query:sentence_tag, query:keyword | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list | 获取低粉爆款榜/Fetch low fan explosion list | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_search_list | 获取搜索热榜/Fetch search hot list | - | body:page_num, body:page_size, body:date_window, body:keyword | search | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list | 获取话题热榜/Fetch topic hot list | - | body:page, body:page_size, body:date_window, body:tags | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/billboard/fetch_hot_total_video_list | 获取视频热榜/Fetch video hot list | - | body:page, body:page_size, body:date_window, body:sub_type, body:tags | trend | Douyin-Billboard-API |
| GET | /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list | 获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only | query:aweme_id | query:option | trend | Douyin-Billboard-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis | 获取创作者账号诊断/Fetch author diagnosis | body:cookie | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical | 获取作品垂类标签/Fetch item analysis involved vertical | body:cookie, body:start_date, body:end_date | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance | 获取投稿表现数据/Fetch item analysis item performance | body:cookie, body:start_date, body:end_date, body:primary_verticals | body:genres, body:metric_type | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview | 获取投稿分析概览/Fetch item analysis overview | body:cookie, body:start_date, body:end_date, body:primary_verticals | body:genres | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_audience_others | 获取作品观众其他数据分析/Fetch item audience others analysis | body:cookie, body:item_id | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait | 获取作品观众数据分析/Fetch item audience portrait | body:cookie, body:item_id | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis | 获取作品弹幕分析/Fetch item bullet analysis | body:cookie, body:item_id | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_list | 获取投稿作品列表/Fetch item list | body:cookie, body:start_time, body:end_time | body:count, body:order_by, body:fields, body:need_cooperation, body:need_long_article, body:cursor | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_list_download | 导出投稿作品列表/Download item list | body:cookie, body:min_cursor, body:max_cursor | body:type_filters, body:need_long_article | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_overview_data | 获取作品总览数据/Fetch item overview data | body:cookie, body:ids | body:fields | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_play_source | 获取作品流量来源统计/Fetch item play source statistics | body:cookie, body:item_id | - | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword | 获取作品搜索关键词统计/Fetch item search keywords statistics | body:cookie, body:item_id | - | search | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend | 获取作品观看趋势分析/Fetch item watch trend analysis | body:cookie, body:item_id | body:analysis_type | other | Douyin-Creator-V2-API |
| POST | /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list | 获取直播场次历史记录/Fetch live room history list | body:cookie, body:start_date, body:end_date | body:limit, body:need_living, body:download | other | Douyin-Creator-V2-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_activity_detail | 获取创作者活动详情/Get creator activity detail | query:activity_id | - | single_post | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_activity_list | 获取创作者活动列表/Get creator activity list | query:start_time, query:end_time | - | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_content_category | 获取创作者内容创作合集分类/Get creator content creation category | - | - | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_content_course | 获取创作者内容创作课程/Get creator content creation course | query:category_id | query:order, query:limit, query:offset | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard | 获取创作者热门挑战榜单/Get creator hot challenge billboard | - | - | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_course | 获取创作者热门课程/Get creator hot course | - | query:order, query:limit, query:offset, query:category_id | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard | 获取创作者热门音乐榜单/Get creator hot music billboard | - | query:billboard_tag, query:order_key, query:time_filter | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard | 获取创作者热门道具榜单/Get creator hot props billboard | - | query:billboard_tag, query:order_key, query:time_filter | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard | 获取创作者中心创作热点/Get creator hot spot billboard | - | query:billboard_tag, query:hot_search_type, query:city_code | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard | 获取创作者热门话题榜单/Get creator hot topic billboard | - | query:billboard_tag, query:order_key, query:time_filter | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard | 获取创作者中心热门视频榜单/Get creator material center billboard | - | query:billboard_tag, query:order_key, query:time_filter | trend | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_creator_material_center_config | 获取创作者中心配置/Get creator material center config | - | - | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_industry_category_config | 获取行业分类配置/Get industry category config | - | - | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_mission_task_list | 获取商单任务列表/Get mission task list | - | query:cursor, query:limit, query:mission_type, query:tab_scene, query:industry_lv1, query:industry_lv2, query:platform_channel, query:pay_type, ...(+4) | other | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_user_search | 搜索用户/Search users | query:user_name | - | search | Douyin-Creator-API |
| GET | /api/u1/v1/douyin/creator/fetch_video_danmaku_list | 获取作品弹幕列表/Get video danmaku list | query:item_id | query:count, query:offset, query:order_type, query:is_blocked | other | Douyin-Creator-API |
| POST | /api/u1/v1/douyin/search/fetch_challenge_search_v1 | 获取话题搜索 V1/Fetch hashtag search V1 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_challenge_search_v2 | 获取话题搜索 V2/Fetch hashtag search V2 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_challenge_suggest | 获取话题推荐搜索/Fetch hashtag suggestions | - | body:keyword | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_discuss_search | 获取讨论搜索/Fetch discussion search | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_experience_search | 获取经验搜索/Fetch experience search | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_general_search_v1 | 获取综合搜索 V1/Fetch general search V1 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_general_search_v2 | 获取综合搜索 V2/Fetch general search V2 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_general_search_v3 | 获取综合搜索 V3/Fetch general search V3 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_image_search | 获取图片搜索/Fetch image search | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_image_search_v3 | 获取图文搜索 V3/Fetch image-text search V3 | body:keyword | body:cursor, body:search_id | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_live_search_v1 | 获取直播搜索 V1/Fetch live search V1 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_multi_search | 获取多重搜索/Fetch multi-type search | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_music_search | 获取音乐搜索/Fetch music search | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_school_search | 获取学校搜索/Fetch school search | - | body:keyword | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_search_suggest | 获取搜索关键词推荐/Fetch search keyword suggestions | - | body:keyword | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_user_search | 获取用户搜索/Fetch user search | - | body:keyword, body:cursor, body:douyin_user_fans, body:douyin_user_type, body:search_id | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_user_search_v2 | 获取用户搜索 V2/Fetch user search V2 | - | body:keyword, body:cursor | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_video_search_v1 | 获取视频搜索 V1/Fetch video search V1 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_video_search_v2 | 获取视频搜索 V2/Fetch video search V2 | - | body:keyword, body:cursor, body:sort_type, body:publish_time, body:filter_duration, body:content_type, body:search_id, body:backtrace | search | Douyin-Search-API |
| POST | /api/u1/v1/douyin/search/fetch_vision_search | 获取图像识别搜索/Fetch vision search (image-based search) | body:image_uri | body:cursor, body:search_id, body:search_source, body:detection, body:detection_index, body:user_query, body:aweme_id | search | Douyin-Search-API |
| GET | /api/u1/v1/douyin/web/douyin_live_room | 提取直播间弹幕/Extract live room danmaku | query:live_room_url, query:danmaku_type | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/encrypt_uid_to_sec_user_id | 加密用户uid到sec_user_id/Encrypt user uid to sec_user_id | query:uid | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_batch_user_profile_v1 | 获取批量用户信息(最多10个)/Get batch user profile (up to 10) | query:sec_user_ids | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_batch_user_profile_v2 | 获取批量用户信息(最多50个)/Get batch user profile (up to 50) | query:sec_user_ids | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_cartoon_aweme | 二次元作品推荐/Anime Video | query:count | query:refresh_index, query:cookie | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_challenge_posts | 话题作品/Challenge Posts | - | body:challenge_id, body:sort_type, body:cursor, body:count, body:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_douyin_web_guest_cookie | 获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web | query:user_agent | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_food_aweme | 美食作品推荐/Food Video | query:count | query:refresh_index, query:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_game_aweme | 游戏作品推荐/Game Video | query:count | query:refresh_index, query:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_general_search_result | 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords | query:keyword | query:offset, query:count, query:sort_type, query:publish_time, query:filter_duration, query:search_range, query:content_type, query:search_id | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_home_feed | 获取首页推荐数据/Get home feed data | - | query:count, query:refresh_index | home_posts | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_hot_search_result | 获取抖音热榜数据/Get Douyin hot search results | - | - | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_knowledge_aweme | 知识作品推荐/Knowledge Video | query:count | query:refresh_index, query:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_live_gift_ranking | 获取直播间送礼用户排行榜/Get live room gift user ranking | query:room_id | query:rank_type | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_live_im_fetch | 抖音直播间弹幕参数获取/Douyin live room danmaku parameters | query:room_id, query:user_unique_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_live_room_product_result | 抖音直播间商品信息/Douyin live room product information | query:room_id, query:author_id | query:offset, query:limit | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_live_search_result | 获取指定关键词的直播搜索结果/Get live search results of specified keywords | query:keyword | query:offset, query:count, query:search_id | search | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_multi_video | 批量获取视频信息/Batch Get Video Information | body | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_multi_video_high_quality_play_url | 批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos | - | body:aweme_ids | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_music_aweme | 音乐作品推荐/Music Video | query:count | query:refresh_index, query:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_one_video | 获取单个作品数据/Get single video data | query:aweme_id | query:need_anchor_info | single_post | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_one_video_by_share_url | 根据分享链接获取单个作品数据/Get single video data by sharing link | query:share_url | - | single_post | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_one_video_danmaku | 获取单个作品视频弹幕数据/Get single video danmaku data | query:item_id, query:duration, query:end_time, query:start_time | - | single_post | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2 | query:aweme_id | - | single_post | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_product_coupon | 获取商品优惠券信息/Get product coupon information | query:product_id, query:shop_id, query:price, query:author_id, query:sec_user_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_product_detail | 获取商品详情/Get product detail | query:product_id | query:aweme_id, query:room_id, query:sec_user_id | single_post | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_product_review_list | 获取商品评价列表/Get product review list | query:product_id, query:shop_id | query:cursor, query:count, query:sort_type | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_product_review_score | 获取商品评价评分/Get product review score | query:product_id, query:shop_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_product_sku_list | 获取商品SKU列表/Get product SKU list | query:product_id, query:author_id | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_query_user | 查询抖音用户基本信息/Query Douyin user basic information | - | body | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_related_posts | 获取相关作品推荐数据/Get related posts recommendation data | query:aweme_id | query:refresh_index, query:count | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_search_challenge | 搜索话题/Search Challenge | - | body:keyword, body:cursor, body:count, body:cookie | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_series_aweme | 短剧作品/Series Video | query:offset, query:count, query:content_type | query:cookie | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_user_collection_videos | 获取用户收藏作品数据/Get user collection video data | body:cookie | body:max_cursor, body:counts | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_user_collects | 获取用户收藏夹/Get user collection | body:cookie | body:max_cursor, body:counts | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_collects_videos | 获取用户收藏夹数据/Get user collection data | query:collects_id | query:max_cursor, query:counts | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_fans_list | 获取用户粉丝列表/Get user fans list | - | query:sec_user_id, query:max_time, query:count, query:source_type | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_following_list | 获取用户关注列表/Get user following list | - | query:sec_user_id, query:max_time, query:count, query:source_type | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/fetch_user_like_videos | 获取用户喜欢作品数据/Get user like video data | body:sec_user_id | body:max_cursor, body:counts, body:cookie | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_live_info_by_uid | 使用UID获取用户开播信息/Get user live information by UID | query:uid | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_live_videos | 获取用户直播流数据/Get user live video data | query:webcast_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id | 通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1 | query:room_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id_v2 | 通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2 | query:room_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_live_videos_by_sec_uid | 通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid | query:sec_uid | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_mix_videos | 获取用户合辑作品数据/Get user mix video data | query:mix_id | query:max_cursor, query:counts | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_post_videos | 获取用户主页作品数据/Get user homepage video data | query:sec_user_id | query:max_cursor, query:count, query:filter_type, query:cookie | home_posts | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_profile_by_short_id | 使用Short ID获取用户信息/Get user information by Short ID | query:short_id | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_profile_by_uid | 使用UID获取用户信息/Get user information by UID | query:uid | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_search_result | 获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following document for repl... | query:keyword | query:offset, query:count, query:douyin_user_fans, query:douyin_user_type, query:search_id | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_search_result_v2 | 获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the following document ... | query:keyword | query:cursor | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_user_search_result_v3 | 获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the following document ... | query:keyword | query:cursor, query:douyin_user_type, query:douyin_user_fans | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_channel_result | 抖音视频频道数据/Douyin video channel data | query:tag_id | query:count, query:refresh_index | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_comment_replies | 获取指定视频的评论回复数据/Get comment replies data of specified video | query:item_id, query:comment_id | query:cursor, query:count | comments | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_comments | 获取单个视频评论数据/Get single video comments data | query:aweme_id | query:cursor, query:count | comments | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_high_quality_play_url | 获取视频的最高画质播放链接/Get the highest quality play URL of the video | - | query:aweme_id, query:share_url | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_search_result | 获取指定关键词的视频搜索结果/Get video search results of specified keywords | query:keyword | query:offset, query:count, query:sort_type, query:publish_time, query:filter_duration, query:search_id | search | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/fetch_video_search_result_v2 | 获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the following document ... | query:keyword | query:sort_type, query:publish_time, query:filter_duration, query:page, query:search_id | search | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/generate_a_bogus | 使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL | body:url, body:data, body:user_agent | body:index_0, body:index_1, body:index_2 | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/generate_real_msToken | 生成真实msToken/Generate real msToken | - | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/generate_s_v_web_id | 生成s_v_web_id/Generate s_v_web_id | - | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/generate_ttwid | 生成ttwid/Generate ttwid | - | query:user_agent | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/generate_verify_fp | 生成verify_fp/Generate verify_fp | - | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/generate_wss_xb_signature | 生成弹幕xb签名/Generate barrage xb signature | query:user_agent, query:room_id, query:user_unique_id | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/generate_x_bogus | 使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL | body:url, body:user_agent | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/get_all_aweme_id | 提取列表作品id/Extract list video id | body | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/get_all_sec_user_id | 提取列表用户id/Extract list user id | body | - | other | Douyin-Web-API |
| POST | /api/u1/v1/douyin/web/get_all_webcast_id | 提取列表直播间号/Extract list webcast id | body | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/get_aweme_id | 提取单个作品id/Extract single video id | query:url | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/get_sec_user_id | 提取单个用户id/Extract single user id | query:url | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/get_webcast_id | 提取直播间号/Extract webcast id | query:url | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/handler_shorten_url | 生成短链接 | query:target_url | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/handler_user_profile | 使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id | query:sec_user_id | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/handler_user_profile_v2 | 使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id | query:unique_id | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/handler_user_profile_v3 | 根据抖音uid获取指定用户的信息/Get information of specified user by uid | query:uid | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/handler_user_profile_v4 | 根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand) | query:sec_user_id | - | author_profile | Douyin-Web-API |
| GET | /api/u1/v1/douyin/web/webcast_id_2_room_id | 直播间号转房间号/Webcast id to room id | query:webcast_id | - | other | Douyin-Web-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_base_info | 获取创作者基本信息/Get Author Base Info | query:o_author_id | query:platform_source, query:platform_channel, query:recommend, query:need_sec_uid, query:need_linkage_info | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info | 获取创作者商业卡片信息/Get Author Business Card Info | query:o_author_id | - | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords | 获取创作者内容热词/Get Author Content Hot Keywords | query:author_id | query:keyword_type | trend | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens | 获取创作者评论热词/Get Author Hot Comment Tokens | query:author_id | query:num, query:without_emoji | comments | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_local_info | 获取创作者位置信息/Get Author Local Info | query:o_author_id | query:platform_source, query:platform_channel, query:time_range | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_market_fields | 获取达人广场筛选字段/Get Author Market Fields | - | query:market_scene | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_show_items | 获取创作者视频列表/Get Author Show Items | query:o_author_id | query:platform_source, query:platform_channel, query:limit, query:only_assign, query:flow_type | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_author_spread_info | 获取创作者传播价值/Get Author Spread Info | query:o_author_id | query:platform_source, query:platform_channel, query:type, query:flow_type, query:only_assign, query:range | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide | 获取内容趋势指南/Get Content Trend Guide | - | - | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list | 搜索MCN机构列表/Get Demander MCN List | - | query:mcn_name, query:page, query:limit, query:order_by | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list | 获取优秀行业分类列表/Get Excellent Case Category List | - | query:platform_source | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail | 获取星图IP活动详情/Get IP Activity Detail | query:id | - | single_post | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list | 获取星图IP日历行业列表/Get IP Activity Industry List | - | - | other | Douyin-Xingtu-V2-API |
| POST | /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list | 获取星图IP日历活动列表/Get IP Activity List | body:query_start_time, body:query_end_time | body:industry_id_list, body:category_list, body:status_list | other | Douyin-Xingtu-V2-API |
| POST | /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog | 获取短剧演员热榜分类/Get Playlet Actor Rank Catalog | - | - | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list | 获取短剧演员热榜/Get Playlet Actor Rank List | - | query:category, query:name, query:qualifier, query:period, query:date, query:limit | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog | 获取星图热榜分类/Get Ranking List Catalog | - | query:codes, query:biz_scene | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data | 获取星图达人商业榜数据/Get Ranking List Data | - | query:code, query:qualifier, query:version, query:period, query:date, query:limit | other | Douyin-Xingtu-V2-API |
| POST | /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors | 获取相似创作者推荐/Get Recommend Similar Star Authors | body:author_ids | body:similar_type, body:page, body:limit | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_resource_list | 获取营销活动案例/Get Resource List | query:resource_id | - | other | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode | 获取用户主页二维码/Get User Profile QRCode | - | query:core_user_id, query:sec_uid | author_profile | Douyin-Xingtu-V2-API |
| GET | /api/u1/v1/douyin/xingtu/author_content_hot_comment_keywords_v1 | 获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1 | query:kolId | - | comments | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/author_hot_comment_tokens_v1 | 获取kol热词分析评论V1/Get Author Hot Comment Tokens V1 | query:kolId | - | comments | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/get_sign_image | 获取加密图片解析/Get Sign Image | query:uri | query:durationTS, query:format | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id | 根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id | query:sec_user_id | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_uid | 根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID | query:uid | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id | 根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id | query:unique_id | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_audience_portrait_v1 | 获取kol观众画像V1/Get kol Audience Portrait V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_base_info_v1 | 获取kol基本信息V1/Get kol Base Info V1 | query:kolId, query:platformChannel | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_conversion_ability_analysis_v1 | 获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1 | query:kolId, query:_range | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_convert_video_display_v1 | 获取kol转化视频展示V1/Get kol Convert Video Display V1 | query:kolId, query:detailType, query:page | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_cp_info_v1 | 获取kol性价比能力分析V1/Get kol Cp Info V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_daily_fans_v1 | 获取kol粉丝趋势V1/Get kol Daily Fans V1 | query:kolId, query:startDate, query:endDate | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_data_overview_v1 | 获取kol数据概览V1/Get kol Data Overview V1 | query:kolId, query:_type, query:_range, query:flowType | query:onlyAssign | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_fans_portrait_v1 | 获取kol粉丝画像V1/Get kol Fans Portrait V1 | query:kolId | query:fansType | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_link_struct_v1 | 获取kol连接用户V1/Get kol Link Struct V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_rec_videos_v1 | 获取kol内容表现V1/Get kol Rec Videos V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_service_price_v1 | 获取kol服务报价V1/Get kol Service Price V1 | query:kolId, query:platformChannel | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_touch_distribution_v1 | 获取kol连接用户来源V1/Get kol Touch Distribution V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_video_performance_v1 | 获取kol视频表现V1/Get kol Video Performance V1 | query:kolId, query:onlyAssign | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/kol_xingtu_index_v1 | 获取kol星图指数V1/Get kol Xingtu Index V1 | query:kolId | - | other | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/search_kol_v1 | 关键词搜索kol V1/Search Kol V1 | query:keyword, query:platformSource, query:page | - | search | Douyin-Xingtu-API |
| GET | /api/u1/v1/douyin/xingtu/search_kol_v2 | 高级搜索kol V2/Search Kol Advanced V2 | query:keyword | query:followerRange, query:contentTag | search | Douyin-Xingtu-API |

