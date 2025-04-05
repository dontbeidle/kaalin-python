import unittest
from kaalin.string import upper, lower


class TestKaalinString(unittest.TestCase):
  def test_upper(self):
    self.assertEqual(upper("sálem"), "SÁLEM")
    self.assertEqual(upper("Sálem Álem"), "SÁLEM ÁLEM")
    self.assertEqual(upper("ılaq oyın"), "ÍLAQ OYÍN")

  def test_lower(self):
    self.assertEqual(lower("Sálem"), "sálem")
    self.assertEqual(lower("SÁLEM ÁLEM"), "sálem álem")
    self.assertEqual(lower("Ílaq Oyın"), "ılaq oyın")
