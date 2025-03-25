from kaalin.constants import latin_to_cyrillic_uppercase, latin_to_cyrillic_lowercase


class Latin:
  __uppercases = list(filter(lambda char: len(char) == 1, list(latin_to_cyrillic_uppercase.keys())))
  __lowercases = list(filter(lambda char: len(char) == 1, list(latin_to_cyrillic_lowercase.keys())))

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
    return self.text.isalpha()

  def swapcase(self):
    return self.text.swapcase()

  def upper(self):
    upper_mapping = dict(zip(self.__lowercases, self.__uppercases))
    return ''.join(upper_mapping.get(char, char) for char in self.text)

  def lower(self):
    lower_mapping = dict(zip(self.__uppercases, self.__lowercases))
    return ''.join(lower_mapping.get(char, char) for char in self.text)
