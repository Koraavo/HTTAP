import random

def sumUntilEven(lst):
    sum = 0
    new_list = []
    for i in lst:
        if i % 2 == 0:
            break
        new_list.append(i)
    print(new_list)
    for i in new_list:
        sum += i
    return sum

lst = []
for i in range(100):
    lst.append(random.randint(0,1000))
print(lst)

print(sumUntilEven(lst))
