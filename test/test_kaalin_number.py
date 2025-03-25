import unittest
from kaalin.number import Number


class TestKaalinNumber(unittest.TestCase):
  def setUp(self):
    self.kn = Number()

  def test_to_word(self):
    self.assertEqual(self.kn.to_word(5), "bes")
    self.assertEqual(self.kn.to_word(27), "jigirma jeti")
    self.assertEqual(self.kn.to_word(1000), "mıń")


if __name__ == '__main__':
  unittest.main()
