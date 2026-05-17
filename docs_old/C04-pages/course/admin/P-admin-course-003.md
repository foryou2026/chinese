<!-- TARGET-PATH: docs/C04-pages/course/admin/P-admin-course-003.md -->

# P-admin-course-003 · 节编辑

> F3 源:`P-admin-course-003` · R-015

## 1. 进入条件
- admin + 节所属 `track ∈ 主题范围`。

## 2. 初始数据
- → 节基本信息(`code / 多语标题字段 / objective_i18n / 句子顺序号 / is_quiz_required / 发布态)+ 节-知识点关联 关联 KP 列表(按 ``seq` 排序)+ 与节绑定的节末小测 blueprint 引用。

## 3. 主要交互
- 顶部基本信息表单(5 语 Tab 填 多语标题字段 / `objective_i18n`)+ [保存];
- KP 绑定列表:[+ 关联已有 KP] 弹搜索 Modal(可选已存在 KP)/ [+ 新建 KP] 跳 P-admin-course-004 Drawer;
- 调序 Drawer:拖拽 → 保存重写 `节-知识点关联.seq`;
- [发布] / [下架] 行级按钮 → D-4 级联确认(发布)/ D-3 确认(下架);
- 节末小测配置入口跳 P-admin-course-008(同节绑定);
- 表单脏 + 切换 → D-2 离开拦截;
- LWW 冲突 → D-6 Toast。

## 4. 弹窗
- D-2 / D-3 / D-4 / D-6 / D-16(关联/新建 KP)

## 5. 状态
- 加载:表单 + 列表骨架;
- 空:无 KP → 引导添加;
- 错误:保存失败 / 冲突 → Toast + 留在页面。

## 6. 响应式
- ≥1280px:左基本信息 + 右 KP 列表;
- <1280px:垂直堆叠,KP 列表在下。

## 7. 不变量回链
§4 节固定 12 KP 建议、节-知识点关联 多对多、SM-course-form-dirty、§4 多语必填发布前校验。
