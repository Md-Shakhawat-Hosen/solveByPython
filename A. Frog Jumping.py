t = int(input())
for i in range(t):
    a,b,k = map(int,input().split())
    if k % 2 == 0:
            r = k//2
            total_a = r*a
            total_b = r*b
            print(total_a-total_b)

    else:
            r = k // 2
            t1_b = r*b
            t2 = k - r
            t2_a = t2*a
            if a > b:
                print(t2_a-t1_b)
            else:
                print(t2_a-t1_b)


