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

h,w = map(int,input().split())
s0 = [input() for _ in range(h)]
t0 = [input() for _ in range(h)]

s = [[0] * w for _ in range(h)]
t = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        s[i][j] = 1 * (s0[i][j] == '#')
        t[i][j] = 1 * (t0[i][j] == '#')


def rotate(x):
    hx = len(x)
    hw = len(x[0])
    res = [[0] * hx for _ in range(hw)]
    for i in range(hx):
        for j in range(hw):
            res[j][i] = x[hx-i-1][j]
    return res

for _ in range(4):
    while t:
        last = t[-1]
        if 1 in last:
            break
        t.pop()
    
    t = rotate(t)

def check(x,y,i0,j0):
    yh = len(y)
    yw = len(y[0])

    for i1 in range(i0, i0+yh):
        for j1 in range(j0, j0+yw):
            # print(i1,j1,yh,yw)
            if x[i1][j1] + y[i1-i0][j1-j0] == 2:
                return False
    return True

for _ in range(4):
    th = len(t)
    tw = len(t[0])

    for i0 in range(h-th+1):
        for j0 in range(w-tw+1):
            # print(_,i0,j0)
            if check(s,t,i0,j0):
                # print(_,i0,j0)
                print('Yes')
                exit()
    t = rotate(t)

print('No')

