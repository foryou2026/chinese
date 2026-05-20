# 架构规范 · 索引

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：无
> **冻结状态**：✅ 已冻结

---

## 0. 摘要

本项目采用 React/TS + Hono/TS + Supabase(PostgreSQL) 全栈 TypeScript 架构，Docker Compose 部署，单仓多包结构。包含 app（用户系统）和 admin（管理系统）两个独立系统，共享后端 API 按路由前缀隔离。

---

| 序号 | 文件 | 职责 |
|------|------|------|
| 01 | tech-stack | 选型与版本 |
| 02 | project-structure | 仓库结构、模块边界 |
| 03 | database | 命名、通用字段、软删除、迁移 |
| 04 | api-conventions | URL/响应/错误码/分页 |
| 05 | coding-standards | 代码风格、分层、错误处理 |
| 06 | deploy-env | Docker、端口、环境变量 |
| 07 | i18n-responsive | i18n、断点、移动适配 |
| 08 | systems | 系统清单与隔离策略 |
| 09 | auth-infra | 鉴权技术栈 |
| 99 | open-questions | 未决问题 |

## 核心原则速记

1. 全栈 TypeScript，前后端零类型断层
2. 所有源代码必须在 `system/` 目录下
3. 前端数据动态加载，禁止预渲染到静态 HTML（反爬虫）
4. Docker Compose 唯一部署方式
5. Supabase Auth 统一鉴权，后端本地 JWT 验签
6. RLS 强制启用，新表第一条语句即开启
7. i18n 沿用 i18next + TS 资源文件方案，英文源文案
8. 三端响应式，全宽自适应，禁止两侧留白
9. 单仓 npm workspace，严格 TypeScript
10. API REST 风格，按系统拆路由前缀

---

## 99. 待确认问题

全部已决议，详见 `99-open-questions.md`。B01 架构规范已封版。
