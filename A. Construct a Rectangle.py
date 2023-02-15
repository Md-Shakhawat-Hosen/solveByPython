t = int(input())
for i in range(t):
    li = list(map(int,input().split()))
    li.sort()
    m = li[-1]
    if li[0] % 2 == 0 or li[1] % 2 == 0:
        if li[0] == 2 or li[1] == 2:
            print("YES")
        elif (li[0] // 2 == 2 or li[1] // 2 == 2) or (li[0]+li[1] == m):
            print("YES")
        else:
            print("NO")
    elif li[0]+li[1] == m:
        print("YES")
    else:
        print("NO")
