import unittest
import random
from datetime import datetime
from generator import generate_string
from CaesarCipher import caesar_encrypt, caesar_decrypt


n = random.randint(1, 100)

key = random.randint(1, 100)

rand_text = generate_string(n)

f = open("log.txt", "a+", encoding="utf-8")

class TestStringMethods(unittest.TestCase):

    def test_cipher(self):
        f.write(f"tanggal        = {datetime.now()}\n")
        f.write(f"key            = {n} \n")
        f.write("plain text     = ")
        f.write(f'"{rand_text}"\n')
        f.write("encrypted text = ")
        f.write(f'"{caesar_encrypt(rand_text, key)}"\n')
        f.write("decrypted text = ")
        f.write(f'"{caesar_decrypt(caesar_encrypt(rand_text, key), key)}"\n')
        f.write("plain text     = ")
        f.write(f'"{rand_text}"\n')
        if caesar_decrypt(caesar_encrypt(rand_text, key), key) == rand_text:
            f.write("Test Result    = OK \n")
        else:
            f.write("Test Result = Failed \n")
        f.write("-" * 130)
        f.write("\n")
        self.assertEqual(caesar_decrypt(caesar_encrypt(rand_text, n), n), rand_text)

if __name__ == '__main__':
    unittest.main()
