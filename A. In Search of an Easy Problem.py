n = int(input())
li = list(map(int,input().split()))[:n]
h = li.count(1)

if h >= 1:
    print("HARD")
else:
    print("EASY")