"""
processor.py

Processes and normalizes entries from the input file before formatting.

Rules:
- If an entry starts with digits and does not begin with "27", prefix "27".
- If the entry already starts with "27", leave it as is.
- If it contains letters (like CELLC, LEAPPRD), leave it unchanged.
- If it’s numeric but short (like 14811), leave it unchanged.
"""

from typing import List


def normalize_entries(entries: List[str]) -> List[str]:
    """
    Normalize each entry according to business rules.

    Args:
        entries (List[str]): Raw input lines from file.

    Returns:
        List[str]: Normalized entries ready for formatting.
    """
    normalized = []

    for entry in entries:
        clean = entry.strip()

        # Case 1: Purely digits
        if clean.isdigit():
            # Remove leading zero if it exists
            if clean.startswith("0"):
                clean = clean[1:]

            # Add '27' prefix only if it doesn’t already start with '27'
            if not clean.startswith("27"):
                clean = f"27{clean}"

        # Case 2: Mixed alphanumeric or text — leave as is (CELLC, LEAPPRD, etc.)
        # Case 3: Numbers that already start with '27' remain unchanged

        normalized.append(clean)

    return normalized
