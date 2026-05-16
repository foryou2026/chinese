<!-- TARGET-PATH: docs/C02-permissions/03-data-model.md -->

# 03 · 数据结构

> **阶段**：C02-P  
> **上游**：`B01-architecture/03-database.md`、`01-roles.md`、`02-auth-flow.md`  
> **下游**：`system/supabase/migrations/0002_profiles_sessions_audits.sql`、所有需要引用 `profiles` 的 D01 D 阶段产物  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 5 张表：`auth.users`（Supabase 内置）+ `zhiyu.profiles` + `zhiyu.user_sessions` + `zhiyu.auth_login_attempts` + `zhiyu.audit_logs`。
- 业务 schema = **`zhiyu`**（与 `B01-architecture/03-database.md` 一致）。
- 所有业务表 `id`：profiles/auth.users 引用 `auth.users.id`；user_sessions 用 `uuid_generate_v4()`；其他业务表用 `gen_random_uuid()`。时间戳统一 `timestamptz`。
- `profiles` 与 `user_sessions` 启用 RLS；登录尝试 / 审计日志仅 service_role 可写。Hono 后端用 service_role 绕 RLS（前置 `authRequired` 校验）。
- 角色字段权威位置 = `auth.users.raw_app_meta_data->>'role'`；`profiles.role` 仅作冗余索引。
- **来源对齐**：本文档字段定义与 `system/supabase/migrations/0002_profiles_sessions_audits.sql` 完全一致。

---

## 1. `auth.users`（Supabase Auth 内置，约定）

> 由 Supabase Auth 维护，**严禁**业务侧 INSERT / UPDATE / DELETE；统一走 supabase-js Auth API。

| 字段 | 类型 | 业务约定 |
|------|------|---------|
| `id` | uuid | 主键；其他业务表 `user_id` 全部引用此列 |
| `email` | text | 唯一 |
| `encrypted_password` | text | bcrypt；Google 账号此列为 NULL |
| `email_confirmed_at` | timestamptz | Google 注册自动填；邮箱注册需点验证邮件后填 |
| `raw_app_meta_data` | jsonb | **业务约定**：`{ "role": "user"\|"super_admin", "provider": "email"\|"google" }` |
| `raw_user_meta_data` | jsonb | 用户可改的元数据（display.brand_color 等，由设计系统皮肤使用）|
| `last_sign_in_at` | timestamptz | Supabase 自动维护 |

JWT 中映射：`app_metadata.role` ← `raw_app_meta_data->>'role'`。

---

## 2. `zhiyu.profiles`（业务用户档案）

```sql
create table zhiyu.profiles (
  id                uuid primary key references auth.users(id) on delete cascade,
  email             text not null unique,
  role              text not null default 'user' check (role in ('super_admin','user')),
                                                   -- 冗余索引；权威值来自 auth.users.raw_app_meta_data
  display_name      text,
  avatar_url        text,
  locale            text not null default 'zh' check (locale in ('zh','en','vi','th','id')),
  is_active         boolean not null default true,    -- 账号是否启用；false = 已停用
  email_verified_at timestamptz,
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now()
);

create index profiles_role_idx on zhiyu.profiles (role);
```

> **关于"禁用"语义**：v1 schema 仅一个布尔位 `is_active`，无 `disabled_reason / disabled_at / disabled_by` 列。审计原因记录于 `zhiyu.audit_logs.meta` jsonb（`event='user.disable'`），错误码继续使用 `AUTH_ACCOUNT_DISABLED`（语义不变）。若后续要在用户端展示禁用原因，再加 migration 扩列。

### 2.1 自动创建 Trigger

```sql
create or replace function zhiyu.handle_new_user()
returns trigger language plpgsql security definer as $$
declare
  inj_role text := coalesce(new.raw_app_meta_data->>'role', 'user');
begin
  insert into zhiyu.profiles (id, email, role, display_name, avatar_url, locale)
  values (
    new.id,
    new.email,
    inj_role,
    coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)),
    new.raw_user_meta_data->>'avatar_url',
    coalesce(new.raw_user_meta_data->>'locale', 'zh')
  );

  -- 兜底注入 role + provider（GoTrue hook 已注入则跳过）
  if new.raw_app_meta_data->>'role' is null then
    update auth.users
    set raw_app_meta_data = coalesce(raw_app_meta_data, '{}'::jsonb)
      || jsonb_build_object('role', 'user',
                            'provider', coalesce(raw_app_meta_data->>'provider', 'email'))
    where id = new.id;
  end if;

  return new;
end $$;

create trigger on_auth_user_created
after insert on auth.users
for each row execute function zhiyu.handle_new_user();
```

### 2.2 RLS

```sql
alter table zhiyu.profiles enable row level security;

create policy profiles_self_read on zhiyu.profiles
  for select using (id = auth.uid());

create policy profiles_self_update on zhiyu.profiles
  for update using (id = auth.uid());
-- 业务层（Hono）禁止用户自改 is_active / role / email；service_role 绕 RLS 执行管理动作。
```

> service_role（Hono）绕 RLS。

---

## 3. `zhiyu.user_sessions`（多设备会话追踪）

```sql
create table zhiyu.user_sessions (
  id            uuid primary key default uuid_generate_v4(),
  user_id       uuid not null references auth.users(id) on delete cascade,
  device_id     text not null,                 -- 前端 fingerprint（UA+screen hash）
  device_name   text,                          -- 友好名，如 "Chrome on macOS"
  user_agent    text,
  ip            text,
  refresh_jti   text,                          -- 当前 refresh token 的 jti 声明
  last_seen_at  timestamptz not null default now(),
  created_at    timestamptz not null default now(),
  unique (user_id, device_id)
);

create index user_sessions_user_idx on zhiyu.user_sessions (user_id, last_seen_at desc);
```

### 3.1 业务规则

- 登录写：以 `(user_id, device_id)` upsert（同一设备复登 → 更新 `refresh_jti / last_seen_at`，不挤占额度）；
- 多设备硬上限 3：upsert 后 `select count(*) from zhiyu.user_sessions where user_id=?` > 3 → 取 `last_seen_at` 最早行做撚销 + delete（详见 [02-auth-flow §4](./02-authz-mechanism.md)）；
- 登出删自己那条；过期清理由 cron 每日清 `last_seen_at < now() - interval '40 days'`；
- RLS：

```sql
alter table zhiyu.user_sessions enable row level security;
create policy user_sessions_self_read on zhiyu.user_sessions
  for select using (user_id = auth.uid());
-- 删除走 service_role；不开 user delete policy。
```

---

## 4. `zhiyu.auth_login_attempts`（登录失败计数）

```sql
create table zhiyu.auth_login_attempts (
  id          bigserial primary key,
  email       text not null,
  ip          text,
  user_agent  text,
  success     boolean not null,
  reason      text,                            -- 失败原因码（如 'invalid_password' / 'account_disabled'）
  created_at  timestamptz not null default now()
);

create index auth_login_attempts_email_time_idx on zhiyu.auth_login_attempts (email, created_at desc);
```

- 锁定判定：当前 15 min 内 `email + ip` 命中 `success=false` 次数 ≥ 5 → 锁到窗口结束；
- cron 每日清 `created_at < now() - interval '7 days'`；
- RLS：未启用，仅 service_role 可访问（不暴露给 anon / authenticated）。

---

## 5. `zhiyu.audit_logs`（管理端关键操作审计）

```sql
create table zhiyu.audit_logs (
  id          bigserial primary key,
  actor_id    uuid,                            -- nullable：系统事件可空
  actor_role  text,                            -- 'super_admin' / 'user' / 'system'
  event       text not null,                   -- 'user.disable' / 'auth.signin_success' / ...
  target_type text,                            -- 'user' / 'course' / ...
  target_id   text,
  meta        jsonb,                           -- 变更前后 diff、原因（如 { reason: '违规' }）等
  ip          text,
  created_at  timestamptz not null default now()
);

create index audit_logs_event_time_idx on zhiyu.audit_logs (event, created_at desc);
```

**与 B02 相关的最小事件集**（写入 `event` 列）：

- `auth.signin_success` / `auth.signin_failed` / `auth.signout`
- `auth.session_kicked`
- `user.disable` / `user.enable`（`meta` 记 `{ reason, disabled_by }`）
- `user.password_reset`
- `super_admin.self_delete_blocked`
- `super_admin.self_disable_blocked`

---

## 6. TypeScript 类型（前后端共用）

`system/packages/shared-schemas/src/auth.ts`：

```ts
import { z } from 'zod';

export const ROLES = ['user', 'super_admin'] as const;
export type Role = (typeof ROLES)[number];

export const AuthUserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  role: z.enum(ROLES),
  avatarUrl: z.string().url().optional(),
  displayName: z.string().optional(),
  locale: z.enum(['zh', 'en', 'vi', 'th', 'id']),
});
export type AuthUser = z.infer<typeof AuthUserSchema>;

export const UserSessionSchema = z.object({
  id: z.string().uuid(),
  userId: z.string().uuid(),
  deviceId: z.string(),
  deviceName: z.string().optional(),
  userAgent: z.string().optional(),
  ip: z.string().optional(),
  refreshJti: z.string().optional(),
  createdAt: z.string(),
  lastSeenAt: z.string(),
  isCurrent: z.boolean().optional(),
});
export type UserSession = z.infer<typeof UserSessionSchema>;

export const AUTH_ERROR_CODES = [
  'AUTH_TOKEN_MISSING', 'AUTH_TOKEN_INVALID', 'AUTH_TOKEN_EXPIRED',
  'AUTH_INVALID_CREDENTIALS', 'AUTH_EMAIL_NOT_VERIFIED',
  'AUTH_EMAIL_TAKEN', 'AUTH_WEAK_PASSWORD', 'AUTH_ACCOUNT_DISABLED',
  'AUTH_NOT_ADMIN', 'AUTH_FORBIDDEN', 'AUTH_OAUTH_FAILED',
  'AUTH_RESET_TOKEN_INVALID', 'AUTH_LOGIN_RATE_LIMITED',
  'AUTH_FORGOT_RATE_LIMITED', 'AUTH_REGISTER_RATE_LIMITED',
  'AUTH_SESSION_KICKED', 'AUTH_SUPER_ADMIN_SELF_DELETE',
  'AUTH_CSRF_INVALID', 'AUTH_EMAIL_BLOCKED', 'AUTH_IP_BLOCKED',
  'AUTH_INVITE_INVALID',
] as const;
export type AuthErrorCode = (typeof AUTH_ERROR_CODES)[number];
```

---

## 99. 待确认问题
（无）
