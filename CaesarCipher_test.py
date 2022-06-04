import unittest
import random
import pytz
from logFormatter import line_prepender
from datetime import datetime
from generator import generate_string
from CaesarCipher import caesar_encrypt, caesar_decrypt


n = random.randint(1, 100)

key = random.randint(1, 100)

rand_text = generate_string(n)

now = datetime.now()
lokal = pytz.timezone('Asia/Jakarta')

class TestStringMethods(unittest.TestCase):

    def test_cipher(self):
        log = f"tanggal        = {lokal.localize(now).strftime('%Y-%m-%d %H:%M:%S')}\n"
        log += f"key            = {n} \n"
        log += "plain text     = "
        log += f'"{rand_text}"\n'
        log += "encrypted text = "
        log += f'"{caesar_encrypt(rand_text, key)}"\n'
        log += "decrypted text = "
        log += f'"{caesar_decrypt(caesar_encrypt(rand_text, key), key)}"\n'
        log += "plain text     = "
        log += f'"{rand_text}"\n'
        if caesar_decrypt(caesar_encrypt(rand_text, key), key) == rand_text:
            log += "Test Result    = OK \n"
        else:
            log += "Test Result = Failed \n"
        log += "-" * 130
        log += "\n"
        line_prepender("log.txt", log)
        print(log)
        self.assertEqual(caesar_decrypt(caesar_encrypt(rand_text, n), n), rand_text)

if __name__ == '__main__':
    unittest.main()
