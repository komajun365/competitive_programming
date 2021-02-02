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

ab = data[:2*m]
k = data[2*m]
c = data[2*m+1:]

if k==1:
    print(1)
    exit()

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

def bfs(root):
    d = [-1] * (n+1)
    d[root] = 0
    stack = [root]
    while(stack):
        next = []
        while(stack):
            i = stack.pop()
            for j in links[i]:
                if d[j] != -1:
                    continue
                d[j] = d[i] + 1
                next.append(j)
        stack,next = next,stack
    return d

ds = []
for ci in c:
    ds.append(bfs(ci))

for ci in c:
    if ds[0][ci] == -1:
        print(-1)
        exit()

inf = 10**9
dp = [[inf] * (2**k) for _ in range(k)]
for i in range(k):
    dp[i][1<<i] = 1

for j in range(2**k):
    for i in range(k):
        if dp[i][j] == inf:
            continue
        for l in range(k):
            if (j >> l) & 1:
                continue
            dp[l][j + (1<<l)] = min(dp[l][j + (1<<l)], 
                                    dp[i][j] + ds[i][ c[l] ])

ans = inf
for i in range(k):
    ans = min(ans, dp[i][-1])
print(ans)
# print(ds)
# print(dp)





