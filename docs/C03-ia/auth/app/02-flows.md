<!-- TARGET-PATH: docs/C03-ia/auth/app/02-flows.md -->

# `auth` · 业务流程

> 主流程图见 [`C01-requirements/auth/flows/main-flow.md`](../../C01-requirements/auth/flows/main-flow.md)。
> 异常流程图见 [`C01-requirements/auth/flows/exception-flow.md`](../../C01-requirements/auth/flows/exception-flow.md)。
> 本文件只做**索引**：避免主 / 异常流程图在两处重复维护。

| Flow ID | 名称 | 类型 | 文件 |
|---------|------|------|------|
| FL-auth-app-01 | 邮箱注册主流程 | main | [main-flow §1](../../C01-requirements/auth/flows/main-flow.md) |
| FL-auth-app-02 | 登录主流程（密码 / 节流 / 禁用 / 角色错位）| main | [main-flow §2](../../C01-requirements/auth/flows/main-flow.md) |
| FL-auth-app-03 | 个人中心 - 修改资料 | main | [main-flow §3](../../C01-requirements/auth/flows/main-flow.md) |
| FL-auth-app-04 | 修改密码 + 退出登录 | main | [main-flow §4](../../C01-requirements/auth/flows/main-flow.md) |
| FL-auth-app-05 | 错密 5/15min 锁定 | exception | [exception-flow §1](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-06 | 第 4 设备登录被踢 | exception | [exception-flow §2](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-07 | 账号被禁用 | exception | [exception-flow §3](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-08 | OAuth 失败 / 取消 / 角色错位 | exception | [exception-flow §4](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-09 | 邮件 / 重置链接过期 | exception | [exception-flow §5](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-10 | 网络断 / 5xx | exception | [exception-flow §6](../../C01-requirements/auth/flows/exception-flow.md) |
| FL-auth-app-11 | 守卫拦截未登录 | exception | [exception-flow §7](../../C01-requirements/auth/flows/exception-flow.md) |
