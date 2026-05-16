<!-- TARGET-PATH: docs/C02-ia/admin-auth/admin/06-coverage-matrix.md -->

# C02 · 覆盖矩阵 · `admin-auth`

> **ID 缩写约定**:本文件内 `R-NNN` = `R-admin-auth-NNN`;`P-NNN` = `P-admin-admin-auth-NNN`;`M-NN` = `M-admin-auth-NN`;`FL-NN` = `FL-admin-auth-NN`;`SM-NN` = `SM-admin-auth-NN`。完整 ID 见 [`C01/baseline.md`](../../C01-requirements/admin-auth/baseline.md) 与 [`04-pages.md`](./04-pages.md)。

## R × M × Page

| R-ID | M-ID | page-id |
|------|------|---------|
| R-001 | M-01 | P-001 |
| R-002 | M-01 | P-001 + 全局守卫 |
| R-003 | M-02 | 全局 + P-004 |
| R-004 | M-02 | P-001 (kicked) |
| R-005 | M-01 | P-001 |
| R-006 | M-01 | P-002 + P-003 |
| R-007 | M-02 | P-004 |
| R-008 | M-02 | P-004 + 顶栏 |
| R-009 | M-01 | 守卫 → P-001 |
| R-010 | — (运维) | — |

## Flow × Page

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
| FL-10 | (路由) → P-001 |
| FL-11 | 全部页 Toast |

## SM × Page

| SM-ID | page-id |
|-------|---------|
| SM-01 | P-001/002/003/004 |
| SM-02 | P-002 |
| SM-03 | 全局 + P-001 子态 |
