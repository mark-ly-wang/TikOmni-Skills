# youtube API Catalog

- operation_count: 21

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/youtube/web/get_channel_description | 获取频道描述信息/Get channel description | - | query:channel_id, query:continuation_token, query:language_code, query:country_code, query:need_format | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_id | 获取频道ID/Get channel ID | query:channel_name | - | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_id_v2 | 从频道URL获取频道ID V2/Get channel ID from URL V2 | query:channel_url | - | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_info | 获取频道信息/Get channel information | query:channel_id | - | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_short_videos | 获取频道短视频/Get channel short videos | query:channel_id | query:continuation_token | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_url | 从频道ID获取频道URL/Get channel URL from channel ID | query:channel_id | - | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_videos | 获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first) | query:channel_id | query:continuation_token | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_videos_v2 | 获取频道视频 V2/Get channel videos V2 | query:channel_id | query:lang, query:sortBy, query:contentType, query:nextToken | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_channel_videos_v3 | 获取频道视频 V3/Get channel videos V3 | query:channel_id | query:language_code, query:country_code, query:continuation_token, query:need_format | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_general_search | 综合搜索（支持过滤条件）/General search with filters | query:search_query | query:language_code, query:country_code, query:time_zone, query:upload_time, query:duration, query:content_type, query:feature, query:sort_by, ...(+1) | search | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_relate_video | 获取推荐视频/Get related videos | query:video_id | query:continuation_token | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_shorts_search | YouTube Shorts短视频搜索/YouTube Shorts search | query:search_query | query:language_code, query:country_code, query:time_zone, query:upload_time, query:sort_by, query:continuation_token, query:filter_mixed_content | search | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_trending_videos | 获取趋势视频/Get trending videos | - | query:language_code, query:country_code, query:section | trend | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_comment_replies | 获取视频二级评论/Get video sub comments | query:continuation_token | query:language_code, query:country_code, query:need_format | comments | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_comments | 获取视频评论/Get video comments | query:video_id | query:language_code, query:country_code, query:sort_by, query:continuation_token, query:need_format | comments | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_info | 获取视频信息 V1/Get video information V1 | query:video_id | query:url_access, query:lang, query:videos, query:audios, query:subtitles, query:related | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_info_v2 | 获取视频信息 V2/Get video information V2 | query:video_id | - | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_info_v3 | 获取视频详情 V3/Get video information V3 | query:video_id | query:language_code | other | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/get_video_subtitles | 获取视频字幕/Get video subtitles | query:subtitle_url | query:format, query:fix_overlap, query:target_lang | asr_transcription | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/search_channel | 搜索频道/Search channel | query:channel_id, query:search_query | query:language_code, query:country_code, query:continuation_token | search | YouTube-Web-API |
| GET | /api/u1/v1/youtube/web/search_video | 搜索视频/Search video | query:search_query | query:language_code, query:order_by, query:country_code, query:continuation_token | search | YouTube-Web-API |

