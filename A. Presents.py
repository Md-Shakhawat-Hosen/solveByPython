n = int(input())
li = list(map(int,input().split()))[:n]
for j in range(1,n+1):
    for i in range(n):
        if li[i] == j:
            print(i+1,end=" ")


