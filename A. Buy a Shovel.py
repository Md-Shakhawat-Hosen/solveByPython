a,b = map(int,input().split())
sum = 0
i = 1
while i > 0:
    sum = sum + a
    if sum % 10 == 0 or sum % 10 == b:
        print(i)
        break
    else:
        i = i + 1
        continue