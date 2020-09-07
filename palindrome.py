import string


def removeWhite(s):
    # remove any kind of spaces and punctuation
    for element in string.punctuation:
        if element in s:
            new_s = s.replace(element, ' ')
            list = new_s.lower().split()
            s = ''.join(list)
            return s
    return s


def is_palindrome(s):
    reverse = s[::-1]
    return s == reverse


is_palindrome("baab")
is_palindrome("baar")


def remove_dups(astring):
    # your code here
    temp = ''   # create a new string
    for i in astring:
        if i not in temp: # check if the letter is added to temp
            temp += i # if not temp + i
    return temp


remove_dups("mississippi")   #should print misp