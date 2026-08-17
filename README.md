# Kaalin

[![PyPI version](https://img.shields.io/pypi/v/kaalin)](https://pypi.org/project/kaalin/)
[![Python](https://img.shields.io/pypi/pyversions/kaalin)](https://pypi.org/project/kaalin/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Python toolkit for the **Karakalpak language**. Zero dependencies, Python 3.10+.

## Installation

```bash
pip install kaalin
```

## Script Conversion

Bidirectional Latin ↔ Cyrillic conversion. Loanwords with special characters (ь, ъ, э, ё, щ) are handled automatically.

```python
from kaalin.converter import latin2cyrillic, cyrillic2latin

latin2cyrillic("Assalawma áleykum")  # Ассалаўма әлейкум
cyrillic2latin("Ассалаўма әлейкум")  # Assalawma áleykum

# You can extend the built-in loanword dictionary with your own entries
latin2cyrillic("stilistika", custom_loanwords={"stilistika": "стилистика"})
```

## Number to Words

Converts numbers to Karakalpak words. Supports integers, floats, and negatives up to 10³⁰.

```python
from kaalin.number import to_word

to_word(123)                   # bir júz jigirma úsh
to_word(999, num_type="cyr")   # тоғыз жүз тоқсан тоғыз
```

## Syllabification

Splits words into syllables. Works with both Latin and Cyrillic input.

```python
from kaalin.syllable import syllabify

syllabify("qaraqalpaqstan")   # ['qa', 'ra', 'qal', 'paq', 'stan']
syllabify("Шарапат")          # ['Ша', 'ра', 'пат']
```

## String Utilities

Karakalpak-aware `upper()` / `lower()` that correctly handle the dotless `ı` ↔ `Í` pair.

```python
from kaalin.string import upper, lower

upper("Assalawma áleykum")   # ASSALAWMA ÁLEYKUM
lower("ASSALAWMA ÁLEYKUM")   # assalawma áleykum
```

## CLI

Convert text files between scripts from the terminal:

```bash
cyr2lat input.txt              # writes input-lat.txt
lat2cyr input.txt              # writes input-cyr.txt
```

## License

MIT

<!--
API REFERENCE FOR AI AGENTS

## converter

from kaalin.converter import latin2cyrillic, cyrillic2latin

latin2cyrillic(text: str, custom_loanwords: dict[str, str] | None = None) -> str
  Converts Latin script to Cyrillic. Handles multi-char sequences (sh→ш, ch→ч, ya→я, yu→ю).
  Built-in loanword dictionary handles words with ь, ъ, э, ё, щ automatically.
  custom_loanwords merges with (and overrides) built-in dict.
  Supports uppercase, lowercase, and mixed-case text.

cyrillic2latin(text: str) -> str
  Converts Cyrillic script to Latin. Handles special rules: ьи→yi, ьо→yo, ъе→ye.

## number

from kaalin.number import to_word, NumberRangeError

to_word(number: int | float, num_type: str = "lat") -> str
  Converts number to Karakalpak words.
  num_type: "lat" (default) or "cyr" for output script.
  Supports: 0 to 10^30, negatives, floats.
  Raises NumberRangeError if number exceeds 10^30.

## syllable

from kaalin.syllable import syllabify

syllabify(word: str) -> list[str]
  Splits word into syllables. Works with Latin and Cyrillic input.
  Auto-detects script. Preserves original case.
  Words with fewer than two vowels are returned as single-element list.
  Raises TypeError if input is not a string.

## string

from kaalin.string import upper, lower

upper(text: str) -> str
  Karakalpak-aware uppercase. Handles dotless ı → Í correctly.

lower(text: str) -> str
  Karakalpak-aware lowercase. Handles Í → ı correctly.

## CLI

cyr2lat input.txt [output.txt]   Cyrillic → Latin file conversion
lat2cyr input.txt [output.txt]   Latin → Cyrillic file conversion
Default output: input-lat.txt / input-cyr.txt
-->
