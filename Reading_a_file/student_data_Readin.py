
with open("studentdata.txt", "r") as sd:
    check = [aline.split() for aline in sd]
    print(check)
    score_list = [elements[1:] for elements in check]
    print(score_list)
    int_list = [[int(i) for i in elements] for elements in score_list]
    print(int_list)
    avg = [(sum(int_list[i])/len(int_list[i])) for i in range(len(int_list))]
    print(avg)
    names_list = [elements[0] for elements in check]
    max_score = [max(int_list[i]) for i in range(len(int_list))]
    for i in range(len(names_list)):
        print(names_list[i], avg[i])
        print(names_list[i], max_score[i])


# f = open ('studentdata.txt', 'r')
# for aline in f:
#     items = aline.split()
#     total = 0
#     grades = items[1:]
#     print(grades)
#     for grade in grades:
#         total = total + int(grade)
#     print(items[0], (total/(len(grades))))
# f.close()