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

n,*xc = map(int,read().split())

inf = 10**15
lr = [[inf,-1*inf] for _ in range(n)]
it = iter(xc)
for x,c in zip(it,it):
    c -= 1
    lr[c][0] = min(lr[c][0], x)
    lr[c][1] = max(lr[c][1], x)
lr.append([0,0])

dp = [0,0]
l,r = 0,0
for i in range(n+1):
    if lr[i][0] == inf:
        continue
    li,ri = lr[i]
    dp2 = [inf,inf]
    dp2[0] = min(dp2[0], dp[0]+ abs(l-ri) + ri-li)
    dp2[0] = min(dp2[0], dp[1]+ abs(r-ri) + ri-li)
    dp2[1] = min(dp2[1], dp[0]+ abs(l-li) + ri-li)
    dp2[1] = min(dp2[1], dp[1]+ abs(r-li) + ri-li)
    l,r = lr[i]
    dp,dp2 = dp2,dp
    # print(i,dp,l,r)

print(min(dp))
# print(lr[:5])