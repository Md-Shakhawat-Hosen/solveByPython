t = int(input())
for i in range(t):
    r,b,d = map(int,input().split())
    diff = abs(r-b)
    m = min(r,b)
    result = (diff+m-1) // m
    if result <= d:
        print("YES")
    else:
        print("NO")
