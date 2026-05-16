<!-- TARGET-PATH: docs/C03-ia/auth/_shared/state-machines.md -->

# auth · `_shared/state-machines.md` · 跨端共享状态机索引

> **作用**：列出 auth feature 中**所有 surface 共享**的状态机；端独有的状态机仍保留在各自 `app/03-state-machines.md` / `admin/03-state-machines.md`。
> **冻结**：2026-05-17（批次 16 多端合并）

---

## 1. 共享状态机一览

| 状态机 ID | 名称 | 端 | 详情位置 |
|----------|------|----|---------|
| `SM-auth-shared-01` | session 生命周期（cookie 颁发 / 续签 / 撤销） | app + admin | 本文件 §2 |
| `SM-auth-shared-02` | CSRF token（双提交） | app + admin | 本文件 §3 |
| `SM-auth-shared-03` | 设备名册（3 设备硬上限） | app + admin（按 会话记录` 独立计数） | 本文件 §4 |
| `SM-auth-shared-04` | 锁定 / 禁用（5 错锁 15min / 用户档案=false`） | app + admin | 本文件 §5 |

> 端独有状态机（`SM-auth-app-NN` / `SM-auth-admin-NN`）查询各自端的 `03-state-machines.md`。

---

## 2. `SM-auth-shared-01` · session 生命周期

```text
[anonymous] --login_ok--> [active]
[active] --idle≥30min--> [expiring] --refresh_ok--> [active]
[active] --idle≥7d--> [expired]
[active] --explicit_logout--> [revoked]
[active] --global_logout--> [revoked × N]
[active] --kicked_by_4th_device--> [revoked]
[active] --disable_account--> [revoked × all_user]
```

- cookie：`access_token`（30min jwt）+ `refresh_token`（7d，rotation）
- 存储：cookies = `HttpOnly; Secure; SameSite=Lax; Path=/`
- 服务端登记：会话记录(id, user_id, surface, device_label, created_at, last_seen_at, revoked_at)`
- 跨端不共享 cookie name（app 用 `sb-access`、admin 用 `sb-admin-access`）

## 3. `SM-auth-shared-02` · CSRF 双提交

```text
[anonymous] --GET /any --> [issued]   // 写入 csrf cookie + meta
[issued] --POST with X-CSRF-Token header--> [valid] | [rejected]
[rejected] --new GET--> [issued]
```

- header 必须与 cookie `csrf` 值字节级相等
- 仅状态变更接口（POST/PUT/PATCH/DELETE）校验
- OAuth callback / 鉴权与数据底座 webhook 走签名校验，**不**走 CSRF

## 4. `SM-auth-shared-03` · 设备名册（按端独立计数）

```text
device_count(user_id, surface) ≤ 3
```

- 第 4 台登入 → 找 `last_seen_at` 最早一台 revoke → 写入新 session
- 被踢端下次心跳 → 进入 `[revoked]` → 客户端清 cookie 跳登录页（payload `kicked_at_<ts>`）

## 5. `SM-auth-shared-04` · 锁定 / 禁用

```text
失败次数(user_id, ip, 15min窗口) ≥ 5 --> [locked 15min]
[locked] --15min超时--> [normal]
profiles.启用态 = false --> [globally revoked]
[globally revoked] --管理员置 启用态=true--> [normal]
```

- 计数表：`auth_failed_attempts(user_id, ip, ts)`，TTL 60min
- 锁定不区分 surface：admin 错锁也连带 app 端

---

## 99. 上游引用

- [C02-permissions/02-authz-mechanism.md](../../../C02-permissions/02-authz-mechanism.md)
- [B01-architecture/09-auth-infra.md](../../../B01-architecture/09-auth-infra.md)
- [C01-requirements/auth/baseline.md](../../../C01-requirements/auth/baseline.md) R-auth-003 ~ R-auth-010
