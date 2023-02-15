n = int(input())
s = input()
a = 0
d = 0
for x in s:
    if x == 'A':
        a = a + 1
    elif x == 'D':
        d = d + 1
if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")