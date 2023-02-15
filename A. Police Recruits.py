n = int(input())
li = list(map(int,input().split()))[:n]
hired = untreated = 0
for item in li:
    if item > 0:
        hired += item
    elif hired > 0 and item < 0:
        hired -= 1
    elif item < 0:
        untreated += 1

print(untreated)


