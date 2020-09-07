from colors import color

print(color.BLUE + "7. Accept a filename from the user and print the extension of that." + color.END)

print(color.BLUE + "Solutions" + color.END)

file_name = input("Enter the file name with extension: ")
extension = file_name.split(".")[-1]
print(extension)
