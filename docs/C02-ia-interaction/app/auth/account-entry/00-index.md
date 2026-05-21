# 信息架构与交互规范 — 索引

> **阶段**：C02
> **系统**：app
> **模块**：auth
> **功能**：account-entry
> **需求来源**：docs/C01-requirements/app/auth/account-entry/baseline.md

## 文件清单

| 文件 | 内容 |
|------|------|
| 01-feature-catalog.md | 功能模块清单 |
| 02-flows.md | 业务流程图 |
| 03-state-machines.md | 状态机 |
| 04-page-supplement.md | 页面补充规范（表单校验/a11y/角色差异，布局与交互由 C03 原型承载） |
| 05-coverage-matrix.md | R-ID 覆盖矩阵 |
| 06-error-pages.md | 系统兜底页 |
| 99-open-questions.md | 待确认问题 |

## 增量融合 · 第 1 轮 · 功能「account-entry」

### 本轮新增
| 类型 | ID | 说明 |
|------|-----|------|
| 模块 | M-auth-001 | 账号入口模块 |
| 页面 | P-app-auth-001 ~ 006 | 登录/注册/忘记密码/重置密码/设置(修改密码)/设置(密码管理) |
| 流程 | FL-auth-001 ~ 006 | 邮箱登录/注册/Google登录/找回密码/重置密码/修改密码 |
| 状态机 | SM-auth-001 | 登录会话状态 |

### 融合点 / 冲突点
无（首轮）
