t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(2)
    elif n % 3 != 0:
        print(n//3+1)
    else:
        print(n//3)
