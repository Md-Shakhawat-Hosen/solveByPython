t = int(input())
for i in range(t):
    li = list(map(int,input().split()))
    player1 = max(li[0],li[1])
    player2 = max(li[2],li[3])
    li.remove(player1)
    li.remove(player2)
    flag = 0
    for j in range(len(li)):
        if li[j] > player1 or li[j] > player2:
            flag = 1

    if flag == 1:
        print("NO")
    else:
        print("YES")