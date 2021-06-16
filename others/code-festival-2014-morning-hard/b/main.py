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

n,*pl = map(int,read().split())
mod = 10**9 + 7

p0,l0 = pl[:2]
dp = [1] * (l0*2+1)
it = iter(pl[2:])
for p,l in zip(it,it):
    tot = 0
    dp2 = [0] * (l*2+1)
    j = 0
    for i in range(l*2+1):
        while j < l0*2+1:
            if p-l+i > p0-l0+j:
                tot += dp[j]
                tot %= mod
                j += 1
            else:
                break
        dp2[i] = tot
    dp,dp2 = dp2,dp
    p0,l0 = p,l

ans = sum(dp) % mod
print(ans)

