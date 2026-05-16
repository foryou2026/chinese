<!-- TARGET-PATH: docs/D01-data/discover-china/_input/data-rules.md -->

# D01 · 数据规则输入 · discover-china

> 信息源:
> - [`function/01-china/ai/F1-AI-数据模型规范/`](../../../../function/01-china/ai/F1-AI-数据模型规范/) 全部 10 个子文件;
> - [`docs/C01-requirements/discover-china/baseline.md`](../../../C01-requirements/discover-china/baseline.md) §4 边界与不变量;
> - [`grules/G1-架构与技术规范/03-数据库规范.md`](../../../../grules/G1-架构与技术规范/03-数据库规范.md)。

## 关键约束摘要

1. **schema**:`zhiyu`(自托管 Supabase Postgres 16);
2. **多语言**:5 语 key 集合 `{zh,en,vi,th,id}`;`name_i18n` / `description_i18n` / `title_i18n` 用 jsonb,句子内容按性能拆 `content_<lang>` 5 列;
3. **类目固定字典**:12 条种子写入,前端不可 CRUD,FK 走 `ON DELETE RESTRICT`;
4. **软删 30 天 + 不支持恢复**:`china_articles` / `china_sentences` 仅 `deleted_at`,cron 物理清理;
5. **文章编码**:12 位 [A-Z0-9](去掉易混淆 I/O/0/1),RPC `fn_gen_article_code()` 重试 5 次防碰撞;
6. **句子 seq_no**:int 1..9999,UI 4 位左补零;删除 / 重排自动连续重写 RPC;
7. **TTS 音频缓存键**:Storage 路径 `china-tts/{article_code}/{seq_no_padded}.mp3`,DB 字段 `audio_url_zh`,重排自动失效;
8. **下架副作用**:`published → draft` 必须清空所有用户该文章学习进度(跨域 `fn_clear_progress_by_article`)。
