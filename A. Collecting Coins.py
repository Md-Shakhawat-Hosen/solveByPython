t = int(input())
for i in range(t):
    li = list(map(int,input().split()))
    polycarp_coin = li[-1]
    li2 = []
    a = li[0]
    li2.append(a)
    b = li[1]
    li2.append(b)
    c = li[2]
    li2.append(c)
    li2.sort()
    li2.reverse()

    r1 = li2[0]-li2[1]
    r2 = li2[0] - li2[2]
    total = r1 + r2
    coin_has = polycarp_coin - total
    if coin_has < 0:
        print("NO")
    elif coin_has == 0 or coin_has % 3 == 0:
        print("YES")
    else:
        print("NO")

