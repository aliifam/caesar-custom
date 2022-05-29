import unittest
from cc import caesar_encode, caesar_decode


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(caesar_encode("suka suka suka", 4), "x{ri)}\"wn.$'|s")
    def test_case2(self):
        self.assertEqual(caesar_encode("suka suka suka", 4), "x{ri)}\"wn.$'|s")
    def test_case3(self):
        self.assertEqual(caesar_encode("suka suka suka", 4), "x{ri)}\"wn.$'|s")

if __name__ == '__main__':
    unittest.main()
