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

n,m,*st = map(int,read().split())

out = [[] for _ in range(n)]
it = iter(st)
for s,t in zip(it,it):
    s -= 1
    t -= 1
    out[s].append(t)

dp = [0] * n
cut = [-1] * n
for i in range(n-2,-1,-1):
    l = len(out[i])
    tot = 0
    worst = n-1
    for j in out[i]:
        tot += dp[j]
        if dp[worst] < dp[j]:
            worst = j
    dp[i] = tot/l + 1
    if l > 1:
        cut[i] = worst

ans = dp[0]
for i in range(n-1):
    l = len(out[i])
    if l == 1:
        continue
    tot = 0
    for j in out[i]:
        if j == cut[i]:
            continue
        tot += dp[j]
    dp[i] = tot/(l-1) + 1

    for k in range(i-1,-1,-1):
        l = len(out[k])
        tot = 0
        for j in out[k]:
            tot += dp[j]
        dp[k] = tot/l + 1
    
    ans = min(ans,dp[0])

print(ans)

