<!-- TARGET-PATH: docs/C04-pages/course/admin/P-admin-course-008.md -->

# P-admin-course-008 · 考试中心管理(分层)

> F3 源:`P-admin-course-008` · 路由 `/admin/course/exam` · R-020/025

## 1. 进入条件
- admin。

## 2. 初始数据
- 顶部主题选择 → `GET /admin/course/exam/list?track={track}` → 按 `scope_type` 分组列出:
  - `lesson_quiz`(节末小测)/ `chapter_test`(章测)/ `stage_exam`(阶段考)/ `hsk_mock`(HSK 主题独有);
- 字段:`code / scope_type / scope_id(章/节/阶段)/ blueprint JSON / pass_score / time_limit_sec / is_published`。

## 3. 主要交互
- 点击考试行 → 进入编辑页;
- blueprint 编辑器:可视化配置每题型抽题数 + 难度分布 + 来源池(同节 / 同章 / 同阶段);
- [试抽预览] → D-9 抽屉调 `POST /admin/course/exam/{id}/sample` 返抽题列表 + 1:1 用户端渲染;**不写 attempt**;
- 试抽失败(题量不足)→ Toast,[发布] 按钮置灰(FX-course-02);
- [发布] → D-1 确认 → `is_published=true`;
- 节末小测节点联动:每节最多 1 条 `lesson_quiz`,与 P-admin-course-003 节关联绑定。

## 4. 弹窗
- D-1 发布确认 · D-2 离开拦截 · D-9 试抽预览抽屉 · D-16 blueprint 编辑 Drawer

## 5. 状态
- 加载:骨架;
- 空:未配置 → 引导添加;
- 错误:试抽失败 → Banner 提示题源不足。

## 6. 响应式
- ≥1280px:左列表 + 右编辑器;
- <1280px:单页面层级跳转。

## 7. 不变量回链
R-020 / R-025 满分 100 动态均分、阶段考通过解锁、决策 H5 不可重考、FX-course-02 试抽失败拦截发布。
