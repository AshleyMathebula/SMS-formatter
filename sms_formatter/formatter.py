"""
formatter.py

Converts normalized entries into the final output format:
?, ?, <entry>
"""

from typing import List


def format_entries(entries: List[str]) -> List[str]:
    """
    Format entries into the structure '?, ?, <value>'.

    Args:
        entries (List[str]): Normalized entries.

    Returns:
        List[str]: Formatted strings ready for writing to file.
    """
    formatted = [f"?, ?, {entry}" for entry in entries]
    return formatted
