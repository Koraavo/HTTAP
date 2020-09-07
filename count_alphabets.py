import string
import re

def count(p):
    # your code here
    lletters = string.ascii_lowercase
    uletters = string.ascii_uppercase
    punctuation = string.punctuation

    print(lletters, uletters)
    ch = "e"
    letters = 0
    for x in p:
        if x in lletters or x in uletters:
            letters += 1
        if ch in lletters or ch in uletters:
            No_of_e = p.count("e")

            per_of_e = No_of_e / letters * 100
    print("Your text contains", letters, "alphabetic characters of which", No_of_e, "(", per_of_e, "%)", "are 'e'")


p = """For I am the first and the last
I am the venerated and the despised
I am the prostitute and the saint
I am the wife and the virgin
I am the mother and the daughter
I am the arms of my mother
I am the barren and my children are many
I am the married woman and the spinster
I am the woman who gives birth and she who never procreated
I am the consolation for the pain of birth
I am the wife and the husband
And it was my man who created me
I am the mother of my father
I am the sister of my husband
And he is my rejected son
Always respect me
For I am the shameful and the magnificent one.
Eleven Minutes
Hymn to Isis.
"""

count(p)





