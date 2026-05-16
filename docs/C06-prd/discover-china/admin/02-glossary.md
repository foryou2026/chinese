<!-- TARGET-PATH: docs/C06-prd/discover-china/admin/02-glossary.md -->

# 02 · 术语 · discover-china / **admin**

| 术语 | 定义 |
|------|------|
| **5 语完整(5L-complete)** | 一条记录的 5 个语种 key 全部非空白;**发布前** 必须满足 |
| **句子序号锁** | 文章发布后,**已存在** 句子的 4 位编码 **不可** 改;新增句子续号 |
| **TTS 批次** | 一次上传的 MP3 集合;同一文章下,可分多批次替换 |
| **软删除** | 文章 `deleted_at` 非空;学员侧不可见;30 天后定时清理或保留 |
| **索引重建** | Postgres 全文索引 + 拼音索引重建;不可与发布并发 |
| **scope** | 本 feature **不分** scope;super 全权 |
