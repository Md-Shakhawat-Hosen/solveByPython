t = int(input())
li = []
for i in range(t):
    li.append(input().split('|'))


flag = False
for i in range(t):
    for j in range(2):
        if li[i][j] == 'OO':
            li[i][j] = '++'
            flag = True
            break
    if flag:
        break


if flag:
    print("YES")
    for i in range(t):
        for j in range(1):
            print(li[i][j] + '|' + li[i][j + 1])
else:
    print("NO")




