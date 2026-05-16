<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-cookie-set.md -->

# `POST /v1/auth/cookie/set`

## 用途
cookieStorage Adapter 在 signIn / refresh 成功后写 HttpOnly cookie。

## 请求

```json
{ "key": "zhiyu-at", "value": "<jwt>", "maxAge": 3600 }
```

key 白名单：`zhiyu-at`（maxAge 3600）、`zhiyu-rt`（maxAge 2592000）。

## 响应

```http
HTTP/1.1 200 OK
Set-Cookie: zhiyu-at=<jwt>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```
```json
{ "data": null, "error": null }
```

## 鉴权
- 无 (无法在登录瞬间携带有效 token)；
- **必须**校验 body 的 JWT 签名是否能用 `SUPABASE_JWT_SECRET` 验出且未过期，否则视为伪造 → 400 `INVALID_TOKEN`；
- 同时**首次**写 `zhiyu-csrf` cookie（非 HttpOnly，32 字节随机）。

## 错误码
- 400 `INVALID_KEY` / `INVALID_TOKEN`
- 5xx 同全局
