<!-- TARGET-PATH: docs/C05-prd/course/admin/09-design-summary.md -->

# 09 · 设计摘要 · course / **admin**

> admin 端 UI 固定中文(zh),不切语;**仅** 内容字段录入 5 语。

## 9.1 视觉调性

| 维度 | admin 端选择 |
|------|------------|
| 主色 | 沿用 B04 主色;减饱和度(工具感) |
| 暗色模式 | 必须支持(夜间编辑场景) |
| 字号基线 | 中文 14px(默认),数据密度高 |
| 信息密度 | 高;表格 + 侧栏 + toolbar |

## 9.2 关键组件(↑ [B04 05-components](../../../B04-design/design-system/05-components/))

| 高频组件 | 来源 |
|---------|------|
| `Table` | [B04 05-08-table.md](../../../B04-design/design-system/05-components/08-table.md) |
| `Form` | [B04 05-07-form.md](../../../B04-design/design-system/05-components/07-form.md) |
| `Modal` | [B04 05-06-modal.md](../../../B04-design/design-system/05-components/06-modal.md) |
| `Tabs` | [B04 05-09-tabs.md](../../../B04-design/design-system/05-components/09-tabs.md) |
| `Toast` | [B04 05-10-toast.md](../../../B04-design/design-system/05-components/10-toast.md) |

## 9.3 交互模式

- **toolbar 在表格上方**:批量操作 / 导入 / 导出 / 新增统一在 toolbar
- **侧栏导航**:固定左侧 9 大模块入口;选中态高亮
- **拖拽**:章 / 节顺序通过拖拽手柄;**禁用** 整行拖拽避免误操作
- **二次确认**:所有删除 / 撤回 / 高危操作必须 Modal 确认;高危加输入"确认"才允许

## 9.4 响应式

- admin 仅支持桌面浏览器(≥ 1280 px);移动设备访问显示"建议在桌面访问";
- 不做暗色 / 亮色随系统;由用户在 [P-auth-003](../../../auth/admin/06-page-specs/P-auth-003.md) 手动切。

## 9.5 录入态约束

- 5 语字段使用 Tab 切换(zh / en / vi / th / id);**5 key 全填** 才可保存草稿,**5 key 全填且非空** 才可发布;
- 富文本仅在节讲解 / 文章正文出现;其余字段纯文本。
