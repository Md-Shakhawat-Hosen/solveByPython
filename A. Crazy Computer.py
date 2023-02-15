n,c = map(int,input().split())
li = list(map(int,input().split()))[:n]
li.reverse()
li2 = []
if len(li2) == 1:
    print(1)
elif len(li2) == 2:
    if li2[0] - li2[1] <= c:
        print(2)
    else:
        print(0)
else:
    index = 0
    for i in range(n - 1):
        if li[i] - li[i + 1] <= c:
            li2.append(i)
        else:
            index = 1
            li2.append(i)
            break


if index == 1:
    print(len(li2))
else:
    print(len(li))



