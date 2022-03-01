# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n = int(input())
a = list(map(int, input().split()))

def calc_ave(x):
    tot = 0
    remains = []
    rem = []
    for ai in a:
        if ai >= x:
            tot += ai - x
            if len(rem) > 1:
                remains.append(rem)
            rem = []
        else:
            rem.append(ai)
    else:
        if len(rem) > 1:
            remains.append(rem)
    
    for rem in remains:
        l = len(rem)
        dp = [rem[0]-x,0]
        for i in range(1,l):
            dp[0],dp[1] = max(dp[0] + (rem[i]-x), dp[1] + (rem[i]-x)), dp[0]
            # print(dp)
        tot += max(dp)
    # print(tot,remains)
    
    return tot >= 0


# calc_ave(5)
# exit()

ok = 0
ng = 10**9 + 1
while ng-ok > 0.000001:
    mid = (ng+ok)/2
    if calc_ave(mid):
        ok = mid
    else:
        ng = mid
print(ok)

def calc_med(x):
    cnt_up = 0
    remains = []
    rem = []
    for ai in a:
        if ai >= x:
            cnt_up += 1
            if len(rem) > 1:
                remains.append(rem)
            rem = []
        else:
            rem.append(ai)
    else:
        if len(rem) > 1:
            remains.append(rem)
    
    cnt_down = 0
    for rem in remains:
        cnt_down += len(rem)//2
    
    return cnt_up - cnt_down >= 1

ok = 0
ng = 10**9 + 1
while ng-ok > 1:
    mid = (ng+ok)//2
    if calc_med(mid):
        ok = mid
    else:
        ng = mid
print(ok)


