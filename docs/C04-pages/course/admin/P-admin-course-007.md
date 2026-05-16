<!-- TARGET-PATH: docs/C04-pages/course/admin/P-admin-course-007.md -->

# P-admin-course-007 · 媒资库

> F3 源:`P-admin-course-007` · 路由 `/admin/course/media` · R-019

## 1. 进入条件
- admin。

## 2. 初始数据
- `GET /admin/course/media?type=&cursor=` → 媒资列表;字段:`id / hash / kind(audio/image/video)/ size / cdn_url / ref_count / ref_kp_ids / ref_q_ids / uploaded_at / is_deleted`。

## 3. 主要交互
- 顶部上传:接受文件 → 计算 hash → 命中已存在 → 直接复用;新文件 → 写表 + 上传 CDN;
- 行点击 → 详情抽屉(预览 + 引用清单 + [软删]);
- [软删] → 若 `ref_count>0` 弹 D-5 拦截;否则 D-1 二次确认 → `DELETE soft` 写 `is_deleted=true`;
- 物理清理由后台 cron 每天扫 `is_deleted=true AND deleted_at > 30 天前` 执行,本页不操作。

## 4. 弹窗
- D-1 软删确认 · D-5 引用拦截 · 详情抽屉(自定义)

## 5. 状态
- 加载:列表骨架;
- 空:无媒资 → "去上传"占位;
- 错误:上传失败 → Toast 重试。

## 6. 响应式
- ≥1024px:网格视图;
- <1024px:列表视图。

## 7. 不变量回链
§4 媒资按 `hash` 去重、引用拦截删除、30 天物理清理(与 discover-china 软删策略对齐)。
