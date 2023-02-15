n = int(input())
m = 0
c = 0
for i in range(n):
    a,b = map(int,input().split())
    if a > b:
        m = m + 1
    elif a < b:
        c = c + 1
    else:
        m = m + 1
        c = c + 1

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")
