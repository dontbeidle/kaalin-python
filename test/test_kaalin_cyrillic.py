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
