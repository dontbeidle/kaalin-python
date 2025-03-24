import unittest
from kaalin.words.cyrillic import Cyrillic

class TestKaalinCyrillic(unittest.TestCase):
    def setUp(self):
        self.text_upper = "АБВ"
        self.text_lower = "абв"
        self.text_mix = "АбВ"
        self.text_digit = "123"
        self.text_alpha = "абвгд"
        self.text_numeric = "123абв"

    def test_get_uppercases(self):
        expected_uppercases = ['А', 'Ә', 'Б', 'Д', 'Е', 'Ф', 'Г', 'Ғ', 'Ҳ', 'Х', 'Ы', 'И', 'Ж', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң',
                               'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ү', 'В', 'Ў', 'Й', 'З', 'Ш', 'Ц', 'Ч', ' ']
        self.assertEqual(Cyrillic.get_uppercases(), expected_uppercases)

    def test_get_lowercases(self):
        expected_lowercases = ['а', 'ә', 'б', 'д', 'е', 'ф', 'г', 'ғ', 'ҳ', 'х', 'ы', 'и', 'ж', 'к', 'қ', 'л', 'м', 'н', 'ң',
                               'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'в', 'ў', 'й', 'з', 'ш', 'ц', 'ч', ' ']
        self.assertEqual(Cyrillic.get_lowercases(), expected_lowercases)

    def test_isupper(self):
        kc = Cyrillic(self.text_upper)
        self.assertTrue(kc.isupper())

    def test_islower(self):
        kc = Cyrillic(self.text_lower)
        self.assertTrue(kc.islower())

    def test_isdigit(self):
        kc = Cyrillic(self.text_digit)
        self.assertTrue(kc.isdigit())

    def test_isalpha(self):
        kc_alpha = Cyrillic(self.text_alpha)
        self.assertTrue(kc_alpha.isalpha())
        kc_numeric = Cyrillic(self.text_numeric)
        self.assertFalse(kc_numeric.isalpha())

    def test_swapcase(self):
        kc = Cyrillic(self.text_mix)
        self.assertEqual(kc.swapcase(), "аБв")

    def test_upper(self):
        kc = Cyrillic(self.text_lower)
        self.assertEqual(kc.upper(), self.text_upper)

    def test_lower(self):
        kc = Cyrillic(self.text_upper)
        self.assertEqual(kc.lower(), self.text_lower)

if __name__ == '__main__':
    unittest.main()
