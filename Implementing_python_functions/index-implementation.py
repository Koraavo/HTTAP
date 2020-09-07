def index(obj, lst):
    index_number = 0
    for i in lst:
        print(i)
        if i == obj:
            break
        else:
            index_number +=1
    return index_number

print(index("True", ['love', 'lace', 'regards', 'True', 'love']))