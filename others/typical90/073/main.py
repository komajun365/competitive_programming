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
read = sys.stdin.read

n,*data = read().split()
n = int(n)
c = data[:n]
ab = [int(x)-1 for x in data[n:]]
mod = 10**9 + 7

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

stack = [0]
parent = [-1] * n
parent[0] = -2
tp = [0]
while stack:
    i = stack.pop()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

tp = tp[::-1]
dp = [[1,1,0] for _ in range(n)] #only a or b,not_NG, ab
for i in tp:
    dp[i][2] = dp[i][1] - dp[i][0]
    dp[i][2] %= mod
    if i == 0:
        continue
    p = parent[i]
    if c[i] == c[p]:
        dp[p][0] *= dp[i][1]
        dp[p][0] %= mod
        dp[p][1] *= dp[i][0] + dp[i][2] * 2
        dp[p][1] %= mod
    else:
        dp[p][0] *= dp[i][2]
        dp[p][0] %= mod
        dp[p][1] *= dp[i][0] + dp[i][2] * 2
        dp[p][1] %= mod

print(dp[0][2])

# print(tp)
# for i in dp:
#     print(i)

# print(n)
# print(c)
# print(ab)