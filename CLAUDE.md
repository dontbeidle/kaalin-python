# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**kaalin** is a pure Python library (zero external dependencies) for Karakalpak language operations: Latin-Cyrillic script conversion, number-to-word conversion, and Karakalpak-aware string utilities. Published to PyPI as `kaalin`.

## Commands

```bash
# Install in development mode
pip install -e .

# Run all tests
python -m unittest discover test
pytest test/

# Run a single test file
python -m unittest test.test_kaalin_converter
pytest test/test_num2words.py

# Build distribution packages
python -m build

# CLI tools (after install)
cyr2lat input.txt [output.txt]
lat2cyr input.txt [output.txt]
```

## Architecture

The library has four modules under `kaalin/`:

- **converter/** — `latin2cyrillic()` and `cyrillic2latin()` functions using dictionary-based character mapping from `constants.py`. Handles multi-character sequences (e.g., "sh" → "ш") and Cyrillic soft/hard sign rules ('ьи'→'yi', 'ьо'→'yo', 'ъе'→'ye').
- **number/** — `to_word(number, num_type="lat")` converts integers/floats to Karakalpak words in Latin or Cyrillic script. Supports range 0 to 10^30. Raises `NumberRangeError` for out-of-range values.
- **string/** — `upper()` and `lower()` with Karakalpak-specific character handling ('ı' ↔ 'Í').
- **cli/** — Console script entry points (`cyr2lat`, `lat2cyr`) registered in `pyproject.toml` for file-based text conversion.

Public API is re-exported from `kaalin/__init__.py`.

## Code Style

- 2-space indentation (per `.editorconfig`)
- Max line length: 150 characters
- UTF-8 encoding throughout
- Python 3.10+ type hint syntax (`int | float`)

## Release Process

Version is set in `pyproject.toml` under `[project].version`. Pushing a `v*` tag triggers `.github/workflows/release.yml` which builds and publishes to PyPI via twine.

## Key Constraints

- No external runtime dependencies — keep it pure Python
- CLI entry point changes must be reflected in `pyproject.toml` `[project.scripts]`
- Tests use both `unittest` (converter, string) and `pytest` (number)
