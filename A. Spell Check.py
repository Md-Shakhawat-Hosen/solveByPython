t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if n > 5:
        print("NO")
    else:
        c = 0
        s = set(s)
        s = list(s)
        if len(s) != 5:
            print("NO")
        else:
            for i in range(len(s)):
                if s[i] == 'T':
                    c = c + 1
                elif s[i] == 'i':
                    c = c + 1
                elif s[i] == 'm':
                    c = c + 1
                elif s[i] == 'u':
                    c = c + 1
                elif s[i] == 'r':
                    c = c + 1
            if c == 5:
                print("YES")
            else:
                print("NO")
