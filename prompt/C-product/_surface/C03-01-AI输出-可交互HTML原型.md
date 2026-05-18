# C03-01 AI 输出：可交互 HTML 原型

> **阶段**：C03 可交互原型
> **归属**：**按系统独立（_surface）**——每个系统有独立的原型目录和导航
> **步骤**：1 步阶段 —— AI 直接输出（无用户输入步骤）
> **谁产出**：AI（HTML 原型工程师）
> **何时产出**：C01（共享）+ C02（同系统）全部冻结后，AI 基于冻结产物直接生成。
> **落盘**：`C03-prototype/<surface-id>/<module-id>/<feature-id>/<page-id>.html`
> 每轮新增**一个功能**（feature）的页面，更新对应系统→模块的 `index.html` 与 `_shared/proto-nav.html`。

---

## 原型导航结构（四层）

> 用户打开原型时经历四层导航，前三层是"目录"，第四层是"真实演示"。

```
第一层：项目总览          index.html                          列出所有系统卡片
                                ↓ 点击系统
第二层：系统模块目录       <surface>/index.html                 列出该系统下所有模块卡片
                                ↓ 点击模块
第三层：模块功能目录       <surface>/<module>/index.html         列出该模块下所有功能卡片
                                ↓ 点击功能
第四层：演示模式          <surface>/<module>/<feature>/页面      按真实系统交互，无目录
```

### 演示模式规则

- 进入演示模式后**不再出现任何目录层级**，所有页面跳转均按真实业务流程走。
- 每个演示页面**右上角**有一个 **「原型导航」按钮**，点击返回所属模块功能目录页（`<surface>/<module>/index.html`）。
- 演示模式中的所有页面互相跳转、支持返回，感觉就是在用真实系统。
- **同系统内页面互相跳转**；不同系统的页面互相独立，不存在跨系统跳转。

### Web / App 响应式适配

> 每个系统内，如果 C02 UX 规范中该功能同时设计了桌面端和移动端布局，则通过 CSS 响应式实现自适应。

- 无需 Web/App 切换按钮。同一个系统的页面通过 CSS media query 自适应不同屏幕宽度。
- 如果 app 系统和 admin 系统有不同的布局（如 app 偏移动端、admin 偏桌面端），它们本身就是不同系统目录下的独立原型。

---

## 层级说明

| 层级 | 目录位置 | 说明 |
|------|---------|------|
| **项目总览** | `C03-prototype/index.html` | 列出所有系统入口卡片，一次性创建 |
| **系统（surface）** | `C03-prototype/<surface-id>/` | 如 `app`、`admin`；包含 `index.html`（该系统所有模块列表）；**首次为该系统产出时创建** |
| **模块（module）** | `C03-prototype/<surface-id>/<module-id>/` | 如 `auth`、`course`；包含 `index.html` 和 `_shared/`；**首次为该模块产出时创建** |
| **功能（feature）** | `C03-prototype/<surface-id>/<module-id>/<feature-id>/` | 如 `account-entry`、`learning`；**C/D 循环每轮产出一个功能** |

每轮 AI 只产出一个系统的一个功能的页面，必须同时更新所属系统→模块的目录页。

---

## 触发提示词

```
请你扮演"HTML 原型工程师"。
上游冻结产物：C01 共享需求基线、C02 该系统的信息架构与交互规范、B02 体验规范、设计系统。
请按 /prompt/C-product/_surface/C03-01-AI输出-可交互HTML原型.md 输出本轮原型。

本轮围绕系统「<surface-id>」下模块「<module-id>」的功能「<feature-id>」生成原型页面，
落盘到 C03-prototype/<surface-id>/<module-id>/<feature-id>/。
若「<surface-id>/<module-id>」目录不存在，同时创建系统目录、模块目录、index.html 和 _shared/。
必须与同系统内已有页面融合——所有页面可互相跳转、无死链。
引用 B02 输出的 prototype-style/ 样式包（通过相对路径）。
本阶段属于产品设计阶段，严禁引用任何后端实现。
每个原型页面必须实现高保真交互（见规范中"高保真交互标准"一节）。
```

---

## AI 必须遵守

1. **只读**：C01 共享基线（已冻结）+ C02 同系统的交互规范（已冻结）+ B02 体验规范 + B02 prototype-style/ + 同系统已有原型文件（如有）+ 本模板。
2. **C/D 隔离铁律**：严禁引用、读取或假设任何后端实现（接口/表/字段/路由/SQL）。
3. **系统隔离**：不跨系统引用。app 的原型不链接 admin 的页面，反之亦然。
4. **连通性第一**：同系统内每个页面都必须能通过导航或链接到达其他相关页面。不允许死链、孤岛页面。
5. **增量融合**：每轮增加一个功能的原型页面，必须更新同系统内已有页面的导航和链接使之连通。
6. **本地可运行**：通过 `python -m http.server` 在项目根目录启动即可访问全部页面。
7. **高保真交互**：所有页面必须实现业务所需的页面状态交互，用户使用时感觉就是一个真实系统（见下方"高保真交互标准"）。
8. **禁止为弹框单独建页面**：弹框、确认框、抽屉等均在当前页面内实现，不拆成独立 HTML 文件。

---

## 高保真交互标准（Axure 高保真原型级别）

> 原型的目标：让用户感觉在使用一个真实运行的系统，而不是在翻阅静态截图。以下是必须实现的交互类型。

### 1. 页面内导航与返回

- **返回按钮**：凡是从列表/目录跳入的详情页、表单页，**必须**有返回上一页的按钮（或顶部左侧的 `←` 箭头），点击执行 `history.back()` 或跳回明确的来源页。
- **取消按钮**：所有新建/编辑页必须有"取消"按钮，点击返回来源列表页。

### 2. 操作后自动跳转

- **表单提交成功** → 自动跳转到对应结果页（成功页/详情页/列表页），延迟 300–600 ms 模拟网络感。
- **删除确认** → 弹框确认后关闭弹框并执行 DOM 删除动画，无须刷新页面。
- **保存草稿** → toast 提示"已保存草稿"，停留在当前页面。
- **提交审核/发布** → 弹框确认后跳转到状态变更后的详情页或列表页。
- 所有自动跳转使用 `setTimeout(() => location.href = targetPath, delay)` 实现。

### 3. 表单联动（条件显隐）

- 选择了某个选项（如题目类型、媒体类型、权限角色）后，页面上其他相关字段、配置区块必须**立即响应**：
  - 显示/隐藏对应的配置项（`display: none ↔ block`，加过渡动画）。
  - 更新下拉框的可选项（动态替换 `<option>` 列表）。
  - 改变字段的必填/禁用状态（`required`、`disabled` 属性）。
- 实现方式：监听 `change` / `input` 事件，用纯 JS 操作 DOM，无须框架。

### 4. 列表状态管理（类 Axure 中继器）

- **删除行**：点击删除按钮 → 弹确认弹框 → 确认后执行 `row.remove()`，同时更新统计数字（如"共 N 条"）。
- **新增行**：新建表单保存后，返回列表时在列表顶部插入新行（或直接跳转列表页，利用 `sessionStorage` 传递新增标记，页面加载时自动追加高亮行）。
- **状态切换**：启用/禁用、上架/下架等开关，点击后直接在 DOM 中切换状态标签和按钮文案。
- **批量操作**：多选 checkbox 联动"批量删除/导出"按钮的可用状态（`disabled ↔ enabled`）。

### 5. 弹框与抽屉

- **确认弹框**（删除确认、提交审核确认等）：在当前页内用 `<dialog>` 或自定义 `.modal` 实现，点击"确认"执行操作，点击"取消/关闭"关闭弹框。
- **表单弹框**（轻量编辑、快捷填写）：弹框内含完整表单，提交后关闭弹框并更新当前页列表行数据（DOM 原地更新，不跳页）。
- **抽屉/侧滑面板**：从右侧/底部滑出，有关闭按钮，点击遮罩层也可关闭。
- **禁止**：为以上任何弹框单独建立 HTML 页面文件。

### 6. 搜索与筛选即时反馈

- 筛选条件变化后，列表区域立即更新为过滤后的示例数据子集（JS 过滤 DOM 元素的 `display`）。
- 搜索输入框支持 `input` 事件实时过滤（或模拟搜索按钮点击后刷新结果区）。
- 分页按钮点击后，隐藏当前"页"的行，显示对应"页"的行（纯 DOM 切换）。

### 7. 标签页 / 步骤条

- 标签页（Tabs）点击后切换激活状态并显示对应内容区块。
- 步骤条（Stepper）"下一步"/"上一步"按钮控制当前激活步骤，同时显隐对应表单区块。
- 步骤条最后一步的"完成"/"提交"按钮触发跳转或弹框确认。

### 8. 通知与反馈

- **Toast**：操作成功/失败后右上角或顶部出现短暂提示条，2–3 秒后自动消失。
- **内联错误**：表单校验失败时，在对应字段下方显示红色错误文案（不依赖浏览器原生 `alert`）。
- **加载骨架屏**：列表/详情区域首次"加载"时，先显示骨架屏动画（300 ms），再"渲染"示例数据（模拟真实体验）。

### 9. 示例数据规范

- 所有列表、详情页的示例数据**直接写在 HTML 中**（静态 DOM），不发起任何网络请求。
- 示例数据必须**真实且充分**（至少 5–8 条列表数据，字段填写完整），不允许只写"数据占位符"。
- 使用 `sessionStorage` 在页面间传递操作结果标记（如新增成功的 ID），无须后端。

---

## 弹框 vs 跳页判断规则（铁律）

| 场景 | 方式 | 说明 |
|------|------|------|
| **新建**（创建新实体） | **跳页** | 独立新建页，有返回/取消按钮 |
| **编辑**（全字段编辑） | **跳页** | 独立编辑页，有保存/取消按钮 |
| **查看详情**（信息量大） | **跳页** | 独立详情页，有返回按钮 |
| **快捷编辑**（1–3 个字段） | **弹框** | 当前页内 `<dialog>`，提交后原地更新 DOM |
| **删除确认** | **弹框** | 当前页内确认框，确认后 DOM 删除行 |
| **查看详情**（信息量少） | **弹框** | 当前页内抽屉/弹框 |
| **提交/发布确认** | **弹框** | 当前页内确认框 |
| **上传、选择关联对象** | **弹框** | 当前页内选择器弹框 |

> **禁止**将任何弹框类交互拆成独立 HTML 页面。弹框统一在当前页面的 `<script>` 和内联 HTML 中实现。

---

## 功能与页面映射规则

> AI 在规划页面时必须遵守以下映射原则，并在每轮输出时明确给出映射说明。

- **一个功能 → 多个页面**：允许。
- **多个功能 → 一个页面**：允许。如果多个功能共享同一个页面，可以合并为一个 HTML 文件。
- **弹框不算页面**：弹框不单独占用页面文件。
- **新建/编辑必须跳页**：无论功能大小。
- **AI 规划时必须输出映射表**（见验证报告格式）。

---

## 输出目录结构

> 四层组织：系统 → 模块 → 功能 → 页面。每轮迭代新增一个系统下一个功能目录的页面。

```
C03-prototype/
  index.html                                    # 全局总览（列出所有系统，一次性创建）
  _shared/                                      # 跨系统共享资源（如全局样式覆写）
  <surface-id>/                                 # 系统目录（如 app/ admin/）
    index.html                                  # 系统模块目录（列出该系统下所有模块卡片）
    <module-id>/                                # 模块目录（如 auth/ course/）
      index.html                                # 模块功能目录页（列出所有功能卡片）
      _shared/                                  # 模块级共享组件
        proto-nav.html                          # 原型导航组件
      <feature-id>/                             # 功能目录
        <page-id>.html                          # 演示页面
```

### 示例

```
C03-prototype/
  index.html                                    # 全局总览
  app/                                          # 系统：应用端
    index.html                                  # app 系统模块目录
    auth/                                       # 模块：鉴权
      index.html                                # auth 模块功能目录
      _shared/
        proto-nav.html
      account-entry/                            # 功能：账号入口
        P-app-auth-001.html                     # 登录页
        P-app-auth-002.html                     # 注册页
      account-recovery/                         # 功能：账号找回
        P-app-auth-005.html                     # 找回密码页
    course/                                     # 模块：课程
      index.html
      _shared/
        proto-nav.html
      learning/                                 # 功能：学习
        P-app-course-001.html
  admin/                                        # 系统：管理端
    index.html                                  # admin 系统模块目录
    auth/                                       # 模块：鉴权
      index.html
      _shared/
        proto-nav.html
      admin-entry/                              # 功能：管理员入口
        P-admin-auth-001.html
    course/                                     # 模块：课程
      index.html
      _shared/
        proto-nav.html
      content/                                  # 功能：内容管理
        P-admin-course-001.html
```

---

## 核心机制：增量融合

> 每轮产出一个**系统**下一个**功能**的一个或多个页面，必须处理与同系统内已有页面的融合。

### 每轮必须执行的融合步骤

#### 步骤 1：规划功能→页面映射
- 读取 C02 同系统的流程图和操作清单，决定本功能需要哪些页面。
- 明确哪些操作是跳页（新建/编辑），哪些是弹框（确认/快捷编辑）。
- 如果本功能与已有功能共享某些页面，说明合并方案，不重复建文件。
- **输出映射表**（见验证报告）。

#### 步骤 2：生成本轮功能的新页面
- 在 `<surface-id>/<module-id>/<feature-id>/` 下创建新的 HTML 文件。
- 每个页面实现完整的高保真交互（见"高保真交互标准"），不允许只画静态截图。

#### 步骤 3：更新模块共享原型导航组件
- 更新 `<surface-id>/<module-id>/_shared/proto-nav.html`，加入本轮新增页面的入口。
- 导航结构必须与 C02 同系统的 `05-navigation.md` 保持一致。

#### 步骤 4：更新已有页面的出站链接
- 检查同系统内已有页面中是否需要新增指向本轮新页面的链接。
- 具体的链接关系来源于 C02 同系统的流程图和操作清单。

#### 步骤 5：更新目录页
- 更新模块功能目录页（`<surface-id>/<module-id>/index.html`）。
- 如果是该模块的首个功能，还需更新系统模块目录页（`<surface-id>/index.html`）。
- 如果是该系统的首个模块，还需更新项目总览页（`index.html`）。

#### 步骤 6：连通性验证
- 必须输出连通性验证报告（见 §验证报告）。

---

## 页面跳转与导航规范

### 跳转路径计算

所有页面间跳转使用**相对路径**，基于当前文件位置计算：

```
<!-- 同功能目录内：直接同目录 -->
<a href="./P-app-course-002.html">查看详情</a>

<!-- 返回上一页 -->
<button onclick="history.back()">← 返回</button>

<!-- 跨功能跳转（同模块） -->
<a href="../checkout/P-app-order-001.html">去结算</a>

<!-- 返回模块功能目录页（"原型导航"按钮） -->
<a href="../index.html">原型导航</a>

<!-- 返回系统模块目录 -->
<a href="../../index.html">系统目录</a>

<!-- 返回全局项目总览 -->
<a href="../../../index.html">项目总览</a>
```

### 原型导航按钮（演示页面必须包含）

每个演示页面顶部导航**右侧固定区域**必须包含：

```html
<div class="nav-actions">
  <button data-action="toggle-theme" class="btn btn--ghost btn--sm">明/暗</button>
  <!-- 所有演示页面必须有此按钮 -->
  <a data-href="index.html" class="btn btn--primary btn--sm">原型导航</a>
</div>
```

### 共享原型导航组件加载

演示页面在顶部通过 JavaScript fetch 加载 `_shared/proto-nav.html`：

```javascript
const NAV_DEPTH = parseInt(document.querySelector('meta[name="nav-depth"]').content);
const PATH_PREFIX = '../'.repeat(NAV_DEPTH);

fetch(PATH_PREFIX + '_shared/proto-nav.html')
  .then(r => r.text())
  .then(html => {
    document.getElementById('proto-nav-bar').innerHTML = html;
    document.querySelectorAll('#proto-nav-bar [data-href]').forEach(a => {
      a.href = PATH_PREFIX + a.dataset.href;
    });
    const pageId = document.querySelector('meta[name="page-id"]').content;
    const cur = document.querySelector('#proto-nav-bar [data-page="' + pageId + '"]');
    if (cur) cur.classList.add('nav-active');
  });
```

> `nav-depth` 对应当前文件到模块根目录的层数。功能页面 `<surface>/<module>/<feature>/page.html` 距模块根 = 1 层（到 `<module>/`）。

---

## 样式引用规范

### 引用 B02 输出的 prototype-style/

本项目样式包位于 `docs/B02-experience-design/prototype-style/`，从 `C03-prototype/` 出发计算相对路径：

| 页面层级 | 样式引用路径前缀 |
|---------|--------------|
| 项目总览 `C03-prototype/index.html` | `../docs/B02-experience-design/prototype-style/` |
| 系统入口 `<surface>/index.html` | `../../docs/B02-experience-design/prototype-style/` |
| 模块入口 `<surface>/<module>/index.html` | `../../../docs/B02-experience-design/prototype-style/` |
| 功能页面 `<surface>/<module>/<feature>/page.html` | `../../../../docs/B02-experience-design/prototype-style/` |

> **绝不拷贝**样式文件到原型目录。所有 token/组件 CSS/JS 引用 B02 单一来源。

---

## 单页 HTML 规范

### 页面模板

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- 导航深度：从当前文件到模块根目录的层数。<surface>/<module>/<feature>/page.html = 1 层到 <module>/ -->
  <meta name="nav-depth" content="1">
  <!-- 页面元信息 -->
  <meta name="page-id" content="P-app-course-001">
  <meta name="surface-id" content="app">
  <meta name="module-id" content="course">
  <meta name="feature-id" content="learning">
  <meta name="related-r-ids" content="R-course-001,R-course-002">
  <meta name="related-op-ids" content="OP-1,OP-2">
  <title>课程列表 · app · course · learning 原型</title>

  <!-- 样式引用（功能页面距 docs/B02 为 4 层）-->
  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/app.css">

  <style>
    /* 弹框 */
    .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,.45); z-index: 100; align-items: center; justify-content: center; }
    .modal-overlay.is-open { display: flex; }
    /* 行删除动画 */
    @keyframes rowFadeOut { to { opacity: 0; transform: translateX(20px); } }
    .row-removing { animation: rowFadeOut .25s forwards; }
  </style>
</head>
<body>
  <!-- 共享原型导航（fetch 加载） -->
  <div id="proto-nav-bar"></div>

  <!-- 页面主体：按 C02 04-pages.md 的区块清单组织 -->
  <main class="main-content" style="flex:1;padding:var(--space-5)">
    <!-- 页面内容 -->
  </main>

  <!-- 弹框（禁止拆独立页面） -->
  <div class="modal-overlay" id="modal-delete" role="dialog" aria-modal="true">
    <!-- 弹框内容 -->
  </div>

  <script defer src="../../../../docs/B02-experience-design/prototype-style/app.js"></script>
  <script>
    // ── 路径前缀 ──────────────────────────────────────────────
    const NAV_DEPTH = parseInt(document.querySelector('meta[name="nav-depth"]').content);
    const PATH_PREFIX = '../'.repeat(NAV_DEPTH);

    // ── 加载共享原型导航 ──────────────────────────────────────
    fetch(PATH_PREFIX + '_shared/proto-nav.html')
      .then(r => r.text())
      .then(html => {
        document.getElementById('proto-nav-bar').innerHTML = html;
        document.querySelectorAll('#proto-nav-bar [data-href]').forEach(a => {
          a.href = PATH_PREFIX + a.dataset.href;
        });
        const pageId = document.querySelector('meta[name="page-id"]').content;
        const cur = document.querySelector('#proto-nav-bar [data-page="' + pageId + '"]');
        if (cur) cur.classList.add('nav-active');
      });

    // ── 弹框管理 ──────────────────────────────────────────────
    const ProtoModal = {
      open(id) { document.getElementById(id).classList.add('is-open'); },
      close(id) { document.getElementById(id).classList.remove('is-open'); }
    };
    document.querySelectorAll('.modal-overlay').forEach(overlay => {
      overlay.addEventListener('click', e => { if (e.target === overlay) overlay.classList.remove('is-open'); });
    });

    // ── Toast ─────────────────────────────────────────────────
    const ProtoToast = {
      show(msg, type = 'success') {
        const el = document.createElement('div');
        el.textContent = msg;
        Object.assign(el.style, {
          position:'fixed', top:'16px', right:'16px', zIndex:'9999',
          padding:'8px 16px', borderRadius:'6px', color:'#fff', fontSize:'14px',
          background: type === 'success' ? 'var(--color-success, #18a058)' : 'var(--color-danger, #d03050)',
          boxShadow:'0 2px 8px rgba(0,0,0,.18)', transition:'opacity .3s'
        });
        document.body.appendChild(el);
        setTimeout(() => { el.style.opacity = '0'; setTimeout(() => el.remove(), 300); }, 2200);
      }
    };

    // ── 初始化 ────────────────────────────────────────────────
    if (typeof proto !== 'undefined') proto.bootstrap();
  </script>
</body>
</html>
```

---

## `_shared/proto-nav.html` 规范

```html
<!-- 原型导航组件，被各演示页面 fetch 加载 -->
<!-- 所有链接使用 data-href（从模块根目录出发的路径），由加载脚本修正为实际相对路径 -->
<nav class="topnav glass-nav" role="navigation" aria-label="原型导航"
  style="display:flex;align-items:center;gap:var(--space-3);padding:0 var(--space-4);height:56px;position:sticky;top:0;z-index:50">

  <!-- 业务导航链接（按 C02 同系统 05-navigation.md 生成） -->
  <ul class="nav-links" role="list" style="display:flex;gap:var(--space-2);list-style:none;margin:0;padding:0;flex:1">
    <li><a data-href="account-entry/P-app-auth-001.html" data-page="P-app-auth-001" class="nav-link">登录</a></li>
    <li><a data-href="account-recovery/P-app-auth-005.html" data-page="P-app-auth-005" class="nav-link">找回密码</a></li>
    <!-- 增量轮次：新增功能的导航项加在对应位置 -->
  </ul>

  <!-- 右上角固定操作区 -->
  <div class="nav-actions" style="display:flex;align-items:center;gap:var(--space-2)">
    <button data-action="toggle-theme" class="btn btn--ghost btn--sm">明/暗</button>
    <!-- 原型导航：回到模块功能目录页 -->
    <a data-href="index.html" class="btn btn--primary btn--sm proto-home-btn">原型导航</a>
  </div>
</nav>
```

---

## 系统模块目录页 `<surface>/index.html` 规范

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[surface 名] · 系统模块目录 · 可交互原型</title>
  <link rel="stylesheet" href="../../docs/B02-experience-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../docs/B02-experience-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../docs/B02-experience-design/prototype-style/app.css">
</head>
<body>
  <header class="topnav glass-nav"
    style="display:flex;align-items:center;gap:var(--space-3);padding:0 var(--space-4);height:56px">
    <a href="../index.html" class="btn btn--ghost btn--sm">← 项目总览</a>
    <span style="flex:1;font-weight:600">[项目名] · [surface 名]</span>
    <button data-action="toggle-theme" class="btn btn--ghost btn--sm">明/暗</button>
  </header>

  <main style="max-width:900px;margin:0 auto;padding:var(--space-6)">
    <h1>[surface 名] · 模块目录</h1>
    <p class="lead">点击模块卡片进入该模块的功能列表。</p>

    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:var(--space-4);margin-top:var(--space-5)">
      <!-- 每个模块一张卡片 -->
      <a href="./auth/index.html" class="glass-card" style="padding:var(--space-5);text-decoration:none;color:inherit">
        <h3>鉴权 (auth)</h3>
        <p style="font-size:var(--text-sm);color:var(--color-text-secondary)">登录、注册、找回密码、个人中心</p>
      </a>

      <!-- 增量轮次：新增模块的卡片加在此处 -->
    </div>
  </main>

  <script defer src="../../docs/B02-experience-design/prototype-style/app.js"></script>
  <script>if (typeof proto !== 'undefined') proto.bootstrap();</script>
</body>
</html>
```

---

## 模块功能目录页 `<surface>/<module>/index.html` 规范

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="nav-depth" content="0">
  <title>[module 名] · [surface 名] · 功能目录 · 可交互原型</title>
  <link rel="stylesheet" href="../../../docs/B02-experience-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../docs/B02-experience-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../docs/B02-experience-design/prototype-style/app.css">
</head>
<body>
  <header class="topnav glass-nav"
    style="display:flex;align-items:center;gap:var(--space-3);padding:0 var(--space-4);height:56px">
    <a href="../index.html" class="btn btn--ghost btn--sm">← [surface 名] 目录</a>
    <span style="flex:1;font-weight:600">[项目名] · [surface 名] · [module 名]</span>
    <button data-action="toggle-theme" class="btn btn--ghost btn--sm">明/暗</button>
  </header>

  <main style="max-width:900px;margin:0 auto;padding:var(--space-6)">
    <h1>[module 名] · 功能目录</h1>
    <p class="lead">点击功能卡片进入演示。演示过程中点击右上角「原型导航」可随时返回此页。</p>

    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:var(--space-4);margin-top:var(--space-5)">

      <!-- 每个功能一张卡片 -->
      <div class="glass-card" style="padding:var(--space-5)">
        <h3>账号入口 (account-entry)</h3>
        <p style="font-size:var(--text-sm);color:var(--color-text-secondary)">登录、注册、手机验证</p>
        <ul style="list-style:none;padding:0;margin-top:var(--space-3)">
          <li><a href="./account-entry/P-app-auth-001.html">登录页 →</a></li>
          <li><a href="./account-entry/P-app-auth-002.html">注册页 →</a></li>
        </ul>
      </div>

      <!-- 增量轮次：新增功能的卡片加在此处 -->

    </div>
  </main>

  <script defer src="../../../docs/B02-experience-design/prototype-style/app.js"></script>
  <script>if (typeof proto !== 'undefined') proto.bootstrap();</script>
</body>
</html>
```

---

## 增量融合操作手册

> AI 每轮必须按以下清单执行，逐项打勾。

### 新增功能时的完整操作清单

- [ ] **规划映射表**：明确本功能有几个页面，哪些操作是弹框，哪些是跳页
- [ ] **创建功能目录**：`<surface-id>/<module-id>/<feature-id>/`
- [ ] **生成新页面**：每个页面实现完整高保真交互，包含 `proto-nav-bar`、返回按钮、弹框、联动等
- [ ] **更新 `_shared/proto-nav.html`**：加入新页面的导航项
- [ ] **更新已有页面的出站链接**（同系统内）：
  - 检查 C02 同系统流程图，找出已有页面中需要跳转到新页面的操作
  - 在对应的已有 HTML 中添加 `<a>` 或 `<button>` 跳转
- [ ] **更新模块功能目录页** `<surface-id>/<module-id>/index.html`
- [ ] **如果是新模块**：更新系统模块目录页 `<surface-id>/index.html`
- [ ] **如果是新系统**：更新项目总览页 `index.html`
- [ ] **验证连通性**：输出连通性验证报告

### 已有页面的变更规则

| 变更类型 | 操作 |
|---------|------|
| 新增出站链接 | 在同系统已有 HTML 对应 Block 中插入链接/按钮 |
| 导航项变更 | 修改 `<surface>/<module>/_shared/proto-nav.html` |
| 页面路径一旦落盘 | 不允许重命名——直接破坏已有链接 |

---

## 连通性验证报告（每轮必须输出）

```markdown
## 连通性验证报告 · 第 N 轮 · 系统「<surface-id>」· 模块「<module-id>」· 功能「<feature-id>」

### 功能→页面映射表
| 功能 | 页面文件 | 类型 | 弹框列表（不独立建文件） |
|------|---------|------|------------------------|
| account-entry | P-app-auth-001.html | 跳页（独立） | 忘记密码弹框（当前页内） |
| account-entry | P-app-auth-002.html | 跳页（独立） | — |

### 页面清单
| page-id | 路径 | 状态 |
|---------|------|------|
| P-app-auth-001 | app/auth/account-entry/P-app-auth-001.html | ✅ 已有 |
| P-app-auth-005 | app/auth/account-recovery/P-app-auth-005.html | 🆕 本轮新增 |

### 链接矩阵（从→到）
| 从 | 到 | 链接方式 | 状态 |
|------|------|---------|------|
| P-app-auth-001 | P-app-auth-005 | "忘记密码"链接 | ✅ 已连通 |
| P-app-auth-005 | P-app-auth-001 | "← 返回登录"按钮 | ✅ 已连通 |
| 所有演示页面 | 模块 index.html | 「原型导航」按钮 | ✅ 已连通 |

### 死链检查
- [ ] 所有 `<a href>` 目标文件都存在？
- [ ] 所有 `data-href` 目标文件都存在？
- [ ] 从 `<surface>/<module>/index.html` 出发能到达所有页面？
- [ ] 每个演示页面都有「原型导航」按钮？
- [ ] 每个详情页/表单页都有返回按钮？

### 系统隔离检查
- [ ] 没有跨系统的链接（app 页面不链接 admin 页面）？

### 死链数量：0
### 孤岛页面数量：0
```

---

## 硬约束

0. **系统隔离**：不同系统的原型互相独立，不存在跨系统链接。
1. **同系统连通性**：同系统内所有页面必须可互相跳转，每个演示页面有「原型导航」按钮，每个详情/表单页有返回按钮。
2. **本地运行**：通过 `python -m http.server` 在 C03-prototype 目录启动即可访问。不依赖 CDN、不用框架、不用打包器。
3. **样式单一来源**：所有 token/组件 CSS/JS 通过相对路径引用 `docs/B02-experience-design/prototype-style/`，不拷贝。
4. **CSS 变量**：所有颜色/字号/间距/圆角/阴影必须用 CSS 变量，不硬编码。
5. **无真实网络请求**：示例数据直接写在 HTML 静态片段中，可用 `sessionStorage` 传递页面间状态。
6. **响应式**：375 / 768 / 1280 三档无破。
7. **a11y**：`:focus-visible` 焦点环、`<label for>`、语义化标签。
8. **高保真交互**：删除后行消失、表单联动、弹框在当前页、跳转有延迟动画感——必须实现。
9. **禁止弹框独立成页**：任何弹框类交互禁止单独建 HTML 文件。
10. **新建/编辑必须跳页**：无例外。
11. **增量不破坏**：新增页面不能破坏同系统内已有页面的功能和链接。
12. **单文件 ≤ 1200 行**。
13. **不产出辅助文件**：不产出 feature.css / feature.js / mock-data.js / README.md。页面级逻辑内联在 HTML 的 `<style>` / `<script>` 中。

---

## 输出质量自检

### 目录结构
- [ ] 原型在 `C03-prototype/<surface-id>/<module-id>/<feature-id>/` 下？
- [ ] 全局 `index.html` 列出所有系统卡片？
- [ ] 系统 `<surface>/index.html` 列出所有模块卡片？
- [ ] 模块 `<surface>/<module>/index.html` 列出所有功能卡片？

### 高保真交互
- [ ] 列表页：搜索/筛选有即时反馈？
- [ ] 列表页：删除行后 DOM 数据消失、计数更新？
- [ ] 表单页：有返回/取消按钮？提交成功后自动跳转？
- [ ] 详情页：有返回上一页按钮（← 返回）？
- [ ] 有条件显隐的表单：选项变化后配置区块立即响应？
- [ ] 弹框：在当前页内实现，点击遮罩可关闭？
- [ ] 所有操作有 Toast 反馈（成功/失败）？

### 连通性与系统隔离
- [ ] 连通性验证报告已输出？死链数为 0？孤岛数为 0？
- [ ] 同系统内从模块目录出发能到达所有演示页面？
- [ ] 没有跨系统链接？
- [ ] 所有 C02 同系统流程图中的页面跳转都有对应链接？

### 增量融合
- [ ] 同系统内已有页面的出站链接已更新？
- [ ] `_shared/proto-nav.html` 已更新？
- [ ] 模块功能目录页已更新？

### 样式与约束
- [ ] 所有 HTML 通过相对路径引用 `docs/B02` prototype-style/？无拷贝？
- [ ] HTML 中无 hex / px 硬编码？全用 CSS 变量？
- [ ] 通过 `python -m http.server` 可正常访问所有页面？
- [ ] 375 下无横向滚动？
- [ ] 焦点环可见？表单 `<label for>` 齐？
- [ ] 全文未出现接口名 / SQL / 表名 / 字段名 / 真实路由路径？
- [ ] 页面 ID 带 surface 前缀（`P-<surface>-<module>-<seq3>`）？
- [ ] 单文件 ≤ 1200 行？
