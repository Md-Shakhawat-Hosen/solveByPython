t = int(input())
for i in range(t):
    li = list(map(int,input().split()))
    m_value = max(li)
    a = li[0]
    b = li[1]
    c = li[2]
    d = li[3]

    if a + b + c == m_value:
        print(a,b,c)
    elif a + c + d == m_value:
        print(a,c,d)
    elif b + c + d == m_value:
        print(b,c,d)
    elif a + b + d == m_value:
        print(a,b,d)