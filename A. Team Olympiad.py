n = int(input())
li = list(map(int,input().split()))[:n]
one = li.count(1)
two = li.count(2)
three = li.count(3)
c = 0
while one > 0 and two > 0 and three > 0:
    c = c + 1
    one -= 1
    two -= 1
    three -= 1




