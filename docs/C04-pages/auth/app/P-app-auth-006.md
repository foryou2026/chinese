<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-006.md -->

# `P-app-auth-006` · 重置密码

> **path**：`/auth/reset-password` · **角色可见**：未登录（recovery session）  
> **R 覆盖**：R-007 / R-012  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 入参 / 前置

- URL 必含 `?code=...&type=recovery`（来自邮件重置链接）；
- 进入页 first effect 调用 recovery 交换接口（在 D02-api/auth 定义）；
- 成功后处于“recovery-only”会话（**禁止**用此会话调其他业务接口；本页处理完即真正登入）。

## 2. DOM（idle 子态）

```
GlassCard
  ├─ h1 「设置新密码」
  ├─ p  「设置后将自动登入；其他设备会被强制退出。」
  ├─ form
  │    ├─ field new_password (含强度条)
  │    ├─ field confirm_password
  │    └─ button.primary [保存新密码]
```

## 3. 4 态

| 态 | UI |
|---|----|
| `exchanging` | 首帧 Spinner + 「正在校验链接…」 |
| `idle` | 输入新密码 |
| `submitting` | 按钮 spinner |
| `success` | icon check 56px (--success) + 「密码已重置，正在登入…」+ 2s 后自动跳 `/me` |
| `token-invalid` | 警告图标 + 「链接已过期或已使用」+ link 「重新发起忘记密码」 → `/auth/forgot` |

## 4. 字段

| key | 约束（展示用） | |
|-----|----------------|--|
| new_password | ≥ 8，含字母与数字 | 强度条同 P-002 |
| confirm_password | 与 new_password 一致 | 不一致内联红字 |

> 完整校验 schema（含服务端二次校验）在 D01-data 定义。

## 5. 流程

```
1. 调用 recovery 交换接口（在 D02-api/auth 定义）
   - 失败 → token-invalid
2. 字段校验通过 → submit → 调用重置密码接口
3. 成功：
   - 本会话变正式登入会话
   - 后台触发「退出其他设备」逻辑（具体接口与会话表操作在 D02 定义）
   - 切 `success` 态 + 2s 后跳 /me
4. 失败：
   - same_password → confirm 字段下「新密码不能与旧密码相同」
   - 5xx → Toast
```

## 6. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 正常重置 | success → 跳 /me；其他设备下次刷新后登出 |
| S2 | 链接过期 | token-invalid 子态 |
| S3 | 新旧密码一致 | confirm 字段下内联 |
| S4 | 弱密码 | new_password 字段下「强度不足」 |
| S5 | 两次密码不一致 | confirm 字段下「两次输入不一致」 |
