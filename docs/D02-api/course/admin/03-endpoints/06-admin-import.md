<!-- TARGET-PATH: docs/D02-api/course/admin/03-endpoints/06-admin-import.md -->

# 03-6 · 管理端 · 内容导入 (OP-A15)

## OP-course-admin-015a · `POST /import-batches:preview`
- 角色:content_admin+
- Content-Type:`multipart/form-data` (file = csv/xlsx)
- 表单字段:`{ import_type: 'kp|question|media', track? }`
- 副作用:
  1. 计算 `payload_hash`(整文件 sha256);
  2. 若 `(payload_hash, import_type)` 已存在 → 直接返回已有批次(`status='ready' or 'imported'`)幂等;
  3. 否则 INSERT batch(status='draft') → 异步 worker 解析 + 行级校验 → UPDATE status='validating' → 'ready'/'failed';
- 响应 200:
  ```json
  { "batch_id": "...", "status": "draft|ready|failed",
    "summary": {"row_count":120,"success_count":118,"failed_count":2},
    "errors": [{"row":3,"field":"content.tone","message":"..."}] }
  ```

## OP-course-admin-015b · `POST /import-batches/:id:import`
- 用途:确认导入(从 status='ready' → 'imported')
- 副作用:事务内批量 INSERT KP/Question(用 batch 内行,`source_batch_id=batch.id`);失败回滚,状态置 'failed';
- 响应:`{ imported_count, status:'imported' }`
- 错误:`COURSE_IMPORT_HAS_ERRORS` 409(status != 'ready')

## `GET /import-batches/:id`
- 响应:`{ batch, errors[] }`

## `GET /import-batches`
- Query:`?import_type=&track=&status=&page=`
