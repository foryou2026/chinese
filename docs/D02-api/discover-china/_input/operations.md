<!-- TARGET-PATH: docs/D02-api/discover-china/_input/operations.md -->

# D02 · 操作输入 · discover-china

> 信息源:
> - [`function/01-china/ai/F2-AI-接口规范/`](../../../../function/01-china/ai/F2-AI-接口规范/) 全部 11 个子文件;
> - [`function/01-china/prd/F2-用户-操作与业务逻辑.md`](../../../../function/01-china/prd/F2-用户-操作与业务逻辑.md);
> - [`docs/D01-data/discover-china/`](../../../D01-data/discover-china/);
> - [`grules/G1-架构与技术规范/04-API接口规范.md`](../../../../grules/G1-架构与技术规范/04-API接口规范.md)。

## OP-ID 全集

| ID | 名称 | 端 | 状态 |
|----|------|----|------|
| OP-C1 | 列出 12 类目 | app | ✅ |
| OP-C2 | 类目下文章列表(已发布) | app | ✅ |
| OP-C3 | 文章详情(含句子) | app | ✅ |
| OP-C4 | 触发 / 获取句子 TTS | app | ✅ |
| OP-C5 | 全文朗读清单 | app | ✅ |
| OP-C6 | 上报阅读进度 | app | 🚫 已下线(2026-04) |
| OP-C7 | 读取阅读进度 | app | 🚫 已下线(2026-04) |
| OP-A1 | 管理端 12 类目卡片 | admin | ✅ |
| OP-A2 | 类目下文章列表(全状态分页) | admin | ✅ |
| OP-A3 | 文章详情(无句子) | admin | ✅ |
| OP-A4 | 新建文章 | admin | ✅ |
| OP-A5 | 编辑文章基本信息 | admin | ✅ |
| OP-A6 | 发布文章 | admin | ✅ |
| OP-A7 | 下架文章 | admin | ✅ |
| OP-A8 | 删除文章(软删) | admin | ✅ |
| OP-A9 | 句子列表(分页) | admin | ✅ |
| OP-A10 | 句子详情 | admin | ✅ |
| OP-A11 | 新建句子(start/end/after) | admin | ✅ |
| OP-A12 | 编辑句子 | admin | ✅ |
| OP-A13 | 删除句子(软删 + 自动重排) | admin | ✅ |
| OP-A14 | 批量重排句子 | admin | ✅ |
| OP-A15 | 全局搜索(文章 + 句子聚合) | admin | ✅ |
| OP-I1 | TTS Mock 内部回调 | internal | ✅ |
| OP-I2 | 健康检查 | internal | ✅ |
| OP-AUX | TTS 状态轮询(GET) | app | ✅ |
