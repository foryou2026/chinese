<!-- TARGET-PATH: docs/C02-ia-interaction/course/03-state-machines.md -->

# 状态机

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16

---

## SM-course-lesson-progress · 节进度（学员视角）

数据源：`学习进度.status`

```
locked ──unlock_prev_passed──▶ unlocked
unlocked ──first_enter────────▶ in_progress
in_progress ──pass_quiz(≥60%)─▶ passed
in_progress ──skip_quiz────────▶ in_progress（保留状态）
passed ──redo_kp───────────────▶ passed（不回退）
locked ──unlock_share_stage0──▶ unlocked（Stage 0 共享一次性，任一主题完成即四主题解锁）
```

---

## SM-course-content-publish · 内容发布二态

适用于 KP / Question / Lesson / Chapter

```
draft（发布态=false）──publish──▶ live（发布态=true）
live ──unpublish──▶ draft
```

级联规则：
- 章 publish → 子节 + 子 KP + 子题统一 publish
- 节 publish → 子 KP + 子题统一 publish
- 任一层 unpublish：只切自身，**不下传**

---

## SM-course-answer · 单题作答

```
shown ──submit──▶ judging ──correct──▶ scored_pass
                          └──errored──▶ scored_fail ──auto_srs──▶ srs_box_1
```

不可中途撤回，提交即终态（节末小测 / 章测 / 阶段考"统一交卷"除外：统一交卷后批量判分）。

---

## SM-course-srs · SRS Leitner 5 盒

数据源：`复习队列.box`；间隔：1 / 3 / 7 / 14 / 30 天

```
box1 ──correct──▶ box2 ──correct──▶ box3 ──correct──▶ box4 ──correct──▶ box5
任意盒 ──wrong──▶ box1（due=明天）
```

---

## SM-course-exam-attempt · 考试单次尝试

数据源：`考试记录`

```
created ──start──▶ in_progress ──submit──▶ judging ──pass──▶ passed
                                          └──fail──▶ failed
in_progress ──quit/timeout──▶ failed（score=0，不可恢复）
passed（stage_exam）──unlock_next_stage──▶（副作用，触发 SM-course-lesson-progress）
passed（stage_exam）──不可重考（BR-5）
```

---

## SM-course-form-dirty · 管理端编辑 Drawer / Modal

适用于 KP / Question / Lesson / Exam blueprint 编辑

```
clean ──edit_field──▶ dirty ──save_ok──▶ clean
                            └──save_conflict（更新时间_changed）──▶ lww_overwrite（Toast）
dirty ──route_change/close──▶ block_modal D-2（离开 / 留下）
```

---

## SM-course-offline-queue · 弱网答题本地队列

存储：localforage

```
empty ──offline_submit──▶ pending ──online_detected──▶ flushing
flushing ──all_ok──▶ empty
flushing ──partial_fail──▶ pending（retry on next online）
```
