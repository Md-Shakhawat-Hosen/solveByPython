t = int(input())
for i in range(t):
    n = int(input())
    s = input()[:n]
    li = []
    if len(s) == 1:
        if s[0] == 'U':
            print('D')
        elif s[0] == 'D':
            print('U')
        elif s[0] == 'L':
            print("R")
        elif s[0] == 'R':
            print('L')
    else:
        for i in range(len(s)):
            if s[i] == 'U':
                li.append('D')
            elif s[i] == 'D':
                li.append('U')
            elif s[i] == 'L':
                li.append('L')
            elif s[i] == 'R':
                li.append('R')
        for item in li:
            print(item, end="")
        print()


