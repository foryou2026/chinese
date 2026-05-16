<!-- TARGET-PATH: docs/D02-api/app-auth/00-index.md -->

# D02 · `app-auth` 接口规范

> **阶段**：D02-L · **feature**：`app-auth`  
> **上游**：[`C05-prd/app-auth/07-business-rules.md`](../../C05-prd/app-auth/07-business-rules.md)、[`D01-data/app-auth/`](../../D01-data/app-auth/00-index.md)、[`B02-permissions/02-auth-flow.md`](../../B02-permissions/02-auth-flow.md)  
> **下游**：apps/api-app 实现、apps/web-app supabase-js 客户端代码  
> **冻结状态**：已冻结 · 2026-05-16

---

## 文件清单

| 序号 | 文件 | 职责 |
|------|------|------|
| _input | [_input/operations.md](./_input/operations.md) | 输入 |
| 00 | 00-index.md（本文）| 索引 |
| 01 | [01-routes-delta.md](./01-routes-delta.md) | 本 feature 注册到全局路由表的增量行 |
| 02 | [02-overview.md](./02-overview.md) | 接口分组 + 鉴权策略 + 统一响应壳 |
| 03 | [03-endpoints/](./03-endpoints/) | 单接口卡片 × 15 |
| 04 | [04-error-codes.md](./04-error-codes.md) | 错误码清单与文案 |
| 05 | [05-concurrency.md](./05-concurrency.md) | 并发约束（session-register 等）|
| 06 | [06-events.md](./06-events.md) | 审计事件清单 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 无 |
