t = int(input())
while t >= 0:
    A_x1, A_y1 = map(int, input().split())
    B_x1, B_y1 = map(int, input().split())
    F_x1, F_y1 = map(int, input().split())

    if A_x1 != B_x1 != F_x1 and A_y1 != B_y1 != F_y1:
        r = abs(A_x1 - B_x1) + abs(B_y1 - A_y1)
        print(r)
    if A_x1 == B_x1 == F_x1:
        if (B_y1 < F_y1 < A_y1 or A_y1 < F_y1 < B_y1):
            r = abs(A_y1 - B_y1) + 2
            print(r)
        else:
            r = abs(A_y1 - B_y1)
            print(r)
    if A_y1 == B_y1 == F_y1:
        if A_x1 < F_x1 < B_x1 or B_x1 < F_x1 < A_x1:
            r = abs(A_x1 - B_x1) + 2
            print(r)
        else:
            r = abs(A_x1 - B_x1)
            print(r)
    else:
        r = abs(A_x1 - B_x1)
        print(r)
    t = t - 1


