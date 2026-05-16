<!-- TARGET-PATH: docs/D02-api/course/admin/03-endpoints/07-admin-publish-report-log.md -->

# 03-7 · 管理端 · 发布/下架/举报/操作日志 (OP-A16..A19)

## OP-course-admin-016 · `POST /:target_type/:id:publish` / `:unpublish`
- target_type:`kp | question | lesson | chapter | stage | exam`
- 角色:content_admin+
- Request:`{ reason?, cascade?: true }`
- 副作用(`fn_content_publish`):
  - 校验子项有可发布内容,否则 409 `COURSE_CASCADE_TARGET_EMPTY`;
  - 事务内切换 `is_published` + 写 `course_content_action_log(action='publish|unpublish')`;
  - 默认级联规则:
    - 章发布:级联节 + KP + 题目(可在 request `cascade=false` 关闭);
    - 节发布:级联 KP + 题目;
    - 章下架:级联节;节下架不级联 KP;
- 响应:`{ is_published, cascade_summary: { lessons_affected, kps_affected, questions_affected } }`
- 错误:`COURSE_INVALID_PUBLISH_ACTION` 400

## OP-course-admin-017 · `GET /action-log`
- 角色:content_admin+
- Query:`?target_type=&target_id=&actor_id=&action=&from=&to=&page=&page_size=`
- 响应:`{ items:[{id, target_type, target_id, action, actor_id, actor_role, reason, diff, created_at}], pagination }`
- 只读

## OP-course-admin-018 · `GET /reports`
- 用途:学员举报列表(实为 `action_log WHERE action='report'`)
- Query:`?status=pending|handled&report_type=&track=&page=`
- 响应:`{ items:[{report_id, question_id, q_code, report_type, reason, actor_id, created_at, status, handled_by, handled_action}], pagination }`
- `status` 由聚合:存在后续 `action IN ('dismiss','adopt') AND target_id=question_id AND created_at>report.created_at` 则为 handled

## OP-course-admin-019 · `/reports/:id:dismiss` / `:adopt`
- 角色:content_admin+
- Request:`{ note, fixed_target_id? }`(adopt 时可关联 fix 的题目)
- 副作用:INSERT `course_content_action_log(action='dismiss|adopt', target_type='question', target_id=report.question_id, reason=note)`
- 错误:`COURSE_REPORT_ALREADY_HANDLED` 409
