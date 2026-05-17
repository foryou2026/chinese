# C03-01 AI 输出：可交互 HTML 原型

> **阶段**：C03 可交互原型
> **步骤**：1 步阶段 —— AI 直接输出（无用户输入步骤）
> **谁产出**：AI（HTML 原型工程师）
> **何时产出**：C01 + C02 全部冻结后，AI 基于冻结产物直接生成。
> **落盘**：`C03-prototype/<feature-id>/`

---

## 与旧版的核心差异

| 维度 | 旧版（C05） | 新版（C03） |
|------|-----------|-----------|
| 步骤 | 3 步（用户输入→AI 澄清→AI 输出） | 1 步（AI 直接输出） |
| 页面关系 | 孤立单页 HTML | **可交互跳转的连通 HTML 原型** |
| 运行方式 | 双击 index.html | **`python -m http.server` 本地运行** |
| 输出粒度 | 按 surface 平铺 | **按功能组织目录，每功能下按端拆分** |
| 增量机制 | 一次性出齐 | **每轮增加一个功能的原型页面，与已有页面融合** |

---

## 触发提示词

```
请你扮演"HTML 原型工程师"。
上游冻结产物：C01 需求与权限基线、C02 信息架构与交互规范、B02 体验规范、B03 设计系统。
请按 /prompt/C-product/C03-01-AI输出-可交互HTML原型.md 输出本轮原型，
落盘到 C03-prototype/<feature-id>/。

本轮围绕功能「<功能名>」生成原型页面。
必须与已有页面融合——所有页面可互相跳转、无死链。
引用 B02 输出的 prototype-style/ 样式包（通过相对路径）。
本阶段属于产品设计阶段，严禁引用任何后端实现。
```

---

## AI 必须遵守

1. **只读**：C01 基线（已冻结）+ C02 架构与交互规范（已冻结）+ B02 体验规范 + B03 设计系统 + B03 prototype-style/ + 已有原型文件（如有）+ 本模板。
2. **C/D 隔离铁律**：严禁引用、读取或假设任何后端实现（接口/表/字段/路由/SQL）。
3. **连通性第一**：每个页面都必须能通过导航或链接到达其他相关页面。不允许死链、孤岛页面。
4. **增量融合**：每轮增加一个功能的原型页面，必须更新已有页面的导航和链接使之连通。
5. **本地可运行**：通过 `python -m http.server` 在项目根目录启动即可访问全部页面。

---

## 输出目录结构

> 按功能组织，每功能下按端拆分。

```
C03-prototype/<feature-id>/
  index.html                          # feature 总入口（列出所有功能和页面链接）
  _shared/                            # 共享组件片段
    nav.html                          # 全局导航组件（被各页面 fetch 加载）
    footer.html                       # 全局 footer（可选）
  <功能名-kebab>/                      # 按功能组织的目录
    <surface>/                        # 按端拆分
      <page-id>.html                  # 具体页面
    <surface>/
      <page-id>.html
  <功能名-kebab>/
    ...
```

### 示例

```
C03-prototype/order-mgmt/
  index.html
  _shared/
    nav.html
    footer.html
  browse/                             # 功能：课程浏览
    app/
      P-order-001.html                # 课程列表
      P-order-002.html                # 课程详情
  checkout/                           # 功能：下单结算
    app/
      P-order-010.html                # 订单确认
      P-order-011.html                # 支付结果
    admin/
      P-order-040.html                # 订单管理列表
```

---

## 核心机制：增量融合

> 这是新版原型的最关键机制。每轮产出一个功能的页面，必须处理与已有页面的融合。

### 每轮必须执行的融合步骤

#### 步骤 1：生成本轮功能的新页面
- 在对应功能目录下创建新的 HTML 文件
- 每个页面只画默认态（空/加载/错误态由 C02 文字承担）

#### 步骤 2：更新共享导航组件
- 更新 `_shared/nav.html`，加入本轮新增页面的导航入口
- 导航结构必须与 C02 `05-navigation.md` 保持一致

#### 步骤 3：更新已有页面的链接
- 检查已有页面中是否需要新增指向本轮新页面的链接
- 例如：已有课程详情页需要新增"加入课程"按钮指向新增的订单确认页
- 具体的链接关系来源于 C02 流程图和操作清单

#### 步骤 4：更新 index.html 总入口
- 在 feature 总入口页面中加入本轮新增功能的卡片/链接

#### 步骤 5：连通性验证
- 必须输出连通性验证报告（见 §验证报告）

---

## 页面跳转与导航规范

### 跳转路径计算

所有页面间跳转使用**相对路径**，基于当前文件位置计算：

```
<!-- 同功能同端：直接同目录 -->
<a href="./P-order-011.html">支付结果</a>

<!-- 跨功能同端：相对路径回溯 -->
<a href="../../browse/app/P-order-001.html">返回课程列表</a>

<!-- 跨功能跨端：相对路径回溯 -->
<a href="../../checkout/admin/P-order-040.html">管理后台</a>

<!-- 回到总入口 -->
<a href="../../index.html">首页</a>
```

### 共享导航组件加载

每个页面在 `<body>` 开头通过 JavaScript fetch 加载共享导航：

```html
<div id="global-nav"></div>
<script>
  // 计算相对路径到 _shared/nav.html
  // 深度取决于当前页面位置：功能/端/页面 = 2 层
  fetch('../../_shared/nav.html')
    .then(r => r.text())
    .then(html => {
      document.getElementById('global-nav').innerHTML = html;
      // 修正导航中的相对路径
      fixNavLinks(document.getElementById('global-nav'));
    });
</script>
```

> 这就是为什么需要 `python -m http.server` 而非双击打开——fetch 本地文件需要 HTTP 服务。

### 导航路径修正

`_shared/nav.html` 中的链接使用占位路径，由加载脚本根据当前页面深度动态修正：

```html
<!-- nav.html 中使用 data-href 存储从 feature 根目录出发的路径 -->
<a data-href="browse/app/P-order-001.html">课程列表</a>
<a data-href="checkout/app/P-order-010.html">订单确认</a>
<a data-href="index.html">首页</a>
```

```javascript
function fixNavLinks(container) {
  // 当前页面相对于 feature 根目录的深度
  const depth = getCurrentDepth(); // 根据 <meta name="nav-depth"> 获取
  const prefix = '../'.repeat(depth);
  container.querySelectorAll('a[data-href]').forEach(a => {
    a.href = prefix + a.dataset.href;
  });
}
```

---

## 样式引用规范

### 引用 B02 输出的 prototype-style/

所有页面通过相对路径引用 `B02-ux/prototype-style/` 或 `B03-design/prototype-style/`（取决于项目实际结构）：

```html
<!-- 从 C03-prototype/<feature>/功能/端/页面.html 出发 -->
<!-- 需要回溯到项目根目录再进入样式目录 -->
<!-- 具体层数取决于项目目录结构，统一用 <meta> 声明 -->
<meta name="style-base" content="../../../../B03-design/prototype-style/">

<link rel="stylesheet" href="../../../../B03-design/prototype-style/tokens.css">
<link rel="stylesheet" href="../../../../B03-design/prototype-style/themes.css">
<link rel="stylesheet" href="../../../../B03-design/prototype-style/app.css">
<script defer src="../../../../B03-design/prototype-style/app.js"></script>
```

> **绝不拷贝**样式文件到原型目录。所有 token/组件 CSS/JS 引用 B03 单一来源。

---

## 单页 HTML 规范

### 页面模板

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- 导航深度：从当前文件到 feature 根目录的层数 -->
  <meta name="nav-depth" content="2">
  <!-- 页面元信息 -->
  <meta name="page-id" content="P-order-010">
  <meta name="feature-id" content="order-mgmt">
  <meta name="function" content="checkout">
  <meta name="surface" content="app">
  <meta name="related-r-ids" content="R-010,R-011">
  <meta name="related-op-ids" content="OP-1,OP-2">
  <title>[页面名] · [feature 名] 原型</title>

  <!-- 样式引用（相对路径到 B03 prototype-style） -->
  <link rel="stylesheet" href="../../../../B03-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../../B03-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../../B03-design/prototype-style/app.css">

  <!-- 页面级微调（仅在此内联，不产出外部 CSS） -->
  <style>
    /* 页面特有的微调样式，使用 CSS 变量，不硬编码 */
  </style>
</head>
<body>
  <!-- 共享导航（fetch 加载） -->
  <div id="global-nav"></div>

  <!-- 页面主体：按 C02 04-pages.md 的区块清单组织 -->
  <main>
    <section data-block="Block-1">
      <!-- Block 内容，示例数据直接写在 HTML 中 -->
    </section>
    <section data-block="Block-2">
      <!-- 操作按钮加 data-op 便于定位 -->
      <button data-op="OP-1" onclick="proto.toast({type:'success',msg:'已保存'})">保存</button>
    </section>
  </main>

  <!-- 共享 footer（可选） -->
  <div id="global-footer"></div>

  <!-- 脚本 -->
  <script defer src="../../../../B03-design/prototype-style/app.js"></script>
  <script>
    // 加载共享导航
    const depth = parseInt(document.querySelector('meta[name="nav-depth"]').content);
    const prefix = '../'.repeat(depth);

    fetch(prefix + '_shared/nav.html')
      .then(r => r.text())
      .then(html => {
        document.getElementById('global-nav').innerHTML = html;
        // 修正导航链接的相对路径
        document.querySelectorAll('#global-nav a[data-href]').forEach(a => {
          a.href = prefix + a.dataset.href;
        });
        // 高亮当前页面对应的导航项
        const pageId = document.querySelector('meta[name="page-id"]').content;
        const current = document.querySelector('#global-nav [data-page="' + pageId + '"]');
        if (current) current.classList.add('nav-active');
      });

    // 初始化 B03 样式系统
    if (typeof proto !== 'undefined') proto.bootstrap();
  </script>
</body>
</html>
```

---

## `_shared/nav.html` 规范

```html
<!-- 全局导航组件，被各页面 fetch 加载 -->
<!-- 所有链接使用 data-href（从 feature 根出发的路径），由加载脚本修正 -->
<nav class="topnav glass-nav" role="navigation" aria-label="主导航">
  <div class="nav-brand">
    <a data-href="index.html" data-page="home">[项目名] 原型</a>
  </div>
  <ul class="nav-links">
    <!-- 按 C02 05-navigation.md 的结构生成 -->
    <li><a data-href="browse/app/P-order-001.html" data-page="P-order-001">课程列表</a></li>
    <li><a data-href="checkout/app/P-order-010.html" data-page="P-order-010">订单确认</a></li>
    <!-- 增量轮次：新增导航项加在对应位置 -->
  </ul>
  <div class="nav-actions">
    <button data-action="toggle-theme" class="btn btn--ghost">明/暗</button>
  </div>
</nav>
```

---

## `index.html` 总入口规范

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="nav-depth" content="0">
  <title>[feature 名] · 可交互原型</title>
  <link rel="stylesheet" href="../../B03-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../B03-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../B03-design/prototype-style/app.css">
</head>
<body>
  <header class="topnav glass-nav">
    <span>[项目名] · [feature 名] 原型</span>
    <button data-action="toggle-theme" class="btn btn--ghost">明/暗</button>
  </header>

  <main>
    <h1>[feature 名] 可交互原型</h1>
    <p class="lead">本原型通过 <code>python -m http.server</code> 本地运行。所有页面可互相跳转。</p>

    <!-- 按功能分组展示 -->
    <h2>功能列表</h2>
    <div class="card-grid">
      <!-- 每个功能一张卡片 -->
      <div class="glass-card">
        <h3>课程浏览</h3>
        <p>搜索、查看课程信息</p>
        <table class="data-table">
          <thead><tr><th>page-id</th><th>端</th><th>名称</th><th>操作</th></tr></thead>
          <tbody>
            <tr>
              <td><code>P-order-001</code></td>
              <td>app</td>
              <td>课程列表</td>
              <td><a href="./browse/app/P-order-001.html">打开 ↗</a></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 增量轮次：新增功能的卡片加在此处 -->
    </div>

    <h2>连通性状态</h2>
    <p>当前原型页面总数：<strong>N</strong> | 已连通：<strong>N</strong> | 死链：<strong>0</strong></p>
  </main>

  <footer>
    <p>本目录为静态原型，未接入真实接口。空/加载/错误态描述见 C02 架构与交互规范。</p>
  </footer>

  <script defer src="../../B03-design/prototype-style/app.js"></script>
  <script>if (typeof proto !== 'undefined') proto.bootstrap();</script>
</body>
</html>
```

---

## 增量融合操作手册

> AI 每轮必须按以下清单执行，逐项打勾。

### 新增功能时的完整操作清单

- [ ] **创建功能目录**：`<功能名-kebab>/<surface>/`
- [ ] **生成新页面**：每个 page-id 一个 HTML，只画默认态
- [ ] **更新 `_shared/nav.html`**：加入新页面的导航项
- [ ] **更新已有页面的出站链接**：
  - 检查 C02 流程图，找出已有页面中需要跳转到新页面的操作
  - 在对应的已有 HTML 中添加 `<a>` 或 `<button>` 链接
  - 例如：课程详情页新增"加入课程"按钮 → 链接到订单确认页
- [ ] **更新 `index.html`**：添加新功能的卡片和页面列表
- [ ] **更新共享组件**：如新功能引入了新的共享 UI 模式，更新 `_shared/`
- [ ] **验证连通性**：执行下方验证步骤

### 已有页面的变更规则

| 变更类型 | 操作 |
|---------|------|
| 新增出站链接（如新增按钮跳转到新页面） | 在已有 HTML 对应 Block 中插入链接元素 |
| 导航项变更 | 修改 `_shared/nav.html` |
| 共享组件复用 | 新页面引用已有 `_shared/` 中的组件 |
| 页面内容不变但路径变化 | 不允许——一旦落盘路径不可变 |

---

## 连通性验证报告（每轮必须输出）

```markdown
## 连通性验证报告 · 第 N 轮 · 功能「<功能名>」

### 页面清单
| page-id | 路径 | 状态 |
|---------|------|------|
| P-order-001 | browse/app/P-order-001.html | ✅ 已有 |
| P-order-010 | checkout/app/P-order-010.html | 🆕 本轮新增 |

### 链接矩阵（从→到）
| 从 | 到 | 链接方式 | 状态 |
|------|------|---------|------|
| P-order-002 | P-order-010 | OP-1 "加入课程"按钮 | ✅ 已连通 |
| P-order-010 | P-order-011 | 表单提交后跳转 | ✅ 已连通 |
| P-order-011 | P-order-001 | "继续浏览"链接 | ✅ 已连通 |
| 全局导航 | 所有页面 | nav.html | ✅ 已连通 |

### 死链检查
- [ ] 所有 `<a href>` 目标文件都存在？
- [ ] 所有 `data-href` 目标文件都存在？
- [ ] 从 index.html 出发能到达所有页面？
- [ ] 从任意页面能返回 index.html？
- [ ] 共享导航中的所有链接都指向有效文件？

### 孤岛检查
- [ ] 没有无法到达的页面（孤岛）？
- [ ] 每个新增页面至少有 1 个入站链接（除了导航）？

### 死链数量：0
### 孤岛页面数量：0
```

---

## 硬约束

0. **连通性**：所有页面必须可互相跳转。每轮输出后必须通过连通性验证。
1. **本地运行**：通过 `python -m http.server` 在 C03-prototype 目录启动即可访问。不依赖 CDN、不用框架、不用打包器。
2. **样式单一来源**：所有 token/组件 CSS/JS 通过相对路径引用 B03 prototype-style/，不拷贝。
3. **CSS 变量**：所有颜色/字号/间距/圆角/阴影必须用 CSS 变量，不硬编码。
4. **无网络请求**：不发起真实网络请求。示例数据直接写在 HTML 静态片段中。
5. **响应式**：375 / 768 / 1280 三档无破。
6. **a11y**：`:focus-visible` 焦点环、`<label for>`、语义化标签。
7. **只画默认态**：空/加载/错误/无权限态由 C02 文字承担，不出图。
8. **增量不破坏**：新增页面不能破坏已有页面的功能和链接。
9. **单文件 ≤ 1200 行**。
10. **不产出辅助文件**：不产出 feature.css / feature.js / mock-data.js / README.md / changelog.md。页面级微调内联在 HTML 的 `<style>` / `<script>` 中。

---

## 输出质量自检

### 文件结构
- [ ] 按"功能→端"组织目录？
- [ ] `_shared/nav.html` 存在且包含所有页面的导航项？
- [ ] `index.html` 总入口列出所有功能和页面？

### 连通性
- [ ] 连通性验证报告已输出？死链数为 0？孤岛数为 0？
- [ ] 从 index.html 出发能到达所有页面？
- [ ] 从任意页面能通过导航返回 index.html？
- [ ] 所有 C02 流程图中的页面跳转都有对应的 `<a>` 链接？

### 增量融合
- [ ] 已有页面的出站链接已更新？
- [ ] `_shared/nav.html` 已更新？
- [ ] `index.html` 已更新？
- [ ] 新增页面不破坏已有页面功能？

### 样式与约束
- [ ] 所有 HTML 通过相对路径引用 B03 prototype-style/？无拷贝？
- [ ] HTML 中无 hex / px 硬编码？全用 CSS 变量？
- [ ] 通过 `python -m http.server` 可正常访问所有页面？
- [ ] 无控制台报错？
- [ ] 375 下无横向滚动？
- [ ] 焦点环可见？表单 `<label for>` 齐？
- [ ] 全文未出现接口名 / SQL / 表名 / 字段名 / 真实路由路径？
- [ ] 单文件 ≤ 1200 行？
