<!-- TARGET-PATH: docs/C02-ia/course/_shared/state-machines.md -->

# 03 · 状态机(SM-ID) · course

## SM-course-lesson-progress
学员视角节状态(数据源 `user_progress.status`)

```
locked  ──unlock_prev_passed──▶  unlocked
unlocked ──first_enter────────▶  in_progress
in_progress ──pass_quiz(>=60%)─▶ passed
in_progress ──skip_quiz────────▶ in_progress (保留)
passed ──redo_kp───────────────▶ passed (不回退)
locked ──unlock_share_stage0──▶ unlocked (Stage 0 共享一次性,任一主题完成即四主题解锁)
```

## SM-course-content-publish
KP / Question / Lesson / Chapter 内容发布二态(`is_published`)

```
draft (is_published=false) ─publish─▶ live (is_published=true)
live ─unpublish─▶ draft
```

级联规则:
- 章 publish → 子节 + 子 KP + 子题统一 publish;
- 节 publish → 子 KP + 子题统一 publish;
- 任一层 unpublish:只切自身,**不下传**(决策 B1-B4)。

## SM-course-answer
单题作答(`user_answers`)

```
shown ─submit─▶ judging ─correct─▶ scored_pass
                          └errored─▶ scored_fail ─auto_srs─▶ srs_box_1
```

不可中途撤回,提交即终态(节末小测 / 章测 / 阶段考"统一交卷"除外:统一交卷后批量判分)。

## SM-course-srs
SRS Leitner 5 盒(`user_srs.box`)

```
box1 ─correct─▶ box2 ─correct─▶ box3 ─correct─▶ box4 ─correct─▶ box5
任意盒 ─wrong─▶ box1 (due=明天)
间隔:1 / 3 / 7 / 14 / 30 天
```

## SM-course-exam-attempt
考试单次尝试(`user_exam_attempts`)

```
created ─start─▶ in_progress ─submit─▶ judging ─pass─▶ passed
                                     └─fail─▶ failed
in_progress ─quit/timeout─▶ failed(score=0,不可恢复)
passed/stage_exam ─unlock_next_stage─▶ (副作用,SM-course-lesson-progress)
passed/stage_exam ──不可重考(决策 H5)
```

## SM-course-form-dirty
管理端编辑 Drawer/Modal(KP / Question / Lesson / Exam blueprint)

```
clean ─edit_field─▶ dirty ─save_ok─▶ clean
                          └save_conflict(updated_at_changed)─▶ lww_overwrite(Toast)
dirty ─route_change/close─▶ block_modal D-2 [离开/留下]
```

## SM-course-offline-queue
弱网答题本地队列(localforage)

```
empty ─offline_submit─▶ pending ─online_detected─▶ flushing
flushing ─all_ok─▶ empty
flushing ─partial_fail─▶ pending(retry on next online)
```
