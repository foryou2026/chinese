<!-- TARGET-PATH: docs/D01-data/app-auth/04-validations.md -->

# `app-auth` · 校验清单

> 三层校验：UI (`zod` 同步) → API (`zod` 同步 + DB) → DB (CHECK / UNIQUE / FK / RLS)

| 字段 | UI zod | API zod | DB 约束 |
|------|--------|---------|---------|
| `email` | `z.string().email()` | 同 + `.toLowerCase()` 规范化 | `auth.users.email` UNIQUE |
| `password` (注册 / 改密) | `z.string().min(8).regex(/[A-Za-z]/).regex(/\d/)` | 同 | bcrypt cost=10 |
| `display_name` | `z.string().min(1).max(32)` | 同 | `text NOT NULL` |
| `avatar_url` | `z.union([z.string().url(), z.literal('')])` | 同 | `text NULL` |
| `locale` | `z.enum(['zh','en','vi','th','id'])` | 同 | `CHECK (locale IN (...))` |
| `confirm_password` | `eq(new_password)` | — | — |
| `old_password` (改密) | `z.string().min(8)` | 同；后端 signInWithPassword 验证 | — |

错误码与 [B02-permissions §3-authz-mechanism §4](../../B02-permissions/03-authz-mechanism.md) 全局错误码表对齐。
