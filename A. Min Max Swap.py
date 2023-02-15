t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    for i in range(n):
        if a[i] < b[i]:
            a[i],b[i] = b[i],a[i]

    print(max(a)*max(b))
