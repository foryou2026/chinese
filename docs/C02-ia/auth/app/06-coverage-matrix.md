<!-- TARGET-PATH: docs/C02-ia/auth/app/06-coverage-matrix.md -->

# `auth` · 覆盖矩阵

> **冻结状态**：已冻结 · 2026-05-16  
> 此表是 D03 V01 上游链一致性校验的输入。
>
> **ID 缩写约定**:本文件内 `R-NNN` = `R-auth-NNN`;`P-NNN` = `P-auth-NNN`;`M-NN` = `M-auth-app-NN`;`FL-NN` = `FL-auth-app-NN`;`SM-NN` = `SM-auth-app-NN`。完整 ID 见 [`C01/baseline.md`](../../C01-requirements/auth/app/notes.md) 与 [`04-pages.md`](./04-pages.md)。

| R-ID | M | Flow | SM | page-id |
|------|---|------|----|---------|
| R-001 | M-01 | FL-01 | SM-01 / SM-04 | P-002, P-003, P-004 |
| R-002 | M-01 | FL-01 | SM-01 / SM-03 / SM-04 | P-002, P-004 |
| R-003 | M-01 | FL-02 | SM-01 / SM-03 | P-001 |
| R-004 | M-01 | (跨页 cookie) | SM-03 | 全部已登录页 |
| R-005 | M-01 | FL-02 / FL-06 | SM-03 | P-001 |
| R-006 | M-01 | FL-02 / FL-05 / FL-07 | SM-01 / SM-03 | P-001 |
| R-007 | M-02 | FL-04 (改密分支为主)、独立的「忘密-重置」分支由本 R 描述 | SM-01 / SM-04 | P-005, P-006 |
| R-008 | M-03 | FL-03 | SM-01 | P-007, P-009 |
| R-009 | M-03 | FL-04 | SM-01 | P-008 |
| R-010 | M-03 | FL-04 | SM-03 | P-008, 顶栏头像下拉 |
| R-011 | M-01 | FL-08 | SM-01 / SM-04 | P-001, P-004 |
| R-012 | M-01 / M-02 | FL-09 | SM-04 | P-003, P-004, P-006 |
| R-013 | M-01 | FL-11 | SM-03 | 全部受保护页 |
| R-014 | M-01 | FL-01 | SM-01 | P-002 |
| R-015 | M-01 | FL-01 | SM-02 | P-003 |

> 反向校验：每个 page-id 必能命中至少 1 个 R-ID ✓；每个 R-ID 必能命中至少 1 个 page-id 或全局守卫 / 状态机 ✓。
