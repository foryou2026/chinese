<!-- TARGET-PATH: docs/C03-pages/app-auth/P-app-app-auth-009.md -->

# `P-app-app-auth-009` · 编辑资料

> **path**：`/me/profile` · **角色可见**：用户  
> **R 覆盖**：R-008  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

`<PageHeader title="资料" backTo="/me" />` + 一张 `<GlassCard>`。

## 2. DOM

```
GlassCard
  ├─ form
  │    ├─ avatar block：头像预览（96×96 圆形）+ field avatar_url (text input)
  │    │     hint「v1 仅支持 URL 输入；Google 注册的头像会自动填充。」
  │    ├─ field display_name (max 32)
  │    ├─ field locale (Select: zh / en / vi / th / id)
  │    └─ buttons.row：
  │           ├─ button.secondary [取消]
  │           └─ button.primary   [保存]
```

## 3. 字段

| key | zod |
|-----|-----|
| display_name | `min(1).max(32)` |
| avatar_url | `union(url(), literal(''))`（允许清空）|
| locale | `enum(['zh','en','vi','th','id'])` |

## 4. 4 态

| 态 | UI |
|---|----|
| `view` | 字段 readonly + 「编辑」按钮（卡片右上）；进入页时默认此态 |
| `editing` | 字段可写；底部按钮 [取消] [保存] 替换 [编辑] |
| `saving` | 按钮 spinner |

> 进入页若 `?edit=1` 直接 `editing` 态（个人中心首页可加链接快速跳）。

## 5. 流程

```
1. mount → GET /v1/me 写入表单
2. 点「编辑」 → 进 editing
3. 点「保存」 → PATCH /v1/me { display_name, avatar_url, locale }
   - 200 → Toast「已保存」+ 回 view 态；写入 authStore；顶栏头像 / 显示名热更新；
           若 locale 变更 → 立刻切 i18n + reload 当前路由（保持页面）
   - 400 validation → 字段下内联
   - 5xx → Toast
4. 点「取消」 → 字段回滚到上次成功值 + 回 view 态
```

## 6. 表单离开保护

- editing 态触发 `useFormGuard`：dirty 且未保存 → 同站跳转弹「未保存的更改将丢失，确认离开吗？」`<Confirm>`；
- 30s 自动存 `localStorage` key=`app-auth:profile:<user_id>`；保存成功立即清。

## 7. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 改 display_name | Toast「已保存」+ 顶栏头像首字符更新 |
| S2 | 改 avatar_url 非法 URL | 字段下内联「请输入有效 URL」 |
| S3 | 清空 avatar_url | 200，回退到首字符兜底色块 |
| S4 | 切换 locale | i18n 立即生效；当前页文案切换 |
| S5 | editing 态导航离开 | `<Confirm>` 拦截 |
| S6 | 30s 后刷新 | 草稿恢复 + Toast「已恢复上次的草稿」+「清空」按钮 |
| S7 | 保存成功草稿清理 | 下次进入不再恢复 |
