n = int(input())
li = list(map(int,input().split()))[:n]
c = 1
m = 1
for i in range(n-1):
    if li[i+1] > li[i]:
        c += 1
    else:
        if c > m:
            m = c
        c = 1
if c > m:
    m = c
print(m)
