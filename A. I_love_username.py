n = int(input())
li = list(map(int,input().split()))[:n]
max = li[0]
min = li[0]
c = 0
for i in range(1,n):
    if li[i] > max:
        max = li[i]
        c += 1
    elif li[i] < min:
        min = li[i]
        c += 1
print(c)



