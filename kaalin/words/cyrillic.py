from kaalin.constants import cyrillic_to_latin_uppercase, cyrillic_to_latin_lowercase


class Cyrillic:
  __uppercases = list(cyrillic_to_latin_uppercase.keys())
  __lowercases = list(cyrillic_to_latin_lowercase.keys())

  def __init__(self, text):
    self.text = text

  @classmethod
  def get_uppercases(cls):
    return cls.__uppercases

  @classmethod
  def get_lowercases(cls):
    return cls.__lowercases

  def isupper(self):
    return all(char in self.__uppercases for char in self.text)

  def islower(self):
    return all(char in self.__lowercases for char in self.text)

  def isdigit(self):
    return self.text.isdigit()

  def isalpha(self):
    return self.text.isalpha() or self.text.isnumeric()

  def swapcase(self):
    return self.text.swapcase()

  def upper(self):
    upper_mapping = dict(zip(self.__lowercases, self.__uppercases))
    return ''.join(upper_mapping.get(char, char) for char in self.text)

  def lower(self):
    lower_mapping = dict(zip(self.__uppercases, self.__lowercases))
    return ''.join(lower_mapping.get(char, char) for char in self.text)
