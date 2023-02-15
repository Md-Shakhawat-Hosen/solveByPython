t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    li = list(s)
    li2 = []
    j = 0
    while j < len(li)-1:
        if li[j] != li[j+1]:
            li2.append(li[j])
            j = j + 1
        else:
            j = j + 1
    li2.append(li[-1])
    flag = 0
    for i in range(len(li2)):
        for j in range(i+1,len(li2)):
            if li2[i] == li2[j]:
                flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")


