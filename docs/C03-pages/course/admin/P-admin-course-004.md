<!-- TARGET-PATH: docs/C03-pages/course/admin/P-admin-course-004.md -->

# P-admin-course-004 · KP 列表 + Drawer

> F3 源:`P-A-4` · 路由 `/admin/course/kp` · R-016/022

## 1. 进入条件
- admin。

## 2. 初始数据
- `GET /admin/course/kp?filters=...&cursor=&limit=50` → 列表;字段:`code / type / difficulty / title_zh / lesson_count / question_count / is_published / version / updated_at / batch_id`;
- 顶部筛选:主题 / KP 类型(7 类)/ 难度 / 状态 / 导入批次 / 关键词搜索。

## 3. 主要交互
- 行点击 → D-16 Drawer 编辑(Tab:基础 / 内容 / 翻译 / 媒资 / 题目)按 KP 类型差异化字段;
- 行内按钮:[发布] / [下架] / [复制];
- 批量选择 → 顶部[批量发布][批量下架][批量删除] → D-3 确认;
- [批量导入] → D-15 上传 CSV/JSON,预览错误行,确认导入(写 `import_batches` + KP 默认 `is_published=false`);
- 保存 KP:`version+1` + LWW(冲突 → D-6 Toast);
- 删除 KP:`hash` 媒资引用反查 + lesson_kp 关联反查,有引用拦截 D-5;
- 与 P-admin-course-005 题目联动:Drawer 内"题目"Tab → 显示关联题(只读列表 + 跳编辑)。

## 4. 弹窗
- D-1 删除二次确认 · D-2 离开拦截 · D-3 批量动作 · D-5 引用拦截 · D-6 LWW · D-15 导入 · D-16 编辑 Drawer

## 5. 状态
- 加载:列表骨架;
- 空:`tracks_scope` 为空时友好拦截;
- 错误:筛选/搜索失败 → 顶部错误条。

## 6. 响应式
- ≥1280px:左列表 + 右 Drawer;
- <1280px:列表 + 全屏 Drawer。

## 7. 不变量回链
§4 KP code 格式 `kp_{track}_{type_initial}_{seq5}`、版本治理 `version+1`、`is_published` 二态、§4 5 语必填发布前校验。
