<!-- TARGET-PATH: docs/D03-validation/app-auth/01-upstream-chain.md -->

# D03 · V01 上游链一致性校验 · `app-auth`

> 校验目标：本 feature 从 B0* 到 D02 之间所有跨阶段引用是否仍然成立 / 未失效 / 编号一致。
> 校验执行 · 2026-05-16 · 全部 PASS。

---

## 1. B → C 链路

| 项 | 校验 | 结果 |
|----|------|------|
| B01-01 技术栈 中 supabase-js / Hono / TanStack Router | C03 各页 `useAsyncAction` / `_auth root loader` 表述一致 | ✓ |
| B01-04 API 约定 统一响应壳 | D02-02 `{data, error, meta}` 同形 | ✓ |
| B01-06 部署 / 环境 中 `SUPABASE_JWT_SECRET` / `SUPABASE_AUTH_HOOK_SECRET` 等 | D02-03 `cookie/set` 与 `internal/auth-hook` 引用一致 | ✓ |
| B01-09 auth-infra 中 cookieStorage Adapter | D02-03 `cookie/get/set/clear` 三接口与之对齐 | ✓ |
| B02-01 角色定义 `user` / `super_admin` | C01-baseline、C05-08 全部角色枚举一致 | ✓ |
| B02-02 认证流程 主流程图 | C01-flows main-flow §1/§2 mermaid 描述一致 | ✓ |
| B02-03 authz-mechanism 错误码清单 | D02-04 errors 同步全部 21 项 | ✓ |
| B02-04 数据模型 5 张表 | D01-02 entities 5 张表反向引用 | ✓ |
| B02-05 auth-feature-guideline §2.1 9 页 page-id 列表 | C02-04 / C03 各页 `P-app-app-auth-001..009` 一一对应 | ✓ |
| B02-05 §3 接口清单 (~15) | D02-01 routes-delta + 03-endpoints/ 文件数对齐 | ✓ |
| B03-04 voice-tone "不羞辱用户" | C03 各错误码文案均不使用嘲讽语 | ✓ |
| B04-02 layout 居中 + 卡片 | C03-001 / 002 / 005 / 006 全部 `<GlassCard>` 写法一致 | ✓ |
| B04-03 navigation 头像下拉 6 项 | C02-05 §3 列出顺序与项目一致 | ✓ |
| B04-05 interactions 4xx 内联 / 5xx Toast | C03 各页"错误码映射"段一致 | ✓ |

## 2. C → D 链路

| 项 | 校验 | 结果 |
|----|------|------|
| C01 R-ID 15 条 | D02 各 endpoint 覆盖；D01-03 业务规则映射 | ✓ |
| C02 page-id 9 个 | D02 路由可推回页面 (cookie/* 除外，前端不直接走) | ✓ |
| C02 SM-04 token 校验 | D02-03 `POST-internal-auth-hook` 与 callback 流程一致 | ✓ |
| C05-07 业务规则 BR-1~BR-8 | D01-03 + D02-05 (并发) + D02-04 (错误码) 全部落地 | ✓ |
| C05-08 角色权限矩阵 | D02-02 守卫 `authRequired` / `roleRequired('user')` 配置一致 | ✓ |

## 3. 与其它 feature 边界

| 边界 | 校验 |
|------|------|
| `admin-auth` (批次 4 占位) | 本 feature **不**生成任何 `/admin/auth/*` 路由；C05-04 已说明 |
| `user-account` (v2 占位) | `/onboarding` 路径仅在 `P-app-app-auth-004` callback 中 redirect 引用，不属于本 feature 拥有 |
| `wallet/orders/referral/settings` (v2 占位) | C02-05 头像下拉 / C03-007 卡片均标注「即将推出」disabled |
| `admin-users` (v2 占位) | 本 feature 仅消费 `profiles.is_disabled` 字段（只读）|

## 4. 校验结论

**PASS** — 上游链一致性全绿，无需打回任何阶段。
