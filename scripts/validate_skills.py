#!/usr/bin/env python3
"""Check every skill in skills/ against the CONVENTIONS.md authoring contract.

Usage:
    python scripts/validate_skills.py [--quiet] [skill-name ...]

Exit code 0 if every skill passes, 1 otherwise. The checks here are the
mechanical subset of the CONVENTIONS.md section 10 checklist -- the ones a
script can honestly verify. Judgement calls (is the do-not-invent list really
domain-specific? do the options sharpen turn over turn?) still need a human.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"

BLOCKS = [
    "## Context Block",
    "## Instruction Block",
    "## Parameter Block",
    "## Output Block",
    "## Validation Block",
    "## Final Step",
    "## Examples",
    "## Provenance",
]

INSTRUCTION_SUBHEADS = ["### Required Context Keys", "### Missing Context Rule"]

VALIDATION_SUBHEADS = [
    "### Quality gates",
    "### Do not invent",
    "### Common pitfalls",
    "### Assumptions to Validate",
]

HIDDEN_CURRICULUM_HEADS = [
    "## Hidden Curriculum",
    "## Interaction Mode",
    "## Attribution",
]

MODES = ["Facilitation", "Checkpointed co-construction", "Autonomous investigation"]

FINAL_STEP_REPLY = "Reply with `1`, `2`, `3`, `4`"

DESC_MIN, DESC_MAX = 120, 1100


class Result:
    def __init__(self, name: str) -> None:
        self.name = name
        self.errors: list[str] = []
        self.warnings: list[str] = []

    @property
    def ok(self) -> bool:
        return not self.errors

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def split_frontmatter(text: str) -> tuple[str, str] | tuple[None, None]:
    if not text.startswith("---\n"):
        return None, None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None, None
    return text[4:end], text[end + 5 :]


def parse_description(fm: str) -> str | None:
    m = re.search(r"^description:\s*(.*)$", fm, re.M)
    if not m:
        return None
    first = m.group(1).strip()
    if first in (">-", ">", "|", "|-"):
        lines = []
        started = False
        for line in fm.splitlines():
            if re.match(r"^description:", line):
                started = True
                continue
            if started:
                if line.startswith((" ", "\t")):
                    lines.append(line.strip())
                else:
                    break
        return " ".join(lines)
    return first.strip("\"'")


def check_final_step(body: str, r: Result) -> None:
    m = re.search(r"^## Final Step\s*$", body, re.M)
    if not m:
        return
    rest = body[m.end() :]
    nxt = re.search(r"^## ", rest, re.M)
    section = rest[: nxt.start()] if nxt else rest

    opts = re.findall(r"^(\d)\. \S", section, re.M)
    if len(opts) != 4:
        r.err(f"Final Step has {len(opts)} numbered options, expected exactly 4")
    elif opts != ["1", "2", "3", "4"]:
        r.err(f"Final Step options are numbered {''.join(opts)}, expected 1234")

    if opts and "(Recommended)" not in section.split("\n2.")[0]:
        r.err("Final Step option 1 is not marked (Recommended)")

    if FINAL_STEP_REPLY not in section:
        r.err("Final Step is missing the standard 'Reply with `1`, `2`, `3`, `4`' close")


def check_skill_md(path: Path, r: Result) -> None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    if fm is None:
        r.err("no YAML frontmatter delimited by ---")
        return

    if not re.search(r"^name:\s*\S", fm, re.M):
        r.err("frontmatter has no `name:`")
    else:
        declared = re.search(r"^name:\s*(\S+)", fm, re.M).group(1).strip("\"'")
        if declared != path.parent.name:
            r.err(f"frontmatter name '{declared}' != directory '{path.parent.name}'")

    desc = parse_description(fm)
    if not desc:
        r.err("frontmatter has no `description:`")
    elif not (DESC_MIN <= len(desc) <= DESC_MAX):
        r.err(f"description is {len(desc)} chars, expected {DESC_MIN}-{DESC_MAX}")

    comment = re.search(r"<!--(.*?)-->", body, re.S)
    if not comment:
        r.err("no hidden-curriculum HTML comment after the frontmatter")
    else:
        block = comment.group(1)
        for head in HIDDEN_CURRICULUM_HEADS:
            if head not in block:
                r.err(f"hidden-curriculum comment is missing '{head}'")
        found = [m for m in MODES if m in block]
        if not found:
            r.err("hidden-curriculum comment declares no recognised interaction mode")
        elif len(found) > 1 and "Primary:" not in block:
            r.err(f"multiple interaction modes named ({', '.join(found)}) with no Primary:")

    pos = -1
    for head in BLOCKS:
        m = re.search(rf"^{re.escape(head)}\s*$", body, re.M)
        if not m:
            r.err(f"missing block heading '{head}'")
            continue
        if m.start() < pos:
            r.err(f"block '{head}' is out of order")
        pos = m.start()

    # Subheadings may carry a trailing qualifier -- "### Quality gates per box"
    # is still a Quality gates section. The stem is what the contract requires.
    for head in INSTRUCTION_SUBHEADS + VALIDATION_SUBHEADS:
        if not re.search(rf"^{re.escape(head)}\b.*$", body, re.M):
            r.err(f"missing subheading '{head}'")

    check_final_step(body, r)

    if "template.md" not in body:
        r.err("Output Block never points at template.md")

    nonascii = {c for c in text if ord(c) > 127}
    if nonascii:
        allowed = set("—–’“”éçãõáíúóâêôà →·≤≥×°™®©±…½£€¥")
        bad = nonascii - allowed
        if bad:
            r.warn("non-ASCII characters: " + " ".join(sorted(bad))[:80])

    emoji = [c for c in text if 0x1F300 <= ord(c) <= 0x1FAFF or 0x2700 <= ord(c) <= 0x27BF]
    if emoji:
        r.err(f"contains emoji: {''.join(sorted(set(emoji)))}")

    n = len(text.splitlines())
    if n < 120:
        r.warn(f"SKILL.md is only {n} lines -- likely not rebuilt to the Five-Block architecture")
    if n > 320:
        r.warn(f"SKILL.md is {n} lines -- consider moving detail into template.md")


def check_template_md(path: Path, r: Result) -> None:
    if not path.exists():
        r.err("template.md is missing")
        return
    text = path.read_text(encoding="utf-8")
    if len(text.splitlines()) < 40:
        r.err("template.md is under 40 lines -- not a real output contract")
    if "```" not in text:
        r.err("template.md has no fenced schema block")
    if not re.search(r"^#+ *Provenance", text, re.M):
        r.err("template.md has no Provenance section")
    if "Assumptions to Validate" not in text:
        r.warn("template.md never mentions Assumptions to Validate")


def check_examples(d: Path, r: Result) -> None:
    ex = d / "examples"
    if not ex.is_dir():
        r.err("examples/ directory is missing")
        return
    files = sorted(p for p in ex.glob("*.md"))
    if not files:
        r.err("examples/ contains no .md file")
        return
    for f in files:
        text = f.read_text(encoding="utf-8")
        if len(text.splitlines()) < 60:
            r.warn(f"{f.name} is under 60 lines -- thin for a worked example")
        low = text.lower()
        if not any(k in low for k in ("question", "you:", "user:", "asked", "reply", "answer")):
            r.warn(f"{f.name} shows the artifact but maybe not the conversation")


def check_skill(d: Path) -> Result:
    r = Result(d.name)
    skill = d / "SKILL.md"
    if not skill.exists():
        r.err("SKILL.md is missing")
        return r
    check_skill_md(skill, r)
    check_template_md(d / "template.md", r)
    check_examples(d, r)
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("names", nargs="*", help="only check these skills")
    ap.add_argument("--quiet", action="store_true", help="hide warnings")
    args = ap.parse_args()

    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if args.names:
        dirs = [p for p in dirs if p.name in args.names]
        missing = set(args.names) - {p.name for p in dirs}
        for m in sorted(missing):
            print(f"  {m:<28} NOT FOUND")
        if missing:
            return 1

    results = [check_skill(d) for d in dirs]
    width = max((len(r.name) for r in results), default=20) + 2

    print()
    for r in results:
        status = "OK" if r.ok else "FAIL"
        print(f"  {r.name:<{width}} {status}")
        for e in r.errors:
            print(f"    - {e}")
        if not args.quiet:
            for w in r.warnings:
                print(f"    ~ {w}")
    passed = sum(1 for r in results if r.ok)
    failed = len(results) - passed
    print(f"\n  {passed} passed, {failed} failed\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
