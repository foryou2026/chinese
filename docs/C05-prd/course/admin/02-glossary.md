<!-- TARGET-PATH: docs/C05-prd/course/admin/02-glossary.md -->

# 02 · 术语(admin 端局部)

> 项目级术语见 [`../../_glossary.md`](../../_glossary.md);跨端术语见 [`../_shared/glossary.md`](../_shared/glossary.md)。本文件仅列 admin 端运营术语。

| 术语 | admin 端定义 |
|------|-------------|
| **scope(权限范围)** | `content_admin` 角色绑定的 `tracks_scope` 列表(JSON array of track_code);所有列表 / 详情接口自动按 scope 过滤 |
| **批次(batch)** | 一次性导入的 KP / 题目集合,带 `batch_id` + `source_file_hash`,可整体回滚 |
| **点检(QC)** | 发布前的人工 / 抽检流程;P-005 提供抽检 UI |
| **试抽(trial draw)** | 阶段考的题目卡片预览功能(2025-11 新增) |
| **撤回(unpublish)** | 内容从学员侧下架;> 30 天需 super 二次确认;影响学员当前游标节时回滚到上一个 published 版本 |
| **灰度** | 仅对部分订阅用户可见;v1.0 不做,Round 10+ 评估 |
| **媒资(asset)** | 音频 / 图片;独立表 + 引用计数;>= 1 引用不可删 |
| **scope 越权** | `content_admin` 操作非自己 `tracks_scope` 时:UI 隐藏 + 服务端 403;写入 `audit_logs` |
