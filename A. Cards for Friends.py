t = int(input())
for i in range(t):
    w,h,n = map(int,input().split())
    c = 1
    while w % 2 == 0:
        c = c * 2
        w //= 2
    while h % 2 == 0:
        c = c * 2
        h //= 2
    if c >= n:
        print("YES")
    else:
        print("NO")
    # if w % 2 == 0 and h % 2 == 0:
    #     c = 1
    #     while w % 2 == 0:
    #         c = c * 2
    #         w = w // 2
    #     while h % 2 == 0:
    #         c = c * 2
    #         h = h // 2
    #     if c >= n:
    #         print("YES")
    #     else:
    #         print("NO")
    # elif w % 2 == 0 or h % 2 == 0:
    #     if w % 2 == 0:
    #         c = 1
    #         while w % 2 == 0:
    #             c = c * 2
    #             w = w // 2
    #         if c >= n:
    #             print("YES")
    #         else:
    #             print("NO")
    #     else:
    #         c = 1
    #         while h % 2 == 0:
    #             c = c * 2
    #             h = h // 2
    #         if c >= n:
    #             print("YES")
    #         else:
    #             print("NO")
    # elif w % 2 == 1 and h % 2 == 1:
    #     if n == 1:
    #         print("YES")
    #     else:
    #         print("NO")