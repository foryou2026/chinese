<!-- TARGET-PATH: docs/C02-ia/discover-china/admin/02-flows.md -->

# 02 · 关键流程 · discover-china / **admin**

## F-admin-disc-1 · 新分类 + 文章 + 发布

```
P-admin-discover-china-001(分类) → 新建分类(5 语) → P-002(文章列表)
                                → 新建文章 → P-003(编辑器:正文 + 句子拆分)
                                → 句子 TTS 异步生成 → 全部就绪后 → 发布
```

## F-admin-disc-2 · 索引重建

```
P-admin-discover-china-004(搜索运维) → "重建索引" → 异步任务 → 进度条
                                    → 完成 → 校验报告
```

## F-admin-disc-3 · TTS 失败重试

```
P-003 句子列表 → 状态 failed → "重生成" → POST /sentences/:id/tts:regen
              → 队列 → 完成 / 再失败(达上限上报告警)
```
