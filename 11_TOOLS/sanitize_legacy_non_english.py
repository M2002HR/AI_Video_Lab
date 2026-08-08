#!/usr/bin/env python3
"""Remove residual legacy non-English script from tracked repository text.

This is a one-time migration safety net. High-value documents are translated/re-written
explicitly; this tool only ensures older residual prose cannot violate the English-only
repository contract.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
CYRILLIC = re.compile(r"[\u0400-\u04FF\u0500-\u052F]")
FORBIDDEN = re.compile(ARABIC.pattern + "|" + CYRILLIC.pattern)
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".csv", ".py", ".sh", ".ps1", ".ini", ".cfg"}
SKIP_PARTS = {".git", "git_previews", "__pycache__"}
NOTE = "Legacy non-English prose was replaced during the English-only repository migration."


def tracked_files() -> list[pathlib.Path]:
    raw = subprocess.check_output(["git", "ls-files", "-z"])
    return [pathlib.Path(p.decode("utf-8")) for p in raw.split(b"\0") if p]


def clean_json(value):
    if isinstance(value, str) and FORBIDDEN.search(value):
        return NOTE
    if isinstance(value, list):
        return [clean_json(v) for v in value]
    if isinstance(value, dict):
        return {k: clean_json(v) for k, v in value.items()}
    return value


def clean_text_line(line: str) -> str:
    if not FORBIDDEN.search(line):
        return line
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]
    prefix = ""
    if stripped.startswith("- "):
        prefix = "- "
    elif stripped.startswith("> "):
        prefix = "> "
    else:
        m = re.match(r"^(\d+\. )", stripped)
        if m:
            prefix = m.group(1)
        elif stripped.startswith("#"):
            prefix = stripped.split(" ", 1)[0] + " "
    return indent + prefix + NOTE


def main() -> int:
    changed = 0
    for path in tracked_files():
        if path.suffix.lower() not in TEXT_EXTENSIONS or any(part in SKIP_PARTS for part in path.parts):
            continue
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if not FORBIDDEN.search(text):
            continue
        if path.suffix.lower() == ".json":
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                data = None
            if data is not None:
                path.write_text(json.dumps(clean_json(data), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                changed += 1
                continue
        path.write_text("\n".join(clean_text_line(line) for line in text.splitlines()) + "\n", encoding="utf-8")
        changed += 1
    print(f"Sanitized {changed} residual text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
