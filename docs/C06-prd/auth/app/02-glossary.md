<!-- TARGET-PATH: docs/C06-prd/auth/app/02-glossary.md -->

# 02 · 术语表

| 术语 | 释义 |
|------|------|
| **Access Token (zhiyu-at)** | JWT HS256，1h，HttpOnly + Secure + SameSite=Lax，path=/ |
| **Refresh Token (zhiyu-rt)** | 鉴权与数据底座 颁发的 refresh token，30d 滚动更新，HttpOnly cookie |
| **CSRF Token (zhiyu-csrf)** | 32 字节随机串，**非 HttpOnly**，双提交机制 |
| **cookieStorage Adapter** | 自实现的 鉴权与数据底座-js `鉴权与数据底座ClientOptions.auth.storage` 适配器，通过自托管 API（`/首版/auth/cookie/*`）读写 cookie |
| **Auth Hook (before_user_created)** | 鉴权服务 注册前置 webhook，落库 用户档案 + 校验邀请码（暂不支持）|
| **User Session 记录** | `zhiyu.会话记录 行，包含 session_id / refresh_jti / device_id / device_name / 最后活跃时间 |
| **节流 (Throttle)** | 基于 Redis sliding window 的请求频率限制；分前端节流（按钮 cooldown）与后端节流（接口） |
| **锁定 (Lockout)** | 同 email+IP 在 15min 窗口连续 5 次错密 → 拒绝接下来的 15 分钟 |
| **被踢 (Kicked)** | 多设备硬上限 3 触发，最早登录设备的 refresh token 被作废 |
| **Recovery Session** | 通过密码重置链接换取的临时会话，只允许调用 更新用户调用，不允许其他业务接口 |
