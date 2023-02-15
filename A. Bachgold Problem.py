# n = int(input())
# li = []
#
# for i in range(2,n):
#     f = 1
#     for j in range(1,i):
#         if i % j == 0:
#             f = f + 1
#     if f == 2:
#         li.append(i)
# li2 = []
# for i in range(len(li)):
#     for j in range(i,len(li)):
#         s = li[i] + li[j]
#         if s == n:
#             li2.append(li[i])
#             li2.append(li[j])
#             break
# if n % 2 == 0:
#     t = n // 2
#     if t % 2 == 0:
#         print(len(li2))
#         for i in li2:
#             print(i, end=" ")
#     else:
#         print(t)
#         for i in range(t):
#             print(2,"",end="")
# elif len(li2) == 0:
#     print(1)
#     print(n)
# else:
#     print(len(li2))
#     for i in li2:
#         print(i,end=" ")

n = int(input())
if n % 2 == 0:
    ans = n // 2
    print(ans)
    for i in range(ans):
        print(2,'',end="")
elif n == 3:
    print(1)
    print(3)
else:
    n = n - 3
    ans = n // 2
    print(ans+1)
    for i in range(ans):
        print(2,'',end="")
    print(3)
