import unittest

from tpu import transpose

class TestTranspose(unittest.TestCase):
    def test_parsing_simple(self):
        tabs = "A B C D E F G".split()
        expected = "A# C C# D# F F# G#".split()
        self.assertEqual(transpose(tabs, 1), expected)

    def test_parsing_minor(self):
        tabs = "Am Bm Cm Dm Em Fm Gm".split()
        expected = "A#m Cm C#m D#m Fm F#m G#m".split()
        self.assertEqual(transpose(tabs, 1), expected)

    def test_parsing_flats(self):
        tabs = "Db Eb Gb Ab Bb".split()
        expected = "C# D# F# G# A#".split()
        self.assertEqual(transpose(tabs, 0), expected)

    def test_cyclic_property(self):
        tabs = "C# D# F# G# A#".split()
        expected = tabs
        self.assertEqual(transpose(tabs, 12), expected)


if __name__ == "__main__":
    unittest.main()
