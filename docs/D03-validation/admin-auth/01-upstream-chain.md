<!-- TARGET-PATH: docs/D03-validation/admin-auth/01-upstream-chain.md -->

# D03 · V01 上游链一致性校验 · `admin-auth`

> 2026-05-16 · 全部 PASS。

## 1. B → C

| 项 | 校验 | 结果 |
|----|------|------|
| B01-08 surfaces 中 `admin` surface 描述 | C02 路由树 `/admin/auth/*` `/admin/me` 一致 | ✓ |
| B01-09 §1 "邀请制注册" | C01 R-010 + D01-03 seed 流程一致 | ✓ |
| B01-09 §3 中间件 `requireRole('super_admin')` | D02-02 守卫策略一致 | ✓ |
| B02-01 角色定义 仅 `user`/`super_admin` | C05-08 矩阵一致 | ✓ |
| B02-02 主流程 (登录/找回/改密) | C01-flows 4 主路径一致 | ✓ |
| B02-03 错误码清单 | D02-04 全部沿用 + 新增 1 个 `AUTH_USE_USER_ENTRY` (已建议追加进 B02-03 §4 清单 → 本次校验列入「F 层 v1.1 待补」)| ⚠ |
| B02-04 5 表 | D01-01 全部复用,0 新增 | ✓ |
| B02-05 §1 admin 范围对比 | C01 in/out 边界 100% 一致 | ✓ |
| B02-05 §2.2 4 page-id | C02-04 一致 | ✓ |
| B02-05 §3.3 admin 专属接口 | D02-01 路由 delta 一致 | ✓ |
| B02-05 §5 "❌ 自助创建其他 admin" | C05-07 BR-10 + R-010 一致 | ✓ |
| B04-03 navigation 头像下拉 | C02-05 顶栏 + 头像下拉 2 项一致 | ✓ |
| B04-06 暗色模式 token | C03 admin 暗色主题约束一致 | ✓ |

### 1.1 单项轻度警告处置

- `AUTH_USE_USER_ENTRY` 在 B02-03 §4 尚未列入清单 (B02-03 当前 21 个错误码均无 admin 入口拦截语义);
- 处置方案:不重开 F 层;将本错误码记入 [`B02-permissions/99-open-questions.md`](../../B02-permissions/99-open-questions.md) 下一轮 F 修订时补入;
- 不阻断本 feature 冻结 (本错误码已在 D02-04 §1 完整声明)。

## 2. C → D

| 项 | 校验 | 结果 |
|----|------|------|
| C01 10 个 R-ID | D02 10 个 endpoint 覆盖 (R-010 无 endpoint,纯运维) | ✓ |
| C02 4 page-id | D02 路由可逐页推回 | ✓ |
| C05-07 BR-1..BR-10 | D02-02 守卫 + D02-03 各 endpoint 逻辑一致 | ✓ |
| C05-08 角色矩阵 | D02-02 守卫表一一对应 | ✓ |

## 3. 与其它 feature 边界

| 边界 | 校验 |
|------|------|
| `app-auth` | 完全独立路径 (`/v1/*` vs `/admin/v1/*`);service 复用通过依赖注入,文档零交叉 ✓ |
| `admin-users` (v2) | 本 feature 无任何 `/admin/v1/users/*`;C05-04 已声明 ✓ |
| `admin-discover` / `admin-courses` / `admin-novels` | 仅作为本 feature 守卫的下游消费者;无反向依赖 ✓ |

## 4. 结论

**PASS** (含 1 项轻度警告,不阻断冻结)
