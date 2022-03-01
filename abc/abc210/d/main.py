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

h,w,c,*data = map(int,read().split())

a = []
cost = []
for i in range(h):
    a.append(data[i*w:(i+1)*w])
    cost.append(data[i*w:(i+1)*w])

ans = 10**15
for i in range(h):
    now = a[i][0]
    for j in range(1,w):
        now += c
        ans = min(ans, now + a[i][j])
        cost[i][j] = min(cost[i][j], now)
        now = min(now, a[i][j])
    now = a[i][-1]
    for j in range(w-2,-1,-1):
        now += c
        ans = min(ans, now + a[i][j])
        cost[i][j] = min(cost[i][j], now)
        now = min(now, a[i][j])

for j in range(w):
    now = cost[0][j]
    for i in range(1,h):
        now += c
        ans = min(ans, now + cost[i][j])
        now = min(now, cost[i][j])
    now = cost[-1][j]
    for i in range(h-2,-1,-1):
        now += c
        ans = min(ans, now + cost[i][j])
        now = min(now, cost[i][j])
print(ans)
# print(cost)