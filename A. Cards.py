n = int(input())
s = input()
li = list(s)
one = li.count('n')
z = li.count('z')
li1 = []
if one != 0:
    for i in range(one):
        li1.append(1)
if z != 0:
    for i in range(z):
        li1.append(0)


for item in li1:
    print(item,end=" ")

