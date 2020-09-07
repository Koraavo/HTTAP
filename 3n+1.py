def seq3np1(i, j):
    # """ Print the 3n+1 sequence from n, terminating when it reaches 1."""

    maxSofar = 0
    count1 = []
    for start in range(i, j):
        count = 0
        print("the value of start is:", start, "\n")
        while start != 1:
            print(start)

            if start % 2 == 0:  # n is even
                start = start // 2
            else:  # n is odd
                start = start * 3 + 1
            count = count + 1
        count1.append(count)

        print("the count excluding 1 is", count, "\n")

        maxSofar = max(count1)
    print("the largest count is for number ", count1.index(max(count1))+1, "and the count is ", maxSofar)

    # print(start)                  # the last print is 1
    return count1


print(seq3np1(1, 51))

print ("--------------------------")

def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count += 1
    return count


maxSoFar = 0
for item in range(25, 28):
    if seq3np1(item)>= maxSoFar:
        maxSoFar = seq3np1(item)

print(maxSoFar)

