s = input()
n = len(s)
a = 0
for i in s:
    if i == 'a':
        a= a + 1

if a <= int(n/2):
    while a <= int(n/2):
        n = n - 1

print(n)

