import unittest
from kaalin import KaalinLatin

class TestKaalinLatin(unittest.TestCase):
    def setUp(self):
        self.text_upper = "ABC"
        self.text_lower = "abc"
        self.text_mix = "AbC"

    def test_get_uppercases(self):
        expected_uppercases = ['A', 'Á', 'B', 'D', 'E', 'F', 'G', 'Д', 'H', 'X', 'Í', 'I', 'J', 'K', 'Q', 'L', 'M', 'N', 'Ń',
                               'O', 'Ó', 'P', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'Y', 'Z', 'Ш', 'C', 'Ch', ' ']
        self.assertEqual(KaalinLatin.get_uppercases(), expected_uppercases)

    def test_get_lowercases(self):
        expected_lowercases = ['a', 'á', 'b', 'd', 'e', 'f', 'g', 'Ǵ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q', 'l', 'm', 'n', 'ń',
                               'o', 'ó', 'p', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'y', 'z', 'sh', 'c', 'ch', ' ']
        self.assertEqual(KaalinLatin.get_lowercases(), expected_lowercases)

    def test_isupper(self):
        kl = KaalinLatin(self.text_upper)
        self.assertTrue(kl.isupper())

    def test_islower(self):
        kl = KaalinLatin(self.text_lower)
        self.assertTrue(kl.islower())

    def test_isdigit(self):
        kl = KaalinLatin("123")
        self.assertTrue(kl.isdigit())

    def test_isalpha(self):
        kl = KaalinLatin("abc")
        self.assertTrue(kl.isalpha())

    def test_swapcase(self):
        kl = KaalinLatin(self.text_mix)
        self.assertEqual(kl.swapcase(), "aBc")

    def test_upper(self):
        kl = KaalinLatin(self.text_lower)
        self.assertEqual(kl.upper(), self.text_upper)

    def test_lower(self):
        kl = KaalinLatin(self.text_upper)
        self.assertEqual(kl.lower(), self.text_lower)

if __name__ == '__main__':
    unittest.main()
