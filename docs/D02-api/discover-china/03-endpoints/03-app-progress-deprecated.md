<!-- TARGET-PATH: docs/D02-api/discover-china/03-endpoints/03-app-progress-deprecated.md -->

# 应用端 · 学习进度(已下线 · DEPRECATED)

> **2026-04 产品评审决定取消阅读进度功能**。
> - `apps/api-app/src/routes/china/index.ts` 已**移除挂载**,`/api/v1/china/articles/:code/progress` 现返回 404;
> - 文件 `progress.routes.ts` / `progress.service.ts` 保留以便日后恢复,接口形状无需变更;
> - 客户端不再调用 C6 / C7;详情页移除"重新开始"按钮与"阅读进度 x/y"文案;
> - 跨域 `learning_progress` 中已存的 `source='china'` 行保留为历史数据,无需迁移;
> - **跨域副作用仍生效**:管理端 A7 下架 / A8 删除文章触发 `fn_clear_progress_by_article(article_id)` 物理删该文章对应历史进度行(PM 答 Q5)。

## 历史接口形状(参考)

| OP-ID | Method | Path | 状态 |
|-------|--------|------|------|
| OP-C6 | PUT | `/api/v1/china/articles/:code/progress` | 🚫 已下线 |
| OP-C7 | GET | `/api/v1/china/articles/:code/progress` | 🚫 已下线 |

完整原始定义见 [F2-03](../../../../function/01-china/ai/F2-AI-接口规范/03-应用端-学习进度.md)。
