<!-- TARGET-PATH: docs/C06-prd/discover-china/admin/07-business-rules.md -->

# 07 · 业务规则 · discover-china / **admin**

| R-013 | 分类删除前必须为空 |
| R-014 | 文章草稿态可保存任意字段;发布前校验 5 语完整 |
| R-015 | 句子拆分后序号自动连续;手动调序后台校验 |
| R-016 | 文章发布触发全文索引异步 |
| R-017 | 文章 unpublish 不删除 TTS 缓存(留 7 天) |
| R-019 | TTS 重生成 5 次失败上报告警 |
| R-021 | 索引重建为运维操作;只 super 可触发 |
