
n,m = map(int,input().split())
sum = 0
for i in range(1,n+1):
    sum = sum + i

if sum <= m:
    re = 0
    new = 0
    while re <= m:
        for i in range(1, n + 1):
            re = re + i
            if re == m:
                break
            elif re > m:
                new = i
                break

    result = re - new
    print(m - result)

else:
    count = 0
    a = 0
    for i in range(1,n+1):
         count = count + i
         if count <= m:
             continue
         else:
             a = i
             break
    total = count-a
    print(m-total)









