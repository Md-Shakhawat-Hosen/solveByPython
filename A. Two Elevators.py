t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    e_1 = a - 1
    e_2 = abs(b-c) + (c-1)
    if e_1 == e_2:
        print(3)
    elif e_1 < e_2:
        print(1)
    else:
        print(2)




