#!/usr/bin/env python3
"""Fail if tracked text documentation contains Arabic/Persian or Cyrillic script.

English is the canonical repository documentation language. This guard is intentionally
strict about Arabic/Persian script and Cyrillic script so non-English prose cannot silently
re-enter the repository. Binary/media files are skipped.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".csv", ".py", ".sh", ".ps1", ".ini", ".cfg"
}
SKIP_PARTS = {".git", "git_previews", "__pycache__"}

ARABIC_SCRIPT = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
CYRILLIC_SCRIPT = re.compile(r"[\u0400-\u04FF\u0500-\u052F]")


def tracked_files() -> list[pathlib.Path]:
    try:
        raw = subprocess.check_output(["git", "ls-files", "-z"])
        names = [p.decode("utf-8") for p in raw.split(b"\0") if p]
        return [pathlib.Path(n) for n in names]
    except Exception:
        return [p for p in pathlib.Path(".").rglob("*") if p.is_file()]


def main() -> int:
    violations: list[tuple[str, int, str, str]] = []
    for path in tracked_files():
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if ARABIC_SCRIPT.search(line):
                violations.append((str(path), line_no, "Arabic/Persian script", line.strip()))
            if CYRILLIC_SCRIPT.search(line):
                violations.append((str(path), line_no, "Cyrillic script", line.strip()))

    if violations:
        print("English-only documentation check FAILED.\n")
        seen = set()
        for path, line_no, kind, line in violations:
            key = (path, line_no, kind)
            if key in seen:
                continue
            seen.add(key)
            excerpt = line[:240]
            print(f"{path}:{line_no}: {kind}: {excerpt}")
        print(f"\nTotal violations: {len(seen)}")
        return 1

    print("English-only documentation check passed: no Arabic/Persian or Cyrillic script found in tracked text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
