"""
sms_formatter package

Provides utilities for reading, normalizing, and formatting SMS numbers.
"""

__version__ = "1.0.0"
__author__ = "Ashley Mathebula"

# Optional — expose key functions for easy import
from .io_utils import read_lines, write_output
from .processor import normalize_entries
from .formatter import format_entries

__all__ = ["read_lines", "write_output", "normalize_entries", "format_entries"]
