<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-cookie.md -->

# POST /admin/v1/auth/cookie/{get,set,clear}

> 三接口合并描述;实现完全镜像 [`/v1/auth/cookie/*`](../../app-auth/03-endpoints/POST-auth-cookie-get.md)。

## 1. 用途

supabase-js `cookieStorage` adapter 在 admin 端的同源代理。

## 2. 入参 / 出参

| 接口 | 入参 | 出参 |
|------|------|------|
| get | `{ key }` | `{ value: string \| null }` |
| set | `{ key, value, options? }` | `{ ok: true }` |
| clear | `{ key }` | `{ ok: true }` |

## 3. 安全约束

- `key` 白名单:`sb-access-token` / `sb-refresh-token` / `sb-provider-token` / `zhiyu-csrf`;其它拒;
- set 写 Cookie 时强制 `HttpOnly + Secure + SameSite=Lax + Path=/`;
- `zhiyu-csrf` 非 HttpOnly (前端需读);

## 4. 守卫

仅 `csrfGuard` (set/clear);get 公开。

## 5. 审计

不写 (高频)。
