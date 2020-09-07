def wordCount(sentence):
    d = {}
    string = sentence.lower().split()
    for word in string:
        new_word = ''
        for c in word:
            if c.isalpha():
                new_word += c
        d[new_word] = d.get(new_word, 0) + 1
    return d


print(wordCount("She was young the way an Actual young person is young."))