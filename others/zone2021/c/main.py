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

import sys
read = sys.stdin.buffer.read

n,*abcde = map(int,read().split())

def calc(x):
    dp = [[0] * 32 for _ in range(4)]
    dp[0][0] = 1
    for i in range(n):
        status = abcde[i*5:i*5+5]
        st = 0
        for j in status:
            st = st*2 + 1 * (j>=x)
        
        for j in range(2,-1,-1):
            for k in range(32):
                if dp[j][k] == 0:
                    continue
                dp[j+1][k | st] = 1
    
    return dp[-1][-1] == 1

ok = 0
ng = 10**9+1
while ng-ok > 1:
    mid = (ng+ok)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)


