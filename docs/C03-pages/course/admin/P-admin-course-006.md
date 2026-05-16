<!-- TARGET-PATH: docs/C03-pages/course/admin/P-admin-course-006.md -->

# P-admin-course-006 · 学员举报处理

> F3 源:`P-admin-course-006` · 路由 `/admin/course/report` · R-018/024

## 1. 进入条件
- `content_admin / super`(`readonly` 只读)。

## 2. 初始数据
- `GET /admin/course/report?status=open&cursor=` → 按 `question_id` 聚合,`report_count` 倒序;`≥3 自动置顶`;
- 字段:`question_code / question_title_zh / kp_code / track / report_count / latest_report_at / status`。

## 3. 主要交互
- 行点击 → D-7 举报详情抽屉(列出所有未处理举报 + 用户 / 时间 / 文字);
- D-7 内按钮:
  - [跳目标编辑] → 跳 P-admin-course-005 题目 Drawer;
  - [采纳] → D-8 选择关联动作(改了哪些字段)→ 标记 adopted(不自动改 `is_published`);
  - [忽略] → D-8 备注原因 → 标记 dismissed;
- 顶部筛选:状态(open / adopted / dismissed)/ 主题 / 举报数 ≥ N / 时间段。

## 4. 弹窗
- D-7 详情抽屉 · D-8 处理动作

## 5. 状态
- 加载:列表骨架;
- 空:无未处理举报 → 庆祝态;
- 错误:加载失败 → 错误条。

## 6. 响应式
- 标准列表 / 详情抽屉模式。

## 7. 不变量回链
R-024 历史 `user_answers` 不追溯、采纳/忽略不自动改发布、`content_action_log` 留痕。
