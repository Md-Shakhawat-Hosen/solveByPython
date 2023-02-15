a,b,n = map(int,input().split())
while n > 0:
    for i in range(1, a + 1):
        if a % i == 0 and n % i == 0:
            gcd_simon = i

    n = n - gcd_simon
    for i in range(1, b + 1):
        if b % i == 0 and n % i == 0:
            gcd_antisimon = i
    n = n - gcd_antisimon
if n == 0:
    print(1)
else:
    print(0)

