t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    if x != y and x != z and y != z:
        print("NO")
    elif x == y == z:
        print("YES")
        print(x,y,z)
    else:
        m = max(x,y,z)
        mi = min(x,y,z)
        li = []
        li.append(x)
        li.append(y)
        li.append(z)
        c = li.count(m)
        if c >= 2:
            print("YES")
            print(1,mi,m)
        else:
            print("NO")
