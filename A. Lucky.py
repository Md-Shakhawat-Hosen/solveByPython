t = int(input())
for i in range(t):
    s = input()
    li = list(map(int,s))
    c = 0
    last = 0
    for i in range(3):
        c = c + li[i]

    for j in range(3,len(li)):
        last = last + li[j]

    if c == last:
        print("YES")
    else:
        print("NO")


