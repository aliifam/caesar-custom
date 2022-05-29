from cc import caesar_encode, caesar_decode

pw = "suka suka suka"

pw_encode = caesar_encode(pw, 4)

print(pw_encode)

pw_decode = caesar_decode(pw_encode, 4)

print(pw_decode)