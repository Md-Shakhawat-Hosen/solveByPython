t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    even = 0
    odd = 0
    for i in range(n):
        if li[i] % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    # if even > odd:
    #     print(odd)
    # elif odd > even:
    #     print(even)
    # else:
    #     print(odd)
    print(min(even,odd))





