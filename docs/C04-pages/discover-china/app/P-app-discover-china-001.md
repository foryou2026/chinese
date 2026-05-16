<!-- TARGET-PATH: docs/C04-pages/discover-china/app/P-app-discover-china-001.md -->

# `P-app-discover-china-001` · 12 类目卡片页

> **阶段**:C04-N · **feature**:`discover-china` · **surface**:`app`
> **path**:`/china`
> **角色可见**:任意(04-12 类目卡片点击时弹登录提示)
> **R 覆盖**:R-001, R-020
> **冻结状态**:已冻结 · 2026-05-16

---

## 1. 布局

- 全局顶/底 Tab,当前态高亮"发现中国";
- 首屏标题区:H1"发现中国" + 一句副标题(本地语);
- 卡片网格:桌面 3 列 / 平板 2 列 / 移动 1 列;每张卡片 ratio 5:3,封面图 + 标题(中文 + 本地语)+ 介绍(本地语)。

## 2. DOM 骨架

```
TabBar(底/顶)
PageHeader { h1 "发现中国", p subtitle }
Grid(.card-grid) {
  CategoryCard ×12 {
    cover img (远景 + 玻璃罩)
    h2 中文标题
    h3 本地语标题
    p   介绍(本地语,2 行截断)
    badge "需登录"(仅 04-12 + 未登录)
  }
}
```

## 3. 数据

- `GET china/categories` → `[{ code, 多语名称字段, description_i18n, needs_login }]`(在 D02 定义)
- 显示语言由 i18n hook 决定。

## 4. 状态

| 态 | 触发 | UI 表现 |
|---|------|--------|
| idle | 默认 | 12 卡片直出 |
| loading | 首屏 < 200ms | 不显示 skeleton;>200ms 显示 12 卡片骨架 |
| error | 5xx | 通用 ErrorBoundary + Retry |
| login-required | 未登录点 04-12 | 弹 D-8 登录提示 Modal |

## 5. 交互

- **卡片点击 01-03**:直接跳 `/china/categories/{code}`;
- **卡片点击 04-12 + 未登录**:弹 D-8(详见 [C02-07-error-pages §6](../../../C03-ia/discover-china/07-error-pages.md));
- **卡片点击 04-12 + 已登录**:直接跳;
- **悬停**:卡片 lift + 玻璃罩亮度 +5%。

## 6. 错误码映射

- 5xx → Toast"服务异常,稍后重试" + 整页 Retry;
- 401(任何意外 401)→ Toast"请重新登录"(理论不会触发,因本页公开)。

## 7. 移动端差异

- 卡片单列;
- 标题区 padding 减小;
- 卡片高度 180px 固定。

## 8. 无障碍

- 卡片整体可 focus(tabindex=0)+ Enter 触发点击;
- 封面图 `alt={类目名 + 介绍}`;
- 登录引导 Modal 焦点陷阱。

## 9. 性能 / 埋点

- 12 条类目接口走 CDN 缓存 60s;
- 卡片点击 `analytics.track('china.category_click', { code, needs_login })`;
- 登录引导曝光 `china.login_gate_shown`。

## 10. 多语言

- 卡片标题:多语名称字段[currentLang]` || 多语名称字段.en` 兜底;
- 介绍同上;
- 中文用户仅显示中文标题(隐藏 h3 本地语)。
