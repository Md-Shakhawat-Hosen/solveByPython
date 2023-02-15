n = int(input())
sum = 0
m = 0
for i in range(n):
        a,b = map(int,input().split())
        sum = sum - a
        sum = sum + b
        if sum > m:
            m = sum

print(m)





