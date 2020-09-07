number = input("Enter your number: ")


# reverse the string
reversed_numbers = " ".join(reversed(number))
print("The reversed numbers are", reversed_numbers)
if " " in reversed_numbers:
    reversed_wo_spaces = reversed_numbers.replace(" ", "")


def list_numbers(reversed_wo_spaces):
    odd_list = []
    even_list = []
    for i in range(0, len(reversed_wo_spaces)):
        if i % 2 == 0:
            odd_list.append(reversed_wo_spaces[i])
        else:
            even_list.append(reversed_wo_spaces[i])
    print("The odd list is", odd_list)
    print("The even list is", even_list)
    return odd_list, even_list


def doubledigits():
    number_list = list_numbers(reversed_wo_spaces)
    odd_sum = 0
    even_sum = 0

    for odd in number_list[0]:
        int_odd = int(odd)
        odd_sum += int_odd
    print("The sum of the numbers in the odd positions is", odd_sum)

    for even in number_list[1]:
        int_even = int(even)
        multiply = int_even * 2
        if multiply <= 9:
            sum = multiply
        else:
            sum = 1 + (multiply % 10)
        even_sum += sum
    print("The sum of the numbers in the even positions after doubling them is", even_sum)
    checksum = odd_sum + even_sum
    return checksum


# check if the sum of the characters are divisible by 10 as per Luhn's formula

luhntest_sum = doubledigits()
print("The Total sum is", luhntest_sum)
if luhntest_sum % 10 == 0:
    print("This number qualifies the Luhn algorithm")
else:
    print("not valid")
