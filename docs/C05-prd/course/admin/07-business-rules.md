<!-- TARGET-PATH: docs/C05-prd/course/admin/07-business-rules.md -->

# 07 · 业务规则 · course / **admin**

## 内容编辑

| R-ID | 规则 |
|------|------|
| R-013 | 任何文本字段写入必须 5 key {zh,en,vi,th,id} 齐 |
| R-014 | 章节排序必须连续,允许虚拟"占位" |
| R-015 | 删除有引用的资源弹危险确认 |
| R-016 | 题目答案必须至少 1 个正确;选项 ≥ 2 |
| R-017 | KP 与节多对多;不能成环 |
| R-022 | 节关联 KP 上限 5 个 |
| R-023 | 题目关联 KP 上限 3 个 |

## 媒资

| R-019 | 上传按 sha256 去重;命中显示原始上传者(super 可查)|

## 审核

| R-018 | 举报跨端规则同 app(显示给 admin 处置)|
| R-024 | 举报处置必须填 reason;72h 未处置升级 super |

## 发布 / 回滚

| R-030 | 已发布资源 30 天内 super 才能 unpublish;30 天后 content_admin 也可 |
| R-021 | 全局搜索 admin uid 范围限于 tracks_scope |

## 权限

| R-028 | tracks_scope = [] 视为无权 |
| R-029 | DB 走 service_role 跳 RLS;过滤靠 SQL WHERE |
