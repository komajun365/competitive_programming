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

n,s,*ab = map(int,read().split())

dp = [0] * (n+1)
dp[0] = 1
base = (1 << (s+1)) -1

for i in range(n):
    a,b = ab[i*2:i*2+2]
    dp[i+1] = ((dp[i] << a) | (dp[i] << b)) & base

if (dp[-1] >> s) & 1 == 0:
    print('Impossible')
    exit()

now = s
ans = [''] * n
for i in range(n-1,-1,-1):
    a,b = ab[i*2:i*2+2]
    if now >= a:
        if (dp[i] >> (now-a)) & 1:
            ans[i] = 'A'
            now -= a
        else:
            ans[i] = 'B'
            now -= b
    else:
        ans[i] = 'B'
        now -= b

print(''.join(ans))