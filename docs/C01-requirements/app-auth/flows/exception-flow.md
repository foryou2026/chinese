<!-- TARGET-PATH: docs/C01-requirements/app-auth/flows/exception-flow.md -->

# `app-auth` · 异常流程

> **阶段**：C01-R · **feature**：`app-auth`  
> **上游**：[`../baseline.md`](../baseline.md) · [`main-flow.md`](./main-flow.md)  
> **冻结状态**：已冻结 · 2026-05-16

---

## 1. 错密锁定（5/15min）

```mermaid
flowchart TD
    A[输入错密] --> B[POST /v1/auth/login-attempt-record]
    B --> C[insert auth_login_attempts succeeded=false]
    C --> D{当前 15min 内 email+ip 失败次数}
    D -->|< 5| E[继续走 signInWithPassword]
    D -->|≥ 5| F[直接 429 AUTH_LOGIN_RATE_LIMITED + 返回锁定到时间戳]
    F --> G[Toast「登录尝试过多，请于 mm:ss 后重试」]
    G --> H[登录按钮 disabled 含倒计时]
```

> 锁定到期自动解锁；管理员可手动清 `auth_login_attempts`（admin-users feature 提供）。

## 2. 第 4 设备登录被踢

```mermaid
flowchart TD
    A[设备 D4 登录成功] --> B[POST /v1/auth/session-register]
    B --> C[count user_sessions where user_id=? > 3]
    C --> D[找出 created_at 最早 session = S1]
    D --> E[supabase.auth.admin.signOut S1.refresh_token]
    E --> F[delete user_sessions where id = S1.id]

    G[设备 S1 当前 access 仍 ≤ 1h 内有效] -->|access 到期前 60s| H[auth.refreshSession 失败]
    H --> I[onAuthStateChange SIGNED_OUT]
    I --> J[clear cookieStorage + 跳 /auth/login?reason=kicked]
    J --> K[Toast「您的账号在其他设备登录，已被退出」]

    L[或 S1 应用启动时] --> M[GET /v1/auth/session-status]
    M -->|valid=false reason=kicked| N[立即走 J]
```

## 3. 账号被禁用

```mermaid
flowchart TD
    A[admin 在 admin-users 点禁用] --> B[update profiles set is_disabled=true ...]
    B --> C[supabase.auth.admin.signOut user, scope='global']
    C --> D[delete user_sessions where user_id=?]
    D --> E[disabledCache.delete user_id]

    F[该用户已登录另一设备] -->|下一次 API 调用| G[authRequired 30s LRU miss → 查 profiles]
    G --> H[is_disabled=true → 401 AUTH_ACCOUNT_DISABLED]
    H --> I[全局登出 + 跳登录页]
    I --> J[Toast 含 disabled_reason + 客服入口 /help/contact]

    K[该用户尝试新登录] --> L[POST /v1/auth/login-attempt-record]
    L --> M[查 profiles is_disabled=true → 直接 401 AUTH_ACCOUNT_DISABLED]
```

## 4. OAuth 失败 / 取消

```mermaid
flowchart TD
    A[/auth/login 点 Google] --> B[supabase.auth.signInWithOAuth redirect Google]
    B --> C{Google 结果}
    C -->|用户拒绝授权| D[静默回 /auth/login，无 Toast]
    C -->|provider_error| E[/auth/callback?error=...]
    E --> F[Toast: AUTH_OAUTH_FAILED + 「重试 / 用邮箱登录」]
    C -->|成功但 admin 端登录页| G[/admin/auth/callback]
    G --> H[role check → 非 super_admin]
    H --> I[signOut + Toast: AUTH_NOT_ADMIN]
```

> **管理端不展示 Google 按钮**，因此分支 G/H/I 主要存在于「app 端账号误用 admin 入口」场景。

## 5. 邮箱验证 / 重置链接过期

```mermaid
flowchart TD
    A[/auth/callback?type=signup&token=...] --> B[exchangeCodeForSession]
    B -->|otp_expired / token_used| C[页面切换至「链接已过期」状态]
    C --> D[展示「重新发送验证邮件」按钮]
    D --> E[POST /v1/auth/register-throttle 复用]
    E --> F[Supabase admin resendEmailConfirmation]

    G[/auth/reset-password?token=...] --> H[exchangeCodeForSession recovery]
    H -->|expired / used| I[页面切换至「token-invalid」状态]
    I --> J[展示「重新发起忘记密码」按钮 → 跳 /auth/forgot]
```

## 6. 网络断 / 5xx

- 任意 auth 接口 5xx 或 fetch 失败 → 顶部 Toast「服务异常，请稍后重试」+ 表单保持已填值；
- supabase-js 内置自动 retry（最多 3 次，指数退避）；3 次后失败正式抛出。

## 7. 守卫拦截（未登录访问受保护页）

```mermaid
flowchart TD
    A[访问 /me /me/profile 等受保护页] --> B[TanStack Router _auth root loader]
    B --> C[assertSession]
    C -->|有 zhiyu-at cookie & 验证通过| D[正常渲染]
    C -->|无 cookie / 过期| E[redirect → /auth/login?redirect=<encoded full-url>]
    E --> F[登录成功后读 redirect 参数跳回]
```

> 详细守卫实现见 [`B02-permissions/03-authz-mechanism §2.1`](../../B02-permissions/03-authz-mechanism.md)。
