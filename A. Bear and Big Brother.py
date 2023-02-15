limak, bob = map(int,input().split())
if limak == bob:
    print(1)
elif limak != bob:
    count = 0
    while limak <= bob:
        limak = limak * 3
        bob = 2 * bob
        count = count + 1
    print(count)


