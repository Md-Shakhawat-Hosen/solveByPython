T = int(input())
for x in range(T):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if li[0] == 1:
        print("YES")
    else:
        print("NO")