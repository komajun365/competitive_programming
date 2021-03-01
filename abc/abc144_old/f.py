# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ts = []
for i in range(m):
    s,t = map(int,input().split())
    ts.append([t,s])

ts.sort()

deg = [0] * (n+1)
for tmp in ts:
    deg[tmp[1]] += 1

ans = n
for i in range(m+1):
    dp = [0] * (n+1)
    dp_p = [0] * (n+1)
    dp_p[1] = 1
    now = 0
    if(i!=m):
        deg[ts[i][1]] -= 1
    for j,tmp in enumerate(ts):
        if(i==j):
            continue
        t,s = tmp
        if(t > now):
            if(dp_p[now] != 0):
                dp[now] /= dp_p[now]
            now = t

        p = dp_p[s]/deg[s]
        dp[t] += (dp[s] + 1)  * p
        dp_p[t] += p


    if(dp_p[n] == 1):
        ans = min(ans, dp[n])

    if(i!=m):
        deg[ts[i][1]] += 1

print(ans)
