cyrillic_to_latin_uppercase = {
  'А': 'A',
  'Ә': 'Á',
  'Б': 'B',
  'В': 'V',
  'Г': 'G',
  'Ғ': 'Ǵ',
  'Д': 'D',
  'Е': 'E',
  'Ё': 'Yo',
  'Ж': 'J',
  'З': 'Z',
  'И': 'I',
  'Й': 'Y',
  'К': 'K',
  'Қ': 'Q',
  'Л': 'L',
  'М': 'M',
  'Н': 'N',
  'Ң': 'Ń',
  'О': 'O',
  'Ө': 'Ó',
  'П': 'P',
  'Р': 'R',
  'С': 'S',
  'Т': 'T',
  'У': 'U',
  'Ү': 'Ú',
  'Ў': 'W',
  'Ф': 'F',
  'Х': 'X',
  'Ҳ': 'H',
  'Ц': 'C',
  'Ч': 'Ch',
  'Ш': 'Sh',
  'Щ': 'Sh',
  'Ъ': '',
  'Ы': 'Í',
  'Ь': '',
  'Э': 'E',
  'Ю': 'Yu',
  'Я': 'Ya',
}

cyrillic_to_latin_lowercase = {
  'а': 'a',
  'ә': 'á',
  'б': 'b',
  'в': 'v',
  'г': 'g',
  'ғ': 'ǵ',
  'д': 'd',
  'е': 'e',
  'ё': 'yo',
  'ж': 'j',
  'з': 'z',
  'и': 'i',
  'й': 'y',
  'к': 'k',
  'қ': 'q',
  'л': 'l',
  'м': 'm',
  'н': 'n',
  'ң': 'ń',
  'о': 'o',
  'ө': 'ó',
  'п': 'p',
  'р': 'r',
  'с': 's',
  'т': 't',
  'у': 'u',
  'ү': 'ú',
  'ў': 'w',
  'ф': 'f',
  'х': 'x',
  'ҳ': 'h',
  'ц': 'c',
  'ч': 'ch',
  'ш': 'sh',
  'щ': 'sh',
  'ъ': '',
  'ы': 'ı',
  'ь': '',
  'э': 'e',
  'ю': 'yu',
  'я': 'ya',
}

latin_to_cyrillic_uppercase = {
  # we need to put this to the top, otherwise they will be processed as two letters
  'Sh': 'Ш',
  'SH': 'Ш',
  'Ch': 'Ч',
  'CH': 'Ч',
  'Ya': 'Я',
  'YA': 'Я',
  'Yu': 'Ю',
  'YU': 'Ю',

  # the rest is in alphabetical order
  'A': 'А',
  'Á': 'Ә',
  'B': 'Б',
  'D': 'Д',
  'E': 'Е',
  'F': 'Ф',
  'G': 'Г',
  'Ǵ': 'Ғ',
  'H': 'Ҳ',
  'X': 'Х',
  'Í': 'Ы',
  'I': 'И',
  'J': 'Ж',
  'K': 'К',
  'Q': 'Қ',
  'L': 'Л',
  'M': 'М',
  'N': 'Н',
  'Ń': 'Ң',
  'O': 'О',
  'Ó': 'Ө',
  'P': 'П',
  'R': 'Р',
  'S': 'С',
  'T': 'Т',
  'U': 'У',
  'Ú': 'Ү',
  'V': 'В',
  'W': 'Ў',
  'Y': 'Й',
  'Z': 'З',
  'C': 'Ц',
}

latin_to_cyrillic_lowercase = {
  # we need to put this to the top, otherwise they will be processed as two letters
  'sh': 'ш',
  'ch': 'ч',
  'ya': 'я',
  'yu': 'ю',

  # the rest is in alphabetical order
  'a': 'а',
  'á': 'ә',
  'b': 'б',
  'd': 'д',
  'e': 'е',
  'f': 'ф',
  'g': 'г',
  'ǵ': 'ғ',
  'h': 'ҳ',
  'x': 'х',
  'ı': 'ы',
  'i': 'и',
  'j': 'ж',
  'k': 'к',
  'q': 'қ',
  'l': 'л',
  'm': 'м',
  'n': 'н',
  'ń': 'ң',
  'o': 'о',
  'ó': 'ө',
  'p': 'п',
  'r': 'р',
  's': 'с',
  't': 'т',
  'u': 'у',
  'ú': 'ү',
  'v': 'б',
  'w': 'ў',
  'y': 'й',
  'z': 'з',
  'c': 'ц',
}

cyrillic_to_latin = cyrillic_to_latin_uppercase | cyrillic_to_latin_lowercase
latin_to_cyrillic = latin_to_cyrillic_uppercase | latin_to_cyrillic_lowercase
