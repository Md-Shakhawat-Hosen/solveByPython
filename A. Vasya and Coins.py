t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a == 0:
        print(1)
    else:
        burle_1 = a
        burle_2 = 2 * b
        print(burle_1+burle_2+1)