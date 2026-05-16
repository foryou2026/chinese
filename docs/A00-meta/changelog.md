<!-- TARGET-PATH: docs/A00-meta/changelog.md -->

# A00 · changelog · 跨阶段变更与冻结记录

> 本文件按时间倒序记录所有阶段产物的「冻结 / 变更 / 解冻」事件。
> F 层（B01~B04）变更必须列出受影响的所有已开工 feature，并触发它们的 D03 V 重跑。

---

## 2026-05-16 · 批次 3 · `app-auth` feature 全套反向回写

> 用户应用端「账号生命周期」feature 完整入坑：注册 / 登入 / OAuth / 找回 / 改密 / 改资料 / 退出 / 多设备 / 节流 / 禁用 / 链接过期。

| 阶段 | 产物 | 数量 | 状态 |
|------|------|------|------|
| C01 R | `docs/C01-requirements/app-auth/{_input, baseline, flows/main-flow, flows/exception-flow, 99-open-questions}` | 5 | 已冻结 |
| C02 I | `docs/C02-ia/app-auth/*` (00..07 + 99 + _input) | 10 | 已冻结 |
| C03 N | `docs/C03-pages/app-auth/P-app-app-auth-001..009 + P-001.scenarios + 99 + _input` | 12 | 已冻结 |
| C04 H | `docs/C04-prototype/app-auth/{README, _input}` | 2 | **占位** (与 B04-design/prototype-style 一致 deferred) |
| C05 E | `docs/C05-prd/app-auth/*` (00..12 + 99 + 06-page-specs/00-index + _input) | 17 | 已冻结 |
| D01 D | `docs/D01-data/app-auth/*` (00..08 + 99 + 02-entities×5 + _input) | 15 | 已冻结（无新增表，复用 B02-04 5 表）|
| D02 L | `docs/D02-api/app-auth/*` (00..06 + 99 + 03-endpoints×15 + _input) + `docs/D02-api/_global-routes.md`（首建）| 25 | 已冻结 |
| D03 V | `docs/D03-validation/app-auth/{01-upstream-chain, 02-module-closure, 03-prd-traceability}` | 3 | V01/V02/V03 全绿 |

**关键数字**：15 R-ID / 3 M 模块 / 11 Flow / 4 SM / 9 page-id / 15 接口 / 21 错误码 / 11 审计事件。
**关键边界**：本 feature **不**新增任何 PG 表；不涉及 admin 端（admin-auth 批次 4 落）；不涉及 onboarding（user-account v2）；C04 原型与 B04 prototype-style 同步 deferred。
**受影响 feature**：无（首次落 app-auth，不触发其它 feature 的 D03 重跑）。

---

## 2026-04-28 · F 层批量冻结（项目反向初始化）

> 本项目存量代码与 `grules/`、`function/` 既有规范已先于 `/prompt` 框架落地。
> 本次操作是「按 `/prompt` 框架反向重打包」：把既有事实重新切片到 `docs/B*/` 与 `docs/{C,D}*/` 之下，使框架成为唯一事实源。

| 阶段 | 文件 | 状态 | 来源 |
|------|------|------|------|
| B01 · A | `docs/B01-architecture/*` | 已冻结 | 由 `grules/G1-架构与技术规范/` 整体迁入 + 新增 `08-surfaces.md` / `09-auth-infra.md` |
| B02 · P | `docs/B02-permissions/*` | 已冻结 | 由 `grules/G3-权限与认证规范/` 迁入，剥离 `05-注册流程.md` → 留给 `<surface>-auth` feature |
| B03 · X | `docs/B03-ux/*` | 已冻结 | 反推：基于"东南亚汉语学习 + 毛玻璃 + 教育 + 游戏化"四组关键词整理 |
| B04 · S | `docs/B04-design/design-system/*` | 已冻结 | 由 `grules/G2-视觉与交互风格/` 迁入；`prototype-style/` 资产留待 C04 首次原型时补齐 |

**受影响 feature**：`discover-china`、`course`（两个均已落 D02 之前的全部产物，本次 F 冻结不要求其重跑 D03，因为它们的存量产物本身就是 F 现状的依据；后续若 F 再变更，按通常规则触发）。

---

## 2026-04-28 · C/D 阶段批量冻结（反向初始化）

| feature | 阶段 | 状态 | 来源 |
|---------|------|------|------|
| `discover-china` | C01 R ~ D02 L | 已冻结 | 由 `function/01-china/{prd,ai}/` 整体迁入并按多端切分（`app` / `admin`）|
| `discover-china` | D03 V | 已冻结（V01/V02/V03 全绿）| 反向校验 |
| `course` | C01 R ~ D02 L | 已冻结 | 由 `function/02-course/{prd,ai}/` 整体迁入并按多端切分 |
| `course` | C04 H | 已冻结 · 含原型 | 由 `function/02-course/ai/F4-AI-原型设计/` 迁入 `docs/C04-prototype/course/<surface>/` |
| `course` | D03 V | 已冻结（V01/V02/V03 全绿）| 反向校验 |

---

## 2026-04-28 · F 层批次 2 补齐 + B01-09 对齐

- **B04 设计系统**：补齐 `docs/B04-design/design-system/` 全套 10 文件（`_input/visual-input.md` / `00-index` / `01-tokens` / `02-layout` / `03-navigation` / `04-status-components` / `05-interactions` / `06-responsive-dark` / `07-icons-imagery` / `99-open-questions`）；与 `grules/G2-视觉与交互风格/` 内容一致并新增 `07-icons-imagery.md`（grules 缺失）。
- **B04 原型样式骨架**：建立 `docs/B04-design/prototype-style/` 占位（`README.md` / `tokens.css` / `themes.css` / `app.css` / `app.js`），约定待 C04 首次产出 HTML 原型时填充；与 `system/packages/ui-kit/src/tokens/` 是同一份内容的两种载体。
- **B01-09-auth-infra 与 B02 对齐**：将残留的多角色 `roles[]` / `requireRole('admin_*')` / 前端登出清 `localStorage` 等措辞，统一改为单数 `role` / `requireRole('super_admin')` / 调 `POST /v1/auth/logout` 清 HttpOnly Cookie；增加交叉引用到 [`B02-permissions/02-auth-flow.md`](../B02-permissions/02-auth-flow.md)。
- **受影响 feature**：`discover-china`、`course`——本次 B01 修正限于鉴权中间件描述，未触及它们既有 D02 L 的契约（错误码 / Cookie 名称 / 角色枚举均一致），不要求 D03 V 重跑。

---

## 变更约定

- 任何已冻结文件需修改前：在文件头把 `冻结状态` 改为 `变更中`，新开对话让 AI 先出 diff 报告，再改。
- F 层变更广播：B01~B04 任一文件变更，须在本文件追加一行"受影响 feature 列表"，并触发它们的 D03 V 重跑。
- 解冻 / 重冻 都要在本文件追加一行（YYYY-MM-DD · 文件 · 操作 · 签字）。
