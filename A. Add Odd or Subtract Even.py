t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = 1
    d = 0
    if a == b:
        print(0)
        continue
    elif a > b:
        d = a - b
        if d % 2 == 1:
            c = c + 1
    elif a < b:
        d = b - a
        if d % 2 == 0:
            c = c + 1

    print(c)
