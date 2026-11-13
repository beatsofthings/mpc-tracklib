#!/usr/bin/env python3
"""Read-only SDK inspection; heuristic only, not proof of browser support."""
import argparse
from pathlib import Path
import re
import sys

TERMS = {
    "webview": r"\b(webview|web_view|webkit|chromium|cef|browserview)\b",
    "rendering": r"\b(framebuffer|texture|rendercontext|drawimage|customview)\b",
    "touch": r"\b(touch(event|down|up)?|pointerevent|mouseevent)\b",
    "network": r"\b(curl|httpclient|httpsclient|socket|networkrequest)\b",
    "files": r"\b(fopen|filesystem|fileoutputstream|writefile|savefile)\b",
}
EXTENSIONS = {".h", ".hpp", ".hh", ".c", ".cc", ".cpp", ".cmake", ".md", ".txt"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk", type=Path, help="Path to extracted Akai SDK")
    args = parser.parse_args()
    if not args.sdk.is_dir():
        parser.error("SDK directory not found")
    findings = {key: [] for key in TERMS}
    scanned = 0
    for path in args.sdk.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            data = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        for name, pattern in TERMS.items():
            if re.search(pattern, data, re.IGNORECASE):
                findings[name].append(str(path.relative_to(args.sdk)))
    print(f"Inspected {scanned} SDK text/source files")
    for name, matches in findings.items():
        print(f"\n{name}: {len(matches)} matching files")
        for path in matches[:15]:
            print("  " + path)
    print("\nIMPORTANT: Keyword matches are NOT evidence that the SDK exposes usable browser APIs.")
    print("Review API declarations, target platform, licensing and hardware behavior manually.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
