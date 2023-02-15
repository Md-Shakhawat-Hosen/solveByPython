n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)

c = 1
for i in range(len(li)-1):
    if li[i] != li[i+1]:
        c = c + 1

print(c)
