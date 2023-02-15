t = int(input())
for i in range(t):
    s = input()
    a_count = s.count('A')
    b_count = s.count('B')
    c_count = s.count('C')
    if a_count != 0 and b_count != 0 and c_count != 0:
        if a_count > b_count:
            print("NO")
        elif a_count == b_count:
            print("NO")
        else:
            b_count = b_count - a_count
            if b_count == c_count:
                print("YES")
            else:
                print("NO")

    elif a_count == 0 and b_count != 0 and c_count != 0:
        if b_count == c_count:
            print("YES")
        else:
            print("NO")
    elif a_count != 0 and b_count != 0 and c_count == 0:
        if a_count == b_count:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

