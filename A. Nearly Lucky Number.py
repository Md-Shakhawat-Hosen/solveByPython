n = input()
li = list(map(int,n))
count1 = li.count(4)
count2 = li.count(7)
if count1+count2 == 4 or count1+count2 == 7:
    print("YES")
else:
    print("NO")

