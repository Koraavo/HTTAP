from colors import color
print(color.BLUE + "31. Compute the lowest common multiple (LCM) of two positive integers." + color.END)
print(color.YELLOW + "The fastest way to calculate the LCM of two or more numbers is\n"
                     "check if the numbers when divided result in 0\n"
                     "if no, select the biggest of the two\n"
                     "keep on multiplying it with 1-10\n"
                     "one of the numbers will result in a reminder of 0\n"
                     "when divided with the other smaller number\n"
                     "for example: 45, 100\n"
                     "biggest number is 100\n"
                     "100/45 != 0\n"
                     "(100*2)/45 != 0\n"
                     "(100*9)/45 = 0" + color.END)

def lcm(num1,num2):
    if num1<num2:
        num1, num2 = num2, num1
    if num1 > num2:
        if num1 % num2 == 0:
            print(num1)
        else:
            for k in range(1, 11):
                if (num1 * k) % num2 == 0:
                    print(num1 * k)
                    break
    return ()
lcm(18, 24)
lcm (100, 45)