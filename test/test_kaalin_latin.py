import unittest
from kaalin.words.latin import Latin


class TestKaalinLatin(unittest.TestCase):
  def setUp(self):
    self.text_upper = "ABC"
    self.text_lower = "abc"
    self.text_mix = "AbC"

  def test_isupper(self):
    kl = Latin(self.text_upper)
    self.assertTrue(kl.isupper())

  def test_islower(self):
    kl = Latin(self.text_lower)
    self.assertTrue(kl.islower())

  def test_isdigit(self):
    kl = Latin("123")
    self.assertTrue(kl.isdigit())

  def test_isalpha(self):
    kl = Latin("abc")
    self.assertTrue(kl.isalpha())

  def test_swapcase(self):
    kl = Latin(self.text_mix)
    self.assertEqual(kl.swapcase(), "aBc")

  def test_upper(self):
    kl = Latin(self.text_lower)
    self.assertEqual(kl.upper(), self.text_upper)

  def test_lower(self):
    kl = Latin(self.text_upper)
    self.assertEqual(kl.lower(), self.text_lower)


if __name__ == '__main__':
  unittest.main()
