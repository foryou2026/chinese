# UI 文案国际化规范

> **阶段**：B01-A 技术架构
> **冻结状态**：已冻结

---

## 适用范围

按钮、导航、空状态、错误提示、表单 label、页面标题等由产品界面固定提供的文案。

## Key 命名约定

| 规则 | 说明 |
|------|------|
| 格式 | 小写 snake_case：`forgot_password` |
| 组织 | 按业务域分组：`auth`、`nav`、`china`、`course` |
| 通用动作 | 放 `common`：`save`、`cancel`、`loading` |
| 稳定性 | 语义稳定优先，不把展示位置写死到 key |
| 禁止 | `text1`、`button2`、`new_label` 等无法维护的 key |
| 重命名 | 不因改英文文案而重命名 key——key 是 API，不是显示文案 |

## 文案文件结构

```typescript
// packages/shared-i18n/src/en.ts（源文案）
export default {
  common: {
    save: 'Save',
    cancel: 'Cancel',
    loading: 'Loading…',
  },
  auth: {
    login: 'Sign In',
    forgot: 'Forgot password?',
  },
  // 按功能域继续扩展
} as const;
```

```typescript
// packages/shared-i18n/src/index.ts
import en from './en';
import zh from './zh';
import vi from './vi';
import th from './th';
import id from './id';

export type ResourceShape = typeof en;
export const RESOURCES: Record<Locale, ResourceShape> = { en, zh, vi, th, id };
```

## 组件使用方式

```tsx
import { useTranslation } from 'react-i18next';

function SaveButton() {
  const { t } = useTranslation();
  return <button>{t('common.save')}</button>;
}
```

## Placeholder 规则

| 规则 | 说明 |
|------|------|
| 格式 | `{{name}}` |
| 一致性 | 所有语言必须使用完全相同的 placeholder 名称 |
| 校验 | `verify-i18n.ts` 自动检查一致性 |

正确：

```typescript
// en: delete_confirm: 'Delete {{name}}?'
// zh: delete_confirm: '删除 {{name}}？'
```

错误：

```typescript
// vi: delete_confirm: 'Xóa {{title}}?'  // placeholder 名不一致
```

> 需要复数或复杂格式时，先评估 `i18next` plural/context 方案再统一扩展，禁止临时拼字符串。

## 新增 UI 文案流程

1. `en.ts` 添加英文源文案
2. `zh.ts`, `vi.ts`, `th.ts`, `id.ts` 同步补齐同名 key
3. 组件使用 `t('path.to.key')`
4. 有变量用 `t('key', { name })`
5. 运行 `verify-i18n.ts` 校验
6. 巡检硬编码文案
7. 浏览器切换语言检查

> 禁止在 JSX 中硬编码可见文案。禁止只补中英文、其他语言"以后再说"——5 语言必须同次补齐。

## 校验脚本规范

`verify-i18n.ts` 必须检查：

| 检查项 | 说明 |
|--------|------|
| key 完整性 | 每个语言文件的 key 集合 = en 的 key 集合 |
| 值非空 | 每个 leaf value `trim()` 后不为空 |
| placeholder 一致 | 每个 value 的 `{{xxx}}` 集合 = en 对应 value 的集合 |

运行命令：`pnpm --filter @zhiyu/shared-i18n test`

## 硬编码巡检

```bash
# 中文硬编码
rg -n "[\p{Han}]" system/apps/*/src -g "*.tsx" -g "*.ts"

# 英文 UI 文案
rg -n ">[A-Z][^<{]*<|placeholder=|aria-label=|title=" system/apps/*/src -g "*.tsx"
```

**允许存在**：注释、测试 fixture、数据示例、API 字段名、URL、enum、`*_i18n` 渲染

**不允许存在**：按钮、导航、表单 label/placeholder/helper、空状态、错误提示、toast、`aria-label`、`title` 等 UI 文案

## 翻译质量要求

| 规则 | 说明 |
|------|------|
| 翻译方式 | 按含义翻译，非逐字直译 |
| 按钮文案 | 保持简短 |
| 标点 | 按各语言自然标点处理 |
| 品牌名 | 不翻译专有名词 |
| 不确定翻译 | 给出最合理翻译，在 PR 说明中标注疑问，不在代码中写 TODO |

---

## 99. 待确认问题

无
