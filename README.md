# Kaalin

[![PyPI version](https://img.shields.io/pypi/v/kaalin)](https://pypi.org/project/kaalin/)
[![Python](https://img.shields.io/pypi/pyversions/kaalin)](https://pypi.org/project/kaalin/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Python toolkit for the **Karakalpak language**: Latin-Cyrillic script conversion, number-to-words, and locale-aware string operations. Zero dependencies.

## Quick Start

```bash
pip install kaalin
```

```python
from kaalin.converter import latin2cyrillic, cyrillic2latin

print(latin2cyrillic("Assalawma áleykum"))  # Ассалаўма әлейкум
print(cyrillic2latin("Ассалаўма әлейкум"))  # Assalawma áleykum
```

## Supported Features

| Feature | Description |
|---|---|
| **Script Conversion** | Bidirectional Latin ↔ Cyrillic conversion with multi-character mapping (`sh`→`ш`, `ch`→`ч`) and special Cyrillic rules (`ьи`→`yi`, `ьо`→`yo`, `ъе`→`ye`) |
| **Number to Words** | Converts integers and floats to Karakalpak words in Latin or Cyrillic script. Supports range 0 to 10³⁰, negative numbers, and decimal fractions |
| **String Utilities** | Karakalpak-aware `upper()` / `lower()` that correctly handle the dotless `ı` ↔ `Í` character pair |
| **CLI Tools** | `cyr2lat` and `lat2cyr` commands for converting text files from the terminal |

## API Reference

### Script Conversion

```python
from kaalin.converter import latin2cyrillic, cyrillic2latin

latin2cyrillic("Qaraqalpaqstan")    # Қарақалпақстан
cyrillic2latin("Қарақалпақстан")    # Qaraqalpaqstan
```

Both functions accept a `str` and return a `str`. The converter handles uppercase, lowercase, and mixed-case text.

### Number to Words

```python
from kaalin.number import to_word, NumberRangeError

to_word(123)                     # bir júz jigirma úsh
to_word(999, num_type="cyr")     # тоғыз жүз тоқсан тоғыз
to_word(12.75)                   # on eki pútin júzden jetpis bes
to_word(-42)                     # minus qırıq eki
```

**Parameters:**
- `number` (`int | float`) — the number to convert
- `num_type` (`str`) — output script: `"lat"` (default) or `"cyr"`

**Raises:** `NumberRangeError` if `number` exceeds 10³⁰.

### String Utilities

```python
from kaalin.string import upper, lower

upper("Assalawma áleykum")   # ASSALAWMA ÁLEYKUM
lower("ASSALAWMA ÁLEYKUM")   # assalawma áleykum
```

Python's built-in `str.upper()` / `str.lower()` does not handle the Karakalpak dotless `ı` correctly. These functions fix that.

## CLI Usage

Convert text files between scripts directly from the terminal:

```bash
# Cyrillic → Latin
cyr2lat input.txt              # writes input-lat.txt
cyr2lat input.txt output.txt   # writes output.txt

# Latin → Cyrillic
lat2cyr input.txt              # writes input-cyr.txt
lat2cyr input.txt output.txt   # writes output.txt
```

## When to Use Kaalin

- Converting Karakalpak text between Latin and Cyrillic scripts
- Displaying numbers as Karakalpak words (invoices, checks, education)
- NLP preprocessing for Karakalpak text (script normalization)
- Building Karakalpak-language applications that need locale-aware string operations
- Batch-converting text files via CLI

## When NOT to Use Kaalin

- **Not a translator** — it converts scripts (Latin ↔ Cyrillic), not languages
- **Not a spell-checker** — it does not validate or correct Karakalpak text
- **Not for other Turkic languages** — Kazakh, Uzbek, Turkish, etc. have different alphabets and rules
- **Not an OCR tool** — it works with digital text, not images