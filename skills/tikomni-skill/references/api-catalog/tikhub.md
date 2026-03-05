# tikhub API Catalog

- operation_count: 8

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/tikhub/downloader/redirect_download | 重定向到最新版本的下载链接 / Redirect to the latest version download link | header:authorization | - | other | TikHub-Downloader-API |
| GET | /api/u1/v1/tikhub/downloader/version | 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates | header:authorization | - | other | TikHub-Downloader-API |
| GET | /api/u1/v1/tikhub/user/calculate_price | 计算价格/Calculate price | header:authorization, query:endpoint | query:request_per_day | other | TikHub-User-API |
| GET | /api/u1/v1/tikhub/user/get_all_endpoints_info | 获取所有端点信息/Get all endpoints information | header:authorization | - | other | TikHub-User-API |
| GET | /api/u1/v1/tikhub/user/get_endpoint_info | 获取一个端点的信息/Get information of an endpoint | header:authorization, query:endpoint | - | other | TikHub-User-API |
| GET | /api/u1/v1/tikhub/user/get_tiered_discount_info | 获取阶梯式折扣百分比信息/Get tiered discount percentage information | header:authorization | - | other | TikHub-User-API |
| GET | /api/u1/v1/tikhub/user/get_user_daily_usage | 获取用户每日使用情况/Get user daily usage | header:authorization | - | other | TikHub-User-API |
| GET | /api/u1/v1/tikhub/user/get_user_info | 获取TikHub用户信息/Get TikHub user info | header:authorization | - | author_profile | TikHub-User-API |

