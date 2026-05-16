<!-- TARGET-PATH: docs/D02-api/discover-china/00-index.md -->

# D02 · 接口规范 · discover-china

> **阶段**:D02-L · **feature**:`discover-china` · **冻结状态**:已冻结 · 2026-05-16

| 文件 | 内容 |
|------|------|
| [01-routes-delta.md](./01-routes-delta.md) | 本期新增 / 变更 / 下线路由清单 |
| [02-overview.md](./02-overview.md) | 全局约定:鉴权 / 分页 / 限流 / 多语言 / 响应封装 |
| [03-endpoints/01-app-browse.md](./03-endpoints/01-app-browse.md) | C1 / C2 / C3 / C5 应用端浏览 |
| [03-endpoints/02-app-tts.md](./03-endpoints/02-app-tts.md) | C4 + AUX 朗读触发与轮询 |
| [03-endpoints/03-app-progress-deprecated.md](./03-endpoints/03-app-progress-deprecated.md) | C6 / C7 已下线 |
| [03-endpoints/04-admin-categories.md](./03-endpoints/04-admin-categories.md) | A1 管理端 12 类目 |
| [03-endpoints/05-admin-articles.md](./03-endpoints/05-admin-articles.md) | A2..A8 管理端文章 CRUD + 发布 / 下架 / 删除 |
| [03-endpoints/06-admin-sentences.md](./03-endpoints/06-admin-sentences.md) | A9..A14 管理端句子 CRUD + 重排 |
| [03-endpoints/07-admin-search.md](./03-endpoints/07-admin-search.md) | A15 全局搜索 |
| [03-endpoints/08-internal.md](./03-endpoints/08-internal.md) | I1 / I2 内部接口 |
| [04-error-codes.md](./04-error-codes.md) | `CHINA_*` 错误码登记(45000-45999 区段) |
| [05-concurrency.md](./05-concurrency.md) | LWW + 行锁 + Idempotency 策略 |
| [06-events.md](./06-events.md) | 业务事件(发布 / 下架 / TTS 完成) |
| [99-open-questions.md](./99-open-questions.md) | 待确认问题 |

## 基础路径
- 应用端 C 端:`/api/v1`
- 管理端:`/admin/v1`
- 内部:`/internal/v1`(nginx 不暴露)
