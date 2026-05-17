<!-- TARGET-PATH: docs/C02-ia-interaction/course/02-flows.md -->

# 业务流程

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16

---

## 一、跨端共享流程

| Flow-ID | 标题 | 类型 | 涉及 P-ID |
|---------|------|------|---------|
| FL-course-01 | 内容上架主链路 | 主 | P-admin-course-002~008 |
| FL-course-02 | 学员学习一节 | 主 | P-app-course-002 |
| FL-course-03 | SRS 每日复习 | 主 | P-app-course-004 |
| FL-course-04 | 考试（4 类）| 主 | P-app-course-006/007/008 |
| FL-course-05 | 学员举报闭环 | 主 | P-admin-course-006 / P-admin-course-005 |
| FL-course-06 | 首次进入引导 | 主 | P-app-course-001 |
| FX-course-01 | 答题弱网入本地队列 | 异常 | P-app-course-002/004/006 |
| FX-course-02 | 试抽失败 → 发布拦截 | 异常 | P-admin-course-008 |
| FX-course-03 | 题目下架 attempt 不变 | 异常 | P-admin-course-005 / P-app-course-006 |
| FX-course-04 | 媒资引用拦截 | 异常 | P-admin-course-007 |
| FX-course-05 | 阶段考已通过不可重考 | 异常 | P-app-course-006 |
| FX-course-06 | 节包预下载部分失败 | 异常 | P-app-course-002 |
| FX-course-07 | 多管理员并发覆盖 | 异常 | P-admin-course-004/005 |

---

## 二、app 端流程（F-app-course-N）

### F-app-course-1 · 注册到首次学习（冷启动）

```
landing → 注册 → 验证邮件 → 登录
       → P-app-course-001（首页：无轨道）→ 选择轨道（M-onboarding）
       → P-app-course-001（首页：进入轨道地图）
       → P-app-course-002（节）→ P-app-course-003（答题）→ 完成
```

涉及 endpoint：`GET /tracks` · `POST /me/select-track` · `GET /tracks/:t/map` · `GET /lessons/:id` · `POST /answers`。

### F-app-course-2 · 日常学习闭环

```
P-app-course-001（首页）→ "今日待复习" → P-app-course-004（SRS 队列）
                                      → 逐题答题（POST /answers，update_srs=true）
                                      → 队列空 → 推荐 P-app-course-002 新节
```

### F-app-course-3 · 学员举报错题

```
P-app-course-003（答题）→ 长按题目 → D-14（举报浮层）→ POST /questions/:q/report
                       → toast "已提交，人工审核中" → 返回答题
```

### F-app-course-4 · 参加考试

```
P-app-course-001 → 考试入口 tab → P-app-course-006（考试列表）
               → 点击考试 → P-app-course-007（考试进行）
                          ↳ 60s 心跳 + 自动保存
                          ↳ 提交 → P-app-course-008（报告）
                          ↳ 中途离开 → 30 分钟后自动 abandon
```

### F-app-course-5 · 错题本回顾（独立于 SRS）

```
P-app-course-001 → 我的 → P-app-course-005（错题本）
               → 筛选（知识点 / 时间）→ 选题 → 重做（不进 SRS，仅 mark resolved）
```

---

## 三、admin 端流程（F-admin-course-N）

### F-admin-course-1 · 新建一个轨道

```
P-admin-course-001（轨道列表）→ 新建按钮 → 弹窗填轨道码 + 5 语标题
                             → POST /tracks（校验 5 key）→ 列表 +1
                             → P-admin-course-002（阶段编辑）→ 添加阶段
                             → P-admin-course-003（章节编辑，拖拽排序）
                             → P-admin-course-004（节编辑）→ 关联 KP
                             → P-admin-course-005（题目编辑）→ 关联 KP + 设答案
                             → P-admin-course-001 主操作：发布
```

### F-admin-course-2 · 批量导入（题目 / KP / 节）

```
P-admin-course-005（题目）→ "批量导入" → 上传 xlsx
                        → POST /import-batches:preview → 预览报表（成功 N / 失败 M）
                        → 确认 → POST /import-batches/:id:import → 异步
                        → 轮询 GET /import-batches/:id → 完成 → 跳转列表
```

### F-admin-course-3 · 媒资上传与去重

```
P-admin-course-007（媒资库）→ 上传 → 客户端 sha256 → POST /media（秒传命中或新增）
                           → 在 P-admin-course-004/005 选择资源 → 嵌入
```

### F-admin-course-report · 学员举报审核

```
学员侧 POST /questions/:q/report → course_reports.status=pending
admin 侧：
P-admin-course-006（举报列表）→ 筛选 pending → 点击查看
                            → 决策：
                              ├─ 修题 → 跳 P-admin-course-005 编辑 → 回 P-006 mark resolved
                              ├─ 驳回 → status=dismissed + reason
                              └─ 升级 → super 处理
                            → 同步 INSERT action_log
```

### F-admin-course-publish · 发布与回滚

```
任意编辑页 → 草稿态 → "发布" → POST /:type/:id:publish
         → 服务端校验（必填 / 关联 / 5 语 / 题目答案非空）
         → 失败：COURSE_PUBLISH_BLOCKED + 字段清单 → 回编辑页高亮
         → 成功：状态 published + 异步刷搜索索引
回滚：同 endpoint 反向 :unpublish，仅 super 可执行已发布 30 天以上的资源。
```

---

## 四、跨端联动点

| 触发（本端）| 通过 | 影响（另一端）|
|------------|------|------------|
| 学员举报 | `course_reports` insert | admin M-course-report 审核队列 +1 |
| 答题完成 | `course_answers` insert | admin M-course-search 索引异步刷新 |
| 发布（admin）| event `course.published` → 短缓存失效 | app 端轨道地图 / 节内容刷新 |
| 媒资替换（admin）| event `media.replaced` | TTS 缓存按 `kp_id` 失效 |
| 举报处置（resolved + 修题）| 题目版本升级 | 学员下次答题看到新版题 |
