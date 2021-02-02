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


n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
cost = [-1,2,5,5,4,5,6,3,7,6]

inf = -10 * n
dp = [[inf] * (n+1) for _ in range(m+1)]
dp[0][0] = 0

for i,ai in enumerate(a,1):
    ci = cost[ai]
    for j in range(n+1):
        if(j >= ci):
            dp[i][j] = max(dp[i-1][j], dp[i][j-ci] + 1)
        else:
            dp[i][j] = dp[i-1][j]

cnt = [0] * 10
j = n
for i in range(m,0,-1):
    if(dp[i][j] < 0):
        continue

    ai = a[i-1]
    ci = cost[ai]
    while(j>=ci):
        if(dp[i][j] - dp[i][j-ci] == 1):
            j -= ci
            cnt[ai] += 1
        else:
            break

ans = ''
for i in range(9,0,-1):
    ans += str(i) * cnt[i]

print(ans)
