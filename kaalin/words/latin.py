class Latin:
    __uppercases = ['A', 'Á', 'B', 'D', 'E', 'F', 'G', 'Ǵ', 'H', 'X', 'Í', 'I', 'J', 'K', 'Q', 'L', 'M', 'N', 'Ń',
                    'O', 'Ó', 'P', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'Y', 'Z', 'Ш', 'C', 'Ch', ' ']
    __lowercases = ['a', 'á', 'b', 'd', 'e', 'f', 'g', 'ǵ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q', 'l', 'm', 'n', 'ń',
                    'o', 'ó', 'p', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'y', 'z', 'sh', 'c', 'ch', ' ']

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