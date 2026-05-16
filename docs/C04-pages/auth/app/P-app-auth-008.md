<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-008.md -->

# `P-app-auth-008` · 账号与安全

> **角色可见**：用户
> **R 覆盖**：R-009 / R-010
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

`<PageHeader title="账号与安全" backTo="/me" />` + 内容区两张 `<GlassCard>`：「修改密码」+ 「退出登录」。

## 2. 修改密码卡片

### 2.1 DOM

```
GlassCard
  ├─ h2 「修改密码」
  ├─ form
  │    ├─ field old_password
  │    ├─ field new_password (强度条)
  │    ├─ field confirm_password
  │    └─ button.primary [保存新密码]
  └─ p.muted 「修改成功后，其他设备会被强制退出；本设备保持登录。」
```

### 2.2 字段

| key | 约束（展示用） |
|-----|----------------|
| old_password | ≥ 8 |
| new_password | ≥ 8，含字母与数字，且与旧密码不同 |
| confirm_password | 与 new_password 一致 |

> 完整校验 schema（含服务端二次校验）在 D01-data 定义。

### 2.3 流程

```
1. submit → 提交修改密码请求（接口与后端逻辑在 D02-api/auth 定义：验证旧密、更新密码、并退出其他设备会话）
2. 成功 → Toast「密码已修改」+ form reset
3. 失败：
   - 401 invalid_old_password → old 字段下「旧密码不正确」
   - 400 weak_password → new 字段下「强度不足」
   - 400 same_as_old → new 字段下「不能与旧密码相同」
   - 5xx → Toast
```

## 3. 退出登录卡片

### 3.1 DOM

```
GlassCard
  ├─ h2 「退出登录」
  ├─ p  「需要更进一步？可以退出所有设备的登录会话。」
  ├─ button.secondary [本设备退出]
  └─ button.danger    [全部设备退出]
```

### 3.2 流程

- 本设备退出：
  1. 点击 → 调用当前会话退出接口（在 D02-api/auth 定义）
  2. 清理本地会话上下文与 cookie
  3. 跳 对应页面
- 全部设备退出：
  1. **二次确认弹窗** `<Confirm>` 标题「全部设备退出？」+ danger 按钮「确认退出全部」；
  2. 调用全局退出接口（在 D02-api/auth 定义，服务端会退出该用户所有会话）；
  3. 本地会话 clear；
  4. 跳 对应页面。

## 4. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 改密成功 | Toast + 其他设备下次 refresh 后登出 |
| S2 | 旧密码错 | old 字段下内联 |
| S3 | 弱新密码 | new 字段下内联 |
| S4 | 新旧密码一致 | new 字段下内联 |
| S5 | 本设备退出 | 跳 login，无 Toast |
| S6 | 全部退出（确认）| 全设备 401 + 跳 login |
| S7 | 全部退出（取消）| 弹窗关闭，无动作 |
