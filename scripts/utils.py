"""Shared utilities for doc-annotator scripts."""

import os
import sys
from pathlib import Path
from typing import Optional, Tuple

# --- File type detection ---

EXT_ROUTE = {
    ".pptx": "presentation",
    ".ppt": "presentation",
    ".pdf": "paper",
    ".docx": "document",
    ".doc": "document",
    ".xlsx": "spreadsheet",
    ".xls": "spreadsheet",
    ".csv": "spreadsheet",
    ".mp3": "audio",
    ".wav": "audio",
    ".m4a": "audio",
    ".ogg": "audio",
    ".flac": "audio",
    ".html": "web",
    ".htm": "web",
    ".epub": "document",
    ".ipynb": "notebook",
    ".txt": "text",
    ".md": "text",
    ".json": "text",
    ".xml": "text",
}

OUTPUT_EXT = {
    "presentation": ".pptx",
    "paper": ".md",
    "document": ".md",
    "spreadsheet": ".md",
    "audio": ".md",
    "web": ".md",
    "notebook": ".md",
    "text": ".md",
}

ANNOTATION_TYPE_NAMES = {
    "presentation": "演讲备注",
    "paper": "阅读笔记",
    "document": "文档摘要",
    "spreadsheet": "数据解读",
    "audio": "转录纪要",
    "web": "内容摘要",
    "notebook": "代码笔记",
    "text": "关键提炼",
}


def detect_type(file_path: str) -> str:
    """Detect the document type category from file extension."""
    ext = Path(file_path).suffix.lower()
    return EXT_ROUTE.get(ext, "text")


def output_stem(input_path: str) -> str:
    """Generate output file stem based on input path."""
    p = Path(input_path)
    return f"{p.stem}-annotated"


def output_path(input_path: str, output_dir: Optional[str] = None) -> str:
    """Generate full output path for annotation result."""
    p = Path(input_path)
    doc_type = detect_type(input_path)
    ext = OUTPUT_EXT.get(doc_type, ".md")
    stem = output_stem(input_path)
    base = Path(output_dir) if output_dir else p.parent
    return str(base / f"{stem}{ext}")


def find_venv_python() -> Optional[str]:
    """Find a Python executable with required packages.

    Tries in order:
    1. VENV_PATH from environment
    2. Default markitdown venv location
    3. Current Python
    """
    candidates = []

    venv_env = os.environ.get("DOC_ANNOTATOR_VENV")
    if venv_env:
        candidates.append(Path(venv_env) / "Scripts" / "python.exe")
        candidates.append(Path(venv_env) / "bin" / "python")

    # Default venv location (user's markitdown project)
    candidates.append(
        Path("E:/Projects/技能/markitdown 文本转换/.venv/Scripts/python.exe")
    )

    # Current python
    candidates.append(Path(sys.executable))

    for c in candidates:
        if c.exists():
            return str(c)
    return sys.executable
