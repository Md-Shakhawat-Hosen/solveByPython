t = int(input())
for i in range(t):
    h,m = map(int,input().split())
    cal_hourTo_Min = (24 - h) * 60
    print(cal_hourTo_Min-m)
