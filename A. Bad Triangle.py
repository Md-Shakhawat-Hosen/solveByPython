t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li1 = []
    flag = True
    i = 0
    while i+2 < n:
        if li[i]+li[i+1] <= li[n-1]:
            print(i+1,i+2,n)
            flag = False
            break
        i = i + 1
    if flag:
        print(-1)


