<!-- TARGET-PATH: docs/D01-data/app-auth/01-er-diagram.md -->

# `app-auth` · 子 ER 图

```mermaid
erDiagram
    AUTH_USERS ||--|| PROFILES : "1:1 (id = id)"
    AUTH_USERS ||--o{ USER_SESSIONS : "1:N"
    AUTH_USERS ||--o{ AUTH_LOGIN_ATTEMPTS : "1:N (email reference)"
    AUTH_USERS ||--o{ AUDIT_LOGS : "1:N (actor_id)"

    AUTH_USERS {
        uuid id PK
        text email
        text encrypted_password
        timestamptz email_confirmed_at
        timestamptz created_at
    }
    PROFILES {
        uuid id PK,FK
        text display_name
        text avatar_url
        text locale
        text role
        boolean is_disabled
        text disabled_reason
        timestamptz created_at
        timestamptz updated_at
    }
    USER_SESSIONS {
        uuid id PK
        uuid user_id FK
        text refresh_token_hash
        jsonb device_info
        timestamptz last_active_at
        timestamptz created_at
    }
    AUTH_LOGIN_ATTEMPTS {
        bigserial id PK
        text email
        inet ip
        boolean succeeded
        text reason
        timestamptz created_at
    }
    AUDIT_LOGS {
        bigserial id PK
        uuid actor_id
        text action
        jsonb meta
        timestamptz created_at
    }
```

> 完整 DDL 与索引在 [`B02-permissions/04-data-model.md`](../../B02-permissions/04-data-model.md)；本图只截取 `app-auth` 范围内涉及的字段。
