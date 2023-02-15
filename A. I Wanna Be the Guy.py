n = int(input())
li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
unique = []

for i in range(1,len(li)):
    unique.append(li[i])

for i in range(1,len(li2)):
    unique.append(li2[i])

unique.sort()
new = set(unique)
if len(new) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

# for item in li:
#     if item not in unique:
#         unique.append(item)
# for item in li2:
#     if item not in unique:
#         unique.append(item)
#
# if len(unique) == n:
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")


