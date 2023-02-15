t = int(input())
for i in range(t):
    n,d = map(int,input().split())
    li = list(map(int,input().split()))[:n]
    li1 = []
    li2 = []
    for i in range(n):
        if li[i] <= d:
            li1.append(li[i])
        else:
            li2.append(li[i])

    if len(li2) == 0:
        print("YES")
    else:
        li1.sort()
        if len(li1) >= 2:
            if li1[0] + li1[1] <= d:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")