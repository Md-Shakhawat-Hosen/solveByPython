k,n,w = map(int,input().split())
result = int(k*(w*(w+1)/2))
if n >= result:
    print(0)
else:
    print(abs(result-n))
