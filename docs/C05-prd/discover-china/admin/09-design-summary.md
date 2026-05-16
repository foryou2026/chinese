<!-- TARGET-PATH: docs/C05-prd/discover-china/admin/09-design-summary.md -->

# 09 · 设计摘要 · discover-china / **admin**

> 视觉与 course/admin 同源;特有部分:句子编辑表 + TTS 批量上传交互。

## 9.1 关键组件(↑ [B04 05-components](../../../B04-design/design-system/05-components/))

| 组件 | 来源 |
|------|------|
| `Table`(文章 / 句子) | [B04 05-08-table.md](../../../B04-design/design-system/05-components/08-table.md) |
| `Form`(5 语 Tab) | [B04 05-07-form.md](../../../B04-design/design-system/05-components/07-form.md) |
| `Upload`(TTS 批量) | 复用 course/admin/media 同款 |
| `Modal`(发布二次确认) | [B04 05-06-modal.md](../../../B04-design/design-system/05-components/06-modal.md) |

## 9.2 编辑器特有

- **句子表格**:行内编辑;Tab 键切语种;Shift+Tab 切句号
- **拼音建议**:中文输入后 0.5s 防抖触发;`super` 可一键替换 / 整段重算
- **TTS 拖拽**:文件名匹配 4 位编码(`0001.mp3`)自动定位行;不匹配 → 列异常
- **缺失语种红角标**:列头计数;点击跳到首条缺失行

## 9.3 响应式

仅桌面(同 course/admin);移动设备提示。
