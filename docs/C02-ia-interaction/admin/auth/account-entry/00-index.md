# 信息架构与交互规范 — 索引

> **阶段**：C02
> **系统**：admin
> **模块**：auth
> **功能**：account-entry
> **需求来源**：docs/C01-requirements/admin/auth/account-entry/baseline.md

## 文件清单

| 文件 | 内容 |
|------|------|
| 01-feature-catalog.md | 功能模块清单 |
| 02-flows.md | 业务流程图 |
| 03-state-machines.md | 状态机 |
| 04-pages.md | 页面清单与交互规范 |
| 05-navigation.md | 导航结构与角色可见性 |
| 06-coverage-matrix.md | R-ID 覆盖矩阵 |
| 07-error-pages.md | 系统兜底页 |
| 99-open-questions.md | 待确认问题 |

## 增量融合 · 第 1 轮 · 功能「account-entry」

### 本轮新增
| 类型 | ID | 说明 |
|------|-----|------|
| 模块 | M-auth-001 | 账号入口模块 |
| 页面 | P-admin-auth-001 ~ 004 | 登录/忘记密码/重置密码/修改密码 |
| 流程 | FL-auth-001 ~ 004 | 登录/找回密码/重置密码/修改密码 |
| 状态机 | SM-auth-001 | 登录会话状态 |

### 融合点 / 冲突点 / 已有变更 / 导航更新
无（首轮）
