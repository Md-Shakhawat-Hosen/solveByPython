t = int(input())
for i in range(t):
    n = int(input())
    h1 = (n+3) // 3
    r = (n+3) % 3
    h2 = h1 - 1
    h3 = h2 - 1
    if r:
        h1 += 1
        r -= 1
    if r:
        h2 +=1
    print(h2,h1,h3)