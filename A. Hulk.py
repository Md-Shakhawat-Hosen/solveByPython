n = int(input())
if n % 2 == 0:
    s = "I hate that I love that "
    re = int(n/2)
    new = s * re
    li = list(new.split())
    li[-1] = 'it'
    for i in li:
        print(i, end=" ")
else:
    re = int(n/2)
    s = "I hate that I love that "
    new = s * re
    s1 = "I hate that"
    li1 = list(s1.split())
    li = list(new.split())
    for i in li1:
        li.append(i)
    li[-1] = 'it'
    for i in li:
        print(i, end=" ")

