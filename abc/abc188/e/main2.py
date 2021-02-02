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

n,m,*data = map(int,read().split())
a = data[:n]
xy = data[n:]

links = [[] for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    links[x].append(y)


inf = 10**10
ans = inf * -1
dp = [inf] * n
for i in range(n):
    ans = max(ans, a[i]-dp[i])
    dp[i] = min(dp[i],a[i])
    for j in links[i]:
        dp[j] = min(dp[j], dp[i])

print(ans)
