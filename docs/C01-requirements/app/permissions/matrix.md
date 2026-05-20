# 权限矩阵

> 增量更新，标注 [本轮新增] / [本轮变更]。

## P2. 权限矩阵

| 资源/操作 | ROLE-USER | 数据范围 | 所属功能 | 增量标记 |
|-----------|----------|---------|---------|---------|
| 注册页访问 | 允许（公开） | 无 | auth/account-entry | [本轮新增] |
| 登录页访问 | 允许（公开） | 无 | auth/account-entry | [本轮新增] |
| 邮箱注册 | 允许（公开） | 自身数据 | auth/account-entry | [本轮新增] |
| 邮箱登录 | 允许（公开） | 自身凭证 | auth/account-entry | [本轮新增] |
| Google 登录 | 允许（公开） | 自身 OAuth | auth/account-entry | [本轮新增] |
| 忘记密码 | 允许（公开） | 自身邮箱 | auth/account-entry | [本轮新增] |
| 重置密码 | 允许（公开） | 自身 Token | auth/account-entry | [本轮新增] |
| 修改/设置密码 | 允许 | 自身密码 | auth/account-entry | [本轮新增] |
| 退出登录 | 允许 | 自身会话 | auth/account-entry | [本轮新增] |

### P2.2 授权校验机制
- 前端：路由守卫拦截未登录用户
- 后端：Hono 中间件校验 JWT
- 行级/字段级：暂无 RLS（auth 功能不涉及业务数据表）

## P3. 本轮权限变更摘要
| 变更类型 | 对象 | 说明 | 来源功能 |
|---------|------|------|---------|
| 新增角色 | ROLE-USER | 普通用户角色 | auth/account-entry |
| 新增矩阵 | 登录/注册/密码相关 9 项操作 | 首轮全部新增 | auth/account-entry |
