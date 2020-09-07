import string

with open('alice1.txt', encoding='utf-8') as f:
    count = {}
    for line in f:
        for word in line.split():
            # remove punctuation
            word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
            word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
            word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
            word = word.replace(']', '').replace(';', '')

            # ignore case
            word = word.lower()

            # ignore numbers
            if word.isalpha():
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    keys = count.keys()

    # save the word count analysis to a file
    out = open('alice_words.txt', 'w')

    for word in sorted(keys):
        out.write(word + " " + str(count[word]))
        out.write('\n')

    print("The word 'alice' appears " + str(count['alice']) + " times in the book.")