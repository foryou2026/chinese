# 国际化与响应式

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack，用户 i18n 模板 `/template/i18n`
> **冻结状态**：✅ 已冻结

---

## 语言列表与默认

> 沿用用户已有 i18n 规范（来自 `/template/i18n`）。

| Locale | 语言 | 说明 |
|--------|------|------|
| `zh` | 中文 | 默认显示语言 |
| `en` | English | UI 源文案语言、fallback 语言 |
| `vi` | Tiếng Việt | 越南语 |
| `th` | ไทย | 泰语 |
| `id` | Bahasa Indonesia | 印尼语 |

| 项目 | 决定 |
|------|------|
| 源文案语言 | `en`（英文先写，再翻译其他语言） |
| 默认显示语言 | `zh`（浏览器无法匹配时的回退） |
| fallbackLng | `en` |
| 语言检测 | `localStorage` > `navigator.language` > 默认 `zh` |

## 文案组织方式

沿用 i18n 模板方案：

| 项目 | 决定 |
|------|------|
| 运行时库 | `i18next` + `react-i18next` |
| 资源格式 | TypeScript 模块（`en.ts`, `zh.ts` 等），非 JSON |
| 共享包 | `packages/shared-i18n`（资源） + `packages/shared-config`（locale 列表） |
| 类型约束 | `ResourceShape = typeof en`，其他语言结构必须与 en 一致 |
| Key 命名 | 按功能域分组，snake_case：`auth.forgot_password` |
| Placeholder | `{{name}}` 格式，所有语言必须一致 |
| 校验脚本 | `verify-i18n.ts`：检查 key 完整、值非空、placeholder 一致 |

### 两类 i18n 数据

| 类型 | 存储 | 读取方式 |
|------|------|---------|
| UI 文案（按钮、导航、提示） | `shared-i18n` TS 文件 | `t('key')` |
| 业务内容（文章标题、分类名） | 数据库 `*_i18n` JSONB 字段 | `pickI18n(map, lang)` |

> 两类不可混用。UI 文案不进数据库，业务内容不进 i18n 包。

### 新增文案流程

1. `en.ts` 添加英文源文案
2. `zh.ts`, `vi.ts`, `th.ts`, `id.ts` 同步补齐
3. 组件使用 `t('path.to.key')`
4. 运行 `verify-i18n.ts` 校验
5. 禁止在 JSX 中硬编码可见文案

## 时区策略

| 项目 | 决定 |
|------|------|
| 存储 | 数据库统一 UTC (`timestamptz`) |
| 传输 | API 统一 ISO 8601 UTC |
| 展示 | 前端按用户浏览器时区转换 |

## 货币与数字本地化

| 项目 | 决定 |
|------|------|
| 货币 | 使用 `Intl.NumberFormat` 按 locale 格式化 |
| 数字 | 使用 `Intl.NumberFormat` |
| 具体货币类型 | 由 Paddle 支付系统决定，前端按 Paddle 返回展示 |

## 日期格式

| 项目 | 决定 |
|------|------|
| 格式化库 | `Intl.DateTimeFormat`（原生，零依赖） |
| 相对时间 | `Intl.RelativeTimeFormat` |
| 显示格式 | 按用户 locale 自动适配 |

## 字体策略

| 项目 | 决定 |
|------|------|
| 中文 | 系统字体栈：`"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif` |
| 英文/拉丁 | `Inter` 或系统字体 |
| 东南亚语言 | 系统字体栈（各 OS 内置支持） |
| 加载方式 | 系统字体优先，Web 字体按需加载 |

## 断点与 Grid

> 三端必做，全宽自适应，禁止两侧留白。

| 断点名 | 宽度 | 目标设备 |
|--------|------|---------|
| `sm` | ≥ 640px | 大屏手机 |
| `md` | ≥ 768px | 平板竖屏 |
| `lg` | ≥ 1024px | 平板横屏/小笔记本 |
| `xl` | ≥ 1280px | 桌面 |
| `2xl` | ≥ 1536px | 大桌面 |

| 规则 | 说明 |
|------|------|
| 容器 | 不使用 `max-width` 固定容器，内容区域 100% 宽度 |
| 内边距 | 移动端 `px-4`，桌面 `px-6` ~ `px-8`，内容自适应 |
| Grid | Tailwind CSS Grid / Flexbox |
| 最小宽度 | 320px（最小移动端） |
| PC 宽屏 | 内容自然撑满，无两侧留白 |

## 移动端导航形式

| 设备 | 导航 |
|------|------|
| 移动端 | 底部 Tab Bar + 汉堡菜单 |
| 平板 | 可折叠侧栏 |
| 桌面 | 顶部导航栏 |

---

## 99. 待确认问题

无
