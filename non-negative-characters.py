from colors import color

print(color.BLUE + "23. Get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2" + color.END)

def new_copy(str, n):
    if len(str) == 2:
        return (str * n)
    else:
        new_string = str[:2]
        return(new_string*n)

print(new_copy("ab", 3))