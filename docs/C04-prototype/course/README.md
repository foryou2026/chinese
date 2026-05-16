<!-- TARGET-PATH: docs/C04-prototype/course/README.md -->

# `course` · 原型契约

> **阶段**:C04-H · **冻结状态**:v1.0 · 2026-05-16
> **源资产**:[`function/02-course/ai/F4-AI-原型设计/`](../../../function/02-course/ai/F4-AI-原型设计/)(17 HTML + `_assets/` + `index.html`)
> **下游**:实现端 `system/apps/web-app/` 与 `system/apps/web-admin/`

## 1. 原则
本目录是**原型契约文档**,不复制 F4 HTML 资产;实现端按本契约 + F4 视觉效果 + F3 交互规范 + B04 Design Token 三方对齐还原即可。如需查看可运行原型,直接打开:

- [F4 总入口 index.html](../../../function/02-course/ai/F4-AI-原型设计/index.html)

## 2. 原型 → P-ID 映射

### 应用端

| 原型 HTML | P-ID | 路由 |
|----------|------|------|
| `P-C-1-学习地图.html` | P-app-course-002(地图视图) | `/learn` |
| `P-C-2-节学习页.html` | P-app-course-002(节内) + P-app-course-003 | `/learn/{code}` / `/lesson/{code}/kp/{id}` |
| `P-C-3-节末小测.html` | P-app-course-002(节末弹层 D-13)| `/learn/{code}#quiz` |
| `P-C-4-SRS复习.html` | P-app-course-004 | `/review` |
| `P-C-5-错题本.html` | P-app-course-005 | `/wrong` |
| `P-C-6-考试中心.html` | P-app-course-006 | `/exam` |
| `P-C-7-考试进行.html` | P-app-course-007 | `/exam/{attemptId}` |
| `P-C-8-个人统计.html` | P-app-course-008 | `/me` |

> 备注:P-app-course-001(首页)在原型中由 `_assets/` 共用模板 + `P-C-1` 顶部区组合,无独立 HTML。

### 管理端

| 原型 HTML | P-ID | 路由 |
|----------|------|------|
| `P-A-1-课程目录总览.html` | P-admin-course-001 | `/admin/course` |
| `P-A-2-主题-阶段-章列表.html` | P-admin-course-002 | `/admin/course/tree` |
| `P-A-3-节编辑.html` | P-admin-course-003 | `/admin/course/lesson/{code}` |
| `P-A-4-KP列表.html` | P-admin-course-004 | `/admin/course/kp` |
| `P-A-5-题目列表.html` | P-admin-course-005 | `/admin/course/question` |
| `P-A-6-举报处理.html` | P-admin-course-006 | `/admin/course/report` |
| `P-A-7-媒资库.html` | P-admin-course-007 | `/admin/course/media` |
| `P-A-8-考试中心管理.html` | P-admin-course-008 | `/admin/course/exam` |
| `P-A-9-全局搜索.html` | P-admin-course-009 | `/admin/course/search` |

## 3. 组件清单(必须对齐 ui-kit)

| 组件 | 使用页 | 源自 |
|------|--------|------|
| `<TopNav>` (App 5 Tab) | P-app-course-* | ui-kit `<BottomTab>` |
| `<TopNav>` (Admin 9 Tab) | P-admin-course-* | ui-kit `<TopTab>` |
| `<Breadcrumb>` | 全部 admin | ui-kit |
| `<TreeView draggable>` | P-admin-course-002 | 新增组件 |
| `<KpCard>` 7 种变体 | P-app-course-002/003 | 新增,按 KP 类型差异 |
| `<QuestionRenderer>` 12 种 | P-app-course-002/004/007 + P-admin-course-005 预览 | 新增统一渲染器 |
| `<CountdownTimer>` | P-app-course-007 | 新增 |
| `<ProgressMap>` 4 级树 | P-app-course-002 地图视图 | 新增 |
| `<DataTable cursor>` | P-admin-course-004/005/006/007/008 | ui-kit |
| `<EditorDrawer>` Tab 切换 | P-admin-course-003/004/005/008 | ui-kit |
| `<DiffPreview>` LWW | D-6 | 新增 |
| `<ImportWizard>` 3 step | D-15 | 新增 |
| `<LangTabs zh/en/vi/th/id>` | 所有多语字段表单 | ui-kit |

## 4. 状态契约(必须实现)

每页须支持以下渲染态(详见 [`C02-ia/course/07-error-pages.md`](../../C02-ia/course/07-error-pages.md)):

- `loading` 骨架;
- `empty` 空态(对应业务空场景文案);
- `error` 错误占位 + 重试;
- `offline` 顶部红条 + 本地队列计数(仅 P-app-course-002/004/007);
- `403-no-subscription` / `403-no-track-scope` / `404` / `410-unpublished` / `429` / `5xx` 错误页;
- 弹窗态 D-1..D-18(见 [07-error-pages.md §2](../../C02-ia/course/07-error-pages.md))。

## 5. Design Token 契约

- Token 来源:[`docs/B04-design/design-tokens/`](../../B04-design/design-tokens/);
- 主题:5 主题各有强调色 → `--track-color-share / --track-color-ec / --track-color-fc / --track-color-hsk / --track-color-dl`;
- 节状态色:`--lesson-locked / --lesson-unlocked / --lesson-in-progress / --lesson-passed`;
- 答题反馈色:`--answer-correct / --answer-wrong`;
- 暗黑模式 token 对应自动派生;
- 字号 / 间距 / 圆角 / 阴影 / 字体族(中 + 5 语)全部走 token,不写 magic number。

## 6. 多语言对齐

- 文案 key 命名前缀:`course.*`;
- 应用端 UI 5 语全套(`zh/en/vi/th/id`);管理端 UI 中文;
- 内容字段 5 语录入由 `<LangTabs>` 组件统一编辑;
- 缺失语言渲染回退 `zh` + 浅色提示。

## 7. 备注

- 原型与本契约出现冲突时,**以 F3 交互规范 + 本契约为准**,原型 HTML 视为视觉示意;
- 后续迭代:任何 P-ID 改造,需同步更新本表与 [`C03-pages/course/`](../../C03-pages/course/) 对应页面文档。
