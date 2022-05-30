import unittest
from CaesarCipher import caesar_encode, caesar_decode


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(caesar_encode("suka suka suka", 4), "x{ri)}\"wn.$'|s")
    def test_case2(self):
        self.assertEqual(caesar_encode("Aliif Arief Maulana", 10), "Lxvwu0R&|y{6dy0(|,~")
    def test_case3(self):
        self.assertEqual(caesar_encode("Fikri Yurcel Milano", 20), "[!$,$:t31#&.Ao.2(68")

if __name__ == '__main__':
    unittest.main()
