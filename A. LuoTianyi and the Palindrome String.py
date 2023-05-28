t = int(input())
for i in range(t):
    s = input()
    li = list(set(s))
    if len(li) == 1:
        print(-1)
    else:
        print(len(s)-1)