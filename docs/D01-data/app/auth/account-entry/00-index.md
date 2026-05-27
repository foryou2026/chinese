# 数据规范 · account-entry · app 专属总览

> **系统**：app
> **关联 R-ID**：R-auth-001~016 (app)
> **不做**：状态机定义(C02)、路由/接口(D02)、页面(C03)
> **共用数据**：见 docs/D01-data/common/auth/account-entry/
> **专属实体清单**：暂无（待后续业务扩展补充）
> **专属枚举清单**：暂无

---

## 1. ER 图（仅专属实体 + 共用引用关系）

暂无专属实体。

## 2. 共用实体引用

> 以下实体定义在 common/，本系统复用

| 实体 | 本系统使用方式 | RLS/访问控制 |
|------|-------------|-------------|
| user_profiles | 用户资料读写、Google 登录自动创建 | RLS: auth.uid() = id |
| login_attempts | 用户登录限流 | Service 层按 system_id = 'app' 过滤 |
| user_sessions | 用户会话管理、多设备限制 | RLS: auth.uid() = user_id，system_id = 'app' |
| audit_logs | 用户操作审计 | RLS: auth.uid() = user_id，system_id = 'app' |

## 3. 系统专属业务规则与校验

暂无。

## 4. 索引策略

暂无。

## 5. 种子数据

暂无。

## 6. 增量融合报告

暂无。

## 7. 自检报告

暂无（无专属实体，所有数据承接由 common/ 覆盖）。

## 99. 待确认问题

暂无。
