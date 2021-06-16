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
from collections import deque

n,m,*abc = read().split()
n = int(n)
m = int(m)

links = [[] for _ in range(n)]
for i in range(n):
    links[i] = [[] for _ in range(26)]

dp = [[-1] * n for _ in range(n)]
dq = deque()
for i in range(n):
    dq.append(i*n+i)
    dp[i][i] = 0

base = ord('a')
it = iter(abc)
for a,b,c in zip(it,it,it):
    a = int(a) - 1
    b = int(b) - 1
    if a>b:
        a,b = b,a
    c = ord(c) - base
    links[a][c].append(b)
    links[b][c].append(a)
    if dp[a][b] == -1:
        dp[a][b] = 1
        dq.append(a*n+b)

while dq:
    i = dq.popleft()
    a = i // n
    b = i % n
    for ch in range(26):
        la = links[a][ch]
        lb = links[b][ch]
        for x in la:
            for y in lb:
                l = min(x,y)
                r = max(x,y)
                if dp[l][r] != -1:
                    continue
                dp[l][r] = dp[a][b] + 2
                dq.append(l*n+r)
                if l==0 and r == n-1:
                    print(dp[l][r])
                    # print(dp)
                    exit()

print(dp[0][n-1])

