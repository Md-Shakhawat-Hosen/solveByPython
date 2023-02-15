t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if a == b == c:
        print(a+1,b+1,c+1)
    else:
        max_value = max(a,b,c)
        a = abs(max_value-a)
        b = abs(max_value-b)
        c = abs(max_value-c)
        if a == 0 and b != 0 and c != 0:
            print(a,b+1,c+1)
        elif a != 0 and b == 0 and c != 0:
            print(a+1,b,c+1)
        else:
            print(a+1,b+1,c)


