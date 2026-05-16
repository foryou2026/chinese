<!-- TARGET-PATH: docs/C03-pages/app-auth/app/P-app-app-auth-008.md -->

# `P-app-app-auth-008` · 账号与安全

> **path**：`/me/security` · **角色可见**：用户  
> **R 覆盖**：R-009 / R-010  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

`<PageHeader title="账号与安全" backTo="/me" />` + 内容区两张 `<GlassCard>`：「修改密码」+ 「退出登录」。

## 2. 修改密码卡片

### 2.1 DOM

```
GlassCard
  ├─ h2 「修改密码」
  ├─ form
  │    ├─ field old_password
  │    ├─ field new_password (强度条)
  │    ├─ field confirm_password
  │    └─ button.primary [保存新密码]
  └─ p.muted 「修改成功后，其他设备会被强制退出；本设备保持登录。」
```

### 2.2 字段

| key | zod |
|-----|-----|
| old_password | `min(8)` |
| new_password | `min(8).regex(/[A-Za-z]/).regex(/\d/)`，且 `!= old_password` |
| confirm_password | `eq(new_password)` |

### 2.3 流程

```
1. submit → POST /v1/me/password { old, new }
2. 后端：
   - signInWithPassword(email, old) 验证旧密
   - admin.updateUserById(id, { password:new })
   - admin.signOut(user_id, { scope:'others' })
   - delete from user_sessions where user_id=? and id<>current_session_id
3. 成功 → Toast「密码已修改」+ form reset
4. 失败：
   - 401 invalid_old_password → old 字段下「旧密码不正确」
   - 400 weak_password → new 字段下「强度不足」
   - 400 same_as_old → new 字段下「不能与旧密码相同」
   - 5xx → Toast
```

## 3. 退出登录卡片

### 3.1 DOM

```
GlassCard
  ├─ h2 「退出登录」
  ├─ p  「需要更进一步？可以退出所有设备的登录会话。」
  ├─ button.secondary [本设备退出]
  └─ button.danger    [全部设备退出]
```

### 3.2 流程

- 本设备退出：
  1. `supabase.auth.signOut({ scope:'local' })`
  2. cookieStorage 内自动 `POST /v1/auth/cookie/clear`
  3. `POST /v1/auth/session-revoke { sessionId }` 删 user_sessions 行
  4. 跳 `/auth/login?reason=signout`
- 全部设备退出：
  1. **二次确认弹窗** `<Confirm>` 标题「全部设备退出？」+ danger 按钮「确认退出全部」；
  2. `POST /v1/auth/logout-global` → 后端 `admin.signOut(user_id, { scope:'global' })` + `delete from user_sessions where user_id=?`；
  3. cookieStorage clear；
  4. 跳 `/auth/login?reason=signout`。

## 4. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 改密成功 | Toast + 其他设备下次 refresh 后登出 |
| S2 | 旧密码错 | old 字段下内联 |
| S3 | 弱新密码 | new 字段下内联 |
| S4 | 新旧密码一致 | new 字段下内联 |
| S5 | 本设备退出 | 跳 login，无 Toast |
| S6 | 全部退出（确认）| 全设备 401 + 跳 login |
| S7 | 全部退出（取消）| 弹窗关闭，无动作 |
