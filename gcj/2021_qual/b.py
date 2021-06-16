# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.read

t,*data = read().split()
t = int(t)

def calc(x,y,s):
    n = len(s)
    inf = 10**9
    dp = [0,0]
    if s[0] == 'C':
        dp[1] = inf
    elif s[0] == 'J':
        dp[0] = inf
    
    for i in range(1,n):
        dp2 = [0,0]
        if s[i] == 'C':
            dp2[0] = min(dp[0], dp[1] + y)
            dp2[1] = inf
        elif s[i] == 'J':
            dp2[1] = min(dp[1], dp[0] + x)
            dp2[0] = inf
        else:
            dp2[0] = min(dp[0], dp[1] + y)
            dp2[1] = min(dp[1], dp[0] + x)
        dp,dp2 = dp2,dp
    
    return min(dp)

ans = [''] * t
idx = 0
for i in range(t):
    x,y,s = data[idx:idx+3]
    idx += 3
    x = int(x)
    y = int(y)
    res = calc(x,y,s)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))


