n,m,z = map(int,input().split())
kill = 0
li = []
li2 = []
i = n
j = m
for i in range(i,z+1,n):
    li.append(i)
for j in range(j,z+1,m):
    li2.append(j)

common_list = [c for c in li if c in li2]
print(len(common_list))





