<!-- TARGET-PATH: docs/C01-requirements/auth/admin/notes.md -->

# `auth` · admin 端补充说明

> 本文件记录 admin surface 在 `auth` feature 上相对 app 的差异。不重复 `baseline.md`，只列差异。

---

## 1. 无自助注册

- admin 端不开放注册入口；账号统一由运维通过 seed 流程创建。

## 2. 登录身份双重校验

- 在密码校验通过后立即校验"管理员身份"；非管理员被立即登出并提示"请使用用户入口登录"。
- 该判定失败动作必须进入审计。

## 3. 关键动作 100% 审计

- 登录成功 / 登录失败、改密、退出（本设备 / 全部设备）必须全部进入审计记录。
- 审计禁止记录明文密码、长效令牌等敏感内容。

## 4. 不开放 OAuth

- admin 端只走邮箱 + 密码，不接入 Google 等第三方登录。

## 5. 设备上限独立

- admin 端的活跃会话上限 3 台与 app 端独立计数；互不影响。

## 6. 无个人资料维护

- admin 端不展示头像 / 显示名编辑入口；仅含"修改密码 / 退出"。

## 7. 浏览器存储规范

- 严禁在 `localStorage` / `sessionStorage` 等本地存储中保留任何长效凭据。
- 长效凭据只通过 HttpOnly Cookie 维持。
