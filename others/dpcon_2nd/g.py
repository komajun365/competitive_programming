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

n,m,*xy = map(int,read().split())

links = [[] for _ in range(n+1)]
deg = [0] * (n+1)
it = iter(xy)
for x,y in zip(it,it):
    links[y].append(x)
    deg[x] += 1

dp = [0] * (n+1)

stack = []
for i in range(1,n+1):
    if(deg[i] == 0):
        stack.append(i)

while(stack):
    i = stack.pop()
    for j in links[i]:
        dp[j] = max(dp[j], dp[i]+1)
        deg[j] -= 1
        if(deg[j] == 0):
            stack.append(j)

print(max(dp))
