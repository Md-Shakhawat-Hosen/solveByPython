d1,d2,d3 = map(int,input().split())
t1 = 2*d1 + 2*d2
t2 = 2*d2 + 2*d3
t3 = 2*d1 + 2*d3
t4 = d1 + d2 + d3
result = min(t4,min(t3,min(t1,t2)))
print(result)
