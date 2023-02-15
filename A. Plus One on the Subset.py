t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    max_value = max(li)
    min_value = min(li)
    print(max_value-min_value)