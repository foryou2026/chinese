<!-- TARGET-PATH: docs/C02-ia/admin-auth/02-flows.md -->

# C02 · 流程清单 · `admin-auth`

## 主流程 (FL-01..04)

| Flow-ID | 标题 | mermaid 源 |
|---------|------|-----------|
| FL-admin-auth-01 | 邮密登录 | [`main-flow §1`](../../C01-requirements/admin-auth/flows/main-flow.md#1-邮密登录-r-001--r-002--r-004) |
| FL-admin-auth-02 | 忘密 → 重置 | [`main-flow §2`](../../C01-requirements/admin-auth/flows/main-flow.md#2-忘记密码--重置-r-006) |
| FL-admin-auth-03 | 改密 | [`main-flow §3`](../../C01-requirements/admin-auth/flows/main-flow.md#3-改密-r-007) |
| FL-admin-auth-04 | 退出 | [`main-flow §4`](../../C01-requirements/admin-auth/flows/main-flow.md#4-退出-r-008) |

## 异常流程 (FL-05..11)

| Flow-ID | 标题 |
|---------|------|
| FL-admin-auth-05 | 非 super_admin 登录拦截 |
| FL-admin-auth-06 | 锁定 |
| FL-admin-auth-07 | 禁用账号 |
| FL-admin-auth-08 | 第 4 设备踢最早 |
| FL-admin-auth-09 | 重置链接过期 |
| FL-admin-auth-10 | 守卫拦截 + redirect |
| FL-admin-auth-11 | 5xx 兜底 |

> 全部 mermaid 源见 [`exception-flow.md`](../../C01-requirements/admin-auth/flows/exception-flow.md)。
