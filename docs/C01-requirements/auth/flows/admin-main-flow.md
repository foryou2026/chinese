<!-- TARGET-PATH: docs/C01-requirements/admin-auth/flows/main-flow.md -->

# C01 · 主流程 · `admin-auth`

> 4 条主路径 mermaid 图。详细异常分支见 [`exception-flow.md`](./exception-flow.md)。

---

## 1. 邮密登录 (R-001 + R-002 + R-004)

```mermaid
flowchart TD
  Start([/admin/auth/login]) --> Input[输入邮箱+密码]
  Input --> Pre[POST /admin/v1/auth/login-attempt-record]
  Pre -->|locked / disabled| ErrLock[展示锁定/禁用文案]
  Pre -->|ok| Sb[supabase.auth.signInWithPassword]
  Sb -->|invalid| ErrCred[AUTH_INVALID_CREDENTIALS 内联]
  Sb -->|ok| RoleCheck{app_metadata.role==='super_admin'?}
  RoleCheck -->|no| ForceOut[supabase.auth.signOut + Toast AUTH_USE_USER_ENTRY]
  RoleCheck -->|yes| Reg[POST /admin/v1/auth/session-register]
  Reg -->|>3 设备| Kick[Toast 已踢最早设备]
  Reg --> Redirect[跳 redirect 或 /admin]
```

## 2. 忘记密码 → 重置 (R-006)

```mermaid
flowchart TD
  A([/admin/auth/forgot]) --> B[输入邮箱]
  B --> C[POST /admin/v1/auth/forgot-password-throttle]
  C -->|throttled| ErrT[内联节流提示]
  C -->|ok| D[supabase.auth.resetPasswordForEmail]
  D --> E[展示 sent 态]
  E -. 邮件链接 .-> F([/admin/auth/reset-password?token=...])
  F --> G[exchangeCodeForSession]
  G -->|expired/invalid| ErrTok[token-invalid 态]
  G -->|ok| H[updateUser password]
  H --> I[revoke 其他设备 refresh + Toast 成功]
  I --> J[跳 /admin/auth/login]
```

## 3. 改密 (R-007)

```mermaid
flowchart TD
  A([/admin/me]) --> B[输入旧密+新密+重复]
  B --> C[POST /admin/v1/auth/password]
  C -->|old wrong| E1[AUTH_INVALID_OLD_PASSWORD 内联]
  C -->|same as old| E2[AUTH_SAME_AS_OLD_PASSWORD 内联]
  C -->|weak| E3[AUTH_WEAK_PASSWORD 内联]
  C -->|ok| D[updateUser + revoke 其他设备]
  D --> F[Toast 成功 + 留在当前会话]
```

## 4. 退出 (R-008)

```mermaid
flowchart TD
  A[管理员点 顶栏退出 / 全部退出] --> B{scope?}
  B -->|local| L1[POST /admin/v1/auth/session-revoke + cookie/clear]
  B -->|global| G1[POST /admin/v1/auth/logout-global]
  G1 --> G2[supabase.auth.admin.signOut user_id global + revoke 全部 refresh]
  L1 --> End([跳 /admin/auth/login])
  G2 --> End
```
