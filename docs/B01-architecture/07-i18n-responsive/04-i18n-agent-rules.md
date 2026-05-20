# AI/Agent 国际化行为规则

> **阶段**：B01-A 技术架构
> **冻结状态**：已冻结

---

## 规则范围

以下规则适用于所有 AI agent 在修改含 UI 文案的代码时。

## glob 触发范围

- `packages/shared-i18n/src/**`
- `packages/shared-config/src/locales.ts`
- `apps/**/*.tsx`
- `apps/**/*.ts`

## 强制规则

| 规则 | 说明 |
|------|------|
| 源文案语言 | English (`en`)，先写英文再翻译 |
| 硬编码禁止 | React 用户可见文案必须使用 `t('key')` |
| 全语言同步 | 新 key 必须同步 5 种语言：`zh/en/vi/th/id` |
| placeholder 一致 | 所有语言 `{{xxx}}` 集合必须与 en 一致 |
| 校验 | 修改资源后运行 `pnpm --filter @zhiyu/shared-i18n test` |
| Locale 类型 | 统一从 `@zhiyu/shared-config` 引入，禁止手写 union |

## Agent 工作流

1. 确认当前支持语言来自 `packages/shared-config/src/locales.ts`
2. 搜索目标页面中已有 `useTranslation` 和 `t(...)` 用法
3. 新增文案先写 `en.ts`
4. 翻译并补齐 `zh.ts`、`vi.ts`、`th.ts`、`id.ts`
5. 替换 JSX 中的硬编码文案
6. 业务内容继续使用 `pickI18n`，不塞进 UI 文案包
7. 运行 `pnpm --filter @zhiyu/shared-i18n test`
8. 运行相关 typecheck
9. 用 `rg` 巡检硬编码
10. 浏览器切换所有语言做冒烟测试

## AI 翻译提示词模板

```
请为以下新增 i18n key 翻译 zh、vi、th、id。

要求：
- en 是源文案，只根据英文含义翻译
- 保持 TS 对象 key 完全一致
- 保持 {{placeholder}} 完全一致
- 按产品 UI 文案翻译，简短自然，不机器直译
- 按各语言自然标点处理
- 不改动未提到的 key
- 翻译不确定在回复中列出，不在代码写 TODO

新增英文：
...
```

## 浏览器 QA 路线

修改 UI 文案后启动 web-app，按此路线测试：

1. 首页 → 切换 zh/en/vi/th/id
2. 刷新确认 localStorage 保留语言选择
3. 导航、按钮、登录入口、空状态
4. auth 页面（登录/注册/忘记密码）
5. 内容页面（列表/详情/搜索）
6. 课程页面（地图/课时/练习/考试）
7. console 无运行时错误

---

## 99. 待确认问题

无
