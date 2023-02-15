t = int(input())
for i in range(t):
    apartment_number,floor = map(int,input().split())
    result = apartment_number + floor
    if apartment_number == 1 or apartment_number == 2:
        print(1)
    else:
        d = 2 + floor
        s = 2
        while d < apartment_number:
            s = s + 1
            d = d + floor
        print(s)