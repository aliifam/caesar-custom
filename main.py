from CaesarCipher import caesar_encrypt, caesar_decrypt

def main():
    pw = "Fikri Yurcel Milano"

    pw_encrypt = caesar_encrypt(pw, 20)

    print(pw_encrypt)

    pw_decrypt = caesar_decrypt(pw_encrypt, 20)

    print(pw_decrypt)

main()