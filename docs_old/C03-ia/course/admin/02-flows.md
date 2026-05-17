<!-- TARGET-PATH: docs/C03-ia/course/admin/02-flows.md -->

# 02 · 关键用户流程 · course / **admin**

> Round 5 按端过滤。app 端学员流程见 [../app/02-flows.md](../app/02-flows.md)。

## F-admin-course-1 · 新建一个轨道(admin / super)

```
P-admin-course-001(轨道列表)→ 新建按钮 → 弹窗填轨道码 + 5 语标题
                          → POST /tracks(校验 5 key)→ 列表 +1
                          → 进入 P-admin-course-002(阶段编辑)→ 添加阶段
                          → P-admin-course-003(章节编辑,拖拽排序)
                          → P-admin-course-004(节编辑)→ 关联 KP
                          → P-admin-course-005(题目编辑)→ 关联 KP + 设答案
                          → P-admin-course-001 主操作:发布
```

涉及 endpoint:`POST /tracks` · `POST /stages` · `POST /chapters` · `POST /chapters:reorder` · `POST /lessons` · `POST /lessons/:id:bind-kps` · `POST /kps` · `POST /questions` · `POST /:type/:id:publish`。

## F-admin-course-2 · 批量导入(题目 / KP / 节)

```
P-admin-course-005(题目)→ "批量导入" → 上传 xlsx
                       → POST /import-batches:preview → 预览报表(成功 N / 失败 M)
                       → 确认 → POST /import-batches/:id:import → 异步
                       → 轮询 GET /import-batches/:id → 完成 → 跳转列表
```

## F-admin-course-3 · 媒资上传与去重

```
P-admin-course-007(媒资库)→ 上传 → 客户端 sha256 → POST /media(秒传命中或新增)
                          → 在 P-admin-course-004/005 选择资源 → 嵌入
```

## F-admin-course-report · 学员举报审核(对端 app 触发)

```
学员侧 POST /questions/:q:report → course_reports.status=pending
admin 侧:
P-admin-course-006(举报列表)→ 筛选 pending → 点击查看
                           → 决策:
                             ├─ 修题 → 跳 P-admin-course-005 编辑 → 回 P-006 mark resolved
                             ├─ 驳回 → status=dismissed + reason
                             └─ 升级 → super 处理
                           → 同步 INSERT action_log
```

## F-admin-course-publish · 发布与回滚

```
任意编辑页 → 草稿态 → "发布" → POST /:type/:id:publish
        → 服务端校验(必填字段 / 关联 / 5 语 / 题目答案非空)
        → 失败:COURSE_PUBLISH_BLOCKED + 字段清单 → 回编辑页高亮
        → 成功:状态 published + 异步刷搜索索引
回滚:同 endpoint 反向 :unpublish,仅 super 可执行已发布 30 天以上的资源。
```

## F-admin-course-search-stats · 搜索与统计(只读)

```
P-admin-course-009(搜索 + 统计)→ q=关键字 → GET /search → 跨表结果
                              → 切换 tab → GET /stats/overview → 卡片矩阵
```

## 跨端联动点

| 触发(本端) | 通过 | 影响(app 端) |
|------------|------|---------------|
| 发布 | event `course.published` → 短缓存失效 | app 端轨道地图 / 节内容刷新 |
| 媒资替换 | event `media.replaced` | TTS 缓存按 `kp_id` 失效 |
| 举报处置(resolved + 修题)| 同上 | 学员下次答题看到新版题 |
