"""
main.py

Entry point for the SMS Formatter tool.

This script:
1. Reads entries from 'whitelist_numbers.txt'.
2. Normalizes numbers (adds '27' if missing).
3. Formats output as '?, ?, <value>'.
4. Saves to formatted_whitelisted_numbers_output.txt.
"""

from pathlib import Path
from .io_utils import read_lines, write_output
from .processor import normalize_entries
from .formatter import format_entries


def main():
    """
    Main workflow of the SMS formatter.
    """
    project_root = Path(__file__).parent.parent.resolve()
    input_file = project_root / "whitelist_numbers.txt"
    output_file = project_root / "formatted_whitelisted_numbers_output.txt"

    print(f"🔍 Reading from: {input_file}")
    print(f"📝 Writing to: {output_file}")

    # Step 1: Read raw entries
    try:
        entries = read_lines(str(input_file))
    except FileNotFoundError as e:
        print(e)
        return

    # Step 2: Normalize entries (add 27 where necessary)
    normalized = normalize_entries(entries)

    # Step 3: Format them into "?, ?, <value>"
    formatted = format_entries(normalized)

    # Step 4: Write to output file
    write_output(str(output_file), formatted)

    print(f"✅ Done! Processed {len(formatted)} entries.")
    print(f"Results saved in {output_file}")


if __name__ == "__main__":
    main()
