# C03-01 AI 输出：可交互 HTML 原型

> **阶段**：C03 可交互原型
> **归属**：**按系统独立（_system）**
> **谁产出**：AI（HTML 原型工程师）
> **触发条件**：C01（共享）+ C02（同系统）全部冻结
> **落盘**：`C03-prototype/<system-id>/<module-id>/<feature-id>/<page-id>.html`

---

## 核心理念

**原型 = 一个不跑真实数据和接口的完整系统。** 用户使用原型时的体验应与使用真实系统完全一致：所有弹框、新建编辑、表单联动、页面跳转、状态切换都必须模拟真实行为。

**页面与功能是多对多关系**：一个页面可能承载多个功能，一个功能可能横跨多个页面。原型整体按系统形成闭环，功能目录仅作为快捷导航入口。

---

## 导航结构（三层目录 + 演示模式）

```
第一层：项目总览       index.html                       所有系统卡片
第二层：系统模块目录    <system>/index.html               该系统所有模块
第三层：模块功能目录    <system>/<module>/index.html       该模块所有功能（快捷导航）
演示模式：             <system>/<module>/<feature>/页面    按真实系统交互，无目录
```

**三层目录仅是快捷导航跳转**，帮助用户快速定位到某个功能的入口页面。

**演示模式规则**：
- 进入后不再出现任何目录层级，所有跳转按真实业务流程走
- 每个演示页右上角有「原型导航」按钮，返回模块功能目录页
- 同系统内页面互相跳转；不同系统互相独立
- 通过 CSS media query 响应式适配，无需 Web/App 切换按钮

---

## 触发提示词

```
请你扮演"HTML 原型工程师"。
上游：C01 共享基线、C02 同系统交互规范、B02 体验规范与设计系统。
按 /prompt/C-product/_system/C03-01-AI输出-可交互HTML原型.md 输出。
本轮：系统「<system-id>」模块「<module-id>」功能「<feature-id>」。
落盘 C03-prototype/<system-id>/<module-id>/<feature-id>/。
若目录不存在，同时创建系统目录、模块目录、index.html 和 _shared/。
必须与同系统已有页面融合——所有页面可互相跳转、无死链。
引用 B02 的 prototype-style/（相对路径）。严禁引用后端实现。
每个页面必须实现高保真交互。
```

---

## AI 必须遵守

1. **只读**：C01 共享基线 + C02 同系统交互规范 + B02 体验规范 + 同系统已有原型 + 本模板
2. **C/D 隔离**：严禁引用后端实现（接口/表/字段/路由/SQL）
3. **系统隔离**：不跨系统链接
4. **连通闭环**：同系统内每个页面必须能通过导航或链接到达其他相关页面，形成系统级闭环
5. **增量融合**：每轮增加功能页面，同时更新已有页面的导航和链接
6. **本地可运行**：`python -m http.server` 启动即可访问
7. **高保真交互**：所有交互必须模拟真实（见下方标准）
8. **弹框不独立建页**：弹框、确认框、抽屉在当前页内实现

---

## 高保真交互标准

### 1. 页面导航与返回
- 详情页/表单页必须有 `← 返回` 按钮（`history.back()` 或跳明确来源页）
- 新建/编辑页必须有"取消"按钮返回来源列表

### 2. 操作后跳转
- 表单提交成功 → 自动跳转结果页（延迟 300-600ms）
- 删除确认 → 弹框确认后 DOM 删除动画
- 保存草稿 → toast "已保存"
- 提交审核/发布 → 弹框确认后跳转状态变更后的页面

### 3. 表单联动（条件显隐）
- 选择选项后相关字段**立即响应**：显示/隐藏配置项、更新下拉选项、改变必填/禁用状态
- 动态表单：选择不同选项影响其他字段的显示隐藏、校验规则
- 监听 `change`/`input` 事件，纯 JS 操作 DOM

### 4. 列表状态管理
- 删除行：弹确认 → 确认后 `row.remove()` + 更新统计数
- 新增行：返回列表时顶部插入新行（`sessionStorage` 传递标记）
- 状态切换：启用/禁用等开关直接切换 DOM 状态标签和按钮文案
- 批量操作：多选 checkbox 联动批量按钮的可用状态

### 5. 弹框与抽屉
- 确认弹框：当前页 `<dialog>` 或 `.modal` 实现
- 表单弹框：提交后关闭并更新当前页列表行（DOM 原地更新）
- 抽屉：右侧/底部滑出，有关闭按钮，点击遮罩关闭
- **禁止为弹框单独建 HTML 文件**

### 6. 搜索与筛选
- 筛选变化后列表立即更新（JS 过滤 DOM 元素 display）
- 搜索支持实时过滤或按钮触发
- 分页按钮切换（纯 DOM 显隐）

### 7. 标签页/步骤条
- Tabs 切换激活状态并显示对应内容
- Stepper 上一步/下一步控制当前步骤，最后一步触发跳转/确认

### 8. 通知与反馈
- Toast：操作后右上角提示，2-3 秒消失
- 内联错误：字段下方红色错误文案（不用浏览器 `alert`）
- 骨架屏：列表/详情首次加载先骨架屏 300ms 再渲染

### 9. 示例数据
- 直接写在 HTML 中（静态 DOM），不发网络请求
- 至少 5-8 条列表数据，字段完整
- `sessionStorage` 在页面间传递操作标记

---

## 弹框 vs 跳页判断规则

| 场景 | 方式 |
|------|------|
| 新建（创建新实体） | **跳页** |
| 编辑（全字段编辑） | **跳页** |
| 查看详情（信息量大） | **跳页** |
| 快捷编辑（1-3 字段） | **弹框** |
| 删除确认 | **弹框** |
| 查看详情（信息量少） | **弹框/抽屉** |
| 提交/发布确认 | **弹框** |
| 上传、选择关联对象 | **弹框** |

---

## 功能与页面映射

- 一个功能 → 多个页面：允许
- 多个功能 → 一个页面：允许（合并为一个 HTML）
- 弹框不算页面
- 新建/编辑必须跳页
- AI 每轮必须输出映射表

---

## 输出目录结构

```
C03-prototype/
  index.html                                    # 项目总览
  _shared/
  <system-id>/
    index.html                                  # 系统模块目录
    <module-id>/
      index.html                                # 模块功能目录（快捷导航）
      _shared/
        proto-nav.html
      <feature-id>/
        <page-id>.html                          # 演示页面
```

---

## 每轮增量融合步骤

1. **规划映射表**：明确本功能有几个页面，哪些弹框、哪些跳页
2. **创建功能目录**：`<system-id>/<module-id>/<feature-id>/`
3. **生成新页面**：每页实现完整高保真交互
4. **更新 `_shared/proto-nav.html`**：加入新页面导航项
5. **更新已有页面出站链接**：检查 C02 流程图，在已有 HTML 中添加跳转
6. **更新目录页**：模块功能目录 → 系统模块目录 → 项目总览（按需）
7. **输出连通性验证报告**

---

## 页面跳转规范

所有页面间跳转使用**相对路径**：

```html
<!-- 同功能目录内 -->
<a href="./P-app-course-002.html">查看详情</a>
<!-- 返回上一页 -->
<button onclick="history.back()">← 返回</button>
<!-- 跨功能跳转（同模块） -->
<a href="../checkout/P-app-order-001.html">去结算</a>
<!-- 原型导航按钮 -->
<a data-href="index.html" class="btn btn--primary btn--sm">原型导航</a>
```

---

## 样式引用

样式包位于 `docs/B02-experience-design/prototype-style/`：

| 页面层级 | 路径前缀 |
|---------|---------|
| 项目总览 | `../docs/B02-experience-design/prototype-style/` |
| 系统入口 | `../../docs/B02-experience-design/prototype-style/` |
| 模块入口 | `../../../docs/B02-experience-design/prototype-style/` |
| 功能页面 | `../../../../docs/B02-experience-design/prototype-style/` |

> 绝不拷贝样式文件。

---

## 单页 HTML 模板

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="nav-depth" content="1">
  <meta name="page-id" content="P-app-course-001">
  <meta name="system-id" content="app">
  <meta name="module-id" content="course">
  <meta name="feature-id" content="learning">
  <meta name="related-r-ids" content="R-course-001,R-course-002">
  <title>课程列表 · app · course · learning 原型</title>

  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/tokens.css">
  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/themes.css">
  <link rel="stylesheet" href="../../../../docs/B02-experience-design/prototype-style/app.css">

  <style>
    .modal-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,.45); z-index:100; align-items:center; justify-content:center; }
    .modal-overlay.is-open { display:flex; }
    @keyframes rowFadeOut { to { opacity:0; transform:translateX(20px); } }
    .row-removing { animation: rowFadeOut .25s forwards; }
  </style>
</head>
<body>
  <div id="proto-nav-bar"></div>
  <main class="main-content" style="flex:1;padding:var(--space-5)">
    <!-- 按 C02 04-pages.md 区块清单组织 -->
  </main>
  <div class="modal-overlay" id="modal-delete" role="dialog" aria-modal="true"></div>

  <script defer src="../../../../docs/B02-experience-design/prototype-style/app.js"></script>
  <script>
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

    const ProtoModal = {
      open(id) { document.getElementById(id).classList.add('is-open'); },
      close(id) { document.getElementById(id).classList.remove('is-open'); }
    };
    document.querySelectorAll('.modal-overlay').forEach(o => {
      o.addEventListener('click', e => { if (e.target === o) o.classList.remove('is-open'); });
    });

    const ProtoToast = {
      show(msg, type = 'success') {
        const el = document.createElement('div');
        el.textContent = msg;
        Object.assign(el.style, {
          position:'fixed', top:'16px', right:'16px', zIndex:'9999',
          padding:'8px 16px', borderRadius:'6px', color:'#fff', fontSize:'14px',
          background: type === 'success' ? 'var(--color-success,#18a058)' : 'var(--color-danger,#d03050)',
          boxShadow:'0 2px 8px rgba(0,0,0,.18)', transition:'opacity .3s'
        });
        document.body.appendChild(el);
        setTimeout(() => { el.style.opacity = '0'; setTimeout(() => el.remove(), 300); }, 2200);
      }
    };

    if (typeof proto !== 'undefined') proto.bootstrap();
  </script>
</body>
</html>
```

---

## `_shared/proto-nav.html`

```html
<nav class="topnav glass-nav" role="navigation" aria-label="原型导航"
  style="display:flex;align-items:center;gap:var(--space-3);padding:0 var(--space-4);height:56px;position:sticky;top:0;z-index:50">
  <ul class="nav-links" role="list" style="display:flex;gap:var(--space-2);list-style:none;margin:0;padding:0;flex:1">
    <li><a data-href="account-entry/P-app-auth-001.html" data-page="P-app-auth-001" class="nav-link">登录</a></li>
  </ul>
  <div class="nav-actions" style="display:flex;align-items:center;gap:var(--space-2)">
    <button data-action="toggle-theme" class="btn btn--ghost btn--sm">明/暗</button>
    <a data-href="index.html" class="btn btn--primary btn--sm proto-home-btn">原型导航</a>
  </div>
</nav>
```

---

## 目录页规范

**系统模块目录 `<system>/index.html`**：卡片列出所有模块，头部有"← 项目总览"。

**模块功能目录 `<system>/<module>/index.html`**：卡片列出所有功能作为快捷导航入口，每个卡片列出入口页面链接。提示"点击右上角「原型导航」可返回此页"。此目录是快捷跳转，不是原型的一部分。

---

## 连通性验证报告（每轮必须输出）

```markdown
## 连通性验证 · 第 N 轮 · 系统「<system-id>」· 功能「<feature-id>」

### 功能→页面映射表
| 功能 | 页面文件 | 类型 | 弹框列表 |

### 页面清单
| page-id | 路径 | 状态(已有/新增) |

### 链接矩阵
| 从 | 到 | 链接方式 | 状态 |

### 检查
- [ ] 所有 href/data-href 目标存在？
- [ ] 从模块 index 能到所有页面？
- [ ] 每个演示页有「原型导航」？每个表单/详情页有返回？
- [ ] 无跨系统链接？

### 死链数：0 / 孤岛数：0
```

---

## 硬约束

1. **系统闭环**：同系统内所有页面形成完整可交互系统体验
2. **系统隔离**：不同系统互不链接
3. **本地运行**：`python -m http.server`，零依赖
4. **样式单源**：相对路径引用 B02 prototype-style/，不拷贝
5. **CSS 变量**：不硬编码 hex/px
6. **无网络请求**：静态 DOM + sessionStorage
7. **响应式**：375/768/1280 三档无破
8. **a11y**：焦点环、label for、语义标签
9. **高保真**：删除行消失、表单联动、动态表单条件显隐、弹框当前页——必须实现
10. **弹框不独立建页**
11. **新建/编辑必须跳页**
12. **增量不破坏**
13. **单文件 <= 1200 行**
14. **不产出辅助文件**：页面逻辑内联 `<style>`/`<script>`

---

## 质量自检

### 目录
- [ ] 原型在 `C03-prototype/<system-id>/<module-id>/<feature-id>/`？
- [ ] 项目总览、系统目录、模块目录 index.html 均已更新？

### 高保真交互
- [ ] 列表：搜索/筛选即时反馈？删除后 DOM 消失+计数更新？
- [ ] 表单：返回/取消？提交后跳转？
- [ ] 动态表单：选项变化后字段立即显隐/联动？
- [ ] 详情：← 返回？
- [ ] 弹框：当前页实现？遮罩可关闭？
- [ ] Toast 反馈？

### 连通性
- [ ] 验证报告已输出？死链=0？孤岛=0？
- [ ] 从模块目录能到所有页面？
- [ ] 无跨系统链接？

### 样式
- [ ] 相对路径引用 B02？无拷贝？无 hex/px 硬编码？
- [ ] 375 无横滚？焦点环？label for？
- [ ] 无接口名/SQL/表名/字段名？
- [ ] 页面 ID 带 system 前缀？单文件<=1200 行？
