<!-- TARGET-PATH: docs/C02-ia-interaction/discover-china/01-feature-catalog.md -->

# 功能模块清单

> **阶段**：C02-IN · **功能**：`discover-china`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端模块

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID |
|------|------|----------|---------|
| M-discover-browse | 分类 / 文章浏览 / 搜索 | R-discover-china-001/002/003/005 | P-app-discover-china-001/002/003 |
| M-discover-tts | 句子级 TTS 播放 | R-discover-china-004 | P-app-discover-china-003 |
| M-discover-i18n | 5 语切换 + UI 语种 | R-discover-china-028 | 横切 3 页 |

> 不在 app 端：M-discover-content / M-discover-search-admin。

---

## admin 端模块

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID |
|------|------|----------|---------|
| M-discover-category | 分类树 CRUD | R-discover-china-013 | P-admin-discover-china-001 |
| M-discover-content | 文章 + 句子编辑发布 | R-discover-china-014/015/016/017 | P-admin-discover-china-002/003 |
| M-discover-tts-admin | 句子 TTS 重新生成 / 失败重试 | R-discover-china-019 | P-admin-discover-china-003 |
| M-discover-search-admin | 索引重建 / 数据校验 | R-discover-china-021 | P-admin-discover-china-004 |
