<!-- TARGET-PATH: docs/C02-ia-interaction/auth/06-coverage-matrix.md -->

# 覆盖矩阵

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16
>
> 本表用于 D 阶段接口 / 数据规范的上游链一致性校验。

---

## app 端

> **缩写约定**：`R-NNN` = `R-auth-NNN`；`P-NNN` = `P-app-auth-NNN`；`M-NN` = `M-auth-app-NN`；`FL-NN` = `FL-auth-app-NN`；`SM-NN` = `SM-auth-app-NN`。

| R-ID | M | Flow | SM | page-id |
|------|---|------|----|---------|
| R-001 | M-01 | FL-01 | SM-01 / SM-04 | P-002, P-003, P-004 |
| R-002 | M-01 | FL-01 | SM-01 / SM-03 / SM-04 | P-002, P-004 |
| R-003 | M-01 | FL-02 | SM-01 / SM-03 | P-001 |
| R-004 | M-01 | （跨页 cookie）| SM-03 | 全部已登录页 |
| R-005 | M-01 | FL-02 / FL-06 | SM-03 | P-001 |
| R-006 | M-01 | FL-02 / FL-05 / FL-07 | SM-01 / SM-03 | P-001 |
| R-007 | M-02 | FL-04（改密）/ 忘密-重置 | SM-01 / SM-04 | P-005, P-006 |
| R-008 | M-03 | FL-03 | SM-01 | P-007, P-009 |
| R-009 | M-03 | FL-04 | SM-01 | P-008 |
| R-010 | M-03 | FL-04 | SM-03 | P-008, 顶栏头像下拉 |
| R-011 | M-01 | FL-08 | SM-01 / SM-04 | P-001, P-004 |
| R-012 | M-01 / M-02 | FL-09 | SM-04 | P-003, P-004, P-006 |
| R-013 | M-01 | FL-11 | SM-03 | 全部受保护页 |
| R-014 | M-01 | FL-01 | SM-01 | P-002 |
| R-015 | M-01 | FL-01 | SM-02 | P-003 |

> 反向校验：每个 page-id 至少命中 1 个 R-ID ✓；每个 R-ID 至少命中 1 个 page-id 或全局守卫 / 状态机 ✓。

---

## admin 端

> **缩写约定**：`R-NNN` = `R-auth-NNN`；`P-NNN` = `P-admin-auth-NNN`；`M-NN` = `M-auth-admin-NN`；`FL-NN` = `FL-auth-admin-NN`；`SM-NN` = `SM-auth-admin-NN`。

### R × M × Page

| R-ID | M-ID | page-id |
|------|------|---------|
| R-001 | M-01 | P-001 |
| R-002 | M-01 | P-001 + 全局守卫 |
| R-003 | M-02 | 全局 + P-004 |
| R-004 | M-02 | P-001（kicked）|
| R-005 | M-01 | P-001 |
| R-006 | M-01 | P-002 + P-003 |
| R-007 | M-02 | P-004 |
| R-008 | M-02 | P-004 + 顶栏 |
| R-009 | M-01 | 守卫 → P-001 |
| R-010 | —（运维）| — |

### Flow × Page

| Flow-ID | page-id |
|---------|---------|
| FL-01 | P-001 |
| FL-02 | P-002 → 邮箱 → P-003 |
| FL-03 | P-004 |
| FL-04 | P-004 / 顶栏 |
| FL-05 | P-001 not-admin 态 |
| FL-06 | P-001 locked 态 |
| FL-07 | P-001 error 态 |
| FL-08 | P-001 kicked-back 态 |
| FL-09 | P-003 token-invalid 态 |
| FL-10 | （路由）→ P-001 |
| FL-11 | 全部页 Toast |

### SM × Page

| SM-ID | page-id |
|-------|---------|
| SM-01 | P-001/002/003/004 |
| SM-02 | P-002 |
| SM-03 | 全局 + P-001 子态 |
