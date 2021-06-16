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

import itertools

h,w = map(int,input().split())
s = [input() for _ in range(h)]

body = [[],[]]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            body[(i+j)%2].append([i,j])

if len(body[0]) + len(body[1]) == h*w:
    ans = []
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                ans.append('{} {}'.format(i+1, j+1))
            else:
                ans.append('{} {}'.format(i+1, w-j))
    print(h*w)
    print('\n'.join(ans))
    exit()

if len(body[0]) < len(body[1]):
    body = body[::-1]

cnt = [len(body[0]), len(body[1])]
n = len(body[0]) + len(body[1])
cand = [[],[]]
for i in range(2):
    for p in itertools.permutations(range(cnt[i])):
        p = list(p)
        for j in range(len(p)-1):
            x0,y0 = body[i][p[j]]
            x1,y1 = body[i][p[j+1]]
            if abs(x0-x1) + abs(y0-y1) != 2:
                break
        else:
            cand[i].append(p[::])

def check(p0,p1):
    for i in range(n-1):
        x0,y0 = body[0][p0[(i+1)//2]]
        x1,y1 = body[1][p1[i//2]]
        if abs(x0-x1) + abs(y0-y1) != 1:
            return False
    return True

for p0 in cand[0]:
    for p1 in cand[1]:
        if check(p0,p1):
            print(n)
            for i in range(n):
                if i%2 == 0:
                    x,y = body[0][p0[i//2]]
                else:
                    x,y = body[1][p1[i//2]]
                print(x+1,y+1)
            exit()

# print(1/0)
# print(cand[0])
# print(cand[1])