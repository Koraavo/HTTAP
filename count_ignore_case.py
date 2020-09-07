import string
import pprint
message = "It was a bright cold day in April, and the clock struck thirteen."
letter_count = {}
for characters in message.lower():
    if characters in string.ascii_lowercase:
        letter_count.setdefault(characters, 0)
        letter_count[characters] += 1

sorttext = pprint.pformat(letter_count)
print(sorttext)
# for keys in sorted(letter_count.keys()):
#     print(keys, letter_count[keys])
