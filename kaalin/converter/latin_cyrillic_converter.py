import re
import unicodedata

from kaalin.constants import (
  latin_to_cyrillic, cyrillic_to_latin, loanwords, cyrillic_variants, apostrophes, apostrophe_letters,
)

_WORD_RE = re.compile(r'([a-zA-ZáÁǵǴıÍńŃóÓúÚ]+)')
_LATIN_VOWELS = frozenset('aáeiıoóuúAÁEIÍOÓUÚ')


def _convert_chars(text: str) -> str:
  result = []
  i = 0
  while i < len(text):
    if i < len(text) - 1 and text[i:i + 2] in latin_to_cyrillic:
      result.append(latin_to_cyrillic[text[i:i + 2]])
      i += 2
    else:
      result.append(latin_to_cyrillic.get(text[i], text[i]))
      i += 1
  return ''.join(result)


def _apply_case(source: str, target: str) -> str:
  if not source or not target:
    return target
  if source.isupper():
    return target.upper()
  if source[0].isupper():
    return target[0].upper() + target[1:]
  return target


def join_apostrophes(text: str) -> str:
  """Writes the apostrophe spelling in Karakalpak letters: o'zbek → ózbek, g‘alaba → ǵalaba, bardi' → bardı.

  An apostrophe after a, g, i, n, o or u is joined to that letter inside a word and at its end. An apostrophe
  that closes a quotation is kept: in 'Jańa Ózbekstan' the last apostrophe follows n but closes the quotation.
  """
  out = []
  quoted = False  # an opening apostrophe is waiting for its closing one
  prev_letter = False
  i, n = 0, len(text)
  while i < n:
    ch = text[i]
    nxt = text[i + 1] if i + 1 < n else ''
    if ch in apostrophe_letters and nxt and nxt in apostrophes:
      after = text[i + 2] if i + 2 < n else ''
      if after.isalpha() or not quoted:
        out.append(apostrophe_letters[ch])
        prev_letter = True
        i += 2
        continue
    if ch in apostrophes:
      if not prev_letter and nxt.isalpha():
        quoted = True  # opening quotation mark
      elif prev_letter and not nxt.isalpha():
        quoted = False  # closing quotation mark
    elif ch in '\n\r.!?':
      quoted = False
    prev_letter = ch.isalpha()
    out.append(ch)
    i += 1
  return ''.join(out)


def latin2cyrillic(text: str, custom_loanwords: dict[str, str] | None = None, apostrophe_spelling: bool = True) -> str:
  text = unicodedata.normalize('NFC', text)
  if apostrophe_spelling:
    text = join_apostrophes(text)

  merged = loanwords
  if custom_loanwords:
    merged = {**loanwords, **custom_loanwords}

  sorted_keys = sorted(merged, key=len, reverse=True)

  tokens = _WORD_RE.split(text)
  result = []

  for idx, token in enumerate(tokens):
    if idx % 2 == 0:
      result.append(token)
    else:
      word_lower = token.lower().replace('í', 'ı')
      converted = None

      if word_lower in merged:
        converted = _apply_case(token, merged[word_lower])
      else:
        for key in sorted_keys:
          if word_lower.startswith(key):
            suffix = token[len(key):]
            stem = merged[key]
            if stem.endswith('ь') and suffix and suffix[0] in _LATIN_VOWELS:
              stem = stem[:-1]
            prefix_cyrillic = _apply_case(token[:len(key)], stem)
            suffix_cyrillic = _convert_chars(suffix)
            converted = prefix_cyrillic + suffix_cyrillic
            break

      if converted is None:
        converted = _convert_chars(token)

      result.append(converted)

  return ''.join(result)


def cyrillic2latin(text: str) -> str:
  text = unicodedata.normalize('NFC', text).translate(cyrillic_variants)
  text = handle_special_cyrillic_rules_if_needed(text)
  result = []
  for i, char in enumerate(text):
    replacement = cyrillic_to_latin.get(char, char)
    if len(replacement) > 1 and char.isupper():
      prev_upper = False
      next_upper = False
      for j in range(i - 1, -1, -1):
        if text[j].isalpha():
          prev_upper = text[j].isupper()
          break
      for j in range(i + 1, len(text)):
        if text[j].isalpha():
          next_upper = text[j].isupper()
          break
      if prev_upper or next_upper:
        replacement = replacement.upper()
    result.append(replacement)
  return ''.join(result)


# A sign between a letter and a vowel is read as y: Ильин → Ilyin, павильон → pavilyon, объект → obyekt
_SIGN_VOWEL_RE = re.compile(r'(?<=[^\W\d_])(ь[ио]|Ь[ИОио]|ъе|Ъ[Ее])', re.IGNORECASE)
_SIGN_VOWEL = {'ьи': 'yi', 'ьо': 'yo', 'ъе': 'ye'}


def handle_special_cyrillic_rules_if_needed(text: str) -> str:
  def repl(m: re.Match) -> str:
    pair = m.group(1)
    lat = _SIGN_VOWEL.get(pair.lower())
    if lat is None:
      return pair
    if pair[1].isupper():
      return lat.upper() if pair[0].isupper() else 'y' + lat[1].upper()
    return lat

  return _SIGN_VOWEL_RE.sub(repl, text)
