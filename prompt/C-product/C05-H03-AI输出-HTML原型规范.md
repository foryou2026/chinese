# 28 · H03 AI 输出：HTML 原型规范（极简平铺）

> **阶段**：H HTML 原型
> **谁产出**：AI（HTML 原型工程师）
> **落盘**：`docs/C05-prototype/<feature-id>/`
> **目的**：把本 feature 已冻结的 R / I / N 实化为可点开看的纯 HTML，零依赖、本地双击 `index.html` 就能跑。原型只承担"看一眼默认态、走通跳转"，**不**承担状态穷举（空 / 加载 / 错误 / 无权限由 C05 文字描述承担），更不承担生产工程化。

> **样式依赖**：运行时 CSS / JS 资产统一从 [`docs/B03-design/prototype-style/`](../../docs/B03-design/prototype-style/) 相对路径引用（允许 feature 专属包放在 `prototype-style/<feature>/`），永远不拷贝、不依赖任何 `/function/` 下游。

---

## 触发提示词

```
我已答完 H 澄清。请按 /prompt/C-product/C05-H03-AI输出-HTML原型规范.md 输出本 feature 一整套零依赖 HTML 原型，
落盘到 docs/C05-prototype/<feature-id>/。

【极简原则】
- **一个页面 = 一个 HTML**，平铺在 `<surface>/` 根下（或单端 feature 的 feature 根下），**不要**建 `pages/` / `states/` / `assets/` / `vendor/` 等任何子目录。
- **只画默认态**。空 / 加载 / 错误 / 无权限 等状态由 docs/C06-prd/<feature>/ 文字描述承担，**禁止**在原型里出图、禁止生成 `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`。
- **不产出**任何 `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md` 等辅助文件。页面级微调样式 / 微交互一律内联在该 HTML 的 `<style>` / `<script>` 中；全局调性只能回 B04 改。

【运行时资产】
**严禁拷贝**。所有 token / 组件 CSS / 全局交互 JS 必须**通过相对路径直接引用** `docs/B03-design/prototype-style/`，保证全仓单一来源。
统一深度：`<surface>/index.html` 与 `<surface>/<page-id>.html` 均位于 docs 下 3 层（C05-prototype/<feature>/<surface>/），相对路径都是 `../../../B03-design/prototype-style/X`：
  <link rel="stylesheet" href="../../../B03-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../B03-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../B03-design/prototype-style/app.css">
  <script defer src="../../../B03-design/prototype-style/app.js"></script>
  <script>proto.bootstrap();</script>

**可选的 feature 专属样式包**：若本 feature 沿用一套专属视觉结构（类名 / 主题），允许在 `docs/B03-design/prototype-style/<feature>/` 下放置 `styles.css` / `prototype.js`，HTML 引用路径仍为 `../../../B03-design/prototype-style/<feature>/X`（3 ups，只引用、不拷贝）。**绝不**引用 `/function/` 下任何路径。

H01 §3 表里所有 page-id 一次性出齐——每个 page-id 出 1 个默认态 HTML。**禁止**以"分期 / 二期 / 暂不做 / 优先级不高"为由跳过。
本阶段属于产品设计阶段，**严禁**引用、读取或假设任何后续开发阶段产物（架构 / 数据规范 / 接口规范 / 校验规范），也禁止出现真实接口路径、SQL、表名、列名、真实路由路径。
本阶段不产出任何 markdown / changelog 文件；本轮变更说明请直接追入 [docs/A00-meta/changelog.md](docs/A00-meta/changelog.md)。
```

---

## 输出目录

### 双端 feature（推荐形态）

```
docs/C05-prototype/<feature-id>/
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
docs/C05-prototype/<feature-id>/
  index.html
  _input/prototype-direction.md
  <page-id>.html          # 直接平铺，无 <surface>/ 一层
  ...
```

> **硬约束**：`<surface>/` 下**只能出 `index.html` + `P-*.html`**。任何 `pages/` / `states/` / `assets/` / `vendor/` / `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md` 都是脏数据，一律在生产前清除。
> H02 澄清清单不在本目录，统一落 `docs/A00-meta/questions/H-<feature-id>-questions-round<N>.md`。

---

## 硬约束

0. **运行时资产唯一来源**：必须**通过相对路径**直接引用 `docs/B03-design/prototype-style/` 内的 `app.css` / `themes.css` / `tokens.css` / `app.js`，**禁止**在 feature 目录下任何位置复制 B04 文件，**禁止**引用 `/function/` 下任何资产。任何 token / 组件 CSS / 全局交互 JS 的调整都必须直接改 B04 源；因 B04 与该 feature 共用，所有 feature 立即同步生效。
   - 允许：feature 专属样式包放在 `docs/B03-design/prototype-style/<feature>/` 下，引用路径同为 3 ups。
0.1 **极简平铺**：一个页面 = 一个 HTML，只出默认态。不产出 `pages/` / `states/` / `assets/` 子目录，不产出 `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`。
0.2 **surface 目录只能出 HTML**：不产出任何 `feature.css` / `feature.js` / `mock-data.js`（页面级微调一律内联在对应 HTML 的 `<style>` / `<script>`）；不产出任何 `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md`（阶段说明与变更记录由 docs/C06-prd/ 与 docs/A00-meta/changelog.md 统一承担）。
1. **零外部依赖**：不引 CDN、不用框架、不用打包器。仅原生 HTML + CSS + vanilla JS（通过相对路径引用 B04 本地资产，不算外部依赖）。
2. **字体自托管**（除非 B04 显式允许 CDN；字体走 B04 prototype-style/ 中的约定）。
3. **所有颜色 / 字号 / 间距 / 圆角 / 阴影必须用 CSS 变量**：变量来自 `docs/B03-design/prototype-style/tokens.css` + `themes.css`，**禁止**在 HTML 内联样式重新定义任何 token。
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
- 同时给一句话指引："空 / 加载 / 错误 / 无权限等状态描述见 `../../../C06-prd/<feature>/`"

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
- 引入 `../../../B03-design/prototype-style/{tokens,themes,app}.css` + `../../../B03-design/prototype-style/app.js`；`<body>` 末尾调 `proto.bootstrap()`
  - 允许：feature 专属样式包放在 `docs/B03-design/prototype-style/<feature>/` 下，HTML 引用同样 3 ups。
- DOM 结构按 `docs/C04-pages/<feature-id>/<page-id>.md` §3 区块清单
- 每个 Block 加 `data-block="Block-1"` 便于反馈定位
- 每个操作按钮加 `data-op="OP-1"` 便于反馈定位
- 文案直接走 `docs/B02-ux/04-voice-tone.md` 对照表
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

> **token 漂移规则**：任何颜色 / 字号 / 间距 / 圆角的变化都属于 B04 范畴，必须直接改 `docs/B03-design/design-system/01-tokens.md` 与 `docs/B03-design/prototype-style/tokens.css`（改完后所有 feature 自动生效，无需拷贝），**禁止**在页面内联样式里改。
> **后续修改**：若用户走完 G-H 后又要改原型，沿用本模板重跑 H01→H02→H03（同样一次性出齐）。**不要**在文件名上区分"首版/迭代"。

---

## 输出质量自检

- [ ] H01 §3 表里所有 page-id 是否一次性全部产出？有无以"分期 / 暂不做 / 优先级低"为由跳过？
- [ ] `<surface>/` 下**只**有 `index.html` + `P-*.html`？无任何 `pages/` / `states/` / `assets/` / `vendor/` 子目录？
- [ ] **无任何** `*.empty.html` / `*.loading.html` / `*.error.html` / `*.forbidden.html`？
- [ ] **无任何** `feature.css` / `feature.js` / `mock-data.js` / `README.md` / `00-index.md` / `changelog.md` / `99-open-questions.md`？页面级微调均已内联在对应 HTML 中？
- [ ] 所有 HTML 均通过相对路径引用 `docs/B03-design/prototype-style/`（包含可选 feature 子目录）？无任何 B04 副本？无任何 `/function/` 路径引用？
- [ ] HTML 内联 `<style>` 中无任何 token 重定义、无任何 hex / px 硬编码？
- [ ] 双击 `index.html` 在浏览器能跑，无 404、无控制台报错？
- [ ] 所有 page-id 与 `docs/C03-ia/<feature-id>/04-pages.md` 一致？
- [ ] 颜色 / 字号 / 间距 / 圆角全用 CSS 变量（与 docs/B03-design/design-system/01-tokens.md 一致）？
- [ ] 全文未出现任何后续开发阶段产物路径 / 真实接口名 / SQL / 表名 / 列名 / 真实路由路径？
- [ ] 字体自托管（除非 B04 允许 CDN）？
- [ ] 页面示例数据均使用业务语言字段，未出现后端 snake_case / 表列名？
- [ ] 焦点环可见？表单 `<label for>` 齐？
- [ ] 移动端 375 下无横向滚动？
- [ ] 全局 changelog（docs/A00-meta/changelog.md）已追记？
- [ ] 单文件 ≤ 1200 行？

---

## 三级引导页（index.html）统一规范【强制】

> 所有 `index.html` 入口必须遵循三级层级与同一主题骨架；**不允许**临时手写风格不一致的引导页。

### 1. 三级层级（缺一不可）

| 层级 | 路径 | 作用 |
|------|------|------|
| L1 全局 | `docs/C05-prototype/index.html` | 列出本仓的所有 feature（卡片网格） |
| L2 feature | `docs/C05-prototype/<feature>/index.html` | 列出该 feature 的所有 surface（卡片网格）；单端时也保留本页，仅一张卡 |
| L3 surface | `docs/C05-prototype/<feature>/<surface>/index.html` | 列出该 surface 下所有页面（表格） |

### 2. 共同骨架（每一级 index.html 都必须有）

- `<!DOCTYPE html>` + `lang="zh-CN"` + `<meta name="viewport" content="width=device-width, initial-scale=1">`
- `data-theme="light"` 默认；通过 `app.js` 的 `proto.bootstrap()` 接管主题切换
- 引入三件套（按相对路径，从 L1/L2/L3 计算返回到 `docs/B03-design/prototype-style/`）：
  - `tokens.css`、`themes.css`、`app.css`
  - `app.js`（在底部 `<body>` 末尾，`defer` 可选）
- 顶部 `<header class="topnav glass-nav">`：
  - 左：品牌徽标 + 项目名
  - 中：弹性占位
  - 右：`<button data-action="toggle-theme" class="btn btn--ghost">明/暗</button>`
- 紧随其后：面包屑（首页 → feature → surface，按当前层级裁剪）
- Hero 区：`<h1>` 标题 + 一段说明（`p.lead`）+ 若干 chips（feature 数 / surface 数 / 页面数 / 最后更新）
- Footer：版权 + 一行约束声明（如「本目录为静态原型，未接入真实接口」）

### 3. 主体内容形式

- **L1 全局** / **L2 feature**：用 `.glass-card` 卡片网格（`grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`），每张卡 = 标题 + 简介 + 进入按钮 `<a class="btn btn--primary">`。
- **L3 surface**：用 `<table class="data-table">`，列顺序固定：`Page ID | 页面名称 | 路由 | 操作`；操作列放「打开 ↗」链接，跳转到同目录 `./P-*.html`。

### 4. 路径与样式硬约束

- 三件套引用必须走 `B03-design/prototype-style/`；**禁止**写绝对路径、CDN 路径或 `/function/...`。
- **禁止**在 `index.html` 内联硬编码颜色 / 字号 / 间距；一律 `var(--space-*) / var(--text-*) / var(--color-*) / var(--motion-*)`。
- **禁止**新增 `index.css` / `index.js` / `landing.css`；任何动效与交互复用 `app.css` / `app.js`。

### 5. 自检（追加至「输出质量自检」一并执行）

- [ ] L1 / L2 / L3 三层 `index.html` 是否齐全？
- [ ] 顶栏是否为 `topnav glass-nav` + `data-action="toggle-theme"` 按钮？
- [ ] 三件套相对路径是否正确？刷新页面后主题切换正常工作？
- [ ] L1 / L2 是否使用 `.glass-card` 网格？L3 是否使用统一表格？
- [ ] 是否无 hex / px 硬编码、无内联 `<style>` 重定义 token？
