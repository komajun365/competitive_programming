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
read = sys.stdin.read

t,*data = read().split()
t = int(t)

def solve(r,c,f,s,start,goal):
    st = [[0] * c for _ in range(r)]
    go = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if start[i][j] == 'G':
                st[i][j] = 1
            if goal[i][j] == 'G':
                go[i][j] = 1
    
    res = 0
    for i in range(r):
        for j in range(c):
            if i < r-1:
                if st[i][j] != go[i][j] and st[i+1][j] != go[i+1][j] and st[i][j] != st[i+1][j]:
                    st[i][j] = 1 - st[i][j]
                    st[i+1][j] = 1 - st[i+1][j]
                    res += 1
            if j < c-1:
                if st[i][j] != go[i][j] and st[i][j+1] != go[i][j+1] and st[i][j] != st[i][j+1]:
                    st[i][j] = 1 - st[i][j]
                    st[i][j+1] = 1 - st[i][j+1]
                    res += 1
    for i in range(r):
        for j in range(c):
            if st[i][j] != go[i][j]:
                res += 1
    # print(start)
    # print(go)

    return res

ans = [''] * t
idx = 0
for i in range(t):
    r,c,f,s = map(int, data[idx:idx+4])
    start = data[idx+4:idx+4+r]
    goal = data[idx+4+r:idx+4+r+r]
    idx += 4 + r*2
    res = solve(r,c,f,s,start,goal)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))

