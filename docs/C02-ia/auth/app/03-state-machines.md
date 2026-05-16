<!-- TARGET-PATH: docs/C02-ia/auth/app/03-state-machines.md -->

# `auth` · 状态机

> **冻结状态**：已冻结 · 2026-05-16

---

## SM-auth-app-01 · 通用提交按钮（注册 / 登录 / 忘密 / 重置 / 改资料 / 改密）

```mermaid
stateDiagram-v2
    [*] --> idle
    idle --> submitting: 点击提交 (并校验通过)
    idle --> idle: 字段校验失败 (内联错)
    submitting --> idle_error: 4xx / 5xx (回到 idle 并显错)
    submitting --> done: 200
    idle_error --> submitting: 修改后再次提交
    done --> [*]
```

| 状态 | 按钮 | 输入 | UI 反馈 |
|------|------|------|---------|
| idle | 可点 / 校验通过才高亮 | 可写 | — |
| submitting | loading + disabled | readonly | 自身 spinner |
| idle_error | 可点 | 可写 | 字段下内联红字 (4xx) 或顶部 Toast (5xx) |
| done | — | — | Toast 或跳转 |

## SM-auth-app-02 · 重发验证邮件按钮 / 忘密发送按钮

```mermaid
stateDiagram-v2
    [*] --> ready
    ready --> cooldown: 点击 → 200
    ready --> cooldown_after_error: 点击 → 429
    cooldown --> ready: 60s 倒计时到 0
    cooldown_after_error --> ready: 后端给出的剩余秒数到 0
```

> 文案：`重新发送 (NNs)`，倒计时实时刷新；按钮 disabled 期间禁止点击。

## SM-auth-app-03 · 用户会话（前端 supabase-js + cookieStorage）

```mermaid
stateDiagram-v2
    [*] --> anon
    anon --> authed: signIn / signUp 成功 + cookie/set 成功
    authed --> refreshing: access 到期前 60s 触发 refresh
    refreshing --> authed: 200
    refreshing --> anon: 失败 (refresh 过期 / 被踢 / 被禁)
    authed --> anon: signOut 主动 / session-status kicked / 401 from any API
    anon --> anon: 401 from any API (忽略)
```

- 转 `anon` 时统一动作：清 cookieStorage + clear Zustand authStore + 跳 `/auth/login?reason=<kicked|disabled|expired|signout>`；
- `reason=signout` 不弹 Toast；其他 reason 在登录页根据 query 弹 Toast。

## SM-auth-app-04 · 验证邮件 / 重置链接 token 校验

```mermaid
stateDiagram-v2
    [*] --> exchanging
    exchanging --> success: exchangeCodeForSession 200
    exchanging --> token_invalid: otp_expired / token_used / invalid
    exchanging --> failed: 网络 / 5xx
    success --> [*]: 跳目标页
    token_invalid --> [*]: 切换页内子态 → 「链接已过期」+ 重新发起入口
    failed --> exchanging: 用户点「重试」
```
