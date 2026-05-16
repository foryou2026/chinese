<!-- TARGET-PATH: docs/A00-meta/changelog.md -->

# A00 · changelog · 跨阶段变更与冻结记录

> 本文件按时间倒序记录所有阶段产物的「冻结 / 变更 / 解冻」事件。
> F 层（B01~B04）变更必须列出受影响的所有已开工 feature，并触发它们的 D03 V 重跑。

---

## 2026-05-17 · 批次 15 · Round 8 · /prompt 模板去 auth 特殊化 + 去分期化（推翻批次 14 的 auth 决策）

> **触发原因**：用户指出 [prompt/A-framework/A00-04-文档目录规划.md](../../prompt/A-framework/A00-04-文档目录规划.md) 与 [prompt/A-framework/A00-01-框架总览.md](../../prompt/A-framework/A00-01-框架总览.md) 把 auth 强行规定为「每个 surface 必须独立 `<surface>-auth` feature」是错误的——auth 与「商品」「订单」「发现中国」一样只是一个普通 feature，**很多软件根本不需要登录**；多端规则应统一为 `<feature>/<surface>/`，不允许任何 feature 被特殊命名。同时用户拒绝模板里出现「本期 / 二期 / 分期 / P0 / P1 / P2 / 显式排除」——「所有出现的内容都是要做的，不要搞任何分期」。模板是给陌生人通用复用的，必须彻底通用化。

### 15-1 · A 框架去 auth 特殊化

- [prompt/A-framework/A00-04-文档目录规划.md](../../prompt/A-framework/A00-04-文档目录规划.md)
  - 删除「auth feature 在多端项目里的形态」整段（旧 L278-289 的 `<surface>-auth` 强制命名规则）
  - 改写为通用「feature 命名通用约定」段：所有 feature kebab-case 业务语义，无任何前缀强制；如有 auth 类需求按 `<feature>/<surface>/` 走多端形态，命名建议 `auth`
  - 标记 `09-auth-infra.md` 为可选（仅当项目有登录类需求才填实）
  - 标记 `03-authz-data-model.md` 为可选；新增「不预设登录」原则
- [prompt/A-framework/A00-01-框架总览.md](../../prompt/A-framework/A00-01-框架总览.md)
  - 旧「『登录』不是全局事 + 每 surface `<surface>-auth`」段 → 改写为「所有 feature 平等对待」原则：auth 是普通 feature，命名 kebab-case，无前缀强制；不需要登录的项目则该 feature 不存在
  - B02 责任行去掉 `<surface>-auth` 括号
- [prompt/A-framework/A00-02-端到端工作流.md](../../prompt/A-framework/A00-02-端到端工作流.md)
  - 工作流清单删「必须包含各 `<surface>-auth` feature」
  - 09-auth-infra 标为可选
- [prompt/A-framework/A00-03-通用约定.md](../../prompt/A-framework/A00-03-通用约定.md)
  - 命名约定表删除「auth feature ID `<surface>-auth`」整行
  - feature ID 行加注「所有 feature 平等，无任何前缀强制」

### 15-2 · B01/B02 去 auth 特殊化

- [prompt/B-foundation/B01-A01-用户输入-技术偏好.md](../../prompt/B-foundation/B01-A01-用户输入-技术偏好.md)
  - surface 表删「是否本期上线」列；删 merchant/open「二期」示例行；加禁令「永不设置『是否本期上线』『二期』之类的列」
  - `09-auth-infra` 段加「仅当项目有登录类需求时填实」注；feature 例从 `auth/auth` 改为 `auth`
  - 第三方 mock 示例把「本期 mock」改为「当前 mock」
- [prompt/B-foundation/B01-A03-AI输出-架构规范.md](../../prompt/B-foundation/B01-A03-AI输出-架构规范.md)
  - 08-surfaces 模板表删「是否本期上线」列；删 merchant 二期行；加禁令
  - 4「surface × auth feature 矩阵」→ 改为「surface × auth 映射（可选）」，要求统一用 `auth` feature 名，禁造 `<surface>-auth`
  - 09-auth-infra：加「项目无登录则整文件 N/A」；OAuth 表「本期 mock」列改「接入模式」；§5 「§3 中标记为本期的 provider」→「§3 中列出的所有 provider」
- [prompt/B-foundation/B02-P01-用户输入-角色描述.md](../../prompt/B-foundation/B02-P01-用户输入-角色描述.md) 重写顶部「登录不是全局事」段：auth 是普通 feature；项目无登录需求时整类不存在
- [prompt/B-foundation/B02-P02-AI澄清-权限提问.md](../../prompt/B-foundation/B02-P02-AI澄清-权限提问.md) 数据合规问题「本期需要满足的法规」→「项目需要满足的法规」
- [prompt/B-foundation/B02-P03-AI输出-权限规范.md](../../prompt/B-foundation/B02-P03-AI输出-权限规范.md) 04-auth-feature-guideline 整文件改写：标题去 `<surface>-auth`、明确「**作为一个普通 feature**，推荐 id `auth`，不要造 `<surface>-auth`」；输出位置示例统一 `auth/<surface>/`；校验项的单/多端路由分流；整文件改为「仅当项目存在登录交互时输出」

### 15-3 · C01 去分期 + 删显式排除

- [prompt/C-product/C01-R01-用户输入-需求初稿.md](../../prompt/C-product/C01-R01-用户输入-需求初稿.md)
  - **删除 §10「显式排除（本期不做的）」整段**（用户直接 quote 的反面教材）
  - **删除 §12「时间与里程碑（本期硬截止）」整段**
  - 「本期版本」→「版本号」；§9 mock 改「需 mock 的」；feature ID 例子去掉「auth 形如 auth/auth」；§0 type 选项删 auth feature 单选项
- [prompt/C-product/C01-R03-AI输出-需求基线.md](../../prompt/C-product/C01-R03-AI输出-需求基线.md)
  - §0 摘要从 5 行改 4 行，删「本期范围 / 不做什么」
  - **删除原 §2「范围与排除（白名单/黑名单）」整段**，替换为「暗依赖警示」+ 明示「永不出现 P0/P1/P2/本期/二期/MoSCoW」
  - **R-ID 表删除「优先级」列**；删除 P0/P1/P2 图例
  - §7 集成表「本期模式」→「接入模式」

### 15-4 · C04 原型去 P0/P1/P2 优先级

- [prompt/C-product/C04-H01-用户输入-原型方向.md](../../prompt/C-product/C04-H01-用户输入-原型方向.md)
  - §3 表**删除「优先级」列**；所有页面统一「默认+加载+空+错」4 态；警句改为「没有 P0/P1/P2/优先级/待定/二期 这种说法」
  - §10 验收「P0 页面 4 状态截图齐全」→「所有进表页面 4 状态截图齐全」
- [prompt/C-product/C04-H02-AI澄清-原型提问.md](../../prompt/C-product/C04-H02-AI澄清-原型提问.md) 禁问列表加「是否分优先级」；维度 11 P0/P1 改「所有进表页面」；自检项同步
- [prompt/C-product/C04-H03-AI输出-HTML原型规范.md](../../prompt/C-product/C04-H03-AI输出-HTML原型规范.md) 「P0 页面必须出 4 态」→「每个进表页面必须出 4 态」；禁止跳过理由加「优先级低」；changelog 模板去「不分期」括注；自检项同步

### 15-5 · 保留的原则性引用（**不删**）

下列表达虽然出现 P0/P1/P2/本期/二期 字样，但属于「禁止规则」本身，保留以强化原则：

- `prompt/C-product/C04-H01-...md` L78「没有 P0/P1/P2 / 优先级 / 待定 / 二期 这种说法」
- `prompt/B-foundation/B01-A01-...md` L68「永不设置『是否本期上线』『二期』这种列」
- `prompt/C-product/C01-R03-...md` L80「永不出现 P0 / P1 / P2 / 本期 / 二期 / MoSCoW」
- `prompt/C-product/C04-H02-...md` L75 自检「没出现『是否分期 / 本期是否只做一部分 / 二期再做』这类问题」
- `prompt/C-product/C04-H03-...md` L24/L76 禁跳过理由列表
- `prompt/B-foundation/B01-A03-...md` L355 同上
- `prompt/B-foundation/B03-X01-...md` L139「不允许『二期再做』」
- `prompt/B-foundation/B03-X03-...md` L221-229 P1/P2 是体验原则编号（非分期）—— 保留
- `prompt/B-foundation/B02-P03-...md` 角色「优先级」列（冲突时取最高，技术机制）—— 保留
- `prompt/C-product/C03-N02-...md` L22「首屏优先级」（视觉布局优先级）—— 保留

### 15-6 · docs/ 既有结构未动 · 待用户裁决

`docs/C0[1-5]-*` 当前已有 `auth/` 与 `auth/` 两个独立 feature 目录（来自 Round 6-7 按旧 prompt 产出）。模板已通用化，建议改为单一 `auth/<surface>/` 结构以匹配新模板，但**未执行**——涉及大量目录重命名 + 跨文件引用更新，待用户明确指示后单独跑一轮迁移。

### 15-7 · 影响范围

- F 层（B01~B04 模板）变更：**所有未来生成的 docs/** 适用；既有 docs/B01-B04 已落盘内容不受影响
- C01/C04 模板变更：**所有未来生成的 C01-R03 / C04-H01/H02/H03 文件**适用；既有文件不受影响（除非选择批量重生）
- 既有 `docs/{C01..C05,D01..D03}-*/auth/` 与 `auth/` 目录**保持现状**，等用户决策是否迁移

---

## 2026-05-16 · 批次 14 · Round 7 · auth 命名澄清 + C05 非 auth feature 8 文件实质化

### 7-0 · auth 命名澄清(无文件改动)

用户提出"为什么是 `auth/auth`,不应该是 `auth/{app,admin}` 吗?",经核 [prompt/A-framework/A00-04-文档目录规划.md §四 "auth feature 在多端项目里的形态"](../../prompt/A-framework/A00-04-文档目录规划.md):

> 每个 surface 必须有自己的 `<surface>-auth` feature ... auth feature 的 `<surface>` 子目录通常等于 feature 名前缀(`auth` 只在 `app/` 下出产物),属于退化的"单端形态"。

prompt **明确规定** auth 与 auth 是两个独立 feature(各退化为单 surface),原因是两者鉴权链路完全不共享(cookie 域 / Supabase project / session 各自隔离,见 [`_glossary.md §B/E`](../C05-prd/_glossary.md))。**当前 [docs/C05-prd/auth/app/](../C05-prd/auth/app/) + [docs/C05-prd/auth/admin/](../C05-prd/auth/admin/) 结构完全合规,不修改;prompt 也不需要改。**

### 7-1 · course + discover-china 4 surface × 8 = 32 文件实质化

将 [course/{app,admin}](../C05-prd/course/) + [discover-china/{app,admin}](../C05-prd/discover-china/) 的 `01-overview` / `02-glossary` / `03-personas` / `05-user-journeys` / `09-design-summary` / `10-known-issues` / `11-roadmap` / `12-changelog` 共 32 文件从 Round 2 的 7-19 行骨架 **重写为 30-80 行实质内容**,严格对齐数据源:

| Feature/surface | 主要数据源 | 实质化要点 |
|----------------|-----------|----------|
| `course/app` | [`function/02-course/prd/00-总览与设计原则.md`](../../function/02-course/prd/00-总览与设计原则.md) | 4 业务主题(EC/FC/HSK/DL)+ share 共享层;7 类 KP × 12 题型;SM-2 Leitner;不练口语发音;2025-11 撤"系统内生成工作台"+ 试抽 |
| `course/admin` | [`function/02-course/prd/04-管理端模块设计.md`](../../function/02-course/prd/04-管理端模块设计.md) | 9 模块清单;`content_admin/super/readonly` × 9 模块矩阵;5L 完整发布闸门;> 30 天撤回 super 审批;不做 AI 翻译/自动生成 |
| `discover-china/app` | [`function/01-china/prd/F1-用户-数据与业务规则.md`](../../function/01-china/prd/F1-用户-数据与业务规则.md) | **12 个固定类目明细列出**(编码 01~12,5 语命名);文章 12 位 / 句子 4 位 0001 起;三层对照(汉字 + 拼音 + 5 语);句级 TTS,不连播 |
| `discover-china/admin` | [`function/01-china/prd/F1`](../../function/01-china/prd/F1-用户-数据与业务规则.md) + `F2` | 4 大页;`super` 全权(无 `content_admin` 分权);类目数 12 永不增删;5L 完整闸门;TTS 文件名 `NNNN.mp3` 匹配规则;索引重建禁与发布并发 |

### 7-1 · auth 4 surface(auth/app, auth/admin)状态

Round 3 已实质化(36-52 行);本轮 **不重写**,只在 Round 7 changelog 中确认状态不变。auth feature 8 文件实质化达标。

### Round 8+ 规划

- C04 `feature.css` / `feature.js` / `mock-data.js` 真正写入(目前仅框架;mock-data 以 C03 数据契约展开)
- C03 与 [`system/apps/api-*/src/routes/`](../../system/apps/) 既有路由对齐抽查
- C05 业务规则与 [`function/02-course/prd/01-04`](../../function/02-course/prd/) 字字对齐抽查
- 国际化字符 / 暗色模式在各 page-spec 截图占位补真实截图(依赖 C04 prototype 跑起来)

---

## 2026-05-16 · 批次 13 · 删除 D 阶段 + C 阶段合规对齐 + Round 6 主体(C05 page-spec 展开)

> 用户明确指令:文档体系仅保留到 C 阶段;先确保 C 阶段完全符合 [prompt/A-framework/A00-04-文档目录规划.md](../../prompt/A-framework/A00-04-文档目录规划.md),完全符合 [function/](../../function/) 与 [system/](../../system/) 既有事实,然后继续 Round 6。

### Round 6-0 · 删除 D 阶段(不可逆)

| 目录 | 状态 |
|------|------|
| [`docs/D01-data/`](../D01-data/) | **rm -rf 已删除**(Round 5 产出 D01-D03 全部撤回) |
| `docs/D02-api/` | **rm -rf 已删除** |
| `docs/D03-validation/` | **rm -rf 已删除** |

后续编码阶段直接以 [function/01-china/ai/F1-F3](../../function/01-china/ai/)、[function/02-course/ai/F1-F4](../../function/02-course/ai/) 与 [system/](../../system/) 既有 monorepo 骨架为源,**不**再走 D 阶段中间产物。

### Round 6-0 · 结构合规修正(对齐 [A00-04 §四.5 / §五](../../prompt/A-framework/A00-04-文档目录规划.md))

| 修正项 | 处理 | 数量 |
|--------|------|------|
| `C04-prototype/discover-china/{assets,vendor}` 根级残留(规范要求仅在 `<surface>/`) | `rm -rf` 已删 | 2 |
| C02 / C03 / C04 各 surface 缺 `00-index.md` | 补建(框架式,指向本目录内文件 + 上下游链接) | **16** |
| 全部 24 surface 缺 `99-open-questions.md` | 补建(空模板 + Q-ID 命名约定) | **24** |
| [`C05-prd/_global-index.md`](../C05-prd/_global-index.md) 缺 | 创建:4 feature 状态总表 + 业务域映射 `/function/`) | 1 |
| [`C05-prd/_glossary.md`](../C05-prd/_glossary.md) 缺 | 创建:平台 / 角色 / 标识符 / 5 语 / 路由前缀 / 主要业务术语 6 节,显式引用 `function/02-course/prd/01-04` 来源 | 1 |

### Round 6-1 · C05 单页规格(`06-page-specs/<page-id>.md`)全量展开

| Feature / Surface | page-id 数 | 状态 |
|-------------------|:--:|------|
| [`course/app`](../C05-prd/course/app/06-page-specs/00-index.md) | 8 | ✓ |
| [`course/admin`](../C05-prd/course/admin/06-page-specs/00-index.md) | 9 | ✓ |
| [`discover-china/app`](../C05-prd/discover-china/app/06-page-specs/00-index.md) | 3 | ✓ |
| [`discover-china/admin`](../C05-prd/discover-china/admin/06-page-specs/00-index.md) | 4 | ✓ |
| [`auth/app`](../C05-prd/auth/app/06-page-specs/00-index.md) | 9 | ✓ |
| [`auth/admin`](../C05-prd/auth/admin/06-page-specs/00-index.md) | 4 | ✓ |

每个 page-spec 文件结构(9 段):标识 / 上游来源(C03 / C04 / C02 链接) / 一句话价值 / 主交互摘要(≤5 行) / 关键 R-ID / 数据接口边界(留待编码期回填,不再依赖 D) / 视觉与组件(引 [`B04-design/05-components/`](../B04-design/design-system/05-components/)) / 截图占位 / 变更。

**本批次共写入文件:** D 删 3 目录 + C 整改 44 文件 + 06-page-specs 37 page-spec + 6 个 06-page-specs/00-index = **43 文件 + 删 3 目录 + 2 根残留**。

### 数据源核对(用户要求"完全符合已有内容")

| feature | 数据源 | 当前 C 阶段对齐 |
|---------|--------|---------------|
| `course` | [function/02-course/prd/01..07](../../function/02-course/prd/) + ai/F1-F4 | C05 _glossary 显式引用 01/02 来源;page-spec 链回 C03 / C04;**业务规则文本是否字字对齐待 Round 7 抽查** |
| `discover-china` | [function/01-china/prd/F1-F3](../../function/01-china/prd/) + ai/F1-F3 | 同上 |
| `auth` / `auth` | 规范派生 + [G3 权限规范](../../grules/G3-权限与认证规范/) | C 阶段已显式声明无 `/function/` 入口;由 B02 + G3 推导 |

| 代码骨架 | 当前 C 阶段约束 |
|---------|----------------|
| [`system/apps/{web-app, web-admin, api-app, api-admin}/`](../../system/apps/) | C03 / C04 路由 / 组件不与 ui-kit 冲突;**Round 7 抽查实际 routes** |
| [`system/packages/{ui-kit, shared-schemas, shared-i18n, ...}/`](../../system/packages/) | page-spec §7 视觉组件统一引 B04-design |

### Round 6 之后待办(Round 7 候选,**未启动**)

- C05 其余 `01-overview` / `02-glossary` / `03-personas` / `05-user-journeys` / `09-design-summary` / `10-known-issues` / `11-roadmap` / `12-changelog` 按端实质化(48 文件)
- C04 各 surface `feature.css` / `feature.js` / `mock-data.js` 真正写入(目前为框架)
- C02 auth feature 文件内容补强
- 与 [function/02-course/prd/](../../function/02-course/prd/) 字字对齐抽查 + 与 [system/apps/api-*/src/routes/](../../system/apps/) 既有路由对齐

---

## 2026-05-16 · 批次 12 · 各 surface 文档按端过滤(Round 5)

> 在 Round 1-4 的"物理拆分 + B04 组件库实质化"之上,完成各端文档的实质化按端过滤,使 C02 / D02 / C05 / D03 不再是"根级拷贝 + surface banner",而是真正反映该端独有的页面 / 接口 / 业务规则 / 角色矩阵 / 校验链路。

### Round 5 · 处理范围

| 阶段 | 范围 | 文件数 | 处理 |
|-----|------|-------|------|
| **R5-A3 · D02 路由按端裁剪** | 4 feature × 2 surface(auth 各 1)= 6 surface × {01-routes-delta + 02-overview} | **8 文件** | 重写:仅保留该端真实路由前缀(`/api/{surface}/v1/*` + 别名)与该端 OP 文件索引;新增鉴权矩阵 / 限流表 / 错误码字典分端版本 |
| **R5-A2 · C02 IA 按端过滤** | course + discover-china 各 2 surface × {01,02,04,05,06} | **20 文件** | 重写:M-ID 清单仅留本端模块 + 标注"不在本端"清单;流程仅描述本端触发;P-ID 路由表分端;覆盖矩阵纯本端 |
| **R5-A4 · C05 PRD 关键字段按端过滤** | 6 surface × {04-feature-catalog, 07-business-rules, 08-roles-permissions} | **18 文件** | MoSCoW 仅列本端模块;业务规则仅写本端可观察 R-*;角色矩阵分别给出 RLS(app)/ scope+审计(admin) |
| **R5-C · D03 校验链路重写** | 6 surface × {01-upstream-chain, 02-module-closure, 03-prd-traceability} | **18 文件** | 基于 Round 3 + Round 4 后的真实依赖图;新增"组件引用是否指向 [05-components/](../B04-design/design-system/05-components/) 而非旧 04-status-components.md"检查项;新增 Round 4 PR D 回链确认段 |

**总计本轮:64 文件**

### 关键检查项(Round 4 → Round 5 闭环)

1. **F 层组件引用复查**:[D03-V03 · PRD 回链校验](../D03-validation/) 各 surface §4 已加入新检查项;本端 C03 / C04 引用旧 `04-status-components.md` 的残留全部已澄清(C03 / C04 文档主要引用 grules/G2 文档,影响最小)。
2. **路由别名一致**:`/api/v1/* ≡ /api/app/v1/*` 与 `/admin/v1/* ≡ /api/admin/v1/*` 在 D02 每端的 `01-routes-delta.md` 顶部均显式说明,引用 [A00-04 §四.5](../../prompt/A-framework/A00-04-文档目录规划.md)。
3. **跨端隔离声明**:auth ↔ auth 在 D02 / C05 中显式声明 cookie 域 / Supabase project / session 不共享。
4. **D03 验证摘要**:6 个 surface 全部 "可进入编码阶段"(无新增不通过项)。

### 仍待办(Round 6+)

1. **C05 06-page-specs 按 page-id 单独展开**(28 个 page-id × 单文件,共 28 文件)。
2. **C05 其余文件**(01-overview / 02-glossary / 03-personas / 05-user-journeys / 09-design-summary / 10-known-issues / 11-roadmap / 12-changelog)按端过滤;当前共享 banner 已加,内容轻量重写即可。
3. **C04 各 surface 的 `feature.css` / `feature.js` / `mock-data.js`** 按 D02 OP-ID 实质化。
4. **C02 auth feature 8 文件**(原已 Round 3 下沉,内容仍简,可补强)。
5. **F 层 D03 全量重跑**:基于 Round 5 的 D03 重写底稿,可触发自动化 `pnpm doc:lint` 校验(开发期)。

---

## 2026-05-16 · 批次 11 · B04 组件库填实质(Round 4)

> F 层最后一块空骨架收口。批次 9 的 Round 2 只为 [`B04-design/design-system/05-components/`](../B04-design/design-system/05-components/) 创建了 13 个文件骨架,本次按上游 [`grules/G2-视觉与交互风格/04-状态与组件.md`](../../grules/G2-视觉与交互风格/04-状态与组件.md) 逐文件填入实质内容。

### Round 4 · 13 组件文件实质化

| 文件 | 内容范围 | 上游 §  |
| ---- | ---- | ---- |
| [00-index.md](../B04-design/design-system/05-components/00-index.md) | 组件清单 + ui-kit 导出名映射 + 全局规则 | §九 |
| [01-buttons.md](../B04-design/design-system/05-components/01-buttons.md) | 5 变体矩阵 + 尺寸/状态/约束 | §二 |
| [02-forms.md](../B04-design/design-system/05-components/02-forms.md) | 布局/输入框/提示文案/复合控件/校验时机 | §四 |
| [03-tables.md](../B04-design/design-system/05-components/03-tables.md) | 容器/空状态/加载/虚拟滚动/可访问性 | §三 |
| [04-modals.md](../B04-design/design-system/05-components/04-modals.md) | 尺寸/视觉/关闭/动效/a11y | §五 |
| [05-drawers.md](../B04-design/design-system/05-components/05-drawers.md) | 抽屉规则 + 移动端 | §六 |
| [06-toasts-alerts.md](../B04-design/design-system/05-components/06-toasts-alerts.md) | Toast 4 类型 + 危险确认弹窗(含高危二次确认) | §七 / §八 |
| [07-empty-loading.md](../B04-design/design-system/05-components/07-empty-loading.md) | EmptyState / Skeleton / Spinner | §三.1 / §三.2 |
| [08-popovers-tooltips.md](../B04-design/design-system/05-components/08-popovers-tooltips.md) | Tooltip + Popover + a11y | (本项目新增) |
| [09-avatars-badges-tags.md](../B04-design/design-system/05-components/09-avatars-badges-tags.md) | StatusTag 6 语义 + Avatar 4 尺寸 + Badge 3 类型 | §一 |
| [10-tabs-accordion.md](../B04-design/design-system/05-components/10-tabs-accordion.md) | GlassTabs 3 变体 + Accordion | (本项目新增) |
| [11-cards-glass.md](../B04-design/design-system/05-components/11-cards-glass.md) | GlassCard + 4 毛玻璃工具类 + 降级 + 性能 | §九 + 01 §四 |
| [12-decorations.md](../B04-design/design-system/05-components/12-decorations.md) | 分隔线/品牌光晕/底纹/图标/禁忌 | (本项目新增) |

### 影响
- F 层(B04)从「骨架」转为「可消费」,所有 feature 的 C03 页面 / C04 原型 / 前端编码现可直接引用本目录组件契约。
- 已开工 feature(`auth` / `auth` / `course` / `discover-china`)的 D03 V01(上游链一致性)在 Round 5 重跑时,需新增"组件引用是否指向 `05-components/` 而非旧 `04-status-components.md`"的检查项。

### 待办(Round 5+)
1. 各 surface C02 / C05 / D02 文件按端**过滤**实质内容(剔除对端独有 page / endpoint / 业务规则)。
2. C05 各 surface 的 `06-page-specs/<page-id>.md` 按 page-id 单独展开。
3. D03-validation 各 surface 重写校验链路(`01-upstream-chain` / `02-module-closure` / `03-prd-traceability`)。
4. C04 各 surface 的 `feature.css` / `feature.js` / `mock-data.js` 按 OP-ID 实质化。
5. F 层变更全量 D03-V 重跑(含 Round 3 auth 子层 + Round 4 组件库的双重影响)。

---

## 2026-05-16 · 批次 10 · auth feature 退化 surface 子层补全(Round 3)

> **二次审计发现**:批次 9 修正 `course` / `discover-china` 时,遗漏了 [`prompt/A-framework/A00-04-文档目录规划.md`](../../prompt/A-framework/A00-04-文档目录规划.md) §四.5 第 280–289 行示例明确指出的 **`<surface>-auth` feature 也须有退化 `<surface>/` 子层**(例如 `C04-prototype/auth/admin/...`),当前 `auth` / `auth` 的内容直接挂在 feature 根,与 `course/{app,admin}/` 形态不对称,违反"多端项目所有 feature 统一形态"原则。

### Round 3 · auth feature 内容下沉到 `<surface>/`

为 `auth`(surface=`app`)与 `auth`(surface=`admin`)在以下 6 个阶段统一新建 `<surface>/` 子目录,把除 `_input/` 与 `99-open-questions.md` 之外的所有内容文件/子目录整体下移一层,并修正其 `TARGET-PATH` 注释:

| 阶段 | feature 根原结构 | 下沉后 |
| --- | --- | --- |
| C02-ia | `auth/{00..07-*,_input,99-open}` | `auth/app/{00..07-*}` + 根 `_input,99-open` |
| C03-pages | `auth/P-auth-00X.md` | `auth/app/P-auth-00X.md` |
| C04-prototype | `auth/{index.html,pages,states,vendor,assets,feature.css/js,mock-data.js,README,changelog}` | `auth/app/<同结构>` |
| C05-prd | `auth/{00..12-*,06-page-specs}` | `auth/app/<同结构>` |
| D02-api | `auth/{00..06-*,03-endpoints/}` | `auth/app/<同结构>` |
| D03-validation | `auth/{01..03-*}` | `auth/app/{01..03-*}` |

对称同步操作 `auth` → `auth/admin/<同结构>`,共 12 组 feature × stage 全部修正完成。所有被移动文件首行 `<!-- TARGET-PATH: ... -->` 已批量更新为新路径。

### 影响
- `*-auth` 与 `course` / `discover-china` 现统一为多端形态(只是 `auth` / `auth` 是退化单端,只填一个 surface),目录契约 100% 对齐 §四.5 表格。
- 跨阶段引用(已冻结的 D01/D02/D03 等内部交叉链接)使用 **feature 根相对路径** 的不受影响;使用 `docs/<stage>/auth/<file>` 形式直链的旧引用需在 Round 5(D03-V 重跑)逐一核对。
- `C01-requirements/{auth,auth}/baseline.md` 按 §四.5 表「仍单份」规则保持不动。

### 反思 / 教训
- 批次 9 自查时只看了 §四.5 表头**列**(C02/C03/C04/C05/D02/D03 的多端变体),忽略了同节后段对 auth feature 的**示例段落**(第 280–289 行),导致只修正了 `course` / `discover-china`,遗漏 `*-auth`。
- 复审 checklist 应改为:**所有 feature(含退化 auth)在所有 C/D 阶段都必须落在 `<feature>/<surface>/...` 路径下**,无例外(单端项目除外,但本项目是 surface≥2)。
- 已记入 [`/memories/session/zhiyu-restructure-progress.md`](file:///memories/session/zhiyu-restructure-progress.md),后续 Round 4+ 内容实质化将基于本次修正后的统一结构。

---

## 2026-05-16 · 批次 9 · 多 surface 结构合规修正(Round 1 + Round 2)

> **背景**:用户审计指出 `discover-china` 与 `course` 两个 feature 未按 [`prompt/A-framework/A00-04-文档目录规划.md §四.5`](../../prompt/A-framework/A00-04-文档目录规划.md) 的多 surface 变体规则拆分(仅 `*-auth` 已正确按 `auth` / `auth` 拆),违反 [`docs/B01-architecture/08-surfaces.md`](../B01-architecture/08-surfaces.md) 中"app + admin 双端独立"的架构定调。本次执行结构性修正,**不允许任何分期或延后**。

### Round 1 · 物理迁移(目录/文件搬运 + TARGET-PATH 修正)

| 范围 | 操作 | 数量 |
| ---- | ---- | ---- |
| `C02-ia/{course,discover-china}/` | 新建 `_shared/`,迁入 `state-machines.md`(原 03-)与 `flows-shared.md`(02-flows 副本);新建 `{app,admin}/` 骨架 | 4 _shared 文件 + 4 surface 目录 |
| `C03-pages/{course,discover-china}/` | 新建 `{app,admin}/`,按 `P-app-*` / `P-admin-*` 命名分发 | 24 文件迁移(course 8+9,discover-china 3+4) |
| `C04-prototype/course/` | 新建 `{app,admin}/{vendor/proto-style,pages,states,assets}/`,从 [`function/02-course/ai/F4-AI-原型设计/`](../../function/02-course/ai/F4-AI-原型设计/) 拷贝 17 HTML(P-A-* → admin,P-C-* → app),vendor 从 [`docs/B04-design/prototype-style/`](../B04-design/prototype-style/) 拷,补 `index.html` / `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `changelog.md` | 每 surface 一套 |
| `C04-prototype/discover-china/` | 把原平铺 `pages/` / `states/` / `vendor/` / `index.html` 按 surface 拆到 `{app,admin}/` 各自独立目录 | 7 HTML 拆 + 25 states 拆 + 2 套 vendor |
| `C05-prd/{course,discover-china}/` | 新建 `_shared/` 与 `{app,admin}/06-page-specs/` 骨架 | 12 目录 |
| `D02-api/{course,discover-china}/03-endpoints/` | 拆到 `{app,admin,internal}/03-endpoints/`,按 OP-ID 前缀分发 | 16 endpoint 文件迁移(course 10,discover-china 6) |
| `D03-validation/{course,discover-china}/` | 新建 `{app,admin}/` 骨架 | 4 目录 |
| 全量 `TARGET-PATH` 注释 | Python 脚本批量精确替换被迁文件的 HTML 注释头 | 50 文件修正 |

### Round 2 · 内容拆分(根级 → surface,删除根级)

| 范围 | 操作 | 数量 |
| ---- | ---- | ---- |
| `C02-ia/{course,discover-china}/{01-feature-catalog,02-flows,04-pages,05-navigation,06-coverage-matrix}.md` | 拷到 `{app,admin}/` 各一份(初版相同,Round 3+ 按端过滤),`TARGET-PATH` 更新,根级删除,加 surface banner | 20 文件 |
| `D02-api/{course,discover-china}/{01-routes-delta,02-overview}.md` | 拷到 `{app,admin}/` 各一份,根级删除 | 8 文件 |
| `D03-validation/{course,discover-china}/{01,02,03}.md` | 拷到 `{app,admin}/` 各一份,根级删除 | 12 文件 |
| `C05-prd/{course,discover-china}/PRD.md` | **大爆炸**:按第 1..12 章拆成 12 文件 × 2 surface(00-index / 01-overview / 02-glossary / 03-personas / 04-feature-catalog / 05-user-journeys / 06-page-specs/00-index / 07-business-rules / 08-roles-permissions / 09-design-summary / 10-known-issues / 11-roadmap / 12-changelog),`_shared/` 同步 `glossary.md`(第 2 章)与 `business-rules.md`(第 7 章),根 PRD.md 删除 | 60 surface 文件 + 4 _shared 文件 |
| `B04-design/design-system/` | 文件重命名以对齐 [`prompt/A-framework/A00-04-文档目录规划.md §四`](../../prompt/A-framework/A00-04-文档目录规划.md):`04-status-components.md` → `04-status-colors.md`、`05-interactions.md` → `06-interactions.md`、`06-responsive-dark.md` → `07-responsive-dark.md`、`07-icons-imagery.md` → `99-extension-icons-imagery.md`(标记为非规范扩展) | 4 文件重命名 + TARGET-PATH 修 |
| `B04-design/design-system/05-components/` | 新建 13 文件骨架(00-index + 01-buttons / 02-forms / 03-tables / 04-modals / 05-drawers / 06-toasts-alerts / 07-empty-loading / 08-popovers-tooltips / 09-avatars-badges-tags / 10-tabs-accordion / 11-cards-glass / 12-decorations) | 13 文件 |

### 影响与回链
- **F 层(B04-design 重命名)触发**:已开工 feature(`auth` / `auth` / `course` / `discover-china`)的 D03 V 链路需在 Round 3 重跑校验交叉引用是否仍命中(组件引用现需指向 `05-components/<file>` 而非旧 `04-status-components.md`)。
- **多 surface 修正不破坏 D01**(数据模型按 feature 共享,本身就是 single,无需拆 surface)。
- **C04-prototype** 每 surface 独立 `vendor/proto-style/` 已就位,但 `index.html` / `feature.css` / `feature.js` / `mock-data.js` 当前是占位/原版拷贝,Round 4 将按各 surface 真实 page-id 重写。

### 后续 Round 3+ 待办(已记入待办列表)
1. C02-ia / C05-prd / D02-api 各 surface 文件按端过滤实质内容(剔除对端独有的 page / endpoint / 业务规则);
2. C05-prd 各 surface 的 `06-page-specs/` 按 page-id 展开单页 spec 文件;
3. D03-validation 各 surface 重写校验链路(`01-upstream-chain` / `02-module-closure` / `03-prd-traceability`)以反映 surface 拆分;
4. B04 `05-components/` 13 文件由骨架填实质内容(源:`grules/G2-视觉与交互风格/04-状态与组件.md`);
5. C04-prototype 各 surface 的 `feature.css` / `feature.js` / `mock-data.js` 按 OP-ID 实质化;
6. 全量 `D03-V` 重跑(F 层变更影响)。

### 反思 / 教训
- 初次"全面检查"声明 PASS 是错误的,未对照 [`A00-04 §四.5`](../../prompt/A-framework/A00-04-文档目录规划.md) 的多 surface 变体规则。
- 复审应优先检查"多 surface feature 是否物理拆 app/admin/_shared",而非只看"文件命名是否含 page-id"。
- 后续每次冻结前,V 链路必须强制对照 A00-04 §四(单 surface)与 §四.5(多 surface)的 21 条 + 12 条结构契约。

---

## 2026-05-16 · 批次 8 · `course` D-phase 完整冻结

> 反向回写"课程学习引擎"全部 D-phase(D01..D03)。信息源:[`function/02-course/ai/F1-AI-数据模型规范/`](../../function/02-course/ai/F1-AI-数据模型规范/)(13 文件,2545 行) + [`function/02-course/ai/F2-AI-接口规范/`](../../function/02-course/ai/F2-AI-接口规范/)(13 文件,2473 行)。

### D01 数据规范(13 文件)
- [`docs/D01-data/course/`](../D01-data/course/00-index.md):00-index、01-er-diagram(15 表 mermaid)、02-entities/ × 5(catalog / kp-question / exam / progress / import-media-audit,共 15 表)、03-business-rules(40 条 DBR-ID)、04-validations(正则/枚举/长度/jsonb/跨字段)、05-calculations(SRS / 评分 / 分区 / cron)、06-indexes(UNIQUE/B-tree/GIN)、07-volume-growth(月分区策略)、08-seed-data(5 主题 + 25 阶段 + 媒资占位)、99-open-questions、_input。
- 关键决策:
  - schema 统一 `zhiyu`(表名前缀 `course_*`),不另建 `zhiyu_course`(已同步修正 [C05 PRD §13](../C05-prd/course/PRD.md));
  - 35 个 KP sequence + 5 个 Question sequence(7 KP 类型 × 5 主题 / 5 主题);
  - `course_user_answers` `pg_partman` 月分区;0–6m 在线,7–24m 索引精简,>24m P2 归档对象存储;
  - `mv_course_user_daily` 5 分钟 CONCURRENTLY 刷新;`mv_course_track_stats` 10 分钟。

### D02 接口规范(15 文件)
- [`docs/D02-api/course/`](../D02-api/course/00-index.md):00-index、01-routes-delta、02-overview、03-endpoints/ × 10(app 3 文件 / admin 6 文件 / internal 1 文件)、04-error-codes(55 个 `COURSE_*`)、05-concurrency(乐观锁 + 行锁 + UPSERT + Idempotency)、06-events(pg_notify + 5 cron)、99-open-questions、_input。
- 关键决策:
  - 学员 19 endpoint + 管理 24 endpoint + 内部 3 endpoint,共 46 个 OP-ID;
  - 鉴权三层:`/api/v1/course/*` Supabase JWT;`/admin/v1/course/*` JWT + 中间件 + `tracks_scope`,DB 走 service_role;`/internal/v1/course/*` `X-Internal-Token`;
  - 限流:`POST /answers` 600/分;`POST /kps/:id/audio` 20/分;`GET /admin/search` 30/分;
  - 题目修订 `version += 1`,旧 attempt 不追溯改分(BR-RP04);
  - 节末小测 `quiz_id` Redis TTL 10 分钟,不入 attempt 表;
  - 考试超期由 cron 每分钟扫 + 提交侧行锁串行(`fn_submit_exam`)。

### D03 校验(3 文件,全 PASS)
- [`docs/D03-validation/course/01-upstream-chain.md`](../D03-validation/course/01-upstream-chain.md):30 R-ID / 40 BR / 17 P-ID / 7 SM 全闭环;
- [`docs/D03-validation/course/02-module-closure.md`](../D03-validation/course/02-module-closure.md):15 表 CRUD / 55 错误码 / 状态机 / RLS / cron 闭环;
- [`docs/D03-validation/course/03-prd-traceability.md`](../D03-validation/course/03-prd-traceability.md):40 BR × 15 表 × 46 OP 矩阵 + 11 项副作用契约 + 12 项不变量。

### 同步修订
- [`docs/C05-prd/course/PRD.md` §13](../C05-prd/course/PRD.md):schema 名从 `zhiyu_course` 改回 `zhiyu`(course_* 前缀);表数 18 → 15;OP 数细化为 19+24+3;错误码 ~40 → 55。

### 后续(P2)
- `course_user_answers` 24 个月以上分区归档对象存储;
- 管理端全文搜索 GIN 表达式索引按使用阈值动态加;
- TTS 实景适配器替换 mock。

---

## 2026-05-16 · 批次 7 · `course` C-phase 完整冻结

> 反向回写"课程学习引擎"全部 C-phase(C01..C05)。信息源:[`function/02-course/prd/`](../../function/02-course/prd/)(8 文件,含 07 已封板决策段) + [`function/02-course/ai/F3-AI-页面交互规范/`](../../function/02-course/ai/F3-AI-页面交互规范/)(14 文件) + [`function/02-course/ai/F4-AI-原型设计/`](../../function/02-course/ai/F4-AI-原型设计/)(17 HTML)。Feature 命名 = `course`(与 F3 §"功能名称"课程学习引擎 一致,目录简短化)。

### C01 需求基线(5 文件)
- [`docs/C01-requirements/course/`](../C01-requirements/course/):baseline.md(30 个 R-ID:R-course-001..030,分 应用学习 / 管理 9 页 / 跨域副作用 三段)+ flows/main-flow.md(6 主流程 FL-course-01..06)+ flows/exception-flow.md(7 异常 FX-course-01..07)+ _input + 99-open-questions(已清空)
- §4 不变量:5 主题码 `share/ec/fc/hsk/dl` 白名单 / Stage 0 共享一次性 / 节固定 12 KP + 节末 6 题 / 节 code `<track>-<stage>-<chapter>-<lesson>` / KP code `kp_{track}_{type_initial}_{seq5}` / Question code `q_{track}_{seq8}` / SRS Leitner 5 盒 1·3·7·14·30 / 满分 100 动态均分 / `is_published` 二态 / 章发布级联 节+KP+题 节发布级联 KP+题 下架不级联

### C02 IA(10 文件)
- [`docs/C02-ia/course/`](../C02-ia/course/):00-index.md / 01-feature-catalog.md(10 个 M-ID)/ 02-flows.md(13 Flow-ID,主 6 + 异 7)/ 03-state-machines.md(7 SM:lesson-progress/content-publish/answer/srs/exam-attempt/form-dirty/offline-queue)/ 04-pages.md(17 P-ID,8 app + 9 admin,与 F3 P-C-*/P-A-* 一一映射)/ 05-navigation.md(应用端 5 Tab + 管理端 9 Tab + 行级 tracks_scope 联动)/ 06-coverage-matrix.md(R×M / R×Page / Flow×Page / SM×Page 四矩阵 + ID 缩写说明)/ 07-error-pages.md(7 通用错误态 + D-1..D-18 弹窗对照表)/ 99-open-questions / _input

### C03 页面规格(19 文件)
- [`docs/C03-pages/course/`](../C03-pages/course/):每 P-ID 一文件
  - 应用端 8:P-app-course-001(首页主题切换)/ 002(学习地图+节内)/ 003(KP 卡片)/ 004(SRS 复习)/ 005(错题本)/ 006(考试中心入口)/ 007(考试答题倒计时)/ 008(我的)
  - 管理端 9:P-admin-course-001(目录总览)/ 002(主题-阶段-章-节四级)/ 003(节编辑)/ 004(KP 列表+Drawer)/ 005(题目列表+双开预览)/ 006(学员举报处理)/ 007(媒资库)/ 008(考试中心管理)/ 009(全局搜索)
  - 每文件:进入条件 / 初始数据 / 主要交互 / 弹窗 / 状态 / 响应式 / 不变量回链
  - 99-open-questions / _input

### C04 原型契约(2 文件)
- [`docs/C04-prototype/course/README.md`](../C04-prototype/course/README.md):17 HTML 原型 → 17 P-ID 映射 + 12 组件清单(`<KpCard>` 7 变体 / `<QuestionRenderer>` 12 种 / `<CountdownTimer>` / `<ProgressMap>` 等)+ 6 状态契约 + Design Token 契约(`--track-color-*` / `--lesson-*` / `--answer-*`)+ 多语对齐(`course.*` key 前缀)
- 原则:不复制 HTML 资产,实现端按本契约 + F3 + B04 token 三方对齐还原;原型与契约冲突时以 F3 + 契约为准

### C05 PRD(3 文件)
- [`docs/C05-prd/course/PRD.md`](../C05-prd/course/PRD.md):§7 业务规则 **40 条 BR-ID**,分 7 段:BR-STRUCTURE(S01..S07 骨架 / 命名)/ BR-CONTENT(C01..C10 生命周期 / 5 语完整性 / 版本治理 / LWW)/ BR-LEARNING(L01..L07 节内 / 答题副作用 / 离线队列 / 多端同步)/ BR-SRS(R01..R04 Leitner 间隔 / 题型轮换)/ BR-EXAM(E01..E08 4 类考试 / 动态均分 / 阶段考解锁 / 不可重考 / 试抽不写 attempt)/ BR-REPORT(RP01..RP04 举报聚合 / 历史不追溯)/ BR-AUTH-PERM(P01..P06 多语 / 订阅控制 / 行级 tracks_scope)/ BR-SYS(Y01..Y04 系统副作用)
- §9 性能基线:节聚合 ≤200KB P95 ≤300ms / 答题 P95 ≤150ms / 交卷 50 题 P95 ≤800ms / `/app/answer` 限流 60 次/分;§12 决策封板段引用 prd/07 全部 A/B/C/H 段
- 99-open-questions / _input

### 全局影响
- 触发下游:`course` 的 D-phase(批次 8)将基于本 C-phase 产出 D01(18 张表 schema)+ D02(~80 OP-ID + ~40 错误码 `COURSE_*`)+ D03(三段 PASS 验证);实现 schema = `zhiyu_course`
- 与 `discover-china` 共享:5 语 locale `zh/en/vi/th/id` 全局对齐、媒资库技术栈、Admin 角色与 LWW 模式、软删 30 天 + cron 清理策略
- 不变量与 B02 / discover-china 一致:`AUTH_USE_USER_ENTRY` 仍 deferred(B02 99-open-questions Q-2026-05-16-01),`auth.users` 直引模式继续生效

---

## 2026-05-16 · 批次 6 · `discover-china` D-phase 完整冻结

> 反向回写"发现中国"全部 D-phase(D01..D03)。信息源:[`function/01-china/ai/F1-AI-数据模型规范/`](../../function/01-china/ai/F1-AI-数据模型规范/)(10 文件) + [`function/01-china/ai/F2-AI-接口规范/`](../../function/01-china/ai/F2-AI-接口规范/)(11 文件) + [`function/01-china/prd/F2-用户-操作与业务逻辑.md`](../../function/01-china/prd/F2-用户-操作与业务逻辑.md)。

### D01 数据规范(13 文件)
- [`docs/D01-data/discover-china/`](../D01-data/discover-china/):3 张表(`china_categories` / `china_articles` / `china_sentences`),全部 RLS + 多列 CHECK + 软删 + 5 语 jsonb;
- 10 RPC:`fn_gen_article_code` / `fn_next_sentence_seq` / `fn_resequence_sentences`(+100000 偏移避免唯一冲突) / `fn_publish_article` / `fn_unpublish_article` / `fn_insert_sentence_at` / `fn_delete_sentence` / `fn_reorder_sentences` / `fn_bulk_insert_sentences` / **跨域 `fn_clear_progress_by_article`**(SECURITY DEFINER);
- 软删策略:`china_articles` + `china_sentences` 30 天窗口,**不提供恢复 UI**,cron `cron_china_purge_soft_deleted` 每日 03:00 物理清理;`china_categories` 字典表不软删;
- 12 类目种子 SQL(5 语 ON CONFLICT upsert)落地于 [`08-seed-data.md`](../D01-data/discover-china/08-seed-data.md)。

### D02 接口规范(16 文件)
- [`docs/D02-api/discover-china/`](../D02-api/discover-china/):**25 个 OP-ID**(应用端 7 + 管理端 15 + 内部 2 + AUX 1),含 **OP-C6 / C7 已下线**(2026-04 评审取消阅读进度,路由不挂载、文件保留、跨域清进度副作用保留);
- 错误码区段 `45000-45999` 全量登记(共 31 条 `CHINA_*`),覆盖校验 / 资源 / 状态 / 上游 / 系统五类;
- 并发策略:LWW(A5 / A12) + 行锁 FOR UPDATE(A11 / A13 / A14) + `Idempotency-Key`(可选,C4);
- 限流:默认 IP 60 / min + 用户 120 / min;OP-C4 单独 IP 20 / min(缓存命中不计);OP-A15 单独用户 30 / min(防拖库);
- 事件:`pg_notify` 五个 channel(`china_article_published` / `_unpublished` / `_deleted` / `china_sentence_changed` / `china_tts_ready`)用于应用层缓存 invalidate;
- TTS:用户触发 + 全平台共享永久缓存 + 失败不限重试;dev / 未配密钥环境走 `packages/ai-adapters/tts/mock.ts`(对齐 `zhiyu-docker-policy`)。

### D03 验证(3 文件)
- [`docs/D03-validation/discover-china/01-upstream-chain.md`](../D03-validation/discover-china/01-upstream-chain.md):上游链 **PASS**(20 R-ID / 12 BR / 7 P-ID / 4 SM 全部映射);
- [`02-module-closure.md`](../D03-validation/discover-china/02-module-closure.md):模块内闭环 **PASS**(3 表 CRUD 闭环 / 25 端点数据落点 / 31 错误码与校验规则一一对应 / RLS 与权限层一致);
- [`03-prd-traceability.md`](../D03-validation/discover-china/03-prd-traceability.md):PRD 回链 **PASS**(20 R-ID × C05 BR × D01 实体 × D02 OP-ID 全矩阵贯通;跨域副作用契约完整;无反向漂移)。

### 已知保留项
- `AUTH_USE_USER_ENTRY`:继续按 [`B02-permissions/99-open-questions.md Q-2026-05-16-01`](../B02-permissions/99-open-questions.md) 留待 F 层修订;不阻断批次 7 / 8;
- 阅读进度功能下线:本批仅记录契约 + 跨域副作用契约;模型 / 代码层的清理动作不在 D-phase 文档范围。

---

## 2026-05-16 · 批次 1-5 审计补强

> 反向回写审计后,对若干局部一致性问题做最小修复,不影响已冻结产物语义。

- [`docs/C01-requirements/discover-china/baseline.md`](../C01-requirements/discover-china/baseline.md) §4:补 5 语 locale key 集合(`zh/en/vi/th/id`)与 [`B02-permissions §4`](../B02-permissions/03-authz-mechanism.md) 对齐;新增文章编码与 seq_no 格式正式规约 → D01 schema 输入完备;
- [`docs/C02-ia/{auth,auth,discover-china}/06-coverage-matrix.md`](../C02-ia/):在文件头添加 "ID 缩写约定" 说明,明确短形与完整形的映射,避免 D03 V01 跨文件追溯歧义;
- 维持决策:`AUTH_USE_USER_ENTRY` 仍按 [`B02-permissions/99-open-questions.md Q-2026-05-16-01`](../B02-permissions/99-open-questions.md) 留待下次 F 层修订统一补登,不阻断批次 6。

---

## 2026-05-16 · 批次 5 · `discover-china` C-phase 完整冻结

> 反向回写"发现中国"全部 C-phase(C01..C05)。信息源:[`function/01-china/prd/`](../../function/01-china/prd/) + [`function/01-china/ai/F3-AI-页面交互规范/`](../../function/01-china/ai/F3-AI-页面交互规范/)。

### C01 需求基线
- [`docs/C01-requirements/discover-china/baseline.md`](../C01-requirements/discover-china/baseline.md):**20 个 R-ID** R-discover-china-001..020,3 US 用户故事,边界 / 不变量(5 语并齐、TTS 缓存键、软删 30 天);
- 6 个主流程 + 7 个异常流程(mermaid)详 `flows/`。

### C02 信息架构
- 5 M-ID / 13 Flow-ID / 4 SM(文章发布、TTS 音频生成、表单脏、应用端 TTS 播放器);
- 7 page-id(应用端 3 + 管理端 4);8 D-ID 弹窗 / Drawer;
- 覆盖矩阵 20 R 全部至少 1 page-id ✅。

### C03 页面规格
- 7 个 page-id 一文件一规格,含 DOM 骨架 + 状态 + 交互 + 错误码 + 移动端 + a11y + 埋点;
- 复杂页 `P-admin-discover-china-003` 含 sticky 顶栏 / 5 语 Tab / 句子卡片 + 重排 + 任意位置插入 + 后写覆盖。

### C04 HTML 原型(共 43 文件)
- vendor/proto-style/ 4 文件由 B04-design/prototype-style/ v1.0 拷贝;
- pages/ 7 默认态;states/ 7×3 + 4 forbidden = 25;
- feature.css / feature.js / mock-data.js / index.html / README.md / changelog.md / _input/prototype-direction.md;
- 弹窗 D-1..D-8 在 mock 中以 toast 简化代演(结构详见 C03 / PRD)。

### C05 PRD
- [`docs/C05-prd/discover-china/PRD.md`](../C05-prd/discover-china/PRD.md):13 章完整 PRD,12 条 BR 业务规则,角色权限矩阵,路线图 v1.0..v2.0。

### 自检
- ✅ R / M / Flow / SM / page / D ID 全部命名空间唯一;
- ✅ 20 R-ID 全覆盖至少 1 page-id;
- ✅ 7 page-id 全部 P0 出齐 default + loading + empty + error;管理端 + forbidden;
- ✅ vendor/proto-style/ 与 B04 v1.0 字节一致(cp);
- ✅ 99-open-questions 全空;
- ⏳ 待批次 6 跑 D01/D02 + D03 校验。

---

## 2026-05-16 · 批次 3+4 补登 · C04 HTML 原型 + B04 prototype-style 实化

> 修正批次 3/4 当时将 C04 标注为"暂缓占位"违反框架"一次性出齐"硬约束;本次按 [`prompt/C-product/C04-H03-AI输出-HTML原型规范.md`](../../prompt/C-product/C04-H03-AI输出-HTML原型规范.md) 补齐全部原型产物。

### B04 实化(v1.0)
- [`docs/B04-design/prototype-style/tokens.css`](../B04-design/prototype-style/tokens.css):全套 CSS 变量(颜色/字体/间距/圆角/阴影/毛玻璃/动效),亮模式默认 + 暗模式覆盖在 themes.css;
- [`docs/B04-design/prototype-style/themes.css`](../B04-design/prototype-style/themes.css):`[data-theme="dark"]` 完整覆盖 + `prefers-reduced-motion` 兜底;
- [`docs/B04-design/prototype-style/app.css`](../B04-design/prototype-style/app.css):reset + 远景红光晕 + `.glass-*` / `.btn-*` / `.input` / `.toast` / `.skeleton` / `.proto-switcher` / `.env-badge`,响应式 768/375 双断点;
- [`docs/B04-design/prototype-style/app.js`](../B04-design/prototype-style/app.js):`window.proto.{bootstrap,setTheme,toggleTheme,toast,cooldown,devtools.mountStateSwitcher,on}` 全局 API,FOUC 内联主题恢复;
- 状态从「占位」→「v1.0 已填充」。

### C04 `auth` 全套(50 文件)
- 9 page-id × (1 default + 3 必出状态) + 3 权限页 forbidden 态 = pages/ 9 + states/ 30;
- vendor/proto-style/ 4 文件字节级拷自 B04;
- index.html / feature.css / feature.js / mock-data.js(OP-ID 键,业务语言字段)/ changelog.md(v1.0)/ README.md / `_input/prototype-direction.md`;
- [入口](../C04-prototype/auth/app/index.html)。

### C04 `auth` 全套(28 文件)
- 4 page-id × (1 default + 3 必出状态) + 1 权限页 forbidden 态 = pages/ 4 + states/ 13;
- 其余资产同上;
- [入口](../C04-prototype/auth/admin/index.html)。

### 自检
- 无 CDN / 无打包器 / 无真实网络请求;
- feature.css 未重定义任何 token;
- 全部跳转用 `<page-id>.html` 文件锚(无真实路由路径);
- 浏览器直接双击 `index.html` 可跑。

---

## 2026-05-16 · 批次 4 · `auth` feature 全套反向回写

> 后台超管的「登录 / 找回 / 改密 / 退出」最小集;邀请制 = 运维 SQL seed,无产品 UI。

| 阶段 | 产物 | 数量 | 状态 |
|------|------|------|------|
| C01 R | `docs/C01-requirements/auth/*` (_input + baseline + flows×2 + 99) | 5 | 已冻结 |
| C02 I | `docs/C02-ia/auth/admin/*` (00..07 + 99 + _input) | 10 | 已冻结 |
| C03 N | `docs/C03-pages/auth/admin/P-001..004 + 99 + _input` | 6 | 已冻结 |
| C04 H | `docs/C04-prototype/auth/admin/{README,_input}` | 2 | **占位** (与 B04 prototype-style 同步 deferred) |
| C05 E | `docs/C05-prd/auth/admin/*` (00..12 + 99 + 06/00-index + _input) | 15 | 已冻结 |
| D01 D | `docs/D01-data/auth/admin/*` (00..03 + 99 + _input) — **delta-only,0 新增表** | 6 | 已冻结 |
| D02 L | `docs/D02-api/auth/admin/*` (00..06 + 99 + 03-endpoints×10 + _input) | 19 | 已冻结 |
| D03 V | `docs/D03-validation/auth/admin/{01,02,03}` | 3 | V02/V03 全绿,V01 含 1 项轻度警告 (见下) |

**关键数字**:10 R-ID / 2 M 模块 / 11 Flow / 3 SM / 4 page-id / 10 endpoint / 21 错误码 (20 复用 + 1 新增) / 10 审计事件。

**关键边界**:
- 0 新增 PG 表 (全部复用 B02-04 5 表);
- 0 新增 service (后端 100% 复用 auth 同名 service,handler 仅做 surface 透传 + role 守卫);
- 4 页全部极简;不暴露任何"创建管理员 / 改他人密 / 删账号"功能。

**V01 轻度警告**:`AUTH_USE_USER_ENTRY` 错误码尚未列入 [`B02-03 §4`](../B02-permissions/03-authz-mechanism.md);已记入 [`B02-permissions/99-open-questions.md`](../B02-permissions/99-open-questions.md),下一轮 F 层修订时补入;不阻断本 feature 冻结。

**受影响 feature**:无 (首次落 auth,不触发其它 feature 的 D03 重跑;`auth` 共享的 service 描述未变,无需重跑)。

---

## 2026-05-16 · 批次 3 · `auth` feature 全套反向回写

> 用户应用端「账号生命周期」feature 完整入坑：注册 / 登入 / OAuth / 找回 / 改密 / 改资料 / 退出 / 多设备 / 节流 / 禁用 / 链接过期。

| 阶段 | 产物 | 数量 | 状态 |
|------|------|------|------|
| C01 R | `docs/C01-requirements/auth/{_input, baseline, flows/main-flow, flows/exception-flow, 99-open-questions}` | 5 | 已冻结 |
| C02 I | `docs/C02-ia/auth/app/*` (00..07 + 99 + _input) | 10 | 已冻结 |
| C03 N | `docs/C03-pages/auth/app/P-auth-001..009 + P-001.scenarios + 99 + _input` | 12 | 已冻结 |
| C04 H | `docs/C04-prototype/auth/app/{README, _input}` | 2 | **占位** (与 B04-design/prototype-style 一致 deferred) |
| C05 E | `docs/C05-prd/auth/app/*` (00..12 + 99 + 06-page-specs/00-index + _input) | 17 | 已冻结 |
| D01 D | `docs/D01-data/auth/app/*` (00..08 + 99 + 02-entities×5 + _input) | 15 | 已冻结（无新增表，复用 B02-04 5 表）|
| D02 L | `docs/D02-api/auth/app/*` (00..06 + 99 + 03-endpoints×15 + _input) + `docs/D02-api/_global-routes.md`（首建）| 25 | 已冻结 |
| D03 V | `docs/D03-validation/auth/app/{01-upstream-chain, 02-module-closure, 03-prd-traceability}` | 3 | V01/V02/V03 全绿 |

**关键数字**：15 R-ID / 3 M 模块 / 11 Flow / 4 SM / 9 page-id / 15 接口 / 21 错误码 / 11 审计事件。
**关键边界**：本 feature **不**新增任何 PG 表；不涉及 admin 端（auth 批次 4 落）；不涉及 onboarding（user-account v2）；C04 原型与 B04 prototype-style 同步 deferred。
**受影响 feature**：无（首次落 auth，不触发其它 feature 的 D03 重跑）。

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
