from colors import color
print(color.BLUE + "Write a Python program which accepts the radius of a circle from the user and compute the area.\n" + color.END)

from math import pi
r = input("Please enter the radius of the circle: ")
area = pi * (float(r) ** 2)
print("The area of the circle is: ", area)
