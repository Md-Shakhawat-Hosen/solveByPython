t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    index = 0
    for i in range(len(li)-1):
        if li[0] != li[1] and li[1] == li[2]:
            index = i+1
            break
        elif li[i] != li[i+1]:
            index = i+2
            break
    print(index)