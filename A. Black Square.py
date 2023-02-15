a1,a2,a3,a4 = map(int,input().split())
s = input()
li = list(map(int,s))
c1 = li.count(1)
c2 = li.count(2)
c3 = li.count(3)
c4 = li.count(4)
result = a1*c1 + a2*c2 + a3*c3 + a4*c4
print(result)