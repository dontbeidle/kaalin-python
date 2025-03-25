from kaalin.constants import latin_to_cyrillic, cyrillic_to_latin


def latin2cyrillic(text: str) -> str:
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


def cyrillic2latin(text: str) -> str:
  text = handle_special_cyrillic_rules_if_needed(text)
  result = []
  for char in text:
    result.append(cyrillic_to_latin.get(char, char))
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
