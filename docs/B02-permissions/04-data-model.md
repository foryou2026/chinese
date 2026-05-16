<!-- TARGET-PATH: docs/B02-permissions/04-data-model.md -->

# 04 · 数据结构

> **阶段**：B02-P  
> **上游**：`B01-architecture/03-database.md`、`01-roles.md`、`02-auth-flow.md`  
> **下游**：`supabase/migrations/0001_auth_baseline.sql`、所有需要引用 `profiles` 的 D01 D 阶段产物  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 5 张表：`auth.users`（Supabase 内置）+ `public.profiles` + `public.user_sessions` + `public.auth_login_attempts` + `public.audit_logs`。
- 所有 `id` UUID v7（与 `B01-architecture/03-database.md` 一致）；所有时间戳 `timestamptz`。
- 全表强制 RLS；Hono 后端用 service_role 绕 RLS（前置 `authRequired` 校验）。
- 角色字段权威位置 = `auth.users.raw_app_meta_data->>'role'`；`profiles.role` 仅作冗余索引。

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

## 2. `public.profiles`（业务用户档案）

```sql
create table public.profiles (
  id              uuid primary key references auth.users(id) on delete cascade,
  email           text not null,
  role            text not null default 'user' check (role in ('user', 'super_admin')),
                                                  -- 冗余索引；权威值来自 auth.users.raw_app_meta_data
  display_name    text,
  avatar_url      text,
  locale          text not null default 'zh' check (locale in ('zh','en','vi','th','id')),
  is_disabled     boolean not null default false,
  disabled_reason text,
  disabled_at     timestamptz,
  disabled_by     uuid references auth.users(id),
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

create index profiles_email_idx       on public.profiles (email);
create index profiles_role_idx        on public.profiles (role);
create index profiles_is_disabled_idx on public.profiles (is_disabled) where is_disabled = true;
```

### 2.1 自动创建 Trigger

```sql
create function public.handle_new_user()
returns trigger language plpgsql security definer as $$
declare
  inj_role text := coalesce(new.raw_app_meta_data->>'role', 'user');
begin
  insert into public.profiles (id, email, role, display_name, avatar_url, locale)
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
for each row execute function public.handle_new_user();
```

### 2.2 RLS

```sql
alter table public.profiles enable row level security;

create policy profiles_self_read on public.profiles
  for select using (auth.uid() = id);

create policy profiles_self_update on public.profiles
  for update using (auth.uid() = id)
  with check (
    auth.uid() = id
    and is_disabled = (select is_disabled from public.profiles where id = auth.uid())
    and role = (select role from public.profiles where id = auth.uid())
  );
-- 防止用户自改 is_disabled / role
```

> service_role（Hono）绕 RLS。

---

## 3. `public.user_sessions`（多设备会话追踪）

```sql
create table public.user_sessions (
  id                  uuid primary key default gen_random_uuid(),
  user_id             uuid not null references auth.users(id) on delete cascade,
  refresh_token_hash  text not null,     -- sha256(refresh_token) 16 进制，不存明文
  device              text not null,      -- 'web' / 'mobile-web'
  user_agent          text,
  ip                  inet,
  created_at          timestamptz not null default now(),
  last_seen_at        timestamptz not null default now()
);

create index user_sessions_user_idx     on public.user_sessions (user_id, created_at);
create unique index user_sessions_refresh_idx on public.user_sessions (refresh_token_hash);
```

### 3.1 业务规则

- 登录写 + 检查 count > 3 → 撚销最早 1 条（详见 [02-auth-flow §4](./02-auth-flow.md)）；
- 登出删自己那条；过期清理由 cron 每日清 `last_seen_at < now() - interval '40 days'`；
- RLS：

```sql
alter table public.user_sessions enable row level security;
create policy sessions_self_read   on public.user_sessions for select using (auth.uid() = user_id);
create policy sessions_self_delete on public.user_sessions for delete using (auth.uid() = user_id);
```

---

## 4. `public.auth_login_attempts`（登录失败计数）

```sql
create table public.auth_login_attempts (
  id           bigserial primary key,
  email        text not null,
  ip           inet not null,
  succeeded    boolean not null,
  attempted_at timestamptz not null default now()
);

create index login_attempts_email_time_idx on public.auth_login_attempts (email, attempted_at desc);
create index login_attempts_ip_time_idx    on public.auth_login_attempts (ip, attempted_at desc);
```

- 锁定判定：当前 15 min 内 `email + ip` 失败次数 ≥ 5 → 锁到窗口结束；
- cron 每日清 `attempted_at < now() - interval '7 days'`；
- RLS：仅 service_role 可访问。

---

## 5. `public.audit_logs`（管理端关键操作审计）

```sql
create table public.audit_logs (
  id          bigserial primary key,
  actor_id    uuid references auth.users(id),
  actor_role  text not null,           -- 'super_admin' / 'system'
  action      text not null,           -- 'user.disable' / 'auth.signin_success' / ...
  target_type text,                    -- 'user' / 'course' / ...
  target_id   text,
  payload     jsonb,                   -- 变更前后 diff 或参数
  ip          inet,
  user_agent  text,
  created_at  timestamptz not null default now()
);

create index audit_logs_actor_idx  on public.audit_logs (actor_id, created_at desc);
create index audit_logs_target_idx on public.audit_logs (target_type, target_id, created_at desc);
```

**与 B02 相关的最小事件集**：

- `auth.signin_success` / `auth.signin_failed` / `auth.signout`
- `auth.session_kicked`
- `user.disable` / `user.enable`
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
  device: z.enum(['web', 'mobile-web']),
  userAgent: z.string().optional(),
  ip: z.string().optional(),
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
