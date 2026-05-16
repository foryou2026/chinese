<!-- TARGET-PATH: docs/D02-api/course/admin/03-endpoints/09-admin-search-stats.md -->

# 03-9 · 管理端 · 全局搜索 / 统计大屏 (OP-A23..A24)

## OP-course-admin-023 · `GET /search`
- 角色:readonly+
- 限流:30 / 分
- Query:`?q=<text>&types=kp,question,lesson&track=&limit_per_type=10`
- 响应:`{ kps:[{id,kp_code,title_zh,kp_type,highlight}], questions:[...], lessons:[...] }`
- 实现:基于 `to_tsvector('simple', title_zh || ' ' || coalesce(translations->>'en',''))`;不支持拼音(F2 Q7)
- 错误:`COURSE_FIELD_TOO_LONG` 400(q > 100 字符)

## OP-course-admin-024 · `GET /stats/overview` / `GET /stats/track/:track`
- 角色:readonly+
- 数据源:`mv_course_track_stats`(10 分钟刷新)
- 响应:
  ```json
  {
    "kp_total": 11200, "active_learners_30d": 8214, "answers_today": 18230,
    "accuracy_today": 0.78, "lessons_passed_today": 412,
    "by_track": [{"track":"ec","kp":..,"q":..,"learners":..}]
  }
  ```
- 路径变体:`/stats/track/:track` 返单主题维度
