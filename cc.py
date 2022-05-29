from LinkedList import LinkedList

"""
character moved based on ASCII table
"""


def caesar_encode(string, key):
    linked_list = LinkedList()
    for i in range(1, len(string) + 1):
        char = string[i - 1]
        index = ord(char) + key + i
        if index > 126:
            index = (index - 126) + 33
            linked_list.add_last(chr(index))
        else:
            linked_list.add_last(chr(index))
    result = "".join(linked_list.as_array())
    return result


def caesar_decode(encoded, key):
    linked_list = LinkedList()
    for i in range(1, len(encoded) + 1):
        char = encoded[i - 1]
        index = ord(char) - key - i
        if index < 33:
            index = (index + 126) - 33
            linked_list.add_last(chr(index))
        else:
            linked_list.add_last(chr(index))
    result = "".join(linked_list.as_array())
    return result
