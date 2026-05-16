<!-- TARGET-PATH: docs/B02-permissions/99-open-questions.md -->

# 99 · B02 待确认问题

## Q-2026-05-16-01 · 错误码补登 `AUTH_USE_USER_ENTRY`

- **来源**:批次 4 `admin-auth` D03 V01 校验
- **问题**:本期新增错误码 `AUTH_USE_USER_ENTRY` (403,管理端登录检测到非 super_admin 角色) 已在 [`D02-api/admin-auth/04-error-codes.md §1`](../D02-api/admin-auth/04-error-codes.md) 完整声明并落地,但尚未补入 B02-03 §4 全局错误码清单
- **处置**:下一次 F 层修订时,在 [`03-authz-mechanism.md §4`](./03-authz-mechanism.md) 错误码表新增一行;不阻断当前 feature 冻结
- **责任**:F 层维护者

## 历史回顾

- 2026-04-28：B02 整组冻结（与 grules/G3 决策完全一致：2 角色 / HttpOnly Cookie / 多设备 3 上限 / 无 2FA / mock 邮件 / 无第三方验证码）。
- 12 个澄清问题全部归并到 `docs/A00-meta/questions/A-questions-round1-resolved.md`，本目录无单独遗留问题。

未来新增未决问题请在此追加，并同步 `docs/A00-meta/changelog.md` 标记 B02 进入变更状态。
