t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    odd = 0
    even = 0
    for i in range(n):
        if li[i] % 2 != 0:
            odd = odd + 1
        else:
            even = even + 1

    if odd == 0 or (even == 0 and n % 2 == 0):
        print("NO")
    else:
        print("YES")