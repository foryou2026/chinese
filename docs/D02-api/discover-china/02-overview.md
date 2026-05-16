<!-- TARGET-PATH: docs/D02-api/discover-china/02-overview.md -->

# 02 · 全局约定

## 1. 路径与编码

- 路径中 `:code` 指业务编码(类目 `01..12`、文章 12 位 `[A-Z0-9]`);`:id` 指 UUID;
- C 端优先暴露 `code`(更短更稳),管理端在内部 CRUD 用 `id`(无需关心 code 是否被改);
- 文章 code 由后端 RPC `fn_gen_article_code()` 生成,前端不可传入。

## 2. 鉴权

| 端 | 头 | 中间件 |
|----|------|--------|
| C 端公开接口 | 无 | Hono `cors` + rate-limit |
| C 端登录接口 | `Authorization: Bearer <supabase token>` | `apps/api-app` `authMiddleware` |
| 管理端 | `Authorization: Bearer <admin token>` | `apps/api-admin` `requireRole('super_admin')` |
| 内部 I1 | `Authorization: Bearer <service-role JWT>` | `serviceRoleOnly` + nginx 网段白名单 |

C 端 OP-C2 / C3 / C5 为**分级公开**:类目 `01..03` 完全公开,`04..12` 必须登录(401 + `redirect_to=/login`)。

## 3. 响应封装(G1-04 §3.1)

```ts
type ApiResponse<T> = {
  code: number;            // 0 = 成功
  message: string;
  data?: T;
  errors?: { field: string; code: string; message: string }[];
  request_id: string;      // UUID v4,Hono 中间件注入
  server_time: string;     // ISO-8601 +08:00
};
```

所有示例为简洁省略 `request_id` / `server_time`,中间件保证存在。

## 4. 分页

```ts
type Pagination = {
  page: number;            // 1-based
  page_size: number;       // 默认 20,上限 100(A15 上限 50)
  total: number;
  total_pages: number;
  has_next: boolean;
};
```

## 5. 排序

- 字段名以 `sort` 传,前缀 `-` 表示降序;
- 必须命中白名单,否则 `40002 SORT_FIELD_NOT_ALLOWED`,前端只提示"排序方式不支持"。

## 6. 多语言文案

- 响应统一下发完整 5 语言 jsonb(`name_i18n` / `title_i18n` / `description_i18n`),前端按 `Accept-Language` 取键;
- 错误文案在 `packages/shared-config/src/error-codes.ts` 提供 5 语言。

## 7. 时间字段

全部 ISO-8601 带时区(`+08:00`)。

## 8. 限流(G1-04 §六)

| 维度 | 默认 | china 域覆盖 |
|------|------|-------------|
| IP | 60 / min | OP-C4 单独 **20 / min**(缓存命中不计) |
| 用户 | 120 / min | OP-A15 单独 **30 / min**(防拖库) |

## 9. 缓存

- OP-C1 `Cache-Control: public, max-age=3600`(类目极少变);
- OP-C2 / C3 SWR 30s + 应用层缓存(`pg_notify('china_article_published'/.unpublished')` 触发 invalidate);
- TTS mp3 走 Storage CDN,永久缓存。

## 10. Idempotency

- OP-C4 接受可选 `Idempotency-Key` 头,同 key + 同 sentence_id 5 分钟内只发起一次上游调用;
- 写接口默认无幂等键(管理员场景容忍重复提交)。
