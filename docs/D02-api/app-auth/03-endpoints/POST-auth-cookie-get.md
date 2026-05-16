<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-cookie-get.md -->

# `POST /v1/auth/cookie/get`

## 用途
cookieStorage Adapter 从浏览器读 `zhiyu-at` / `zhiyu-rt`；因 supabase-js 期望"同步 storage"，前端调用是同步 IPC + 后端 echo cookie 值（HttpOnly 不能直接 JS 访问）。

## 请求

```json
{ "key": "zhiyu-at" }
```

## 响应

```json
{ "data": { "value": "<jwt>" }, "error": null }
```

值不存在 → `{ "data": { "value": null }, "error": null }`。

## 错误码
- 400 `INVALID_KEY`（key 不在 `[zhiyu-at, zhiyu-rt]` 白名单）

## 备注
- 不做鉴权（cookie 已是浏览器自己持有的，echo 不增加风险）；
- 实际生产建议在 web-app 内置同步内存缓存 + Cookie store API，本接口只是 Adapter 兜底。
