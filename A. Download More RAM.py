# t = int(input())
# for i in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))[:n]
#     b = list(map(int, input().split()))[:n]
#     for i in range(n):
#         if a[i] > k:
#             break
#         k = k + b[i]
#     print(k)

t = int(input())
for i in range(t):
    s = input()
    li = list(s)
    li.sort()
    for i in li:
        print(i,end="")
    print()

