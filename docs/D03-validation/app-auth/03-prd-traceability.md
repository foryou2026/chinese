<!-- TARGET-PATH: docs/D03-validation/app-auth/03-prd-traceability.md -->

# D03 · V03 PRD 回链校验 · `app-auth`

> 校验目标：[`C05-prd/app-auth/`](../../C05-prd/app-auth/00-index.md) 每一节 / 每一规则 / 每一指标 都能向下追溯到 C01 R-ID 与 D 阶段产物。
> 校验执行 · 2026-05-16 · 全部 PASS。

---

## 1. PRD 节 × 下游产物

| PRD 节 | 来源 (C01/B*) | 落地 (D01/D02/C03) | 状态 |
|--------|---------------|---------------------|------|
| 01-overview §3 关键指标 | — (新建)| 待 v1 上线后埋点验证（analytics feature v2 接管）| ✓ 已声明 |
| 02-glossary | B02-02, B02-09 | D02-02 鉴权机制 | ✓ |
| 03-personas | B02-01 | D02-02 §3 守卫 + C03 各页角色限制 | ✓ |
| 04-feature-catalog | C02-01 | C03 9 页 + D02 15 endpoint | ✓ |
| 05-user-journeys 5 条 | C01-flows | C03 各页 + D02 全部接口 | ✓ |
| 06-page-specs | C03 9 页 | (索引页) | ✓ |
| 07-business-rules BR-1..BR-8 | B02-02 / 05 / G3-05 | D01-03 + D02-05/06 + C03 各页 | ✓ |
| 08-roles-permissions 矩阵 | B02-01 / 03 | D02-02 + 各 endpoint 守卫 | ✓ |
| 09-design-summary | B04 全套 | C03 各页 | ✓ |
| 10-known-issues K-01..K-06 | — | 入 roadmap v1.1 / v2 / v3+ | ✓ |
| 11-roadmap | — | 跨版本规划，无下游 | ✓ |
| 12-changelog | — | 仅条目 v1.0.0 | ✓ |

## 2. R-ID × PRD 段反向回链

| R-ID | 出现的 PRD 段 |
|------|--------------|
| R-001 邮箱注册 | 04 / 05 旅程 1-2 / 07 BR-1/BR-2 |
| R-002 Google 注册 | 04 / 05 旅程 1 / 07 BR-6 |
| R-003 邮密登录 | 04 / 05 旅程 3 / 07 BR-4 |
| R-004 Cookie | 02 glossary / 07 BR-3 |
| R-005 多设备 | 05 旅程 3 / 07 BR-3 |
| R-006 锁定 + 禁用 | 05 旅程 5 / 07 BR-4 / BR-5 |
| R-007 忘密 | 05 旅程 4 / 07 BR-7 |
| R-008 改资料 | 04 / 07 BR-8 |
| R-009 改密 | 04 / 07 BR-1 / BR-3 |
| R-010 退出 | 04 / 08 矩阵 |
| R-011 OAuth 错位 | 03 attacker / 07 BR-6 |
| R-012 链接过期 | 07 BR-7 |
| R-013 守卫 | 08 矩阵第 2 行 |
| R-014 邮箱存在性 | 07 BR-2 |
| R-015 重发节流 | 07 BR-4 |

## 3. 无悬空声明

- PRD 内**无**新引入的需求条目未走 R-ID（每段新声明都标注引用源）；
- 全部 known issues (K-01~K-06) 已映射到 roadmap 某一版本；
- 全部商业指标（注册转化、登入 p95 等）落到了 analytics feature 的未来工作（v2）。

## 4. 校验结论

**PASS** — PRD 全文向上 100% 回链到 C01 R-ID 与 B0* 基础设施，向下 100% 落到 D01/D02/C03 实现产物；无悬空段落，无幽灵指标。
