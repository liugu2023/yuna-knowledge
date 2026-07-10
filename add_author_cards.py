#!/usr/bin/env python3
"""Append author cards to articles with authors frontmatter."""
# uv run --with pyyaml add_author_cards.py  

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
AUTHORS_FILE = ROOT / "authors.yml"
MARKER_PREFIX = "**作者**："


def load_authors(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def extract_authors(md_path: Path) -> list[str] | None:
    """Return the authors list from YAML frontmatter, or None if absent."""
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_text = text[3:end]
    try:
        doc = yaml.safe_load(fm_text)
    except Exception as e:
        print(f"  YAML parse error: {md_path}: {e}")
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
    parts = []
    for aid in author_ids:
        info = authors.get(aid) or {"github": aid, "display": aid}
        github = info.get("github", aid)
        display = info.get("display", github)
        parts.append(
            f"[{display}](https://github.com/{github}) "
            f"![{display}](https://avatars.githubusercontent.com/{github}?s=40)"
        )
    return f"{MARKER_PREFIX}{' · '.join(parts)}"


def already_has_card(text: str) -> bool:
    return re.search(rf"^\s*{re.escape(MARKER_PREFIX)}", text, re.MULTILINE) is not None


def remove_card(text: str) -> str:
    """Remove all generated author card marker lines and the separator line that
    preceded the last card. Frontmatter and other '---' separators are left alone."""
    trailing_match = re.search(r"\s*$", text)
    trailing = text[trailing_match.start():] if trailing_match else ""
    body = text[:trailing_match.start()]
    # Remove all generated author card lines.
    body = re.sub(r"^\*\*作者\*\*：.*$", "", body, flags=re.MULTILINE)
    # Remove the now-orphaned '---' separator that was right before the card.
    # This regex is not MULTILINE, so it only matches the '---' at the end of body.
    body = re.sub(r"\n?---\s*$", "", body, count=1)
    return body + trailing


def append_card(md_path: Path, card: str, update: bool = False) -> bool:
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    if already_has_card(text):
        if not update:
            print(f"  SKIP (already has author card): {md_path}")
            return False
        text = remove_card(text)
        print(f"  REPLACE (existing author card): {md_path}")

    trailing_match = re.search(r"\s*$", text)
    trailing = text[trailing_match.start():] if trailing_match else ""
    body = text[:trailing_match.start()]

    if not body.endswith("\n"):
        separator = "\n\n---\n\n"
    elif body.endswith("\n\n"):
        separator = "---\n\n"
    else:  # exactly one trailing newline
        separator = "\n---\n\n"

    # Ensure the card line is separated from any preserved trailing whitespace.
    if trailing and not trailing.startswith("\n"):
        trailing = "\n" + trailing

    new_text = f"{body}{separator}{card}{trailing}"
    # Normalize trailing whitespace to a single newline.
    new_text = new_text.rstrip() + "\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    if not update:
        print(f"  UPDATED: {md_path}")
    return True


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Append or regenerate author cards.")
    parser.add_argument("--update", action="store_true", help="Replace existing author cards")
    args = parser.parse_args()

    authors = load_authors(AUTHORS_FILE)
    print(f"Loaded {len(authors)} author entries from {AUTHORS_FILE}")

    updated = 0
    skipped = 0
    errored = 0

    for md_path in sorted(ROOT.rglob("*.md")):
        if md_path.name == "TODO.md":
            # This file is a project TODO, not an article; skip if desired.
            # Keeping it included because it has authors frontmatter.
            pass
        author_ids = extract_authors(md_path)
        if author_ids is None:
            continue

        print(f"Processing {md_path} (authors: {author_ids})")
        card = build_card(author_ids, authors)
        try:
            if append_card(md_path, card, update=args.update):
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
