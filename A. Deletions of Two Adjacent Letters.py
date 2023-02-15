t = int(input())
for i in range(t):
    s = input()
    ch = input()
    if ch not in s:
        print("NO")
    else:
        flag = False
        for i in range(len(s)):
            if ch == s[i]:
                ind = i+1
                if ind % 2 == 1:
                    flag = True
                    break
            else:
                flag = False
        if flag:
            print("YES")
        else:
            print("NO")
