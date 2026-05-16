<!-- TARGET-PATH: docs/D02-api/discover-china/04-error-codes.md -->

# 04 · 错误码登记(china 域)

> 数值区段:`45000-45999`;字符串 code 注册到 `system/packages/shared-config/src/error-codes.ts` 的 `china` 命名空间;
> 每个码提供 5 语言文案,前端按 `Accept-Language` 取,兜底 `en → zh`。

## 校验类(45000-45099)

| 数值 | 字符串 code | HTTP | 触发 | 默认文案 |
|------|------------|------|------|---------|
| 45001 | `CHINA_CATEGORY_CODE_INVALID` | 400 | 类目编码格式不合法 | 类目编码格式不正确 |
| 45002 | `CHINA_CATEGORY_NAME_I18N_MISSING` | 400 | name_i18n 缺 5 语 | 请补全 5 种语言的类目名称 |
| 45003 | `CHINA_CATEGORY_NAME_TOO_LONG` | 400 | name 任一 > 40 | 类目名称最多 40 字 |
| 45004 | `CHINA_CATEGORY_DESC_I18N_MISSING` | 400 | description 缺 5 语 | 请补全 5 种语言的类目说明 |
| 45005 | `CHINA_CATEGORY_DESC_TOO_LONG` | 400 | description 任一 > 200 | 类目说明最多 200 字 |
| 45011 | `CHINA_ARTICLE_CATEGORY_REQUIRED` | 400 | 缺 category_id | 请选择文章类目 |
| 45012 | `CHINA_ARTICLE_CODE_INVALID` | 400 | 文章 code 格式不合法 | 文章编码不合法 |
| 45013 | `CHINA_ARTICLE_TITLE_PINYIN_LEN` | 400 | 拼音 0 或 > 200 | 文章标题拼音最多 200 字 |
| 45014 | `CHINA_ARTICLE_TITLE_I18N_MISSING` | 400 | 标题缺 5 语 | 请补全 5 种语言的文章标题 |
| 45015 | `CHINA_ARTICLE_TITLE_TOO_LONG` | 400 | 任一 > 40 | 文章标题最多 40 字 |
| 45021 | `CHINA_SENTENCE_PINYIN_LEN` | 400 | 拼音 0 或 > 600 | 句子拼音最多 600 字符 |
| 45022 | `CHINA_SENTENCE_CONTENT_ZH_LEN` | 400 | 0 或 > 400 | 中文句子最多 400 字 |
| 45023 | `CHINA_SENTENCE_CONTENT_EN_LEN` | 400 | 同 | 英文句子最多 400 字 |
| 45024 | `CHINA_SENTENCE_CONTENT_VI_LEN` | 400 | 同 | 越语句子最多 400 字 |
| 45025 | `CHINA_SENTENCE_CONTENT_TH_LEN` | 400 | 同 | 泰语句子最多 400 字 |
| 45026 | `CHINA_SENTENCE_CONTENT_ID_LEN` | 400 | 同 | 印尼语句子最多 400 字 |
| 45027 | `CHINA_SENTENCE_SEQ_RANGE` | 400 | seq_no 越界 | 句子序号超出范围 |
| 45028 | `CHINA_REORDER_IDS_MISMATCH` | 400 | A14 列表不匹配 | 重排列表与当前句子不匹配 |
| 45029 | `CHINA_SEARCH_QUERY_TOO_SHORT` | 400 | A15 q 为空 | 请输入搜索关键字 |
| 45030 | `CHINA_SEARCH_QUERY_TOO_LONG` | 400 | A15 q > 60 | 关键字过长,最多 60 字符 |

## 资源 / 状态类(45100-45199)

| 数值 | 字符串 code | HTTP | 触发 | 默认文案 |
|------|------------|------|------|---------|
| 45100 | `CHINA_CATEGORY_NOT_FOUND` | 404 | 类目不存在 | 类目不存在 |
| 45101 | `CHINA_ARTICLE_NOT_FOUND` | 404 | 文章不存在 / 未发布 / 已删 | 文章不存在 |
| 45102 | `CHINA_SENTENCE_NOT_FOUND` | 404 | 句子不存在 / 已删 | 句子不存在 |
| 45110 | `CHINA_ARTICLE_CATEGORY_NOT_FOUND` | 404 | A4 / A5 指定类目不存在 | 类目不存在 |
| 45120 | `CHINA_ARTICLE_STATUS_CONFLICT` | 409 | 发布 / 下架 / 删除时状态不符 | 文章状态不允许此操作 |
| 45121 | `CHINA_ARTICLE_CODE_DUPLICATE` | 409 | code 撞车(极小概率) | 文章编码冲突,请重试 |
| 45122 | `CHINA_SENTENCE_SEQ_DUPLICATE` | 409 | (article_id, seq_no) 唯一冲突 | 句子顺序冲突,请重试 |
| 45123 | `CHINA_SENTENCE_SEQ_OVERFLOW` | 409 | 句子数 > 9999 | 单篇文章句子数已达上限 |
| 45130 | `CHINA_ARTICLE_PUBLISH_NO_SENTENCES` | 422 | 发布时无句子 | 请至少添加一条句子后再发布 |
| 45131 | `CHINA_ARTICLE_PUBLISH_INCOMPLETE_TRANSLATION` | 422 | 任一句缺多语 / 拼音 | 句子翻译或拼音不完整 |

## 上游 / 系统类(45200-45299)

| 数值 | 字符串 code | HTTP | 触发 | 默认文案 |
|------|------------|------|------|---------|
| 45200 | `CHINA_TTS_UPSTREAM_FAILED` | 502 | TTS 上游 5xx / 网络失败 | 语音生成失败,请稍后重试 |
| 45201 | `CHINA_TTS_UPSTREAM_TIMEOUT` | 504 | TTS 上游超时(15s) | 语音生成超时,请稍后重试 |
| 45202 | `CHINA_TTS_RATE_LIMITED` | 429 | TTS 上游限流 / 本地节流 | 语音生成过于频繁,请稍后重试 |
| 45210 | `CHINA_ARTICLE_CODE_GEN_FAILED` | 500 | 重试 5 次仍冲突 | 系统繁忙,请稍后重试 |

## 通用 / 框架级(沿用 G1,不在 china 域单独登记)

40100 / 40300 / 40001 / 40002 / 40400 / 50000。

## 响应结构

```ts
{
  code: number | string,   // 数值 45xxx 或字符串 'CHINA_*'
  message: string,
  field?: string,          // 校验类指明出错字段
  meta?: Record<string, unknown>,
  request_id: string,      // 中间件注入
}
```
