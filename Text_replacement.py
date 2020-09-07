# Simple program:
# if answer is y, it says I told you so
# else something is wrong

Word = "Y"
question = ""
question = input("Enter your answer, Y or N: ")
if question.islower():
    question = question.upper()
    print(question)
    if Word == question:
        print("I told you so")
    else:
        print("Something is wrong")

print("--------------------------------------")

print("Making a translator.\n Replace all the vowels to g")


def translate(phrase):  # A 'phrase' string must be passed in whenever this 'translate' function is called
    new_phrase = ""  # First, create an empty string named 'new_phrase'
    for letter in phrase:  # Next, for each character in the passed-in 'phrase' string, do the following:
        if letter.lower() in "aeiou":  # so if aeiou is lower case, it is checking
            # if all letters when converted to lower match to aeiou
            if letter.isupper():  # If the analyzed character is in UPPER CASE, do the following:
                new_phrase = new_phrase + "Z"  # Add a "Z" to the current (string) value of 'translation'
            else:  # If the analyzed character is NOT in UPPER CASE, do the following:
                new_phrase = new_phrase + "z"  # Add a "z" to the current (string) value of 'translation'
        else:  # If the lower-case version of the analyzed character is NOT in the string "aeiou",
            # then do the following:
            new_phrase = new_phrase + letter  # Add the analyzed (non-vowel) character
    # returns hzllz

    for H in new_phrase:  # Program to replace h in the result.
        if new_phrase.isupper():
            new_phrase = new_phrase.replace('H', 'X')
        else:
            new_phrase = new_phrase.replace('h', 'x')
    return new_phrase


print(translate(input("enter a phrase: ")))

print("--------------------EOP-----------------------------------")


print("Python program to Replace Characters in a String.\n Only works if one character is entered")

str1 = input("Please Enter your Own String : ")
ch = input("Please Enter your Own Character : ")
newch = input("Please Enter the New Character : ")

str2 = ''
for i in str1:
    if (i == ch):
        str2 = str2 + newch
    else:
        str2 = str2 + i

print("\nOriginal String :  ", str1)
print("Modified String :  ", str2)

print("--------------------EOP-----------------------------------")

print("Python program to Replace Characters in a String")

str1 = input("Please Enter your Own String : ")
ch = input("Please Enter your Own Character : ")
newch = input("Please Enter the New Character : ")

str2 = ''
for i in range(len(str1)):  # for i in range of the length of the string entered
    if (str1[i] == ch):  # if i exists in the array of string 1 and is equal to the character entered
        str2 = str2 + newch  # add it to string 2
    else:
        str2 = str2 + str1[i]

print("\nOriginal String :  ", str1)
print("Modified String :  ", str2)

print("--------------------EOP-----------------------------------")

new = ['|<', '@', '1', '3', '7', '0', '8', '\/']
old = ['K', 'A', 'L', 'E', 'T', 'O', 'B', 'V']
ask_user = input("Type a sentence: ")


def ask_replace_letters():
    ask_user2 = input("Do you want to replace letters? ").upper()  # different name for variable
    if ask_user2 == "YES":
        ask_user1 = input("What letters do you want to replace? ").upper()
        letters = []  # letters to replace
        for letter in ask_user1:
            if letter not in old:
                print("This program cannot replace the letter: ", letter)  # may be repeated
            else:
                letters += letter  # add letter to letters to replace
        print(replace_letters(letters))  # replace them

    elif ask_user2 == "NO":
        print(replace_letters())

    else:
        print("Please enter yes or no.")


def replace_letters(letters=[]):  # input for which chars to replace, rather than all
    result = ask_user.upper()  # so it will match
    for i in letters:  # for each to replace
        pos = old.index(i)  # get pos in old/new lists
        result = result.replace(old[pos], new[pos])  # replace
    return result.lower()  # lower, since we have done upper


ask_replace_letters()

# ----------------------------------------
