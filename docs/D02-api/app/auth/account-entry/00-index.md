# 接口规范 · account-entry · 总览

> **系统**：app
> **关联 R-ID**：R-auth-001~016
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **特殊说明**：Token 刷新由前端 `supabase-js` 自动处理(B01-09)，不经后端；Google OAuth 弹窗由前端 `supabase.auth.signInWithOAuth()` 发起，成功后调后端同步接口。
> **共用接口**：见 docs/D02-api/common/auth/account-entry/
> **专属接口详情**：01-register.md ~ 04-session.md

---

## 1. 路由表

### 1.1 page-id → URL 映射

| page-id | 页面名称 | URL | 鉴权 | 可见角色 |
|---------|---------|-----|------|---------|
| P-app-auth-001 | 登录页 | /login | 公开 | 全部 |
| P-app-auth-002 | 注册页 | /register | 公开 | 全部 |
| P-app-auth-003 | 忘记密码页 | /forgot-password | 公开 | 全部 |
| P-app-auth-004 | 重置密码页 | /reset-password | 公开(需验证码token) | 全部 |
| P-app-auth-005 | 修改/设置密码页 | /settings/password | Bearer JWT | ROLE-USER |
| P-app-auth-006 | 设置页 | /settings | Bearer JWT | ROLE-USER |

---

## 2. 共用接口引用

> 以下接口定义在 common/，本系统复用，路径前缀为 `/api/v1/app/`

| API-ID | 方法 | 路径(本系统) | 职责 |
|--------|------|-------------|------|
| API-common-auth-forgot-password | POST | /api/v1/app/auth/forgot-password | 发送重置验证码 |
| API-common-auth-verify-reset-otp | POST | /api/v1/app/auth/forgot-password/verify | 验证重置OTP |
| API-common-auth-reset-password | POST | /api/v1/app/auth/reset-password | 重置密码 |
| API-common-auth-logout | POST | /api/v1/app/auth/logout | 退出登录 |

---

## 3. 系统专属接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 角色 | R-ID | SM 转移 | 详情 |
|--------|------|------|------------|------|------|--------|------|
| API-app-auth-register | POST | /api/v1/app/auth/register | 邮箱注册+发OTP | 公开 | R-auth-001,010,011,015 | TR-004 | 01 |
| API-app-auth-verify-register | POST | /api/v1/app/auth/register/verify | 验证注册OTP | 公开 | R-auth-001,015 | TR-004→已登录 | 01 |
| API-app-auth-login | POST | /api/v1/app/auth/login | 邮箱密码登录 | 公开 | R-auth-002,004,016 | TR-001,003,007 | 02 |
| API-app-auth-google-sync | POST | /api/v1/app/auth/google/sync | Google登录后同步 | Bearer JWT | R-auth-003,012,016 | TR-005,006 | 02 |
| API-app-auth-change-password | PUT | /api/v1/app/auth/password | 修改/设置密码 | Bearer JWT | R-auth-007,010,014 | 无 | 03 |
| API-app-auth-me | GET | /api/v1/app/auth/me | 获取当前用户信息 | Bearer JWT | R-auth-014 | 无 | 04 |

---

## 4. 错误码汇总（含共用+专属）

| code | HTTP | 含义 | 文案 | 触发接口 | 来源 |
|------|------|------|------|---------|------|
| 40001 | 400 | 参数校验失败 | 请检查输入内容 | register, login, forgot-password, reset-password, change-password | common+专属 |
| 40002 | 400 | 新密码与旧密码相同 | 新密码不能与旧密码相同 | change-password | 专属 |
| 40101 | 401 | 认证失败 | 邮箱或密码错误 | login, me, logout, change-password, google-sync, reset-password | common+专属 |
| 40102 | 401 | 验证码过期 | 验证码已过期，请重新发送 | verify-register, verify-reset-otp | common+专属 |
| 40103 | 401 | 验证码错误 | 验证码错误 | verify-register, verify-reset-otp | common+专属 |
| 40104 | 401 | 旧密码错误 | 旧密码错误 | change-password | 专属 |
| 40901 | 409 | 资源冲突 | 该邮箱已注册 | register | 专属 |
| 42901 | 429 | 请求限流 | 请求过于频繁/账号已锁定 | login, forgot-password | common+专属 |
| 50301 | 503 | 第三方异常 | 服务暂不可用 | register, login | 专属 |

---

## 5. 并发与幂等

| API-ID | 并发场景 | 策略 | 失败处理 |
|--------|---------|------|---------|
| API-app-auth-login | 同一邮箱并发登录 | login_attempts 行级锁(SELECT FOR UPDATE) | 重试 |
| API-app-auth-google-sync | 同一用户并发调用 | user_profiles UPSERT(ON CONFLICT DO NOTHING) | 幂等 |

---

## 6. 事件/Webhook

无

---

## 7. 增量融合报告

### 7.1 本轮变更
重构：将 forgot-password、verify-reset-otp、reset-password、logout 提取为共用接口(common/)。专属保留 6 个接口。

---

## 8. 自检报告

> 共用+专属合并自检。

**R-ID 覆盖**

| R-ID | 承接 API-ID | 来源 |
|------|------------|------|
| R-auth-001 邮箱注册 | register + verify-register | 专属 |
| R-auth-002 邮箱登录 | login | 专属 |
| R-auth-003 Google登录 | google-sync (OAuth由前端supabase-js驱动) | 专属 |
| R-auth-004 登录限流 | login (BR-002/BR-002a) | 专属 |
| R-auth-005 忘记密码 | common-forgot-password + common-verify-reset-otp | common |
| R-auth-006 重置密码 | common-reset-password | common |
| R-auth-007 修改密码 | change-password | 专属 |
| R-auth-008 退出登录 | common-logout | common |
| R-auth-009 Token过期 | 前端supabase-js自动刷新(B01-09) | — |
| R-auth-010 密码强度 | register, common-reset-password, change-password | common+专属 |
| R-auth-011 邮箱格式 | 各接口 email 字段校验 | — |
| R-auth-012 Google自动注册 | google-sync | 专属 |
| R-auth-013 登录注册切换 | 前端路由 | — |
| R-auth-014 Google密码管理 | change-password + me | 专属 |
| R-auth-015 注册验证码 | register + verify-register | 专属 |
| R-auth-016 多设备限制 | login + google-sync | 专属 |

- [x] 每条 R-ID 均有接口承接

**SM 转移覆盖**

| SM 转移 | 承接 | 来源 |
|---------|------|------|
| TR-001~003 登录流程 | login | 专属 |
| TR-004 注册 | register + verify-register | 专属 |
| TR-005~006 Google | google-sync | 专属 |
| TR-007 锁定 | login (BR-002) | 专属 |
| TR-008~009 Token | 前端supabase-js | — |
| TR-010 退出 | common-logout | common |

- [x] 每条 SM 转移均有承接

**D01/B01 一致性**
- [x] 字段名/类型与 D01 一致
- [x] 错误码范围遵守 B01
- [x] URL 遵守 B01（/api/v1/app/auth/...）

**page-id 覆盖**
- [x] 6 个 page-id 100% 来自 C02

**边界**
- [x] 未写 UI/HTML、未修改 SM、不跨系统

---

## 99. 待确认问题

无
