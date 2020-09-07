def reverse(lst):
    return lst[::-1]

print(reverse(['love', 'lace', 'regards', 'True', 'love']))

def reverse(lst):
    reversed = []
    for i in range(len(lst)-1, -1, -1): # step through the original list backwards
        reversed.append(lst[i])
    return reversed