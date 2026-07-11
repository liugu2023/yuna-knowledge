#!/usr/bin/env python3
"""Insert author cards after YAML frontmatter for articles with authors."""
# uv run --with pyyaml add_author_cards.py [--update]

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
AUTHORS_FILE = ROOT / "authors.yml"
MARKER_PREFIX = "**本文作者：**"
OLD_MARKER_PREFIX = "**作者**："


def load_authors(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def split_frontmatter(content: str) -> tuple[str | None, str | None]:
    if not content.startswith("---"):
        return None, None
    end = content.find("\n---", 3)
    if end == -1:
        return None, None
    return content[3:end], content[end + 4:]


def replace_xhx_in_authors(frontmatter_text: str) -> str:
    lines = frontmatter_text.split("\n")
    result = []
    in_authors = False
    for line in lines:
        if re.match(r"^authors:\s*$", line):
            in_authors = True
            result.append(line)
        elif in_authors:
            if line.startswith("  -") or line.startswith("- "):
                result.append(line.replace("xhx", "HaoxiangXia"))
            else:
                in_authors = False
                result.append(line)
        else:
            result.append(line)
    return "\n".join(result)


def extract_author_ids(frontmatter_text: str) -> list[str] | None:
    try:
        doc = yaml.safe_load(frontmatter_text)
    except Exception:
        return None
    if not isinstance(doc, dict):
        return None
    authors = doc.get("authors")
    if isinstance(authors, str):
        return [authors]
    if isinstance(authors, list):
        return [str(a) for a in authors if a is not None]
    return None


def build_card(author_ids: list[str], authors: dict) -> str:
    lines = [MARKER_PREFIX]
    for aid in author_ids:
        info = authors.get(aid) or {"github": aid, "display": aid}
        github = info.get("github", aid)
        display = info.get("display", github)
        lines.append(
            f"- ![{display}](https://avatars.githubusercontent.com/{github}?s=40)"
            f"@[{display}](https://github.com/{github})"
        )
    return "\n".join(lines)


def already_has_card(text: str) -> bool:
    return (
        re.search(rf"^\s*{re.escape(MARKER_PREFIX)}", text, re.MULTILINE) is not None
        or re.search(rf"^\s*{re.escape(OLD_MARKER_PREFIX)}", text, re.MULTILINE) is not None
    )


def remove_card(text: str) -> str:
    """Remove old and new author card blocks without touching other '---' separators."""
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(MARKER_PREFIX):
            # Skip marker and bullet lines
            i += 1
            while i < len(lines) and lines[i].startswith("- "):
                i += 1
            # Skip trailing blank lines and the single '---' separator after the card
            skipped_separator = False
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped == "":
                    i += 1
                elif stripped == "---" and not skipped_separator:
                    skipped_separator = True
                    i += 1
                else:
                    break
            continue
        elif line.startswith(OLD_MARKER_PREFIX):
            # Old format: remove the line and the nearest preceding '---' separator
            while result and result[-1].strip() == "":
                result.pop()
            if result and result[-1].strip() == "---":
                result.pop()
                while result and result[-1].strip() == "":
                    result.pop()
            i += 1
            continue
        result.append(line)
        i += 1
    return "\n".join(result)


def insert_card(md_path: Path, card: str, update: bool = False) -> bool:
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter_text, body = split_frontmatter(content)
    if frontmatter_text is None:
        return False

    author_ids = extract_author_ids(frontmatter_text)
    if author_ids is None:
        return False

    new_frontmatter_text = replace_xhx_in_authors(frontmatter_text)
    new_author_ids = [aid if aid != "xhx" else "HaoxiangXia" for aid in author_ids]

    if already_has_card(body):
        if not update:
            print(f"  SKIP (already has author card): {md_path}")
            return False
        body = remove_card(body)
        print(f"  REPLACE (existing author card): {md_path}")

    body_lines = body.split("\n")

    # Strip leading blank lines so the card is inserted right after frontmatter
    while body_lines and body_lines[0].strip() == "":
        body_lines.pop(0)

    heading_idx = -1
    for i, line in enumerate(body_lines):
        if line.startswith("# "):
            heading_idx = i
            break

    if heading_idx == -1:
        new_body = "\n" + card + "\n"
    else:
        before = body_lines[:heading_idx]
        after = body_lines[heading_idx:]
        new_body = "\n".join(before) + "\n\n" + card + "\n\n---\n\n" + "\n".join(after)

    new_content = f"---{new_frontmatter_text}\n---{new_body}"
    new_content = new_content.rstrip() + "\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  UPDATED: {md_path}")
    return True


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Insert or regenerate author cards after frontmatter.")
    parser.add_argument("--update", action="store_true", help="Replace existing author cards")
    args = parser.parse_args()

    authors = load_authors(AUTHORS_FILE)
    print(f"Loaded {len(authors)} author entries from {AUTHORS_FILE}")

    updated = 0
    skipped = 0
    errored = 0

    for md_path in sorted(ROOT.rglob("*.md")):
        frontmatter_text, _ = split_frontmatter(md_path.read_text(encoding="utf-8"))
        if frontmatter_text is None:
            continue
        author_ids = extract_author_ids(frontmatter_text)
        if author_ids is None:
            continue

        new_author_ids = [aid if aid != "xhx" else "HaoxiangXia" for aid in author_ids]
        print(f"Processing {md_path} (authors: {new_author_ids})")
        card = build_card(new_author_ids, authors)
        try:
            if insert_card(md_path, card, update=args.update):
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR updating {md_path}: {e}")
            errored += 1

    print(f"\nDone: {updated} updated, {skipped} skipped, {errored} errored")
    return 1 if errored else 0


if __name__ == "__main__":
    sys.exit(main())
