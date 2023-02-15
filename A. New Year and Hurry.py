n,k = map(int,input().split())
total_time = 240
get_time = total_time - k
sum = 0
count = 0
for i in range(1,n+1):
    sum = sum + i*5
    if sum <= get_time:
        count = count + 1

print(count)