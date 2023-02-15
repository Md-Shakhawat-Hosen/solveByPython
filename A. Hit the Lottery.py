n = int(input())
c = 0
while n != 0:
    if n >= 100:
        r = n // 100
        c = c + r
        n = n % 100
    elif n >= 20 and n < 100:
        r = n // 20
        c = c + r
        n = n % 20
    elif n >= 10 and n < 20:
        r = n // 10
        c = c + r
        n = n % 10
    elif n >= 5 and n < 10:
        r = n // 5
        c = c + r
        n = n % 5

    elif n >= 1 and n < 5:
        c = c + n
        break
print(c)


