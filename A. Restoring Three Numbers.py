li = list(map(int,input().split()))[:4]
li.sort()
c = li[3] - li[0]
b = li[2] - c
a = li[3] - (b+c)
print(a," ",b," ",c)