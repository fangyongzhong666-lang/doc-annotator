#!/usr/bin/env python3
"""Convert any supported file to Markdown using markitdown."""

import argparse
import json
import sys
from pathlib import Path


def ensure_markitdown():
    try:
        from markitdown._markitdown import MarkItDown
        return MarkItDown
    except ImportError:
        sys.stderr.write(
            "markitdown is required. Install with: pip install markitdown\n"
        )
        raise SystemExit(2)


def convert_file(input_path: str, output_path: str | None = None) -> str:
    """Convert a file to Markdown text. Returns the markdown string."""
    MarkItDown = ensure_markitdown()
    md = MarkItDown()
    result = md.convert_local(input_path)
    text = result.text_content.strip()

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")

    return text


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Convert a file to Markdown using markitdown."
    )
    parser.add_argument("input", type=Path, help="Input file path")
    parser.add_argument("--output", "-o", type=Path, help="Output .md file path")
    parser.add_argument("--json", action="store_true", help="Output as JSON with metadata")
    args = parser.parse_args(argv)

    if not args.input.exists():
        sys.stderr.write(f"Input not found: {args.input}\n")
        return 1

    text = convert_file(str(args.input), str(args.output) if args.output else None)

    if args.json:
        import json as _json
        result = {
            "file": str(args.input),
            "text_length": len(text),
            "content": text,
        }
        print(_json.dumps(result, ensure_ascii=False, indent=2))
    elif not args.output:
        print(text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
