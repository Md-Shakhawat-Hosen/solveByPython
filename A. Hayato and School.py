t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li2 = []
    if n == 3:
        s = sum(li)
        if s % 2 == 1:
            print("YES")
            print(1,2,3)
        else:
            print("NO")
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = li[i] + li[j] + li[k]
                    if s % 2 == 1:
                        li2.append(i + 1)
                        li2.append(j + 1)
                        li2.append(k+1)
                        break

        if len(li2) == 0:
            print("NO")
        else:
            print("YES")
            c = 0
            for item in li2:
                c = c + 1
                print(item,end=" ")
                if c == 3:
                    break
            print()



