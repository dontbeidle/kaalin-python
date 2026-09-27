import unittest
from kaalin.constants import loanwords
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
    self.assertEqual(latin2cyrillic("evropa"), "европа")
    self.assertEqual(latin2cyrillic("ÁJINIYAZ"), "ӘЖИНИЯЗ")

  def test_latin2cyrillic_loanwords_soft_sign(self):
    """Soft sign (ь) must not be dropped in borrowed words."""
    self.assertEqual(latin2cyrillic("avtomobil"), "автомобиль")
    self.assertEqual(latin2cyrillic("akropol"), "акрополь")
    self.assertEqual(latin2cyrillic("bolshoy"), "большой")
    self.assertEqual(latin2cyrillic("veksel"), "вексель")
    self.assertEqual(latin2cyrillic("gegel"), "гегель")
    self.assertEqual(latin2cyrillic("delta"), "дельта")
    self.assertEqual(latin2cyrillic("dúnya"), "дүнья")
    self.assertEqual(latin2cyrillic("dárya"), "дәрья")
    self.assertEqual(latin2cyrillic("impuls"), "импульс")
    self.assertEqual(latin2cyrillic("knyaz"), "князь")
    self.assertEqual(latin2cyrillic("kompyuter"), "компьютер")
    self.assertEqual(latin2cyrillic("korol"), "король")
    self.assertEqual(latin2cyrillic("krovat"), "кровать")
    self.assertEqual(latin2cyrillic("model"), "модель")
    self.assertEqual(latin2cyrillic("neapol"), "неаполь")
    self.assertEqual(latin2cyrillic("nol"), "ноль")
    self.assertEqual(latin2cyrillic("oblast"), "область")
    self.assertEqual(latin2cyrillic("optimal"), "оптималь")
    self.assertEqual(latin2cyrillic("parallel"), "параллель")
    self.assertEqual(latin2cyrillic("pech"), "печь")
    self.assertEqual(latin2cyrillic("relef"), "рельеф")
    self.assertEqual(latin2cyrillic("rol"), "роль")
    self.assertEqual(latin2cyrillic("rıcar"), "рыцарь")
    self.assertEqual(latin2cyrillic("statya"), "статья")
    self.assertEqual(latin2cyrillic("stil"), "стиль")
    self.assertEqual(latin2cyrillic("fevral"), "февраль")
    self.assertEqual(latin2cyrillic("filtraciya"), "фильтрация")
    self.assertEqual(latin2cyrillic("folklor"), "фольклор")

  def test_latin2cyrillic_loanwords_э(self):
    """э must not become е in borrowed words."""
    self.assertEqual(latin2cyrillic("aloe"), "алоэ")
    self.assertEqual(latin2cyrillic("koefficient"), "коэффициент")
    self.assertEqual(latin2cyrillic("poeziya"), "поэзия")
    self.assertEqual(latin2cyrillic("poet"), "поэт")
    self.assertEqual(latin2cyrillic("evolyuciya"), "эволюция")
    self.assertEqual(latin2cyrillic("ekzistencializm"), "экзистенциализм")
    self.assertEqual(latin2cyrillic("ekzonim"), "экзоним")
    self.assertEqual(latin2cyrillic("ekologiya"), "экология")
    self.assertEqual(latin2cyrillic("ekonomika"), "экономика")
    self.assertEqual(latin2cyrillic("ekran"), "экран")
    self.assertEqual(latin2cyrillic("eksperiment"), "эксперимент")
    self.assertEqual(latin2cyrillic("ekspert"), "эксперт")
    self.assertEqual(latin2cyrillic("ekspressiv"), "экспрессив")
    self.assertEqual(latin2cyrillic("elektron"), "электрон")
    self.assertEqual(latin2cyrillic("element"), "элемент")
    self.assertEqual(latin2cyrillic("emitent"), "эмитент")
    self.assertEqual(latin2cyrillic("emocional"), "эмоционал")
    self.assertEqual(latin2cyrillic("empiriya"), "эмпирия")
    self.assertEqual(latin2cyrillic("enciklopediya"), "энциклопедия")
    self.assertEqual(latin2cyrillic("epotoponim"), "эпотопоним")
    self.assertEqual(latin2cyrillic("etika"), "этика")
    self.assertEqual(latin2cyrillic("etimologiya"), "этимология")

  def test_latin2cyrillic_loanwords_hard_sign(self):
    """ъ must not become й in borrowed words."""
    self.assertEqual(latin2cyrillic("obyekt"), "объект")
    self.assertEqual(latin2cyrillic("obyektiv"), "объектив")
    self.assertEqual(latin2cyrillic("subyekt"), "субъект")
    self.assertEqual(latin2cyrillic("subyektiv"), "субъектив")

  def test_latin2cyrillic_loanwords_ё(self):
    """ё must not become йо in borrowed words."""
    self.assertEqual(latin2cyrillic("samolyot"), "самолёт")
    self.assertEqual(latin2cyrillic("schyot"), "счёт")

  def test_latin2cyrillic_loanwords_щ(self):
    """щ must not become ш in borrowed words."""
    self.assertEqual(latin2cyrillic("obshina"), "община")
    self.assertEqual(latin2cyrillic("borsh"), "борщ")
    self.assertEqual(latin2cyrillic("shit"), "щит")
    self.assertEqual(latin2cyrillic("shchit"), "щит")

  def test_latin2cyrillic_soft_sign_before_vowel_suffix(self):
    """A stem-final ь is dropped before a vowel-initial suffix, kept before a consonant."""
    self.assertEqual(latin2cyrillic("oktyabrinde"), "октябринде")
    self.assertEqual(latin2cyrillic("oktyabrde"), "октябрьде")
    self.assertEqual(latin2cyrillic("sekretarı"), "секретары")
    self.assertEqual(latin2cyrillic("sekretardıń"), "секретарьдың")
    self.assertEqual(latin2cyrillic("lageri"), "лагери")
    self.assertEqual(latin2cyrillic("lagerdiń"), "лагерьдиң")
    self.assertEqual(latin2cyrillic("avtomobilin"), "автомобилин")
    self.assertEqual(latin2cyrillic("avtomobiller"), "автомобильлер")
    self.assertEqual(latin2cyrillic("ansambli"), "ансамбли")
    self.assertEqual(latin2cyrillic("ansambldi"), "ансамбльди")
    self.assertEqual(latin2cyrillic("tabeli"), "табели")
    self.assertEqual(latin2cyrillic("spektaklinde"), "спектаклинде")
    self.assertEqual(latin2cyrillic("modeli"), "модели")
    self.assertEqual(latin2cyrillic("dvigateliniń"), "двигателиниң")

  def test_latin2cyrillic_loanword_does_not_steal_longer_word(self):
    """A short loanword key must not swallow a longer, unrelated word."""
    self.assertEqual(latin2cyrillic("cirkul"), "циркуль")
    self.assertEqual(latin2cyrillic("cirkulyar"), "циркуляр")
    self.assertEqual(latin2cyrillic("ventil"), "вентиль")
    self.assertEqual(latin2cyrillic("ventilyaciya"), "вентиляция")
    self.assertEqual(latin2cyrillic("ventilyator"), "вентилятор")
    self.assertEqual(latin2cyrillic("modul"), "модуль")
    self.assertEqual(latin2cyrillic("modulyaciya"), "модуляция")
    self.assertEqual(latin2cyrillic("kontrol"), "контроль")
    self.assertEqual(latin2cyrillic("kontroller"), "контроллер")

  def test_latin2cyrillic_new_loanwords(self):
    """Words added from the qaraqalpaq explanatory dictionary."""
    self.assertEqual(latin2cyrillic("apelsin"), "апельсин")
    self.assertEqual(latin2cyrillic("aprel"), "апрель")
    self.assertEqual(latin2cyrillic("asfalt"), "асфальт")
    self.assertEqual(latin2cyrillic("bulvar"), "бульвар")
    self.assertEqual(latin2cyrillic("dekabr"), "декабрь")
    self.assertEqual(latin2cyrillic("kartofel"), "картофель")
    self.assertEqual(latin2cyrillic("kolco"), "кольцо")
    self.assertEqual(latin2cyrillic("korabl"), "корабль")
    self.assertEqual(latin2cyrillic("palto"), "пальто")
    self.assertEqual(latin2cyrillic("fakultet"), "факультет")
    self.assertEqual(latin2cyrillic("aeroport"), "аэропорт")
    self.assertEqual(latin2cyrillic("energiya"), "энергия")
    self.assertEqual(latin2cyrillic("eskiz"), "эскиз")
    self.assertEqual(latin2cyrillic("podyezd"), "подъезд")
    self.assertEqual(latin2cyrillic("semya"), "семья")
    self.assertEqual(latin2cyrillic("sudya"), "судья")
    self.assertEqual(latin2cyrillic("plash"), "плащ")
    self.assertEqual(latin2cyrillic("ovosh"), "овощ")

  def test_latin2cyrillic_preserves_case(self):
    """Loanword lookup must keep the casing of the source token."""
    self.assertEqual(latin2cyrillic("Aprel"), "Апрель")
    self.assertEqual(latin2cyrillic("APREL"), "АПРЕЛЬ")
    self.assertEqual(latin2cyrillic("Sekretarı"), "Секретары")
    self.assertEqual(latin2cyrillic("KORABL"), "КОРАБЛЬ")

  def test_loanword_round_trip(self):
    """Every loanword must survive cyrillic -> latin -> cyrillic unchanged."""
    broken = [cyr for cyr in loanwords.values()
              if latin2cyrillic(cyrillic2latin(cyr)) != cyr]
    self.assertEqual(broken, [])

  def test_loanword_keys_match_their_values(self):
    """Each key must be the latin transliteration of its cyrillic value.

    Aliases are exempt: they accept a spelling a user may type even though
    cyrillic2latin never produces it. "shchit" is the russian-style
    transliteration of щит, which cyrillic2latin renders as "shit".
    """
    aliases = {'shchit'}
    mismatched = [(key, value) for key, value in loanwords.items()
                  if key not in aliases
                  and cyrillic2latin(value).lower().replace('í', 'ı') != key]
    self.assertEqual(mismatched, [])

  def test_loanword_keys_are_long_enough(self):
    """Very short keys match too many unrelated words through prefix lookup.

    "a" would rewrite every word starting with a, "al" every form of alıw.
    """
    too_short = [key for key in loanwords if len(key) < 3]
    self.assertEqual(too_short, [])


if __name__ == '__main__':
  unittest.main()
