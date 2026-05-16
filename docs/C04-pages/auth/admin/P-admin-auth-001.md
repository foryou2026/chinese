<!-- TARGET-PATH: docs/C04-pages/auth/admin/P-admin-auth-001.md -->

# P-admin-auth-001 · admin 登录

> surface=`admin` · 路径 `/admin/auth/login` · 公开
> 覆盖 R-001/002/004/005/009

## 1. 角色 & 守卫

- 公开 (已登录 admin 访问 → redirect 到 `/admin` 或 query.redirect)
- 已登录非 admin → 立即 signOut 并停在本页 not-admin 态

## 2. 布局

- 全屏暗色背景 (admin theme dark) + 居中 `<AdminAuthCard width=420>`
- Header:Logo "知语·后台" + tagline "管理后台登录"
- Body:邮箱 input · 密码 input (带 show/hide) · 主按钮 "登录" · 底部 text-button "忘记密码?" → `/admin/auth/forgot`
- 不展示 "注册" / "Google" / "切换到用户端" 任何链接

## 3. 状态机 (SM-01 扩展)

| 状态 | 触发 | UI |
|------|------|----|
| idle | 进入 | 空表单 (若 query.email 自动回填) |
| submitting | 点登录 | 主按钮 loading + 禁用其它输入 |
| error | 后端 4xx | 红字内联在对应字段下;按钮回到可点 |
| not-admin | role 校验失败 | 红字 banner "请使用用户入口登录" + 清空字段 |
| locked | `AUTH_LOGIN_RATE_LIMITED` | 红字 banner "尝试次数过多,请 {n} 分钟后再试" + 按钮禁用 retryAfter 秒 |
| kicked-back | query.kicked=1 | 黄字 banner "您已在其它设备登录,本设备已退出" + 表单可填 |

## 4. 数据流

```
点登录
  → 发起 admin 登录（含节流检查、凭证校验、角色校验==='admin'、会话登记；实现接口在 D02-api/auth/admin/login 定义）
  → 角色校验失败 → 立即登出 + 停在本页 not-admin 态
  → 成功 → navigate(query.redirect || '/admin')
```

## 5. 错误码映射

| 错误码 | UI |
|--------|----|
| `AUTH_INVALID_CREDENTIALS` | 密码字段下红字 |
| `AUTH_EMAIL_NOT_VERIFIED` | (admin seed 必带 confirm,此项理论不会出现);若出现 → 提示联系运维 |
| `AUTH_LOGIN_RATE_LIMITED` | locked 态 |
| `AUTH_ACCOUNT_DISABLED` | banner 红字 + 联系超管文案 |
| `AUTH_USE_USER_ENTRY` | not-admin 态 |
| 5xx | 全局 Toast (B03-06) |

## 6. i18n key

- `auth.admin.login.title` · `.subtitle` · `.email` · `.password` · `.submit` · `.forgot`
- `auth.admin.error.not_admin` · `.locked` · `.kicked_back`
- 5 语全量

## 7. 埋点

无 (analytics feature 暂不支持)

## 8. 验收

- 输 user 角色邮箱 → 立即 signOut + not-admin banner
- 5 次错密 → locked 态显示倒计时
- 第 4 设备登录 → 第一设备 10s 内被踢 + 跳本页 kicked-back 态
