t = int(input())
for i in range(t):
    n = int(input())
    li = str(n)
    li1 = list(map(int,li))
    l = len(li1) // 2
    if 1 <= n <= 9:
        if n % 2 == 0:
            print(0)
        else:
            print(-1)
    else:
        if n % 2 == 0:
            print(0)
        elif li1[0] % 2 == 0:
            print(1)
        else:
            flag = False
            for i in range(len(li1)):
                if li1[i] % 2 == 0:
                    flag = True
                    break
            if flag:
                print(2)
            else:
                print(-1)

