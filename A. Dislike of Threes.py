t = int(input())
for i in range(t):
    n = int(input())
    li = []
    j = 1
    while j <= 2000:
        if j % 3 != 0 and j % 10 != 3:
            li.append(j)
            j = j + 1
        else:
            j = j + 1
    print(li[n-1])