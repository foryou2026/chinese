<!-- TARGET-PATH: docs/C02-permissions/99-open-questions.md -->

# 99 · C02 待确认问题

## Q-2026-05-16-01 · 错误码补登 `AUTH_USE_USER_ENTRY`

- **来源**:批次 4 `auth` D03 V01 校验
- **问题**:本期新增错误码 `AUTH_USE_USER_ENTRY` (403,管理端登录检测到非 super_admin 角色) 需补入 [`02-authz-mechanism.md §4`](./02-authz-mechanism.md) 全局错误码清单;D02 路由阶段建立时再同步落到 `D02-api/auth/admin/04-error-codes.md`(目前 D 阶段尚未启动)
- **处置**:下一次 C02 修订时,在 [`02-authz-mechanism.md §4`](./02-authz-mechanism.md) 错误码表新增一行;不阻断当前 feature 冻结
- **责任**:C02 全局维护者

## 历史回顾

- 2026-04-28：C02 整组冻结（2 角色 / HttpOnly Cookie / 多设备 3 上限 / 无 2FA / mock 邮件 / 无第三方验证码）。
- 12 个澄清问题全部归并到 `docs/A00-meta/questions/A-questions-round1-resolved.md`，本目录无单独遗留问题。

未来新增未决问题请在此追加，并同步 `docs/A00-meta/changelog.md` 标记 C02 进入变更状态。
