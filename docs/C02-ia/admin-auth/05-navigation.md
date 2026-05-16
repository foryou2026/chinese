<!-- TARGET-PATH: docs/C02-ia/admin-auth/05-navigation.md -->

# C02 · 导航 · `admin-auth`

## 1. 顶栏 (admin 主框架右上)

| 元素 | 行为 |
|------|------|
| Logo "知语·后台" | 点击 → `/admin` (Dashboard) |
| 语言切换 | 5 语;不要求登录态 |
| 头像 (initial) | 点击展开下拉 |

## 2. 头像下拉 (仅 2 项)

| 序 | 项 | 跳转 |
|---|----|------|
| 1 | 账号与安全 | `/admin/me` |
| 2 | 退出登录 | 调 `POST /admin/v1/auth/session-revoke` 后跳 `/admin/auth/login` |

> 不展示「邀请管理员」「我的设备」「订单」等;admin 端账号面板**极简**。

## 3. 路由树 (新增段)

```
/admin/auth/login                   公开
/admin/auth/forgot                  公开
/admin/auth/reset-password          公开
/admin/me                           super_admin
/admin/*                            super_admin (其它业务路径)
```
