T = int(input())
for x in range(T):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li.sort()
    li.reverse()
    result = True
    for i in range(n-1):
        if li[i] - li[i+1] > 1:
            result = False
            break

    if result == True:
        print("YES")
    else:
        print("NO")




