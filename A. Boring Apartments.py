t = int(input())
for i in range(t):
    s = input()
    sum = 0
    if s[0] == '1':
        for i in range(1,len(s)+1):
            sum = sum + i
        print(sum)
    else:
        re = int(s[0])
        for i in range(1,len(s)+1):
            sum = sum + i
        print((re-1)*10 +sum)