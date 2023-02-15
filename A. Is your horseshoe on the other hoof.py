s1,s2,s3,s4 = map(int,input().split())
li = []
li.append(s1)
li.append(s2)
li.append(s3)
li.append(s4)
new = set(li)
if len(li) == len(new):
    print(0)
else:
    print(len(li)-len(new))