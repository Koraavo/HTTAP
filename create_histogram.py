from colors import color

print(color.BLUE + "26. Create a histogram from a given list of integers." + color.END)
integers = input("Enter the numbers for the histogram: ")
integers1 = integers.split()
print(integers1)
int_integer = [int(i) for i in integers1]
print(int_integer)
# converted string to list
# each number in the list to integer

# integers entered for example were 1,2,3,4
for x in int_integer:
    his = ""
    new_number = x
    while new_number > 0:
        his = his + "@"
        new_number = new_number - 1
    print(his)

# new simpler way:
for x in integers:
   print("@" * int(x))
