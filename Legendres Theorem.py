# number = x**2 + y**2 + z**2

from math import sqrt


def check(n):
    print(sqrt(n))
    s = int(sqrt(n)) + 1
    print(s)
    for i in range(s):
        for j in range(s):
            for k in range(s):
                if i ** 2 + j ** 2 + k ** 2 == n:
                    return ("yes")
    return "no"


print(check(4))

print("---------------------------------------------")

#Kinjal's method

# Legendre's three-square theorem

import math

number = int(input("Enter a number: "))

# finding all the squares in the range of number and putting them in a list called list1
list1 = []
for i in range(0, number + 1):
    sqrt_num = math.sqrt(i)
    if sqrt_num - int(sqrt_num) == 0:
        list1.append(i)
print("All the squares in the list from 0 to", number, "are", list1)

# creating a 3x3 permutation list of all the numbers and making a list of this list as well
list2 = []
for a in list1:
    for b in list1:
        for c in list1:
            numbers = [a, b, c]
            list2.append(numbers)
print(list2)

# checking if each number in the list adds to the main number
list3 = []
for lis in list2:
    sum_of_list = lis[0] + lis[1] + lis[2]
    list3.append(sum_of_list)

if number in list3:
    print("number passes the theorem")
else:
    print("number does not pass the theorem")