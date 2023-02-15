t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if n == 1:
        print(li[0])
    else:
        if n % 2 == 0:
            li2 = []
            li3 = []
            li4 = []
            for i in range(n // 2):
                li2.append(li[i])
            for i in range(n // 2, n):
                li3.append(li[i])
            li3.reverse()
            for i in range(n // 2):
                li4.append(li2[i])
                li4.append(li3[i])
            for item in li4:
                print(item, end=" ")
            print()
        else:
            li2 = []
            li3 = []
            li4 = []
            for i in range(n // 2):
                li2.append(li[i])
            for i in range((n // 2) + 1, n):
                li3.append(li[i])
            li3.reverse()
            for i in range(n // 2):
                li4.append(li2[i])
                li4.append(li3[i])
            for item in li4:
                print(item, end=" ")
            print(li[n // 2])

