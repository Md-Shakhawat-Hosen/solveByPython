
# T = int(input())
# for x in range(T):
#     n = int(input())
#     sum = 0
#     for i in range(1, int(n / 2) + 1):
#         if n % i == 0:
#             sum = sum + i
#     print(sum)


T = int(input())
for x in range(T):
    a,b,c = map(int,input().split())
    max_value = max(a,b,c)
    total = a + b + c
    if (total - max_value) == max_value:
        print("YES")
    else:
        print("NO")








