"""
io_utils.py

Handles file input and output operations for the SMS formatter tool.
"""

from pathlib import Path
from typing import List


def read_lines(file_path: str) -> List[str]:
    """
    Reads lines from a text file, one per line.

    Args:
        file_path (str): Path to the input file.

    Returns:
        List[str]: List of non-empty lines stripped of whitespace.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"❌ Error: {file_path} not found.")

    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def write_output(file_path: str, lines: List[str]) -> None:
    """
    Writes output lines to a file, one per line.

    Args:
        file_path (str): Path to the output file.
        lines (List[str]): List of formatted lines to write.

    Notes:
        - Overwrites the file if it already exists.
        - Each element is written on a new line.
    """
    path = Path(file_path)
    path.write_text("\n".join(lines), encoding="utf-8")
