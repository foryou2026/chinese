# 鉴权基础设施

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack, 08-systems
> **冻结状态**：✅ 已冻结

---

> 只定义全局鉴权技术栈，不写登录/注册流程。

## 1. Token 策略

| 项目 | 决定 |
|------|------|
| Token 类型 | JWT（Supabase Auth 签发） |
| Access Token 有效期 | 1 小时（Supabase 默认 3600s） |
| Refresh Token 有效期 | 7 天 |
| 存储位置 | 前端 `supabase-js` 自动管理（内存 + localStorage） |
| 携带方式 | `Authorization: Bearer <access_token>` |
| 刷新机制 | `supabase-js` 自动静默刷新；后端不参与刷新 |
| 多系统隔离 | 共用 Supabase Auth 实例，JWT `app_metadata.role` 区分系统权限 |

## 2. 后端验签

| 项目 | 决定 |
|------|------|
| 验签方式 | 本地无状态验签，使用 `SUPABASE_JWT_SECRET` |
| 验签库 | `jose`（TS 原生 JWT 库） |
| 验签位置 | Hono 中间件 `middleware/auth.ts` |
| 上下文透传 | 解析 `user_id`、`role` 注入 Hono Context，向下透传 |
| 性能 | 毫秒级本地解析，不发起 HTTP 请求 |

## 3. 密码安全

| 项目 | 决定 |
|------|------|
| 哈希算法 | bcrypt（Supabase Auth 内置，后端不直接处理） |
| 密码强度 | ≥ 8 字符，包含字母 + 数字 |
| 登录失败限制 | Supabase Auth 内置速率限制 + API 层限流 |
| MFA | 暂不启用，后续按需开启 Supabase TOTP MFA |

## 4. 第三方登录

| Provider | 适用系统 | 回调路径 | 接入模式 |
|----------|---------|---------|---------|
| Google OAuth | app | `/auth/callback` | Supabase Auth OAuth flow |

## 5. 会话与设备策略

| 项目 | 决定 |
|------|------|
| 多设备登录 | 允许，Supabase Auth 默认支持多会话 |
| 设备数量限制 | 暂不限制 |
| 会话注销 | 前端调用 `supabase.auth.signOut()`，后端清理上下文 |

## 6. 角色与权限

| 角色 | 标识 | 适用系统 | 说明 |
|------|------|---------|------|
| user | `app_metadata.role = 'user'` | app | 注册用户默认角色 |
| admin | `app_metadata.role = 'admin'` | admin | 后台管理员，需手动授予 |

> 细粒度权限矩阵在 C01 阶段按功能定义。

## 7. 给 auth feature 的强制约束

- 必须使用本文件定义的 Token 策略与密码规则
- 后端验签必须本地无状态，禁止每次 HTTP 请求 Supabase 验证
- 角色判断必须基于 JWT `app_metadata.role`
- admin 系统登录必须校验角色，拒绝普通用户访问

---

## 99. 待确认问题

无
