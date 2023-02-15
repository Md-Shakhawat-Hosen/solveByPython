n = int(input())
li = list(map(int,input().split()))[:n-1]
a,b = map(int,input().split())
result = 0
for i in range(a-1,b-1):
     result = result + li[i]
print(result)
