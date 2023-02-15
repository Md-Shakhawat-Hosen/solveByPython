n = int(input())
li = list(map(int,input().split()))[:n]
h = max(li)
sum = 0
for i in li:
    t = h - i
    sum = sum + t
print(sum)