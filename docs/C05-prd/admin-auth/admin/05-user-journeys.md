<!-- TARGET-PATH: docs/C05-prd/admin-auth/admin/05-user-journeys.md -->

# C05 · 05 用户旅程 · `admin-auth`

## J1 · 新管理员首次登录

```
运维 seed (R-010)
  → 超管收到邮件 + 临时密码 (邮件由运维侧人工发送)
  → 打开 /admin/auth/login
  → 输入邮箱+临时密码 → 进 /admin
  → (建议) 立即 /admin/me 改密
```

## J2 · 日常登录 + 改密

```
/admin/auth/login → 输错 → 再试 → 成功
  → /admin (Dashboard)
  → /admin/me 改密 (旧+新+重复)
  → 其它设备瞬间失效
  → 当前会话保留
```

## J3 · 忘记密码

```
/admin/auth/login → 点 "忘记密码?"
  → /admin/auth/forgot 输邮箱 → sent 态
  → 邮件链接 → /admin/auth/reset-password?token=...
  → exchanging → idle → 输新密 → success
  → /admin/auth/login?email=<masked>
```

## J4 · 攻击拦截

```
攻击者用 dictionary 密 5 次错 → locked 态 (15min)
攻击者尝试 user 角色登录 admin → not-admin 态 + signOut
攻击者盗到旧密 → 真主改密后 → 攻击者 401 (refresh revoked)
```

## J5 · 多设备踢

```
超管 在 Mac/Win/手机 已 3 登录 → 在新平板登录 ok
  → user_sessions 删 Mac 那条 (最早)
  → Mac 端 10s 内 session-status 401 → 跳 /admin/auth/login?kicked=1 (kicked-back 态)
```
