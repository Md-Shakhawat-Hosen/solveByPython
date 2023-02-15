n = int(input())
li = list(map(int,input().split()))[:n]
s = 0
d = 0
z = 0
l = 0
r = len(li)-1
while l <= r:
    if z % 2 == 0:
        z = z + 1
        if li[l] > li[r]:
            s += li[l]
            l = l + 1
        else:
            s += li[r]
            r = r - 1
    else:
        z = z + 1
        if li[l] > li[r]:
            d += li[l]
            l = l + 1
        else:
            d += li[r]
            r = r-1

print(s,d)


