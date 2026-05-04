# 24 · P4 AI 输出：HTML 原型生成规范

> **谁产出**：AI（Designer）
> **落盘**：`content/<proj>/prototype/html/`
> **目的**：把 P3 的页面清单变成可点通的本地 HTML 原型，供 PM 评审与迭代。

---

## 一、目录结构

```
content/<proj>/prototype/html/
  index.html              ← 评审用入口，列出所有页面链接 + 设备/角色切换器
  styles.css              ← 单一全局样式表（灰阶骨架，G2 冻结后再上色）
  app.js                  ← 单一全局脚本：mock 登录态、mock 数据、设备切换
  mock-data.js            ← 所有假数据集中此文件
  pages/
    public-login.html
    public-register.html
    app-home.html
    app-learn.html
    admin-courses.html
    ...
  states/                 ← 每个关键页面的 4 态独立文件，便于评审"打靶"
    app-home.empty.html
    app-home.error.html
    app-home.loading.html
    app-home.forbidden.html
  changelog.md            ← 每次迭代追加
```

> 文件名规则：`<scope>-<page>.html`，scope ∈ {public, app, admin}。

---

## 二、index.html 必含

- 一个表格列出所有 page，每行：路由 / 文件名 / 承载 R-ID / 角色 / 4 态链接
- 顶部"设备切换"按钮：PC（1280）/ Pad（768）/ Mobile（375），点击给 iframe 设宽
- "Mock 登录态"下拉：未登录 / ROLE-USER / ROLE-EDITOR / ROLE-ADMIN，切换会写 localStorage 然后 iframe reload
- "原型版本号 / 生成时间 / 上游 baseline 版本"显示在顶部

---

## 三、HTML 写法约束

1. **零依赖**：禁止引 React/Vue/Tailwind 等。只能用原生 HTML + 一份 CSS + 一份 JS。理由：原型阶段评审者要能任何环境双击打开。
2. **CSS 命名**：BEM；类名英文，不依赖颜色，仅描述结构（如 `.card`、`.card__title`、`.btn--primary`）。
3. **可访问性**：
   - 每个交互元素有 `aria-label` 或可见文字
   - 表单字段有 `<label for>`
   - 按钮用 `<button>`，链接用 `<a>`，不要乱用 `<div onclick>`
4. **页面顶部元信息条**（评审专用，G2 冻结后会移除）：
   ```html
   <div class="proto-meta-bar">
     <span>P-china-003 · /home · ROLE-USER</span>
     <span>承载：R-china-010, R-china-011</span>
     <span>v1 · 2026-05-04</span>
     <a href="../index.html">← 回总览</a>
   </div>
   ```
5. **假数据**：写死 5-10 条有真实感的中文/越南语条目，不要 `lorem ipsum`。
6. **跳转**：所有按钮/链接的 `href` 都必须指向某个真实文件（哪怕是占位空页），禁止 `href="#"` 死链。
7. **响应式**：用 `<meta viewport>` + 单一 CSS 媒体查询 `@media (max-width: 768px)` + `@media (max-width: 375px)`。

---

## 四、四态实现要求

每个 P0 页面必须额外产出 4 个 `.<state>.html` 文件，**不要**用 JS 切换态——分文件可让评审者直接 diff 视觉。

| 状态 | 实现 | 必含元素 |
|------|------|---------|
| empty | 数据全无 | 插画/图标占位 + 引导 CTA + 一句解释 |
| error | 模拟接口失败 | 错误图标 + 错误标题 + 错误详情（可隐藏） + 重试按钮 |
| loading | 主区骨架屏 | 至少有 3 个 shimmer 块对应真实结构 |
| forbidden | 当前角色无权限 | 锁图标 + 角色不匹配文案 + 切角色 / 退出 CTA |

---

## 五、JS 约束（app.js）

- 只做 3 件事：① 顶部元信息条注入 ② Mock 登录态读取/切换 ③ 设备切换。
- 数据从 `mock-data.js` 取，不要散在各处。
- 全部用原生 ES6+，不要打包工具。
- 整个 app.js ≤ 200 行；超出就拆。

---

## 六、changelog.md 模板

```markdown
# 原型变更日志 · <project>

## v1 · 2026-05-04 · 首版
- 生成 12 个页面（含 4 个公开 + 6 个应用 + 2 个管理）
- 全部 P0 R-ID 已承载

## v2 · 2026-05-06 · PM 反馈
- [改] 今日课表卡片改 3 列，移动端纵向堆叠
- [增] 增加"水平测试结果分享"页（来自 R-china-031）
- [删] 移除"打卡日历周视图"，改月视图
```

---

## 七、生成顺序（AI 必须按此顺序输出）

1. 先生成 `styles.css` 骨架（灰阶 + 4 态通用样式）
2. 生成 `mock-data.js`
3. 生成 `app.js`
4. 生成 `index.html`（评审入口）
5. **逐页**生成 `pages/<scope>-<page>.html` —— 每页输出一份，按 P3 页面清单顺序
6. 对每个 P0 页面追加 4 态文件
7. 最后写 `changelog.md`

> AI 一次回复如果放不下全部，按"先发 1-3 步、PM 确认骨架可接受 → 再批量发页面"分批，每批 ≤ 3 个 HTML 文件，避免一次塞爆。

---

## 八、迭代流程

```
PM 看 v1 → 列出"改/增/删"清单（用统一格式）→
AI 检查变更是否在 R3 范围内 →
  在 → 直接出 v2 + changelog
  超 → 停手，提示先回 R 阶段补 baseline
```

变更清单标准格式（PM 用）：
```
- 改 P-china-003 今日课表：卡片改 3 列
- 增 P-china-031 测试结果分享：来源 R-china-031
- 删 P-china-009 周打卡日历
```

---

## 九、AI 自检

- [ ] 每页 href 都不为 `#`？
- [ ] 每页都有顶部元信息条？
- [ ] 每个 P0 页都补齐 4 态文件？
- [ ] index.html 表格 R-ID 链接到对应 baseline 章节？
- [ ] 整个原型零依赖、双击可开？
- [ ] 单文件 ≤ 1200 行？

任何一项 No → 重生成。
