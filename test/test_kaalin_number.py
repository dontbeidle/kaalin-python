import unittest

from kaalin.number.number import NumberLatin, NumberCyrillic


class TestKaalinNumber(unittest.TestCase):

  def test_to_word_latin(self):
    self.kn = NumberLatin()
    self.assertEqual(self.kn.to_words(5), "bes")
    self.assertEqual(self.kn.to_words(10), "on")
    self.assertEqual(self.kn.to_words(27), "jigirma jeti")
    self.assertEqual(self.kn.to_words(60), "alpıs")
    self.assertEqual(self.kn.to_words(100), "júz")
    self.assertEqual(self.kn.to_words(1_000), "mıń")
    self.assertEqual(self.kn.to_words(1_590), "bir mıń bes júz toqsan")
    self.assertEqual(self.kn.to_words(39_406), "otız toǵız mıń tórt júz altı")
    self.assertEqual(self.kn.to_words(1_000_000), "bir million")
    self.assertEqual(self.kn.to_words(117_790_283), "bir júz on jeti million jeti júz toqsan mıń eki júz seksen úsh")
    self.assertEqual(self.kn.to_words(1_000_000_000), "bir milliard")
    self.assertEqual(self.kn.to_words(303_019_867_115), "úsh júz úsh milliard on toǵız million segiz júz alpıs jeti mıń bir júz on bes")

  def test_to_word_cyrillic(self):
    self.kn = NumberCyrillic()
    self.assertEqual(self.kn.to_words(8), "сегиз")
    self.assertEqual(self.kn.to_words(61), "алпыс бир")
    self.assertEqual(self.kn.to_words(5_000), "бес мың")
    self.assertEqual(self.kn.to_words(965_713), "тоғыз жүз алпыс бес мың жети жүз он үш")
    self.assertEqual(self.kn.to_words(497_781_216), "төрт жүз тоқсан жети миллион жети жүз сексен бир мың еки жүз он алты")
    self.assertEqual(self.kn.to_words(294_619_742_229),"еки жүз тоқсан төрт миллиард алты жүз он тоғыз миллион жети жүз қырық еки мың еки жүз жигирма тоғыз")


if __name__ == '__main__':
  unittest.main()
