n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
       if i % 2 != 0:
           print("#",end="")
       elif i % 4 == 0:
           if j == 1:
               print("#",end="")
           else:
               print(".",end="")
       elif i % 4 == 2:
           if j == m:
               print("#",end="")
           else:
               print(".",end="")

    print()


