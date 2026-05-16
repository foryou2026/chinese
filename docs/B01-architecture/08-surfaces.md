<!-- TARGET-PATH: docs/B01-architecture/08-surfaces.md -->

# 08 · 应用端（surface）清单与跨端隔离策略

> **阶段**：B01-A 架构  
> **角色**：架构师  
> **feature**：全局  
> **上游依赖**：`_input/preferences.md`、`A-questions-round1-resolved.md Q5`  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：B02 角色×surface 矩阵、所有 feature 的 C/D 目录形态、`docs/C05-prd/_global-index.md`

---

## 0. 摘要

- **本项目 = 多端项目**：surface 数 = **2**（`app` + `admin`）。
- 所有 feature 的 C03 / C04 / C05 / D02 阶段产物**必须**按 `<surface>/` 拆子目录；C01 R baseline、C02 I `_shared/state-machines.md`、D01 D 表结构跨端共享。
- 路由前缀强制：`/api/app/*`（应用端，对外别名 `/api/v1`）、`/api/admin/*`（后台，对外别名 `/admin/v1`）。
- 鉴权基础设施共享（详见 [09-auth-infra.md](./09-auth-infra.md)）；登录 / 注册 / 找回密码等具体流程留给未来的 `auth` / `auth` feature。

---

## 1. surface 清单

| surface ID | 角色面向 | 前端应用 | 后端应用 | 端口（fe / be）| 路由前缀 | 备注 |
|-----------|---------|---------|---------|--------------|---------|------|
| `app` | 学习者（C 端）| `system/apps/web-app` | `system/apps/api-app` | 3100 / 8100 | `/api/v1`（≡ `/api/app/v1`）| 移动优先；纯 CSR/SPA；游戏化页面 |
| `admin` | 内容运营、客服、AI 训练师 | `system/apps/web-admin` | `system/apps/api-admin` | 4100 / 9100 | `/admin/v1`（≡ `/api/admin/v1`）| 桌面优先；表格 / 富文本编辑 |

> **未来扩展**：若新增 `merchant`（B 端商户）或 `open`（开放平台），需先更新本文件 + B02 角色矩阵 + 加 D03 V 重跑所有已开工 feature。

---

## 2. 跨端隔离策略

### 2.1 强一致 → 共享层（`_shared/`）

跨端必须一致的内容沉淀到 feature 的 `_shared/` 子目录，作为单一真相：

| 共享层文件 | 含义 |
|-----------|------|
| `docs/C01-requirements/<feature>/baseline.md` | feature 级业务意图整体（**仍单份**，不拆 surface）|
| `docs/C02-ia/<feature>/_shared/state-machines.md` | 状态机集中（跨端必须一致）|
| `docs/C02-ia/<feature>/_shared/flows-shared.md` | 跨端共享业务流程（如 admin 改价 → app 看到改价）|
| `docs/C05-prd/<feature>/_shared/business-rules.md` | 跨端业务规则 |
| `docs/C05-prd/<feature>/_shared/glossary.md` | feature 局部术语（跨端用）|
| `docs/D01-data/<feature>/*` | 数据模型是单一真相，**全量共享**，不拆 surface |

### 2.2 端特定 → `<surface>/` 子目录

每端独立，按 surface 拆：

| 端特定文件 | 含义 |
|-----------|------|
| `docs/C02-ia/<feature>/<surface>/01-feature-catalog.md` | 端内功能清单 |
| `docs/C02-ia/<feature>/<surface>/02-flows.md` | 端特定流程图 |
| `docs/C02-ia/<feature>/<surface>/04-pages.md` | 端内页面清单 |
| `docs/C02-ia/<feature>/<surface>/05-navigation.md` | 端导航 |
| `docs/C02-ia/<feature>/<surface>/06-coverage-matrix.md` | R-ID × 页面覆盖矩阵 |
| `docs/C03-pages/<feature>/<surface>/<page-id>.md` | 单页交互（含 4 态 + 角色可见性）|
| `docs/C04-prototype/<feature>/<surface>/...` | 原型（每端独立 index.html + vendor）|
| `docs/C05-prd/<feature>/<surface>/...` | 端 PRD（overview + page-specs + design-summary）|
| `docs/D02-api/<feature>/<surface>/...` | 端路由 + 接口（强制 `/api/<surface>/*` 前缀）|

### 2.3 跨端联动

- admin 改价同步 app 学员看到 → 真相位于 `_shared/state-machines.md` 中对应 SM 的状态转移；
- admin 与 app 各自的 D02 路由调用同一份 D01 表 / 同一组 RPC 函数；
- 跨端引用必须先沉淀到 `_shared/`，不允许 surface A 直接引用 surface B 的端特定产物。

---

## 3. page-id 命名

- 多端项目强制 `P-<surface>-<feature>-<seq3>`，例：
  - `P-app-discover-china-001`（应用端"发现中国"首页）
  - `P-admin-course-014`（管理后台课程编辑页）
- C04 原型 HTML 文件名 = `<scope>-<page>.html`，scope 取 surface（`app` / `admin`）+ 可选业务子域。

---

## 4. 路由前缀强制

| 表现层 | 内部前缀 | 对外别名（保持 RESTful 习惯）|
|-------|---------|---------------------------|
| 应用端 | `/api/app/v1/*` | `/api/v1/*` |
| 管理后台 | `/api/admin/v1/*` | `/admin/v1/*` |

> 后端实现：Hono 子 app `app.route('/v1', ...)`；网关层（生产 Nginx）按域名 / 路径转发。dev 环境直接 `IP:端口` 走 `/api/v1` 或 `/admin/v1`。

---

## 5. 鉴权与 auth feature 提示

- **B02 不定**任何登录 / 注册 / 找回密码 / 邮箱验证流程。
- 鉴权按 **单一 feature 多端形态** 组织（遵循 `prompt/A-framework/A00-04 §四.5`）：
  - feature ID：`auth`
  - 目录形态：`C01-requirements/auth/{baseline.md, app/notes.md, admin/notes.md, flows/, ...}` · `C02-ia/auth/{_shared/, app/, admin/}` · 其余 C03/C04/C05 同样按 `auth/<surface>/` 拆分
  - 业务范围：
    - `auth` (surface=`app`) → 学员账号体系（邮箱 + 密码 + Google OAuth；本期 mock SMTP）
    - `auth` (surface=`admin`) → 后台账号体系（仅邮密；邀请制，超管 seed）
- 共享的鉴权基础设施（Token 规格、密码策略、会话管理、OAuth provider 接入位）由 [09-auth-infra.md](./09-auth-infra.md) 定义；后续 C 阶段全部从此处取「基线行为」，差异由各 surface 的 `notes.md` 收敛。
- 上下层 surface 在 `user_sessions.surface` 维度独立计数（3-设备硬上限按端隔离）。

---

## 6. 单文件夹原型资产引用

按多端约定，**每个 surface 在 C04 阶段拥有独立目录**；运行时 CSS / JS 资产**统一通过相对路径直接引用 [`docs/B04-design/prototype-style/`](../B04-design/prototype-style/)**（严禁在 feature 目录下拷贝）：

```
docs/C04-prototype/<feature>/
├── _input/prototype-direction.md
├── app/
│   ├── index.html        ← 引用 ../../../B04-design/prototype-style/X
│   └── pages/, states/, mock-data.js, feature.css, feature.js
└── admin/
    ├── index.html
    └── pages/, states/, ...   ← pages/*.html 引用 ../../../../B04-design/prototype-style/X
```

例外：feature 若在 `/function/<feature>/ai/F4-AI-原型设计/` 存在上游 AI 原型（如 `course`），则改为引用上游 `_assets/`（同样不得拷贝）。

---

## 99. 待确认问题
（无）
