s1 = input()
s2 = input()
li = []
for i in range(len(s1)):
    if s1[i] == '0' and s2[i] == '0':
        li.append(0)
    elif s1[i] == '1' and s2[i] == '1':
        li.append(0)
    elif (s1[i] == '0' and s2[i] == '1') or (s1[i] == '1' and s2[i] == '0'):
        li.append(1)

for i in li:
    print(i,end="")
