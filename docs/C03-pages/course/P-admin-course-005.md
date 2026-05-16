<!-- TARGET-PATH: docs/C03-pages/course/P-admin-course-005.md -->

# P-admin-course-005 · 题目列表 + 双开预览

> F3 源:`P-A-5` · 路由 `/admin/course/question` · R-017/022/024

## 1. 进入条件
- admin。

## 2. 初始数据
- `GET /admin/course/question?filters=...&cursor=&limit=50` → 列表;字段:`code / type / kp_code / difficulty / report_count / is_published / version / updated_at`;
- 顶部筛选:主题 / 题型(12 种)/ KP / 难度 / 状态 / 举报数 ≥ N。

## 3. 主要交互
- **双开布局**:左列表 + 右预览(1:1 复用应用端答题组件实时渲染当前选中题);
- 行点击 → 右侧预览;预览下方"编辑解析"快速编辑解析 + 标准答案保存;
- 全字段编辑通过 D-16 Drawer 打开(选项 / 答案 / 解析 / 翻译 / 媒资);
- 行内 + 批量发布 / 下架 / 删除;
- 删除 → 反查 attempt snapshot 引用,有 snapshot 不可硬删,只能下架(已发卷快照保留);
- 保存 → `version+1`,LWW 冲突 → D-6;
- 学员举报跳转入口:点列表"举报数 N" → 跳 P-admin-course-006 过滤本题。

## 4. 弹窗
- D-1 / D-2 / D-3 / D-6 / D-15 批量导入 · D-16 编辑 Drawer

## 5. 状态
- 加载:列表 + 预览骨架;
- 空:无题 → "去导入"或"绑 KP 后新建";
- 错误:预览渲染失败 → 占位 + 错误详情。

## 6. 响应式
- ≥1440px:左列表 + 右预览 1:1;
- <1440px:单列表,行点击进全屏 Drawer 预览。

## 7. 不变量回链
R-024 历史不追溯 / R-025 动态均分 / §4 题 code 格式 `q_{track}_{seq8}` / SM-course-content-publish / SM-course-form-dirty。
