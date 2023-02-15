t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    s = 0
    i = 1
    while s < n:
        c = c + 1
        s = s + i
        i = i + 2
    print(c)