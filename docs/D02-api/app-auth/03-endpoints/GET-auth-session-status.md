<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/GET-auth-session-status.md -->

# `GET /v1/auth/session-status`

## 用途
前端轮询或事件触发时校验：本 session 仍有效吗？被踢了吗？被禁了吗？

## 鉴权
authRequired（authRequired 自身已经能 401，但本接口对**业务**额外报告 reason，故仍需此守卫；401 时本接口反回标准 401 响应即可）。

## 请求体
空。

## 响应

```json
{
  "data": {
    "valid": true,
    "reason": null,
    "user": { "id": "...", "role": "user", "isDisabled": false }
  },
  "error": null
}
```

失效：
```json
{ "data": { "valid": false, "reason": "kicked" | "disabled" | "expired" }, "error": null }
```

## 实现
1. cookie 取 sessionId；
2. `SELECT 1 FROM user_sessions WHERE id=? AND user_id=?` → false → `reason="kicked"`；
3. `SELECT is_disabled FROM profiles WHERE id=?` (走 LRU) → true → `reason="disabled"`；
4. 否则 `valid=true`。

## 备注
- 不返 401 即使 `valid=false`，由前端按 reason 自主处理（避免 401 与具体 reason 混淆）；
- 但 access token 已过期时 cookie 失效 → 走 401（authRequired 拦下）。
