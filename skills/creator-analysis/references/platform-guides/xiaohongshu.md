# 小红书 Creator 指引

## 作者侧优先资源

- 昵称
- handle
- IP 属地
- 头像
- 粉丝数、累计获赞数、作品数

## 作品侧优先资源

- 作品 ID：`note_id`
- 标题 / 文案：`title` / `desc` / `content`
- 视频作品优先检查原生字幕
- 互动指标：点赞、评论、收藏、分享、播放

## 当前参考实现

- `skills/tikomni-skill/scripts/author_home/adapters/platform_adapters.py`
- `skills/tikomni-skill/scripts/author_home/orchestrator/run_author_analysis.py`
