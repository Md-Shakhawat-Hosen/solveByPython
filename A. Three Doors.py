t = int(input())
for i in range(t):
    x = int(input())
    a,b,c = map(int,input().split())
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    c = 0
    for i in range(len(li)-1):
        if li[x-1] == 0:
            c = 1
            break
        x = li[x-1]
    if c == 0:
        print("YES")
    else:
        print("NO")