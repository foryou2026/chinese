<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-cookie-clear.md -->

# `POST /v1/auth/cookie/clear`

## 用途
退出时清 3 个 cookie。

## 请求体
空。

## 响应

```http
Set-Cookie: zhiyu-at=; Max-Age=0; ...
Set-Cookie: zhiyu-rt=; Max-Age=0; ...
Set-Cookie: zhiyu-csrf=; Max-Age=0; ...
```
```json
{ "data": null, "error": null }
```

## 鉴权
无（即使无 cookie 也允许清——幂等）。
