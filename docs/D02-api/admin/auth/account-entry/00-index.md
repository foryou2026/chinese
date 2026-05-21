# 接口规范 · account-entry · 总览

> **系统**：admin
> **关联 R-ID**：R-auth-001~011
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **特殊说明**：admin 系统无注册、无 Google 登录。Token 刷新由前端 `supabase-js` 自动处理(B01-09)。登录时必须校验 `app_metadata.role=admin`。IP 白名单由 Nginx 层处理（因 VPN IP 不固定，API 层不做 IP 校验）。
> **接口详情**：01-login.md ~ 03-session.md

---

## 1. 路由表

### 1.1 page-id → URL 映射

| page-id | 页面名称 | URL | 鉴权 | 可见角色 |
|---------|---------|-----|------|---------|
| P-admin-auth-001 | 登录页 | /login | 公开 | 全部 |
| P-admin-auth-002 | 忘记密码页 | /forgot-password | 公开 | 全部 |
| P-admin-auth-003 | 重置密码页 | /reset-password | 公开(需验证码token) | 全部 |
| P-admin-auth-004 | 后台壳 | / | Bearer JWT + role=admin | ROLE-ADMIN |

---

## 2. 接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 角色 | R-ID | SM 转移 | 详情 |
|--------|------|------|------------|------|------|--------|------|
| API-admin-auth-login | POST | /api/v1/admin/auth/login | 管理员邮箱登录 | 公开 | R-auth-001,002,008,011 | TR-001~004 | 01 |
| API-admin-auth-forgot-password | POST | /api/v1/admin/auth/forgot-password | 发送重置验证码 | 公开 | R-auth-003 | 无 | 02 |
| API-admin-auth-verify-reset-otp | POST | /api/v1/admin/auth/forgot-password/verify | 验证重置OTP | 公开 | R-auth-003 | 无 | 02 |
| API-admin-auth-reset-password | POST | /api/v1/admin/auth/reset-password | 重置密码 | 公开(需token) | R-auth-004,009 | 无 | 02 |
| API-admin-auth-change-password | PUT | /api/v1/admin/auth/password | 修改密码 | JWT+admin | R-auth-005,009 | 无 | 02 |
| API-admin-auth-logout | POST | /api/v1/admin/auth/logout | 退出登录 | JWT+admin | R-auth-006 | TR-007 | 03 |
| API-admin-auth-me | GET | /api/v1/admin/auth/me | 获取管理员信息 | JWT+admin | — | 无 | 03 |

---

## 3. 错误码汇总

| code | HTTP | 含义 | 文案 | 触发接口 |
|------|------|------|------|---------|
| 40001 | 400 | 参数校验失败 | 请检查输入内容 | login, forgot-password, reset-password, change-password |
| 40002 | 400 | 新密码与旧密码相同 | 新密码不能与旧密码相同 | change-password |
| 40101 | 401 | 认证失败 | 邮箱或密码错误 | login, me, logout, change-password |
| 40102 | 401 | 验证码过期 | 验证码已过期，请重新发送 | verify-reset-otp |
| 40103 | 401 | 验证码错误 | 验证码错误 | verify-reset-otp |
| 40104 | 401 | 旧密码错误 | 旧密码错误 | change-password |
| 40301 | 403 | 权限不足 | 您没有管理后台访问权限 | login, me |
| 42901 | 429 | 请求限流 | 请求过于频繁/账号已锁定 | login, forgot-password |
| 50301 | 503 | 第三方异常 | 服务暂不可用 | login |

---

## 4. 并发与幂等

| API-ID | 并发场景 | 策略 | 失败处理 |
|--------|---------|------|---------|
| API-admin-auth-login | 同一邮箱并发登录 | login_attempts 行级锁(SELECT FOR UPDATE) | 重试 |

---

## 5. 事件/Webhook

无

---

## 6. 增量融合报告

### 6.1 本轮新增 / 融合点 / 冲突点
首轮产出。共 7 个接口。无融合/冲突。

---

## 7. 自检报告

**R-ID 覆盖**

| R-ID | 承接 API-ID |
|------|------------|
| R-auth-001 邮箱登录 | login |
| R-auth-002 登录限流 | login (BR-002) |
| R-auth-003 忘记密码 | forgot-password + verify-reset-otp |
| R-auth-004 重置密码 | reset-password |
| R-auth-005 修改密码 | change-password |
| R-auth-006 退出登录 | logout |
| R-auth-007 Token过期 | 前端supabase-js自动刷新(B01-09) |
| R-auth-008 角色校验 | login (BR-013) |
| R-auth-009 密码强度 | reset-password, change-password |
| R-auth-010 邮箱格式 | 各接口 email 字段校验 |
| R-auth-011 多设备限制 | login 中会话管理 |

- [x] 每条 R-ID 均有接口承接

**SM 转移覆盖**

| SM 转移 | 承接 |
|---------|------|
| TR-001~004 登录流程 | login |
| TR-005~006 Token | 前端supabase-js |
| TR-007 退出 | logout |

- [x] 每条 SM 转移均有承接

**D01/B01 一致性**
- [x] 字段名/类型与 D01 一致
- [x] 错误码范围遵守 B01
- [x] URL 遵守 B01（/api/v1/admin/auth/...）

**page-id 覆盖**
- [x] 4 个 page-id 100% 来自 C02

**边界**
- [x] 未写 UI/HTML、未修改 SM、API-ID 带 admin 前缀、不跨系统

---

## 99. 待确认问题

无（已全部确认：IP 白名单由 Nginx 层处理，API 层不做；role≠admin 的登录失败不计入 login_attempts）
