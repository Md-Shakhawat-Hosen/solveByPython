t = int(input())
for i in range(t):
    n = int(input())
    for i in range(2,n+1):
        for j in range(n,2,-1):
            r = n % i
            r1 = n % j
            if r == r1 and i < j:
                print(i,j)
                break
        break

