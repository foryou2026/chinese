<!-- TARGET-PATH: docs/C04-pages/auth/admin/00-index.md -->

# 00 · 索引 · auth / **admin**

> 页面交互规范（Pages）· auth feature · `admin` 端。

## 本目录页面

| 文件 | 页面 |
|------|------|
| [P-admin-auth-001.md](P-admin-auth-001.md) | admin 登录 |
| [P-admin-auth-002.md](P-admin-auth-002.md) | 忘记密码 |
| [P-admin-auth-003.md](P-admin-auth-003.md) | 重置密码 |
| [P-admin-auth-004.md](P-admin-auth-004.md) | 账号与安全 |

## 上下游

- **上游**：
  - [`C01-requirements/auth/baseline.md`](../../../C01-requirements/auth/baseline.md)（需求基线）
  - [`C03-ia/auth/admin/`](../../../C03-ia/auth/admin/)（IA + 状态机 + 流程）
  - 本 feature 退化为单 surface，无 `_shared/`
- **下游**：
  - [`C05-prototype/auth/admin/`](../../../C05-prototype/auth/admin/)（HTML 原型）
  - [`C06-prd/auth/admin/`](../../../C06-prd/auth/admin/)（PRD）

## 状态

| 字段 | 值 |
|------|----|
| 冻结状态 | 进行中 |
| 最近更新 | 2026-05-16 |

未决问题写入 [99-open-questions.md](../99-open-questions.md)。
