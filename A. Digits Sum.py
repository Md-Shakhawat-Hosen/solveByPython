t = int(input())
for i in range(t):
    n = int(input())
    if n == 9:
        print(1)
    elif n >= 1 and n <= 8:
        print(0)
    else:
        div = n // 10
        rem = n % 10
        if rem == 9:
            print(div+1)
        else:
            print(div)
