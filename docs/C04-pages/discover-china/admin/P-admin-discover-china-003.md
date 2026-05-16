<!-- TARGET-PATH: docs/C04-pages/discover-china/admin/P-admin-discover-china-003.md -->

# `P-admin-discover-china-003` · 文章编辑(基本信息 + 句子)

> **path**:`/admin/china/articles/:id` · **R 覆盖**:R-010..R-015, R-017, R-019
> **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- sticky 顶栏:`返回文章列表` · 文章标题(中) · 右侧 `发布或下架 / 保存` 按钮组(脏态高亮);
- 上半区(D-2):文章基本信息内联编辑(5 Tab 切语言 + 拼音 + 状态);
- 下半区:句子列表(分页),每句卡片 + 行操作 `编辑 / +在后插入 / 删除`;
- 右侧浮动操作栏:`+ 在开头添加` · `+ 在结尾添加` · `句子重排(D-7)` · `删除文章(D-5)`。

## 2. DOM 骨架
```
StickyTopbar { BackBtn, h2 中文标题, BtnGroup[发布或下架, 保存(主)] }
ArticleInfoArea(D-2) {
  LangTabs[ 中 / 英 / 越 / 泰 / 印尼 ]
  Field 拼音
  Field 标题(当前 Tab 语言)
  StatusBadge
  DirtyDot
}
SentenceListToolbar { TotalBadge "共 N 句", SearchBox(本文章), AddBtn[在开头 / 结尾], ReorderBtn(D-7) }
SentenceList {
  SentenceCard ×N {
    SeqBadge {句子顺序号}
    pinyin (preview, 当前 Tab 显示)
    chinese (preview)
    local (preview, 当前 Tab 语言)
    Actions[ 编辑(D-3) / +在当前后插入(D-4) / 删除(D-5) ]
  }
}
Pagination
```

## 3. 数据
- `GET admin/china/articles/:id` + `GET admin/china/articles/:id/sentences?page&pageSize&q`;
- `PUT admin/china/articles/:id`(标题 5 语 + 拼音 + 状态);
- `POST admin/china/articles/:id/sentences { after_句子顺序号? | position: "head"|"tail" }`;
- `PUT admin/china/sentences/:id`;
- `DELETE admin/china/sentences/:id`(自动重排 句子顺序号 + 缓存键失效);
- `POST admin/china/articles/:id/sentences/reorder { order: [id...] }`。

## 4. 状态
| 态 | 表现 |
|---|------|
| idle | 默认 |
| dirty | 顶栏保存按钮高亮 + DirtyDot |
| saving | 按钮 loading |
| save-conflict | Toast"该内容在你编辑期间被 {name} 修改过,已覆盖"(R-017) |
| publish-blocked | 5 语未齐:Modal 列错误 + 跳到首个缺失句(R-013 / R-013 联动 + E7) |
| sentence-empty | 文章无句子 → 空态"还没有句子,点击下方添加首句" |
| deleted-toast | 删除句子后 Toast"已删除并重排" |

## 5. 交互
- **D-2 切 Tab**:同字段切换,字段 onChange 标 dirty;
- **保存**:`PUT` 全量;若 更新时间(本地) < `server` → 后写覆盖 + Toast(R-017);
- **发布**:先客户端校验所有句子 5 语齐;否则弹错误 Modal;
- **下架**:D-5 二次确认 + 说明"将清空所有用户进度";
- **句子编辑 D-3**:Drawer 600px,5 Tab + 拼音 + 中文校对;保存归列表;
- **句子新建 D-4**:同 D-3,带"插入位置:开头 / 结尾 / 在第 N 句后";
- **句子删除**:D-5 确认;删除后所有 > 当前 句子顺序号 的 -1,音频缓存键随之失效(R-012);
- **句子重排 D-7**:Drawer 拖拽 → 保存触发批量 句子顺序号 重写;
- **未保存离开拦截**:任意 dirty → 路由切换 / 关闭 → 弹 D-6(R-015)。

## 6. 错误码
- 422 5 语未齐 → 字段下内联 + Modal 汇总;
- 409 并发后写覆盖 → 已在 save-conflict 处理;
- 404 文章被并发删除 → Toast + 跳列表;
- 5xx → Retry。

## 7-10. 略,沿管理端通用约定。
