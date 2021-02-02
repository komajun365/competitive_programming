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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# input
n,*p = map(int,read().split())

# make links
child = [[] for _ in range(n)]
for i,pi in enumerate(p,1):
    child[pi].append(i)

# tp sort
tp = []
stack = [0]
while(stack):
    i = stack.pop()
    tp.append(i)
    stack += child[i]


# dp [max, tot], ans
dp = [[0,1] for _ in range(n)]
ans = [0] * n
for i in tp[::-1]:
    for j in child[i]:
        dp[i][0] = max(dp[i][0], dp[j][1])
        dp[i][1] += dp[j][1]
    ans[i] = max(dp[i][0], n-dp[i][1])

print('\n'.join(map(str,ans)))
