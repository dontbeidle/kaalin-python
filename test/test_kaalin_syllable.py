import unittest

from kaalin.syllable import syllabify


class TestKaalinSyllable(unittest.TestCase):

    def test_latin_basic(self):
        self.assertEqual(syllabify("adam"), ["a", "dam"])
        self.assertEqual(syllabify("adamlar"), ["a", "dam", "lar"])
        self.assertEqual(syllabify("áke"), ["á", "ke"])
        self.assertEqual(syllabify("ata"), ["a", "ta"])
        self.assertEqual(syllabify("balalar"), ["ba", "la", "lar"])
        self.assertEqual(syllabify("úydegiler"), ["úy", "de", "gi", "ler"])
        self.assertEqual(syllabify("usıdan"), ["u", "sı", "dan"])
        self.assertEqual(syllabify("házir"), ["há", "zir"])
        self.assertEqual(syllabify("futbol"), ["fut", "bol"])
        self.assertEqual(syllabify("yanvar"), ["yan", "var"])
        self.assertEqual(syllabify("mart"), ["mart"])
        self.assertEqual(syllabify("úlke"), ["úl", "ke"])
        self.assertEqual(syllabify("telefon"), ["te", "le", "fon"])
        self.assertEqual(syllabify("meniń"), ["me", "niń"])
        self.assertEqual(syllabify("seniń"), ["se", "niń"])
        

    def test_latin_complex_clusters(self):
        self.assertEqual(
            syllabify("qaraqalpaqstan"),
            ["qa", "ra", "qal", "paq", "stan"],
        )
        self.assertEqual(syllabify("ózbekstan"), ["óz", "bek", "stan"])

    def test_latin_digraphs(self):
        # "yu" is a single vocalic sound: yu → ŷ
        self.assertEqual(syllabify("kompyuter"), ["kom", "pyu", "ter"])
        # "aw" collapses into one vowel unit: aw → å
        self.assertEqual(syllabify("awıl"), ["aw", "ıl"])
        # "sh" collapses into one consonant unit: sh → ş
        self.assertEqual(syllabify("sharapat"), ["sha", "ra", "pat"])
        # "ch" collapses into one consonant unit: ch → ç
        self.assertEqual(syllabify("chempion"), ["chem", "pi", "on"])

    def test_latin_single_vowel_returns_whole_word(self):
        self.assertEqual(syllabify("hám"), ["hám"])
        self.assertEqual(syllabify("top"), ["top"])
        self.assertEqual(syllabify("zor"), ["zor"])
        self.assertEqual(syllabify("men"), ["men"])

    def test_latin_preserves_case(self):
        self.assertEqual(syllabify("Adam"), ["A", "dam"])
        self.assertEqual(syllabify("Sharapat"), ["Sha", "ra", "pat"])
        self.assertEqual(syllabify("ADAMLAR"), ["A", "DAM", "LAR"])

    def test_cyrillic_basic(self):
        self.assertEqual(syllabify("адам"), ["а", "дам"])
        self.assertEqual(syllabify("баллалар"), ["бал", "ла", "лар"])
        self.assertEqual(syllabify("әке"), ["ә", "ке"])
        self.assertEqual(syllabify("ата"), ["а", "та"])

    def test_cyrillic_complex(self):
        self.assertEqual(
            syllabify("қарақалпақстан"),
            ["қа", "ра", "қал", "пақ", "стан"],
        )
        self.assertEqual(syllabify("өзбекстан"), ["өз", "бек", "стан"])
        self.assertEqual(syllabify("шарапат"), ["ша", "ра", "пат"])

    def test_cyrillic_preserves_case(self):
        self.assertEqual(syllabify("Адам"), ["А", "дам"])
        self.assertEqual(syllabify("Шарапат"), ["Ша", "ра", "пат"])

    def test_cyrillic_single_vowel(self):
        self.assertEqual(syllabify("ҳәм"), ["ҳәм"])
        self.assertEqual(syllabify("топ"), ["топ"])
        self.assertEqual(syllabify("зор"), ["зор"])

    def test_whitespace_is_stripped(self):
        self.assertEqual(syllabify("  adam  "), ["a", "dam"])

    def test_empty_string(self):
        self.assertEqual(syllabify(""), [])
        self.assertEqual(syllabify("   "), [])

    def test_non_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            syllabify(42)
        with self.assertRaises(TypeError):
            syllabify(None)
        with self.assertRaises(TypeError):
            syllabify(["adam"])

    def test_exposed_at_package_root(self):
        import kaalin

        self.assertIs(kaalin.syllabify, syllabify)


if __name__ == "__main__":
    unittest.main()
