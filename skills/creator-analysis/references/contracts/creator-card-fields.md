# Creator Card Fields

## Fixed Display Fields

- `platform`
- `platform_author_id`
- `author_handle`
- `nickname`
- `ip_location`
- `signature`
- `avatar_url`
- `fans_count`
- `liked_count`
- `collected_count`
- `works_count`
- `verified`
- `snapshot_at`

## Key Rules

- The creator card is the fact container for creator-level data.
- The creator-level analysis body comes from `author_analysis_v2`, not from platform process fields.
- Platform-native IDs stay in the internal reference layer and should not appear in the final creator-card body.
