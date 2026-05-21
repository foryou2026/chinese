# C03-02 HTML 原型模板

> **用途**：被 `C03-01-AI输出-可交互HTML原型.md` 引用的可替换模板集合。
> 如需自定义视觉风格、路径约定或报告格式，只需修改本文件，无需改动 C03-01 的技能规则。

---

## 样式引用

样式包位于 `docs/B02-experience-design/<system-id>/prototype-style/`。

页面（`C03-prototype/<system-id>/<page-id>.html`）引用路径：

```html
<link rel="stylesheet" href="../../docs/B02-experience-design/<system-id>/prototype-style/app.css">
<script src="../../docs/B02-experience-design/<system-id>/prototype-style/app.js"></script>
```

> 绝不拷贝样式文件。`<system-id>` 替换为实际系统 ID。

---

## 页面跳转规范

所有跳转用**相对路径**：

```html
<!-- 同系统页面 -->
<a href="P-app-course-002.html">查看详情</a>
<!-- 返回上一页 -->
<button onclick="history.back()">← 返回</button>
<!-- 原型导航 -->
<a href="auth/account-entry/index.html" class="btn btn--primary btn--sm">原型导航</a>
```

---

## 单页 HTML 模板

```html
<!DOCTYPE html>
<html lang="zh-CN" data-mode="light" data-accent="ink" data-density="default">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="page-id" content="P-app-course-001">
  <meta name="system-id" content="app">
  <meta name="module-id" content="course">
  <meta name="feature-id" content="learning">
  <meta name="related-r-ids" content="R-course-001,R-course-002">
  <title>课程列表 · app 原型</title>

  <link rel="stylesheet" href="../../B02-experience-design/app/prototype-style/app.css">
  <style>
    body { display:flex; flex-direction:column; min-height:100dvh; }
    /* 场景选择下拉（需要时添加） */
    .scenario-dropdown { position:fixed; z-index:var(--z-dropdown); background:var(--glass-bg-elevated); -webkit-backdrop-filter:var(--glass-blur); backdrop-filter:var(--glass-blur); border:1px solid var(--glass-border); border-radius:var(--radius-md); box-shadow:var(--shadow-lg); padding:var(--space-1) 0; min-width:200px; display:none; }
    .scenario-dropdown.is-open { display:block; }
    .scenario-item { padding:var(--space-2) var(--space-4); font-size:var(--text-sm); cursor:pointer; transition:background var(--motion-fast); color:var(--text-primary); }
    .scenario-item:hover { background:var(--glass-bg); }
    .scenario-item small { display:block; font-size:var(--text-xs); color:var(--text-muted); margin-top:2px; }
  </style>
</head>
<body>
  <!-- 毛玻璃网格渐变背景 -->
  <div class="mesh-gradient-bg" aria-hidden="true">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
  </div>

  <div id="proto-nav-bar"></div>
  <main style="position:relative;z-index:1;flex:1;padding:var(--space-5)">
    <!-- 使用 glass-card 类获得毛玻璃卡片效果 -->
    <div class="glass-card" style="padding:var(--space-6)">
      <!-- 按 C02 04-pages.md 区块清单组织 -->
    </div>
  </main>

  <script src="../../B02-experience-design/app/prototype-style/app.js"></script>
  <script>
    fetch('_shared/proto-nav.html')
      .then(function(r){return r.text()})
      .then(function(html){
        document.getElementById('proto-nav-bar').innerHTML = html;
        var pid = document.querySelector('meta[name="page-id"]').content;
        var cur = document.querySelector('#proto-nav-bar [data-page="' + pid + '"]');
        if(cur) cur.style.cssText = 'font-size:var(--text-sm);padding:var(--space-1) var(--space-2);border-radius:var(--radius-sm);background:var(--color-brand-50);color:var(--color-brand-default);text-decoration:none;font-weight:var(--weight-medium)';
        var themeBtn = document.querySelector('[data-action="toggle-theme"]');
        if(themeBtn) themeBtn.addEventListener('click', function(){
          var m = document.documentElement.getAttribute('data-mode');
          proto.switchTheme(m === 'dark' ? 'light' : 'dark');
        });
      });

    if(typeof proto !== 'undefined') proto.bootstrap();
  </script>
</body>
</html>
```

---

## `_shared/proto-nav.html`

```html
<nav class="topnav glass-bar" role="navigation" aria-label="原型导航"
  style="display:flex;align-items:center;gap:var(--space-3);padding:0 var(--space-4);height:56px;position:sticky;top:0;z-index:50">
  <span style="font-weight:var(--weight-semibold);font-size:var(--text-lg);color:var(--color-brand-default)">系统名</span>
  <ul style="display:flex;gap:var(--space-2);list-style:none;margin:0;padding:0;flex:1;overflow-x:auto">
    <li><a href="P-app-auth-001.html" data-page="P-app-auth-001" class="nav-link" style="font-size:var(--text-sm);padding:var(--space-1) var(--space-2);border-radius:var(--radius-sm);color:var(--text-secondary);text-decoration:none;white-space:nowrap">登录</a></li>
  </ul>
  <div style="display:flex;align-items:center;gap:var(--space-2)">
    <button data-action="toggle-theme" class="proto-btn proto-btn-ghost proto-btn-sm">明/暗</button>
    <a href="index.html" class="proto-btn proto-btn-primary proto-btn-sm" style="text-decoration:none">原型导航</a>
  </div>
</nav>
```

> 页面平铺在系统根目录，所有链接均为同级相对路径（如 `P-app-auth-001.html`）。

---

## 目录页规范

- **项目总览 `index.html`**：大卡片列出所有系统（系统数量少时占满屏幕，自适应布局）
- **系统导航 `<system>/index.html`**：卡片列出所有模块，**仅显示模块名称和简短描述**，不展示功能细节。头部有 `← 项目总览`
- **模块导航 `<system>/<module>/index.html`**：卡片列出该模块所有功能入口，**仅显示功能名称和描述**。头部有 `← 系统名`
- **功能导航 `<system>/<module>/<feature>/index.html`**：列出该功能关联的所有原型页面链接。头部有 `← 模块名`

所有目录页使用 `glass-card` 毛玻璃卡片 + `mesh-gradient-bg` 背景。

---

## 连通性验证报告（每轮必输出）

```markdown
## 连通性验证 · 第 N 轮 · 系统「<system-id>」· 功能「<feature-id>」

### 功能→页面映射
| 功能 | 页面文件 | 类型 | 弹框列表 |

### 页面清单
| page-id | 路径 | 状态(已有/新增) |

### 链接矩阵
| 从 | 到 | 链接方式 | 状态 |

### 检查
- [ ] 所有 href 目标存在？
- [ ] 从系统 index 能到所有页面？
- [ ] 每个演示页有导航栏？每个表单/详情页有返回？
- [ ] 无跨系统链接？

### 死链：0 / 孤岛：0
```
