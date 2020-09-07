def insert(pos, obj, lst):
    new_list = []
    for i in range(len(lst)):
        if i == pos:
            new_list.append(obj)
            print(new_list)
        new_list.append(lst[i])
    return new_list


lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(insert(3, "j", lst))