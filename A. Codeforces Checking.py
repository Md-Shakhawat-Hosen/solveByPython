t = int(input())
for i in range(t):
    ch = input()
    s = 'codeforces'
    flag = False
    for i in range(len(s)):
        if s[i] == ch:
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")