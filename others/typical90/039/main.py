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

n,*ab = map(int,read().split())
links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

stack = [0]
parents = [-1] * n
parents[0] = 0
tp = []
while stack:
    i = stack.pop()
    for j in links[i]:
        if parents[j] != -1:
            continue
        parents[j] = i
        tp.append(j)
        stack.append(j)

ans = 0
dp = [1] * n
for i in tp[::-1]:
    ans += dp[i] * (n-dp[i])
    dp[parents[i]] += dp[i]
    # print(i,dp[i],ans)
print(ans)

# print(parents)
# print(tp)
# print(dp)