# 系统清单与隔离策略

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack
> **冻结状态**：✅ 已冻结

---

## 1. 系统清单

| system-id | 显示名 | 用户群 | 鉴权方式 | 部署形态 | 域名策略 |
|-----------|--------|--------|---------|---------|----------|
| app | 用户系统 | 终端用户 | 邮箱登录 + Google 登录 | Docker (web-app:3000) | 主域名 |
| admin | 管理系统 | 内部运营 | 邮箱登录 | Docker (admin-app:3001) | 独立子域名（不可预测命名）+ IP/VPN 访问限制 |

## 2. 产出目录映射

| system-id | B02 体验设计 | C01 需求 | C02 交互 | C03 原型 | D02 接口 |
|-----------|-------------|---------|---------|---------|---------|
| app | docs/B02-experience-design/app/ | docs/C01-requirements/app/ | docs/C02-ia-interaction/app/ | C03-prototype/app/ | docs/D02-api/app/ |
| admin | docs/B02-experience-design/admin/ | docs/C01-requirements/admin/ | docs/C02-ia-interaction/admin/ | C03-prototype/admin/ | docs/D02-api/admin/ |

> 共享产出：`docs/B01-architecture/`、`docs/D01-data/common/`

## 3. 隔离策略

| 维度 | 策略 |
|------|------|
| 前端代码库 | 单仓双 app：`system/apps/web-app`（app）、`system/apps/admin-app`（admin） |
| 用户体系 | 共用 Supabase Auth 实例，通过 JWT `app_metadata.role` 区分系统权限；admin 角色需手动授予 |
| API 路由前缀 | app: `/api/v1/app/*`，admin: `/api/v1/admin/*` |
| 域名隔离 | admin 使用独立子域名（不可预测命名，如 `xk9m-admin.example.com`），禁止使用路径 `/admin` 区分（防止 Cookie 作用域污染和扫描器探测） |
| 访问限制 | admin 子域名配合 IP 白名单或 VPN 访问限制，Nginx 层拦截非授权来源 |
| 部署 | 同一 Docker Compose，不同容器和端口 |

## 4. 跨系统业务关联

| 关联场景 | 触发系统 | 受影响系统 | 共享数据来源 |
|---------|---------|----------|------------|
| 用户管理 | admin | app | `user_profiles` 表 |
| 内容管理 | admin | app | 业务内容表（文章、课程等） |
| 订单/支付 | app | admin | `orders`、`payments` 表 |

## 5. system x auth 映射

| system-id | 邮箱登录 | Google 登录 | 说明 |
|-----------|---------|------------|------|
| app | 是 | 是 | Supabase Auth 原生支持 |
| admin | 是 | 否 | 仅邮箱，需 admin 角色校验 |

---

## 99. 待确认问题

无
