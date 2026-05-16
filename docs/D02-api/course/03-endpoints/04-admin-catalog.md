<!-- TARGET-PATH: docs/D02-api/course/03-endpoints/04-admin-catalog.md -->

# 03-4 · 管理端 · 主题/阶段/章/节 CRUD (OP-A1..A4)

> Prefix:`/admin/v1/course`。`readonly+` 读;`content_admin+` 写;`tracks_scope` 列级过滤。

---

## OP-course-admin-001 · `GET /tracks`
- 角色:readonly+
- 响应:`{ items:[...] }`(基本同 C 端,但含 `is_enabled=false` 全量)

## OP-course-admin-002 · `/stages[/:id]`
- 方法:GET 列表 / GET 详情 / POST 新增 / PATCH(If-Match) / DELETE(软删,实为禁用)
- 关键校验:
  - `stage_no` 1–6,share 才能 0;
  - 删除前校验 `course_chapters.stage_id=...` 必须为空,否则 409 `COURSE_STAGE_NOT_EMPTY`;
- 乐观锁:`If-Match: updated_at` → 409 `COURSE_STALE_VERSION`

## OP-course-admin-003 · `/chapters[/:id]` + `/chapters:reorder`
- 方法:CRUD + 调序
- `POST /chapters:reorder`:`{ stage_id, ordered_ids:[uuid] }` → 事务内 `FOR UPDATE` + 批量 UPDATE chapter_no / sort_order;
- 删除前校验:`course_lessons.chapter_id=...` 为空 → 否则 409 `COURSE_CHAPTER_NOT_EMPTY`
- 软删:`UPDATE deleted_at=now()`(30 天 cron 物理删)

## OP-course-admin-004 · `/lessons[/:id]` + `/lessons/:id:bind-kps` + `/lessons:reorder`
- 方法:CRUD + 调序 + KP 绑定
- 创建校验:`code` 必须匹配父级编号(否则 `COURSE_LESSON_CODE_MISMATCH` 400);
- `POST /lessons/:id:bind-kps`:`{ kp_orders:[{kp_id, position, is_new_in_lesson}] }`;事务内 `DELETE FROM course_lesson_kp WHERE lesson_id=$1` + 批量 `INSERT`;
- 软删:同 chapters。
- 列表 query:`?stage_id=&chapter_id=&is_published=&q=&page=&sort=`
