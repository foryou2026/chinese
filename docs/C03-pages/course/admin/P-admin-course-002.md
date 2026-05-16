<!-- TARGET-PATH: docs/C03-pages/course/admin/P-admin-course-002.md -->

# P-admin-course-002 · 主题-阶段-章-节四级列表

> F3 源:`P-admin-course-002` · 路由 `/admin/course/tree?track={track}` · R-014/023

## 1. 进入条件
- admin + `track ∈ tracks_scope`。

## 2. 初始数据
- `GET /admin/course/tree?track={track}&depth=4` → 阶段[6] → 章[6] → 节[6] 树形;每节字段 `code / title_i18n.zh / is_published / kp_count / question_count`;
- 节点 lazy expand(章/节默认折叠首屏只渲染阶段)。

## 3. 主要交互
- 拖拽排序:阶段 / 章 / 节内同级拖动 → `PATCH /admin/course/{level}/reorder` 写 `seq_no`;
- 行内操作:[发布] / [下架] / [进入编辑];
- 章发布 → D-4 级联确认("将级联发布 N 个节、N 个 KP、N 个题")→ `POST /admin/course/chapter/{id}/publish?cascade=true`;
- 节发布 → 类似 D-4(级联 KP+题);
- 下架:章下架只切自身(D-3 确认),不级联;
- 节标题点击 → 跳 P-admin-course-003;
- 新建:阶段 / 章 / 节按钮 → D-16 新建表单。

## 4. 弹窗
- D-3 批量发布 / 下架 · D-4 级联发布 · D-16 新建表单 · D-10 主题缺口

## 5. 状态
- 加载:树骨架;
- 空:主题骨架尚未建 → "去创建"按钮;
- 错误:树加载失败 → 顶部错误条;
- 拖拽:落位时显示 hover 高亮 + 确认动效。

## 6. 响应式
- ≥1024px:左侧树 + 右侧选中节点详情;
- <1024px:仅树,点击节点跳详情。

## 7. 不变量回链
R-023 级联规则(章→节→KP+题、节→KP+题、下架不级联)、§4 节 code 格式、`is_published` 二态。
