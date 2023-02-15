T = int(input())
for x in range(T):
    n = int(input())
    if n == 1:
        print(0)
        continue

    count = 0
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
            count = count + 1
        elif n % 3 == 0:
            n = int((2*n)/3)
            count = count + 1
        elif n % 5 == 0:
            n = int((4*n)/5)
            count = count + 1
        elif (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
            if n != 1:
                print(-1)
                break
        if n == 1:
            print(count)
            break

