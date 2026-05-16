<!-- TARGET-PATH: docs/C02-ia/admin-auth/03-state-machines.md -->

# C02 · 状态机清单 · `admin-auth`

| SM-ID | 标题 | 状态 | 转移 |
|-------|------|------|------|
| SM-admin-auth-01 | 通用提交 (复用 SM-01) | `idle → submitting → (success / error / locked / not-admin / token-invalid)` | 应用于 4 页全部表单 |
| SM-admin-auth-02 | 重发/找回 cooldown (复用 SM-02) | `enabled → throttled(retryAfter) → enabled` | 应用于 `/admin/auth/forgot` |
| SM-admin-auth-03 | admin 会话 | `signed-out → signed-in (admin) → (kicked / expired / disabled / signout)` | 全局,与 app 会话隔离 (surface 维度) |

> 不存在 SM-04 token-exchange:admin 端 reset 走与 app 同一份 `exchangeCodeForSession`,复用 app 的 SM-04 不重复定义。
