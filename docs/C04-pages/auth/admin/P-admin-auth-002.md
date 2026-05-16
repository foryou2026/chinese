<!-- TARGET-PATH: docs/C04-pages/auth/admin/P-admin-auth-002.md -->

# P-admin-auth-002 · 忘记密码

> 路径 `/admin/auth/forgot` · 公开 · 覆盖 R-006

## 1. 布局

居中 AdminAuthCard;字段:邮箱;主按钮 "发送重置邮件";底部 text-button "返回登录" → `/admin/auth/login`

## 2. 状态机 (SM-01 + SM-02)

| 状态 | UI |
|------|----|
| idle | 空表单 |
| submitting | 按钮 loading |
| sent | 卡片切换为成功态 "若邮箱存在,我们已发送重置邮件,请在 15 分钟内点击链接。" + 倒计时 60s 后允许重发 |
| throttled | 内联 "请求过于频繁,请 {retryAfter} 秒后再试" + 按钮禁用 |

## 3. 数据流

```
发起 admin 忘密接口（含节流检查与重置链接邮件发送，接口在 D02-api/auth/admin/forgot 定义，重置链接跳回 `/admin/auth/reset-password`）
  → UI = sent
```

> **统一返回**:无论邮箱是否存在,UI 都展示 sent 态,避免邮箱探测攻击。

## 4. 错误码

| 错误码 | UI |
|--------|----|
| `AUTH_FORGOT_RATE_LIMITED` | throttled 态 |
| 5xx | Toast |

## 5. i18n key

- `auth.admin.forgot.title` · `.email` · `.submit` · `.sent` · `.resend_in`

## 6. 验收

- 输入任意 (含不存在) 邮箱均显示 sent;
- 60s 内点重发 → throttled;
- dev 模式可在 `system/.dev/mailbox/` 看到占位邮件。
