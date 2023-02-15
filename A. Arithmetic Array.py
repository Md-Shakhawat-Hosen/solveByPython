t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    total_sum = sum(li)
    if total_sum == n:
        print(0)
    else:
        if total_sum <= 0 or total_sum < n:
            print(1)
        else:
            r = total_sum - n
            print(r)