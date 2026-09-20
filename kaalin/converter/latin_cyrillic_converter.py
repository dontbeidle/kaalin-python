import re

from kaalin.constants import latin_to_cyrillic, cyrillic_to_latin, loanwords

_WORD_RE = re.compile(r'([a-zA-ZáÁǵǴıÍńŃóÓúÚ]+)')


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


def latin2cyrillic(text: str, custom_loanwords: dict[str, str] | None = None) -> str:
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
            prefix_cyrillic = _apply_case(token[:len(key)], merged[key])
            suffix_cyrillic = _convert_chars(token[len(key):])
            converted = prefix_cyrillic + suffix_cyrillic
            break

      if converted is None:
        converted = _convert_chars(token)

      result.append(converted)

  return ''.join(result)


def cyrillic2latin(text: str) -> str:
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


def handle_special_cyrillic_rules_if_needed(text: str) -> str:
  special_rule_pairs = {
    'ьи': 'yi',
    'ьо': 'yo',
    'ъе': 'ye',
  }

  for cyr, lat in special_rule_pairs.items():
    if cyr in text and not text.startswith(cyr):
      text = text.replace(cyr, lat)
  return text
