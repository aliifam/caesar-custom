from CaesarCipher import caesar_encode, caesar_decode

pw = "Fikri Yurcel Milano"

pw_encode = caesar_encode(pw, 20)

print(pw_encode)

pw_decode = caesar_decode(pw_encode, 20)

print(pw_decode)