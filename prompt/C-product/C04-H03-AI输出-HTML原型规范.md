# 28 · H03 AI 输出：HTML 原型规范

> **阶段**：H HTML 原型
> **谁产出**：AI（HTML 原型工程师）
> **落盘**：`docs/C04-prototype/<feature-id>/`
> **目的**：把本 feature 已冻结的 R / I / N 实化为可点开看的纯 HTML，零依赖、本地双击 `index.html` 就能跑。原型只承担"看效果 + 走通流程"，不承担生产工程化。

---

## 触发提示词

```
我已答完 H 澄清。请按 /prompt/C-product/C04-H03-AI输出-HTML原型规范.md 输出本 feature 一整套零依赖 HTML 原型，
落盘到 docs/C04-prototype/<feature-id>/。

【运行时资产】
**严禁拷贝**。所有 token / 组件 CSS / 全局交互 JS 必须**通过相对路径直接引用** `docs/B04-design/prototype-style/`，保证全仓单一来源。
页面以相对路径引入（多端结构 `<feature>/<surface>/{pages,states}/<page>.html` 共需 `../../../../`；`<feature>/<surface>/index.html` 共需 `../../../`）：
  <!-- pages/*.html 与 states/*.html -->
  <link rel="stylesheet" href="../../../../B04-design/prototype-style/app.css">
  <script src="../../../../B04-design/prototype-style/app.js"></script>
  <script>proto.bootstrap();</script>
  <!-- index.html -->
  <link rel="stylesheet" href="../../../B04-design/prototype-style/app.css">
  <script src="../../../B04-design/prototype-style/app.js"></script>
仅写本 feature 专属的 feature.css（贴 B04 变量，禁止重定义 token）与 feature.js（调 B04 暴露的 proto.* API）。

**例外（上游 AI 原型来源）**：若本 feature 在 `/function/<feature>/ai/F4-AI-原型设计/` 已有上游 AI 生成的成品原型（如 `function/02-course/ai/F4-AI-原型设计/`），则**改为引用该上游来源的 `_assets/`** 而非 B04，并按其结构在 C04 mirror 文件（仅改 P-ID、不改样式与类名），确保与上游字节等价。

H01 §3 表里所有 page-id 一次性出齐——**每个进表页面都必须出 4 份独立状态文件**（默认 / 加载 / 空 / 错误）；权限页加 forbidden 态。**禁止**以“分期 / 二期 / 暂不做 / 优先级不高”为由跳过。
mock 的接口数据放 mock-data.js（OP-ID 为键，与 docs/C03-pages/<feature-id>/<page-id>.md §4 一致；字段名用业务语言，**不假设**任何后端字段）。
本阶段属于产品设计阶段，**严禁**引用、读取或假设任何后续开发阶段产物（架构 / 数据规范 / 接口规范 / 校验规范），也禁止出现真实接口路径、SQL、表名、列名、真实路由路径。
完成后写 changelog.md（v1.0 首次产出）。
```

---

## 输出目录

多端 feature（推荐形态）：

```
docs/C04-prototype/<feature-id>/
  index.html              # feature 级索引：列出 app / admin 两端入口（多端时必出）
  changelog.md
  README.md               # H01 §4 勾选时产出
  _input/
    prototype-direction.md
  <surface>/              # app / admin 等；每个 surface 一份独立原型集
    index.html            # surface 内页面索引（含 4 态切换链接）
    feature.css           # 仅本 (feature × surface) 专属页面级样式；引用 B04 token，禁止重定义
    feature.js            # 仅本 (feature × surface) 专属页面级交互；调 B04 暴露的 proto.* API
    mock-data.js          # 假数据（按 OP-ID 组织）
    pages/
      <page-id>.html      # 页面默认态
    states/
      <page-id>.loading.html
      <page-id>.empty.html
      <page-id>.error.html
      <page-id>.forbidden.html    # 仅权限页
    assets/
      images/             # 仅业务占位图（如截图）；字体/图标/全局 CSS/JS 一律引用 B04，不放本地
```

> **`vendor/` 已废弃**：旧版本曾要求把 B04 拷贝到 `<surface>/vendor/proto-style/`，**该规则作废**（R9）。任何形如 `<surface>/vendor/` 的目录都属脏数据，必须清理；HTML 一律改为相对路径引用 `docs/B04-design/prototype-style/`。

> **`assets/styles.css` / `assets/prototype.js` 等运行时资产也属脏数据**（B04 才是唯一来源），允许保留的只有 `assets/images/` 一类业务占位图。

> 单端 feature 退化形态：省略 `<feature-id>/index.html` 与 `<surface>/` 层即可，其余规则不变。

> H02 澄清清单不在本目录，统一落 `docs/A00-meta/questions/H-<feature-id>-questions-round<N>.md`。

---

## 硬约束

0. **运行时资产唯一来源**：必须**通过相对路径**直接引用 `docs/B04-design/prototype-style/` 内的 `app.css` / `themes.css` / `tokens.css` / `app.js`，**禁止**在 feature 目录下任何位置复制 B04 文件（包括但不限于 `vendor/`、`assets/styles.css`、`assets/app.css`）。任何 token / 组件 CSS / 全局交互 JS 的调整都必须直接改 B04 源；因 B04 与该 feature 共用，所有 feature 立即同步生效。
   - 例外：若 feature 在 `/function/<feature>/ai/F4-AI-原型设计/` 有上游 AI 原型，则改引用该上游 `_assets/`；仍不得拷贝。
1. **零外部依赖**：不引 CDN、不用框架、不用打包器。仅原生 HTML + CSS + vanilla JS（通过相对路径引用 B04 本地资产，不算外部依赖）。
2. **字体自托管**（除非 B04 显式允许 CDN；字体走 B04 prototype-style/ 中的约定）。
3. **所有颜色/字号/间距/圆角/阴影必须用 CSS 变量**：变量来自 `docs/B04-design/prototype-style/tokens.css` + `themes.css`，**禁止**在 feature.css 重新定义任何 token。
4. **不得发起真实网络请求**。所有数据从 `mock-data.js` 取，键为 OP-ID。
5. **每个进表页面必出 4 状态文件**：默认 / 加载 / 空 / 错误。可选状态：`<page-id>.dark.html`、`<page-id>.mobile.html`。涉及权限页面再加 `<page-id>.forbidden.html`。
6. **响应式**：最少在 375 / 768 / 1280 三档下视觉无破。
7. **a11y**：每个交互元素 `:focus-visible` 必有焦点环；表单字段必有 `<label for>`。
8. **页面跳转一律用 `<page-id>.html` 文件锚**，**禁止**使用任何真实 URL 路径（路由属于 D02 阶段）。
9. **范围一次性出齐**：H01 §3 表里所有 page-id 必须本轮全部产出，**禁止**以“分期 / 二期 / 暂不做 / 优先级低”跳过。如发现某 page-id 在 C03-N 缺规范，应回到澄清提问而非跳过。
10. **单文件 ≤ 1200 行**。

---

## `index.html` 规范

- 顶部一句话项目名 + B03 一句话定调
- 表格列出所有页面：

| page-id | 默认 | 加载 | 空 | 错误 | 暗 | 移动 | 无权限 |
|---------|-----|------|----|------|----|------|--------|
| home | [↗](pages/home.html) | [↗](states/home.loading.html) | … | … | … | … | — |

---

## `pages/<page-id>.html` 规范

- 顶部 HTML 注释列出：page-id、对应 R-ID、对应 OP-ID（本页交互点）、当前状态名、最后更新时间
- 引入 `../../../../B04-design/prototype-style/app.css` + `../../../../B04-design/prototype-style/app.js`，另引 `../feature.css` + `../feature.js`；`<body>` 末尾调 `proto.bootstrap()`
  - （例外：feature 有 `function/<feature>/ai/F4-AI-原型设计/_assets/` 上游资产时，改为 `../../../../../function/<feature>/ai/F4-AI-原型设计/_assets/styles.css` 等等价路径）
- DOM 结构按 `docs/C03-pages/<feature-id>/<page-id>.md` §3 区块清单
- 每个 Block 加 `data-block="Block-1"` 便于反馈定位
- 每个操作按钮加 `data-op="OP-1"` 便于反馈定位
- 文案直接走 `docs/B03-ux/04-voice-tone.md` 对照表

---

## `states/<page-id>.<state>.html` 规范

- 与 default 共用同一 layout 但替换内容区域
- 加载态：骨架屏（用 `<div class="skeleton">`，CSS 动画 1.4s）
- 空态：插画位（占位 SVG）+ 主文案 + 主操作按钮
- 错误态：错误图标 + 错误文案 + 重试按钮 + 折叠展开"详情"
- 无权限态：直接用 B04 prototype-style 提供的 forbidden 组件 / 文案

---

## `feature.js` 规范

> 全局交互（modal / drawer / dropdown / toast / 主题切换 …）一律调 B04 prototype-style/app.js 暴露的 `proto.*` API，**不要**在 feature.js 重写。`feature.js` 只放本 feature 页面级的 mock 调度与小型逻辑。

```js
// 仅本 feature 的页面级逻辑
window.feature = {
  goto(pageId, state = 'default') {
    location.href = `./${state === 'default' ? 'pages' : 'states'}/${pageId}${state === 'default' ? '' : '.' + state}.html`;
  },
  mockApi(opId, params) { return window.MOCK[opId](params); },
};

// 顶栏：环境徽标（红色 "PROTOTYPE"）由 B04 prototype-style 自带组件渲染
// 状态切换浮窗：B04 prototype-style 提供 proto.devtools.mountStateSwitcher()，feature.js 仅负责挂载点
```

---

## `mock-data.js` 规范

```js
window.MOCK = {
  'OP-1': () => ({ ok: true, data: { items: [...], total: 12 } }),
  'OP-2': (params) => { /* ... */ },
  // 每个 OP-ID 都给一组成功 + 一组失败 fixture
  // 字段名用业务语言（"课程标题" / "讲师" / "价格"），**不得**出现 snake_case 数据库列名 / 后端字段名
};
```

---

## `changelog.md` 规范

```markdown
# 原型变更日志

## v1.0 · YYYY-MM-DD
- 范围：H01 §3 全表 page-id 全部产出（P-001…P-NNN）
- 进表页面 4 状态齐：<list>
- 权限页 forbidden 态：<list>
- B04 资产来源：docs/B04-design/prototype-style/ @ <commit/version>（本 feature **引用**，未拷贝）
- token 漂移：无 / 已回写 docs/B04-design/design-system/01-tokens.md
- 已知不同点：<>
```

> **token 漂移规则**：任何颜色 / 字号 / 间距 / 圆角的变化都属于 B04 范畴，必须直接改 `docs/B04-design/design-system/01-tokens.md` 与 `docs/B04-design/prototype-style/tokens.css`（改完后所有 feature 自动生效，无需拷贝），**禁止**在 feature.css 改。
> **后续修改**：若用户走完 G-H 后又要改原型，沿用本模板重跑 H01→H02→H03（同样一次性出齐），changelog 追加 v1.1 / v2.0 段落。**不要**在文件名上区分"首版/迭代"。

---

## 输出质量自检

- [ ] H01 §3 表里所有 page-id 是否一次性全部产出？有无以“分期/暂不做/优先级低”为由跳过？
- [ ] **无任何** `vendor/`、`assets/styles.css`、`assets/app.css`等 B04 拷贝产物（`assets/images/` 业务占位图除外）？所有 HTML 均通过相对路径引用 `docs/B04-design/prototype-style/`（或 feature 有 F4 上游时引用 `function/<feature>/ai/F4-*/_assets/`）？
- [ ] feature.css / feature.js 中无任何 token 重定义、无任何 hex / px 硬编码？
- [ ] 双击 `index.html` 在浏览器能跑，无 404、无控制台报错？
- [ ] 所有 page-id 与 `docs/C02-ia/<feature-id>/04-pages.md` 一致？
- [ ] 进表页面 4 状态齐？权限页 forbidden 态齐？
- [ ] 颜色 / 字号 / 间距 / 圆角全用 CSS 变量（与 docs/B04-design/design-system/01-tokens.md 一致）？
- [ ] 全文未出现任何后续开发阶段产物路径 / 真实接口名 / SQL / 表名 / 列名 / 真实路由路径？
- [ ] 字体自托管（除非 B04 允许 CDN）？
- [ ] mock-data.js 键都是 OP-ID（与 C03 页面一致），字段名都是业务语言？
- [ ] 焦点环可见？表单 `<label for>` 齐？
- [ ] 移动端 375 下无横向滚动？
- [ ] changelog 已更新？
- [ ] 单文件 ≤ 1200 行？
