<!-- TARGET-PATH: docs/C03-ia/auth/admin/02-flows.md -->

# C03 · 流程清单 · `auth`

## 主流程 (FL-01..04)

| Flow-ID | 标题 | mermaid 源 |
|---------|------|-----------|
| FL-auth-admin-01 | 邮密登录 | [`main-flow §1`](../../../C01-requirements/auth/flows/admin-main-flow.md#1-邮密登录-r-001--r-002--r-004) |
| FL-auth-admin-02 | 忘密 → 重置 | [`main-flow §2`](../../../C01-requirements/auth/flows/admin-main-flow.md#2-忘记密码--重置-r-006) |
| FL-auth-admin-03 | 改密 | [`main-flow §3`](../../../C01-requirements/auth/flows/admin-main-flow.md#3-改密-r-007) |
| FL-auth-admin-04 | 退出 | [`main-flow §4`](../../../C01-requirements/auth/flows/admin-main-flow.md#4-退出-r-008) |

## 异常流程 (FL-05..11)

| Flow-ID | 标题 |
|---------|------|
| FL-auth-admin-05 | 非 super_admin 登录拦截 |
| FL-auth-admin-06 | 锁定 |
| FL-auth-admin-07 | 禁用账号 |
| FL-auth-admin-08 | 第 4 设备踢最早 |
| FL-auth-admin-09 | 重置链接过期 |
| FL-auth-admin-10 | 守卫拦截 + redirect |
| FL-auth-admin-11 | 5xx 兜底 |

> 全部 mermaid 源见 [`exception-flow.md`](../../../C01-requirements/auth/flows/admin-exception-flow.md)。
