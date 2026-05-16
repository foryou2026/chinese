<!-- TARGET-PATH: docs/D01-data/discover-china/07-volume-growth.md -->

# 07 · 容量与增长估算

## 基线(v1.0 上线 6 个月内)

| 表 | 行数 | 单行平均 | 总空间 | 增速 |
|----|------|---------|--------|------|
| `china_categories` | 12(固定) | 1 KB | < 16 KB | 0 |
| `china_articles` | 100..500 | 1.5 KB | < 1 MB | ~50 / 月 |
| `china_sentences` | 5000..30000 | 4 KB(含 5 语) | ~100 MB | ~3000 / 月 |
| Storage TTS mp3 | 5000..30000 | 30 KB(平均 4s @ 64kbps) | ~1 GB | ~100 MB / 月 |

## 索引开销

- `china_sentences` GIN(zh)≈ 30 MB @ 30k 行;
- 部分索引 `WHERE deleted_at IS NULL` 节省 ~30% 体积。

## 关键瓶颈

- TTS mp3 存储增长最快 → Storage 桶生命周期策略:30 天未访问归档冷存储;
- 句子表 jsonb / GIN 重建在 100k 行后需 `REINDEX CONCURRENTLY`;
- 学习进度表(他域)增长与 DAU × 已读文章数挂钩,与本域无直接耦合。

## 性能 SLO

| 接口 | P95 | 备注 |
|------|-----|------|
| 应用端类目列表 | < 50ms | CDN 边缘缓存 60s |
| 应用端文章列表 | < 100ms | DB + 应用层 SWR 30s |
| 应用端句子列表 | < 150ms | 句子 + 文章 join |
| 管理端文章 CRUD | < 200ms | service-role |
| 管理端全局搜索 | < 300ms | GIN(zh) + ILIKE 兜底 |
| TTS 首次生成 | < 2000ms | 外部依赖,失败立即返回不阻塞 |
| TTS 命中缓存 | < 200ms | Storage CDN |
