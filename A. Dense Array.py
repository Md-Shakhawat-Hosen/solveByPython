t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    c = 0
    for i in range(n-1):
        if max(li[i],li[i+1]) // min(li[i],li[i+1]) >= 2:
            max_value = max(li[i],li[i+1])
            min_value = min(li[i],li[i+1])
            while max_value > 2 * min_value:
                min_value = 2 * min_value
                c = c + 1
    print(c)