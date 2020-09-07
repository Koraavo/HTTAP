'''
sub = {'A': 'V',
       'B': 'J',
       'C': 'Z',
       'D': 'B',
       'E': 'G',
       'F': 'N',
       'G': 'F',
       'H': 'E',
       'I': 'P',
       'J': 'L',
       'K': 'I',
       'L': 'T',
       'M': 'M',
       'N': 'X',
       'O': 'D',
       'P': 'W',
       'Q': 'K',
       'R': 'Q',
       'S': 'U',
       'T': 'C',
       'U': 'R',
       'V': 'Y',
       'W': 'A',
       'X': 'H',
       'Y': 'S',
       'Z': 'O'}

'''

import string
import collections

def caesar(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by) # option only in collections
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    outtab_h = 'VJZBGNFEPLITMXDWKQUCRYAHSO'
    outtab_l = outtab_h.lower()

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))
print("\n")
print(caesar("This is the code", 1))
print("\n")

our_string = "TESTing"

for i in range(len(string.ascii_uppercase)):
    print(i, "|", caesar(our_string, i))



print("SIMPLIFIED WAY")
print("_______________")
print ("\n")


import string

cipher = "badcfehgjilknmporqtsvuxwzy".upper() + "badcfehgjilknmporqtsvuxwzy"

def encrypt(message, cipher):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

def decrypt(encrypted, cipher):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted




encrypted = encrypt('HELLO world', cipher)
print(encrypted)

decrypted = decrypt(encrypted, cipher)
print(decrypted)

