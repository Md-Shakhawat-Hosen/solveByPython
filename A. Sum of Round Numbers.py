t = int(input())

for i in range(t):
    n = int(input())
    li = []
    if n >= 1000:
        rem = n % 1000
        r = n - rem
        li.append(r)
        n %= 1000
    if n >= 100:
        rem = n % 100
        r = n - rem
        li.append(r)
        n %= 100

    if n >= 10:
        rem = n % 10
        r = n - rem
        li.append(r)
        n %= 10
    if n < 10 and n > 0:
        li.append(n)

    print(len(li))
    for i in li:
        print(i,end=" ")
    print()





