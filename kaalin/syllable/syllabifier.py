"""Split Karakalpak words into syllables.

Works with both Latin and Cyrillic Karakalpak text. Cyrillic input is
transliterated to Latin for the pattern-matching pass and then
converted back, so callers get syllables in the same script they
passed in. Original letter case is preserved.

The algorithm:

1. Collapse multi-character letter sequences (``sh``, ``ch``, ``yu``,
   ``ya``, ``aw``, ``ew``) into single placeholder characters so the
   classifier can treat them atomically.
2. Map each character to ``V`` (vowel), ``C`` (consonant) or ``?``
   (unknown).
3. Walk the resulting pattern with a fixed set of rules that reflect
   Karakalpak phonotactics, producing a list of syllable lengths.
4. Slice the original word with those lengths so each syllable keeps
   its own characters and case.
"""

from kaalin.converter import cyrillic2latin, latin2cyrillic


_VOWELS = set("aáeioóuúíıÿŷåê")
_CONSONANTS = set("bcdfgǵhjklmnńpqrsştçvwxyz")

_ONSET_CLUSTERS = frozenset({
    "bl", "br", "dr", "fl", "fr", "gl", "gr",
    "kl", "kr", "pl", "pr", "sk", "sl", "sm", "sn", "sp", "st",
    "tr",
})

# (original multi-char sequence, single-char placeholder)
_AUTO_CORRECT_PAIRS = (
    ("sh", "ş"),
    ("ch", "ç"),
    ("yu", "ŷ"),
    ("ya", "ÿ"),
    ("aw", "å"),
    ("ew", "ê"),
)


def _auto_correct(text: str) -> str:
    for src, dst in _AUTO_CORRECT_PAIRS:
        text = text.replace(src, dst)
    return text


def _inverse_correct(text: str) -> str:
    for src, dst in _AUTO_CORRECT_PAIRS:
        text = text.replace(dst, src)
    return text


def _classify(text: str) -> str:
    return "".join(
        "V" if ch in _VOWELS else "C" if ch in _CONSONANTS else "?"
        for ch in text
    )


def _create_map(pattern: str, text: str) -> list[int]:
    syllable_map: list[int] = []
    i = 0
    n = len(pattern)

    def p(offset: int = 0) -> str:
        idx = i + offset
        return pattern[idx] if idx < n else ""

    while i < n:

        # ── V-initial ──────────────────────────────────────────────
        if p(0) == "V":
            if p(1) in ("", "V"):
                syllable_map.append(1); i += 1
            elif p(1) == "C" and p(2) == "V":
                syllable_map.append(1); i += 1
            elif p(1) == "C" and p(2) == "C" and p(3) == "V":
                if text[i + 1 : i + 3] in _ONSET_CLUSTERS:
                    syllable_map.append(1); i += 1
                else:
                    syllable_map.append(2); i += 2
            elif p(1) == "C" and p(2) == "C" and p(3) == "C" and p(4) == "V":
                syllable_map.append(3); i += 3
            elif p(1) == "C" and p(2) == "C":
                syllable_map.append(3); i += 3
            else:
                syllable_map.append(2); i += 2

        # ── C-initial ──────────────────────────────────────────────
        elif p(0) == "C":

            # CCV-initial
            if p(1) == "C" and p(2) == "V":
                if p(3) in ("", "V"):
                    syllable_map.append(3); i += 3
                elif p(3) == "C" and p(4) == "V":
                    syllable_map.append(3); i += 3
                elif p(3) == "C" and p(4) == "C" and p(5) == "V":
                    syllable_map.append(4); i += 4
                elif p(3) == "C" and p(4) == "C":
                    syllable_map.append(5); i += 5
                else:
                    syllable_map.append(4); i += 4

            # CV-initial
            elif p(1) == "V":
                if p(2) in ("", "V"):
                    syllable_map.append(2); i += 2
                elif p(2) == "C" and p(3) == "V":
                    syllable_map.append(2); i += 2
                elif p(2) == "C" and p(3) == "C" and p(4) == "V":
                    syllable_map.append(3); i += 3
                elif p(2) == "C" and p(3) == "C" and p(4) == "C" and p(5) == "V":
                    syllable_map.append(3); i += 3
                elif p(2) == "C" and p(3) == "C":
                    syllable_map.append(4); i += 4
                else:
                    syllable_map.append(3); i += 3

            else:
                syllable_map.append(1); i += 1
        else:
            syllable_map.append(1); i += 1

    return syllable_map


def _count_vowels(text: str) -> int:
    return sum(1 for ch in text if ch in _VOWELS)


def _is_cyrillic(text: str) -> bool:
    return any("\u0400" <= ch <= "\u04FF" for ch in text)


def syllabify(word: str) -> list[str]:
    """Split a single Karakalpak word into syllables.

    Accepts Latin or Cyrillic Karakalpak input and returns the
    syllables in the same script as the input, with the original
    letter case preserved.

    Args:
        word: The word to split. Leading and trailing whitespace is
            ignored.

    Returns:
        A list of syllables. An empty input yields an empty list.
        Words with fewer than two vowels are returned as a single
        syllable unchanged.

    Raises:
        TypeError: If ``word`` is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")

    stripped = word.strip()
    if not stripped:
        return []

    was_cyrillic = _is_cyrillic(stripped)
    latin_word = cyrillic2latin(stripped) if was_cyrillic else stripped

    lower_word = latin_word.lower()
    corrected = _auto_correct(lower_word)

    if _count_vowels(corrected) < 2:
        return [stripped]

    pattern = _classify(corrected)
    syllable_map = _create_map(pattern, corrected)

    # Slice the corrected (placeholder) string so we know how much of
    # it belongs to each syllable.
    rem = corrected
    corrected_parts: list[str] = []
    for length in syllable_map:
        corrected_parts.append(rem[:length])
        rem = rem[length:]
    if rem:
        corrected_parts[-1] += rem

    # Restore multi-char letters — the length of each restored part
    # now matches the original Latin word.
    restored = [_inverse_correct(part) for part in corrected_parts]

    # Index into the original Latin word to keep the caller's case.
    cased: list[str] = []
    idx = 0
    for part in restored:
        step = len(part)
        cased.append(latin_word[idx : idx + step])
        idx += step

    if was_cyrillic:
        return [latin2cyrillic(part) for part in cased]
    return cased
