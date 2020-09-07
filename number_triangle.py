"""
1
12
123
1234
12345
"""


def number_triangle(num):
    for row in range(1, num):
        for col in range(1, row + 1):
            print(col, end='')
        print()


number_triangle(11)
