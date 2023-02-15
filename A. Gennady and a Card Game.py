s = input()
li = list(map(str,input().split()))
l = list(s)
flag = 0
# for i in range(len(li)):
#     l1 = list(li[i])
#     for j in range(2):
#         for i in range(2):
#             if l[j] == l1[i]:
#                 print("YES")
#                 flag = 1
#                 break
#         if flag == 1:
#             break
#     if flag == 1:
#         break
#
# if flag == 0:
#     print("NO")
for i in range(len(li)):
    l1 = list(li[i])
    if l[0] == l1[0] or l[1] == l1[1]:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")

