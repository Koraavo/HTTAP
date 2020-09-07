def replace(s, old, new):
    list1 = list(s)
    for i in range(len(list1)):
        if list1[i] == old:
            list1[i] = new
    return "".join(list1)

s = "Mississippi"
print(replace(s, "i", "I"))

# ('Mississippi', 'i', 'I'), 'MIssIssIppI'