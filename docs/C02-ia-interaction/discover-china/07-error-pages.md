<!-- TARGET-PATH: docs/C02-ia-interaction/discover-china/07-error-pages.md -->

# 错误 / 空态页 / 弹窗清单

> **阶段**：C02-IN · **功能**：`discover-china`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端

| 场景 | 表现 | 位置 |
|------|------|------|
| 类目下无已发布文章 | 空态插画 + 文案"暂无文章，敬请期待" + 返回类目按钮 | P-app-discover-china-002 |
| 文章 404 / 已下架 | 空态插画 + 文案"该文章已下架或不存在" + 返回类目 | P-app-discover-china-003 |
| TTS 失败 | Toast "朗读失败，稍后重试"；不阻断 UI | P-app-discover-china-003 |
| 网络 5xx | 通用 ErrorBoundary + Retry | 全部 |

**D-8 登录提示 Modal**：触发于 04-12 类目卡片点击；主按钮跳登录页（含回跳参数）。

---

## admin 端

| 场景 | 表现 | 位置 |
|------|------|------|
| 类目无文章 | 空态"该类目下还没有文章" + 新建按钮 | P-admin-discover-china-002 |
| 文章无句子 | 空态"还没有句子，点击下方添加首句" | P-admin-discover-china-003 |
| 搜索无结果 | 空态"没有命中" + 重置按钮 | P-admin-discover-china-004 |
| 类目删除尝试 | 后端 405，前端 disabled + tooltip "类目固定不可删" | P-admin-discover-china-001 |
| 5 语未齐发布 | Modal 错误清单 + 跳首个缺失句子 | P-admin-discover-china-003 |

---

## 守卫错误

- admin 不通过 → 跳 `/admin/auth/login`（由 auth feature 守卫产生）
- 应用端用户访问管理端 → 跳应用端首页 + Toast "无权访问"

---

## 通用错误码呈现

| 错误码族 | 呈现位置 | 默认动作 |
|---------|---------|---------|
| 4xx 字段错误 | 字段下内联 | 留在表单 |
| 4xx 业务 | Modal / Toast | 视严重度 |
| 5xx | Toast + Retry | 表单值保留 |

---

## 弹窗 / Drawer 清单（D-1 ~ D-8）

| D-ID | 名称 | 触发 | 类型 |
|------|------|------|------|
| D-1 | 新建文章 Modal | P-admin-discover-china-002 顶部 | Modal |
| D-2 | 文章基本信息编辑（同页）| P-admin-discover-china-003 顶部区 | 内联区 |
| D-3 | 句子编辑 Drawer | P-admin-discover-china-003 句子卡片 | 右侧 600px，5 Tab + 拼音 + 中文校对 |
| D-4 | 句子新建 Drawer | P-admin-discover-china-003 "+ 添加" | 右侧 600px，同 D-3 + 插入位置 |
| D-5 | 二次确认 Modal | 多处 | Modal 380px |
| D-6 | 未保存离开 Modal | 路由切换前 | Modal 380px，离开 / 取消 / 保存后离开 |
| D-7 | 句子重排 Drawer | P-admin-discover-china-003 重排 | 右侧 480px，拖拽列表 |
| D-8 | 登录提示 Modal | P-app-discover-china-001 04-12 卡片 | Modal 380px，主按钮跳登录 + 取消 |
