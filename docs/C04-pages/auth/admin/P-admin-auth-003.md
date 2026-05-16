<!-- TARGET-PATH: docs/C04-pages/auth/admin/P-admin-auth-003.md -->

# P-admin-auth-003 · 重置密码

> 路径 `/admin/auth/reset-password?token=...` · 公开 · 覆盖 R-006

## 1. 入口

- 仅由邮件链接进入；首次进入页面立即调用 recovery 交换接口（在 D02-api/auth 定义）
- 若 token 无效/过期 → 切换为 token-invalid 态

## 2. 布局

居中 AdminAuthCard;字段:新密码 / 重复新密码;主按钮 "设置新密码"

## 3. 状态机 (SM-04 复用 + SM-01)

| 状态 | UI |
|------|----|
| exchanging | "正在验证链接..." (整页 loading) |
| idle | 表单可填 |
| submitting | 按钮 loading |
| success | 卡片切换为 "密码已重置,即将跳转登录页..." + 3s 自动跳 管理端登录页（含回跳参数） |
| token-invalid | 红字 "链接已失效或被使用过" + 按钮 "重新申请" → `/admin/auth/forgot` |

## 4. 数据流

```
进入页 → recovery 交换接口
  ok → idle
  失败 → token-invalid

提交 → 客户端展示性校验 (≥8+字母+数字+两次相同；完整 schema 在 D01-data 定义)
     → 调用重置密码接口（并吊销其他 admin 会话，接口在 D02-api/auth 定义）
     → 跳 /admin/auth/login?email=<masked>
```

## 5. 错误码

| 错误码 | UI |
|--------|----|
| `AUTH_TOKEN_INVALID` | token-invalid 态 |
| `AUTH_WEAK_PASSWORD` | 字段下内联 |
| `AUTH_SAME_AS_OLD_PASSWORD` | (后端二次校验) 字段下内联 |
| 5xx | Toast |

## 6. i18n key

- `auth.admin.reset.title` · `.new_password` · `.repeat` · `.submit` · `.success` · `.token_invalid` · `.reapply`
