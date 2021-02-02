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

n,m,*ab = map(int,read().split())

neigh = [[0] * n for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    neigh[a][b] = 1
    neigh[b][a] = 1

links = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        if(neigh[i][j] == 0):
            links[i].append(j)

towns = []
done = [0] * n
for i in range(n):
    if(done[i] == 1):
        continue

    color = [-1] * n
    color[i] = 0
    stack = [i]
    num = [1,0]
    while(stack):
        j = stack.pop()
        done[j] = 1
        for k in links[j]:
            if(color[k] != -1):
                if color[k] == color[j]:
                    print(-1)
                    exit()
                continue
            color[k] = 1 - color[j]
            num[color[k]] += 1
            stack.append(k)
    
    towns.append(num[:])

m = len(towns)
dp = [0] * (n+1)
dp[0] = 1
for a,b in towns:
    next = [0] * (n+1)
    for i in range(n):
        if(dp[i] == 1):
            next[i+a] = 1
            next[i+b] = 1
    dp, next = next,dp

ans = n**2
for i in range(n):
    if(dp[i] == 1):
        j = n-i
        ans = min(ans, i*(i-1)//2 + j*(j-1)//2)
print(ans)


"""
補グラフを取って、二彩色できればクリークに分けられる。


"""