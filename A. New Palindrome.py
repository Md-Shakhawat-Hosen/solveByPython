t = int(input())
for i in range(t):
    s = input()
    li = list(s)
    num = 0
    if len(s) % 2 == 0 and len(s) > 2:
        for i in range(1,len(s)//2):
            if s[i] != s[i-1]:
                num = num + 1
                break
    elif len(s) % 2 != 0 and len(s) > 3:
        for i in range(1,len(s)//2):
            if s[i] != s[i-1]:
                num = num + 1
                break
    if num:
        print("YES")
    else:
        print("NO")



