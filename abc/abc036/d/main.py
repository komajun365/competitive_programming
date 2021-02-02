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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*ab = map(int,read().split())
mod = 10**9 + 7

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

parent = [-1] * n
parent[0] = -2
stack = [0]
tp = [0]
while(stack):
    i = stack.pop()
    for j in links[i]:
        if(parent[j] != -1):
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

dp = [[0,0] for _ in range(n)]
for i in tp[::-1]:
    w,b = 1,1
    for j in links[i]:
        if(parent[i] == j):
            continue
        w *= dp[j][0] + dp[j][1]
        b *= dp[j][0]
        w %= mod
        b %= mod
    dp[i] = [w,b]

ans = sum(dp[0]) % mod
print(ans)


