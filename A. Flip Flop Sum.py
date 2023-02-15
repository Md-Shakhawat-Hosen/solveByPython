t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    p_one = li.count(1)
    n_one = li.count(-1)
    if n == 2:
        if li[0] == li[1] == 1:
            print(-2)
        elif li[0] == li[1] == -1:
            print(2)
        else:
            print(sum(li))
    elif n_one >= 2:
        for i in range(n-1):
            if li[i] == li[i+1] == -1:
                li[i] = 1
                li[i+1] = 1
                break
        print(sum(li))
    else:
        for i in range(n-1):
            if li[i] == li[i+1] == 1:
                li[i] = -1
                li[i+1] = -1
                break
        print(sum(li))






