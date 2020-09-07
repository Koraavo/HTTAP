from colors import color

print(color.BLUE + "10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn."

"Sample value of n is 5"
"Expected Result : 615" + color.END)

number = input("Your number is: " )
number_adds = int(number) + int(number+number) + int(number+number+number)
print(number_adds)