t = int(input())
for i in range(t):
    s = input()
    if len(s) % 2 == 1:
        print("NO")
    else:
        flag = 0
        d = len(s) // 2
        for j in range(len(s)-d):
            if s[j] == s[d]:
                d = d + 1
            else:
                flag = 1
                break
        if flag == 1:
            print("NO")
        else:
            print("YES")