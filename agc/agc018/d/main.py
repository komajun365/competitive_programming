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

n,*abc = map(int,read().split())
links = [[] for _ in range(n)]

it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    links[a].append([b,c])
    links[b].append([a,c])

tp = [0]
par = [-1] * n
par[0] = -2
stack = [0]
while(stack):
    i = stack.pop()
    for j,_ in links[i]:
        if par[j] != -1:
            continue
        par[j] = i
        stack.append(j)
        tp.append(j)

dp = [1] * n
for i in tp[::-1]:
    if i == 0:
        break
    dp[par[i]] += dp[i]

x = 0
while(True):
    next = -1
    for j,_ in links[x]:
        if j == par[x]:
            continue
        if dp[j] >= (n+1)//2:
            next = j
            break
    
    if next == -1:
        break
    x = next


def calc(x):
    stack = [x]
    d = [-1] * n
    d[x] = 0
    while(stack):
        i = stack.pop()
        for j,c in links[i]:
            if d[j] != -1:
                continue
            d[j] = d[i] + c
            stack.append(j)

    ans = sum(d) * 2
    max_size = 0
    max_j = -1
    for j,_ in links[x]:
        if j == par[x]:
            size = n - dp[x]
        else:
            size = dp[j]
        if max_size < size:
            max_size = size
            max_j = j

    if max_size * 2 == n:
        ans -= d[max_j]
    else:
        min_c = 10**8
        for j,c in links[x]:
            min_c = min(min_c, c)
        ans -= min_c
    
    return ans

ans = calc(x)
if dp[x] * 2 == n:
    y = par[x]
    ans = max(ans, calc(y))
print(ans)


