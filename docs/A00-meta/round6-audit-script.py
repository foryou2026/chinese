#!/usr/bin/env python3
"""
Round-6 全量审计：在 R5 的 D1-D11 基础上新增 D12-D17。
- D12: 文件 ≤ 1200 行（prompt A00-03 §六）
- D13: M-ID 格式（每 feature 选定一种风格，不混用）
- D14: P-ID 多端必须含 surface 前缀（不得仅 P-<surface>-NNN）
- D15: HTML 文件基本合规（DOCTYPE / <html> / <head> / <body> / 标签闭合 / 无控制字符）
- D16: 字符编码 / 文件无 BOM / 末尾换行
- D17: index.md 是否覆盖同目录所有 .md（孤儿文件检测）
"""
from __future__ import annotations
import os, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/opt/projects/zhiyu')
DOCS = ROOT / 'docs'
PROMPT = ROOT / 'prompt'

# ====== R5 (D1-D11) 既有规则保留 ======
BANNED_D1 = [
    r'\bsuper_admin\b', r'\bcontent_admin\b', r'\beditor\+\b',
    r'\bsignInWithPassword\b', r'\bsignInWithOAuth\b',
    r'\bexchangeCodeForSession\b', r'\bresetPasswordForEmail\b',
    r'\bsignUp\(', r'\buser_sessions\b', r'\bprofiles\.role\b',
    r'\bapp_metadata\b', r'\bcookieStorage\b',
    r'supabase\.\w+\(', r'\bGoTrue\b',
    r'\bSupabase\b(?!\s*\(自托管\))',  # B 阶段允许
]
DAMAGED_D5 = [r'鉴权与数据底座', r'/首版/', r'首版\.0', r'Round\s*10\+']
LEGACY_D7 = [r'\bB04-S\b', r'\bB05-X\b', r'\bC02-I\b', r'\bC03-N\b',
             r'\bC04-H\b', r'\bC05-E\b', r'\bB03-X\b', r'\bC07-', r'\bC06-N\b']
PHASING_D8 = [r'本期', r'二期', r'\bv2\+', r'MoSCoW', r'H5\s*封板', r'路线图',
              r'\bP0\b', r'\bP1\b', r'\bP2\b', r'11-roadmap\.md', r'12-changelog\.md']

# ====== R6 新增 ======
MAX_LINES = 1200  # D12

# 不同 feature 允许的 M-ID 风格（既成事实）
# course: 语义化 M-course-<tag>
# auth/discover-china: 数字 M-<feature>-NNN（3 位）或带 surface 限定的 M-auth-<surface>-NN（已被 R6 允许）
# 真正违规：M-<feature>-N（1 位）/ M-<feature>-NN（2 位但非 surface 限定形式）

FEATURES_NUMERIC = {'auth', 'discover-china'}

def is_in_fenced(line_idx, lines):
    fence = False
    for i in range(line_idx):
        if lines[i].lstrip().startswith('```'):
            fence = not fence
    return fence

def strip_inline_code(s):
    return re.sub(r'`[^`\n]*`', '', s)

def list_md_files():
    files = []
    for base in [DOCS, PROMPT]:
        for p in base.rglob('*.md'):
            if '.git' in p.parts:
                continue
            files.append(p)
    return sorted(files)

def list_html_files():
    return sorted(DOCS.rglob('*.html'))

# ============ 各维度检查 ============

def check_d1(path, content):
    rel = str(path.relative_to(ROOT))
    # C 阶段禁用，B/C02/_input/A00-meta/prompt 豁免
    if any(seg in rel for seg in ['B01-', 'B02-', 'B03-', 'C02-', '_input/', 'A00-meta/', 'prompt/']):
        return []
    issues = []
    lines = content.splitlines()
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for pat in BANNED_D1:
            m = re.search(pat, line)
            if m:
                issues.append(f'L{i}: D1 banned `{m.group(0)}`')
    return issues

def resolve_link(path, target):
    if target.startswith(('http://', 'https://', 'mailto:', '#')):
        return None
    target = target.split('#')[0].strip()
    if not target:
        return None
    try:
        return (path.parent / target).resolve()
    except Exception:
        return None

def check_d2(path, content):
    rel = str(path.relative_to(ROOT))
    # 豁免：prompt 模板示例、A00-meta 历史
    if any(seg in rel for seg in ['prompt/', '_input/', 'A00-meta/']):
        return []
    issues = []
    lines = content.splitlines()
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for m in re.finditer(r'\[([^\]\n]+?)\]\(([^)\n]+?)\)', line):
            target = m.group(2)
            # 跳过 D01/D02/D03/system 目录（未生成）
            if any(t in target for t in ['D01-data', 'D02-api', 'D03-validation', 'system/']):
                continue
            if not target.endswith('.md') and '.md#' not in target:
                continue
            resolved = resolve_link(path, target)
            if resolved is None:
                continue
            if not resolved.exists():
                issues.append(f'L{i}: D2 broken link → {target}')
    return issues

def check_d3(path, content):
    rel = str(path.relative_to(ROOT))
    if 'prompt/' in rel or 'A00-meta/' in rel:
        return []
    m = re.search(r'<!--\s*TARGET-PATH:\s*(\S+?)\s*-->', content)
    if not m:
        return []
    declared = m.group(1).strip()
    actual = str(path.relative_to(ROOT))
    if declared != actual:
        return [f'L1: D3 TARGET-PATH `{declared}` != actual `{actual}`']
    return []

def check_d4(path, content):
    if not re.search(r'(?m)^#\s+\S', content):
        return ['L1: D4 missing H1']
    return []

def check_d5(path, content):
    rel = str(path.relative_to(ROOT))
    if any(seg in rel for seg in ['_input/', 'A00-meta/']):
        return []
    issues = []
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        for pat in DAMAGED_D5:
            if re.search(pat, line):
                issues.append(f'L{i}: D5 damaged token `{pat}`')
    return issues

def check_d6(path, content):
    rel = str(path.relative_to(ROOT))
    if not any(rel.startswith(f'docs/{s}') for s in ['C01-', 'C03-', 'C04-', 'C06-']):
        return []
    if any(seg in rel for seg in ['_input/', 'prompt/', 'A00-meta/']):
        return []
    issues = []
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*```\s*mermaid\b', line):
            issues.append(f'L{i}: D6 stray mermaid in C-stage')
    return issues

def check_d7(path, content):
    rel = str(path.relative_to(ROOT))
    if any(seg in rel for seg in ['_input/', 'A00-meta/', 'prompt/', 'changelog.md']):
        return []
    issues = []
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        for pat in LEGACY_D7:
            if re.search(pat, line):
                issues.append(f'L{i}: D7 legacy stage `{pat}`')
    return issues

def check_d8(path, content):
    rel = str(path.relative_to(ROOT))
    if any(seg in rel for seg in ['B01-', 'B02-', 'B03-', '_input/', 'prompt/', 'A00-meta/']):
        return []
    issues = []
    lines = content.splitlines()
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence; continue
        if fence: continue
        # 豁免禁令元陈述：以 不存在/不出现/禁止/不允许/不准 开头的句子
        norm = line.lstrip('- ').lstrip('* ').lstrip('> ').strip()
        if re.match(r'(不出现|不存在|禁止|不允许|不准|避免)', norm):
            continue
        for pat in PHASING_D8:
            if re.search(pat, line):
                issues.append(f'L{i}: D8 phasing `{pat}`')
    return issues

def check_d9(path, content):
    rel = str(path.relative_to(ROOT))
    if 'A00-meta/' in rel:
        return []
    issues = []
    lines = content.splitlines()
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence; continue
        if fence: continue
        # 排除 markdown 链接里的反引号
        cnt = line.count('`')
        if cnt % 2 != 0:
            issues.append(f'L{i}: D9 unmatched backtick (count={cnt})')
    return issues

def check_d10(path, content):
    issues = []
    lines = content.splitlines()
    fence = False
    prev_cols = None
    in_table = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            in_table = False; prev_cols = None
            continue
        if fence:
            continue
        stripped = strip_inline_code(line)
        if '|' in stripped and stripped.strip().startswith('|'):
            cols = stripped.count('|') - 1
            if prev_cols is None:
                prev_cols = cols
                in_table = True
            else:
                if abs(cols - prev_cols) > 1:
                    issues.append(f'L{i}: D10 col drift {cols} vs {prev_cols}')
        else:
            in_table = False
            prev_cols = None
    return issues

def check_d11(path, content):
    issues = []
    for i, line in enumerate(content.splitlines(), 1):
        for ch in line:
            if ord(ch) < 32 and ch not in '\t':
                issues.append(f'L{i}: D11 control char U+{ord(ch):04X}')
                break
    return issues

def check_d12(path, content):
    n = len(content.splitlines())
    if n > MAX_LINES:
        return [f'D12 file too long ({n} > {MAX_LINES})']
    return []

def check_d13(path, content):
    rel = str(path.relative_to(ROOT))
    if 'prompt/' in rel or 'A00-meta/' in rel or '_input/' in rel:
        return []
    issues = []
    # 不允许 M-<feat>-N（1 位）或 M-<feat>-NN 但非允许形式
    # 允许：M-course-<semantic tag>; M-auth-<surface>-NN; M-auth-NNN; M-discover-china-NNN
    for i, line in enumerate(content.splitlines(), 1):
        for m in re.finditer(r'\bM-([a-z][a-z0-9-]*?)-([a-z0-9-]+)\b', line):
            feat_token = m.group(1)
            suffix = m.group(2)
            full = m.group(0)
            # 不允许纯 1 位数字
            if re.fullmatch(r'[0-9]', suffix):
                issues.append(f'L{i}: D13 M-ID `{full}` numeric must be 3 digits')
            # discover-china / auth 数字风格须 3 位（除非中段是 surface）
            if feat_token == 'auth':
                # 允许 M-auth-NNN 或 M-auth-(app|admin|shared)-NN
                if re.fullmatch(r'[0-9]{1,2}', suffix):
                    issues.append(f'L{i}: D13 M-ID `{full}` should be M-auth-NNN (3 digits)')
    return issues

def check_d14(path, content):
    rel = str(path.relative_to(ROOT))
    if 'prompt/' in rel or 'A00-meta/' in rel or '_input/' in rel:
        return []
    issues = []
    # 多端 P-ID 必须 P-<surface>-<feature>-NNN，不得 P-<surface>-NNN（缺 feature）
    for i, line in enumerate(content.splitlines(), 1):
        for m in re.finditer(r'\bP-(app|admin|merchant)-([0-9]{3})\b', line):
            issues.append(f'L{i}: D14 P-ID `{m.group(0)}` missing <feature> (should be P-{m.group(1)}-<feature>-{m.group(2)})')
    return issues

def check_d15_html(path, content):
    issues = []
    if not re.search(r'<!DOCTYPE\s+html', content, re.I):
        issues.append('D15 missing <!DOCTYPE html>')
    if not re.search(r'<html\b', content, re.I):
        issues.append('D15 missing <html>')
    if not re.search(r'</html>\s*$', content, re.I):
        issues.append('D15 missing closing </html>')
    if not re.search(r'<head\b', content, re.I):
        issues.append('D15 missing <head>')
    if not re.search(r'<body\b', content, re.I):
        issues.append('D15 missing <body>')
    # 标签计数粗校验（自闭合标签排除）
    SELF = {'br','hr','img','input','meta','link','source','area','base','col','embed','param','track','wbr'}
    opens = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(?<!/)>', content)
    closes = re.findall(r'</([a-zA-Z][a-zA-Z0-9]*)\s*>', content)
    oc = defaultdict(int); cc = defaultdict(int)
    for t in opens:
        tl = t.lower()
        if tl in SELF: continue
        oc[tl] += 1
    for t in closes: cc[t.lower()] += 1
    for tag in set(oc) | set(cc):
        if oc[tag] != cc[tag]:
            issues.append(f'D15 tag <{tag}> unbalanced (open={oc[tag]} close={cc[tag]})')
    # 控制字符
    for i, line in enumerate(content.splitlines(), 1):
        for ch in line:
            if ord(ch) < 32 and ch not in '\t':
                issues.append(f'L{i}: D15 control char in HTML')
                break
    return issues

def check_d16(path, content_bytes):
    issues = []
    if content_bytes.startswith(b'\xef\xbb\xbf'):
        issues.append('D16 BOM present')
    if content_bytes and not content_bytes.endswith(b'\n'):
        issues.append('D16 missing trailing newline')
    return issues

def check_d17_orphan(all_md):
    """index.md 应链接到同目录所有兄弟 .md（仅检查 B01-/C02- 等有 00-index.md 的）"""
    issues_by_file = defaultdict(list)
    by_dir = defaultdict(list)
    for p in all_md:
        by_dir[p.parent].append(p)
    for d, files in by_dir.items():
        rel_d = str(d.relative_to(ROOT))
        if 'prompt' in rel_d or 'A00-meta' in rel_d or '_input' in rel_d:
            continue
        idx = d / '00-index.md'
        if not idx.exists():
            continue
        try:
            txt = idx.read_text(encoding='utf-8')
        except Exception:
            continue
        siblings = [f for f in files if f.name not in {'00-index.md', '99-open-questions.md', '_glossary.md', '_global-index.md'}]
        for s in siblings:
            if s.name not in txt:
                issues_by_file[idx].append(f'D17 index does not reference sibling `{s.name}`')
    return issues_by_file

# D18: 标题层级不得跳跃（H1→H3）
def check_d18(path, content):
    issues = []
    lines = content.splitlines()
    fence = False
    last_level = 0
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence; continue
        if fence: continue
        m = re.match(r'^(#+)\s+\S', line)
        if not m: continue
        lvl = len(m.group(1))
        if last_level and lvl - last_level > 1:
            issues.append(f'L{i}: D18 heading skip H{last_level}→H{lvl}')
        last_level = lvl
    return issues

# D19: markdown 表头分隔行格式
def check_d19(path, content):
    issues = []
    lines = content.splitlines()
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence; continue
        if fence: continue
        stripped = line.strip()
        if i < len(lines):
            nxt = lines[i].strip() if i < len(lines) else ''
        else:
            nxt = ''
        # 当前行像表头（| ... |）且下一行不是分隔行
        if (stripped.startswith('|') and stripped.endswith('|')
            and '|' in stripped[1:-1] and nxt.startswith('|')):
            # 检查是否为表头-分隔对
            if not re.fullmatch(r'\|[\s:|\-—]+\|', nxt):
                # 仅当下一行也是 | 起始但非分隔时检查上一行是不是分隔
                prev = lines[i-2].strip() if i >= 2 else ''
                if not re.fullmatch(r'\|[\s:|\-—]+\|', prev) and prev.startswith('|'):
                    pass  # 已是数据行，跳过
                elif not re.fullmatch(r'\|[\s:|\-—]+\|', prev):
                    # 当前是表头但下一行不是分隔且上一行不是分隔
                    pass
    return issues  # 暂留空，过于复杂

# D20: 交叉 P-ID 存在性（C04/C06 中引用的 P-ID 必须有对应文件）
def check_d20(path, content, all_files_set):
    rel = str(path.relative_to(ROOT))
    if 'A00-meta/' in rel or '_input/' in rel or 'prompt/' in rel:
        return []
    if not any(rel.startswith(p) for p in ['docs/C03-', 'docs/C04-', 'docs/C06-']):
        return []
    issues = []
    seen = set()
    # 仅 multi-surface 模式 P-<surface>-<feature>-NNN
    for m in re.finditer(r'\bP-(app|admin|merchant)-([a-z][a-z-]+?)-([0-9]{3})\b', content):
        pid = m.group(0)
        if pid in seen: continue
        seen.add(pid)
        surface, feat, seq = m.groups()
        expected = f'docs/C04-pages/{feat}/{surface}/{pid}.md'
        if expected not in all_files_set:
            # 行级豁免：明确标注「暂不支持/暂未/未实现/即将推出/待落地」
            line_idx = content[:m.start()].count('\n')
            line_txt = content.splitlines()[line_idx]
            if any(k in line_txt for k in ['暂不支持', '暂未', '未实现', '即将推出', '待落地', '不存在', 'feature 未落地']):
                continue
            issues.append(f'L{line_idx+1}: D20 P-ID `{pid}` referenced but `{expected}` missing')
    return issues

# D21/D22: HTML 元数据
def check_d21_22_html(path, content):
    issues = []
    if not re.search(r'<meta\s+charset\s*=\s*["\']?utf-8', content, re.I):
        issues.append('D21 missing <meta charset="utf-8">')
    if not re.search(r'<html\b[^>]*\blang\s*=', content, re.I):
        issues.append('D22 missing <html lang="...">')
    return issues


# ============ 主流程 ============

def main():
    md_files = list_md_files()
    html_files = list_html_files()

    dims_md = [('D1', check_d1), ('D2', check_d2), ('D3', check_d3), ('D4', check_d4),
               ('D5', check_d5), ('D6', check_d6), ('D7', check_d7), ('D8', check_d8),
               ('D9', check_d9), ('D10', check_d10), ('D11', check_d11),
               ('D12', check_d12), ('D13', check_d13), ('D14', check_d14),
               ('D18', check_d18)]
    all_md_set = {str(p.relative_to(ROOT)) for p in md_files}
    
    rows = []
    issue_count_by_dim = defaultdict(int)
    total_issues = 0
    perfect = 0
    
    # 预跑 D17
    d17_map = check_d17_orphan(md_files)
    
    for p in md_files:
        rel = str(p.relative_to(ROOT))
        try:
            content = p.read_text(encoding='utf-8')
            content_b = p.read_bytes()
        except Exception as e:
            rows.append((rel, '✗', [f'IO error: {e}']))
            total_issues += 1
            continue
        file_issues = []
        flags = []
        for name, fn in dims_md:
            iss = fn(p, content)
            if iss:
                flags.append('✗')
                file_issues.extend([f'[{name}] {x}' for x in iss])
                issue_count_by_dim[name] += len(iss)
            else:
                flags.append('✓')
        # D15: HTML, skip for md
        flags.append('—')  # D15 placeholder for md rows
        # D16
        iss16 = check_d16(p, content_b)
        if iss16:
            flags.append('✗')
            file_issues.extend([f'[D16] {x}' for x in iss16])
            issue_count_by_dim['D16'] += len(iss16)
        else:
            flags.append('✓')
        # D17
        iss17 = d17_map.get(p, [])
        if iss17:
            flags.append('✗')
            file_issues.extend([f'[D17] {x}' for x in iss17])
            issue_count_by_dim['D17'] += len(iss17)
        else:
            flags.append('✓')
        # D20
        iss20 = check_d20(p, content, all_md_set)
        if iss20:
            flags.append('✗')
            file_issues.extend([f'[D20] {x}' for x in iss20])
            issue_count_by_dim['D20'] += len(iss20)
        else:
            flags.append('✓')
        total_issues += len(file_issues)
        if not file_issues:
            perfect += 1
        rows.append((rel, ''.join(flags), file_issues))
    
    # HTML
    html_rows = []
    html_perfect = 0
    for p in html_files:
        rel = str(p.relative_to(ROOT))
        try:
            content = p.read_text(encoding='utf-8')
            content_b = p.read_bytes()
        except Exception as e:
            html_rows.append((rel, '✗', [f'IO error: {e}']))
            continue
        iss = check_d15_html(p, content)
        iss16 = check_d16(p, content_b)
        iss2122 = check_d21_22_html(p, content)
        all_iss = [f'[D15] {x}' for x in iss] + [f'[D16] {x}' for x in iss16] + [f'[D21/22] {x}' for x in iss2122]
        issue_count_by_dim['D15'] += len(iss)
        issue_count_by_dim['D16'] += len(iss16)
        issue_count_by_dim['D21/22'] += len(iss2122)
        total_issues += len(all_iss)
        if not all_iss:
            html_perfect += 1
        html_rows.append((rel, '✓' if not all_iss else '✗', all_iss))
    
    # 输出
    print(f'\n=== Round-6 Audit ===')
    print(f'MD files: {len(md_files)} | Perfect: {perfect} | With issues: {len(md_files) - perfect}')
    print(f'HTML files: {len(html_files)} | Perfect: {html_perfect} | With issues: {len(html_files) - html_perfect}')
    print(f'Total issues: {total_issues}')
    print(f'By dim: ' + '  '.join(f'{k}:{v}' for k,v in sorted(issue_count_by_dim.items())))
    
    # 详细问题
    print('\n=== Issues ===')
    for rel, flag, issues in rows:
        if issues:
            print(f'\n{rel}')
            for it in issues:
                print(f'  {it}')
    for rel, flag, issues in html_rows:
        if issues:
            print(f'\n{rel}')
            for it in issues:
                print(f'  {it}')
    
    # 写 TSV
    with open('/tmp/r6-per-file.tsv', 'w', encoding='utf-8') as f:
        f.write('file\tD1\tD2\tD3\tD4\tD5\tD6\tD7\tD8\tD9\tD10\tD11\tD12\tD13\tD14\tD15\tD16\tD17\tcount\n')
        for rel, flag, issues in rows:
            cells = list(flag) if len(flag) == 17 else (list(flag) + ['?']*(17-len(flag)))
            f.write(rel + '\t' + '\t'.join(cells) + f'\t{len(issues)}\n')
        for rel, flag, issues in html_rows:
            f.write(rel + '\t' + '\t'.join(['—']*14) + f'\t{flag}\t{"✓" if not any("D16" in i for i in issues) else "✗"}\t—\t{len(issues)}\n')
    
    return 0 if total_issues == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
