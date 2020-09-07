# from test import testEqual
import string


def removeWhite(s):
    for element in string.punctuation:
        if element in s:
            new_s = s.replace(element, ' ')
            list = new_s.lower().split()
            s = ''.join(list)
            return s
    return s


def isPal(s):
    reverse = s[::-1]
    return s == reverse


# print(isPal(removeWhite("madam i'm adam")))
# print(isPal(removeWhite("x")))
print(removeWhite('x'))
# print(removeWhite("madam i'm adam"))
