t = int(input())
for i in range(t):
    s = input()
    li = []
    i = 1
    while i < len(s)-1:
        if s[i] == s[i+1]:
            li.append(s[i+1])
            i = i + 2
    li.insert(0,s[0])
    li.append(s[-1])
    for i in li:
        print(i,end="")
    print()

