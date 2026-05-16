<!-- TARGET-PATH: docs/C05-prd/discover-china/admin/10-known-issues.md -->

# 10 · 已知问题 · discover-china / **admin**

| ID | 一句话 | 影响 | 计划 |
|----|-------|------|------|
| KI-admin-disc-001 | 大文章(>200 句)行内编辑卡顿 | [P-003](06-page-specs/P-admin-discover-china-003.md) | 虚拟滚动 |
| KI-admin-disc-002 | TTS 批量上传超 100 文件后失败概率上升 | [P-003](06-page-specs/P-admin-discover-china-003.md) | 分片 + 重试 |
| KI-admin-disc-003 | 拼音自动建议在多音字下偶尔出错 | [P-003](06-page-specs/P-admin-discover-china-003.md) | 提供建议词表 + 手动覆盖 |
| KI-admin-disc-004 | 索引重建进度无 UI 反馈 | [P-004](06-page-specs/P-admin-discover-china-004.md) | 加进度条 |

## 已澄清不修

| ID | 原因 |
|----|------|
| KI-admin-disc-005 类目数量改动 | 业务约定 12 固定;**永不** 改 |
| KI-admin-disc-006 删除文章硬删除 | 保护学员侧"最近阅读"游标 |
