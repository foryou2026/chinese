<!-- TARGET-PATH: docs/C01-requirements/auth/flows/exception-flow.md -->

# C01 · 异常流程 · `auth`

---

## 1. 非 super_admin 角色登录 (R-001/002)

```mermaid
flowchart TD
  A[user 账号 尝试 /admin/auth/login] --> B[signInWithPassword ok]
  B --> C{role==='super_admin'?}
  C -->|no| D[立即 signOut]
  D --> E[Toast AUTH_USE_USER_ENTRY · 红字: 请使用用户入口登录]
  E --> F[clear cookies + 留在登录页 not-admin 态]
```

## 2. 锁定 (R-005)

```mermaid
flowchart TD
  A[连续 5 次密码错误 15min 内] --> B[POST login-attempt-record]
  B --> C[AUTH_LOGIN_RATE_LIMITED with retryAfter]
  C --> D[页面 locked 态 + 显示剩余分钟数]
```

## 3. 禁用账号 (R-005)

```mermaid
flowchart TD
  A[运维 SQL 把 zhiyu.profiles.is_active=false] --> B[管理员尝试登录]
  B --> C[login-attempt-record 查 disabledCache]
  C --> D[AUTH_ACCOUNT_DISABLED]
  D --> E[页面 error 态 + Toast 请联系超级管理员]
```

## 4. 第 4 设备 → 踢最早 (R-004)

```mermaid
flowchart TD
  A[管理员 已在 3 个 admin 设备登录] --> B[第 4 处登录成功]
  B --> C[session-register: SELECT FOR UPDATE SKIP LOCKED]
  C --> D[DELETE oldest user_sessions where surface='admin']
  D --> E[落 audit: admin.session_kicked]
  E -. 被踢端 10s 轮询 .-> F[session-status: 401]
  F --> G[跳 /admin/auth/login?kicked=1]
```

## 5. 重置链接过期 (R-006)

```mermaid
flowchart TD
  A([/admin/auth/reset-password?token=expired]) --> B[exchangeCodeForSession]
  B --> C[AUTH_TOKEN_INVALID]
  C --> D[token-invalid 态: 链接已过期 + 重新申请按钮]
  D --> E[跳 /admin/auth/forgot]
```

## 6. 守卫拦截 (R-009)

```mermaid
flowchart TD
  A[未登录访问 /admin/users] --> B[_admin loader assertSession]
  B --> C[AUTH_NOT_AUTHED]
  C --> D[跳 /admin/auth/login?redirect=%2Fadmin%2Fusers]
  D --> E[登录成功后 redirect 回 /admin/users]
```

## 7. 5xx 兜底

```mermaid
flowchart TD
  A[任意 admin 接口 5xx] --> B[Toast 系统繁忙 · trace_id]
  B --> C[按钮回到可点状态 + 保留输入]
```
