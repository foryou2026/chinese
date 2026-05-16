<!-- TARGET-PATH: docs/C03-pages/discover-china/P-admin-discover-china-001.md -->

# `P-admin-discover-china-001` · 管理端 12 类目卡片

> **path**:`/admin/china` · **R 覆盖**:R-008, R-016, R-018
> **角色可见**:super_admin · **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- 侧栏激活"发现中国";
- 顶部面包屑 + 全局搜索框(范围切换器:`全局 / 本类目 / 本文章`,默认全局);
- 卡片网格 12 张;每张显示 `名称 / 介绍(中文)/ 已发布 X · 共 Y`。

## 2. DOM 骨架
```
Sidebar(管理端)
PageHeader { h1 发现中国, ScopeSearch { input, scope select } }
Grid {
  AdminCategoryCard ×12 {
    h2 类目名
    p 介绍(中文)
    StatBadge "已发布 X / 总 Y"
    DeleteBtn(disabled, tooltip="类目固定不可删")
  }
}
```

## 3. 数据
- `GET admin/china/categories?include_stats=1` → `[{ code, name_i18n, description_i18n, total, published }]`。

## 4. 状态
| 态 | 表现 |
|---|------|
| idle | 12 卡片 |
| loading | 12 卡片 skeleton |
| error | 整页 Retry |
| forbidden | 后端 403 → 跳 /admin/auth/login |

## 5. 交互
- 卡片点击 → `/admin/china/categories/{code}`;
- 删除按钮永远 disabled + tooltip;
- 搜索:输入 + 范围"全局" → 跳 `P-admin-discover-china-004?scope=global&q={q}`。

## 6. 错误码
- 403 → 守卫跳;
- 5xx → Retry。

## 7-10. 移动端 / a11y / 性能 / 多语言
- 管理端响应到 768px 即可,无小屏特殊优化;
- 卡片 Enter 触发;
- 接口 SWR 60s;
- 管理端文案默认中文,不切语言。
