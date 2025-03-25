import unittest
from kaalin.converter.latin_cyrillic_converter import latin2cyrillic, cyrillic2latin


class TestKaalinConverter(unittest.TestCase):

  def test_cyrillic2latin(self):
    self.assertEqual(cyrillic2latin("щётка"), "shyotka")
    self.assertEqual(cyrillic2latin("циркуль"), "cirkul")
    self.assertEqual(cyrillic2latin("чемпион"), "chempion")
    self.assertEqual(cyrillic2latin("интервью"), "intervyu")
    self.assertEqual(cyrillic2latin("объект"), "obyekt")
    self.assertEqual(cyrillic2latin("дәрья"), "dárya")
    self.assertEqual(cyrillic2latin("павильон"), "pavilyon")
    self.assertEqual(cyrillic2latin("Ильин"), "Ilyin")
    self.assertEqual(cyrillic2latin("адъютант"), "adyutant")
    self.assertEqual(cyrillic2latin("адъютант"), "adyutant")
    self.assertEqual(cyrillic2latin("КҮНХОЖА"), "KÚNXOJA")

  def test_latin2cyrillic(self):
    self.assertEqual(latin2cyrillic("Sharapat"), "Шарапат")
    self.assertEqual(latin2cyrillic("hújdan"), "ҳүждан")
    self.assertEqual(latin2cyrillic("tuwısqanlıq"), "туўысқанлық")
    self.assertEqual(latin2cyrillic("Olarǵa"), "Оларға")
    self.assertEqual(latin2cyrillic("qádir-qımbat"), "қәдир-қымбат")
    self.assertEqual(latin2cyrillic("yupiter"), "юпитер")
    self.assertEqual(latin2cyrillic("ÁJINIYAZ"), "ӘЖИНИЯЗ")


if __name__ == '__main__':
  unittest.main()
