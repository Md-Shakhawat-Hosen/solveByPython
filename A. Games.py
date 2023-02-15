n = int(input())
li = []
li2 = []
for i in range(n):
    a,b = map(int,input().split())
    li.append(a)
    li2.append(b)

c = 0
for i in range(n):
    for j in range(n):
        if li[i] == li2[j]:
            c += 1

print(c)