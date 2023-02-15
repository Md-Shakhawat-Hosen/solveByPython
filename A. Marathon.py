t = int(input())
for i in range(t):
    li = list(map(int,input().split()))
    timur = li[0]
    c = 0
    for i in range(len(li)):
        if li[i] > timur:
            c = c + 1
    print(c)