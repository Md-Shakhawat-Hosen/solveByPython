t = int(input())
for i in range(t):
    inp_1 = input()
    word = input()
    li = []
    for i in range(len(word)):
        ind = inp_1.index(word[i])
        li.append(ind+1)

    if len(word) == li.count(li[0]):
        print(0)
    else:
        s = 0
        for i in range(len(li)-1):
            s = s + abs(li[i]-li[i+1])
        print(s)
