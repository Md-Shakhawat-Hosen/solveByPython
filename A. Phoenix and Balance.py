t = int(input())
for i in range(t):
    n = int(input())
    li = []
    m = 1
    for j in range(n):
        m = 2*m
        li.append(m)

    first_pile = li[-1]
    for i in range(n//2-1):
        first_pile = first_pile + li[i]

    second_pile = 0
    for i in range(n//2-1,n-1):
        second_pile = second_pile + li[i]
    print(first_pile-second_pile)

