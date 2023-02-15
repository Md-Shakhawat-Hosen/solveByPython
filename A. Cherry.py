t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    s = 0
    for i in range(n - 1):
        if li[i] * li[i + 1] > s:
            s = li[i] * li[i + 1]

    print(s)


