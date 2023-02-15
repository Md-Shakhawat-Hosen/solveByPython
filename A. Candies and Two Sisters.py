import math
T = int(input())
for x in range(T):
    n = int(input())
    if n > 2:
        result = (n / 2) - 1
        print(math.ceil(result))
    else:
        print(0)
