<!-- TARGET-PATH: docs/D02-api/app-auth/_input/operations.md -->

# `app-auth` · L01 操作输入

> 反推回写 · 2026-05-16

- 接口框架 Hono，按 [B01-architecture/04-api-conventions.md](../../B01-architecture/04-api-conventions.md) 统一响应壳；
- 全部 auth 接口跨域支持必须开 CORS 携 cookie；
- HMAC Hook 用独立子路由 `/internal/auth-hook`，**不**走 `/v1/`；
- 节流计数后端 Redis，sliding window 算法；
- 全部审计写入异步，业务返回不依赖审计完成。
