# 页面补充规范

> 页面 ID：`P-app-<module>-<seq3>`。布局/操作/场景/文案由 C03 原型体现，本文件仅补充原型无法表达的规范。

## 页面总览
| page-id | 名称 | 类型 | 角色 | M-ID | 关键 R-ID | SM-ID |
|---------|------|------|------|------|----------|-------|
| P-app-auth-001 | 登录页 | form | 公开 | M-auth-001 | R-auth-002~004, R-auth-013, R-auth-017~018 | SM-auth-001 |
| P-app-auth-002 | 注册页 | form | 公开 | M-auth-001 | R-auth-001, R-auth-003, R-auth-015, R-auth-017~018 | SM-auth-001 |
| P-app-auth-003 | 忘记密码页 | form | 公开 | M-auth-001 | R-auth-005, R-auth-017~018 | 无 |
| P-app-auth-004 | 重置密码页 | form | 公开 | M-auth-001 | R-auth-006, R-auth-017~018 | SM-auth-001 |
| P-app-auth-005 | 修改/设置密码页 | form | ROLE-USER | M-auth-001 | R-auth-007, R-auth-014, R-auth-018 | 无 |
| P-app-auth-006 | 设置页 | list | ROLE-USER | M-auth-001 | R-auth-007~009, R-auth-018 | SM-auth-001 |

---

## 通用：语言切换器规范（R-auth-017）

> 适用于所有公开页面：P-app-auth-001 ~ P-app-auth-004

### 位置与样式
- **位置**：页面右上角（移动端）/ 顶部导航栏右侧（桌面端）
- **形态**：下拉选择器（非固定按钮组），因为语言数量不确定，未来可能增加
- **默认显示**：当前语言的中文名称（如"中文"、"English"、"Tiếng Việt"）
- **下拉选项**：来自 API `GET /api/v1/app/i18n/languages` 返回的已启用语言列表
- **当前支持**：中文、英文（English）、越南语（Tiếng Việt）

### 交互规则
- 选择语言后即时切换页面所有 UI 文案（通过 `i18next.changeLanguage()`）
- 同时将选择持久化到 `localStorage`（key: `zhiyu-locale`）
- 刷新页面后自动恢复上次选择的语言
- 语言检测优先级：`localStorage` > `navigator.language` > 默认 `zh`
- 下拉选项中当前语言高亮显示

### 布局示意（登录页）
```
┌─────────────────────────────┐
│                    [中文 ▼] │  ← 语言下拉选择器
│                             │
│         LOGO / 品牌名        │
│                             │
│     ┌───────────────────┐   │
│     │ 邮箱               │   │
│     ├───────────────────┤   │
│     │ 密码               │   │
│     ├───────────────────┤   │
│     │     [登录]         │   │
│     └───────────────────┘   │
│     忘记密码?    Google登录   │
│     还没有账号？去注册        │
└─────────────────────────────┘
```

---

## 通用：UI 文案国际化规范（R-auth-018）

### 文案 key 映射表（auth 域）

| i18n Key | 中文源文案 | 使用页面 |
|----------|-----------|---------|
| `auth.login` | 登录 | P-001 |
| `auth.register` | 注册 | P-002 |
| `auth.email` | 邮箱 | P-001~003 |
| `auth.password` | 密码 | P-001~002 |
| `auth.confirm_password` | 确认密码 | P-002, P-004~005 |
| `auth.forgot_password` | 忘记密码？ | P-001 |
| `auth.reset_password` | 重置密码 | P-004 |
| `auth.change_password` | 修改密码 | P-005 |
| `auth.set_password` | 设置密码 | P-005 |
| `auth.new_password` | 新密码 | P-004~005 |
| `auth.old_password` | 旧密码 | P-005 |
| `auth.google_login` | Google 登录 | P-001~002 |
| `auth.no_account` | 还没有账号？ | P-001 |
| `auth.has_account` | 已有账号？ | P-002 |
| `auth.go_login` | 去登录 | P-002 |
| `auth.go_register` | 去注册 | P-001 |
| `auth.send_code` | 发送验证码 | P-002~003 |
| `auth.resend_code` | 重新发送 | P-002~003 |
| `auth.verification_code` | 验证码 | P-002~003 |
| `auth.logout` | 退出登录 | P-006 |
| `auth.logout_confirm` | 确定要退出登录吗？ | P-006 |
| `auth.settings` | 设置 | P-006 |
| `auth.password_management` | 密码管理 | P-006 |
| `auth.err_email_required` | 请输入邮箱 | P-001~003 |
| `auth.err_email_invalid` | 请输入有效的邮箱地址 | P-001~003 |
| `auth.err_password_required` | 请输入密码 | P-001 |
| `auth.err_password_weak` | 密码至少 8 位，包含字母和数字 | P-002, P-004~005 |
| `auth.err_password_mismatch` | 两次输入的密码不一致 | P-002, P-004~005 |
| `auth.err_password_same` | 新密码不能与旧密码相同 | P-005 |
| `auth.err_old_password_wrong` | 旧密码错误 | P-005 |
| `auth.err_credentials` | 邮箱或密码错误 | P-001 |
| `auth.err_credentials_count` | 邮箱或密码错误（已失败 {{count}}/5 次） | P-001 |
| `auth.err_locked` | 登录失败次数过多，账号已锁定 30 分钟 | P-001 |
| `auth.err_email_registered` | 该邮箱已注册，去登录 | P-002 |
| `auth.err_code_wrong` | 验证码错误 | P-002~003 |
| `auth.err_code_expired` | 验证码已过期，请重新发送 | P-002~003 |
| `auth.err_no_permission` | 无权限访问 | P-001 |
| `auth.password_reset_success` | 密码重置成功，请重新登录 | P-004 |
| `auth.password_change_success` | 密码修改成功 | P-005 |
| `auth.code_sent` | 验证码已发送到您的邮箱 | P-002~003 |
| `auth.code_resend_countdown` | {{seconds}} 秒后可重新发送 | P-002~003 |

### 规则
- 所有文案使用 `t('auth.xxx')` 引用，禁止硬编码
- 错误文案中使用 `{{count}}`、`{{seconds}}` 等 placeholder
- 所有 placeholder 在各语言翻译中必须保持一致

---

## P-app-auth-001 登录页

### 表单校验规则
| 字段 | 必填 | 校验规则 | 错误文案 (i18n key) |
|------|------|---------|---------|
| 邮箱 | 是 | 非空 + 邮箱格式 | 空：`auth.err_email_required`；格式错误：`auth.err_email_invalid` |
| 密码 | 是 | 非空 | `auth.err_password_required` |

### 登录失败分级提示
| 失败次数 | 错误文案 (i18n key) |
|---------|---------|
| 第 1-2 次 | `auth.err_credentials` |
| 第 3-5 次 | `auth.err_credentials_count` (placeholder: count) |
| 第 5 次后 | `auth.err_locked` |

### 键盘/a11y
- Tab：语言选择器→邮箱→密码→登录→忘记密码→Google→注册
- Enter 提交；触控 ≥ 44px

---

## P-app-auth-002 注册页

### 表单校验规则
| 字段 | 必填 | 校验规则 | 错误文案 (i18n key) |
|------|------|---------|---------|
| 邮箱 | 是 | 非空 + 邮箱格式 | 同登录页 |
| 密码 | 是 | ≥8 字符，含字母+数字 | `auth.err_password_weak` |
| 确认密码 | 是 | 与密码一致 | `auth.err_password_mismatch` |
| 邮箱验证码 | 是 | 6 位数字 | 错误：`auth.err_code_wrong`；过期：`auth.err_code_expired` |

### 后端校验
| 场景 | 错误文案 (i18n key) |
|------|---------|
| 邮箱已注册 | `auth.err_email_registered` |

### 键盘/a11y
- Tab：语言选择器→邮箱→密码→确认密码→注册→Google→去登录
- Enter 提交

---

## P-app-auth-003 忘记密码页

### 表单校验规则
| 字段 | 必填 | 校验规则 | 错误文案 (i18n key) |
|------|------|---------|---------|
| 邮箱 | 是 | 非空 + 邮箱格式 | 同登录页 |
| 验证码 | 是 | 6 位数字 | 错误：`auth.err_code_wrong`；过期：`auth.err_code_expired` |

### 键盘/a11y
- Tab：语言选择器→邮箱→发送→验证码→验证→重新发送
- Enter 提交

---

## P-app-auth-004 重置密码页

### 表单校验规则
| 字段 | 必填 | 校验规则 | 错误文案 (i18n key) |
|------|------|---------|---------|
| 新密码 | 是 | ≥8 字符，含字母+数字 | `auth.err_password_weak` |
| 确认密码 | 是 | 与新密码一致 | `auth.err_password_mismatch` |

### 键盘/a11y
- Tab：语言选择器→新密码→确认密码→确认重置
- Enter 提交

---

## P-app-auth-005 修改/设置密码页

### 角色差异
| 条件 | 表现 (i18n key) |
|------|------|
| 邮箱注册用户 | 显示旧密码字段，标题 `auth.change_password` |
| Google 登录用户 | 隐藏旧密码字段，标题 `auth.set_password` |

### 表单校验规则
| 字段 | 必填 | 校验规则 | 错误文案 (i18n key) |
|------|------|---------|---------|
| 旧密码 | 仅邮箱用户 | 非空 | 后端：`auth.err_old_password_wrong` |
| 新密码 | 是 | ≥8 字符，含字母+数字，≠旧密码 | 强度不足：`auth.err_password_weak`；相同：`auth.err_password_same` |
| 确认新密码 | 是 | 与新密码一致 | `auth.err_password_mismatch` |

### 键盘/a11y
- Enter 提交；触控 ≥ 44px

---

## P-app-auth-006 设置页

### 角色差异
无（仅 ROLE-USER）

### 语言设置
- 设置列表中包含「语言」选项，展示当前语言
- 点击后弹出语言选择器（与公开页面的下拉选择器数据源一致）
- 切换后即时生效

### 键盘/a11y
- 列表项 Tab 可达；退出登录需确认弹框（弹框文案使用 `auth.logout_confirm`）
