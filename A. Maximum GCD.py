t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            c = c + 1
    print(c)