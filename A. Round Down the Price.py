t = int(input())
for i in range(t):
    n = int(input())
    if n <= 9:
        r = n - 1
        print(r)
    else:
        n = str(n)
        li = list(n)
        r = len(li)-1
        p = pow(10,r)
        print(int(n)-p)