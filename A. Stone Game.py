t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if n > 4:
        half = n // 2
        min_value = min(li)
        max_value = max(li)
        min_index = li.index(min_value)
        max_index = li.index(max_value)
        if min_index < half and max_index < half:
            if min_index < max_index:
                print(max_index+1)
            else:
                print(min_index+1)
        elif min_index > half and max_index > half:
            if max_index < min_index:
                c = 0
                for i in range(max_index,1,-1):
                    c = c + 1
                print(c)
            else:
                c = 0
                for i in range(min_index, 1, -1):
                    c = c + 1
                print(c)
        elif min_index == half or max_index == half:
            if min_index == half:
                if min_index < max_index:
                    c = 0
                    for i in range(min_index, -1, -1):
                        c = c + 1
                    print(c)
                else:
                    print(min_index + 1)
            elif max_index == half:
                if max_index < min_index:
                    c = 0
                    for i in range(max_index,-1,-1):
                        c = c + 1
                    print(c)
                else:
                    print(max_index+1)
        elif (min_index < half and max_index > half) or (max_index < half and min_index > half):
            if min_index < half and max_index > half:
                print((min_index+1)+(n-max_index))
            else:
                print((max_index + 1) + (n - min_index))


    else:
        half = n // 2
        min_value = min(li)
        max_value = max(li)
        min_index = li.index(min_value)
        max_index = li.index(max_value)




