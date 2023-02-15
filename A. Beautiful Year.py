n = int(input())
j = n
while n != 0:
    l = str(n)
    li = list(map(int,l))
    new = set(li)
    if len(li) == len(new) and n > j:
        for i in li:
            print(i,end="")
        break
    else:
        n = n + 1