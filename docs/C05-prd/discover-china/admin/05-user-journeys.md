<!-- TARGET-PATH: docs/C05-prd/discover-china/admin/05-user-journeys.md -->

# 05 · 用户旅程 · discover-china / **admin**

## 5.1 主旅程

### J-admin-disc-1 · 新文章上架闭环
1. `super` 登录(2FA)→ 进入 [P-002](06-page-specs/P-admin-discover-china-002.md)
2. "新增" → [P-003](06-page-specs/P-admin-discover-china-003.md)
3. 选类目 → 填标题(5 语)+ 标题拼音 → 加句子(中文 → 自动拼音建议 → 校对 → 5 语翻译)
4. 上传句级 TTS(批量 ZIP 解包 或 单句拖入)
5. 校验 5 语完整 → 校验 TTS 数量与句子一致
6. 点击"发布" → 立刻上线

### J-admin-disc-2 · 类目命名调整
1. [P-001](06-page-specs/P-admin-discover-china-001.md) → 编辑某类目 5 语名称
2. 保存 → 立即生效;不需重建索引

### J-admin-disc-3 · TTS 重传(单句修订)
1. [P-003](06-page-specs/P-admin-discover-china-003.md) → 句子行 → "替换音频"
2. 上传新 MP3 → 立即生效;CDN 通过 query string 版本号强刷新

### J-admin-disc-4 · 索引重建
1. [P-004](06-page-specs/P-admin-discover-china-004.md) → "全量重建"
2. 系统二次确认(任务运行期间禁止发布)
3. 异步执行 ≤ 5 min;完成 toast

## 5.2 异常旅程

| ID | 触发 | 处理 |
|----|-------|------|
| J-admin-disc-X1 | 5 语未齐 | 发布按钮禁用 + 高亮缺失 key |
| J-admin-disc-X2 | TTS 数量与句子不一致 | 发布前校验失败;列出缺失 / 多余句号 |
| J-admin-disc-X3 | 索引重建期间尝试发布 | 阻断;提示等待 |
| J-admin-disc-X4 | 想删除被引用文章 | 改走软删除 + 30 天后定时清理 |
| J-admin-disc-X5 | 尝试增删类目 | UI 隐藏入口;服务端 403 |
