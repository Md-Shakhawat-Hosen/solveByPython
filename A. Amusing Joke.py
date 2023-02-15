s1 = input()
s2 = input()
s3 = input()
new_s = s1 + s2
li = list(new_s)
li.sort()
li1 = list(s3)
li1.sort()

if li == li1:
    print("YES")
else:
    print("NO")



