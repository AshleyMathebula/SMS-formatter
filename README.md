# SMS Formatter

A simple Whitelisting Python tool to read phone numbers, short codes, or text entries from a file and format them into a standardized output suitable for SMS or system processing.

---

## 🧩 Features

- Reads numbers and entries from a text file (`numbers.txt`).
- Normalizes South African phone numbers:
  - Adds country code `27` if missing.
  - Removes leading zeros from local numbers.
- Leaves short codes (e.g., `14811`) or text entries (e.g., `CELLC`) unchanged.
- Outputs formatted lines in the pattern:

?, ?, <number>

- Modular, maintainable code with separate modules for I/O, processing, and formatting.

---

## 🏆 Project Impact

Before this tool, formatting phone numbers, short codes, and text entries into the required SMS-ready format was manual and time-consuming. Staff had to check each line, add the country code (27) if missing, remove leading zeros, and then format the output correctly. This process could take hours depending on the file size.

With the SMS Formatter:

- The entire process is now fully automated.

- Numeric entries are normalized automatically (adds 27, removes leading zeros).

- Text entries and short codes are preserved without errors.

- All entries are formatted in the ?, ?, <entry> pattern in seconds.

- Large files that previously took hours can now be processed in less than 10 minutes, improving efficiency and reducing human error.
