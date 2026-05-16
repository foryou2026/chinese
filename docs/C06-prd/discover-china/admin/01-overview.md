<!-- TARGET-PATH: docs/C06-prd/discover-china/admin/01-overview.md -->

# 01 · 总览 · discover-china / **admin**

> 跨端真相在 [`../_shared/`](../_shared/)。

## 1.1 admin 端定位

`discover-china` admin 端由 **`super` 独立维护**(无 `content_admin` 分权;feature 体量小,集中管控),负责 **12 类目命名维护 + 文章 + 句子 + TTS 音频上传 + 发布管控**。来源:〔历史素材〕。

## 1.2 admin 端 4 大页

| 页面 | 入口 |
|------|------|
| 分类管理(12 固定类目名称 5 语) | [P-admin-discover-china-001](06-page-specs/P-admin-discover-china-001.md) |
| 文章列表 + 发布 | [P-admin-discover-china-002](06-page-specs/P-admin-discover-china-002.md) |
| 文章编辑 + 句子 / TTS | [P-admin-discover-china-003](06-page-specs/P-admin-discover-china-003.md) |
| 搜索运维(索引重建) | [P-admin-discover-china-004](06-page-specs/P-admin-discover-china-004.md) |

## 1.3 关键运营规则

1. **12 类目固定**:类目数量与编码 **不可** 增删;`super` 仅能修改 5 语名称 / 说明。
2. **文章编码**:12 位,系统生成,不可改;**句子编码**:4 位,0001 起,系统生成。
3. **必须 5 语齐备** 才可发布(zh / en / vi / th / id 全 key)。
4. **TTS 音频**:每句独立 1 个 MP3;支持后台批量生成(线下产出后上传)或单句重传;CDN 强缓存。
5. **发布即生效**;撤回 > 30 天需再确认(与 course 一致)。
6. **删除文章**:仅当未被任何"最近阅读"游标引用 / 或引用清零 30 天后允许硬删除;否则软删除。

## 1.4 性能基线

| 操作 | 目标 |
|------|------|
| 文章列表(100 / 页) | P95 ≤ 400 ms |
| 单文章保存(含 100 句子) | P95 ≤ 600 ms |
| 单句 TTS 上传 | 走预签名 URL |
| 索引重建(全量 12 类目)| 异步,≤ 5 min |
