n = int(input())
s = input()[:n]
t = s.lower()
unique = []
for i in t:
    if i not in unique:
        unique.append(i)

if len(unique) == 26:
    print("YES")
else:
    print("NO")

