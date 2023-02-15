s = input()
count = 0
up = 0
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        count = count + 1
    else:
        up = up + 1

if up > count:
    print(s.upper())
else:
    print(s.lower())