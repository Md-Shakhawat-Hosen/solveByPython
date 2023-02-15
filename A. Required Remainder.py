t = int(input())
for i in range(t):
    x,y,n = map(int,input().split())
    ans = n - n % x + y
    if ans <= n:
        print(ans)
    else:
        result = ((n - n % x) - (x - y))
        print(result)
