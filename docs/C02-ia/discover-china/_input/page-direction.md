<!-- TARGET-PATH: docs/C02-ia/discover-china/_input/page-direction.md -->

# I01 · 信息架构方向 · discover-china

> 反向回写自 〔历史素材〕

## 双 surface 三层一致
- 应用端:`/china` → `/china/categories/:code` → `/china/articles/:code`(3 层逐层下钻);
- 管理端:`/admin/china` → `/admin/china/categories/:code` → `/admin/china/articles/:id`(对应 3 层 + 全局搜索 1 页);
- 两侧导航互不交叉,管理端走 super_admin 守卫。

## 模块分组
- M-1 应用端浏览(3 页);
- M-2 管理端类目;
- M-3 管理端文章;
- M-4 管理端句子(嵌入文章编辑页);
- M-5 全局搜索(管理端独立页)。

## 8 个公共组件 / 弹窗
新建文章 Modal / 文章信息内联区 / 句子编辑 Drawer / 句子新建 Drawer / 二次确认 Modal / 未保存提示 Modal / 句子重排 Drawer / 登录提示 Modal。
