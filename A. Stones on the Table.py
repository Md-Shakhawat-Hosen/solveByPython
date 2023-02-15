n = int(input())
s = input()[:n]
li = list(s)
count = 0
for i in range(len(li)-1):
    if li[i] == li[i+1]:
        count = count + 1

print(count)