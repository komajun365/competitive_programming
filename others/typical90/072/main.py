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
c = [input() for _ in range(h)]

def calc(end, now_x, now_y, bit):
    res = -100
    for dx,dy in zip([0,0,-1,1], [-1,1,0,0]):
        dx += now_x
        dy += now_y
        if 0 <= dx < h and 0 <= dy < w:
            num = dx*w + dy
            if num == end:
                res = max(res,1)
            elif (bit >> num) & 1 == 0:
                res = max(res, 1 + calc(end, dx, dy, bit + (1<<num)))
    return res

bit0 = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == '#':
            bit0 += 1 << (i*w+j)

res = -100
for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            res = max(res,calc(i*w+j, i, j, bit0))

if res < 3:
    res = -1
print(res)


