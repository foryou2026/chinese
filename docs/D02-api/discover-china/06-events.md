<!-- TARGET-PATH: docs/D02-api/discover-china/06-events.md -->

# 06 · 业务事件

> 通过 Postgres `pg_notify` 由 RPC 在事务提交后发出;`apps/api-app` 与 `apps/api-admin` 订阅,触发应用层缓存 invalidate。
> 现阶段不接入外部消息队列(MQ);本表给出事件契约,便于将来横切扩展。

## 事件清单

| Channel | Payload | 触发 RPC | 订阅方 | 动作 |
|---------|---------|---------|--------|------|
| `china_article_published` | `{article_id, code, category_code}` JSON | `fn_publish_article` | api-app(C2/C3 缓存)、api-admin(A2/A3 缓存) | LRU invalidate 按 category_code 和 article_code |
| `china_article_unpublished` | 同上 | `fn_unpublish_article` | 同 | 同 + 触发 `fn_clear_progress_by_article` 已在 RPC 内完成 |
| `china_article_deleted` | 同上(原 status 附在 meta) | A8 处理器(后端代码层,非 RPC) | 同 | 同 |
| `china_sentence_changed` | `{article_id, sentence_ids[]}` | `fn_insert_sentence_at` / `fn_delete_sentence` / `fn_update_sentence` / `fn_reorder_sentences` | api-app(C3 详情缓存) | 按 article_id invalidate |
| `china_tts_ready` | `{sentence_id, audio_url}` | C4 处理器写 ready 后 | api-app(C3 详情缓存,可选乐观刷新) | invalidate 该句缓存 |

## 跨域事件(不属本域,但本域是触发源)

| Channel | 触发 | 跨域副作用 |
|---------|------|-----------|
| `learning_progress_cleared` | A7 / A8 / A11(start\|after)/ A13 / A14 | learning-engine 域已经在 `fn_clear_progress_by_article` 中直接 DELETE,可同时发 notify 给监控 |

## 注意事项

- `pg_notify` payload 上限 8000 字节;超过需改走临时表 + id 索引;
- 订阅丢失场景:容器重启时通过启动 hook 全量 invalidate `china_*` 缓存;
- 现阶段无需消息持久化(应用层缓存可重建)。
