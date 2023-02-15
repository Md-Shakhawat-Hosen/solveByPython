# import sys
#
# R = 0
# for line in sys.stdin:
# 	A = int(line)
# 	if A == 0:
# 		break
# 	R += A
# print(R)
# a = input()
# print(a)
# a=a.strip(',')
# print(a)
# b=list(a)
# print(b)
# b.sort()
# print(b)
# new = set(b)
# print(new)
# c=0
# for i in range(len(b)):
# 	if(b[i]!='{' and b[i]!='}' and b[i]!=',' and b[i]!=' '):
# 		if (b[i]!=b[i-1]):
# 			c+=1
# print(c)

# s = input().strip()
# print(s)
# li = list(s)
# print(li)
# li.sort()
# print(li)
# c = 0
# for i in range(len(li)):
# 	if li[i] != '{' and li[i] != '}' and li[i] != ',' and li[i] != ' ':
# 		if li[i] != li[i-1]:
# 			c = c + 1
# print(c)

s = input()
li = set(s)
n = list(li)
c = 0
for i in range(len(li)):
	if n[i] >= 'a' and n[i] <= 'z':
		c = c+1
print(c)

