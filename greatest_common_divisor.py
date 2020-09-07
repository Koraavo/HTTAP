from colors import color
import time

print(color.BLUE + "31. Compute the greatest common divisor (GCD) of two positive integers." + color.END)
print(color.YELLOW + "GCD or Greatest common divisor of a number can be calculated by two methods\n"
                     "in the first method, find the remainder of the first two numbers\n"
                     "for example: 3768/1701 leaves a reminder of 366\n"
                     "divide r i.e 366 by the smallest of the numbers\n"
                     "reminder is 237.\n Divide 237 with 366\n"
                     "reminder of 129\n. Divide this with again the smallest i.e 237\n"
                     "keep on dividing until the result is 0" + color.END)


def gcd(num1, num2):
    if num1 < num2:
        num1 = num2
        num2 = num1
    while num2 != 0:
        r = num1 % num2
        print("r", r)
        num1 = num2
        print("num1", num1)
        num2 = r
        print("num2", num2)
    print(num1)
    return num1


# Measure how long the encryption/decryption takes:
startTime = time.time()
gcd(3768, 1701)
totalTime = round(time.time() - startTime, 2)
print('%s seconds' % totalTime)
