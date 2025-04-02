"""
This module provides two functions for converting text between uppercase and lowercase
while handling a special character replacement:
- `upper(text: str) -> str`: Converts text to uppercase, replacing 'ı' with 'Í'.
- `lower(text: str) -> str`: Converts text to lowercase, replacing 'Í' with 'ı'.

These functions are useful when working with text that includes the Karakalpak dotless 'ı'
and its uppercase variant.
"""


def upper(text: str) -> str:
  """Convert the text to uppercase with special character replacement."""
  return text.replace("ı", "Í").upper()


def lower(text: str) -> str:
  """Convert the text to lowercase with special character replacement."""
  return text.lower().replace("Í", "ı")
