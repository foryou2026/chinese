<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-recovery/04-pages.md -->

# 页面清单 · account-recovery

> **阶段**：C02-IN · **模块**：`auth` · **功能**：`account-recovery`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端页面（2 页）

| page-id | 名称 | 类型 | 角色 | M-ID | 关联 R-ID | 主要 4 态 |
|---------|------|------|------|------|-----------|----------|
| P-app-auth-005 | 忘记密码 | 表单页 | 未登录 | M-auth-app-02 | R-auth-007/014 | idle · submitting · sent · throttled |
| P-app-auth-006 | 重置密码 | 表单页 | 未登录（recovery session）| M-auth-app-02 | R-auth-007/013 | idle · submitting · success · token-invalid |
