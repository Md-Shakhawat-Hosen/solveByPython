s = input()
li = []
for i in range(len(s)):
    if s[i] != '+':
        li.append(s[i])

li.sort()
new = []
for i in li:
    new.append(i)
    new.append('+')

for i in range(len(new)-1):
    print(new[i],end="")


