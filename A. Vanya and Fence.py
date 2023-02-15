n,h = map(int,input().split())
li = list(map(int,input().split()))[:n]
sum = 0
for x in li:
    if x <= h:
        sum = sum + 1
    else:
        sum = sum + 2
print(sum)