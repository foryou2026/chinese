<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-logout-global.md -->

# `POST /v1/auth/logout-global`

## 用途
"全部设备退出"。

## 鉴权
authRequired + roleRequired('user')（admin 走自己的 logout-global）。

## 请求体
空（必须 CSRF 双提交）。

## 流程
1. `supabase.auth.admin.signOut(user_id, { scope:'global' })`；
2. `DELETE FROM user_sessions WHERE user_id = ?`；
3. 当前 cookie 清掉（同 `cookie/clear`）；
4. 审计 `auth.signout_global { trigger:'user' }`。

## 响应

`{ "data": null, "error": null }` + 3 个 cookie max-age=0。
