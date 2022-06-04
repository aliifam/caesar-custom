import random
import string

def generate_string(n):
    rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    return rand_string 
