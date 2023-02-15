t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:2*n]
    c = 0
    for i in range(2*n):
        if li[i] % 2 != 0:
            c = c + 1
    if c == n:
        print("YES")
    else:
        print("NO")
    # if n == 1:
    #     s = sum(li)
    #     if s % 2 == 1:
    #         print("YES")
    #     else:
    #         print("NO")
    # else:
    #     while n > 0:
    #         s = li[0] + li[1]
    #         if s % 2 == 1:
    #             c = c + 1
    #             li.remove(li[0])
    #             li.remove(li[1])
    #             n = n - 1
    #         else:
    #             break
    #     if c == n:
    #         print("YES")
    #     else:
    #         print("NO")

