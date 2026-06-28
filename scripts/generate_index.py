#!/usr/bin/env python3
"""Generate the solved-problems index in README.md from solution files.

Scans every `<id>.md` solution file whose parent directory is a date
(YYYY-MM-DD), reads its frontmatter, and rewrites the table between the
`<!-- INDEX:START -->` and `<!-- INDEX:END -->` markers in README.md.

Run from anywhere:  python scripts/generate_index.py
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"

DATE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FIELD = re.compile(r'^(\w+):\s*"(.*)"\s*$')

DIFF_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2}


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Return the frontmatter fields of a solution file, or None if absent."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[3:end].splitlines():
        m = FIELD.match(line.strip())
        if m:
            fields[m.group(1)] = m.group(2)
    return fields


def collect() -> list[dict[str, str]]:
    """Walk the repo and collect one record per solved problem (latest solve)."""
    by_id: dict[str, dict[str, str]] = {}
    for path in REPO_ROOT.rglob("*.md"):
        if not DATE_DIR.match(path.parent.name):
            continue
        fm = parse_frontmatter(path)
        if not fm or not fm.get("question_id"):
            continue
        rec = {
            "id": fm["question_id"],
            "title": fm.get("title", "").replace("-", " "),
            "link": fm.get("question_link", ""),
            "difficulty": fm.get("difficulty", ""),
            "date": path.parent.name,
            "path": path.relative_to(REPO_ROOT).as_posix(),
        }
        prev = by_id.get(rec["id"])
        # Keep the most recent attempt if the same problem was solved twice.
        if prev is None or rec["date"] >= prev["date"]:
            by_id[rec["id"]] = rec
    return sorted(by_id.values(), key=lambda r: int(r["id"]))


def build_block(records: list[dict[str, str]]) -> str:
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for r in records:
        if r["difficulty"] in counts:
            counts[r["difficulty"]] += 1

    lines = [START, ""]
    lines.append(f"**{len(records)} problems documented** &nbsp;·&nbsp; "
                 f"{counts['Easy']} Easy &nbsp;·&nbsp; "
                 f"{counts['Medium']} Medium &nbsp;·&nbsp; "
                 f"{counts['Hard']} Hard")
    lines.append("")
    lines.append("| # | Problem | Difficulty | Date | Solution |")
    lines.append("|---|---------|------------|------|----------|")
    for r in records:
        title = f"[{r['title']}]({r['link']})" if r["link"] else r["title"]
        lines.append(
            f"| {r['id']} | {title} | {r['difficulty']} | {r['date']} | [code]({r['path']}) |"
        )
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main() -> None:
    records = collect()
    block = build_block(records)
    text = README.read_text(encoding="utf-8")

    if START in text and END in text:
        new = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            lambda _: block,
            text,
            flags=re.DOTALL,
        )
    else:
        new = text.rstrip() + "\n\n" + block + "\n"

    if new != text:
        README.write_text(new, encoding="utf-8")
        print(f"Updated README.md with {len(records)} problems.")
    else:
        print(f"README.md already up to date ({len(records)} problems).")


if __name__ == "__main__":
    main()
