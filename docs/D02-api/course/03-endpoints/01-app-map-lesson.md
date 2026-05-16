<!-- TARGET-PATH: docs/D02-api/course/03-endpoints/01-app-map-lesson.md -->

# 03-1 · 学员端 · 学习地图 / 节学习 / TTS / 节末小测 (OP-C1..C8)

> Prefix:`/api/v1/course`。请求/响应字段按 F2 源固化。

---

## OP-course-app-001 · `GET /tracks`
- 用途:列出 5 主题(C 端首页 / 切换抽屉)
- 鉴权:公开
- 响应 200:`{ ok, data: { items: [{ code, name_zh, name_i18n, icon_url, sort_order }] } }`
- DB:`SELECT * FROM course_tracks WHERE is_enabled=true ORDER BY sort_order`

## OP-course-app-002 · `POST /me/select-track`
- 用途:切换当前主题
- 鉴权:登录
- 限流:120/分
- Request:`{ track: 'share|ec|fc|hsk|dl' }`
- 响应 200:`{ current_track, redirect_to: '/learn/<track>' }`
- 错误:`COURSE_INVALID_TRACK_CODE` 400
- DB:UPDATE `auth_user_profiles.current_track` = $1(账号域字段)

## OP-course-app-003 · `GET /tracks/:track/map`
- 用途:学习地图(阶段/章/节 + 我的进度)
- 鉴权:登录
- Query:`?include=progress`(默认包含)
- 响应 200:
  ```json
  { "stages":[{"id","stage_no","title_i18n","unlock_status",
      "chapters":[{"id","chapter_no","title_i18n",
        "lessons":[{"id","code","title_i18n","est_minutes","my_status","best_score"}]}]}]}
  ```
- DB:`vw_course_lesson_full` JOIN `course_user_progress` LEFT
- 副作用:无;若无 progress 行则视为 `locked`(stage 1 chapter 1 lesson 1 默认 `unlocked`)

## OP-course-app-004 · `GET /lessons/:lesson_id`
- 用途:进入节,返 KP 卡片序列 + 断点
- 鉴权:登录;RLS 通过
- 响应 200:`{ lesson, kp_cards:[{kp_id,kp_type,content,media}], checkpoint:{last_kp_id,last_position}, progress }`
- 副作用:**首次进入**写 `course_user_progress(status='in_progress', started_at=now())`(UPSERT)
- 错误:`COURSE_NOT_VISIBLE` 404 / `COURSE_PREREQUISITE_NOT_MET` 403

## OP-course-app-005 · `GET /kps/:kp_id`
- 用途:KP 详情卡(媒体 + 翻译 + 我的 SRS 状态)
- 响应:`{ content, translations, audio_url, image_url, srs_state:{box,due_at,correct_streak} }`
- 限流:120/分

## OP-course-app-006 · `POST /kps/:kp_id/audio`
- 用途:触发 TTS(若 audio_url 已有则直接返,否则异步生成)
- 限流:20/分(UID)
- Request:`{ voice_profile?: 'xiaoxiao_zh', speed?: 1.0 }`
- 响应:
  - 200 命中缓存:`{ audio_url, duration_ms }`
  - 202 异步生成:`{ status:'pending', poll_after_ms: 1500 }`
- DB:命中走 `course_media_assets WHERE hash=...`;新增异步任务 → mock TTS adapter
- 错误:`COURSE_RATE_LIMIT` 429

## OP-course-app-007 · `PUT /lessons/:lesson_id/checkpoint`
- 用途:断点续学保存
- Request:`{ last_kp_id, last_position }`
- 响应:`{ saved: true }`
- DB:UPSERT `course_user_progress (last_kp_id, last_position, updated_at)`(单 RPC,前端 debounce)
- 错误:`COURSE_KP_NOT_IN_LESSON` 400

## OP-course-app-008 · `GET /lessons/:lesson_id/quiz`
- 用途:取节末小测(若 `lesson.has_quiz=false` 返 204)
- 响应:`{ quiz_id, questions:[{id,q_type,payload,exam_scope_excerpt}], pass_score:60, time_limit_minutes:null }`
- 抽题:`SELECT * FROM course_questions WHERE kp_id IN (lesson kp[]) AND 'lesson_quiz'=ANY(exam_scope) AND is_published AND deleted_at IS NULL ORDER BY random() LIMIT N`(N 由 lesson 配置)
- 写入:仅生成内存 `quiz_id`(uuid v4),不入 attempt 表;
- TTL:10 分钟(超时返 `COURSE_QUIZ_EXPIRED`)
