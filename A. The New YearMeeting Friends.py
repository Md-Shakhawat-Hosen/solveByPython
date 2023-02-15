a,b,c = map(int,input().split())
li = [a,b,c]
li.sort()
second_largest = li[1]
total_distance = abs(a-second_largest) + abs(b-second_largest) + abs(c-second_largest)
print(total_distance)
