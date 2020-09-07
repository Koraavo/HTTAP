'''
# count the number of instances of a letter
word = 'JOKKERS'
for i in range(len(word)):
    if string.startswith('K',i):
        print(i)

#OR
print([i for i in range(len(word)) if word.startswith('K', i)])

#OR
count = [i for i, ltr in enumerate(word, 1) if ltr == letter] # which position are the letters
    final_count = str(count).strip('[]') # converting count to string

'''

import string

word = "hanging".upper()
total_guesses = len(word)
letter = input("Enter a letter: ").upper()
# spaces = "_ " * total_guesses
# print(spaces)
# out_of_guesses = False




