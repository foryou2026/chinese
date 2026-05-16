# 28 · H03 AI 输出：HTML 原型规范（极简平铺）

> **阶段**：H HTML 原型
> **谁产出**：AI（HTML 原型工程师）
> **落盘**：`docs/C04-prototype/<feature-id>/`
> **目的**：把本 feature 已冻结的 R / I / N 实化为可点开看的纯 HTML，零依赖、本地双击 `index.html` 就能跑。原型只承担"看一眼默认态、走通跳转"，**不**承担状态穷举（空 / 加载 / 错误 / 无权限由 C05 文字描述承担），更不承担生产工程化。

> **参照范例**：[`function/02-course/ai/F4-AI-原型设计/`](../../function/02-course/ai/F4-AI-原型设计/)——17 个 P-*.html + `index.html` + `_assets/` 平铺于一目录。C04 就照这个模式做，区别仅在于按 surface 拆进 `<surface>/`。

---

## 触发提示词

```
我已答完 H 澄清。请按 /prompt/C-product/C04-H03-AI输出-HTML原型规范.md 输出本 feature 一整套零依赖 HTML 原型，
落盘到 docs/C04-prototype/<feature-id>/。

【极简原则】
- **一个页面 = 一个 HTML**，平铺在 `<surface>/` 根下（或单端 feature 的 feature 根下），**不要**建 `pages/` / `states/` / `assets/` / `vendor/` 等任何子目录。
- **只画默认态**。空 / 加载 / 错误 / 无权限 等状态由 docs/C05-prd/<feature>/ 文字描述承担，**禁止**在原型里出图、禁止生成 `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`。
- **不产出**任何 `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md` 等辅助文件。页面级微调样式 / 微交互一律内联在该 HTML 的 `<style>` / `<script>` 中；全局调性只能回 B04 改。

【运行时资产】
**严禁拷贝**。所有 token / 组件 CSS / 全局交互 JS 必须**通过相对路径直接引用** `docs/B04-design/prototype-style/`，保证全仓单一来源。
统一深度：`<surface>/index.html` 与 `<surface>/<page-id>.html` 均位于 docs 下 3 层（C04-prototype/<feature>/<surface>/），相对路径都是 `../../../B04-design/prototype-style/X`：
  <link rel="stylesheet" href="../../../B04-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../B04-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../B04-design/prototype-style/app.css">
  <script defer src="../../../B04-design/prototype-style/app.js"></script>
  <script>proto.bootstrap();</script>

**例外（上游 AI 原型来源）**：若本 feature 在 `/function/<feature>/ai/F4-AI-原型设计/` 已有上游 AI 生成的成品原型（如 `function/02-course/ai/F4-AI-原型设计/`），HTML **改为引用该上游来源的 `_assets/`** 而非 B04；按其类名与结构在 C04 mirror 文件（仅改 P-ID、不改样式与类名），确保与上游字节等价。路径写 `../../../../function/<feature>/ai/F4-AI-原型设计/_assets/styles.css`（surface 深度 → 4 ups → docs 根 → function/...）。

H01 §3 表里所有 page-id 一次性出齐——每个 page-id 出 1 个默认态 HTML。**禁止**以"分期 / 二期 / 暂不做 / 优先级不高"为由跳过。
本阶段属于产品设计阶段，**严禁**引用、读取或假设任何后续开发阶段产物（架构 / 数据规范 / 接口规范 / 校验规范），也禁止出现真实接口路径、SQL、表名、列名、真实路由路径。
本阶段不产出任何 markdown / changelog 文件；本轮变更说明请直接追入 [docs/A00-meta/changelog.md](docs/A00-meta/changelog.md)。
```

---

## 输出目录

### 双端 feature（推荐形态）

```
docs/C04-prototype/<feature-id>/
  index.html              # feature 级入口（列 app / admin 两张卡片，分别指向 <surface>/index.html）
  _input/
    prototype-direction.md   # H01 用户输入（一次性，覆盖本 feature 全部 page-id）
  app/                    # surface 级原型
    index.html            # 列出本 surface 全部 page-id（每行 1 个 → 1 个 HTML 链接）
    <page-id>.html        # 一个页面 = 一个 HTML，平铺
    ...
  admin/                  # 同 app/
    index.html
    <page-id>.html
    ...
```

### 单端 feature（退化形态）

```
docs/C04-prototype/<feature-id>/
  index.html
  _input/prototype-direction.md
  <page-id>.html          # 直接平铺，无 <surface>/ 一层
  ...
```

> **硬约束**：`<surface>/` 下**只能出 `index.html` + `P-*.html`**。任何 `pages/` / `states/` / `assets/` / `vendor/` / `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md` 都是脏数据，一律在生产前清除。
> H02 澄清清单不在本目录，统一落 `docs/A00-meta/questions/H-<feature-id>-questions-round<N>.md`。

---

## 硬约束

0. **运行时资产唯一来源**：必须**通过相对路径**直接引用 `docs/B04-design/prototype-style/` 内的 `app.css` / `themes.css` / `tokens.css` / `app.js`，**禁止**在 feature 目录下任何位置复制 B04 文件。任何 token / 组件 CSS / 全局交互 JS 的调整都必须直接改 B04 源；因 B04 与该 feature 共用，所有 feature 立即同步生效。
   - 例外：若 feature 在 `/function/<feature>/ai/F4-AI-原型设计/` 有上游 AI 原型，则改引用该上游 `_assets/`；仍不得拷贝。
0.1 **极简平铺**：一个页面 = 一个 HTML，只出默认态。不产出 `pages/` / `states/` / `assets/` 子目录，不产出 `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`。
0.2 **surface 目录只能出 HTML**：不产出任何 `feature.css` / `feature.js` / `mock-data.js`（页面级微调一律内联在对应 HTML 的 `<style>` / `<script>`）；不产出任何 `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md`（阶段说明与变更记录由 docs/C05-prd/ 与 docs/A00-meta/changelog.md 统一承担）。
1. **零外部依赖**：不引 CDN、不用框架、不用打包器。仅原生 HTML + CSS + vanilla JS（通过相对路径引用 B04 本地资产，不算外部依赖）。
2. **字体自托管**（除非 B04 显式允许 CDN；字体走 B04 prototype-style/ 中的约定）。
3. **所有颜色 / 字号 / 间距 / 圆角 / 阴影必须用 CSS 变量**：变量来自 `docs/B04-design/prototype-style/tokens.css` + `themes.css`，**禁止**在 HTML 内联样式重新定义任何 token。
4. **不得发起真实网络请求**。页面上需要展示数据的位置直接在 HTML 中用静态样本插入（可与 C03 §4 的 OP-ID 响应形状对齐，不假设后端字段）。
5. **响应式**：最少在 375 / 768 / 1280 三档下视觉无破。
6. **a11y**：每个交互元素 `:focus-visible` 必有焦点环；表单字段必有 `<label for>`。
7. **页面跳转一律用 `<page-id>.html` 文件锚**（同目录），**禁止**使用任何真实 URL 路径（路由属于 D02 阶段）。
8. **范围一次性出齐**：H01 §3 表里所有 page-id 必须本轮全部产出，**禁止**以"分期 / 二期 / 暂不做 / 优先级低"跳过。如发现某 page-id 在 C03-N 缺规范，应回到澄清提问而非跳过。
9. **单文件 ≤ 1200 行**。

---

## `<surface>/index.html` 规范

- 顶部一句话项目名 + B03 一句话定调
- 表格或卡片网格列出本 surface 全部 page-id，每行 / 每卡 1 个 `<a href="./<page-id>.html">`
- 同时给一句话指引："空 / 加载 / 错误 / 无权限等状态描述见 `../../../C05-prd/<feature>/`"

示例（B04 风格）：

```html
<table>
  <thead><tr><th>page-id</th><th>名称</th><th>入口</th></tr></thead>
  <tbody>
    <tr><td><code>P-app-auth-001</code></td><td>登录</td><td><a href="./P-app-auth-001.html">↗ 打开</a></td></tr>
    ...
  </tbody>
</table>
```

---

## `<surface>/<page-id>.html` 规范

- 顶部 HTML 注释列出：page-id、对应 R-ID、对应 OP-ID（本页交互点）、最后更新时间
- 引入 `../../../B04-design/prototype-style/{tokens,themes,app}.css` + `../../../B04-design/prototype-style/app.js`；`<body>` 末尾调 `proto.bootstrap()`
  - 例外：feature 有 F4 上游资产时，改为 `../../../../function/<feature>/ai/F4-AI-原型设计/_assets/styles.css` 等等价路径
- DOM 结构按 `docs/C03-pages/<feature-id>/<page-id>.md` §3 区块清单
- 每个 Block 加 `data-block="Block-1"` 便于反馈定位
- 每个操作按钮加 `data-op="OP-1"` 便于反馈定位
- 文案直接走 `docs/B03-ux/04-voice-tone.md` 对照表
- 页面需展示的示例数据直接在 HTML 中以静态片段写出（业务语言，不假设后端字段）；**不**产出外部 `mock-data.js`
- **只画默认态**。如该页面在 C03 中有空 / 加载 / 错误 / 无权限态，用文字 / 注释在该 HTML 顶部一句话指引读者去 C05 看，**不**再画一份 `*.empty.html`

---

## 页面级交互 与 示例数据

> 全局交互（modal / drawer / dropdown / toast / 主题切换 …）一律调 B04 prototype-style/app.js 暴露的 `proto.*` API。**不**在 surface 目录下产出任何 `feature.js` / `feature.css` / `mock-data.js`。
> 页面需展示的业务示例数据直接写在 HTML 静态片段中（可与 C03 §4 的 OP-ID 响应形状对齐，字段名用业务语言）。页面级微调样式可内联在 `<style>`；需要交互占位时以内联 `<script>` 调 `proto.*` 实现，例如：

```html
<button data-op="OP-1" onclick="proto.toast({type:'success',msg:'已保存'})">保存</button>
```

> 页面间跳转一律用同目录 `<a href="./<page-id>.html">`；回到 surface 入口用 `<a href="./index.html">`。

---

## 变更记录

> C04 本身不产出 `changelog.md`。本轮原型与上一轮的不同、token 漂移、已知差异等信息一律追入 [`docs/A00-meta/changelog.md`](docs/A00-meta/changelog.md)，按「C04 · <feature>」条目记录。

> **token 漂移规则**：任何颜色 / 字号 / 间距 / 圆角的变化都属于 B04 范畴，必须直接改 `docs/B04-design/design-system/01-tokens.md` 与 `docs/B04-design/prototype-style/tokens.css`（改完后所有 feature 自动生效，无需拷贝），**禁止**在页面内联样式里改。
> **后续修改**：若用户走完 G-H 后又要改原型，沿用本模板重跑 H01→H02→H03（同样一次性出齐）。**不要**在文件名上区分"首版/迭代"。

---

## 输出质量自检

- [ ] H01 §3 表里所有 page-id 是否一次性全部产出？有无以"分期 / 暂不做 / 优先级低"为由跳过？
- [ ] `<surface>/` 下**只**有 `index.html` + `P-*.html`？无任何 `pages/` / `states/` / `assets/` / `vendor/` 子目录？
- [ ] **无任何** `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`？
- [ ] **无任何** `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md`？页面级微调均已内联在对应 HTML 中？
- [ ] 所有 HTML 均通过相对路径引用 `docs/B04-design/prototype-style/`（或 feature 有 F4 上游时引用 `function/<feature>/ai/F4-AI-原型设计/_assets/`）？无任何 B04 副本？
- [ ] HTML 内联 `<style>` 中无任何 token 重定义、无任何 hex / px 硬编码？
- [ ] 双击 `index.html` 在浏览器能跑，无 404、无控制台报错？
- [ ] 所有 page-id 与 `docs/C02-ia/<feature-id>/04-pages.md` 一致？
- [ ] 颜色 / 字号 / 间距 / 圆角全用 CSS 变量（与 docs/B04-design/design-system/01-tokens.md 一致）？
- [ ] 全文未出现任何后续开发阶段产物路径 / 真实接口名 / SQL / 表名 / 列名 / 真实路由路径？
- [ ] 字体自托管（除非 B04 允许 CDN）？
- [ ] 页面示例数据均使用业务语言字段，未出现后端 snake_case / 表列名？
- [ ] 焦点环可见？表单 `<label for>` 齐？
- [ ] 移动端 375 下无横向滚动？
- [ ] 全局 changelog（docs/A00-meta/changelog.md）已追记？
- [ ] 单文件 ≤ 1200 行？
