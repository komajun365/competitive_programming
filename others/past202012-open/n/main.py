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

n,q,*data = map(int,read().split())
lr0 = data[:2*(n-1)]
it = iter(lr0)
lr = [[l,r] for l,r in zip(it,it)]
ab = data[2*(n-1):]

n2 = 20
inf = 10**9

def make_dbl(lr):
    dbl_up = [[x[1]] for x in lr]
    dbl_up.append([inf])
    for j in range(n2-1):
        for i in range(n):
            go = min(n-1, i + (1<<j))
            dbl_up[i].append(min(dbl_up[i][j], dbl_up[go][j]))
    
    dbl_down = [[x[0]] for x in lr]
    dbl_down.append([0])
    for j in range(n2-1):
        for i in range(n):
            go = min(n-1, i + (1<<j))
            dbl_down[i].append(max(dbl_down[i][j], dbl_down[go][j]))
    
    return [dbl_up, dbl_down]

east = make_dbl(lr)
west = make_dbl(lr[::-1])
west[0] = west[0][::-1]
west[1] = west[1][::-1]

# print(west[0])
# print(west[1])

def calc(ai,bi):
    bi -= 1

    left = bi
    right = bi
    if bi != n-1:
        now = bi
        for i in range(19,-1,-1):
            if east[0][now][i] >= ai:
                now = min(n-1, now + (1<<i))
        right = now
        now = bi
        for i in range(19,-1,-1):
            if east[1][now][i] <= ai:
                now = min(n-1, now + (1<<i))
        right = min(right,now)
    
    if bi != 0:
        now = bi
        for i in range(19,-1,-1):
            if west[0][now][i] >= ai:
                now = max(0, now - (1<<i))
        left = now
        now = bi
        for i in range(19,-1,-1):
            if west[1][now][i] <= ai:
                now = max(0, now - (1<<i))
        left = max(left,now)
    
    return right-left + 1

ans = []
it = iter(ab)
for a,b in zip(it,it):
    ans.append(calc(a,b))
print('\n'.join(map(str,ans)))



