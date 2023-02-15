t = int(input())
for i in range(t):
    n = int(input())
    d = int(n/3)
    re = n % 3
    c1 = d
    c2 = d
    if re == 1:
        c1 = c1 + 1
    elif re == 2:
        c2 = c2 + 1

    print(c1,c2)
