n,m = map(int,input().split())
if m > n:
    f = 1
    for i in range(1,m//2+1):
        if m % i == 0:
            f = f + 1
    if f == 2:
        flag = 0
        for j in range(n+1,m+1):
            c = 1
            for k in range(1,n+1//2+1):
                if j % k == 0:
                    c = c + 1
            if c == 2:
                flag = flag + 1
        if flag == 1:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")
else:
    print("NO")