# tL = int(input())
# for i in range(tL):
#     aL, bL = map(int, input().split())
#     c = 0
#
#     if bL > aL:
#         print(bL-aL)
#     else:
#         while aL != 0:
#             if aL % bL == 0:
#                 break
#             else:
#                 c = c + 1
#                 aL = aL + 1
#         print(c)

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a % b == 0:
        print(0)
    else:
        r = a % b
        print(b-r)