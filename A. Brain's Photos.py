n,m = map(int,input().split())
li = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(input())
    li.append(a)


flag = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == 'W' or li[i][j] == 'B' or li[i][j] == 'G':
            flag = 1
            break
        else:
            continue
if flag == 1:
    print("#Black&White")
else:
    print("#Color")

