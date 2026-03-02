# temp_mail API Catalog

- operation_count: 3

| Method | Path | Summary | Required Params | Optional Params | Suggested Intent | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/u1/v1/temp_mail/v1/get_email_by_id | Get Email By Id | header:authorization, query:token, query:message_id | - | other | Temp-Mail-API |
| GET | /api/u1/v1/temp_mail/v1/get_emails_inbox | Get Emails | header:authorization, query:token | - | other | Temp-Mail-API |
| GET | /api/u1/v1/temp_mail/v1/get_temp_email_address | Get Temp Email | header:authorization | - | other | Temp-Mail-API |

