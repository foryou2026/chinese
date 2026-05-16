<!-- TARGET-PATH: docs/C05-prd/app-auth/app/01-overview.md -->

# 01 · 概述

## 1. 目标

让"知语"东南亚汉语学习平台具备完整的"账号生命周期"基础能力：注册、登入、保活、找回、改密码、改资料、退出。

## 2. 范围（v1）

- 注册：邮箱 + 密码 / Google OAuth
- 登入：邮箱 + 密码 / Google OAuth / refresh 续期
- 找回：忘记密码 → 邮件链接 → 重置
- 修改：资料（头像URL / 昵称 / 偏好语言）、密码
- 退出：本设备 / 全部设备

## 3. 不在范围

详 [C01 §3 范围外](../../C01-requirements/app-auth/baseline.md)。

## 4. 关键指标

| 指标 | 目标 |
|------|------|
| 注册到首次登入转化 | ≥ 60%（Google 渠道 ≥ 75%） |
| 登入接口 p95 时延 | < 800ms |
| 找回密码完成率 | ≥ 40% |
| 月活账号被禁用率 | < 0.5% |
| 多设备活跃比例（≥2 设备）| 跟踪即可，不设目标 |

## 5. 依赖

- 自托管 Supabase Auth（GoTrue v2.130+）
- 自建 Hook：`/internal/auth-hook`（before_user_created）
- 邮件：dev mock / prod SMTP（v2 接）
- Redis：节流计数（kv 后端）
