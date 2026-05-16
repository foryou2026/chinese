<!-- TARGET-PATH: docs/D02-api/course/02-overview.md -->

# 02 · 总览(鉴权 / 限流 / 分页 / 错误信封) · course

## 2.1 鉴权矩阵

| Prefix | 鉴权 | 角色 | DB 层 |
|--------|------|------|-------|
| `/api/v1/course/*` | Supabase JWT | `learner`(注册即获) | RLS by `auth.uid()` |
| `/admin/v1/course/*` | Supabase JWT + 中间件 | `readonly` / `content_admin` / `super` + 列级 `tracks_scope` | DB 走 `service_role`,跳过 RLS;数据过滤由 SQL `WHERE track_code = ANY($scope)` 显式叠加 |
| `/internal/v1/course/*` | `X-Internal-Token` 等于 env `CRON_TOKEN` | — | `service_role` |

权限细节参考 [G3 角色定义](../../../grules/G3-权限与认证规范/01-角色定义.md)。

## 2.2 限流

| 路由 | 限制 | 桶 |
|------|------|----|
| `POST /api/v1/course/answers` | 600 / 分 | UID |
| `POST /api/v1/course/kps/:id/audio` | 20 / 分 | UID(TTS 触发避免滥用)|
| `GET /admin/v1/course/search` | 30 / 分 | admin uid |
| 其他 `/api/v1/*` | 120 / 分 | UID + IP |
| 其他 `/admin/v1/*` | 默认不限(网关 200/分基础防护) | — |
| `/internal/*` | 不限 | 内部 |

## 2.3 分页约定

- 普通后台列表:`?page=1&page_size=20&sort=created_at:desc`;响应 `{items, pagination:{total, page, page_size}}`;
- 高基数(流水/动作日志):`?cursor=<base64>&limit=50`,响应 `{items, pagination:{next_cursor}}`;
- `sort` 白名单:每个 endpoint 在文档明列允许排序字段。

## 2.4 5 语字段

- 写入:requestBody jsonb 必须 `{zh,en,vi,th,id}` 全 key 否则返 `COURSE_FIELD_TOO_LONG` / Schema mismatch 错误;
- 返回:始终返完整 5 key;
- UI 语言切换:由 C 端基于 `Accept-Language` header 或用户 `current_lang` 选取展示 key,后端不做截选。

## 2.5 错误信封

```json
// 成功
{ "ok": true, "data": { ... } }

// 失败
{
  "ok": false,
  "error": {
    "code": "COURSE_STALE_VERSION",
    "message": "记录已被他人更新,请刷新后重试",
    "details": { "current_updated_at": "2026-05-16T03:21:00Z" }
  }
}
```

HTTP 状态码:
- 400:字段 / schema / 状态机不允许;
- 401:未登录或 JWT 失效;
- 403:角色/可见性/前置不满足;
- 404:资源不存在或 RLS 不可见;
- 409:乐观锁冲突 / 唯一冲突 / 资源被引用;
- 410:quiz_id 或 exam_attempt 已过期 / 已结束;
- 429:限流;
- 5xx:系统错误,详细在 server log。

## 2.6 通用 Header

| Header | 必填 | 用途 |
|--------|------|------|
| `Authorization` | ✓(除 `/health`)| JWT |
| `Accept-Language` |  | UI 语言提示(后端用于错误 message 翻译,数据 jsonb 仍全返)|
| `If-Match` | 管理端 PATCH ✓ | 乐观锁 |
| `Idempotency-Key` | 可选 | 写入幂等 24h |
| `X-Internal-Token` | 内部 ✓ | cron 鉴权 |

## 2.7 OpenAPI / TS 类型

- OpenAPI schema 落 `system/packages/shared-schemas/openapi/course/*.yaml`(后续生成);
- Zod schema 落 `system/packages/shared-schemas/src/course/*.ts`,前后端共享;
- 错误码常量落 `system/packages/shared-schemas/src/course/error-codes.ts`。
