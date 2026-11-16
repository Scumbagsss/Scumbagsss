"""Offline checks for the public GitHub portfolio.

Only validates local Markdown references and SVG syntax. No network access,
credentials, private repositories or external-link probing is required.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

DOCS = ("README.md", "PORTFOLIO.md", "REVIEWERS.md",
        "VISUAL_SHOWCASE.md", "MODULE_CATALOG.md")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_ATTR = re.compile(r"""\b(?:src|href)\s*=\s*["']([^"']+)["']""")
CODE_FENCE = re.compile(r"(?ms)^\x60{3}.*?^\x60{3}\s*$")


def relative_targets(text: str):
    """Yield local targets; ignore remote URLs, fragments and examples in code."""
    cleaned = CODE_FENCE.sub("", text)
    for raw in MARKDOWN_LINK.findall(cleaned) + HTML_ATTR.findall(cleaned):
        value = raw.strip()
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value.startswith("#") or not parsed.path:
            continue
        yield unquote(parsed.path)


def validate_links(root: Path, paths=DOCS) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for filename in paths:
        doc = root / filename
        if not doc.is_file():
            errors.append(f"Missing document: {filename}")
            continue
        for ref in relative_targets(doc.read_text(encoding="utf-8")):
            candidate = (doc.parent / ref).resolve()
            if not candidate.is_relative_to(root):
                errors.append(f"{filename}: path escapes repository: {ref}")
            elif not candidate.exists():
                errors.append(f"{filename}: broken local reference: {ref}")
    return errors


def validate_svg(root: Path) -> list[str]:
    errors: list[str] = []
    for path in (root / "assets").glob("*.svg"):
        try:
            svg = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{path.name}: invalid XML: {exc}")
            continue
        if svg.tag.rsplit("}", 1)[-1] != "svg":
            errors.append(f"{path.name}: root element is not SVG")
        for item in svg.iter():
            if item.tag.rsplit("}", 1)[-1] in {"script", "foreignObject"}:
                errors.append(f"{path.name}: embedded active content is not permitted")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = validate_links(root) + validate_svg(root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Portfolio OK: {len(DOCS)} docs checked; local references and SVGs valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
