<!-- TARGET-PATH: docs/C03-pages/auth/admin/P-auth-004.md -->

# P-auth-004 · 账号与安全

> 路径 `/admin/me` · 守卫:super_admin · 覆盖 R-003/007/008

## 1. 布局

嵌入 admin 主框架 (左侧导航 + 顶栏);右栏内容:
- 卡片 A "基本信息"(只读):邮箱 (脱敏) · 角色 "超级管理员" · 上次登录时间 · 当前活跃设备数
- 卡片 B "修改密码":旧密码 / 新密码 / 重复新密码 / 主按钮 "修改密码"
- 卡片 C "退出登录":两个按钮 "本设备退出" (`outline`) + "所有设备退出登录" (`danger outline`)

## 2. 状态机

| 状态 | UI |
|------|----|
| view | 三卡片只读 + 卡片 B 表单可填 |
| changing-password | 卡片 B 按钮 loading;其他卡片不变 |
| done | Toast 成功后,卡片 B 表单字段清空 + 回到 view |

## 3. 数据流

```
进入 → GET /admin/v1/auth/me (邮箱脱敏 + sessionsCount + lastSignInAt)

改密 → POST /admin/v1/auth/password { old, new, repeat }
       → 校验旧密 → updateUser → revoke 其他 admin refresh
       → 当前 session 保留 + Toast

本设备退出 → POST /admin/v1/auth/session-revoke → cookie/clear → 跳 /admin/auth/login

全部设备退出 → POST /admin/v1/auth/logout-global
            → supabase.auth.admin.signOut(uid, { scope:'global' })
            → cookie/clear → 跳 /admin/auth/login
```

## 4. 错误码

| 错误码 | UI |
|--------|----|
| `AUTH_INVALID_OLD_PASSWORD` | 旧密码下内联 |
| `AUTH_SAME_AS_OLD_PASSWORD` | 新密码下内联 |
| `AUTH_WEAK_PASSWORD` | 新密码下内联 |
| `AUTH_PASSWORD_CHANGE_RATE_LIMITED` | Toast |
| 5xx | Toast |

## 5. i18n key

- `auth.admin.me.title` · `.email_masked` · `.role` · `.last_sign_in` · `.active_sessions`
- `auth.admin.me.change_password` · `.old` · `.new` · `.repeat` · `.submit` · `.success`
- `auth.admin.me.signout_local` · `.signout_global` · `.confirm_global`

## 6. 不允许的操作

- 不显示 "删除账号" 按钮
- 不显示 "修改邮箱" 按钮
- 不显示 "邀请管理员" 按钮
- 不显示 "我的设备列表" (v2)
