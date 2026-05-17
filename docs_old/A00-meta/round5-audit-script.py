#!/usr/bin/env python3
"""Per-file audit of /docs and /prompt across 11 dimensions.

Output:
  - /tmp/audit-per-file.tsv : one row per .md file with ✓/✗ per dimension
  - /tmp/audit-issues.txt   : aggregated issue list (file:line:dim:detail)
  - stdout summary

Dimensions:
  D1  banned C-stage tokens (super_admin, content_admin, editor+, supabase, etc.)
  D2  broken markdown links (target file missing; tolerate D01-data/D02-api/D03-validation/system/_input/A00-meta)
  D3  TARGET-PATH header mismatch with actual path
  D4  H1 heading present (structural)
  D5  damaged token strings from previous over-substitution (鉴权与数据底座, /首版/, 首版.0)
  D6  stray mermaid code fence in C-stage files
  D7  legacy stage codes (B04-S, B05-, C02-I, C03-N, C04-H, C05-E, B03-X, C07-)
  D8  phasing wording (本期, 二期, v2+, MoSCoW, H5 封板, 路线图, P0/P1/P2)
  D9  unclosed inline code backticks per line (odd count of backticks)
  D10 broken table rows (| col count varies wildly within same table block)
  D11 trailing markup junk / control chars
"""
from __future__ import annotations
import os, re, sys
from collections import defaultdict

ROOTS = ["/opt/projects/zhiyu/docs", "/opt/projects/zhiyu/prompt"]
SKIP_DIRS = {"_input"}  # historical drafts — record but do not fail
# Files that legitimately discuss backend mechanics:
C02_PATH_PREFIX = "/opt/projects/zhiyu/docs/C02-permissions/"
A00_PATH_PREFIX = "/opt/projects/zhiyu/docs/A00-meta/"
INPUT_PATH_FRAG = "/_input/"
PROMPT_PATH_PREFIX = "/opt/projects/zhiyu/prompt/"

# -------- Dimension regexes --------
D1_BANNED = re.compile(
    r"\bsuper_admin\b|\bcontent_admin\b|\beditor\+|\beditor_only\b|\b"
    r"signInWithPassword\b|\bsignInWithOAuth\b|\bsignUp\(|\b"
    r"exchangeCodeForSession\b|\bresetPasswordForEmail\b|\b"
    r"user_sessions\b|\bsupabase\.[a-z]|\bSupabase\b|\bGoTrue\b|"
    r"\bcookieStorage\b|\bapp_metadata\b|profiles\.role"
)
D5_DAMAGED = re.compile(r"鉴权与数据底座|/首版/|首版\.[0-9]|Round\s*10\+")
D6_MERMAID = re.compile(r"```mermaid")
D7_LEGACY = re.compile(
    r"\bB04-S\b|\bB05-[A-Z]|\bC02-I\b|\bC03-N\b|\bC04-H\b|\bC05-E\b|"
    r"\bB03-X\b|\bC07-[A-Z]|\bC06-N\b"
)
D8_PHASE = re.compile(r"本期|二期|v2\+|MoSCoW|H5 封板|路线图|\bP0\b|\bP1\b|\bP2\b|11-roadmap\.md|12-changelog\.md")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")
TARGET_PATH_RE = re.compile(r"<!--\s*TARGET-PATH:\s*([^\s]+)\s*-->")
H1_RE = re.compile(r"^#\s+\S", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|")

# Tolerated link targets (D01/D02/D03/system/_input not yet built)
TOLERATED_LINK_PREFIXES = (
    "D01-data/", "D02-api/", "D03-validation/",
    "../D01-data/", "../D02-api/", "../D03-validation/",
    "../../D01-data/", "../../D02-api/", "../../D03-validation/",
    "../../../D01-data/", "../../../D02-api/", "../../../D03-validation/",
)

def is_url(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))

def gather_files() -> list[str]:
    files = []
    for root in ROOTS:
        for dp, dn, fn in os.walk(root):
            for f in fn:
                if f.endswith(".md"):
                    files.append(os.path.join(dp, f))
    return sorted(files)

def audit_file(path: str, all_paths: set[str]) -> tuple[dict[str, bool], list[str]]:
    """Return (dim_pass, issues). dim_pass: {dim: True/False}. issues: list of 'dim|line|detail'."""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    lines = raw.splitlines()
    issues: list[str] = []
    in_input = INPUT_PATH_FRAG in path
    is_c02 = path.startswith(C02_PATH_PREFIX)
    is_meta = path.startswith(A00_PATH_PREFIX)
    is_prompt = path.startswith(PROMPT_PATH_PREFIX)

    # D1: banned tokens forbidden ONLY in C-stage product docs.
    # B-stage architecture/design legitimately specs Supabase / SDK; C02 is the auth spec.
    is_c_stage = "/docs/C01-" in path or "/docs/C03-" in path or "/docs/C04-" in path or "/docs/C06-" in path
    if is_c_stage and not (is_c02 or is_meta or in_input or is_prompt):
        for i, ln in enumerate(lines, 1):
            for m in D1_BANNED.finditer(ln):
                issues.append(f"D1|{i}|banned token: {m.group(0)!r}")

    # D5: damaged token from over-substitution (everywhere except _input, meta)
    if not (in_input or is_meta):
        for i, ln in enumerate(lines, 1):
            for m in D5_DAMAGED.finditer(ln):
                issues.append(f"D5|{i}|damaged: {m.group(0)!r}")

    # D6: mermaid in C-stage (allowed in prompt + _input + meta + D-stage)
    if not (in_input or is_meta or is_prompt) and "/docs/C0" in path:
        for i, ln in enumerate(lines, 1):
            if D6_MERMAID.search(ln):
                issues.append(f"D6|{i}|stray mermaid block")

    # D7: legacy stage codes (skip prompt + _input + meta + changelog which records history)
    if not (in_input or is_meta or is_prompt or path.endswith("/changelog.md")):
        for i, ln in enumerate(lines, 1):
            for m in D7_LEGACY.finditer(ln):
                issues.append(f"D7|{i}|legacy stage code: {m.group(0)!r}")

    # D8: phasing forbidden ONLY in C-stage product docs (PRD/IA/pages must be version-less).
    # B-stage tech-stack & prompt templates legitimately discuss 本期/二期 for tech adoption order.
    if is_c_stage and not (in_input or is_meta or is_prompt):
        for i, ln in enumerate(lines, 1):
            for m in D8_PHASE.finditer(ln):
                # tolerate "不出现 P0 / P1 ..." style meta-statements
                if ("不出现" in ln and "P0" in ln) or ("永不" in ln and "MoSCoW" in ln):
                    continue
                # tolerate D-prompt phrases like "本表" (本)— D8 only flags exact phasing
                tok = m.group(0)
                if tok in ("本期", "二期", "v2+", "MoSCoW", "H5 封板", "路线图"):
                    issues.append(f"D8|{i}|phasing: {tok!r}")
                elif tok in ("P0", "P1", "P2") and is_prompt:
                    # prompt may discuss these in meta context — allow only if line has 不出现 / 永不 / 禁止
                    continue
                elif tok in ("P0", "P1", "P2"):
                    issues.append(f"D8|{i}|phasing: {tok!r}")
                elif tok in ("11-roadmap.md", "12-changelog.md"):
                    issues.append(f"D8|{i}|stale ref: {tok!r}")

    # D2: broken links (skip historical/draft files: _input + A00 meta audits + prompt templates)
    base_dir = os.path.dirname(path)
    if in_input or is_meta or is_prompt:
        pass  # D2 skipped for historical/template content
    else:
        for i, ln in enumerate(lines, 1):
            for m in LINK_RE.finditer(ln):
                tgt = m.group(2).split("#", 1)[0]
                if not tgt or is_url(tgt):
                    continue
                if tgt.startswith("/"):
                    continue
                if any(tgt.startswith(p) or ("/" + p) in tgt for p in TOLERATED_LINK_PREFIXES):
                    continue
                if "system/" in tgt:
                    continue
                resolved = os.path.normpath(os.path.join(base_dir, tgt))
                if not os.path.exists(resolved):
                    issues.append(f"D2|{i}|missing link target: {tgt!r}")

    # D3: TARGET-PATH header (skip prompt — templates contain literal placeholder)
    if not is_prompt:
        m = TARGET_PATH_RE.search(raw[:500])
        if m:
            declared = m.group(1)
            actual = os.path.relpath(path, "/opt/projects/zhiyu")
            if declared != actual:
                issues.append(f"D3|1|TARGET-PATH mismatch: declared={declared!r} actual={actual!r}")

    # D4: H1 present
    if not H1_RE.search(raw):
        issues.append("D4|1|no H1 heading")

    # D9: odd inline backticks per line (excluding fenced code blocks)
    in_fence = False
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # count triple-backticks not present here (already filtered); count single
        # Skip lines that are pure separators or tables
        bt = ln.count("`")
        if bt % 2 != 0:
            issues.append(f"D9|{i}|odd backtick count ({bt}): {ln.strip()[:80]!r}")

    # D10: table column drift within a contiguous table block (skip fenced code blocks)
    block: list[tuple[int, int]] = []  # (line_no, col_count)
    def flush_block(blk):
        if len(blk) < 2: return
        counts = {c for _, c in blk}
        if len(counts) > 1 and max(counts) - min(counts) > 1:
            issues.append(f"D10|{blk[0][0]}|table column drift {sorted(counts)} over rows {blk[0][0]}..{blk[-1][0]}")
    in_fence_t = False
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("```"):
            in_fence_t = not in_fence_t
            flush_block(block); block = []
            continue
        if in_fence_t:
            continue
        if TABLE_ROW_RE.match(ln):
            stripped = re.sub(r"`[^`]*`", "", ln).replace(r"\|", "")
            cols = stripped.count("|") - 1
            block.append((i, cols))
        else:
            flush_block(block)
            block = []
    flush_block(block)

    # D11: control chars / NUL / weird trailing
    for i, ln in enumerate(lines, 1):
        if any(ord(c) < 9 or ord(c) == 11 or ord(c) == 12 for c in ln):
            issues.append(f"D11|{i}|control char")

    # Pass map
    dims = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11"]
    pass_map = {d: True for d in dims}
    for it in issues:
        d = it.split("|", 1)[0]
        pass_map[d] = False
    return pass_map, issues


def main():
    files = gather_files()
    all_paths = {p: True for p in files}
    per_file_lines = []
    all_issues = []
    dim_fail_counts = defaultdict(int)
    perfect = 0
    for p in files:
        pmap, issues = audit_file(p, all_paths)
        rel = os.path.relpath(p, "/opt/projects/zhiyu")
        flags = "".join("✓" if pmap[d] else "✗" for d in ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11"])
        per_file_lines.append(f"{flags}\t{rel}")
        for it in issues:
            d = it.split("|", 1)[0]
            dim_fail_counts[d] += 1
            all_issues.append(f"{rel}\t{it}")
        if not issues:
            perfect += 1

    with open("/tmp/audit-per-file.tsv", "w") as f:
        f.write("D1D2D3D4D5D6D7D8D9D10D11\tpath\n")
        f.write("\n".join(per_file_lines) + "\n")
    with open("/tmp/audit-issues.txt", "w") as f:
        f.write("\n".join(all_issues) + "\n")

    print(f"Audited files : {len(files)}")
    print(f"Perfect (all 11 dims ✓) : {perfect}")
    print(f"With issues : {len(files) - perfect}")
    print(f"Total issues : {len(all_issues)}")
    print(f"By dimension:")
    for d in ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11"]:
        print(f"  {d}: {dim_fail_counts[d]}")


if __name__ == "__main__":
    main()
