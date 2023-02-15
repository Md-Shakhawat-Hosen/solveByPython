t = int(input())
for i in range(t):
    a,b,c,x,y = map(int,input().split())
    if a+c >= x and b+c >= y and a+b+c >= x+y:
        print("YES")
    else:
        print("NO")
