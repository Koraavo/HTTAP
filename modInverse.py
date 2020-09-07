"""
A modular inverse of two numbers is represented by the expression
(a * i) % m == 1, where i is the modular inverse and a and m are the two
numbers. For example, the modular inverse of 5 mod 7 would be some
number i where (5 * i) % 7 is equal to 1.


"""


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that (a * x) % m = 1.
    if gcd(a, m) != 1:
        return None # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m