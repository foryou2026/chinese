<!-- TARGET-PATH: docs/C02-permissions/03-data-model.md -->

# 03 · 数据结构

> **阶段**：C02-P  
> **上游**：`B01-architecture/03-database.md`、`01-roles.md`、`02-auth-flow.md`  
> **下游**：`system/鉴权与数据底座/migrations/0002_profiles_sessions_audits.sql`、所有需要引用 用户档案 的 D01 D 阶段产物  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 5 张表：用户账号（鉴权与数据底座 内置）+ 用户档案 + `zhiyu.会话记录 + `zhiyu.登录尝试记录 + `zhiyu.审计记录。
- 业务 schema = **`zhiyu`**（与 `B01-architecture/03-database.md` 一致）。
- 所有业务表 `id`：profiles/用户账号 引用 用户账号`；会话记录 用 `uuid_generate_v4()`；其他业务表用 `gen_random_uuid()`。时间戳统一 `timestamptz`。
- 用户档案 与 会话记录 启用 RLS；登录尝试 / 审计日志仅 service_role 可写。Hono 后端用 service_role 绕 RLS（前置 `authRequired` 校验）。
- 角色字段权威位置 = 用户账号->>'role'`；用户角色字段` 仅作冗余索引。
- **来源对齐**：本文档字段定义与 `system/鉴权与数据底座/migrations/0002_profiles_sessions_audits.sql` 完全一致。

---

## 1. 用户账号（鉴权服务 内置，约定）

> 由 鉴权服务 维护，**严禁**业务侧 INSERT / UPDATE / DELETE；统一走 鉴权与数据底座-js Auth API。

| 字段 | 类型 | 业务约定 |
|------|------|---------|
| `id` | uuid | 主键；其他业务表 `user_id` 全部引用此列 |
| `email` | text | 唯一 |
| `encrypted_password` | text | bcrypt；Google 账号此列为 NULL |
| 邮箱验证时间 | timestamptz | Google 注册自动填；邮箱注册需点验证邮件后填 |
| `raw_app_meta_data` | jsonb | **业务约定**：`{ "role": "user"\|"admin", "provider": "email"\|"google" }` |
| `raw_user_meta_data` | jsonb | 用户可改的元数据（display.brand_color 等，由设计系统皮肤使用）|
| `last_sign_in_at` | timestamptz | 鉴权与数据底座 自动维护 |

JWT 中映射：账号元数据.role` ← `raw_app_meta_data->>'role'`。

---

## 2. 用户档案（业务用户档案）

```sql
create table 用户档案 (
  id                uuid primary key references 用户账号(id) on delete cascade,
  email             text not null unique,
  role              text not null default 'user' check (role in ('admin','user')),
                                                   -- 冗余索引；权威值来自 用户账号
  display_name      text,
  avatar_url        text,
  locale            text not null default 'zh' check (locale in ('zh','en','vi','th','id')),
  启用态         boolean not null default true,    -- 账号是否启用；false = 已停用
  email_verified_at timestamptz,
  created_at        timestamptz not null default now(),
  更新时间        timestamptz not null default now()
);

create index profiles_role_idx on 用户档案 (role);
```

> **关于"禁用"语义**：首版 schema 仅一个布尔位 启用态，无 `disabled_reason / disabled_at / disabled_by` 列。审计原因记录于 `zhiyu.审计记录.meta` jsonb（`event='user.disable'`），错误码继续使用 `AUTH_ACCOUNT_DISABLED`（语义不变）。若后续要在用户端展示禁用原因，再加 migration 扩列。

### 2.1 自动创建 Trigger

```sql
create or replace function zhiyu.handle_new_user()
returns trigger language plpgsql security definer as $$
declare
  inj_role text := coalesce(new.raw_app_meta_data->>'role', 'user');
begin
  insert into 用户档案 (id, email, role, display_name, avatar_url, locale)
  values (
    new.id,
    new.email,
    inj_role,
    coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)),
    new.raw_user_meta_data->>'avatar_url',
    coalesce(new.raw_user_meta_data->>'locale', 'zh')
  );

  -- 兜底注入 role + provider（鉴权服务 hook 已注入则跳过）
  if new.raw_app_meta_data->>'role' is null then
    update 用户账号
    set raw_app_meta_data = coalesce(raw_app_meta_data, '{}'::jsonb)
      || jsonb_build_object('role', 'user',
                            'provider', coalesce(raw_app_meta_data->>'provider', 'email'))
    where id = new.id;
  end if;

  return new;
end $$;

create trigger on_auth_user_created
after insert on 用户账号
for each row execute function zhiyu.handle_new_user();
```

### 2.2 RLS

```sql
alter table 用户档案 enable row level security;

create policy profiles_self_read on 用户档案
  for select using (id = auth.uid());

create policy profiles_self_update on 用户档案
  for update using (id = auth.uid());
-- 业务层（Hono）禁止用户自改 启用态 / role / email；service_role 绕 RLS 执行管理动作。
```

> service_role（Hono）绕 RLS。

---

## 3. `zhiyu.会话记录（多设备会话追踪）

```sql
create table zhiyu.会话记录 (
  id            uuid primary key default uuid_generate_v4(),
  user_id       uuid not null references 用户账号(id) on delete cascade,
  device_id     text not null,                 -- 前端 fingerprint（UA+screen hash）
  device_name   text,                          -- 友好名，如 "Chrome on macOS"
  user_agent    text,
  ip            text,
  refresh_jti   text,                          -- 当前 refresh token 的 jti 声明
  last_seen_at  timestamptz not null default now(),
  created_at    timestamptz not null default now(),
  unique (user_id, device_id)
);

create index 会话记录_user_idx on zhiyu.会话记录 (user_id, last_seen_at desc);
```

### 3.1 业务规则

- 登录写：以 `(user_id, device_id)` upsert（同一设备复登 → 更新 `refresh_jti / last_seen_at`，不挤占额度）；
- 多设备硬上限 3：upsert 后 `select count(*) from zhiyu.会话记录 where user_id=?` > 3 → 取 `last_seen_at` 最早行做撚销 + delete（详见 [02-auth-flow §4](./02-authz-mechanism.md)）；
- 登出删自己那条；过期清理由 cron 每日清 `last_seen_at < now() - interval '40 days'`；
- RLS：

```sql
alter table zhiyu.会话记录 enable row level security;
create policy 会话记录_self_read on zhiyu.会话记录
  for select using (user_id = auth.uid());
-- 删除走 service_role；不开 user delete policy。
```

---

## 4. `zhiyu.登录尝试记录（登录失败计数）

```sql
create table zhiyu.登录尝试记录 (
  id          bigserial primary key,
  email       text not null,
  ip          text,
  user_agent  text,
  success     boolean not null,
  reason      text,                            -- 失败原因码（如 'invalid_password' / 'account_disabled'）
  created_at  timestamptz not null default now()
);

create index 登录尝试记录_email_time_idx on zhiyu.登录尝试记录 (email, created_at desc);
```

- 锁定判定：当前 15 min 内 `email + ip` 命中 `success=false` 次数 ≥ 5 → 锁到窗口结束；
- cron 每日清 `created_at < now() - interval '7 days'`；
- RLS：未启用，仅 service_role 可访问（不暴露给 anon / authenticated）。

---

## 5. `zhiyu.审计记录（管理端关键操作审计）

```sql
create table zhiyu.审计记录 (
  id          bigserial primary key,
  actor_id    uuid,                            -- nullable：系统事件可空
  actor_role  text,                            -- 'admin' / 'user' / 'system'
  event       text not null,                   -- 'user.disable' / 'auth.signin_success' / ...
  target_type text,                            -- 'user' / 'course' / ...
  target_id   text,
  meta        jsonb,                           -- 变更前后 diff、原因（如 { reason: '违规' }）等
  ip          text,
  created_at  timestamptz not null default now()
);

create index 审计记录_event_time_idx on zhiyu.审计记录 (event, created_at desc);
```

**与 B02 相关的最小事件集**（写入 `event` 列）：

- `auth.signin_success` / `auth.signin_failed` / `auth.signout`
- `auth.session_kicked`
- `user.disable` / `user.enable`（`meta` 记 `{ reason, disabled_by }`）
- `user.password_reset`
- `admin.self_delete_blocked`
- `admin.self_disable_blocked`

---

## 6. TypeScript 类型（前后端共用）

`system/packages/shared-schemas/src/auth.ts`：

```ts
import { z } from 'zod';

export const ROLES = ['user', 'admin'] as const;
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
