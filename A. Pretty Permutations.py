t = int(input())
for i in range(t):
    n = int(input())
    li = []
    for i in range(1, n + 1):
        li.append(i)

    if n % 2 == 0:
        for i in range(0, n - 1, 2):
            li[i], li[i + 1] = li[i + 1], li[i]

        for item in li:
            print(item, end=" ")
        print()
    else:
        for i in range(0, n - 1, 2):
            li[i], li[i + 1] = li[i + 1], li[i]

        li[-1],li[-2] = li[-2],li[-1]
        for item in li:
            print(item, end=" ")
        print()


