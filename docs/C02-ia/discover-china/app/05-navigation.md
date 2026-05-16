<!-- TARGET-PATH: docs/C02-ia/discover-china/app/05-navigation.md -->

> **本文件为 surface=`app` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端过滤实质内容)。** 跨端通用部分见 [_shared/flows-shared.md](../_shared/flows-shared.md) 与 [_shared/state-machines.md](../_shared/state-machines.md)。


# 05 · 导航

## 应用端

- 底部 / 顶部 Tab(取决于 viewport):`首页 · 课程 · 发现中国 · 我`;
- 类目内面包屑:`发现中国 > {类目名}`;
- 文章内面包屑:`发现中国 > {类目名} > {文章标题}`;
- 文章详情页右上 Anchor:`返回类目`。

## 管理端

- 侧栏菜单一级:`发现中国`(图标);
- 侧栏激活规则:`/admin/china*`;
- 面包屑:`管理后台 > 发现中国 > {类目名} > {文章标题}`;
- 面包屑节点点击回上层;
- 文章编辑页 sticky 顶栏:左侧"返回文章列表" · 中间标题 · 右侧"发布 / 下架 / 保存"按钮组;
- 文章编辑页右侧操作侧栏:句子重排 · 删除文章 · 历史(v2)。

## 全局搜索入口

- 管理端类目页 / 文章列表页顶部搜索框 → 触发后跳 `P-admin-discover-china-004` 并保留搜索范围参数 `scope=global|category|article`。
