<!-- TARGET-PATH: docs/C04-pages/auth/app/00-index.md -->

# 00 · 索引 · auth / **app**

> 页面交互规范（Pages）· auth feature · `app` 端。

## 本目录页面

| 文件 | 页面 |
|------|------|
| [P-app-auth-001.md](P-app-auth-001.md) | 登录 |
| [P-app-auth-001.scenarios.md](P-app-auth-001.scenarios.md) | 场景验证脚本 |
| [P-app-auth-002.md](P-app-auth-002.md) | 注册 |
| [P-app-auth-003.md](P-app-auth-003.md) | 验证邮件已发送 |
| [P-app-auth-004.md](P-app-auth-004.md) | OAuth / 邮箱验证回调 |
| [P-app-auth-005.md](P-app-auth-005.md) | 忘记密码 |
| [P-app-auth-006.md](P-app-auth-006.md) | 重置密码 |
| [P-app-auth-007.md](P-app-auth-007.md) | 个人中心首页 |
| [P-app-auth-008.md](P-app-auth-008.md) | 账号与安全 |
| [P-app-auth-009.md](P-app-auth-009.md) | 编辑资料 |

## 上下游

- **上游**：
  - [`C01-requirements/auth/baseline.md`](../../../C01-requirements/auth/baseline.md)（需求基线）
  - [`C03-ia/auth/app/`](../../../C03-ia/auth/app/)（IA + 状态机 + 流程）
  - 本 feature 退化为单 surface，无 `_shared/`
- **下游**：
  - [`C05-prototype/auth/app/`](../../../C05-prototype/auth/app/)（HTML 原型）
  - [`C06-prd/auth/app/`](../../../C06-prd/auth/app/)（PRD）

## 状态

| 字段 | 值 |
|------|----|
| 冻结状态 | 进行中 |
| 最近更新 | 2026-05-16 |

未决问题写入 [99-open-questions.md](../99-open-questions.md)。
