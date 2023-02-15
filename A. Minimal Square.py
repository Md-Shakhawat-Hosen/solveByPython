t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a > b:
        t = b
        b = a
        a = t
    result = max(a*2,b)*max(a*2,b)
    print(result)