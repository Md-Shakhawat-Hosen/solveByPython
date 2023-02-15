n,k = map(int,input().split())
s = input()
first = s.index('G')
last = s.index('T')
if first < last:
    if s[first+k] == 'T':
        print("YES")
    elif s[first+k] == '#':
        print("NO")
    elif first+k > last:
        print("NO")
    elif s[first+k] == '.':
        while first < last:
            if s[first + k] == 'T':
                print("YES")
                break
            elif s[first + k] == '.':
                first = first + k
                continue
            elif s[first + k] == '#':
                print("NO")
                break
            else:
                print("NO")
                break
        first = first + k
else:
    if s[first-k] == 'T':
        print("YES")
    elif s[first-k] == '#':
        print("NO")
    elif s[first-k] == '.':
        while first >= last:
            if s[first-k] == 'T':
                print("YES")
                break
            elif s[first-k] == '.':
                first = first - k
                continue
            elif s[first-k] == '#':
                print("NO")
                break
            else:
                print("NO")
                break
        first = first - k



