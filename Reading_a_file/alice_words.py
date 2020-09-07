import string
import re

def count_words(file_name):
    """Count the approx length of words in the document"""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry {file_name} is not found")
    else:
        puncs = string.punctuation
        print(puncs)
        d = {}
        words = contents.lower().split()
        for word in words:
            word = re.sub('[^\w]', "", word).replace("_", "")
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        # list out keys and values separately
        key_list = list(d.keys())
        val_list = list(d.values())

        for values in sorted(key_list):
            print(values, d[values])

        maxi = 0
        for k, v in d.items():
            if v > maxi:
                maxi = v
        print(f"Alice appears {d['alice']} times.")
        print(f"The longest word in the text is '{key_list[val_list.index(maxi)]}' with {maxi} values")


count_words('alice1.txt')

# with open('alice1.txt', encoding='utf-8') as f:
#     count = {}
#     for line in f:
#         for word in line.split():
#             # remove punctuation
#             word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
#             word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
#             word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
#             word = word.replace(']', '').replace(';', '')
#
#             # ignore case
#             word = word.lower()
#
#             # ignore numbers
#             if word.isalpha():
#                 if word in count:
#                     count[word] = count[word] + 1
#                 else:
#                     count[word] = 1
#
#     keys = count.keys()
#
#     # save the word count analysis to a file
#     out = open('alice_words.txt', 'w')
#
#     for word in sorted(keys):
#         out.write(word + " " + str(count[word]))
#         out.write('\n')
#
#     print("The word 'alice' appears " + str(count['alice']) + " times in the book.")