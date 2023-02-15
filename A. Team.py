n = int(input())
sum = 0
for x in range(n):
    p,v,t = map(int,input().split())
    if p + v + t >= 2:
        sum = sum + 1

print(sum)