n = int(input())

if n % 2 == 1:
    print(-1)
else:
    li = []
    li2 = []
    for i in range(2,n+1,2):
        li.append(i)
    for j in range(1,n+1,2):
        li2.append(j)

    li3 = []
    for i in range(n // 2):
        li3.append(li[i])
        li3.append(li2[i])
    for item in li3:
        print(item, end=" ")


