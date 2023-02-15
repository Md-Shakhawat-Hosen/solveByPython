t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if li[0] == li[n-1]:
        print("NO")
    else:
        print("YES")
        print(li[0],end=" ")
        for i in range(n-1,0,-1):
            print(li[i],end=" ")
        print()