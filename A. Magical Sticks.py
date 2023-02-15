t = int(input())
for i in range(t):
    n = int(input())
    a = n // 2
    if n % 2 != 0:
        a = a + 1

    print(a)