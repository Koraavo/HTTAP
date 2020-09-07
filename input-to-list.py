from colors import color

print(color.BLUE + "# 6. Write a program which accepts a sequence of comma-separated numbers from user\n and generate a list and a tuple with those numbers." + color.END)

X = input("Enter your numbers: ")
Values = X.split(",")
print (list(Values))
print(tuple(Values))
