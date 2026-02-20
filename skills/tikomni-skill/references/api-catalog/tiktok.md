# tiktok API Catalog

- operation_count: 204

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/tiktok/ads/get_ad_interactive_analysis | 获取广告互动分析/Get ad interactive analysis | query:material_id | query:metric_type, query:period_type | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_ad_keyframe_analysis | 获取广告关键帧分析/Get ad keyframe analysis | query:material_id | query:metric | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_ad_percentile | 获取广告百分位数据/Get ad percentile data | query:material_id | query:metric, query:period_type | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_ads_detail | 获取单个广告详情/Get single ad detail | query:ads_id | - | single_post | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_creative_patterns | 获取创意模式排行榜/Get creative pattern rankings | - | query:first_industry_id, query:period_type, query:order_field, query:order_type, query:week, query:page, query:limit | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_creator_filters | 获取创作者筛选器/Get creator filters | - | - | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_creator_list | 获取创作者列表/Get creator list | - | query:page, query:limit, query:sort_by, query:creator_country, query:audience_country, query:audience_count, query:keyword | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_hashtag_creator | 获取标签创作者信息/Get hashtag creator info | query:hashtag | - | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_hashtag_filters | 获取标签筛选器/Get hashtag filters | - | - | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_hashtag_list | 获取热门标签列表/Get popular hashtags list | - | query:page, query:limit, query:period, query:country_code, query:sort_by, query:industry_id, query:filter_by | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_keyword_details | 获取关键词详细信息/Get keyword details | - | query:keyword, query:page, query:limit, query:period, query:country_code, query:order_by, query:order_type, query:industry, ...(+2) | single_post | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_keyword_filters | 获取关键词筛选器/Get keyword filters | - | - | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_keyword_insights | 获取关键词洞察数据/Get keyword insights data | - | query:page, query:limit, query:period, query:country_code, query:order_by, query:order_type, query:industry, query:objective, ...(+2) | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_keyword_list | 获取关键词列表/Get keyword list | - | query:keyword, query:period, query:page, query:limit, query:country_code, query:industry | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_popular_trends | 获取流行趋势视频/Get popular trend videos | - | query:period, query:page, query:limit, query:order_by, query:country_code | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_product_detail | 获取产品详细信息/Get product detail | query:id | query:last, query:ecom_type, query:period_type, query:country_code | single_post | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_product_filters | 获取产品筛选器/Get product filters | - | - | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_product_metrics | 获取产品指标数据/Get product metrics | query:id | query:last, query:metrics, query:ecom_type, query:period_type, query:country_code | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_query_suggestions | 获取查询建议/Get query suggestions | - | query:count, query:scenario | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_recommended_ads | 获取推荐广告/Get recommended ads | query:material_id | query:industry, query:country_code | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_related_keywords | 获取相关关键词/Get related keywords | - | query:keyword, query:period, query:country_code, query:rank_type, query:content_type, query:page, query:limit | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_sound_detail | 获取音乐详情/Get sound detail | query:clip_id | query:period, query:country_code | single_post | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_sound_filters | 获取音乐筛选器/Get sound filters | - | query:rank_type | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_sound_rank_list | 获取热门音乐排行榜/Get popular sound rankings | - | query:period, query:page, query:limit, query:rank_type, query:new_on_board, query:commercial_music, query:country_code | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_sound_recommendations | 获取音乐推荐/Get sound recommendations | query:clip_id | query:limit | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_top_ads_spotlight | 获取热门广告聚光灯/Get top ads spotlight | - | query:industry, query:page, query:limit | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/get_top_products | 获取热门产品列表/Get top products list | - | query:last, query:page, query:limit, query:country_code, query:first_ecom_category_id, query:ecom_type, query:period_type, query:order_by, ...(+1) | other | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/search_ads | 搜索广告/Search ads | - | query:objective, query:like, query:period, query:industry, query:keyword, query:page, query:limit, query:order_by, ...(+4) | search | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/search_creators | 搜索创作者/Search creators | query:keyword | query:page, query:limit, query:sort_by, query:creator_country | search | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/search_sound | 搜索音乐/Search sounds | query:keyword | query:period, query:page, query:limit, query:rank_type, query:new_on_board, query:commercial_music, query:country_code | search | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/ads/search_sound_hint | 搜索音乐提示/Search sound hints | query:keyword | query:period, query:page, query:limit, query:rank_type, query:country_code, query:filter_by_checked, query:commercial_music | search | TikTok-Ads-API |
| GET | /api/u1/v1/tiktok/analytics/detect_fake_views | 检测视频虚假流量分析/Detect fake views in video | query:item_id | query:content_category | other | TikTok-Analytics-API |
| GET | /api/u1/v1/tiktok/analytics/fetch_comment_keywords | 获取视频评论关键词分析/Get comment keywords analysis | query:item_id | - | comments | TikTok-Analytics-API |
| GET | /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones | 获取创作者信息和里程碑数据/Get creator info and milestones | query:user_id | - | other | TikTok-Analytics-API |
| GET | /api/u1/v1/tiktok/analytics/fetch_video_metrics | 获取作品的统计数据/Get video metrics | query:item_id | - | other | TikTok-Analytics-API |
| GET | /api/u1/v1/tiktok/app/v3/add_video_play_count | 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID | query:aweme_type, query:item_id | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/check_live_room_online | 检测直播间是否在线/Check if live room is online | query:room_id | - | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/check_live_room_online_batch | 批量检测直播间是否在线/Batch check if live rooms are online | - | body:room_ids | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request | 加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body | - | body:username, body:password, body:mode | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/fetch_content_translate | 获取内容翻译数据/Get content translation data | - | body:trg_lang, body:src_content | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_info | 获取带货创作者信息/Get shopping creator information | query:creator_uid | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights | 创作者搜索洞察/Creator Search Insights | - | query:offset, query:limit, query:tab, query:language_filters, query:category_filters, query:creator_source, query:force_refresh | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail | 创作者搜索洞察详情/Creator Search Insights Detail | query:query_id_str | query:time_range, query:start_date, query:end_date, query:dimension_list | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend | 创作者搜索洞察趋势/Creator Search Insights Trend | query:query_id_str | query:from_tab_path, query:query_analysis_required | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos | 创作者搜索洞察相关视频/Creator Search Insights Videos | query:keyword | query:offset, query:count | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list | 获取创作者橱窗商品列表/Get creator showcase product list | query:kol_id | query:count, query:next_scroll_param | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_general_search_result | 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords | query:keyword | query:offset, query:count, query:sort_type, query:publish_time | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail | 获取指定话题的详情数据/Get details of specified hashtag | query:ch_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result | 获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords | query:keyword | query:offset, query:count | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list | 获取指定话题的作品数据/Get video list of specified hashtag | query:ch_id | query:cursor, query:count | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/fetch_home_feed | 获取主页视频推荐数据/Get home feed(recommend) video data | - | body:cookie | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank | 获取直播每日榜单数据/Get live daily rank data | - | query:anchor_id, query:room_id, query:rank_type, query:region_type, query:gap_interval, query:cookie | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list | 获取直播间排行榜数据/Get live room ranking list | query:room_id, query:anchor_id | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_room_info | 获取指定直播间的数据/Get data of specified live room | query:room_id | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list | 获取直播间商品列表数据/Get live room product list data | query:room_id, query:author_id | query:page_size, query:offset, query:region, query:cookie | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2 | 获取直播间商品列表数据 V2 /Get live room product list data V2 | query:room_id, query:author_id | query:page_size, query:offset, query:region, query:cookie | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_live_search_result | 获取指定关键词的直播搜索结果/Get live search results of specified keywords | query:keyword | query:offset, query:count, query:region | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_location_search | 获取地点搜索结果/Get location search results | query:keyword | query:offset, query:count | search | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/fetch_multi_video | 批量获取视频信息/Batch Get Video Information | body | - | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2 | 批量获取视频信息 V2/Batch Get Video Information V2 | body | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_music_chart_list | 音乐排行榜/Music Chart List | - | query:scene, query:cursor, query:count | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_music_detail | 获取指定音乐的详情数据/Get details of specified music | query:music_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_music_search_result | 获取指定关键词的音乐搜索结果/Get music search results of specified keywords | query:keyword | query:offset, query:count, query:filter_by, query:sort_type, query:region | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_music_video_list | 获取指定音乐的视频列表数据/Get video list of specified music | query:music_id | query:cursor, query:count | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_one_video | 获取单个作品数据/Get single video data | query:aweme_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url | 根据分享链接获取单个作品数据/Get single video data by sharing link | query:share_url | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2 | 根据分享链接获取单个作品数据/Get single video data by sharing link | query:share_url | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_one_video_v2 | 获取单个作品数据 V2/Get single video data V2 | query:aweme_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_one_video_v3 | 获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter) | query:aweme_id | query:region | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_detail | 获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead) | query:product_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2 | 获取商品详情数据V2/Get product detail data V2 | query:product_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3 | 获取商品详情数据V3 / Get product detail data V3 | query:product_id | query:region | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4 | 获取商品详情数据V4 / Get product detail data V4 | query:product_id | query:region | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link | 通过分享链接获取商品ID/Get Product ID by Share Link | query:share_link | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_review | 获取商品评价数据/Get product review data | query:product_id | query:cursor, query:size, query:filter_id, query:sort_type | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_product_search | 获取商品搜索结果/Get product search results | query:keyword | query:cursor, query:count, query:sort_type, query:customer_review_four_star, query:have_discount, query:min_price, query:max_price | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_share_qr_code | 获取分享二维码/Get share QR code | query:object_id | query:schema_type | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_share_short_link | 获取分享短链接/Get share short link | query:url | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_home | 获取商家主页数据/Get shop home page data | query:page_id, query:seller_id | - | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list | 获取商家主页Page列表数据/Get shop home page list data | query:seller_id | - | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link | 通过分享链接获取店铺ID/Get Shop ID by Share Link | query:share_link | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_info | 获取商家信息数据/Get shop information data | query:shop_id | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_product_category | 获取商家产品分类数据/Get shop product category data | query:seller_id | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_product_list | 获取商家商品列表数据/Get shop product list data | query:seller_id | query:scroll_params, query:page_size, query:sort_field, query:sort_order | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2 | 获取商家商品列表数据 V2/Get shop product list data V2 | query:seller_id | query:scroll_params, query:page_size, query:sort_field, query:sort_order | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend | 获取商家商品推荐数据/Get shop product recommend data | query:seller_id | query:scroll_param, query:page_size | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations | 获取类似用户推荐/Similar User Recommendations | query:sec_uid | query:page_token | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username | 通过用户名获取用户账号国家地区/Get user account country by username | query:username | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_follower_list | 获取指定用户的粉丝列表数据/Get follower list of specified user | - | query:user_id, query:sec_user_id, query:count, query:min_time, query:page_token | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_following_list | 获取指定用户的关注列表数据/Get following list of specified user | - | query:user_id, query:sec_user_id, query:count, query:min_time, query:page_token | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_like_videos | 获取用户喜欢作品数据/Get user like video data | query:sec_user_id | query:max_cursor, query:counts | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_music_list | 获取用户音乐列表数据/Get user music list data | query:sec_uid | query:cursor, query:count | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_post_videos | 获取用户主页作品数据 V1/Get user homepage video data V1 | - | query:sec_user_id, query:unique_id, query:max_cursor, query:count, query:sort_type | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2 | 获取用户主页作品数据 V2/Get user homepage video data V2 | - | query:sec_user_id, query:unique_id, query:max_cursor, query:count, query:sort_type | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3 | 获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster) | - | query:sec_user_id, query:unique_id, query:max_cursor, query:count, query:sort_type | home_posts | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos | 获取用户转发的作品数据/Get user repost video data | query:user_id | query:offset, query:count | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_user_search_result | 获取指定关键词的用户搜索结果/Get user search results of specified keywords | query:keyword | query:offset, query:count, query:user_search_follower_count, query:user_search_profile_type, query:user_search_other_pref | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies | 获取指定视频的评论回复数据/Get comment replies data of specified video | query:item_id, query:comment_id | query:cursor, query:count | comments | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_video_comments | 获取单个视频评论数据/Get single video comments data | query:aweme_id | query:cursor, query:count | comments | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_video_search_result | 获取指定关键词的视频搜索结果/Get video search results of specified keywords | query:keyword | query:offset, query:count, query:sort_type, query:publish_time, query:region | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info | 获取指定 Webcast 用户的信息/Get information of specified Webcast user | - | query:user_id, query:sec_user_id | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username | 使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username | query:username | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/handler_user_profile | 获取指定用户的信息/Get information of specified user | - | query:user_id, query:sec_user_id, query:unique_id | author_profile | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search | 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result | query:keyword | - | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message | 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users | query:uid | - | other | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile | 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile | query:uid | - | author_profile | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail | 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page | query:aweme_id | - | single_post | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/search_follower_list | 搜索粉丝列表/Search follower list | query:user_id, query:keyword | - | search | TikTok-App-V3-API |
| GET | /api/u1/v1/tiktok/app/v3/search_following_list | 搜索关注列表/Search following list | query:user_id, query:keyword | - | search | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm | TikTok APP加密算法/TikTok APP encryption algorithm | - | body:url, body:data, body:device_info | other | TikTok-App-V3-API |
| POST | /api/u1/v1/tiktok/creator/get_account_health_status | 获取创作者账号健康状态/Get Creator Account Health Status | - | body:cookie, body:proxy | health | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_account_insights_overview | 获取创作者账号概览/Get Creator Account Overview | - | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_account_violation_list | 获取创作者账号违规记录列表/Get Creator Account Violation Record List | - | body:cookie, body:proxy, body:page | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_creator_account_info | 获取创作者账号信息/Get Creator Account Info | - | body:cookie, body:proxy | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_live_analytics_summary | 获取创作者直播概览/Get Creator Live Overview | - | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_product_analytics_list | 获取创作者商品列表分析/Get Creator Product List Analytics | - | body:cookie, body:proxy, body:start_date, body:end_date, body:page | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_product_related_videos | 获取同款商品关联视频/Get Product Related Videos | body:item_id, body:product_id | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_showcase_product_list | 获取橱窗商品列表/Get Showcase Product List | - | body:cookie, body:proxy, body:count, body:offset | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_analytics_summary | 获取创作者视频概览/Get Creator Video Overview | - | body:cookie, body:proxy | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_associated_product_list | 获取视频关联商品列表/Get Video Associated Product List | body:item_ids | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_audience_stats | 获取视频受众分析数据/Get Video Audience Analysis Data | body:item_id | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_detailed_stats | 获取视频详细分段统计数据/Get Video Detailed Statistics | body:item_id | body:cookie, body:proxy, body:start_date | single_post | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_list_analytics | 获取创作者视频列表分析/Get Creator Video List Analytics | - | body:cookie, body:proxy, body:start_date, body:page, body:rules | other | TikTok-Creator-API |
| POST | /api/u1/v1/tiktok/creator/get_video_to_product_stats | 获取视频与商品关联统计数据/Get Video-Product Association Statistics | body:item_id, body:product_id | body:cookie, body:proxy, body:start_date | other | TikTok-Creator-API |
| GET | /api/u1/v1/tiktok/interaction/apply | 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope) | query:api_key, query:invite_code | - | other | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/collect | 收藏/Collect | - | body:aweme_id, body:cookie, body:device_id, body:iid, body:proxy | other | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/follow | 关注/Follow | - | body:user_id, body:sec_user_id, body:cookie, body:device_id, body:iid, body:proxy | other | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/forward | 转发/Forward | - | body:aweme_id, body:cookie, body:device_id, body:iid, body:proxy | other | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/like | 点赞/Like | - | body:aweme_id, body:cookie, body:device_id, body:iid, body:proxy | other | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/post_comment | 发送评论/Post comment | - | body:aweme_id, body:text, body:cookie, body:device_id, body:iid, body:proxy | comments | TikTok-Interaction-API |
| POST | /api/u1/v1/tiktok/interaction/reply_comment | 回复评论/Reply to comment | - | body:aweme_id, body:reply_id, body:text, body:cookie, body:device_id, body:iid, body:proxy | comments | TikTok-Interaction-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list | 获取热卖商品列表/Get hot selling products list | - | query:region | trend | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_product_detail | 获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data) | query:product_id | query:seller_id, query:region | single_post | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2 | 获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data) | query:product_id | query:seller_id, query:region | single_post | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3 | 获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data) | query:product_id | query:region | single_post | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1 | 获取商品评论V1/Get product reviews V1 | query:product_id | query:sort_type, query:filter_id, query:offset | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2 | 获取商品评论V2/Get product reviews V2 | query:product_id | query:page_start, query:sort_rule, query:filter_type, query:filter_value, query:region | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id | 根据分类ID获取商品列表/Get products by category ID | query:category_id | query:offset, query:region | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_products_category_list | 获取商品分类列表/Get product category list | - | query:region | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_search_products_list | 搜索商品列表V1/Search products list V1 | query:search_word | query:offset, query:page_token, query:region | search | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2 | 搜索商品列表V2(移动端)/Search products list V2 (Mobile) | query:search_word | query:offset, query:page_token, query:region | search | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3 | 搜索商品列表V3/Search products list V3 | query:keyword | query:offset, query:region, query:sort_by, query:filters_data | search | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion | 获取搜索关键词建议V1/Get search keyword suggestions V1 | query:search_word | query:lang, query:region | search | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2 | 获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile) | query:search_word | query:lang, query:region | search | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_seller_products_list | 获取商家商品列表V1/Get seller products list V1 | query:seller_id | query:search_params, query:region | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2 | 获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile) | query:seller_id | query:searchParams, query:region | other | TikTok-Shop-Web-API |
| GET | /api/u1/v1/tiktok/web/decrypt_strData | 解密strData/Decrypt strData | query:encrypted_data | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/device_register | 设备注册/Register device for TikTok Web | - | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/encrypt_strData | 加密strData/Encrypt strData | query:data | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_batch_check_live_alive | 批量直播间开播状态检测/Batch live room start status check | query:room_ids | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_check_live_alive | 直播间开播状态检测/Live room start status check | query:room_id | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_explore_post | 获取探索作品数据/Get explore video data | - | query:categoryType, query:count | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_general_search | 获取综合搜索列表/Get general search list | query:keyword | query:offset, query:search_id, query:cookie | search | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/fetch_gift_name_by_id | 根据Gift ID查询礼物名称/Get gift name by gift ID | body:gift_id | - | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/fetch_gift_names_by_ids | 批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50) | body:gift_ids | - | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/fetch_home_feed | 首页推荐作品/Home Feed | - | body:count, body:cookie | home_posts | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_live_gift_list | 获取直播间礼物列表/Get live room gift list | - | query:room_id | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_live_im_fetch | TikTok直播间弹幕参数获取/tiktok live room danmaku parameters | query:room_id, query:user_unique_id | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_live_recommend | 获取直播间首页推荐列表/Get live room homepage recommendation list | query:related_live_tag | - | home_posts | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_post_comment | 获取作品的评论列表/Get video comments | query:aweme_id | query:cursor, query:count, query:current_region | comments | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_post_comment_reply | 获取作品的评论回复列表/Get video comment replies | query:item_id, query:comment_id | query:cursor, query:count, query:current_region | comments | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_post_detail | 获取单个作品数据/Get single video data | query:itemId | - | single_post | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_post_detail_v2 | 获取单个作品数据 V2/Get single video data V2 | query:itemId | - | single_post | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_search_keyword_suggest | 搜索关键字推荐/Search keyword suggest | query:keyword | - | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_search_live | 搜索直播/Search live | query:keyword | query:count, query:offset, query:search_id, query:cookie | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_search_photo | 搜索照片/Search photo | query:keyword | query:count, query:offset, query:search_id, query:cookie | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_search_user | 搜索用户/Search user | query:keyword | query:cursor, query:search_id, query:cookie | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_search_video | 搜索视频/Search video | query:keyword | query:count, query:offset, query:search_id, query:cookie | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_sso_login_auth | 认证SSO登录/Authenticate SSO login | query:device_id, query:verifyFp, query:region, query:proxy | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_sso_login_qrcode | 获取SSO登录二维码/Get SSO login QR code | query:device_id, query:region, query:proxy | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_sso_login_status | 获取SSO登录状态/Get SSO login status | query:token, query:device_id, query:verifyFp, query:region, query:proxy | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_tag_detail | Tag详情/Tag Detail | query:tag_name | - | single_post | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_tag_post | Tag作品/Tag Post | query:challengeID | query:count, query:cursor | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_tiktok_live_data | 通过直播链接获取直播间信息/Get live room information via live link | query:live_room_url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_tiktok_web_guest_cookie | 获取游客 Cookie/Get the guest Cookie | query:user_agent | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_trending_post | 获取每日热门内容作品数据/Get daily trending video data | - | - | trend | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_trending_searchwords | 获取每日趋势搜索关键词/Get daily trending search words | - | - | search | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_collect | 获取用户的收藏列表/Get user favorites | query:cookie, query:secUid | query:cursor, query:count, query:coverFormat | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_fans | 获取用户的粉丝列表/Get user followers | query:secUid | query:count, query:maxCursor, query:minCursor | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_follow | 获取用户的关注列表/Get user followings | query:secUid | query:count, query:maxCursor, query:minCursor | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_like | 获取用户的点赞列表/Get user likes | query:secUid | query:cursor, query:count, query:coverFormat, query:post_item_list_request_type | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_live_detail | 获取用户的直播详情/Get user live details | query:uniqueId | - | single_post | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_mix | 获取用户的合辑列表/Get user mix list | query:mixId | query:cursor, query:count | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_play_list | 获取用户的播放列表/Get user play list | query:secUid | query:cursor, query:count | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_post | 获取用户的作品列表/Get user posts | query:secUid | query:cursor, query:count, query:coverFormat, query:post_item_list_request_type | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_profile | 获取用户的个人信息/Get user profile | - | query:uniqueId, query:secUid | author_profile | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/fetch_user_repost | 获取用户的转发作品列表/Get user reposts | query:secUid | query:cursor, query:count, query:coverFormat | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/generate_fingerprint | 生成浏览器指纹/Generate browser fingerprint | - | query:browser_type | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/generate_hashed_id | 生成哈希ID/Generate hashed ID | query:email | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/generate_real_msToken | 生成真实msToken/Generate real msToken | - | query:random_strData, query:browser_type | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/generate_ttwid | 生成ttwid/Generate ttwid | - | query:user_agent | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/generate_webid | 生成web_id/Generate web_id | - | query:cookie, query:user_agent, query:url, query:referer, query:user_unique_id, query:app_id | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/generate_xbogus | 生成 XBogus/Generate XBogus | body:url, body:user_agent | - | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/generate_xgnarly | 生成 XGnarly /Generate XGnarly | body:url, body:user_agent | body:body | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/generate_xgnarly_and_xbogus | 生成 XGnarly 和 XBogus /Generate XGnarly and XBogus | body:url | body:body | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/get_all_aweme_id | 提取列表作品id/Extract list video id | body | - | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/get_all_sec_user_id | 提取列表用户sec_user_id/Extract list user sec_user_id | body | - | other | TikTok-Web-API |
| POST | /api/u1/v1/tiktok/web/get_all_unique_id | 获取列表unique_id/Get list unique_id | body | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/get_aweme_id | 提取单个作品id/Extract single video id | query:url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/get_live_room_id | 根据直播间链接提取直播间ID/Extract live room ID from live room link | query:live_room_url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/get_sec_user_id | 提取用户sec_user_id/Extract user sec_user_id | query:url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/get_unique_id | 获取用户unique_id/Get user unique_id | query:url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/get_user_id | 提取用户user_id/Extract user user_id | query:url | - | other | TikTok-Web-API |
| GET | /api/u1/v1/tiktok/web/tiktok_live_room | 提取直播间弹幕/Extract live room danmaku | query:live_room_url, query:danmaku_type | - | other | TikTok-Web-API |

