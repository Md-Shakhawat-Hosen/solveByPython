a,b = map(int,input().split())
s_a = 1

m = min(a,b)
for i in range(2,m+1):
    s_a = s_a * i

print(s_a)