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
read = sys.stdin.read

h,w,*a = read().split()
h,w = int(h),int(w)

inf = -1 * 10**9
for i in range(h-1,-1,-1):
    if i == h-1:
        dp = [inf] * w
        dp[-1] = 0
        for j in range(w-2,-1,-1):
            add = 1 if a[i][j+1] == '+' else -1
            dp[j] = max(dp[j], -1 * dp[j+1] + add)
    else:
        dp2 = [inf] * w
        for j in range(w-1,-1,-1):
            if j != w-1:
                add = 1 if a[i][j+1] == '+' else -1
                dp2[j] = max(dp2[j], -1 * dp2[j+1] + add)
            add = 1 if a[i+1][j] == '+' else -1
            dp2[j] = max(dp2[j], -1 * dp[j] + add)
        dp,dp2 = dp2,dp

if dp[0] > 0:
    print('Takahashi')
elif dp[0] < 0:
    print('Aoki')
else:
    print('Draw')
