"""
character moved based on ASCII table
dynamic changes by index process
"""

def caesar_encode(string, key):
    lres = []
    for i in range(1, len(string) + 1):
        char = string[i - 1]
        index = ord(char) + key + i
        if index > 126:
            index = (index - 126) + 32
            lres.append(chr(index))
        else:
            lres.append(chr(index))
    result = "".join(lres)
    return result

def caesar_decode(encoded, key):
    lres = []
    for i in range(1, len(encoded) + 1):
        char = encoded[i - 1]
        index = ord(char) - key - i
        if index < 32:
            index = (index + 126) - 32
            lres.append(chr(index))
        else:
            lres.append(chr(index))
    result = "".join(lres)
    return result