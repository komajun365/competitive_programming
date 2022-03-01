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

from collections import deque

h,w = map(int,input().split())
s = [input() for _ in range(h)]

s2 = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s2[i][j] = 1

cost = [[-1] * w for _ in range(h)]
cost[0][0] = 0
done = [[0] * w for _ in range(h)]
dq = deque()
dq.append(0)
while dq:
    x = dq.popleft()
    i = x//w
    j = x%w
    if done[i][j] == 1:
        continue
    done[i][j] = 1
    for di,dj in zip([1,-1,0,0], [0,0,1,-1]):
        di += i
        dj += j
        if di < 0 or di >= h or dj < 0 or dj>= w:
            continue
        # print(i,j,di,dj)
        if 0 <= cost[di][dj] <= cost[i][j]:
            continue
        if s2[di][dj] == 1:
            cost[di][dj] = cost[i][j]
            dq.appendleft(di*w+dj)
        elif cost[di][dj] == cost[i][j] + 1:
            continue
        else:
            cost[di][dj] = cost[i][j] + 1
            dq.append(di*w+dj)
    for di,dj in zip([-2,-2,-2,-1,-1,-1,-1,0,0,1,1,1,1,2,2,2],
                     [-1,0,1,-2,-1,1,2,-2,2,-2,-1,1,2,-1,0,1]):
        di += i
        dj += j
        if di < 0 or di >= h or dj < 0 or dj>= w:
            continue
        if cost[di][dj] != -1 :
            continue
        cost[di][dj] = cost[i][j] + 1
        dq.append(di*w+dj)
    # print(dq)

print(cost[-1][-1])

# for i in cost:
#     print(i)


